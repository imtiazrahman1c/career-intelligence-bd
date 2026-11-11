import {pathToFileURL} from 'node:url';
import {databaseConfig} from '../web/config.mjs';
import {readSnapshot,validateSnapshot} from '../web/snapshot-client.mjs';
import {snapshotHealth,analysisTotals} from '../web/model.mjs';

export function assessDataHealth(snapshot,now=Date.now()){
 const issues=[];
 try{validateSnapshot(snapshot);}catch{return {ok:false,issues:['invalid_snapshot']};}
 const freshness=snapshotHealth(snapshot,now);
 if(freshness.state!=='recent')issues.push('snapshot_'+freshness.state);
 const actual=new Set(snapshot.results.map(row=>row.source));
 if(!['himalayas','jobicy'].every(source=>actual.has(source)))issues.push('missing_source');
 const analysis=analysisTotals(snapshot.results);
 if(!analysis||analysis.partial)issues.push('incomplete_or_incompatible_analysis');
 return {ok:issues.length===0,issues,checkedAt:snapshot.checked_at,
  ageHours:freshness.ageHours,sourceCount:actual.size,
  methodVersion:analysis?.methodVersion??null,recordsAnalyzed:analysis?.records??null};
}

if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 try{
  const result=assessDataHealth(await readSnapshot(databaseConfig));
  console.log(JSON.stringify(result));
  if(!result.ok)process.exitCode=1;
 }catch{
  // Never emit credentials, raw data, provider response bodies or request headers.
  console.error('Published data health check failed: snapshot could not be read.');
  process.exitCode=1;
 }
}
