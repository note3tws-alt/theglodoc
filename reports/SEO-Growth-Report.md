# THEGLODOC: healthcare personal brand SEO and growth report
Prepared 26 Nov 2026 for theglodoc.in (Dr. Athmika Prakash). It builds on `reports/SEO-Report.md` (22 Nov 2026) and covers the work in this pull request. **Measured** facts are kept separate from **unverified** ones throughout.

## 1. Summary
- **Live site check (26 Nov):** theglodoc.in/about/ loads, so the 11-page SEO build from 22 Nov is deployed. Ahrefs Domain Rating is **0.0**, meaning the site is new and has no authority yet.
- **Built in this PR:**
  - a **Brand partnerships** page with a full enquiry form, at `/brand-partnerships/` (`/partnerships/` now 301-redirects there)
  - a **Media kit** page plus a **downloadable PDF**, both generated from one data file
  - **Editorial policy**, **Medical disclaimer**, **Privacy policy** and **Terms** pages
  - GA4-ready **conversion tracking**
  - credential schema
  - partnership copy rewritten for compliance
  - 192-keyword research with Dubai, Kerala and India maps
  - an article template
- **Tested:**
  - 17 pages plus the 404 page
  - one H1 per page and valid JSON-LD
  - no overflow at 390px
  - all internal links return 200
  - both forms post correctly, and the partnership form cannot be sent without the standards checkbox
  - the PDF is served
  - analytics events fire
  - local Lighthouse scores: Performance 99, Accessibility 96 to 100, Best practices 100, SEO 100. LCP is 1.6 to 1.8s, CLS 0, TBT 0ms.
- **Not deployed.** Deployment is a manual Netlify drag-and-drop of `deploy-packages/glodoc-seo-deploy.zip`, and it should wait for your review of section 9 (compliance).
- **Biggest gaps:**
  - **No measured keyword volumes.** The Ahrefs free plan still returns "Insufficient plan".
  - **No verified audience analytics.**
  - Only a little public information about Dr. Athmika exists beyond her own channels. Every missing fact is listed in section 11, and no figure was invented.

## 2. What the research found about the brand
| Item | Finding | Source / status |
|---|---|---|
| Identity | Dr. Athmika Prakash. BHMS (Bachelor of Homoeopathic Medicine and Surgery). FMC (Fellowship in Medical Cosmetology). Certified Consultant Medical Cosmetologist. Kannur, Kerala | FMC confirmed by client 26 Nov 2026; the issuing body is not confirmed |
| Type of doctor | **Homoeopathic doctor (BHMS)**, not an MBBS physician or a specialist. Her regulator is the **National Commission for Homoeopathy (NCH)**, not the NMC | Inferred from the BHMS degree. Confirm her registration (State Board / NCH register) |
| Content | Short videos on women's health, everyday and gut health, skin and hair, and medical cosmetology. Five YouTube Shorts are linked on the site | Existing site |
| Platforms | Instagram @the.glodoc (12.3K followers, per the handoff); YouTube @The.glodoc | Follower count is not re-verified (Instagram cannot be fetched from here) |
| Experience | "4,000+ patient consultations", online and offline | Given by the client; not independently verifiable |
| Languages | Not confirmed (likely Malayalam and English) | **Needed from you** |
| Audience demographics | Not available | **Needed from Instagram Insights** |
| Past brand collaborations | None found publicly | **Needed from you** |
| Media coverage | None found. A web search for her name and handle returned only a Pinterest profile | Search, 26 Nov 2026 |

**Positioning statement (now used on the site):**
> Dr. Athmika Prakash is a doctor (BHMS) and certified consultant medical cosmetologist from Kannur, Kerala. As THEGLODOC, she explains women's health, everyday health, skin and hair in short, plain-language videos for people who want health information they can trust. For healthcare organisations and responsible health brands, she offers doctor-led, education-first content that is checked for accuracy and clearly disclosed.

