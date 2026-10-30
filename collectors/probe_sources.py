"""Bounded, read-only source feasibility probe; never writes raw job content."""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analysis.skills import VERSION, SKILLS, skill_mentions, bangladesh_location_signal
from collectors.job_records import normalize_jobs
from collectors.availability import check_jobicy

SOURCES = {
    'himalayas': 'https://himalayas.app/jobs/api?limit=20',
    'jobicy': 'https://jobicy.com/api/jobs?count=20',
}
FIELDS = {
    'himalayas': {'id': 'guid', 'title': 'title', 'company': 'companyName',
                 'description': 'description', 'application': 'applicationLink',
                 'published': 'pubDate', 'countries': 'locationRestrictions'},
    'jobicy': {'id': 'id', 'title': 'jobTitle', 'company': 'companyName',
               'description': 'jobDescription', 'application': 'url',
               'published': 'pubDate', 'countries': 'jobGeo'},
}


def summarize(source, payload, analyze=False):
    """Presence is not correctness, suitability, eligibility or market coverage."""
    if not isinstance(payload, dict) or payload.get('success') is False:
        raise ValueError('Source returned invalid or unsuccessful payload')
    jobs = payload.get('jobs')
    if not isinstance(jobs, list) or any(not isinstance(j, dict) for j in jobs):
        raise ValueError('Expected a jobs array of objects')
    fields = FIELDS[source]
    ids = [str(j[fields['id']]) for j in jobs if j.get(fields['id']) is not None]
    result = {
        'source': source,
        'sample_records': len(jobs),
        'unique_source_ids': len(set(ids)),
        'duplicate_ids': len(ids) - len(set(ids)),
        'fields_present_in_sample': sorted(set().union(*(j.keys() for j in jobs))) if jobs else [],
        'nonempty_field_counts': {
            name: sum(j.get(field) is not None and j.get(field) != '' and j.get(field) != [] for j in jobs)
            for name, field in fields.items()
        },
        'has_next_cursor': bool(payload.get('nextCursor')),
        'reported_total_not_collected': payload.get('totalCount'),
        'limitations': ['First page only; not a representative sample',
                        'Eligibility and skill extraction not validated',
                        'Historical retention rights not established by this probe'],
    }
    if analyze:
        # Count each source ID once; records without IDs cannot enter analysis.
        seen = set()
        counts = dict.fromkeys(SKILLS, 0)
        locations = {}
        analyzed = 0
        for job in jobs:
            identity = job.get(fields['id'])
            if identity is None or str(identity) in seen:
                continue
            seen.add(str(identity))
            analyzed += 1
            for skill in skill_mentions(job.get(fields['description'])):
                counts[skill] += 1
            signal = bangladesh_location_signal(job.get(fields['countries']))
            locations[signal] = locations.get(signal, 0) + 1
        result['analysis'] = {
            'method_version': VERSION, 'unique_records_analyzed': analyzed,
            'skill_mention_counts': counts, 'location_signal_counts': locations,
            'limitations': ['Mentions include optional and negative statements; not requirements',
                            'Editorial vocabulary; not an official occupational taxonomy',
                            'Location signals are not verified application eligibility',
                            'No cross-source deduplication; not market demand'],
        }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', choices=[*SOURCES, 'all'], default='all')
    parser.add_argument('--analyze', action='store_true', help='Emit aggregate experimental mention counts only')
    parser.add_argument('--include-listings', action='store_true', help='Include minimal attributed display metadata; no descriptions')
    parser.add_argument('--check-availability', action='store_true', help='Check Jobicy batch status when including listings')
    args = parser.parse_args()
    results = []
    for source in SOURCES if args.source == 'all' else [args.source]:
        try:
            request = Request(SOURCES[source], headers={
                'Accept': 'application/json',
                'User-Agent': 'CareerIntelligenceBD/0.1 (bounded feasibility research)',
            })
            with urlopen(request, timeout=25) as response:
                body = response.read(8_000_001)
                if len(body) > 8_000_000:
                    raise ValueError('Response exceeds probe size limit')
                payload = json.loads(body)
                result = summarize(source, payload, analyze=args.analyze)
                if args.include_listings:
                    result['listings'] = normalize_jobs(source, payload['jobs'])
                    if args.check_availability and source == 'jobicy':
                        result['listings'] = check_jobicy(result['listings'])
                result['http_status'] = response.status
            results.append(result)
        except Exception as error:
            results.append({'source': source, 'error_type': type(error).__name__, 'ok': False})
    print(json.dumps({'checked_at': datetime.now(timezone.utc).isoformat(),
                      'results': results}, ensure_ascii=False, indent=2))
    return int(any('error_type' in r for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
