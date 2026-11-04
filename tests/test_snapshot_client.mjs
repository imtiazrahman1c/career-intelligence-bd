import assert from 'node:assert/strict';
import {readSnapshot} from '../web/snapshot-client.mjs';
const config={url:'https://example.supabase.co',publishableKey:'sb_publishable_test'};
const row={source:'jobicy',http_status:200,sample_records:1,duplicate_ids:0,nonempty_field_counts:{title:1,company:1,description:1,application:1,published:1,countries:1}};
const payload={checked_at:'2026-10-30T00:00:00Z',results:[row]};
assert.deepEqual(await readSnapshot(config,async(url,options)=>{assert.match(url,/dashboard_snapshots/);assert.equal(options.headers.apikey,config.publishableKey);return {ok:true,json:async()=>[{payload}]};}),payload);
await assert.rejects(readSnapshot(config,async()=>({ok:false,status:503})),/503/);
await assert.rejects(readSnapshot(config,async()=>({ok:true,json:async()=>[]})),/No published/);
await assert.rejects(readSnapshot({...config,publishableKey:'secret'},async()=>{}),/Invalid/);
console.log('PASS: database response, access header, empty state, failure and key validation');

for(const results of [[null],[row,row],[{...row,http_status:503}],[{...row,sample_records:'1'}],[{...row,listings:[null]}],[]]){
 await assert.rejects(readSnapshot(config,async()=>({ok:true,json:async()=>[{payload:{...payload,results}}]})),/snapshot/);
}
console.log('PASS malformed snapshots rejected before they reach the dashboard');
