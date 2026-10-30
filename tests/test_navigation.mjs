import assert from 'node:assert/strict';
import {viewFromHash,requiresSnapshot,views} from '../web/navigation.mjs';
for(const view of views)assert.equal(viewFromHash('#'+view),view);
assert.equal(viewFromHash('#<script>'),'overview');
assert.equal(viewFromHash(''),'overview');
assert.equal(requiresSnapshot('tools'),false);
assert.equal(requiresSnapshot('platforms'),false);
assert.equal(requiresSnapshot('jobs'),true);
console.log('PASS deep-link validation and database-independent views');
