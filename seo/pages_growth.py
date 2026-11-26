# Growth pages for theglodoc.in: brand partnerships, media kit, trust pages.
# Imported by seo/build.py after its helpers are defined (exec'd in build.py's namespace).
# Every statistic comes from data/site.json; empty values are hidden, never invented.

STAT_LABELS = [
    ('instagramFollowers', 'Instagram followers'),
    ('youtubeSubscribers', 'YouTube subscribers'),
    ('avgReelViews', 'Average Reel views'),
    ('avgReach30d', 'Average 30-day reach'),
    ('engagementRate', 'Engagement rate'),
]
AUDIENCE_LABELS = [
    ('audienceTopCountries', 'Top audience countries'),
    ('audienceTopCities', 'Top audience cities'),
    ('audienceAge', 'Audience age'),
    ('audienceGender', 'Audience gender'),
]
MISSING = [lbl for k, lbl in STAT_LABELS + AUDIENCE_LABELS if not ST.get(k)]
if not DATA.get('contentLanguages'): MISSING.append('Content languages')
if not DATA.get('statsAsOf'): MISSING.append('Date the statistics were taken (statsAsOf)')
if not DATA.get('registration'): MISSING.append('Registration number and council (optional to show)')

def stat_items():
    out = ''
    for k, lbl in STAT_LABELS:
        if ST.get(k):
            out += f'<li><strong data-site="{k}">{html.escape(ST[k])}</strong><span>{lbl}</span></li>'
    out += f'<li><strong data-site="consultations">{html.escape(DATA["consultations"])}</strong><span>patient consultations</span></li>'
    return out

def audience_rows():
    rows = ''.join(f'<li><strong>{lbl}</strong><span>{html.escape(ST[k])}</span></li>' for k, lbl in AUDIENCE_LABELS if ST.get(k))
    return rows

AS_OF = f'<p class="small">Figures as of {html.escape(DATA["statsAsOf"])}, from platform insights.</p>' if DATA.get('statsAsOf') else ''
QUALS = ''.join(f'<li>{html.escape(q)}</li>' for q in DATA['qualifications'])
LANGS = DATA.get('contentLanguages', '')

POSITIONING = ("Dr. Athmika Prakash is a doctor (BHMS) and certified consultant medical cosmetologist from Kannur, Kerala. "
               "As THEGLODOC, she explains women's health, everyday health, skin and hair in short, plain-language videos for people who want "
               "health information they can trust. For healthcare organisations and responsible health brands, she offers doctor-led, "
               "education-first content that is checked for accuracy and clearly disclosed.")

FORMATS = [
    ('Health awareness campaigns', 'Short videos and Story sets that explain a health topic, a screening or a habit, for awareness days, hospital outreach and public health messaging.'),
    ('Educational content series', 'A multi-part series that explains a topic properly, where one Reel is not enough.'),
    ('Expert interviews and podcasts', 'Interviews, panels, Lives and podcast episodes on women\'s health, skin, hair and everyday health.'),
    ('Events and speaking', 'Talks, workshops and health camps for organisations, colleges and corporate wellness programmes.'),
    ('Product education', 'For suitable wellness, skincare and haircare products: what the product is, who it is and is not for, and how to use it sensibly. Clearly labelled as a paid partnership.'),
]
NOT_DONE = [
    'Promotion or endorsement of prescription medicines, drugs or medical devices.',
    'Claims of cure, guaranteed results, or words such as "best", "100%" or "no side effects".',
    'Patient testimonials, before-and-after images or patient stories without documented consent.',
    'Fear-based messaging, or content that encourages self-diagnosis or self-medication.',
    'Supplements or products whose claims cannot be supported by evidence.',
    'Undisclosed paid content. Every paid partnership is labelled.',
]
PROCESS = [
    ('Enquiry', 'You share the brief using the form below.'),
    ('Fit check', 'Dr. Athmika checks whether the product or campaign fits her audience and her professional standards. Not every enquiry is accepted.'),
    ('Claims review', 'Every claim is checked against evidence and the brand\'s approved information. Wording is agreed in writing.'),
    ('Approvals', 'Where a campaign needs regulatory approval, for example an advertiser permit or a health authority approval in the UAE, it proceeds only once that is in place.'),
    ('Publish and report', 'Content goes live with clear disclosure, and performance figures are shared after the campaign.'),
]
AUDIENCES = [
    ('Hospitals and clinics', 'Awareness campaigns, screening drives, health camps and patient education.'),
    ('Health-tech and diagnostics', 'Explaining tests, apps and digital health tools in plain language.'),
    ('Wellness and personal care', 'Evidence-based skincare, haircare, nutrition and lifestyle products.'),
    ('Agencies and PR teams', 'Doctor-led voices for healthcare communication and media campaigns.'),
    ('Public health and NGOs', 'Myth-busting, awareness days and community health education.'),
    ('Colleges and corporates', 'Talks and workshops on women\'s health and everyday wellbeing.'),
]
FAQ = [
    ('Does Dr. Athmika accept every partnership?', 'No. Each enquiry is checked for fit with her audience, the evidence behind the product, and the professional and advertising rules that apply to doctors. She declines work that does not meet those standards.'),
    ('Which countries do you work with?', 'Enquiries are welcome from organisations in India, the UAE and the wider Gulf. Dr. Athmika is based in Kannur, Kerala. For campaigns aimed at the UAE, the required permits and approvals are confirmed before any content is produced.'),
    ('Is paid content disclosed?', 'Yes. Every paid partnership is labelled clearly at the start of the content, in line with ASCI guidelines in India and the rules of the platform.'),
    ('Can she promote medicines or treatments?', 'No. She does not endorse prescription medicines, drugs or medical devices, and she does not promise treatment outcomes.'),
    ('What are the rates?', 'Rates depend on the format, the number of deliverables and usage rights. They are shared after the brief is reviewed.'),
    ('How soon will we hear back?', 'The team aims to reply to complete enquiries within a few working days.'),
]

