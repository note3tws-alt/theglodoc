# THEGLODOC (theglodoc.in) - project handoff for Claude Code

Personal website + brand media kit for **Dr. Athmika Prakash** (doctor, certified consultant medical cosmetologist, health educator, creator; Kannur, Kerala). Client contact/owner: Abhishek Prakash (Dubai). Brand name is written THEGLODOC.
Instagram @the.glodoc (https://www.instagram.com/the.glodoc/, 12.3K followers), YouTube @The.glodoc (https://www.youtube.com/@The.glodoc), email drathmika999@gmail.com, "4,000+ patient consultations", online + offline.

## Design rules (keep)
White + sage green (`--sage:#4a5c4b`, `--sage-100:#e3e9dd`, `--sage-50:#f3f5f0`), Times New Roman (Tinos fallback), minimal and premium. Only the name "Dr. Athmika" animates (per-letter); consultations number counts 1 -> 4,000+. No phone/WhatsApp. No "Doctor · Creator · Vlogger" line. Hero H1: "Real health talk. With Dr. Athmika."

## Layout
- `seo/build.py`  CURRENT generator. Run from project root: `python3 seo/build.py` -> writes `site-seo/` and `glodoc-seo-deploy.zip`. Reads `backup/site/index.html` (pre-SEO homepage), `site/config.js`, `photos/`, `thumbs/`, `icons/`. Needs Pillow.
- `seo/test.js` Playwright test (serves `site-seo/` on :8099): links, one H1, JSON-LD, overflow at 390px, forms, mobile menu. `node seo/test.js` (needs `playwright`). `seo/shot.js` takes screenshots.
- `seo/docs.py` regenerates `reports/keyword-research.csv`, `keyword-to-url-mapping.csv`, `90-day-content-calendar.csv` (writes to `deliver/`; create that dir or edit the path).
- `site-seo/` built output (11 pages + 404, sitemap, robots, `_headers`, `_redirects`). `deploy-packages/glodoc-seo-deploy.zip` is the same, ready for Netlify.
- `site/` and `deploy-packages/glodoc-deploy.zip` = the single-page version live BEFORE the SEO work. `legacy/` holds the older generators (`gen/refine.py` makes the single page; `legacy/deploy.py`).
- `reports/SEO-Report.md` full audit, status, remaining tasks. Read it first.
- `site/config.js` editable values (`window.SITE`): instagramFollowers, consultations, email, URLs.

## Hosting / infra (no credentials here)
Netlify drag-and-drop deploy (zip with `index.html` at top level; team "drathmikaprakash", project theglodoc, also theglodoc.netlify.app). Netlify Forms: `partnership` and `contact` (honeypot `bot-field`; `window.GLODOC_LIVE=true` is set in the built pages so forms post to "/").
Domain theglodoc.in at Hostinger: A @ -> 75.2.60.5, CNAME www -> theglodoc.netlify.app, TXT google-site-verification (Search Console domain property `sc-domain:theglodoc.in`). Hostinger sent a domain email verification to theworldstoriez@gmail.com due 24 Nov 2026 - check it was completed.
Claude in Chrome cannot operate app.netlify.com in Dr. Athmika's profile ("Blocked"), so deploys are manual.

## State at handoff (26 Nov 2026)
- SEO build is finished and tested locally but **may not be uploaded to Netlify yet**; verify https://theglodoc.in/about/ and /sitemap.xml exist. The live site may still be the single-page version.
- After deploy: re-submit https://theglodoc.in/sitemap.xml in Search Console and request indexing for /, /about/, /consultations/, /partnerships/.
- GA4 not set up (needs Measurement ID).

## Hard rules for health/YMYL content
No invented credentials, registration numbers, testimonials, stats or medical facts; no guaranteed outcomes; no unreviewed medical articles (Dr. Athmika reviews, add WHO/ICMR/MoHFW references, author box, dates, disclaimer). No VideoObject schema until each video's upload date/title/description are known. No Physician/LocalBusiness schema without a verified registration and a real practice address. No location landing pages. Keyword volumes were NOT available (Ahrefs free plan); never fabricate them - use Keyword Planner / Search Console.

## Open items
Confirm BHMS wording, meaning of "FMC", certifying body; confirm Kannur wording and offline consultation details/fees; consider replacing "most viewed and favourite health influencer" with a measurable fact; Instagram follower auto-update would need the Instagram Login API (instagram_business_basic) + a server-side token (Netlify Function), refresh about every 60 days; Malayalam articles per the 37-row calendar.
