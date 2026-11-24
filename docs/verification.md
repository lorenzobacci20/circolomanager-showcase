# Verification scope

## Product shown

The demonstration runs the actual application with a dedicated SQL Server database. All members, staff, dates of birth, membership periods, bookings, competition entries and financial movements in the media are fictional. The venue has three courts, twelve members and two courses. The seed and the application binaries stay in the private demo environment. Messaging and payments are disabled.

The recording follows two writes from selection to confirmation. A staff member finds Elena Valli, previews her renewal, confirms it and returns to the member record. The same operator opens the court calendar, chooses a player and a free slot, reviews the fee and saves a booking. The separate stills cover the dashboard, calendar, member record, renewal preview, attendance, tournaments, member account and mobile interface.

On 24 November 2026, the Release build, schema consistency check, test suites and publish completed from the application revision used for this demonstration. All 608 xUnit tests and 43 Node tests passed, with zero skipped. SQL Server integration cases ran against a separate temporary database. These counts describe the private application's test suites.

The recorded installation check of 21 November 2026 verified service readiness and system-administrator access. First-club onboarding and member-facing and staff workflows on that installation remain open. Optional integrations have separate activation requirements. The demonstration supplies local workflow evidence.

## Portfolio checks

Four static pages cover the product and the case study in English and Italian. They were exercised in Chrome at 320, 390, 768 and 1440 CSS pixels, under the same project path expected on the static host.

| Check | Observed result |
| --- | --- |
| Navigation and media | Local links, sections, language switches, all eight images and their full-size destinations loaded. The 61.36-second film played and retained the requested position when seeking to its midpoint and ending. Both languages have timed descriptions and a text alternative. |
| Keyboard and reflow | The skip link moved focus to the main content. The gallery supported arrow keys, Home and End, and each tab showed the corresponding image. Content remained accessible with JavaScript disabled. No horizontal overflow was observed at the tested widths. |
| Accessibility | axe checks targeting WCAG A/AA through 2.2 reported zero violations in the four pages at all four widths. Desktop and mobile layouts were visually inspected. These checks do not constitute accessibility certification or physical-device or screen-reader acceptance. |
| Requests | Browser observation found same-origin resource requests only and no JavaScript errors. The LinkedIn contact is an outbound link. The showcase includes no form, tracking client, external font or embedded third-party player. |
| Loading | A local Lighthouse 13 run on the English landing page measured performance scores of 99 on mobile and 100 on desktop. Largest Contentful Paint was 2.2 s and 0.4 s respectively, with a cumulative layout shift of 0 in both runs. These are laboratory measurements. |
| Release boundary | The runtime downloads only static presentation files. The build selects them from the explicit release inventory. The original application and its data are kept separately. |

An independent reviewer inspected the screenshots, social previews, animated excerpt, film samples, media metadata, asset licensing and publication inventory. The candidate received local secret scanning. Public hosting still requires the owner's approval and a separate live smoke test.
