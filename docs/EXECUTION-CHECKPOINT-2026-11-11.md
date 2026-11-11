# Execution checkpoint — 11 November 2026

## Product boundary
Career and industry intelligence for motivated Bangladeshi learners. Global evidence, Bengali explanations, practical learning. No applications, CV intake or hiring. Hind Siliguri for Bengali. All core categories remain visible on the home dashboard. Abroad preparation remains explicitly deferred.

## Completed and verified
- Eight home category cards and detail routes; curated occupation, learning and AI tool guides.
- Source filter, tool search, empty/stale/error paths and keyboard heading focus.
- Real v2 collection at 16:29:04 Bangladesh time: Himalayas 20 + Jobicy 20; validated aggregate projection appended to Supabase, public read-back health passed. Browser showed the updated skill counts.
- Responsive iframe tests at outer widths 320/375/768 (content widths 305/360/753 after scrollbar): Overview, Skills, Learning, Tools, Work data, Business and Methodology rendered with document scroll width equal to viewport width in all 21 checks. This is CSS reflow testing, not physical device emulation.
- Narrow-screen text and control sizes improved; skip-to-content interaction corrected to preserve the selected route.
- Expanded live collection obtained 20 Himalayas + 100 Jobicy records, coverage version bounded-h20-j100-v2. Publication waits for the compatible frontend deployment.
- New source coverage version prevents interpreting a changed collection bound as growth. No public historical growth calculation is enabled.
- Collection workflow changed to aggregate-only; no job listing/application metadata needed for the current UI.
- 42 Python tests plus all JavaScript suites passed after these changes.
- Security advisor reported only INFO: collection_runs has RLS and no policy. It is intentionally internal; do not grant public access to silence that notice.

## Source terms rechecked
Official pages accessed 11 November 2026:
- https://himalayas.app/terms — API integrations permitted subject to attribution/linking, supplied apply URLs if used, no onward feed redistribution, cache/rate limits and expiry removal. Permanent raw history rights remain unresolved; raw descriptions are not retained.
- https://jobicy.com/jobs-rss-feed — free public endpoint without a key, up to 100 records per page in a seven-day discovery window. Fair-use section explicitly permits retained data and derived analysis, with source credit and closed-job handling. Paid direct ATS links are unnecessary because this platform does not accept job applications.

## Remaining release gates
1. Verify final committed build and expanded sample in the browser and public read client.
2. Complete recovery evidence: application/data export checks are not a full Supabase/Postgres restore rehearsal.
3. Test on an actual phone and with real target students; iframe checks do not prove mobile usability.
4. Obtain a public support/correction destination and final release identity/domain from the owner.
5. Broader evidence coverage and human validation before market-wide or long-term trend claims. The sample remains limited to two remote-job providers.
6. Paid sources, AI research APIs and courses have not been purchased, activated or silently included.

## Honest release position
This is a working pilot with real source data, editorial guidance and explicit limits. It is not the complete original vision, a validated global market model, a forecast engine or a nationally representative career recommendation system. Do not label it 100% complete.

## Follow-up verification
- Expanded payload published with original collection time 16:34:24 Bangladesh; public read health returned 120 observations, two sources, editorial-mentions-v2.
- Compatible staging deployment dpl_3CmzQEydq3uwBGm6tjexdUM7c7vU READY. Browser verified 120 combined observations, Jobicy filter 100, and Overview reset to 120.
- Final build repeated all 21 narrow iframe checks; no document-level horizontal overflow in those cases.
- Keyboard skip link now focuses main-content without changing the Skills route.
- Aggregate export and checksum roundtrip succeeded with the real live payload. Full database restoration remains a separate gate.
- Added daily aggregate artifact backup (14-day retention). First scheduled backup and six-hour health runs still require observation.
- Reopened the final preview and verified live skill totals again after the work resumed.

## Source and learner guidance extension
- Added a reviewed BLS report extract for four occupations (United States, 2025–2035), with source/copyright links, metric, date and geography. Downloaded source table values were checked independently. This is not another live vacancy API and is not merged with the two-provider sample.
- Added an editorial five-session starter plan on Learning. The learner explicitly chooses one of three topics, phone/computer, and 15/30/60 minutes per session. Time allocation sums to the selected duration. Preferences remain in page memory and are not transmitted/stored. No model call, aptitude score, payment or completion guarantee.
- This extends the existing device/time adaptation requirement. It does not infer a national personality or choose a career for a student.