def li_pairs(items):
    return ''.join(f'<li><strong>{a}.</strong> {b}</li>' for a, b in items)

def partnership_form():
    opt = lambda xs: ''.join(f'<option>{x}</option>' for x in xs)
    return f'''<form class="enq-form" name="partnership" method="POST" data-netlify="true" netlify-honeypot="bot-field" data-ok="Thank you. Your enquiry has been received. The team will review the brief and reply by email.">
<input type="hidden" name="form-name" value="partnership">
<p class="hp" aria-hidden="true"><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<div class="f"><label for="p-company">Organisation name</label><input id="p-company" name="company" type="text" autocomplete="organization" required></div>
<div class="f"><label for="p-name">Contact person</label><input id="p-name" name="name" type="text" autocomplete="name" required></div>
<div class="f"><label for="p-email">Business email</label><input id="p-email" name="email" type="email" autocomplete="email" required></div>
<div class="f"><label for="p-website">Company website</label><input id="p-website" name="website" type="url" inputmode="url" placeholder="https://" required></div>
<div class="f"><label for="p-industry">Industry</label><select id="p-industry" name="industry" required><option value="">Select one</option>{opt(['Hospital or clinic', 'Diagnostics or laboratory', 'Health-tech or telemedicine', 'Medical education', 'Wellness or nutrition', 'Skincare or haircare', 'Agency or PR', 'NGO or public health', 'Corporate wellness', 'Media', 'Other'])}</select></div>
<div class="f"><label for="p-country">Country</label><input id="p-country" name="country" type="text" autocomplete="country-name" required></div>
<div class="f full"><label for="p-type">Type of enquiry</label><select id="p-type" name="partnership_type" required><option value="">Select one</option>{opt(['Health awareness campaign', 'Health education content', 'Medical communication project', 'Corporate wellness initiative', 'Public health project', 'Podcast or interview invitation', 'Event or speaking invitation', 'Media enquiry', 'Product education (wellness, skincare, haircare)', 'Other'])}</select></div>
<div class="f full"><label for="p-goals">Campaign objectives</label><textarea id="p-goals" name="objectives" rows="3" required placeholder="What should the campaign achieve?"></textarea></div>
<div class="f"><label for="p-audience">Target audience</label><input id="p-audience" name="target_audience" type="text" placeholder="For example, women 25 to 40 in Kerala" required></div>
<div class="f"><label for="p-deliv">Expected deliverables</label><input id="p-deliv" name="deliverables" type="text" placeholder="For example, 2 Reels and 1 Story set" required></div>
<div class="f"><label for="p-time">Proposed timeline</label><input id="p-time" name="timeline" type="text" placeholder="For example, launch in March" required></div>
<div class="f"><label for="p-budget">Budget range <span>(optional)</span></label><select id="p-budget" name="budget"><option value="">Prefer to discuss</option>{opt(['Under ₹50,000', '₹50,000 to ₹1,50,000', '₹1,50,000 to ₹5,00,000', 'Above ₹5,00,000', 'Under AED 5,000', 'AED 5,000 to 20,000', 'Above AED 20,000'])}</select></div>
<div class="f full"><label for="p-msg">Additional information <span>(optional)</span></label><textarea id="p-msg" name="message" rows="4" placeholder="Product or service, key messages, links, approvals already in place."></textarea></div>
<div class="f full check"><label><input type="checkbox" name="standards_ack" value="yes" required> I understand that all content is subject to Dr. Athmika's editorial and claims review, and that paid content is always disclosed.</label></div>
<div class="f full enq-actions"><button class="btn" type="submit">Send partnership enquiry</button><p class="enq-status" role="status" aria-live="polite"></p></div>
</form>'''

