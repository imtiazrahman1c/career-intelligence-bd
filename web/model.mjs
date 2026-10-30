export function selectResults(snapshot,source='all'){
  if(!snapshot || !Array.isArray(snapshot.results))throw new Error('Invalid snapshot');
  return snapshot.results.filter(r=>source==='all'||r.source===source);
}
export function totals(results){
 const good=results.filter(r=>r.http_status===200&&!r.error_type);
 return {records:good.reduce((n,r)=>n+r.sample_records,0),sources:good.length,descriptions:good.reduce((n,r)=>n+r.nonempty_field_counts.description,0),duplicateIds:good.reduce((n,r)=>n+r.duplicate_ids,0)};
}
export function evidenceRows(results){const good=results.filter(r=>r.http_status===200&&!r.error_type);return ['title','company','description','application','published','countries'].map(field=>({field,count:good.reduce((n,r)=>n+(r.nonempty_field_counts?.[field]||0),0)}));}
export function snapshotHealth(snapshot,now=Date.now()){
 const timestamp=Date.parse(snapshot?.checked_at),age=now-timestamp;
 if(!Number.isFinite(timestamp)||age < -300000)return {state:'invalid',ageHours:null};
 return {state:age>86400000?'stale':'recent',ageHours:Math.max(0,Math.floor(age/3600000))};
}
export const skillLabels={sql:'SQL',python:'Python',spreadsheets:'Spreadsheets',power_bi:'Power BI',tableau:'Tableau',seo:'SEO',google_ads:'Google Ads',meta_ads:'Meta Ads',ga4:'GA4',copywriting:'Copywriting',photoshop:'Photoshop',illustrator:'Adobe Illustrator',figma:'Figma',typography:'Typography'};
export const careerSkills={data_analyst:['sql','python','spreadsheets','power_bi','tableau'],digital_marketer:['seo','google_ads','meta_ads','ga4','copywriting'],graphic_designer:['photoshop','illustrator','figma','typography']};
export function skillsForCareer(analysis,career='all'){
 if(!analysis)return [];
 if(career==='all')return analysis.skills;
 if(!Object.hasOwn(careerSkills,career))return [];
 return analysis.skills.filter(skill=>careerSkills[career].includes(skill.id));
}
export function jobListings(snapshot,source='all',query='',location='all',now=Date.now()){
 if(snapshotHealth(snapshot,now).state!=='recent')return [];
 const search=query.trim().toLocaleLowerCase();
 return selectResults(snapshot,source).filter(r=>r.http_status===200&&!r.error_type).flatMap(r=>(Array.isArray(r.listings)?r.listings:[]).filter(j=>{
  if(j.source!==r.source||j.availability==='closed'||typeof j.title!=='string'||typeof j.company!=='string')return false;
  try{const u=new URL(j.application_url);if(u.protocol!=='https:'||u.username||u.password||u.port||u.hostname!==({jobicy:'jobicy.com',himalayas:'himalayas.app'})[j.source])return false;}catch{return false;}
  return (!search||(j.title+' '+j.company).toLocaleLowerCase().includes(search))&&(location==='all'||j.location_signal===location);
 }));
}
export function availabilityLabel(status){return status==='active_at_collection'?'সংগ্রহের সময় source API-তে active':'Availability নিশ্চিত করা যায়নি';}
export function analysisTotals(results){
 const good=results.filter(r=>r.http_status===200&&!r.error_type);
 const valid=good.filter(r=>{const a=r.analysis,n=a?.unique_records_analyzed;
  return a?.method_version==='editorial-mentions-v1'&&Number.isInteger(n)&&n>=0&&n<=r.sample_records&&
   Object.keys(skillLabels).every(k=>Number.isInteger(a.skill_mention_counts?.[k])&&a.skill_mention_counts[k]>=0&&a.skill_mention_counts[k]<=n)&&
   a.location_signal_counts&&Object.entries(a.location_signal_counts).every(([k,v])=>['unknown','bangladesh_listed_review_required','worldwide_listed_review_required'].includes(k)&&Number.isInteger(v)&&v>=0)&&Object.values(a.location_signal_counts).reduce((s,v)=>s+v,0)===n;
 });
 if(!valid.length)return null;
 const counts=Object.fromEntries(Object.keys(skillLabels).map(k=>[k,valid.reduce((n,r)=>n+r.analysis.skill_mention_counts[k],0)]));
 return {records:valid.reduce((n,r)=>n+r.analysis.unique_records_analyzed,0),sources:valid.length,partial:valid.length!==good.length,skills:Object.entries(counts).map(([id,count])=>({id,label:skillLabels[id],count})).sort((a,b)=>b.count-a.count||a.label.localeCompare(b.label)),locations:Object.fromEntries(['unknown','bangladesh_listed_review_required','worldwide_listed_review_required'].map(k=>[k,valid.reduce((n,r)=>n+(r.analysis.location_signal_counts[k]||0),0)]))};
}
