export const views=['overview','skills','jobs','tools','platforms','methodology'];
export function viewFromHash(hash){const view=hash.replace(/^#/,'');return views.includes(view)?view:'overview';}
export function requiresSnapshot(view){return !['tools','platforms'].includes(view);}
