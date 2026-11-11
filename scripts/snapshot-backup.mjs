import {createHash} from 'node:crypto';
import {writeFile,readFile} from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
import {databaseConfig} from '../web/config.mjs';
import {readSnapshot,validateSnapshot} from '../web/snapshot-client.mjs';
const digest=text=>createHash('sha256').update(text).digest('hex');
export function encodeBackup(snapshot){
 validateSnapshot(snapshot);
 // Explicit aggregate projection: no raw listing metadata or descriptions.
 const payload={checked_at:snapshot.checked_at,coverage_version:snapshot.coverage_version??'bounded-20-v1',results:snapshot.results.map(row=>({source:row.source,http_status:row.http_status,sample_records:row.sample_records,duplicate_ids:row.duplicate_ids,nonempty_field_counts:row.nonempty_field_counts,analysis:row.analysis}))};
 const text=JSON.stringify(payload);
 return JSON.stringify({format:'career-public-aggregate-v1',exported_at:new Date().toISOString(),sha256:digest(text),payload:text},null,2);
}
export function decodeBackup(text){
 const envelope=JSON.parse(text);
 if(envelope.format!=='career-public-aggregate-v1'||typeof envelope.payload!=='string'||digest(envelope.payload)!==envelope.sha256)throw Error('Invalid backup integrity');
 return validateSnapshot(JSON.parse(envelope.payload));
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 try{
  const [mode,path]=process.argv.slice(2);
  if(!path||!['export','verify'].includes(mode))throw Error('Expected export|verify path');
  if(mode==='export')await writeFile(path,encodeBackup(await readSnapshot(databaseConfig)),{flag:'wx'});
  const restored=decodeBackup(await readFile(path,'utf8'));
  console.log(JSON.stringify({ok:true,mode,checkedAt:restored.checked_at,sources:restored.results.length}));
 }catch{console.error('Aggregate backup operation failed. Existing files were not replaced.');process.exitCode=1;}
}
