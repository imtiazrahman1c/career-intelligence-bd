// Editorial refresh is independent from automated market-sample collection.
export const reviewRegister=[
 {id:'bls',label:'BLS: যুক্তরাষ্ট্রের পেশার প্রক্ষেপণ',checked:'2026-11-11',intervalDays:90},
 {id:'outlook',label:'WEF: কাজ ও স্কিলের সম্ভাবনা',checked:'2026-11-11',intervalDays:90},
 {id:'business',label:'IEA: জ্বালানি বিনিয়োগ',checked:'2026-11-11',intervalDays:90},
 {id:'skills',label:'O*NET: পেশার পরিচয়',checked:'2026-11-11',intervalDays:90},
 {id:'learning',label:'শেখার লিংক ও প্রবেশের শর্ত',checked:'2026-11-11',intervalDays:30},
 {id:'platforms',label:'বাংলাদেশের উৎসের প্রাপ্যতা',checked:'2026-11-11',intervalDays:7}
];
export function reviewStatus(item,now=Date.now()){
 const checked=Date.parse(item.checked+'T00:00:00Z');
 if(!Number.isFinite(checked)||!Number.isInteger(item.intervalDays)||item.intervalDays<1||!Number.isFinite(now)||now<checked)return {state:'unknown',due:null};
 const due=checked+item.intervalDays*86400000;
 return {state:now>=due?'due':'scheduled',due:new Date(due).toISOString().slice(0,10)};
}
