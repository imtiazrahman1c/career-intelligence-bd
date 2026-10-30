# Dashboard design specification

## Reference decision — 2026-10-30
Primary reference: user-supplied Microsoft Clarity dashboard screenshot. Secondary references: cashflow, daily pulse, sales, HubSpot, Salesforce and account-manager dashboards. They are visual references, not datasets for this product.

## Layout
1. Compact top navigation: Overview, Skills, Jobs, AI Tools, Platforms, Methodology.
2. Filter row: observed period, source, career family and geography where supported. Clearly distinguish employer location from applicant eligibility.
3. Four compact summary cards: unique observed postings, observed skills, source coverage and last successful update. Do not invent values or success scores.
4. Responsive grid: skill-frequency bars, role distribution, collection coverage and market signals. Trend charts appear only with comparable historical observations.
5. Evidence drill-down: source links, exact period, denominator, extraction method and limitations.
6. Career guidance: concise Bangla explanation and a practical next step, visually distinguished from measured data.

## Visual system
Light blue-gray canvas; white panels; restrained blue and violet interaction accents; readable dark text; subtle borders and shadows. Consistent spacing, aligned values, compact headings and clear chart labels. Bangla-first explanations with searchable English role and skill names. Final tokens will be validated in the implemented interface.

## Interactions
Filters must update relevant cards, charts and tables consistently. Every chart states units and denominator. Source changes must never silently produce comparable-looking growth. Empty, stale, loading and error states are explicit. Mobile cards stack and tables preserve essential content.

## Integrity
- Mock numbers are explicitly labeled demo and never mixed with real observations.
- No revenue, user-analytics, conversion, confidence or readiness scores borrowed from reference products.
- No decorative maps, gauges or rankings without a meaningful supported metric.
- Real charts must have evidence and traceable calculations.

## First implementation acceptance
A user can identify what the dashboard measures, apply a meaningful filter, inspect a source, distinguish sample coverage from market demand, and find one practical next step. Keyboard, mobile, empty and error states work.
