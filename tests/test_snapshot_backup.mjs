import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {encodeBackup,decodeBackup} from '../scripts/snapshot-backup.mjs';
const snapshot=JSON.parse(await readFile(new URL('../docs/analysis-probe-summary.json',import.meta.url)));
snapshot.checked_at=new Date().toISOString();
snapshot.results[0].analysis.unexpected_raw='must not be exported';
snapshot.results[0].listings=[{description:'must not be exported'}];
const encoded=encodeBackup(snapshot);
assert.doesNotMatch(encoded,/must not be exported/);
const restored=decodeBackup(encoded);
assert.equal(restored.results[0].analysis.method_version,snapshot.results[0].analysis.method_version);
assert.equal(restored.results[0].analysis.skill_mention_counts.sql,snapshot.results[0].analysis.skill_mention_counts.sql);
assert.equal(restored.results[0].analysis.unexpected_raw,undefined);
const damaged=JSON.parse(encoded);damaged.payload+=' ';
assert.throws(()=>decodeBackup(JSON.stringify(damaged)),/integrity/);
assert.throws(()=>decodeBackup('{}'),/integrity/);
console.log('PASS aggregate backup roundtrip, metadata projection and corruption rejection');

const noAnalysis=structuredClone(snapshot);delete noAnalysis.results[0].analysis;assert.throws(()=>encodeBackup(noAnalysis),/analysis/);