## 3. Architecture
| URL | Status | Purpose |
|---|---|---|
| `/` | updated | Homepage. The partnership block now shows compliant formats and links to the media kit and the full form; the quick form is now its own Netlify form, `partnership-quick` |
| `/about/` | updated | Biography and qualifications; links to the partnership pages |
| `/brand-partnerships/` | **new** (replaces `/partnerships/`, which 301-redirects) | Positioning, who she works with, formats, what she does not do, process, FAQ, full enquiry form |
| `/media-kit/` + `/media-kit/theglodoc-media-kit.pdf` | **new** | Profile, qualifications, reach, audience (when provided), pillars, formats, standards, content samples |
| `/editorial-policy/`, `/medical-disclaimer/`, `/privacy-policy/`, `/terms/` | **new** | E-E-A-T and trust pages, linked from every footer |
| `/consultations/`, `/health-education/`, 4 topic hubs, `/videos/`, `/contact/` | unchanged content, new navigation and footer | |
| `/articles/...` | planned | 37 briefs in `90-day-content-calendar.csv`. Template in `templates/ARTICLE-TEMPLATE.md` |

**Recommended against, for now:**
- `/press-and-media/`, `/health-campaigns/` and `/blog/`: there is no press coverage, no campaigns and no published articles yet. Empty pages would be thin content and would hurt trust. Add each one when it has real items. `data/site.json` already has `press` and `pastCollaborations` lists ready.
- `/dubai-healthcare-collaborations/` and `/kerala-healthcare-collaborations/`: she is not based in or licensed in Dubai, and there is no verified UAE audience data. A Dubai page would be a thin doorway page and risks implying a UAE presence. The UAE and Gulf angle sits on `/brand-partnerships/` (copy and FAQ) instead. Build a Dubai page only if her Instagram insights show a meaningful UAE audience **and** a UAE permit route is in place.
- Renaming `/health-education/` to `/health-content/`: the existing URL is fine, and renaming creates churn for no gain.

## 4. Brand partnership and enquiry system
- The full form at `/brand-partnerships/#enquiry` (Netlify form `partnership`) collects:
  - organisation, contact person, business email and company website
  - industry and country
  - enquiry type (the 10 categories from the brief)
  - objectives, target audience, deliverables and timeline
  - optional budget (INR and AED ranges)
  - additional information
  - a **required acknowledgement** that content is subject to editorial and claims review and that paid content is disclosed. This deliberately filters out low-quality enquiries.
- Spam protection is a honeypot field. Netlify also runs Akismet on form submissions.
- After a successful send, a confirmation message replaces the form button. If the send fails, an error message points to Instagram.
- **Action needed in Netlify:**
  - Under Forms > Notifications, add email notifications for the `partnership`, `partnership-quick` and `contact` forms. Without them, enquiries only appear in the Netlify dashboard.
  - Optionally add a Slack or email integration so you see enquiries quickly.
- WhatsApp was **not** added. The design rules say "No phone/WhatsApp". It is easy to add later if you change that rule.

## 5. Media kit
- `data/site.json` is now the **single source** for every fact and statistic. Edit it, then run `python3 seo/build.py`. That rebuilds the website config, the media kit page and the PDF.
- Empty values are hidden everywhere. They are never shown as placeholders on the public site.
- Fields waiting for real data:
  - `youtubeSubscribers`, `avgReelViews`, `avgReach30d`, `engagementRate`
  - `audienceTopCountries`, `audienceTopCities`, `audienceAge`, `audienceGender`
  - `contentLanguages`, `statsAsOf`, `registration`
  - `pastCollaborations`, `press`
- The PDF is A4, three pages (cover, reach and audience, working together), in the site's sage and Times design. It is generated with Playwright.

## 6. Keyword research
Files:
- `reports/keyword-research-v2.csv`: 192 keywords
- `keyword-map-dubai-uae.csv`: 27
- `keyword-map-kerala.csv`: 129
- `keyword-map-india.csv`: 36
- `keyword-to-url-mapping-v2.csv`

| | |
|---|---|
| Measured data | **None.** Ahrefs Keywords Explorer still returns "Insufficient plan" (checked 26 Nov 2026). Google Keyword Planner and Search Console were not accessible from here. |
| How rows are marked | Every volume, difficulty, CPC and competition cell says `not measured`, and `data_status` says `Unverified opportunity`. |
| Priority basis | Fit with her real profile, commercial intent, and likely competition. **Not** demand. |

