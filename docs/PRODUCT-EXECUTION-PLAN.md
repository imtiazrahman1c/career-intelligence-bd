> Historical planning baseline. For the current verified state, see EXECUTION-CHECKPOINT-2026-11-11.md. The old baseline and unchecked items below are not current status.

# Product execution reference
Updated: 2026-11-09, Asia/Dhaka

## Scope
Help motivated Bangladeshi students interpret international and local changes in business, work, skills and AI, and choose practical next learning steps.
No application submission, CV collection, hiring or application tracker. Job posts are evidence inputs. Optional Bangladesh portal directory links to original providers.
Bangladesh-focused audience does not require geographic blocking.
All Bengali typography uses Hind Siliguri.
Home displays every core category as an information card with its own detail view, inspired by the supplied Clarity layout.

## Verified access and baseline
GitHub push access works. Audited main commit: 7abf91a5763acf3e206ba9da5e07bcd6e1b3c295.
Latest scheduled collection/publish runs succeeded: 42575185881 (2026-11-09T06:47:22Z), 42509159872 (2026-11-08T18:16:40Z), 42455090729 (2026-11-08T06:31:35Z).
Supabase accessible: data_sources 2 rows; dashboard_snapshots 15 rows; collection_runs 0 rows. RLS enabled on these tables. These are tool-reported counts, not content accuracy checks.
Vercel latest listed deployment dpl_9uSf3h6KqFZVYqw2e66AndddTx7X is READY with staging target. Browser journey/public launch not verified.
Reviewed web/index.html, web/app.js and analysis/skills.py.
Existing functionality: sample counts, skill mention extraction, curated tools, browser watchlist.
Gaps: overview lacks the agreed categories; industry growth, comparable history and five-year scenarios are absent. Application wording conflicts with scope. Freshness text incorrectly says automatic collection is inactive. Investigate empty collection_runs before using it for monitoring.
Existing tests have not been rerun in this audit.

## Category contract
- Skills: mentions, prerequisites and practical exercises.
- Work market: role/task signals by geography and period, no applications.
- AI/tools: task-based use, limitations, cost and verification date.
- Emerging work: sourced changes in roles and tasks.
- Business/industries: distinct investment, revenue or other indicators; no automatic inference of hiring growth.
- Five-year outlook: conditional scenarios with assumptions and review dates.
- Learning pathways: device/time/budget, first exercise and international communication practice.
- Working-abroad preparation: later phase; destination-specific official information required.

## Evidence contract
Distinguish observed fact, editorial interpretation and future scenario.
Quantitative insights require source, geography, period, denominator, coverage and checked date.
Compare compatible periods and methods; deduplicate; retain history.
Posting counts are not hires or total market demand.
Missing evidence is unavailable, never zero or invented model output.
AI research/classification/drafting must retain source provenance.
No unsupported career suitability scores, salary guarantees or precise forecast probabilities.
Adapt to declared learner constraints; do not infer one national psychology.

## Launch checklist
1. [x] Access and baseline audit; deeper payload/browser/testing checks below.
2. [ ] Apply scope contract; new features require explicit plan updates.
3. [ ] Source matrix: fields, cost, coverage, permitted use, samples.
4. [ ] Analysis rules and validation cases.
5. [ ] Bangladesh adaptation and editorial rules.
6. [ ] Overview/detail design, mobile layout, Hind Siliguri.
7. [ ] Collection, normalized storage and failure visibility.
8. [ ] One complete topic from source to learning exercise.
9. [ ] Extend validated pattern to first-release categories.
10. [ ] Refresh schedule, stale states and correction flow.
11. [ ] Security/access, backups, cost limits, contact information.
12. [ ] Regression tests, browser/API/data verification, student usability checks.
13. [ ] Final preview review, domain decision and public release.
14. [ ] Public smoke check, refresh verification and handover.

Assistant owns research, design, code, data and tests. User supplies blocked access, paid-service decisions, product review and final release decision.
Next implementation: overview category navigation/detail structure; remove application framing; correct freshness text. Preserve the collection pipeline.

