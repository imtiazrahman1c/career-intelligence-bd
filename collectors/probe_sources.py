"""Bounded, read-only source feasibility probe; never writes raw job content."""
import argparse
import json
from datetime import datetime, timezone
from urllib.request import Request, urlopen

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


def summarize(source, payload):
    """Presence is not correctness, suitability, eligibility or market coverage."""
    if not isinstance(payload, dict) or payload.get('success') is False:
        raise ValueError('Source returned invalid or unsuccessful payload')
    jobs = payload.get('jobs')
    if not isinstance(jobs, list) or any(not isinstance(j, dict) for j in jobs):
        raise ValueError('Expected a jobs array of objects')
    fields = FIELDS[source]
    ids = [str(j[fields['id']]) for j in jobs if j.get(fields['id']) is not None]
    return {
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', choices=[*SOURCES, 'all'], default='all')
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
                result = summarize(source, json.loads(body))
                result['http_status'] = response.status
            results.append(result)
        except Exception as error:
            results.append({'source': source, 'error_type': type(error).__name__, 'ok': False})
    print(json.dumps({'checked_at': datetime.now(timezone.utc).isoformat(),
                      'results': results}, ensure_ascii=False, indent=2))
    return int(any('error_type' in r for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