**Key judgements:**
- **Kerala and Malayalam partnership terms are P1.** Examples: "doctor influencer Kerala", "Malayalam doctor influencer", "health influencer collaborations Kerala". She is genuinely Kerala-based, and these niches are thin.
- **Dubai and UAE creator terms are P2.** Each row carries a note: do not claim a Dubai base or a UAE licence. The target is "doctor-creator for UAE brands and Malayali audiences".
- **"doctor sponsored content creator", "health product campaign creator" and "doctor endorsement for products" are marked *Do not target*.** They frame her as a product endorser, which the rules in section 9 restrict.
- **Malayalam-script phrasing is a hypothesis.** Check it with Google autocomplete using a Kerala location, and in Search Console, before writing.

**To get real numbers:**
1. Paste the keyword column into Google Keyword Planner (free with any Google Ads account), set to India and to UAE separately.
2. After the site has been indexed for 2 to 4 weeks, export queries from Search Console > Performance.
3. Re-prioritise the files from those numbers.

## 7. Competitor and landscape research
| Creator / site | What we observed | Ahrefs DR |
|---|---|---|
| Dr Tanaya Narendra (Dr Cuterus) | MBBS, embryologist, sexual and menstrual health, over 1M Instagram followers. She says her content works as a "portfolio" for corporate workshops, government and NGO work, and consultancy. Awards: Health Influencer of the Year (a NITI Aayog and Ayushman Bharat-backed council) and SH24 2020 (ThePrint, Jan 2025). No dedicated website found; drcuterus.com has DR 0.2 | 0.2 |
| Dr Karan Rajan | UK surgeon, author (Penguin), event speaker. Presence runs through publisher and event pages rather than his own site | n/a (drkaranrajan.com DR 25 is not confirmed as his) |
| Dr Rekha Radhamony, Dr Garima Srivastav | Search did not find a personal website for either. The results were hospital and directory listings | n/a |
| Dr Abby Philips (The Liver Doc) | Kerala-origin hepatologist; myth-busting; large following on X | n/a |
| drmanojjohnson.com | Kerala lifestyle physician. Has condition hubs and booking. Shows a council registration number | 11.0 |
| doctorprasoon.com | Doctor, Dofody YouTube. About, Services, Advisory and Book pages | 2.2 |
| UAE doctor creators | Mostly listed on marketplaces (Collabstr, Favikon) rather than their own sites. Several are 30 Under 30 and media profiles | n/a |

**What this means for THEGLODOC:**
1. **Most doctor-creators do not have a strong partnership website.** A clear, compliant brand-partnership page and media kit is a real differentiator.
2. **The winning model is education first.** Workshops, government and NGO work, and awareness campaigns travel further than product posts. Dr Cuterus's "portfolio" approach is the clearest example.
3. **Brands are cautious.** Healthcare is ASCI's most-complained-about ad category, and the new NMC and UAE rules raise the bar. A creator who visibly states her standards is easier for a brand to say yes to.
4. **Malayalam, doctor-written explainers are an open gap.** Malayalam health queries are mostly answered by hospitals and news sites (see the 22 Nov report).

Market context (trade press; figures from unnamed sources, so use with care):
- Mid-tier doctor-creators reportedly earn ₹50,000 to ₹3.5 lakh per integration.
- About 12,400 Indian medical professionals were active creators in 2025 (Open magazine, citing Qoruz).

## 8. Technical SEO and structured data
- **Already in place:**
  - per-page titles and descriptions (validated by length in the build)
  - canonicals, Open Graph and Twitter tags, breadcrumbs
  - sitemap, now 16 URLs; robots.txt; `_headers` security headers
  - WebP images with JPG fallback, lazy loading below the fold, and the hero image preloaded
  - no client-side rendering of content
- **New:**
  - `_redirects` sends `/partnerships/`, `/collaborations/` and `/mediakit/` to their new pages
  - the PDF is cached for 1 day
  - the `Person` schema now has `hasCredential`: the BHMS degree and the cosmetology certificate
  - every new page has `WebPage`/`BreadcrumbList` schema
