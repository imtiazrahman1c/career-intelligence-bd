# Browser QA — 11 November 2026

Tested staging deployment: dpl_2qZxpsYV45MdhMCWqYpP5B6bqzgz (before the UX cleanup below).

## Observed in Chrome
- Overview loaded the saved sample: 40 observations across 2 sources.
- Skills and learning guides rendered; navigation focused the page heading.
- AI tools search for Canva reduced the directory from 4 results to 1 matching result.
- Emerging fields, business, outlook, source directory, methodology and deferred abroad page rendered.
- Jobs source filter Himalayas reduced counts from 40 observations / 2 sources to 20 / 1; completeness table updated consistently.
- Desktop learning screenshot showed the three learning paths side by side.
- Console inspection returned browser-extension metadata errors; these were not application-origin errors. This limited log sample is not a clean-console guarantee.

## UX cleanup from the review
Commit be3b125e70dc2d949b6209e93149dc7893e2912d includes the cumulative app, HTML and CSS edits.
- Hide sample controls on editorial-only guide pages.
- Enable the source selector for both skills and jobs; overview uses the complete sample regardless of the last detail-page filter.
- Hide the single-option period selector and replace developer-facing toolbar/banner labels.
- Remove the application eligibility panel from the skills page to match the product's learning and insight purpose.
- Preserve Hind Siliguri font and add explicit hidden-element styling.
- Local checks: 35 Python tests and all JavaScript suites passed.

## Release gates still open
- Mobile viewport, complete keyboard-only flow and enlarged text (still not verified).
- More source coverage and validated skill classification; current samples cannot support market-wide growth claims.
- Comparable history integration and source reuse/retention review.
- Backup restoration rehearsal, monitoring and final production release verification.

This is staging QA evidence, not production readiness certification.

## Cleanup deployment follow-up

Deployment dpl_4XTFeJBBGG93ADE6oDE8yarUEoEH was READY and opened in Chrome.
- Skills source selector: selecting Himalayas showed 20 observations.
- Returning to Overview showed all 40 source observations, independent of the last detail-page filter.
- Learning page sample toolbar was not visible, as intended.
- Removed eligibility panel was absent from the Skills accessibility tree.
- Learning page heading focus followed by Tab moved to the Google Sheets resource link. This is one focus transition, not a full keyboard audit.
- DOM computed font for body and AI tools search input was Hind Siliguri, sans-serif.
- At desktop width 1348 CSS px, document scroll width was also 1348 px on Learning (no document-level horizontal overflow there).
- Browser device-mode shortcuts did not change the observed viewport. Mobile and enlarged-text results remain unverified; no claim of mobile QA completion.

Next priority: verify a real narrow viewport, then broaden and validate the evidence base before publishing market trend claims.
