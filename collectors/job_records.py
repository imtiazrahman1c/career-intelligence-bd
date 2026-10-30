"""Minimal display metadata only; no job descriptions or employer ATS links."""
from datetime import datetime, timezone
from urllib.parse import urlsplit
from html import unescape
from analysis.skills import bangladesh_location_signal


def normalize_jobs(source, jobs, now=None):
    now = now or datetime.now(timezone.utc)
    output, seen = [], set()
    for job in jobs:
        identity = job.get('guid' if source == 'himalayas' else 'id')
        title = job.get('title' if source == 'himalayas' else 'jobTitle')
        company = job.get('companyName')
        url = job.get('applicationLink' if source == 'himalayas' else 'url')
        if identity is None or not str(identity).strip() or str(identity) in seen:
            continue
        if not all(isinstance(v, str) and v.strip() for v in (title, company, url)):
            continue
        try:
            parsed = urlsplit(url)
            if parsed.scheme != 'https' or parsed.hostname != ('himalayas.app' if source == 'himalayas' else 'jobicy.com') or parsed.username or parsed.password or parsed.port not in (None,443):
                continue
            expiry = job.get('expiryDate')
            if expiry:
                end = datetime.fromtimestamp(float(expiry), timezone.utc)
                if end <= now:
                    continue
        except (ValueError, TypeError, OverflowError, OSError):
            continue
        location = job.get('locationRestrictions' if source == 'himalayas' else 'jobGeo')
        display_location = ', '.join(v for v in location if isinstance(v,str)) if isinstance(location,list) else location if isinstance(location,str) else ''
        seen.add(str(identity))
        output.append({'source':source, 'source_id':str(identity),
                       'title':unescape(title.strip())[:240], 'company':unescape(company.strip())[:160],
                       'location':display_location[:300] or 'Not specified',
                       'location_signal':bangladesh_location_signal(location),
                       'application_url':url, 'availability':'sampled_not_rechecked'})
    return output
