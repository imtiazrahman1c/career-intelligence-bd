"""Atomically replace an aggregate snapshot only after both probes succeed.

No database credentials, publication or raw job retention. Run from repo root:
python -m collectors.refresh_snapshot --output /path/to/snapshot.json
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from collectors.probe_sources import SOURCES
from analysis.skills import SKILLS, VERSION


def integer(value):
    return type(value) is int and value >= 0


def validate_listings(source, listings, maximum):
    if not isinstance(listings, list) or len(listings) > maximum:
        raise ValueError('Invalid listing count')
    expected = {'source','source_id','title','company','location','location_signal','application_url','availability'}
    seen = set()
    for job in listings:
        if not isinstance(job, dict) or set(job) != expected:
            raise ValueError('Only minimal display metadata may be retained')
        if any(not isinstance(v,str) or not v.strip() for v in job.values()):
            raise ValueError('Invalid listing fields')
        if job['source'] != source or job['source_id'] in seen:
            raise ValueError('Mismatched source or duplicate listing')
        seen.add(job['source_id'])
        if job['availability'] != 'sampled_not_rechecked' or job['location_signal'] not in {'unknown','bangladesh_listed_review_required','worldwide_listed_review_required'}:
            raise ValueError('Unverified listing status')
        url = urlsplit(job['application_url'])
        if url.scheme != 'https' or url.hostname != {'himalayas':'himalayas.app','jobicy':'jobicy.com'}[source] or url.username or url.password or url.port not in (None,443):
            raise ValueError('Invalid source link')


def validate(snapshot):
    if not isinstance(snapshot, dict):
        raise ValueError('Invalid snapshot')
    stamp = datetime.fromisoformat(snapshot.get('checked_at', '').replace('Z', '+00:00'))
    if stamp.tzinfo is None or abs((datetime.now(timezone.utc)-stamp).total_seconds()) > 3600:
        raise ValueError('Collection timestamp outside one-hour validation window')
    rows = snapshot.get('results')
    if not isinstance(rows, list) or len(rows) != len(SOURCES):
        raise ValueError('Expected all configured sources')
    if {r.get('source') for r in rows if isinstance(r, dict)} != set(SOURCES):
        raise ValueError('Missing or duplicated source')
    for row in rows:
        count = row.get('sample_records')
        if row.get('http_status') != 200 or row.get('error_type') or not integer(count) or count > 20:
            raise ValueError('Probe failed or exceeded sample bound')
        analysis = row.get('analysis', {})
        n = analysis.get('unique_records_analyzed')
        skills = analysis.get('skill_mention_counts', {})
        locations = analysis.get('location_signal_counts', {})
        if analysis.get('method_version') != VERSION or not integer(n) or n > count:
            raise ValueError('Invalid analysis method or denominator')
        if set(skills) != set(SKILLS) or any(not integer(v) or v > n for v in skills.values()):
            raise ValueError('Invalid skill aggregates')
        if not isinstance(locations, dict) or not set(locations) <= {'unknown', 'bangladesh_listed_review_required', 'worldwide_listed_review_required'} or any(not integer(v) for v in locations.values()) or sum(locations.values()) != n:
            raise ValueError('Invalid location aggregates')
        if 'listings' in row:
            validate_listings(row['source'], row['listings'], count)
    return snapshot


def save_snapshot(snapshot, destination):
    validate(snapshot)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=destination.parent, delete=False) as handle:
            temporary = handle.name
            json.dump(snapshot, handle, ensure_ascii=False, indent=2)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--include-listings', action='store_true', help='Include validated minimal display metadata')
    args = parser.parse_args()
    try:
        command = [sys.executable, '-m', 'collectors.probe_sources', '--analyze']
        if args.include_listings:
            command.append('--include-listings')
        result = subprocess.run(command,
                                capture_output=True, text=True, timeout=65, check=True)
        snapshot = json.loads(result.stdout)
        save_snapshot(snapshot, args.output)
    except Exception as error:
        # Do not print provider body, credentials or raw content on failure.
        print('Refresh failed; previous snapshot preserved: '+type(error).__name__, file=sys.stderr)
        return 1
    print('Validated aggregate snapshot saved; database publication not performed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
