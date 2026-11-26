import csv, datetime
# Volume/difficulty are deliberately "unavailable": the Ahrefs plan here is Free (Keywords Explorer returned "Insufficient plan"), no Keyword Planner / Search Console data yet.
NA='unavailable'
H=['keyword','category','language','search_volume','difficulty','intent','geo_relevance','target_page','priority','notes']
R=[]
def add(cat,lang,intent,page,pri,kws,geo='Kerala / India',note=''):
    for k in kws: R.append([k,cat,lang,NA,NA,intent,geo,page,pri,note])
add('A Personal brand','English','Navigational / branded','/','P1',['Dr Athmika Prakash','Dr Athmika','The Glodoc','THEGLODOC','The Glodoc doctor','Dr Athmika Kerala'],note='Branded; no competition expected. Confirm demand in Search Console after indexing.')
add('A Personal brand','English','Navigational / branded','/about/','P1',['Dr Athmika health tips','Dr Athmika Instagram','Dr Athmika YouTube'])
add('A Personal brand','English','Commercial','/partnerships/','P1',['Malayalam doctor influencer','female doctor influencer Kerala','healthcare content creator Kerala'])
add('B Malayalam health education','English (transliterated)','Informational','/health-education/','P1',['Malayalam health tips','health tips in Malayalam','doctor health tips Malayalam','health awareness Malayalam','health education Malayalam','health facts Malayalam','medical advice Malayalam'],note='Hub target; individual articles per calendar.')
add('B Malayalam health education','English (transliterated)','Informational','/womens-health/','P1',["women's health Malayalam"])
add('B Malayalam health education','English (transliterated)','Informational','/skin-and-hair/','P1',['skin care tips Malayalam','hair care tips Malayalam','skin care Malayalam'])
add('B Malayalam health education','English (transliterated)','Informational','/gut-health/','P1',['hormone health Malayalam','gut health Malayalam'])
add('B Malayalam health education','Malayalam script','Informational','/health-education/','P2',['ആരോഗ്യ ടിപ്സ്','ആരോഗ്യ വിവരങ്ങൾ','ആരോഗ്യ സംശയങ്ങൾ'],note='Needs Malayalam articles (calendar). Check Malayalam autocomplete in Search Console.')
add('B Malayalam health education','Malayalam script','Informational','/womens-health/','P1',['സ്ത്രീകളുടെ ആരോഗ്യം','ഹോർമോൺ പ്രശ്നങ്ങൾ'])
add('B Malayalam health education','Malayalam script','Informational','/skin-and-hair/','P1',['ചർമ്മ സംരക്ഷണം','മുടി സംരക്ഷണം'])
add('B Malayalam health education','Malayalam script','Informational','/gut-health/','P1',['വയറിന്റെ ആരോഗ്യം'])
add('C Womens health','English','Informational','/womens-health/','P1',["women's health Kerala",'female health tips','hormonal imbalance symptoms','menstrual health','female reproductive health','women\'s health checkup'])
add('C Womens health','English / Malayalam','Informational','/articles/pcos-malayalam/','P1',['PCOS Malayalam','PCOD Malayalam','PCOS symptoms and causes','PCOS എന്താണ്'],note='Competitors seen ranking: Star Health (ml), Asianet News, Continental Hospitals (ml) in a web search.')
add('C Womens health','English / Malayalam','Informational','/articles/irregular-periods-causes/','P1',['irregular periods causes','ക്രമരഹിതമായ ആർത്തവം'])
add('C Womens health','English / Malayalam','Informational','/articles/pregnancy-myths/','P2',['pregnancy myths Malayalam','ഗർഭധാരണം തെറ്റിദ്ധാരണകൾ'])
add('C Womens health','English','Informational','/articles/menopause-symptoms/','P3',['menopause symptoms'],note='Broad national keyword; very competitive. Long-term.')
add('D Gut and general health','English','Informational','/gut-health/','P1',['digestive health','gut microbiome','lifestyle diseases Malayalam','health checkup Malayalam','routine health tests'])
add('D Gut and general health','English','Informational','/articles/bloating-causes/','P2',['bloating causes','acidity Malayalam','constipation causes'])
add('D Gut and general health','English / Malayalam','Informational','/articles/vitamin-d-deficiency-symptoms/','P2',['vitamin deficiency symptoms','vitamin D deficiency symptoms Malayalam'])
add('D Gut and general health','English / Malayalam','Informational','/articles/thyroid-symptoms/','P2',['thyroid symptoms Malayalam','തൈറോയ്ഡ് ലക്ഷണങ്ങൾ'])
add('D Gut and general health','English / Malayalam','Informational','/articles/health-checks-before-marriage/','P1',['health checkup before marriage','വിവാഹത്തിന് മുമ്പ് ആരോഗ്യ പരിശോധന'],note='Matches an existing video (Health checks before marriage).')
add('E Skin hair cosmetology','English','Informational','/skin-and-hair/','P1',['skin care tips','hair growth tips','scalp health','hair fall Malayalam'])
add('E Skin hair cosmetology','English / Malayalam','Informational','/articles/hair-fall-causes/','P1',['hair fall causes','മുടികൊഴിച്ചിൽ കാരണങ്ങൾ'])
add('E Skin hair cosmetology','English / Malayalam','Informational','/articles/skin-pigmentation-causes/','P1',['skin pigmentation','acne causes Malayalam','ചർമ്മത്തിലെ പിഗ്മെന്റേഷൻ'])
add('E Skin hair cosmetology','English / Malayalam','Informational / commercial','/articles/skin-whitening-treatment-truth/','P1',['skin whitening treatment Malayalam'],note='Matches an existing video. YMYL: needs careful, evidence-based, non-promotional wording.')
add('E Skin hair cosmetology','English','Informational','/medical-cosmetology/','P2',['medical cosmetologist Kerala','medical cosmetologist India','cosmetic procedures Malayalam','anti-ageing skincare'],note='Only as far as her qualification and services are confirmed.')
add('E Skin hair cosmetology','English','Informational','/articles/prp-hair-treatment-explained/','P3',['PRP hair treatment explained'],note='Publish only if she confirms she performs/endorses it.')
add('F Consultation','English','Transactional / local','/consultations/','P1',['online doctor consultation Kerala','female doctor consultation online','online health consultation','skin consultation online'])
add('F Consultation','English','Transactional','/consultations/','P3',['BHMS doctor Kerala','homoeopathic consultation'],note='Only if she practises homoeopathy; confirm scope before targeting.')
add('G Brand collaboration','English','Commercial (B2B)','/partnerships/','P1',['Kerala health influencer','Malayalam health influencer','medical influencer Kerala','skincare influencer Kerala','doctor influencer for brand collaboration','healthcare content creator India','wellness influencer Kerala','healthcare brand promotion','medical creator for Instagram campaigns'],note='Low volume, high commercial value. Verify audience stats before pitching.')
for loc in ['Kerala','Kochi','Kozhikode','Calicut','Thrissur','Kannur','Malappuram','Trivandrum','Kollam','Kottayam','Palakkad']:
    pri='P1' if loc in('Kerala','Kannur') else 'P3'
    add('H Geographic','English','Local / informational','/consultations/' if loc in('Kannur','Kerala') else '/health-education/',pri,[f'online doctor consultation {loc}' if loc!='Kerala' else 'health tips Kerala'],geo=loc,note='No location landing pages (no physical practice there). Reach these cities through Kerala-wide content and Search Console query data.')
