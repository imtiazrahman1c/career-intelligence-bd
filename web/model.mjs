export function selectResults(snapshot,source='all'){
  if(!snapshot || !Array.isArray(snapshot.results))throw new Error('Invalid snapshot');
  return snapshot.results.filter(r=>source==='all'||r.source===source);
}
export function totals(results){
 const good=results.filter(r=>r.http_status===200&&!r.error_type);
 return {records:good.reduce((n,r)=>n+r.sample_records,0),sources:good.length,descriptions:good.reduce((n,r)=>n+r.nonempty_field_counts.description,0),duplicateIds:good.reduce((n,r)=>n+r.duplicate_ids,0)};
}
export function evidenceRows(results){return ['title','company','description','application','published','countries'].map(field=>({field,count:results.reduce((n,r)=>n+(r.nonempty_field_counts?.[field]||0),0)}));}
