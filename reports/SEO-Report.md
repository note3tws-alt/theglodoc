# THEGLODOC SEO project report
Prepared 22 Nov 2026 for theglodoc.in (Dr. Athmika Prakash). Everything below separates what was **done and tested** from what is **blocked or needs a person**.

## 1. What was done, at a glance
- Rebuilt the single-page site into **11 crawlable pages** (home, about, consultations, health education hub, 4 topic hubs, videos, partnerships, contact) plus a 404 page, keeping the existing sage/Times design, count-up, name animation and enquiry form.
- Added per-page titles, descriptions, canonicals, Open Graph/Twitter tags, breadcrumbs, JSON-LD schema, sitemap (11 URLs), robots.txt, security headers and redirects.
- Converted images to WebP with JPG fallback and descriptive file names; created a 1200x630 share image.
- Produced a keyword research file (103 keywords), keyword-to-URL mapping, and a 37-article content calendar (3 per week, 30 Nov 2026 to 22 Feb 2027).
- Tested locally: all internal links return 200, one H1 per page, JSON-LD parses on every page, no horizontal overflow at 390px, no broken images, forms post correctly, mobile menu works.
- **Not deployed yet.** The package `glodoc-seo-deploy.zip` must be uploaded to Netlify (my browser access to Netlify is blocked in Dr. Athmika's Chrome).

## 2. Audit of the site before changes
**Strengths:** clean HTML, fast (no framework, about 23 KB page), HTTPS, content is plain server-rendered HTML so JavaScript does not hide it from Google, mobile layout works, working form, domain serves correctly, Search Console verified and sitemap submitted.

**Problems found:**
1. One URL only: no pages for Google to rank for consultations, women's health, skin, partnerships, etc.
2. No canonical tag in the page content, no Twitter tags, no structured data, og:image was a 980x1280 portrait (wrong ratio for sharing).
3. Weak H1 for search: "Real health talk. With Dr. Athmika." carries no keyword. (Kept for design; the hero line below it and the page title now carry the name and role.)
4. Section labels (Consultations, Focus, Partnerships, Enquiry) were not headings.
5. No internal links, no breadcrumbs, no 404 page, no robots/sitemap beyond the single URL.
6. Images were generically named (portrait.jpg, video-1.jpg) with no WebP.
7. Content gaps: no Malayalam content, no articles, no About/credentials page, no consultation explanation, no limits/disclaimer text.
8. Indexing: a search for `site:theglodoc.in` returned no results on 22 Nov 2026, and a brand search returned other doctors, so the site is new and not yet indexed. Domain Rating (Ahrefs) is 0.0.

## 3. Keyword research: what could and could not be done
**Blocked:** Ahrefs Keywords Explorer returned "Insufficient plan" (Free plan), Google Keyword Planner and Google Trends were not accessible, and Search Console has no data yet (site brand new). **No search volumes or difficulty scores were fabricated:** every row in `keyword-research.csv` says `unavailable`.

**What the file does contain:** 103 keywords across your categories A to H, with language (English, transliterated, Malayalam script), intent, geography, target page, a P1/P2/P3 judgement priority, and notes. Priority is based on relevance to Dr. Athmika, intent and likely competition, **not on measured demand**. To get real numbers: (a) open Google Keyword Planner (free with any Google Ads account) and paste column A, (b) after 2 to 4 weeks, use Search Console > Performance to see real queries, (c) upgrade Ahrefs/Semrush if you want difficulty scores.

**Observed SERP signals (from web searches, not volume data):** for PCOS Malayalam searches the results were Star Health (Malayalam pages), Asianet News and Continental Hospitals (Malayalam pages). Malayalam health queries are served mostly by hospitals and news sites, which suggests a doctor-authored, Malayalam article from a named expert is a realistic gap.

## 4. Competitors (public data only)
| Site | What it is | Observed | Ahrefs Domain Rating |
|---|---|---|---|
| drmanojjohnson.com | Lifestyle physician, WordPress/Elementor | Hub of 14 condition pages, articles, diet charts, booking, shop. Shows Kerala Medical Council reg. no. and follower counts. English only, no visible schema or disclaimer, "most renowned" superlative claim in meta description | 11.0 |
| doctorprasoon.com | Doctor, Dofody YouTube (500k+ subs), book and advisory | About, Services, Advisory, Book pages. No blog structure, English only, no disclaimers visible | 2.2 |
| onmanorama.com, asianetnews.com, starhealth.in/ml, continentalhospitals.com/ml | Media and hospital sites | Rank for Malayalam condition queries | onmanorama 73.0 |
| theglodoc.in | This site | New, not indexed | 0.0 |

I did not analyse Dr. Hernold Paul E. or Doc on the Move in depth, and backlink, keyword and traffic data for competitors is unavailable on the Free Ahrefs plan.

**Realistic gaps for THEGLODOC:** (1) Malayalam-language, doctor-authored explainers (competitors are mostly English or generic hospital pages), (2) women's health and skin/hair as a personal-brand niche, (3) visible trust signals and disclaimers (both competitors show few), (4) consultation + partnership pages optimised for their own intents, (5) linking each article to a matching YouTube Short.

## 5. Website architecture (live in the package)
```
/                      Home (ProfilePage + Person + Organization + WebSite)
/about/                About Dr. Athmika (ProfilePage)
/consultations/        Online and offline consultations, limits, how to enquire
/health-education/     Hub (CollectionPage)
  /womens-health/  /gut-health/  /skin-and-hair/  /medical-cosmetology/
/videos/               5 videos linked to YouTube
/partnerships/         Brand partnership page + form
/contact/              Contact form
/404.html              noindex
```
Planned (not published, see section 9): `/articles/...` pages from the content calendar.

## 6. Titles and meta descriptions (all unique)
| URL | Title | Meta description |
|---|---|---|
| / | Dr. Athmika Prakash | Doctor & Health Educator | THEGLODOC | Meet Dr. Athmika Prakash, a doctor and health educator in Kerala sharing clear insights on women's health, gut health, skin, hair and everyday wellness. |
| /about/ | About Dr. Athmika Prakash | Doctor & Health Educator | Dr. Athmika Prakash is a doctor, certified consultant medical cosmetologist and health educator in Kerala, sharing clear everyday health education as THEGLODOC. |
| /consultations/ | Online & Offline Consultation | Dr. Athmika Prakash | Consult Dr. Athmika Prakash, a doctor and certified consultant medical cosmetologist, online or in person. 4,000+ consultations completed. See how to enquire. |
| /health-education/ | Health Education by Dr. Athmika | Women&#x27;s, Gut, Skin | Clear health education from Dr. Athmika Prakash: women's health, gut and everyday health, skin and hair, and medical cosmetology. Watch her videos. |
| /womens-health/ | Women&#x27;s Health Education | Dr. Athmika Prakash | Women's health explained by Dr. Athmika Prakash: periods, hormones, health checks before marriage, pregnancy myths and when to see a doctor. |
| /gut-health/ | Gut & Everyday Health Education | Dr. Athmika Prakash | Gut health, digestion, routine tests, vitamin levels and thyroid explained in simple language by Dr. Athmika Prakash, a doctor and health educator. |
| /skin-and-hair/ | Skin & Hair Health Education | Dr. Athmika Prakash | Skin and hair concerns explained by Dr. Athmika Prakash, a certified consultant medical cosmetologist: pigmentation, hair fall, myths and what to ask a doctor. |
| /medical-cosmetology/ | Medical Cosmetology Education | Dr. Athmika Prakash | Understand medical cosmetology with Dr. Athmika Prakash, a certified consultant medical cosmetologist: what procedures involve, who they suit and what to ask. |
| /videos/ | Health Videos by Dr. Athmika Prakash | YouTube Shorts | Watch short health videos by Dr. Athmika Prakash on women's health, health checks, skin and everyday wellness. Follow THEGLODOC on YouTube and Instagram. |
| /partnerships/ | Brand Collaborations with Doctor Creator | THEGLODOC | Partner with Dr. Athmika Prakash (THEGLODOC), a doctor and health creator, for health, wellness, skincare and haircare campaigns on Instagram and YouTube. |
| /contact/ | Contact Dr. Athmika Prakash | Consultations & Partnerships | Contact Dr. Athmika Prakash (THEGLODOC) to enquire about a consultation, a brand partnership or a media request. Email, Instagram and enquiry form. |

Lengths: titles 46 to 58 characters, descriptions 140 to 160.

## 7. Technical implementation
| Item | Status |
|---|---|
| Canonical on every page | Done (https://theglodoc.in/..., trailing slash) |
| XML sitemap | Done: 11 URLs, referenced in robots.txt. **Must be re-submitted in Search Console after deploy** (the old sitemap only had 1 URL) |
| robots.txt | Done: allow all + sitemap line |
| HTTPS | Already on (Netlify). Check "Force HTTPS" in Netlify Domain settings |
| Redirects | `_redirects`: /index.html and /home go to /. www to apex is handled by Netlify's primary domain setting (confirm theglodoc.in is the primary domain) |
| 404 page | Done, noindex |
| Breadcrumbs | Visible + BreadcrumbList schema on all inner pages |
| Open Graph + Twitter | Done, 1200x630 share image |
| Images | WebP + JPG fallback via `<picture>`, descriptive filenames, width/height set, hero preloaded, others lazy |
| Fonts | System Times New Roman first; Tinos (Google Fonts) only as fallback, with preconnect and display=swap |
| JavaScript | One small file (3 KB). All content is in the HTML, so rendering does not affect indexing |
| Security headers | `_headers`: nosniff, referrer policy, frame, permissions policy, 30-day image cache |
| Page weight | Home first load about 59 KB (HTML, CSS, JS, hero image), 5 thumbnails lazy-loaded at about 8 to 13 KB each as WebP |

**Performance caveat:** I could not run Lighthouse/PageSpeed against the live site (my network cannot reach theglodoc.in and PageSpeed is not on the allowlist). Run https://pagespeed.web.dev for the home page after deploy and send me the result. Based on size and structure I expect a good score, but that is an expectation, not a measurement.

## 8. Structured data implemented
- Person (Dr. Athmika Prakash): name, jobTitle, image, email, location (Kannur, Kerala), knowsAbout, sameAs (Instagram, YouTube).
- Organization (THEGLODOC) and WebSite.
- ProfilePage (home and About), CollectionPage (hubs, videos), ContactPage, WebPage, BreadcrumbList.
- **Deliberately not added:** Physician/LocalBusiness (needs a verified registration number and a real practice address), VideoObject (Google requires an upload date, title and description for each video; I could not read them from YouTube, so I would have had to guess), Article (no articles yet), reviews/ratings.
- Validation: every JSON-LD block parses on every page. I could not run Google's Rich Results Test (not reachable); please test the home page at https://search.google.com/test/rich-results after deploy.

## 9. What I intentionally did not publish
The brief says not to publish unreviewed machine-written medical content. So:
- The four topic pages are short orientation pages (what is covered, the questions to be answered, disclaimers, links, related videos). They make **no medical claims**.
- The 37 calendar articles (`90-day-content-calendar.csv`) are briefs (title, meta, H1, H2s, keywords, links, CTA). Each should be drafted or reviewed by Dr. Athmika, with 2 to 3 references from WHO, ICMR, MoHFW or peer-reviewed sources, an author box with credentials, published and updated dates, and the disclaimer.
- No video pages: I could not read the videos' titles or descriptions from YouTube, and I will not invent summaries. Send the transcript/caption or a short summary per video and I will build them with VideoObject schema.
- No location pages (Kochi, Calicut, etc.): she has no practice there. These cities are covered through Kerala-wide content.

## 10. Search Console and Analytics status
- Search Console: **connected and verified** (domain property, TXT record). Old 1-URL sitemap submitted; it showed "Couldn't fetch" immediately after submission and I could not recheck (the tab froze).
- **To do after deploy:** re-submit sitemap.xml, use URL Inspection > Request indexing for the home page, /about/, /consultations/, /partnerships/.
- Google Analytics 4: **not set up**. It needs her Google account and a Measurement ID (G-XXXX). Send me the ID and I will add the tag and enquiry-form events.

## 11. Backlink and authority plan (legitimate only)
1. Link from her Instagram bio and YouTube channel About page to theglodoc.in (immediate, highest value, free).
2. Add the site to YouTube video descriptions and Instagram highlights.
3. Kerala media and health sites: offer expert quotes or contributions (Onmanorama health, Asianet News health, Mathrubhumi, Manorama Online).
4. Podcast and interview guest spots, collaborations with other Kerala creators and brands that already link to partners.
5. Genuine professional directories only after she confirms registration details.
6. No bought links, no link exchanges.

## 12. Changes made to the codebase
New generator `seo/build.py` (rebuilds everything from the backed-up homepage), output `site-seo/` and `glodoc-seo-deploy.zip`. Homepage changes: head metadata and schema; new nav and mobile menu; "Focus" items became links to topic pages; consultations and partnership links added; footer expanded with link groups; images now `<picture>` with WebP; hero line under the headline now reads "Dr. Athmika Prakash · BHMS, FMC · Kannur, Kerala"; "More on YouTube" became "All videos". Scripts and styles moved to shared `styles.css` and `app.js`. The previous version is backed up in `backup/`.

## 13. Remaining manual tasks that need you or Dr. Athmika
1. **Upload `glodoc-seo-deploy.zip` to Netlify** (Deploys > drag and drop). Then re-submit the sitemap in Search Console.
2. **Confirm credentials before they go further:** exact BHMS wording, what "FMC" stands for, the certifying body for medical cosmetology, and her medical registration number if she wants it shown. The About page currently states BHMS and Certified Consultant Medical Cosmetologist only.
3. **Confirm location wording:** the site says she is based in Kannur, Kerala. Offline consultation location, days and fees are not published because I do not have them.
4. **Review claims on the site:** "People's most viewed and favourite health influencer" in the hero is a superlative you asked for, but Google and advertising rules treat unsubstantiated "most viewed/favourite" claims as risky. I suggest replacing it with a measurable fact (for example "12.3K Instagram followers"). Also confirm the partnership text "product details and claims are reviewed with the brand before anything is published" matches how she works.
5. **Hostinger domain email verification** (sent to theworldstoriez@gmail.com) must be clicked by 24 Nov 2026 or the domain is suspended.
6. Provide: GA4 Measurement ID, video titles/dates/summaries, Instagram audience insights (country, age, gender) for the media kit, and any past brand collaborations she wants listed.
7. Approve the article topics, then have her review each draft before publishing.
8. Get real keyword volumes (Keyword Planner) and review Search Console after 2 to 4 weeks, then I will re-prioritise the calendar.

## 14. Honest expectations
No ranking is promised. A new domain with Domain Rating 0 usually needs weeks to be indexed and months of consistent, reviewed content and links before competing for Malayalam health queries. Brand searches (Dr Athmika Prakash, THEGLODOC) are the first realistic wins.
