// Provider capabilities checked against official pages; career use cases are editorial.
export const toolsDirectory=[
 {id:'canva',name:'Canva AI',careers:['digital_marketer','graphic_designer'],use:'Brief থেকে design draft, presentation বা social content-এর প্রাথমিক ধারণা তৈরি।',practice:'কাল্পনিক local business-এর জন্য একটি পোস্ট বানাও; typography ও বাংলা বানান নিজে ঠিক করো।',limit:'Generated design সরাসরি final ধরে নিও না; brand fit, text ও asset rights যাচাই করো।',url:'https://www.canva.com/canva-ai/',checked:'2026-10-30'},
 {id:'firefly',name:'Adobe Firefly',careers:['digital_marketer','graphic_designer'],use:'Text prompt দিয়ে image concept তৈরি ও generative image editing।',practice:'একই brief-এর তিনটি visual direction বানিয়ে composition তুলনা করো।',limit:'Image-এর detail, লেখা ও ব্যবহারের উপযোগিতা review করো; feature ও credit allowance plan অনুযায়ী বদলায়।',url:'https://helpx.adobe.com/firefly/web/get-started/learn-the-basics/adobe-firefly-overview.html',checked:'2026-10-30'},
 {id:'github-copilot',name:'GitHub Copilot',careers:['data_analyst'],use:'Code suggestion, code বোঝা ও coding প্রশ্নে সহায়তা।',practice:'Synthetic data-র একটি Python cleaning script বুঝে লেখো; output হাতে মিলিয়ে দেখো।',limit:'Code ভুল হতে পারে। Run করার আগে review এবং test করো; শেখার বিকল্প নয়।',url:'https://docs.github.com/en/copilot/get-started/about-github-copilot',checked:'2026-10-30'},
 {id:'microsoft-copilot',name:'Microsoft Copilot · Image generation',careers:['digital_marketer','graphic_designer'],use:'Prompt থেকে image তৈরি এবং visual idea পরীক্ষা।',practice:'একটি কাল্পনিক campaign-এর mood-board image তৈরি করে audience fit ব্যাখ্যা করো।',limit:'Generated image-এ ভুল থাকতে পারে; ব্যক্তি, brand ও asset rights বিবেচনা করে ব্যবহার করো।',url:'https://support.microsoft.com/en-us/microsoft-copilot/using-image-generation-in-microsoft-copilot',checked:'2026-10-30'},
];
export function findTools(query='',career='all'){
 const q=query.trim().toLocaleLowerCase();
 return toolsDirectory.filter(t=>(career==='all'||t.careers.includes(career))&&(!q||(t.name+' '+t.use).toLocaleLowerCase().includes(q)));
}
