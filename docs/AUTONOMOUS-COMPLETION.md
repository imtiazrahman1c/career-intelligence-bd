# Autonomous release-preparation checklist

11 November 2026. Working pilot scope, not the complete long-term vision.

## Completed
- [x] Eight-category navigation, source-aware occupation/tool/learning guides, official report examples and learner-selected starter exercises.
- [x] Real aggregate ingestion, public read verification, expanded 120-record collection and method/coverage version boundaries.
- [x] Missing-source warning, explicit stale/empty/error states, saved content retained on refresh failure.
- [x] Avoid rerendering editorial forms when the background sample request completes.
- [x] Reject unexpected client endpoint hosts, URL credentials and unknown collection coverage before sending a request.
- [x] Explicit aggregate-only backup projection; unsupported/incomplete analysis and corrupt envelopes rejected.
- [x] Public aggregate backup export, GitHub artifact retention and verified download/recovery path.
- [x] Disposable PostgreSQL application database dump/restore: migration, real aggregate payload, synthetic visibility fixtures, RLS and anon/authenticated read-only grants tested in source and restored databases. Run 43032077488 succeeded; job 130561405609 and its restore verification step succeeded.
- [x] Narrow iframe reflow, keyboard focus and planner interactions tested. Physical mobile and real-user testing remain distinct.
- [x] Security headers configured: CSP restricting scripts/connect destinations, nosniff, same-origin framing, referrer policy, disabled unused device permissions. Final deployed header/browser verification recorded after release build below.
- [x] Correction-report form prepared in the project's enabled GitHub Issues; no email account, message sending or personal-data form required. Reports are public and require a GitHub account.
- [x] Technical data-connection and local-preference notice in Methodology.
- [x] Offline checks: 42 Python tests and all JS suites pass, including malformed data, form-state preservation and backup boundary checks.

## Not claimed complete
- The original vision's broad global coverage, validated occupation classification and national/international demand estimates.
- A representative longitudinal dataset. Do not fabricate historical growth from changing sample limits or a new extraction method.
- A full Supabase service restore including Auth/private schemas/storage. The tested application uses the three public-schema tables from its migration.
- Feedback from real Bangladeshi students, real-device checks, and a final public launch.
- Paid providers, AI API budgets, courses and the deferred abroad-preparation module.

The correction-report link removes the earlier email dependency. Owner feedback is still needed to validate whether the actual learners understand and benefit from the product.

## Final deployment verification
- Preview deployment `dpl_AnDtnMY2T21MsTjdVBXSr6X3Yee4` is READY, built from application state at `7b3cac651a4d12dcebffae693a5c6142ea204806`.
- HTTP 200 and actual CSP, nosniff, SAMEORIGIN, referrer and permissions headers verified through Vercel fetch.
- Browser loaded the 120-observation saved snapshot, collected 11 November 2026 at 16:34:24 Bangladesh time.
- Learning form generated five digital-marketing exercises for phone / 30 minutes, split into 7 learning + 18 practice + 5 review minutes.
- Responsive harness and external script worked under CSP; 320px outer frame had equal 305px document client/scroll width, with the learning form present. This is CSS reflow testing, not physical-device certification.
- No application console errors observed; a browser-extension metadata error was unrelated to application source.
- Latest application checks run `43032651534` succeeded. Previous restore, backup and health runs also succeeded.
- Deployment remains a development preview; no production launch or paid API activation was performed.
