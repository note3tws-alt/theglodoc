# THEGLODOC (theglodoc.in) - project handoff for Claude Code

Personal website + brand media kit for **Dr. Athmika Prakash** (doctor, certified consultant medical cosmetologist, health educator, creator; Kannur, Kerala). Client contact/owner: Abhishek Prakash (Dubai). Brand name is written THEGLODOC.
Instagram @the.glodoc (https://www.instagram.com/the.glodoc/, 12.3K followers), YouTube @The.glodoc (https://www.youtube.com/@The.glodoc), email drathmika999@gmail.com, "4,000+ patient consultations", online + offline.

## Design rules (keep)
White + sage green (`--sage:#4a5c4b`, `--sage-100:#e3e9dd`, `--sage-50:#f3f5f0`), Times New Roman (Tinos fallback), minimal and premium. Only the name "Dr. Athmika" animates (per-letter); consultations number counts 1 -> 4,000+. No phone/WhatsApp. No "Doctor · Creator · Vlogger" line. Hero H1: "Real health talk. With Dr. Athmika."

## Layout
- `data/site.json` SINGLE SOURCE for every editable fact/statistic (followers, audience insights, languages, GA4 ID, collaborations, press). Empty values are hidden on the site and PDF, never shown as placeholders.
- `seo/build.py`  CURRENT generator. Run from project root: `python3 seo/build.py` -> writes `site-seo/` (incl. generated `config.js` and media kit PDF) and `deploy-packages/glodoc-seo-deploy.zip`. Reads `backup/site/index.html` (pre-SEO homepage), `data/site.json`, `photos/`, `thumbs/`, `icons/`. Needs Pillow, node + playwright (for the PDF).
- `seo/pages_growth.py` (exec'd by build.py): /brand-partnerships/, /media-kit/ (+ PDF via `seo/pdf.js`), /editorial-policy/, /medical-disclaimer/, /privacy-policy/, /terms/. Partnership copy follows the compliance findings in `reports/SEO-Growth-Report.md` section 9.
- `seo/keywords.py` regenerates `reports/keyword-research-v2.csv`, regional maps and `keyword-to-url-mapping-v2.csv`.
- `templates/ARTICLE-TEMPLATE.md` structure, schema and compliance checklist for health articles.
- `seo/test.js` Playwright test (serves `site-seo/` on :8099): links, one H1, JSON-LD, overflow at 390px, forms, mobile menu. `node seo/test.js` (needs `playwright`). `seo/shot.js` takes screenshots.
- `seo/docs.py` regenerates `reports/keyword-research.csv`, `keyword-to-url-mapping.csv`, `90-day-content-calendar.csv` (writes to `deliver/`; create that dir or edit the path).
- `site-seo/` built output (11 pages + 404, sitemap, robots, `_headers`, `_redirects`). `deploy-packages/glodoc-seo-deploy.zip` is the same, ready for Netlify.
- `site/` and `deploy-packages/glodoc-deploy.zip` = the single-page version live BEFORE the SEO work. `legacy/` holds the older generators (`gen/refine.py` makes the single page; `legacy/deploy.py`).
- `reports/SEO-Growth-Report.md` (26 Nov 2026) latest report: compliance findings, missing info, roadmap. Read it first. `reports/SEO-Report.md` is the earlier 22 Nov audit.
- `site/config.js` editable values (`window.SITE`): instagramFollowers, consultations, email, URLs.

## Hosting / infra (no credentials here)
Netlify drag-and-drop deploy (zip with `index.html` at top level; team "drathmikaprakash", project theglodoc, also theglodoc.netlify.app). Netlify Forms: `partnership` (full form on /brand-partnerships/), `partnership-quick` (homepage) and `contact` (honeypot `bot-field`; `window.GLODOC_LIVE=true` is set in the built pages so forms post to "/").
Domain theglodoc.in at Hostinger: A @ -> 75.2.60.5, CNAME www -> theglodoc.netlify.app, TXT google-site-verification (Search Console domain property `sc-domain:theglodoc.in`). Hostinger sent a domain email verification to theworldstoriez@gmail.com due 24 Nov 2026 - check it was completed.
Claude in Chrome cannot operate app.netlify.com in Dr. Athmika's profile ("Blocked"), so deploys are manual.

## State (26 Nov 2026)
- The 11-page SEO build is live (verified /about/ on 26 Nov). The growth pages (brand partnerships, media kit, trust pages) are built and tested but NOT deployed yet; deploy after the client reviews report section 9.
- After deploy: re-submit https://theglodoc.in/sitemap.xml in Search Console and request indexing for /, /about/, /consultations/, /partnerships/.
- GA4 not set up (needs Measurement ID).

## Hard rules for health/YMYL content
No invented credentials, registration numbers, testimonials, stats or medical facts; no guaranteed outcomes; no unreviewed medical articles (Dr. Athmika reviews, add WHO/ICMR/MoHFW references, author box, dates, disclaimer). No VideoObject schema until each video's upload date/title/description are known. No Physician/LocalBusiness schema without a verified registration and a real practice address. No location landing pages (no Dubai page unless real UAE audience data + permit route). She is BHMS (homoeopathy, regulated by NCH): never imply MBBS/specialist/UAE licence. Partnerships: no drug/device/medicine endorsement, no superlatives, paid content always disclosed. Keyword volumes were NOT available (Ahrefs free plan); never fabricate them - use Keyword Planner / Search Console.

## Open items
FMC = Fellowship in Medical Cosmetology (confirmed 26 Nov 2026); still confirm BHMS wording and the FMC issuing body; confirm Kannur wording and offline consultation details/fees; consider replacing "most viewed and favourite health influencer" with a measurable fact; Instagram follower auto-update would need the Instagram Login API (instagram_business_basic) + a server-side token (Netlify Function), refresh about every 60 days; Malayalam articles per the 37-row calendar.
