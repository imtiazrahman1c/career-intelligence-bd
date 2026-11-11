import assert from 'node:assert/strict';
import {reviewRegister,reviewStatus} from '../web/content-review.mjs';
const item={checked:'2026-11-11',intervalDays:7};
assert.equal(reviewStatus(item,Date.parse('2026-11-17T23:59:59Z')).state,'scheduled');
assert.equal(reviewStatus(item,Date.parse('2026-11-18T00:00:00Z')).state,'due');
assert.equal(reviewStatus({...item,checked:'bad'}).state,'unknown');
assert.equal(reviewStatus(item,Date.parse('2026-11-10')).state,'unknown');
assert.equal(new Set(reviewRegister.map(x=>x.id)).size,reviewRegister.length);
console.log('PASS editorial review deadlines, invalid dates and future checks');
