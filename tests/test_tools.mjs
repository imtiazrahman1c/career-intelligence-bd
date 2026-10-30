import assert from 'node:assert/strict';
import {toolsDirectory,findTools} from '../web/tools.mjs';
assert.equal(findTools('CANVA').length,1);
assert.equal(findTools('','data_analyst')[0].id,'github-copilot');
assert.equal(findTools('Canva','data_analyst').length,0);
assert.equal(findTools('missing').length,0);
assert.equal(new Set(toolsDirectory.map(t=>t.id)).size,toolsDirectory.length);
for(const t of toolsDirectory){assert.equal(new URL(t.url).protocol,'https:');assert.ok(t.checked&&t.limit&&t.practice);}
console.log('PASS tool search, career filter, no-match and source metadata');
