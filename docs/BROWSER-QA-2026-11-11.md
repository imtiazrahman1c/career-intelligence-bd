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
- Browser verification of the cleanup deployment, mobile viewport, keyboard-only flow and enlarged text.
- More source coverage and validated skill classification; current samples cannot support market-wide growth claims.
- Comparable history integration and source reuse/retention review.
- Backup restoration rehearsal, monitoring and final production release verification.

This is staging QA evidence, not production readiness certification.
