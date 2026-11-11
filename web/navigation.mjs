export const views=['overview','skills','jobs','tools','platforms','methodology','emerging','business','outlook','learning','abroad'];
export function viewFromHash(hash){const view=hash.replace(/^#/, '');return views.includes(view)?view:'overview';}
export function requiresSnapshot(view){return ['jobs','methodology'].includes(view);}
