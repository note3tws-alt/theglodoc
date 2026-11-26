# Health article template (THEGLODOC)

Use this for every article in `reports/90-day-content-calendar.csv`. Nothing is published until Dr. Athmika has written or reviewed it.

## Brief (fill before writing)
- Search intent:
- Primary keyword:
- Supporting keywords:
- URL: `/articles/<slug>/` (English) or `/ml/articles/<slug>/` (Malayalam, only for a genuine Malayalam version; add hreflang pairs)
- SEO title (max 60 characters):
- Meta description (120 to 155 characters):
- Related video (YouTube/Instagram link):

## Page structure
1. H1: the question, in plain words (no sensational wording, no "cure", no "guaranteed").
2. Byline: "Written by Dr. Athmika Prakash, BHMS, Certified Consultant Medical Cosmetologist" + published date + "Last reviewed" date.
3. Short answer (2 to 3 sentences).
4. H2 sections from the brief. Explain what is common, what deserves attention, and when to see a doctor.
5. "When to see a doctor" box. Emergency signs go first.
6. "What the evidence says and its limits": where evidence is weak or mixed, say so.
7. Related video embed (lazy-loaded facade; click to load the player).
8. Internal links: the topic hub, one related article, /consultations/.
9. References: 2 to 5 sources (WHO, ICMR, MoHFW, NHS, national guidelines, peer-reviewed reviews). Real links only; never cite a source you have not opened.
10. Author box linking to /about/ and /editorial-policy/.
11. Disclaimer: the standard text from /medical-disclaimer/.

## Structured data (add to seo/build.py when the first article ships)
`Article` (or `MedicalWebPage` for condition explainers) with `headline`, `author` -> `#person`, `reviewedBy` -> `#person`, `datePublished`, `dateModified`, `lastReviewed`, `citation` (the references), `inLanguage` (`en-IN` or `ml-IN`), `isPartOf` -> `#website`, plus `BreadcrumbList`.
Add `VideoObject` only when the video's real title, description, upload date and thumbnail are known.

## Compliance checks before publishing
- No product, medicine or brand mentions in editorial articles.
- No patient photos, stories or testimonials without documented consent.
- No claims of cure or guaranteed results; no fear-based framing.
- Advice stays general; no individual diagnosis or dosing.
