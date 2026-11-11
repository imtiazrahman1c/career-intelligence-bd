import assert from 'node:assert/strict';
import {makeStarterPlan} from '../web/learning-plan.mjs';
for(const career of ['data_analyst','digital_marketer','graphic_designer'])for(const device of ['phone','computer'])for(const minutes of [15,30,60]){
 const p=makeStarterPlan({career,device,minutes});
 assert.equal(Object.values(p.blocks).reduce((a,b)=>a+b,0),minutes);
 assert.ok(Object.values(p.blocks).every(n=>n>0));assert.equal(p.completionGuarantee,false);
 assert.equal(p.steps.length,5);
}
for(const x of [{career:'unknown',device:'phone',minutes:15},{career:'data_analyst',device:'phone',minutes:0},{career:'data_analyst',device:'server',minutes:30}])assert.equal(makeStarterPlan(x),null);
console.log('PASS starter plan time budgets, supported constraints and invalid input');
