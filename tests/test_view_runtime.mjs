import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import {makeStarterPlan} from '../web/learning-plan.mjs';
import {occupationProjection} from '../web/projections.mjs';
import * as review from '../web/content-review.mjs';
import * as model from '../web/model.mjs';
import * as navigation from '../web/navigation.mjs';
import * as learning from '../web/learning-resources.mjs';
import * as profiles from '../web/career-profiles.mjs';
import * as watch from '../web/watchlist.mjs';
import * as tools from '../web/tools.mjs';
const elements=new Map();
const element=id=>{if(!elements.has(id))elements.set(id,{value:id==='source'?'all':'',textContent:'',innerHTML:'',className:'',focus(){this.focused=true;},addEventListener(type,fn){this[type]=fn;},setAttribute(){},removeAttribute(){}});return elements.get(id);};
const nav=navigation.views.map(id=>({dataset:{tab:id},textContent:id,setAttribute(){},removeAttribute(){}}));
const context={makeStarterPlan,occupationProjection,...review,...model,...navigation,...profiles,...learning,...watch,...tools, databaseConfig:{},readSnapshot:async()=>{throw Error('simulated offline');},document:{getElementById:element,querySelector:selector=>nav.find(n=>selector.includes('"'+n.dataset.tab+'"')),querySelectorAll:()=>nav},window:{localStorage:{getItem:()=>null},addEventListener(){}},location:{hash:''},history:{pushState(){}},console};
vm.createContext(context);
vm.runInContext(fs.readFileSync('web/app.js','utf8').replace(/^import .*;\n/gm,''),context);
assert.equal((element('content').innerHTML.match(/data-go=/g)||[]).length,8);
for(const id of navigation.views){element('tabs').click({target:{closest:()=>({dataset:{tab:id}})}});assert.ok(element('content').innerHTML.length>0,id);}
element('tabs').click({target:{closest:()=>({dataset:{tab:'skills'}})}});
assert.match(element('content').innerHTML,/15-2051.01/);
assert.match(element('content').innerHTML,/কাজটা করে দেখো/);
assert.equal(navigation.requiresSnapshot('skills'),false);
element('tabs').click({target:{closest:()=>({dataset:{tab:'methodology'}})}});
assert.match(element('content').innerHTML,/কনটেন্ট আবার যাচাইয়ের সময়/);
assert.doesNotMatch(element('content').innerHTML,/Invalid Date/);
element('tabs').click({target:{closest:()=>({dataset:{tab:'learning'}})}});
assert.match(element('content').innerHTML,/skillshop.withgoogle.com/);
assert.match(element('content').innerHTML,/মোট খরচ নিশ্চিত করা হয়নি/);
await new Promise(resolve=>setImmediate(resolve));
assert.match(element('status').textContent,/পড়া যায়নি/);
console.log('PASS offline overview, all view routes, sourced skill profiles and failed database load');

const sample={checked_at:new Date().toISOString(),results:[{source:'jobicy',http_status:200,sample_records:2,duplicate_ids:0,nonempty_field_counts:{title:2,company:2,description:2,application:2,published:2,countries:2}}]};
context.readSnapshot=async()=>sample;
await vm.runInContext('load()',context);
for(const id of navigation.views){element('tabs').click({target:{closest:()=>({dataset:{tab:id}})}});assert.ok(element('content').innerHTML.length>0,id);}
assert.equal(element('page-title').focused,true);
element('tabs').click({target:{closest:()=>({dataset:{tab:'jobs'}})}});
assert.match(element('content').innerHTML,/নমুনায় কাজের পর্যবেক্ষণ/);
assert.doesNotMatch(element('content').innerHTML,/application_url|বিস্তারিত ও আবেদন/);
context.readSnapshot=async()=>({...sample,checked_at:new Date(Date.now()-48*3600000).toISOString()});
await vm.runInContext('load()',context);
element('tabs').click({target:{closest:()=>({dataset:{tab:'overview'}})}});
assert.match(element('freshness').textContent,/২৪ ঘণ্টার বেশি পুরোনো/);
context.readSnapshot=async()=>{throw Error('simulated refresh failure');};
await vm.runInContext('load()',context);
assert.match(element('status').textContent,/আগের সংরক্ষিত snapshot/);
assert.equal((element('content').innerHTML.match(/data-go=/g)||[]).length,8);
console.log('PASS loaded/stale samples, retained content after refresh failure and navigation focus');

let skipPrevented=false;element('skip-link').click({preventDefault(){skipPrevented=true;}});assert.equal(skipPrevented,true);assert.equal(element('main-content').focused,true);

element('tabs').click({target:{closest:()=>({dataset:{tab:'emerging'}})}});assert.match(element('content').innerHTML,/২০২৫–২০৩৫/);assert.match(element('content').innerHTML,/34.6%/);assert.match(element('content').innerHTML,/বাংলাদেশের পূর্বাভাস/);

element('tabs').click({target:{closest:()=>({dataset:{tab:'learning'}})}});
element('learning-career').value='digital_marketer';element('learning-device').value='phone';element('learning-minutes').value='30';
element('content').submit({target:{id:'learning-plan'},preventDefault(){}});
assert.match(element('content').innerHTML,/প্রথম পাঁচটি অনুশীলন/);assert.equal(element('starter-plan').focused,true);
