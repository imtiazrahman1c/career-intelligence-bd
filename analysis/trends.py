"""Conservative comparison gate. Input counts are observations, never total demand."""
from datetime import date


def compare_periods(previous, current):
    required = ('source_set', 'geography', 'method_version', 'coverage_version', 'metric', 'unit')
    if any(not previous.get(k) or not current.get(k) or previous[k] != current[k] for k in required):
        return {'state': 'unavailable', 'reason': 'incompatible_metadata'}
    if previous['metric'] != 'unique_postings' or previous['unit'] != 'count':
        return {'state': 'unavailable', 'reason': 'unsupported_metric'}
    try:
        a, b, c, d = [date.fromisoformat(x) for x in (previous['start'], previous['end'], current['start'], current['end'])]
        old, new = previous['value'], current['value']
    except (KeyError, TypeError, ValueError):
        return {'state': 'unavailable', 'reason': 'invalid_period'}
    if a > b or c > d or b >= c or (b-a).days != (d-c).days:
        return {'state': 'unavailable', 'reason': 'incompatible_periods'}
    if any(type(n) is not int or n < 0 for n in (old, new)):
        return {'state': 'unavailable', 'reason': 'invalid_counts'}
    if any(x.get('complete') is not True or x.get('deduplicated') is not True for x in (previous, current)):
        return {'state': 'unavailable', 'reason': 'incomplete_or_not_deduplicated'}
    return {'state': 'comparable', 'absolute_change': new-old,
            'percent_change': (new-old)/old*100 if old else None,
            'scope': 'observed_unique_postings_only'}
