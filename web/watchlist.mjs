export const careerNames={data_analyst:'Data Analyst',digital_marketer:'Digital Marketer',graphic_designer:'Graphic Designer'};
const key='career-intelligence-bd:watchlist:v1';
export function cleanWatchlist(value){return Array.isArray(value)?[...new Set(value.filter(v=>typeof v==='string'&&Object.hasOwn(careerNames,v)))]:[];}
export function readWatchlist(storage){try{return cleanWatchlist(JSON.parse(storage.getItem(key)));}catch{return [];}}
export function writeWatchlist(storage,value){try{storage.setItem(key,JSON.stringify(cleanWatchlist(value)));return true;}catch{return false;}}
export function toggleCareer(current,id){if(!Object.hasOwn(careerNames,id))return cleanWatchlist(current);const list=cleanWatchlist(current);return list.includes(id)?list.filter(v=>v!==id):[...list,id];}
