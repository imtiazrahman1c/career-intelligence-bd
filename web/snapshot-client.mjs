import {snapshotHealth} from './model.mjs';

const sources=new Set(['himalayas','jobicy']);
const fields=['title','company','description','application','published','countries'];
const count=(value,max)=>Number.isSafeInteger(value)&&value>=0&&value<=max;

export function validateSnapshot(payload){
 if(snapshotHealth(payload).state==='invalid'||!Array.isArray(payload?.results)||!payload.results.length)throw new Error('Invalid snapshot');
 if(!['bounded-20-v1','bounded-h20-j100-v2'].includes(payload.coverage_version??'bounded-20-v1'))throw new Error('Unknown snapshot coverage');
 const seen=new Set();
 for(const row of payload.results){
  if(!sources.has(row?.source)||seen.has(row.source))throw new Error('Invalid snapshot source');
  seen.add(row.source);
  if(row.http_status!==200||row.error_type)throw new Error('Incomplete source snapshot');
  const n=row.sample_records;
  if(!count(n,row.source==='jobicy'&&payload.coverage_version==='bounded-h20-j100-v2'?100:20)||!count(row.duplicate_ids,n)||!fields.every(k=>count(row.nonempty_field_counts?.[k],n)))throw new Error('Invalid snapshot counts');
  if(row.listings!==undefined&&(!Array.isArray(row.listings)||row.listings.length>n||row.listings.some(j=>!j||typeof j!=='object')))throw new Error('Invalid snapshot listings');
 }
 return payload;
}

export async function readSnapshot(config, fetchImpl=fetch) {
 let origin;try{const parsed=new URL(config?.url);if(parsed.protocol!=='https:'||parsed.username||parsed.password||parsed.port||parsed.pathname!=='/'||parsed.search||parsed.hash||!parsed.hostname.endsWith('.supabase.co')||typeof config.publishableKey!=='string'||!config.publishableKey.startsWith('sb_publishable_'))throw Error();origin=parsed.origin;}catch{throw new Error('Invalid public configuration');}
 const url=origin+'/rest/v1/dashboard_snapshots?select=payload&is_published=eq.true&order=checked_at.desc&limit=1';
 const response=await fetchImpl(url,{headers:{apikey:config.publishableKey},cache:'no-store',signal:AbortSignal.timeout(12000)});
 if(!response.ok)throw new Error('Database HTTP '+response.status);
 const rows=await response.json();
 if(!Array.isArray(rows)||!rows[0]?.payload)throw new Error('No published snapshot');
 return validateSnapshot(rows[0].payload);
}

