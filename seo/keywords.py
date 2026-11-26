#!/usr/bin/env python3
"""Builds reports/keyword-research-v2.csv and the regional keyword maps.
Merges the original 103-row research (reports/keyword-research.csv) with the new
Dubai/UAE, Kerala, India, partnership, personal-brand and Malayalam clusters.
No search volume, difficulty or CPC is filled in: none was measurable (Ahrefs free plan
returns "Insufficient plan"; Keyword Planner and Search Console data not yet available).
Run from the project root: python3 seo/keywords.py"""
import csv

COLS = ['keyword', 'cluster', 'language', 'location', 'search_volume', 'keyword_difficulty', 'cpc', 'competition',
        'data_status', 'intent', 'priority', 'target_page', 'content_recommendation', 'notes']
NM = 'not measured'
rows = []

def add(cluster, location, intent, page, pri, kws, rec, lang='English', notes=''):
    for k in kws:
        rows.append({'keyword': k, 'cluster': cluster, 'language': lang, 'location': location, 'search_volume': NM,
                     'keyword_difficulty': NM, 'cpc': NM, 'competition': NM, 'data_status': 'Unverified opportunity',
                     'intent': intent, 'priority': pri, 'target_page': page, 'content_recommendation': rec, 'notes': notes})

UAE_NOTE = ('Do not claim she is Dubai-based or UAE-licensed. Target as "doctor-creator for UAE brands and Malayali audiences". '
            'UAE campaigns need a Media Council advertiser permit check; medical products cannot be promoted by influencers (EDE, Nov 2026).')
# A. Dubai / UAE creator
add('A Dubai and UAE creator', 'Dubai / UAE', 'Commercial investigation', '/brand-partnerships/', 'P2', [
    'doctor influencer Dubai', 'Dubai doctor influencer', 'healthcare influencer Dubai', 'medical influencer Dubai',
    'doctor content creator Dubai', 'health content creator Dubai', 'medical content creator UAE', 'healthcare content creator UAE',
    'female doctor influencer Dubai', 'female health influencer Dubai', 'doctor Instagram influencer UAE', 'Dubai health educator',
    'medical educator Dubai', 'health awareness creator Dubai', 'doctor YouTuber Dubai', 'healthcare social media creator Dubai',
    'UAE health education influencer', 'Dubai doctor Instagram collaborations', 'Malayali doctor influencer Dubai',
    'Indian doctor influencer UAE', 'Indian healthcare content creator UAE', 'Malayalam health creator Gulf'],
    'Brand partnerships page section on India, UAE and Gulf enquiries; media kit audience countries once insights are added.', notes=UAE_NOTE)
# B. Kerala creator
add('B Kerala creator', 'Kerala', 'Commercial investigation', '/brand-partnerships/', 'P1', [
    'doctor influencer Kerala', 'Kerala doctor influencer', 'healthcare influencer Kerala', 'medical influencer Kerala',
    'health content creator Kerala', 'medical content creator Kerala', 'female doctor influencer Kerala', 'Malayalam doctor influencer',
    'Malayalam health influencer', 'Malayalam health content creator', 'Kerala health educator', 'Malayalam medical educator',
    'doctor Instagram influencer Kerala', 'Kerala healthcare content creator', 'Malayalam health awareness creator',
    'health educator Malayalam', 'doctor YouTuber Kerala', 'Kannur doctor Instagram'],
    'Brand partnerships + media kit. Strongest realistic fit: she is Kerala-based. Add content languages to data/site.json.')
# C. India / international
add('C India and international', 'India', 'Commercial investigation', '/brand-partnerships/', 'P3', [
    'Indian doctor influencer', 'Indian medical influencer', 'Indian health content creator', 'female doctor content creator India',
    'Indian healthcare influencer', 'medical education content creator India', 'health awareness influencer India',
    'doctor social media creator India', 'Malayalam health creator worldwide'],
    'Broad national terms dominated by large creators and listicles. Long-term; rely on PR mentions and listings.')