# ================= BRAND PARTNERSHIPS =================
t = [('Home', '/'), ('Brand partnerships', '/brand-partnerships/')]
faq_html = ''.join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
bp_body = f'''<section><div class="wrap tight"><div class="prose">
<p class="lede">{POSITIONING}</p>
<ul class="fact-list" style="max-width:none">{stat_items()}</ul>
{AS_OF}
<div class="row"><a class="btn" href="#enquiry">Send a partnership enquiry</a><a class="link" href="/media-kit/">View the media kit</a></div>
</div></div></section>
<section class="tint"><div class="wrap tight"><h2 style="margin-bottom:28px">Who she works with</h2>
<div class="cards">{''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in AUDIENCES)}</div></div></section>
<section><div class="wrap tight"><div class="prose">
<h2>Ways to collaborate</h2>
<ul>{li_pairs(FORMATS)}</ul>
<h2>Why a doctor-led voice</h2>
<p>People increasingly look to doctors on social media to tell them what is true. That trust is the reason brands want doctor-creators, and the reason it has to be protected. Dr. Athmika's content is built on her medical training, her experience of {html.escape(DATA["consultations"])} patient consultations, and a simple rule: explain clearly, never overstate.</p>
<h2>What she does not do</h2>
<ul>{''.join(f'<li>{x}</li>' for x in NOT_DONE)}</ul>
<h2>How a partnership works</h2>
<ol class="steps">{''.join(f'<li><strong>{a}.</strong> {b}</li>' for a, b in PROCESS)}</ol>
<h2>Questions brands ask</h2>
<div class="faqs">{faq_html}</div>
</div></div></section>
<section class="tint" id="enquiry"><div class="wrap tight enq"><div class="enq-intro"><h2>Send a partnership enquiry</h2>
<p class="lede">Share the brief and the team will reply by email. Prefer email? Write to <a class="link" href="mailto:{EMAIL}" data-site="email" data-site-mailto="email">{EMAIL}</a>.</p>
<p class="small">Patients: please use the <a class="link" href="/contact/">contact page</a> for consultation enquiries.</p></div>
{partnership_form()}</div></section>'''
write('/brand-partnerships/', 'Doctor-Led Health Brand Partnerships | THEGLODOC',
      'Partner with Dr. Athmika Prakash, a doctor and health educator from Kerala, for health awareness campaigns, education content and talks in India and the UAE.',
      page_hero('Brand partnerships with Dr. Athmika', 'Doctor-led health education for hospitals, health-tech, wellness brands and agencies in India, the UAE and the Gulf.', t),
      bp_body, t)

# ================= MEDIA KIT =================
t = [('Home', '/'), ('Media kit', '/media-kit/')]
aud = audience_rows()
aud_block = (f'<h2>Audience</h2><ul class="fact-list kv" style="max-width:none">{aud}</ul>' if aud else
             '<h2>Audience</h2><p>Detailed audience insights (top countries and cities, age and gender, average reach and Reel views) are shared with brands on request, taken from current platform insights.</p>')
