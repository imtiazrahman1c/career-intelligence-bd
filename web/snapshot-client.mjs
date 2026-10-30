export async function readSnapshot(config, fetchImpl=fetch) {
 if(!config.url.startsWith('https://')||!config.publishableKey.startsWith('sb_publishable_'))throw new Error('Invalid public configuration');
 const url=config.url+'/rest/v1/dashboard_snapshots?select=payload&order=checked_at.desc&limit=1';
 const response=await fetchImpl(url,{headers:{apikey:config.publishableKey},cache:'no-store',signal:AbortSignal.timeout(12000)});
 if(!response.ok)throw new Error('Database HTTP '+response.status);
 const rows=await response.json();
 if(!Array.isArray(rows)||!rows[0]?.payload)throw new Error('No published snapshot');
 return rows[0].payload;
}
