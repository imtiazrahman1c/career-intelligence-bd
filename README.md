# Career Intelligence BD

A Bangladesh-first career intelligence platform for students and early-career learners. International evidence informs exploration; it is never presented as Bangladesh-specific demand without supporting data.

## Delivery scope
- Skills Intelligence
- Jobs Intelligence
- AI Tools directory
- Job Platform directory
- Evidence-backed Market Signals where comparable history exists

Initial coverage: three career paths, up to two approved job sources and one occupation/skills taxonomy.

## Design direction
Microsoft Clarity is the primary user-provided reference: a light canvas, white cards, compact top navigation, a persistent filter row, readable metrics, and clear chart panels. Other supplied dashboards inform comparisons and chart hierarchy, not sales metrics or employee leaderboards.

See [design specification](docs/DESIGN.md) and [progress checklist](docs/PROGRESS.md).

## Proposed structure
- web/: dashboard application (not implemented yet)
- collectors/: source adapters and validation (not implemented yet)
- supabase/: versioned database migrations (not implemented yet)
- tests/: meaningful data and integration tests (not implemented yet)
- docs/: scope, methods, design and checkpoints

## Environment
Dedicated Supabase and Vercel projects are provisioned. No production app, schema, source integration or scheduled collection has been deployed yet. Secrets must remain outside this public repository.