- **Structured data validation:** every page's JSON-LD parses, and the types and properties are standard schema.org. The Google Rich Results Test and the Schema Markup Validator need a public URL, so run them after deployment (section 12). Deliberately **not** used:
  - `Physician`, `MedicalOrganization` and `LocalBusiness`: there is no verified registration or practice address.
  - `VideoObject`: the videos' real titles, descriptions and dates are not known.
  - `FAQPage`: Google limits FAQ rich results to authoritative government and health sites. The FAQ is still visible on the page.
- **PageSpeed:** these are local Lighthouse 12.6 results on a desktop profile, not PageSpeed Insights, which needs the live URL.

| Page | Performance | Accessibility | Best practices | SEO | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|
| `/` | 99 | 96 | 100 | 100 | 1.8 s | 0 | 0 ms |
| `/brand-partnerships/` | 99 | 96 → fixed | 100 | 100 | 1.7 s | 0 | 0 ms |
| `/media-kit/` | 99 | 100 | 100 | 100 | 1.6 s | 0 | 0 ms |

The only accessibility issue was low contrast on the "(optional)" form labels. It is fixed in this PR.
- **hreflang:** not added, because there is no Malayalam version yet. Add `en-IN`/`ml-IN` pairs when real Malayalam pages exist.

## 9. Medical advertising and professional compliance (needs your review before deployment)
**Important: I am not a lawyer. These are findings from public sources, labelled by source type. Have the partnership language checked by someone qualified in Indian and UAE healthcare advertising before you rely on it commercially.**

**India**
1. **NCH (Professional Conduct, Etiquette and Code of Ethics) Regulations, 2022** apply to homoeopathic practitioners. Read from the NCH PDF (primary source).
   - Reg 8: soliciting patients through advertisements is unethical. No publicity tied to manufacturers or traders the doctor is connected with. No "objectionable claims" on e-platforms.
   - Reg 36 (misconduct) includes:
     - publishing patient photos or case details without consent
     - publicly displaying fee scales
     - claiming specialist status without a listed qualification
     - advertising facilities that are not offered
   - **Impact on the site:**
     - fees stay "on request", and that is how they are shown now
     - no testimonials or before-and-after images
     - "consultant medical cosmetologist" should match a recognised certificate. **Please confirm the certifying body.**
   - The PDF's wording on writing about health in the media was partly unreadable. Check the gazette version.
2. **NMC Guidelines on Ethical Advertising and Public Communication (Oct 2026)**, from trade press. They reportedly ban:
   - commercial endorsement of drugs, health formulations and devices
   - paid reviews and before-and-after images
   - superlatives

   These rules cover NMC-registered (allopathic) doctors. AYUSH practitioners follow their own councils' rules. The site's partnership standards follow these rules anyway, as a safe baseline.
3. **ASCI influencer guidelines (Addendum, April 2025):**
   - Health claims in ads need a qualified person.
   - The qualification must be disclosed up front.
   - Paid content must be labelled prominently at the start.
   - **Impact:** her claims must stay within her qualification, and every paid post needs a clear "Paid partnership / #ad" label at the start.

**UAE**
4. **DHA social media medical advertising standard.** Reported as circular CIR-2026-00000144, issued 17 Aug 2026 according to one secondary source; other reports say August 2026. It applies to DHA-licensed facilities, professionals and the influencers promoting them in Dubai. It bans absolute claims ("best", "100%", "guaranteed", "no side effects") and fear-based marketing, and requires written patient consent. **She is not DHA-licensed.** Promoting a Dubai clinic would bring her under this standard through that clinic.
5. **Emirates Drug Establishment, 19 Nov 2026** (The National). It restated the ban on advertising, promoting or endorsing **medical products** through social media influencers. All such ads need EDE approval.
6. **UAE Media Council advertiser permit.** Mandatory under Federal Media Law No. 55 of 2023, from 2025/2026 (sources disagree on the exact date). It covers paid and unpaid promotion by people creating content in the UAE, and visitors need a visitor permit through a licensed agency. Whether it applies to a creator posting from India to UAE audiences is **not clear** from the sources. **Confirm this before taking a UAE-paid campaign.**