past = DATA.get('pastCollaborations') or []
past_block = ('<h2>Selected collaborations</h2><ul>' + ''.join(f'<li>{html.escape(x)}</li>' for x in past) + '</ul>') if past else ''
lang_row = f'<li><strong>Content languages</strong><span>{html.escape(LANGS)}</span></li>' if LANGS else ''
mk_body = f'''<section><div class="wrap tight"><div class="prose">
<p class="lede">{POSITIONING}</p>
<div class="row"><a class="btn" href="/media-kit/theglodoc-media-kit.pdf" download>Download the media kit (PDF)</a><a class="link" href="/brand-partnerships/#enquiry">Send an enquiry</a></div>
<h2>Profile</h2>
<ul class="fact-list kv" style="max-width:none">
<li><strong>Name</strong><span>{html.escape(DATA["name"])}</span></li>
<li><strong>Brand</strong><span>{html.escape(DATA["brand"])}</span></li>
<li><strong>Based in</strong><span>{html.escape(DATA["basedIn"])}</span></li>
{lang_row}
<li><strong>Platforms</strong><span><a href="{IG}" target="_blank" rel="noopener">Instagram {html.escape(DATA["instagramHandle"])}</a>, <a href="{YT}" target="_blank" rel="noopener">YouTube {html.escape(DATA["youtubeHandle"])}</a></span></li>
</ul>
<h3>Qualifications</h3><ul>{QUALS}</ul>
<h2>Reach</h2>
<ul class="fact-list" style="max-width:none">{stat_items()}</ul>
{AS_OF}
{aud_block}
<h2>Content pillars</h2>
<ul><li><a href="/womens-health/">Women's health</a>: periods, hormones, checkups and pregnancy myths</li><li><a href="/gut-health/">Gut and everyday health</a>: digestion, routine tests and deficiencies</li><li><a href="/skin-and-hair/">Skin and hair</a>: common concerns and myths</li><li><a href="/medical-cosmetology/">Medical cosmetology</a>: what procedures involve and who they suit</li></ul>
<h2>Collaboration formats</h2>
<ul>{li_pairs(FORMATS)}</ul>
{past_block}
<h2>Standards</h2>
<ul>{''.join(f'<li>{x}</li>' for x in NOT_DONE)}</ul>
</div></div></section>
<section class="tint"><div class="wrap tight"><div class="vids-head"><h2>Content samples</h2><a class="link" href="/videos/">All videos</a></div><div class="vids grid">{vid_cards()}</div></div></section>
{cta_band('Planning a health campaign?', '/brand-partnerships/#enquiry', 'Send an enquiry')}'''
write('/media-kit/', 'Media Kit: Dr. Athmika Prakash, Doctor Creator | THEGLODOC',
      'Media kit for Dr. Athmika Prakash (THEGLODOC): profile, qualifications, reach, content pillars and collaboration formats for health brands. Download the PDF.',
      page_hero('Media kit', 'Dr. Athmika Prakash, doctor and health educator. THEGLODOC on Instagram and YouTube.', t), mk_body, t)

