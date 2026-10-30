"""Server-only publisher for this project's validated snapshot table."""
import argparse
import json
import os
import sys
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen
from collectors.refresh_snapshot import validate

PROJECT_URL='https://oqqyqqkrgsjoxfmwbqur.supabase.co'


def public_payload(snapshot):
    validate(snapshot)
    # Explicit projection: accidental fields from upstream cannot be published.
    rows=[]
    for row in snapshot['results']:
        safe={key:row[key] for key in ('source','sample_records','unique_source_ids','duplicate_ids','http_status')}
        fields=row.get('nonempty_field_counts',{})
        safe['nonempty_field_counts']={key:fields.get(key,0) for key in ('id','title','company','description','application','published','countries')}
        if any(type(value) is not int or value<0 or value>row['sample_records'] for value in safe['nonempty_field_counts'].values()):
            raise ValueError('Invalid completeness counts')
        a=row['analysis']
        safe['analysis']={key:a[key] for key in ('method_version','unique_records_analyzed','skill_mention_counts','location_signal_counts')}
        if 'listings' in row:
            safe['listings']=row['listings']
        rows.append(safe)
    return {'checked_at':snapshot['checked_at'],'results':rows}


def publish(snapshot, secret, opener=urlopen):
    if not isinstance(secret,str) or not secret.startswith('sb_secret_'):
        raise ValueError('Server secret key is required')
    payload=public_payload(snapshot)
    endpoint=PROJECT_URL+'/rest/v1/dashboard_snapshots'
    headers={'apikey':secret,'Content-Type':'application/json',
             'Prefer':'resolution=ignore-duplicates,return=minimal'}
    body=json.dumps({'checked_at':payload['checked_at'],'payload':payload,'is_published':True}).encode()
    with opener(Request(endpoint+'?on_conflict=checked_at',data=body,headers=headers,method='POST'),timeout=20) as response:
        if response.status not in (200,201,204):
            raise ValueError('Publication failed')
    # Confirm the exact timestamp exists and is published. No destructive replacement.
    query='?select=checked_at,is_published&checked_at=eq.'+quote(payload['checked_at'],safe='')+'&limit=1'
    with opener(Request(endpoint+query,headers={'apikey':secret}),timeout=20) as response:
        result=json.loads(response.read(10001))
        if not isinstance(result,list) or len(result)!=1 or result[0].get('is_published') is not True:
            raise ValueError('Publication verification failed')
    return payload['checked_at']


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',required=True)
    args=parser.parse_args()
    try:
        publish(json.loads(Path(args.input).read_text()),os.environ.get('CAREER_SUPABASE_SECRET_KEY'))
    except Exception as error:
        print('Snapshot publication failed: '+type(error).__name__,file=sys.stderr)
        return 1
    print('Validated snapshot published and read-back verified.')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