**Compliance changes made on the site**
- **Product endorsement removed from the lead.** Partnership formats now lead with awareness campaigns, education series, interviews and podcasts, and events. "Product education" is limited to wellness, skincare and haircare, labelled, and reviewed.
- **"What she does not do" section added**, on the partnership page and in the media kit:
  - no prescription medicines, drugs or devices
  - no cure or guarantee claims and no superlatives
  - no testimonials or before-and-after images without consent
  - no fear-based messaging
  - no unsupported supplements
  - no undisclosed paid content
- **UAE approvals step added to the process.** UAE campaigns proceed only once the required permits and approvals are in place.
- **Editorial policy** keeps paid content separate from editorial content.

**Items for you to decide or confirm**
- **Hero line: "People's most viewed and favourite health influencer."** This is an unsubstantiated superlative. ASCI, the NMC-style rules and the DHA standard all treat this kind of claim as risky. **Recommend replacing it** with a measurable line. It has been left unchanged because it was your earlier request.
- **"FMC" = Fellowship in Medical Cosmetology** (confirmed 26 Nov). Now spelled out on the About page, the media kit and in schema. Still needed: the issuing body.
- **Is Dr. Athmika willing to do product education at all?** If not, remove that format from `seo/pages_growth.py`.
- **Medical cosmetology procedures.** A homoeopath performing aesthetic procedures may be restricted in some states. Confirm what she actually performs, versus explains, before any procedure-related partnership.

## 10. Analytics and conversion tracking
- `app.js` pushes these events to `dataLayer` and loads GA4 only when `ga4Id` is set in `data/site.json`:
  - `generate_lead` (any form)
  - `partnership_enquiry` (the full form)
  - `file_download` (media kit PDF)
  - `email_click`, `instagram_click`, `youtube_click`, `whatsapp_click`
  - `portfolio_video_click`
- **Setup (about 10 minutes):**
  1. Create a GA4 property and copy the Measurement ID (G-XXXXXXX).
  2. Put the ID in `data/site.json` → `ga4Id`, then rebuild and redeploy.
  3. In GA4 > Admin > Events, mark `partnership_enquiry` and `generate_lead` as **key events**.
  4. Link GA4 to Search Console.
- **Monthly dashboard.** Build it in Looker Studio (free) from GA4 and Search Console. Pages:
  - organic clicks, impressions and average position
  - top queries and landing pages
  - country split: India, UAE, other. City split: Kerala cities, Dubai
  - media kit downloads
  - partnership enquiries, and enquiries ÷ sessions on `/brand-partnerships/` (enquiry conversion rate)

  Keep a separate monthly log of **real** enquiries (date, organisation, type, outcome), because form submissions include spam and patients. No dashboard was built here, because there is no data yet and none should be invented.

## 11. Information needed from you
1. **Instagram Insights** (last 30 or 90 days), with the date you took them:
   - followers
   - average Reel views and average reach
   - engagement rate
   - top countries and cities
   - age and gender split
2. **YouTube subscribers.**
3. **Content languages**, e.g. Malayalam and English.
4. **Registration details:** council, number, and whether to show them. Also the issuing body for the FMC and the cosmetology certificate.
5. **Past brand collaborations, talks and campaigns** she is happy to list, and any **press or interviews**.
6. **Whether she does product education at all**, and any categories she refuses.
7. **GA4 Measurement ID.**
8. **Video details** (title, date, one-line summary) for each featured video. These are needed for VideoObject schema and video pages.
9. **Offline consultation location and days**, if she wants them shown. Fees stay private.

## 12. Google Search Console setup (after deployment)
1. Search Console → property `sc-domain:theglodoc.in` (already verified).
2. Sitemaps → submit `https://theglodoc.in/sitemap.xml` (now 16 URLs). Remove the old sitemap entry if it still shows "Couldn't fetch".
3. URL Inspection → Request indexing for:
   - `/`
   - `/about/`
   - `/brand-partnerships/`
   - `/media-kit/`
   - `/consultations/`
