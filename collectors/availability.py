"""Bounded Jobicy status check. A failed check never implies active or closed."""
import json
from urllib.request import Request, urlopen
from urllib.parse import urlsplit
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor


def fetch_status(ids):
    request=Request('https://jobicy.com/api/jobs/status?ids='+','.join(ids),
                    headers={'Accept':'application/json','User-Agent':'CareerIntelligenceBD/0.1'})
    with urlopen(request,timeout=15) as response:
        body=response.read(100001)
        if len(body)>100000:
            raise ValueError('Oversize status response')
        return json.loads(body)


def check_jobicy(listings, fetcher=fetch_status):
    if len(listings)>20:
        raise ValueError('Status sample limit exceeded')
    ids=[j['source_id'] for j in listings if j['source']=='jobicy' and j['source_id'].isdigit()]
    statuses={}
    try:
        payload=fetcher(ids) if ids else {}
        if payload.get('success') is True and payload.get('statusCode')==200 and isinstance(payload.get('jobs'),list):
            duplicates=set()
            for row in payload['jobs']:
                if not isinstance(row,dict):
                    continue
                identity=str(row.get('id'))
                if identity in statuses:
                    duplicates.add(identity)
                if identity in ids:
                    statuses[identity]=row.get('status')
            for identity in duplicates:
                statuses[identity]='unknown'
    except Exception:
        # Deliberately retain no provider body/error details.
        statuses={}
    output=[]
    for job in listings:
        status=statuses.get(job['source_id'])
        if status=='closed':
            continue
        output.append({**job,'availability':'active_at_collection' if status=='active' else 'unknown'})
    return output


def fetch_himalayas_status(identity):
    url=urlsplit(identity)
    if url.scheme!='https' or url.hostname!='himalayas.app' or url.username or url.password or url.query or url.fragment or not url.path.startswith('/companies/') or '/jobs/' not in url.path or url.port:
        return 'unknown'
    request=Request('https://himalayas.app/jobs/api'+url.path,
                    headers={'Accept':'application/json','User-Agent':'CareerIntelligenceBD/0.1'})
    try:
        with urlopen(request,timeout=8) as response:
            body=response.read(500001)
            if len(body)>500000:
                return 'unknown'
            payload=json.loads(body)
            job=payload.get('job')
            return 'active' if isinstance(job,dict) and job.get('guid')==identity else 'unknown'
    except HTTPError as error:
        return 'closed' if error.code==410 else 'unknown'


def check_himalayas(listings, fetcher=fetch_himalayas_status):
    if len(listings)>20:
        raise ValueError('Status sample limit exceeded')
    def check(job):
        try:
            status=fetcher(job['source_id']) if job['source']=='himalayas' else 'unknown'
        except Exception:
            status='unknown'
        return None if status=='closed' else {**job,'availability':'active_at_collection' if status=='active' else 'unknown'}
    # At most 20 calls, four in flight; no retries or page scraping.
    with ThreadPoolExecutor(max_workers=4) as executor:
        return [job for job in executor.map(check,listings) if job is not None]