# D. Partnership intent
add('D Brand partnership', 'Dubai / UAE', 'Transactional / commercial', '/brand-partnerships/', 'P2', [
    'healthcare influencer collaborations Dubai', 'doctor brand collaborations Dubai', 'medical influencer partnerships UAE',
    'healthcare brand ambassador Dubai', 'healthcare brand partnerships UAE'],
    'Brand partnerships page + FAQ on UAE campaigns and approvals.', notes=UAE_NOTE)
add('D Brand partnership', 'Kerala', 'Transactional / commercial', '/brand-partnerships/', 'P1', [
    'health influencer collaborations Kerala', 'doctor brand collaborations Kerala', 'Malayalam influencer for health brands',
    'Kerala influencer for hospital campaign'],
    'Brand partnerships page; Kerala hospital awareness-campaign case studies once real campaigns exist.')
add('D Brand partnership', 'India', 'Transactional / commercial', '/brand-partnerships/', 'P2', [
    'healthcare influencer marketing India', 'medical influencer marketing India', 'health brand collaborations India',
    'healthcare content creator for brands', 'doctor for health awareness campaigns', 'medical content creator for brands',
    'healthcare campaign influencer', 'hospital awareness campaign creator', 'health education campaign collaborations',
    'medical PR collaboration', 'doctor influencer media kit'],
    'Brand partnerships + media kit. Avoid "sponsored doctor" and drug/device endorsement framing (NMC Oct 2026, EDE Nov 2026).')
add('D Brand partnership', 'India', 'Transactional / commercial', 'not targeted', 'Do not target', [
    'doctor sponsored content creator', 'health product campaign creator', 'doctor endorsement for products'],
    'Not targeted: wording implies product endorsement by a doctor, which Indian and UAE rules restrict.')
# F. Personal brand
add('F Personal brand', 'All', 'Navigational', '/', 'P1', [
    'Athmika Prakash', 'Dr Athmika Prakash doctor', 'Dr Athmika health influencer', 'Dr Athmika medical content creator',
    'Dr Athmika Dubai', 'Dr Athmika Kerala', 'Dr Athmika Instagram', 'Dr Athmika collaborations', 'Dr Athmika media kit',
    'the.glodoc', 'The GloDoc doctor', 'The GloDoc health creator', 'theglodoc Instagram'],
    'Home, About and Media kit carry the name in titles, H1s and schema. Link the site from Instagram and YouTube bios.')
# G. Malayalam (script and transliterated) - education intent
add('G Malayalam education', 'Kerala', 'Informational', '/health-education/', 'P2', [
    'health tips Malayalam doctor', 'Malayalam health awareness video', 'Malayalam medical education', 'Malayalam doctor Instagram',
    'women health Malayalam doctor', 'medical myths Malayalam', 'health myths Malayalam',
    'ഡോക്ടർ ആരോഗ്യ ടിപ്സ്', 'ആരോഗ്യ ബോധവൽക്കരണം', 'സ്ത്രീകളുടെ ആരോഗ്യം ഡോക്ടർ', 'ആരോഗ്യ മിഥ്യാധാരണകൾ'],
    'Needs genuine Malayalam articles (calendar). Check real phrasing in Google autocomplete with a Kerala location and in Search Console before writing.',
    lang='Malayalam / transliterated', notes='Phrasing is a hypothesis, not verified against autocomplete or Search Console.')

# merge original research
with open('reports/keyword-research.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        rows.append({'keyword': r['keyword'], 'cluster': 'v1 ' + r['category'], 'language': r['language'],
                     'location': 'Kerala' if 'Kerala' in r['geo_relevance'] else r['geo_relevance'], 'search_volume': NM,
                     'keyword_difficulty': NM, 'cpc': NM, 'competition': NM, 'data_status': 'Unverified opportunity',
                     'intent': r['intent'], 'priority': r['priority'],
                     'target_page': r['target_page'].replace('/partnerships/', '/brand-partnerships/'),
                     'content_recommendation': '', 'notes': r['notes']})