# printable media kit (rendered to PDF by seo/pdf.js; not deployed as a page)
stat_print = ''.join(f'<div><b>{html.escape(ST[k])}</b><span>{lbl}</span></div>' for k, lbl in STAT_LABELS if ST.get(k))
stat_print += f'<div><b>{html.escape(DATA["consultations"])}</b><span>patient consultations</span></div>'
aud_print = ''.join(f'<p><b>{lbl}:</b> {html.escape(ST[k])}</p>' for k, lbl in AUDIENCE_LABELS if ST.get(k)) or '<p>Detailed audience insights are available on request.</p>'
here = os.path.abspath('.')
print_html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>THEGLODOC media kit</title><style>
@page{{size:A4;margin:0}}*{{box-sizing:border-box}}body{{margin:0;font-family:"Times New Roman",Tinos,"Liberation Serif",serif;color:#1d261e}}
.pg{{width:210mm;height:297mm;padding:18mm;position:relative;overflow:hidden;page-break-after:always}}
.cover{{background:#e3e9dd;display:grid;grid-template-columns:1fr 78mm;gap:12mm;align-items:end}}
.cover img{{width:78mm;height:102mm;object-fit:cover;border-radius:6mm}}
.ey{{letter-spacing:.2em;font-size:10pt;color:#4a5c4b;text-transform:uppercase}}
h1{{font-size:40pt;line-height:1;margin:6mm 0;font-weight:400}}h2{{font-size:16pt;font-weight:400;color:#4a5c4b;margin:8mm 0 3mm;border-bottom:.3mm solid #c9d3c1;padding-bottom:2mm}}
p,li{{font-size:10.5pt;line-height:1.5;margin:0 0 2mm}}ul{{margin:0;padding-left:5mm}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin:4mm 0}}.stats div{{background:#f3f5f0;border-radius:4mm;padding:5mm}}
.stats b{{display:block;font-size:22pt;font-weight:400;color:#4a5c4b}}.stats span{{font-size:9pt;color:#5d685d}}
.foot{{position:absolute;bottom:12mm;left:18mm;right:18mm;font-size:9pt;color:#5d685d;display:flex;justify-content:space-between}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:10mm}}
</style></head><body>
<section class="pg cover"><div><p class="ey">THEGLODOC · Media kit</p><h1>Dr. Athmika Prakash</h1>
<p style="font-size:13pt">Doctor (BHMS, FMC) · Certified Consultant Medical Cosmetologist · Health educator</p>
<p>{html.escape(DATA["basedIn"])}</p><p style="margin-top:8mm">{POSITIONING}</p></div>
<img src="file://{here}/photos/portrait.jpg" alt=""></section>
<section class="pg"><p class="ey">Reach and audience</p><h2>Reach</h2><div class="stats">{stat_print}</div>
{('<p style="font-size:9pt;color:#5d685d">Figures as of ' + html.escape(DATA["statsAsOf"]) + ', from platform insights.</p>') if DATA.get('statsAsOf') else ''}
<h2>Audience</h2>{aud_print}
<h2>Platforms</h2><p>Instagram {html.escape(DATA["instagramHandle"])} · {html.escape(IG)}</p><p>YouTube {html.escape(DATA["youtubeHandle"])} · {html.escape(YT)}</p>
{('<p>Content languages: ' + html.escape(LANGS) + '</p>') if LANGS else ''}
<h2>Content pillars</h2><ul><li>Women's health: periods, hormones, checkups and pregnancy myths</li><li>Gut and everyday health: digestion, routine tests, deficiencies</li><li>Skin and hair: common concerns and myths</li><li>Medical cosmetology: what procedures involve and who they suit</li></ul>
<h2>Qualifications</h2><ul>{QUALS}</ul>
<div class="foot"><span>theglodoc.in/media-kit</span><span>{html.escape(EMAIL)}</span></div></section>
<section class="pg"><p class="ey">Working together</p><h2>Collaboration formats</h2><ul>{li_pairs(FORMATS)}</ul>
{('<h2>Selected collaborations</h2><ul>' + ''.join(f'<li>{html.escape(x)}</li>' for x in past) + '</ul>') if past else ''}
<h2>How it works</h2><ol>{''.join(f'<li><b>{a}.</b> {b}</li>' for a, b in PROCESS)}</ol>
<h2>Standards</h2><ul>{''.join(f'<li>{x}</li>' for x in NOT_DONE)}</ul>
<h2>Contact</h2><p>Partnership enquiries: theglodoc.in/brand-partnerships · {html.escape(EMAIL)} · Instagram {html.escape(DATA["instagramHandle"])}</p>
<div class="foot"><span>THEGLODOC</span><span>Updated {TODAY}</span></div></section>
</body></html>'''
os.makedirs('build', exist_ok=True)
open('build/media-kit-print.html', 'w', encoding='utf-8').write(print_html)

# ================= TRUST PAGES =================
def legal(path, title, desc, h1, lede, inner, kind='WebPage'):
    tr = [('Home', '/'), (h1, path)]
    b = f'<section><div class="wrap tight"><div class="prose"><p class="small">Last updated {TODAY}</p>{inner}</div></div></section>'
    write(path, title, desc, page_hero(h1, lede, tr), b, tr, kind=kind)

legal('/editorial-policy/', 'Editorial Policy | THEGLODOC by Dr. Athmika Prakash',
      'How THEGLODOC health content is written, sourced, reviewed and updated by Dr. Athmika Prakash, and how paid partnerships are kept separate and disclosed.',
      'Editorial policy', 'How health content on THEGLODOC is written, checked and updated.', f'''
<h2>Who writes the content</h2><p>Health content on this site and on THEGLODOC channels is written or reviewed by Dr. Athmika Prakash ({html.escape(", ".join(DATA["qualifications"]))}). Each article names its author and reviewer and shows when it was published and last reviewed.</p>
<h2>Sources</h2><p>Articles are based on recognised sources such as the World Health Organization, the Indian Council of Medical Research, the Ministry of Health and Family Welfare, national and international clinical guidelines, and peer-reviewed research. Sources are listed at the end of each article.</p>
<h2>Accuracy and limits</h2><ul><li>Content explains health topics in general terms. It is not a diagnosis or a treatment plan for any individual.</li><li>Where evidence is limited or uncertain, the article says so.</li><li>Content does not promise results, and avoids sensational headlines.</li></ul>
<h2>Review and updates</h2><p>Articles are reviewed at least once a year, and sooner when guidance changes. If you spot an error, email <a href="mailto:{EMAIL}">{EMAIL}</a> and it will be checked and corrected.</p>
<h2>Paid partnerships</h2><p>Editorial content is never paid for. Paid partnerships are labelled clearly, follow the standards on the <a href="/brand-partnerships/">brand partnerships</a> page, and do not influence health articles. Dr. Athmika does not endorse prescription medicines, drugs or medical devices.</p>
<h2>Use of artificial intelligence</h2><p>Tools may help with drafting or formatting, but every health statement is checked by Dr. Athmika against the sources before it is published.</p>''')

legal('/medical-disclaimer/', 'Medical Disclaimer | THEGLODOC by Dr. Athmika Prakash',
      'THEGLODOC content is general health education by Dr. Athmika Prakash. It is not a diagnosis or personal medical advice and does not replace a consultation.',
      'Medical disclaimer', 'Health education, not personal medical advice.', '''
<p>The information on theglodoc.in and on THEGLODOC Instagram and YouTube channels is for general education. It is not a diagnosis, a prescription or personal medical advice, and it does not create a doctor and patient relationship.</p>
<ul><li>Always speak to a qualified doctor about your own symptoms, test results or treatment.</li><li>Do not stop, start or change any medicine because of something you read or watched here.</li><li>In an emergency, go to the nearest hospital or call your local emergency number.</li></ul>
<p>Every person is different, so results of any treatment or procedure vary and are never guaranteed.</p>
<p>Some content is produced in paid partnership with brands. Such content is labelled, and it is not a medical recommendation for any individual.</p>''')

legal('/privacy-policy/', 'Privacy Policy | THEGLODOC',
      'How theglodoc.in collects and uses the information you send through its enquiry forms, how analytics are used, and how to ask for your data to be deleted.',
      'Privacy policy', 'What information this site collects and how it is used.', f'''
<h2>What we collect</h2><ul><li><strong>Enquiry forms.</strong> When you send an enquiry, we receive what you enter, such as your name, email, organisation and message. Forms are processed by our hosting provider, Netlify.</li><li><strong>Analytics.</strong> If analytics are enabled, Google Analytics collects anonymous usage data such as pages visited, device type and approximate location, using cookies.</li><li><strong>Email.</strong> If you email us, we receive your email address and message.</li></ul>
<h2>How we use it</h2><p>Only to reply to your enquiry, to manage consultations and partnerships, and to understand how the site is used. We do not sell your information.</p>
<h2>Health information</h2><p>Please do not send medical history, reports or other sensitive health information through the forms. If a consultation needs it, you will be told how to share it safely.</p>
<h2>How long we keep it</h2><p>Enquiries are kept for as long as needed to respond and for related records, and then deleted.</p>
<h2>Your choices</h2><p>To see, correct or delete the information you sent us, email <a href="mailto:{EMAIL}">{EMAIL}</a>. You can block or delete cookies in your browser settings.</p>
<h2>Contact</h2><p>{html.escape(DATA["name"])}, {html.escape(DATA["basedIn"])}. Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>''')

legal('/terms/', 'Terms of Use | THEGLODOC',
      'Terms of use for theglodoc.in, the website of Dr. Athmika Prakash (THEGLODOC): use of content, health information, partnerships and links to other sites.',
      'Terms of use', 'The terms for using theglodoc.in.', f'''
<h2>Using this site</h2><p>By using theglodoc.in you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Health information</h2><p>Content is for general education only. Please read the <a href="/medical-disclaimer/">medical disclaimer</a>.</p>
<h2>Content ownership</h2><p>Text, images and videos on this site belong to THEGLODOC unless stated otherwise. You may share links, but please do not copy or republish content without written permission.</p>
<h2>Enquiries and partnerships</h2><p>Sending an enquiry does not create an agreement. Consultations and partnerships are confirmed separately in writing.</p>
<h2>Links to other sites</h2><p>This site links to Instagram, YouTube and other websites. We are not responsible for their content or privacy practices.</p>
<h2>Changes</h2><p>These terms may be updated. The date at the top shows the latest version. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>''')
