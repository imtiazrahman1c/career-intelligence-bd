import {readFile,writeFile} from 'node:fs/promises';
import {decodeBackup} from './snapshot-backup.mjs';
const [input,output]=process.argv.slice(2);
if(!input||!output)throw Error('Expected verified aggregate backup and output SQL paths');
const snapshot=decodeBackup(await readFile(input,'utf8'));
const literal=value=>"'"+String(value).replaceAll("'","''")+"'";
// Executed only in the disposable CI database. The hidden row is synthetic.
const sql=`insert into public.data_sources(source_key,display_name,documentation_url,public_visible) values
('himalayas','Fixture visible source','https://himalayas.app/',true),
('jobicy','Fixture hidden source','https://jobicy.com/',false);
insert into public.dashboard_snapshots(checked_at,payload,is_published) values
(${literal(snapshot.checked_at)}::timestamptz,${literal(JSON.stringify(snapshot))}::jsonb,true),
('2000-01-01T00:00:00Z'::timestamptz,'{"results":[],"synthetic_private_fixture":true}'::jsonb,false);
`;
await writeFile(output,sql,{flag:'wx'});
console.log('Disposable restore fixture prepared from verified aggregate.');