seen = set(); out = []
for r in rows:
    k = r['keyword'].lower()
    if k in seen: continue
    seen.add(k); out.append(r)

def dump(path, rs):
    with open(path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, COLS); w.writeheader(); w.writerows(rs)

dump('reports/keyword-research-v2.csv', out)
dump('reports/keyword-map-dubai-uae.csv', [r for r in out if r['location'] in ('Dubai / UAE',)])
KERALA_CITIES = ('Kerala', 'Calicut', 'Kannur', 'Kochi', 'Kollam', 'Kottayam', 'Kozhikode', 'Malappuram', 'Palakkad', 'Thrissur', 'Trivandrum')
dump('reports/keyword-map-kerala.csv', [r for r in out if r['location'] in KERALA_CITIES])
dump('reports/keyword-map-india.csv', [r for r in out if r['location'] in ('India', 'All', 'Kerala / India')])
print(len(out), 'keywords;', {l: sum(1 for r in out if r['location'] == l) for l in sorted({r['location'] for r in out})})

# keyword-to-page mapping (live pages + planned articles)
MAP = [
 ('/', 'live', 'Dr Athmika Prakash', 'THEGLODOC | The GloDoc doctor | Dr Athmika Kerala | the.glodoc', 'Navigational'),
 ('/about/', 'live', 'Dr Athmika Prakash doctor', 'Dr Athmika health influencer | Athmika Prakash BHMS | Dr Athmika Instagram', 'Navigational'),
 ('/brand-partnerships/', 'live (new)', 'doctor influencer Kerala', 'Malayalam doctor influencer | healthcare content creator Kerala | doctor for health awareness campaigns | healthcare influencer collaborations Dubai | medical content creator UAE | Indian doctor influencer UAE', 'Commercial'),
 ('/media-kit/', 'live (new)', 'Dr Athmika media kit', 'doctor influencer media kit | health content creator Kerala | Malayalam health influencer', 'Commercial'),
 ('/consultations/', 'live', 'online doctor consultation Kerala', 'female doctor consultation online | skin consultation online', 'Transactional'),
 ('/health-education/', 'live', 'Malayalam health tips', 'health tips in Malayalam | health education Malayalam | medical myths Malayalam', 'Informational'),
 ('/womens-health/', 'live', "women's health Malayalam", 'സ്ത്രീകളുടെ ആരോഗ്യം | female health tips | women health Malayalam doctor', 'Informational'),
 ('/gut-health/', 'live', 'gut health Malayalam', 'digestive health | routine health tests | vitamin deficiency symptoms', 'Informational'),
 ('/skin-and-hair/', 'live', 'skin care tips Malayalam', 'hair care tips Malayalam | ചർമ്മ സംരക്ഷണം | hair fall causes', 'Informational'),
 ('/medical-cosmetology/', 'live', 'medical cosmetologist Kerala', 'cosmetic procedures Malayalam | what is medical cosmetology', 'Informational'),
 ('/videos/', 'live', 'Dr Athmika YouTube', 'Malayalam health awareness video | health videos Malayalam doctor', 'Navigational'),
 ('/editorial-policy/', 'live (new)', 'THEGLODOC editorial policy', 'trust page (E-E-A-T), not a ranking target', 'Trust'),
]
with open('reports/keyword-to-url-mapping-v2.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['target_url', 'status', 'primary_keyword', 'secondary_keywords', 'intent'])
    for u, st, pk, sk, it in MAP: w.writerow(['https://theglodoc.in' + u, st, pk, sk, it])
    with open('reports/keyword-to-url-mapping.csv', encoding='utf-8-sig') as g:
        for r in csv.DictReader(g):
            if '/articles/' in r['target_url']: w.writerow([r['target_url'], r['status'], r['primary_keyword'], r['secondary_keywords'], r['intent']])