4. Check Pages → "Page with redirect" shows `/partnerships/` (expected).
5. Run the [Rich Results Test](https://search.google.com/test/rich-results) on `/` and `/about/`, and [PageSpeed Insights](https://pagespeed.web.dev/) on `/` and `/brand-partnerships/`. Record the results here.
6. After 4 weeks: Performance → filter by country (India, UAE) → export queries for keyword re-prioritisation.

## 13. 90-day SEO execution roadmap
**Weeks 1 to 2 (foundation)**
1. Review section 9, then deploy the zip.
2. Do the Search Console steps above.
3. Add GA4.
4. Set up Netlify form notifications.
5. Put theglodoc.in in the Instagram and YouTube bios.
6. Fill in `data/site.json` with real insights and rebuild the media kit.

**Weeks 3 to 6 (content and proof)**
1. Publish the first 4 to 6 articles from the calendar. Each one must be reviewed by Dr. Athmika and include references.
2. Add 2 to 3 real collaboration or talk entries.
3. Pitch 3 Kerala outlets (Onmanorama health, Mathrubhumi, Asianet News health) with expert-comment offers.

**Weeks 7 to 10 (authority)**
1. Pitch podcasts and college and corporate talks.
2. Approach hospital education teams in Kerala for awareness-day content, such as World PCOS Awareness Month in September and Breast Cancer Awareness Month in October.
3. Create a `/press-and-media/` page once there are 2 or more real items.

**Weeks 11 to 13 (measure and adjust)**
1. Pull Search Console and Keyword Planner data.
2. Re-prioritise the keyword files.
3. Review the enquiry log.
4. Decide on a Malayalam section and on a UAE page using real audience data.

## 14. Prioritised next actions
1. Review and approve the compliance items in section 9, especially the hero superlative.
2. Deploy `deploy-packages/glodoc-seo-deploy.zip` to Netlify.
3. Turn on Netlify form email notifications.
4. Search Console: submit the sitemap and request indexing.
5. Send the Instagram Insights figures and content languages, then rebuild the media kit.
6. Add the GA4 ID.
7. Link the website from Instagram and YouTube. This is the highest-value free backlink.
8. Start the reviewed article programme, with Malayalam first.
9. Begin PR outreach for genuine editorial mentions. No paid links.

No ranking is guaranteed. A DR 0 site needs consistent, reviewed content and genuine mentions over months. Branded and Kerala partnership searches are the first realistic wins.

## Sources consulted
- NCH Code of Ethics 2022 (PDF): https://nch.org.in/upload/professional_conduct_etiquette_and_code_of_ethics_compressed.pdf
- DHA standard (secondary sources):
  - https://abspartners.ae/dha-standards-for-medical-advertising/
  - https://insurancepolicy.ae/uncategorized/dubai-tightens-social-media-rules-for-doctors-healthcare-facilities-and-influencers-what-uae-residents-need-to-know/
  - https://www.lexisnexis.com/blogs/ae-legal/b/insights/posts/dubai-health-authority-bans-exaggerated-medical-advertising-on-social-media
- EDE: https://www.thenationalnews.com/news/uae/2026/11/19/uae-drug-regulator-bans-social-media-influencers-from-promoting-medical-products/
- UAE advertiser permit:
  - https://gulfnews.com/uae/new-uae-law-advertiser-permit-now-mandatory-for-influencers-and-creators-for-social-media-1.500427938
  - https://www.tamimi.com/law-update/technology-edition/articles/uae-introduces-mandatory-advertiser-permit-for-content-creators/
- NMC guidelines (trade press):
  - https://www.exchange4media.com/influence-zone-news/national-medical-body-cracks-down-on-influencers-what-it-means-for-health-brands-159150.html
  - https://mapmyclinic.com/compliance/india-nmc-advertising-rules/
- ASCI: https://www.legal500.com/intelligence/india/media-telecoms-it-entertainment/asci-update-to-influencer-advertising-guidelines-qualification-mandatory-for-making-claims-related-to-technical-aspects-of-health-nutrition-and-finance
- Landscape:
  - https://theprint.in/health/the-age-of-health-fluencers-blending-humour-expertise-to-bust-myths-promote-health-literacy/2452599/
  - https://openthemagazine.com/india/from-clinics-to-clicks-why-indias-doctors-are-becoming-influencers-2