with open('deliver/keyword-research.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f);w.writerow(H);w.writerows(R)
print(len(R),'keywords')
# mapping
pages={}
for r in R: pages.setdefault(r[7],[]).append(r)
with open('deliver/keyword-to-url-mapping.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f);w.writerow(['target_url','status','primary_keyword','secondary_keywords','best_priority','intent'])
    live={'/','/about/','/consultations/','/health-education/','/womens-health/','/gut-health/','/skin-and-hair/','/medical-cosmetology/','/videos/','/partnerships/','/contact/'}
    for u,rows in sorted(pages.items()):
        pr=min(x[8] for x in rows)
        w.writerow(['https://theglodoc.in'+u,'live' if u in live else 'planned (needs Dr. Athmika review)',rows[0][0],' | '.join(x[0] for x in rows[1:]),pr,rows[0][5]])
# calendar
Cal=[ # cluster, h1, primary, secondary, angle, h2s, video
('Women','What is PCOS? Symptoms and causes','PCOS Malayalam','PCOS symptoms; PCOD vs PCOS; PCOS എന്താണ്','What PCOS is, common symptoms, and when to see a doctor, explained in simple language.','What is PCOS?|Common symptoms|PCOS vs PCOD|When to see a doctor'),
('Women','Why are periods irregular? Common causes','irregular periods causes','ക്രമരഹിതമായ ആർത്തവം; late periods','Common reasons periods become irregular and which signs mean it is time to get checked.','What is a normal cycle?|Common causes|Warning signs|Tests a doctor may suggest'),
('Gut','What is gut health, and why does it matter?','gut health Malayalam','gut microbiome; digestive health','A plain explanation of gut health, everyday habits that affect digestion and when to see a doctor.','What is the gut microbiome?|Habits that affect digestion|Signs worth checking|Myths'),
('Skin','Why does skin pigmentation happen?','skin pigmentation','ചർമ്മത്തിലെ പിഗ്മെന്റേഷൻ; dark spots causes','Why pigmentation appears, which types exist and what to ask a doctor before any treatment.','Common types|Causes|Sun and skin|Treatment questions'),
('Hair','Common causes of hair fall','hair fall causes','മുടികൊഴിച്ചിൽ; hair fall Malayalam','The common causes of hair fall, what is normal shedding, and when a check-up helps.','Normal shedding vs hair loss|Common causes|Tests|When to see a doctor'),
('Women','Health checks to do before marriage','health checkup before marriage','വിവാഹത്തിന് മുമ്പ് പരിശോധന','Which health checks couples commonly consider before marriage and why, in plain language.','Why check?|Common tests|What the results mean|Talking to a doctor'),
('General','Vitamin D deficiency: symptoms and testing','vitamin D deficiency symptoms','vitamin deficiency symptoms Malayalam','Common signs of low vitamin D, who should get tested and what a doctor looks at.','What vitamin D does|Possible symptoms|Testing|Sun and food'),
('General','Thyroid problems: common symptoms','thyroid symptoms Malayalam','തൈറോയ്ഡ് ലക്ഷണങ്ങൾ; thyroid test','Common thyroid symptoms, which test is used and when to see a doctor.','What the thyroid does|Overactive vs underactive|Testing|When to seek care'),
('Women','Pregnancy myths and facts','pregnancy myths Malayalam','ഗർഭധാരണം തെറ്റിദ്ധാരണകൾ','Common pregnancy myths and what doctors say instead.','Myth 1-5|Why myths spread|Who to ask'),
('Skin','Skin whitening treatments: what to know','skin whitening treatment Malayalam','skin lightening safe?','What skin whitening treatments claim, what is realistic, risks, and questions to ask.','What do they claim?|Is it safe?|Realistic expectations|Questions to ask'),
('Gut','Bloating: common causes and what helps','bloating causes','acidity Malayalam; gas problem','Common causes of bloating and acidity, simple habits and warning signs.','Common causes|Everyday habits|Warning signs|When to see a doctor'),
('Women','Hormonal imbalance: signs to know','hormonal imbalance symptoms','ഹോർമോൺ പ്രശ്നങ്ങൾ','Possible signs of hormonal imbalance in women and how doctors check.','What are hormones?|Possible signs|Common causes|Tests'),
('Hair','Hair care basics that actually work','hair care tips Malayalam','hair growth tips; scalp health','Everyday hair and scalp care without myths.','Scalp health|Washing|Diet|Myths'),
('Skin','Simple skincare routine for beginners','skin care tips Malayalam','skin care routine; sunscreen','A short, evidence-based skincare routine and what to skip.','Cleanse|Moisturise|Sunscreen|What to skip'),
('Skin','Acne: common causes and when to see a doctor','acne causes Malayalam','pimples causes','Why acne happens, common triggers and when treatment from a doctor helps.','Why acne forms|Triggers|Myths|When to see a doctor'),
('Cosmetology','Medical cosmetology vs salon treatments','medical cosmetologist Kerala','what is medical cosmetology','What medical cosmetology is, how it differs from a salon, and how to choose a practitioner.','What it is|Doctor vs salon|Safety questions|Choosing'),
('General','Routine health tests worth doing','routine health tests','health checkup Malayalam','Which routine tests are commonly advised and how often, explained simply.','Why test?|Common tests|By age|Talking to a doctor'),
('Gut','Constipation: causes and habits','constipation causes','digestive health','Why constipation happens and which habits and signs matter.','Causes|Habits|Warning signs|When to seek care'),
('Women','Menstrual health: what is normal?','menstrual health','period pain; cycle length','What is normal in a cycle and what to get checked.','Cycle basics|Pain|Heavy periods|When to see a doctor'),
('General','Lifestyle diseases: early signs','lifestyle diseases Malayalam','lifestyle habits; prevention','Common lifestyle diseases, early warning signs and prevention.','What are they?|Early signs|Prevention|Check-ups'),
('Skin','Sunscreen: myths and facts','sunscreen Malayalam','SPF; sunscreen for Indian skin','What SPF means and common sunscreen myths.','Why sunscreen|SPF|Myths|How to use'),
('Hair','Dandruff and scalp problems','scalp health','dandruff causes','Why dandruff happens and how to look after the scalp.','Causes|Care|When to see a doctor'),
('Women','Menopause: symptoms and care','menopause symptoms','perimenopause','What menopause is, common symptoms and when to seek help.','What it is|Symptoms|Care|When to see a doctor'),
('General','Do straw bottles and plastic affect ageing?','straw bottles and ageing','plastic bottle myth','Examining the claim from the video with evidence, and what is known.','The claim|What evidence says|Practical advice'),
('Skin','Anti-ageing skincare: what works','anti-ageing skincare','wrinkles; retinoids','A balanced look at anti-ageing skincare ingredients and claims.','What is ageing?|Ingredients|Claims to doubt'),
('Cosmetology','PRP for hair: what it is and who it suits','PRP hair treatment explained','hair PRP risks','What PRP involves, who may be considered, and limits. Publish only if confirmed within her practice.','What is PRP?|Who it may suit|Risks|Questions'),
('General','Iron deficiency and anaemia in women','iron deficiency symptoms','anaemia Malayalam','Common signs of iron deficiency and what testing shows.','Symptoms|Causes|Testing|Food'),
('Gut','Acidity and reflux: common triggers','acidity Malayalam','reflux; heartburn','Common triggers for acidity and when symptoms need a check.','Triggers|Habits|Warning signs'),
('Women','Fertility myths and facts','fertility myths','conceiving; PCOS and fertility','Common fertility myths and when to consult a doctor.','Myths|Facts|When to get checked'),
('Skin','Dark circles: causes and care','dark circles causes','under eye','Why dark circles appear and what actually helps.','Causes|Care|When to see a doctor'),
('Hair','Does hair oil help hair growth?','hair growth tips','hair oil Malayalam','What hair oils can and cannot do.','What oils do|Evidence|Better habits'),
('General','How much sleep and water do you need?','health tips in Malayalam','sleep; hydration','Evidence-based basics on sleep and hydration.','Sleep|Water|Habits'),
('Women','Breast health and self-checks','breast health awareness','breast self exam','Why awareness matters, how to do self-checks, and when to see a doctor.','Why|How|Warning signs'),
('Skin','Skin care during monsoon in Kerala','skin care tips Kerala','fungal infection monsoon','Skin and hair concerns that rise in monsoon and sensible care.','Common issues|Care|When to see a doctor'),
('General','Common health myths in Kerala homes','health facts Malayalam','myths vs facts','Popular health myths and what doctors say.','Myth|Fact|Why it matters'),
('Women','PCOS diet and lifestyle: what is evidence-based','PCOS diet','PCOS lifestyle','What lifestyle changes are supported by evidence for PCOS.','Diet|Exercise|Sleep|Doctor review'),
('Skin','Pigmentation treatments: questions to ask','skin pigmentation treatment','melasma Malayalam','Questions to ask any practitioner before pigmentation treatment.','Options|Risks|Questions'),
]
print("articles:",len(Cal))
start=datetime.date(2026,11,30)  # Mondays
days=[0,2,4]  # Mon Wed Fri
slug=lambda s:''.join(c if c.isalnum() else '-' for c in s.lower()).strip('-')
with open('deliver/90-day-content-calendar.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f);w.writerow(['week','publish_date','topic_cluster','h1','primary_keyword','secondary_keywords','search_intent','suggested_url','seo_title','meta_description','suggested_h2s','internal_links','related_video_or_social','cta','review_status'])
    for i,(cl,h1,pk,sk,angle,h2) in enumerate(Cal):
        d=start+datetime.timedelta(weeks=i//3,days=days[i%3])
        title=(h1+' | Dr. Athmika Prakash'); title=title if len(title)<=60 else h1[:58]
        meta=(angle+' By Dr. Athmika Prakash.')[:158]
        hub={'Women':'/womens-health/','Gut':'/gut-health/','Skin':'/skin-and-hair/','Hair':'/skin-and-hair/','Cosmetology':'/medical-cosmetology/','General':'/gut-health/'}[cl]
        w.writerow([i//3+1,d.isoformat(),cl,h1,pk,sk,'Informational','/articles/'+slug(h1)+'/',title,meta,h2,f'{hub} ; /consultations/ ; /videos/','Matching YouTube Short / Instagram Reel from @the.glodoc if one exists (to be mapped by Dr. Athmika)','Enquire about a consultation (/consultations/)','Draft by Dr. Athmika or reviewed by her; add 2-3 references from WHO / ICMR / MoHFW / peer-reviewed sources before publishing'])
print('calendar ok')
