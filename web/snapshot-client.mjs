import {snapshotHealth} from './model.mjs';

const sources=new Set(['himalayas','jobicy']);
const fields=['title','company','description','application','published','countries'];
const count=(value,max)=>Number.isSafeInteger(value)&&value>=0&&value<=max;

export function validateSnapshot(payload){
 if(snapshotHealth(payload).state==='invalid'||!Array.isArray(payload?.results)||!payload.results.length)throw new Error('Invalid snapshot');
 const seen=new Set();
 for(const row of payload.results){
  if(!sources.has(row?.source)||seen.has(row.source))throw new Error('Invalid snapshot source');
  seen.add(row.source);
  if(row.http_status!==200||row.error_type)throw new Error('Incomplete source snapshot');
  const n=row.sample_records;
  if(!count(n,20)||!count(row.duplicate_ids,n)||!fields.every(k=>count(row.nonempty_field_counts?.[k],n)))throw new Error('Invalid snapshot counts');
  if(row.listings!==undefined&&(!Array.isArray(row.listings)||row.listings.length>n||row.listings.some(j=>!j||typeof j!=='object')))throw new Error('Invalid snapshot listings');
 }
 return payload;
}

export async function readSnapshot(config, fetchImpl=fetch) {
 if(!config.url.startsWith('https://')||!config.publishableKey.startsWith('sb_publishable_'))throw new Error('Invalid public configuration');
 const url=config.url+'/rest/v1/dashboard_snapshots?select=payload&is_published=eq.true&order=checked_at.desc&limit=1';
 const response=await fetchImpl(url,{headers:{apikey:config.publishableKey},cache:'no-store',signal:AbortSignal.timeout(12000)});
 if(!response.ok)throw new Error('Database HTTP '+response.status);
 const rows=await response.json();
 if(!Array.isArray(rows)||!rows[0]?.payload)throw new Error('No published snapshot');
 return validateSnapshot(rows[0].payload);
}

