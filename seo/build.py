#!/usr/bin/env python3
"""Builds the multi-page SEO version of theglodoc.in into ./site-seo and ./glodoc-seo-deploy.zip.
Run from the scratchpad directory:  python3 seo/build.py
Source of truth for the homepage design: backup/site/index.html (the version live before the SEO work)."""
import re, os, json, shutil, zipfile, datetime, html
from PIL import Image, ImageDraw, ImageFont

ROOT = 'https://theglodoc.in'
TODAY = datetime.date.today().isoformat()
OUT = 'site-seo'
IG = 'https://www.instagram.com/the.glodoc/'
YT = 'https://www.youtube.com/@The.glodoc'
EMAIL = 'drathmika999@gmail.com'
OG_IMG = ROOT + '/images/og-dr-athmika-prakash-theglodoc.jpg'

src = open('backup/site/index.html', encoding='utf-8').read()

# ---------- images ----------
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + '/images')
p = Image.open('photos/portrait.jpg').convert('RGB')
p.save(f'{OUT}/images/dr-athmika-prakash-portrait.jpg', quality=80, optimize=True, progressive=True)
p.save(f'{OUT}/images/dr-athmika-prakash-portrait.webp', quality=78, method=6)
p.resize((640, 836), Image.LANCZOS).save(f'{OUT}/images/dr-athmika-prakash-portrait-640.webp', quality=76, method=6)
VIDEOS = [
 ('5NUlKnJgj9U', 'Gizele, Bigg Boss Malayalam 7', 'gizele-bigg-boss-malayalam-7'),
 ('s0Oc1AWgpJc', 'Gizele Thakral, part 2', 'gizele-thakral-part-2'),
 ('pfNJ9mEm_Ak', 'Health checks before marriage', 'health-checks-before-marriage'),
 ('lvnbt2G5gy8', 'Straw bottles and ageing', 'straw-bottles-and-ageing'),
 ('AzWIMHtlgk0', 'Skin whitening treatment', 'skin-whitening-treatment'),
]
for i, (vid, title, slug) in enumerate(VIDEOS, 1):
    im = Image.open(f'thumbs/short-{i}.jpg').convert('RGB')
    im.save(f'{OUT}/images/video-{slug}.jpg', quality=80, optimize=True, progressive=True)
    im.save(f'{OUT}/images/video-{slug}.webp', quality=76, method=6)
# social share image 1200x630
W, H = 1200, 630
bg = Image.new('RGB', (W, H), (227, 233, 221))
d = ImageDraw.Draw(bg)
ph = p.resize((int(H * 0.9 * 980 / 1280 / 0.9), H), Image.LANCZOS)
ph = p.resize((int(H * 980 / 1280), H), Image.LANCZOS)
bg.paste(ph, (W - ph.width, 0))
FB = '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'
FR = '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
d.text((70, 150), 'THEGLODOC', font=ImageFont.truetype(FR, 40), fill=(74, 92, 75))
d.text((70, 215), 'Dr. Athmika', font=ImageFont.truetype(FB, 92), fill=(29, 38, 30))
d.text((70, 315), 'Prakash', font=ImageFont.truetype(FB, 92), fill=(29, 38, 30))
d.text((70, 450), 'Doctor and health educator', font=ImageFont.truetype(FR, 38), fill=(74, 92, 75))
d.text((70, 500), "Women's health · Gut health · Skin and hair", font=ImageFont.truetype(FR, 28), fill=(93, 104, 93))
bg.save(f'{OUT}/images/og-dr-athmika-prakash-theglodoc.jpg', quality=85, optimize=True)
for f in ['favicon.svg', 'favicon.png', 'apple-touch-icon.png']:
    shutil.copy('icons/' + f, f'{OUT}/{f}')
shutil.copy('site/config.js', f'{OUT}/config.js')

# ---------- css / js ----------
css = re.search(r'<style>\n/\* Layout.*?</style>', src, re.S).group(0)[len('<style>\n'):-len('</style>')]
css += """
/* ---- additions for multi-page site ---- */
body{margin:0}[hidden]{display:none!important}
.menu{display:none;position:relative}
.menu summary{list-style:none;cursor:pointer;font-size:15px;padding:10px 18px;border:1px solid var(--line);border-radius:999px;background:var(--paper)}
.menu summary::-webkit-details-marker{display:none}
.menu nav{position:absolute;right:0;top:calc(100% + 8px);background:var(--paper);border-radius:16px;padding:14px 22px;box-shadow:0 10px 40px rgba(29,38,30,.14);display:flex;flex-direction:column;gap:12px;min-width:200px}
.menu nav a{text-decoration:none;font-size:17px}
.phero{background:var(--sage-100)}
.phero .wrap{padding-top:150px;padding-bottom:84px;display:flex;flex-direction:column;gap:22px}
.phero h1{max-width:26ch}
.crumbs{font-size:14px;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px}
.crumbs a{text-decoration:none;border-bottom:1px solid transparent}
.crumbs a:hover{border-bottom-color:currentColor}
.crumbs li{list-style:none}
.crumbs ol{display:flex;flex-wrap:wrap;gap:6px;margin:0;padding:0}
.crumbs li+li::before{content:"/";margin-right:6px;opacity:.5}
.tight{padding-block:80px}
.prose{max-width:68ch;display:flex;flex-direction:column;gap:20px}
.prose h2{font-size:clamp(28px,3vw,36px);margin-top:18px}
.prose h3{font-size:22px;margin-top:6px}
.prose ul{margin:0;padding-left:1.2em;display:flex;flex-direction:column;gap:8px}
.prose a:not(.btn){border-bottom:1px solid currentColor;text-decoration:none}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px}
.card{display:flex;flex-direction:column;gap:10px;background:var(--sage-50);border-radius:16px;padding:28px;text-decoration:none;min-width:0}
.tint .card{background:var(--paper)}
.card p{font-size:16px;color:var(--muted)}
.card .more{font-size:15px;color:var(--sage);margin-top:auto;padding-top:8px}
.card:hover{background:var(--sage-100)}
.note{font-size:15px;color:var(--muted);background:var(--sage-50);border-radius:12px;padding:16px 20px;max-width:68ch}
.row{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.fact-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:0;padding:0;list-style:none}
.fact-list li{background:var(--sage-50);border-radius:16px;padding:22px}
.fact-list strong{display:block;font-weight:400;font-size:28px;color:var(--sage);line-height:1.15}
.fact-list span{font-size:15px;color:var(--muted)}
.vids.grid{grid-template-columns:repeat(auto-fill,minmax(200px,1fr));overflow:visible}
.vid em{font-style:normal;font-size:14px;color:var(--muted)}
.foot-cols{display:flex;flex-wrap:wrap;gap:28px 56px}
.foot-cols h2{font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:10px}
.foot-cols ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:8px;font-size:16px}
.foot-cols a{text-decoration:none}
.foot-cols a:hover{color:var(--sage)}
.contact-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px}
.contact-grid>*{min-width:0}
.contact-list{display:flex;flex-direction:column;gap:14px;font-size:17px}
.contact-list a{overflow-wrap:anywhere}
@media (max-width:820px){
  .menu{display:block}
  .top .nav{display:none}
  .contact-grid{grid-template-columns:1fr;gap:40px}
  .phero .wrap{padding-top:112px;padding-bottom:56px}
  .tight{padding-block:60px}
}
"""
open(f'{OUT}/styles.css', 'w', encoding='utf-8').write(css)

js = re.search(r'<script>\n\(function\(\)\{\n  var S=window\.SITE.*?</script>', src, re.S).group(0)[len('<script>\n'):-len('</script>')]
js += """
(function(){
  document.querySelectorAll("form.enq-form").forEach(function(form){
    var btn=form.querySelector("button[type=submit]"),st=form.querySelector(".enq-status"),label=btn.textContent;
    form.addEventListener("submit",function(e){
      e.preventDefault();
      st.className="enq-status";
      if(!window.GLODOC_LIVE){st.textContent="Preview only. Enquiries are sent from the live website.";return;}
      btn.disabled=true;btn.textContent="Sending...";st.textContent="";
      fetch("/",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:new URLSearchParams(new FormData(form)).toString()})
      .then(function(r){if(!r.ok)throw new Error(r.status);form.reset();st.textContent="Thank you. Your message has been sent and the team will be in touch.";})
      .catch(function(){st.className="enq-status err";st.textContent="Your message didn't send. Please try again, or message "+((window.SITE&&SITE.instagramHandle)||"@the.glodoc")+" on Instagram.";})
      .then(function(){btn.disabled=false;btn.textContent=label;});
    });
  });
})();
"""
open(f'{OUT}/app.js', 'w', encoding='utf-8').write(js)

# ---------- shared fragments ----------
LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="16" fill="#4a5c4b"/><path fill="#ffffff" d="M16 5c.7 6.6 3.7 9.6 11 11-7.3 1.4-10.3 4.4-11 11-.7-6.6-3.7-9.6-11-11 7.3-1.4 10.3-4.4 11-11z"/></svg>'
NAV = [('/about/', 'About'), ('/consultations/', 'Consultations'), ('/health-education/', 'Health education'),
       ('/videos/', 'Videos'), ('/partnerships/', 'Partnerships'), ('/contact/', 'Contact')]
def header():
    links = ''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return (f'<div class="top"><div class="wrap"><a class="logo" href="/" aria-label="THEGLODOC home">{LOGO}<span>THEGLODOC</span></a>'
            f'<nav class="nav" aria-label="Main">{links}<a class="btn" href="{IG}" data-site-href="instagramUrl" target="_blank" rel="noopener">Follow on Instagram</a></nav>'
            f'<details class="menu"><summary>Menu</summary><nav aria-label="Mobile">{links}<a href="{IG}" data-site-href="instagramUrl" target="_blank" rel="noopener">Instagram</a></nav></details>'
            f'</div></div>')
FOOT = f'''<footer><div class="wrap">
<div class="foot-brand"><a class="logo" href="/" aria-label="THEGLODOC home">{LOGO}<span>THEGLODOC</span></a>
<p>Health education by Dr. Athmika Prakash.</p>
<p class="foot-email">Email <a class="link" href="mailto:{EMAIL}" data-site="email" data-site-mailto="email">{EMAIL}</a></p>
<p class="foot-email">YouTube <a class="link" href="{YT}" data-site-href="youtubeUrl" target="_blank" rel="noopener"><span data-site="youtubeHandle">@The.glodoc</span></a></p>
<p class="foot-email">Instagram <a class="link" href="{IG}" data-site-href="instagramUrl" target="_blank" rel="noopener"><span data-site="instagramHandle">@the.glodoc</span></a></p></div>
<div class="foot-cols">
<div><h2>Learn</h2><ul><li><a href="/womens-health/">Women's health</a></li><li><a href="/gut-health/">Gut and everyday health</a></li><li><a href="/skin-and-hair/">Skin and hair</a></li><li><a href="/medical-cosmetology/">Medical cosmetology</a></li><li><a href="/videos/">Videos</a></li></ul></div>
<div><h2>Work with her</h2><ul><li><a href="/consultations/">Consultations</a></li><li><a href="/partnerships/">Partnerships</a></li><li><a href="/contact/">Contact</a></li><li><a href="/about/">About</a></li></ul></div>
</div>
<div class="fine"><span>Content is for general education and does not replace a medical consultation. In an emergency, contact your nearest hospital.</span><span>© 2026 THEGLODOC</span></div>
</div></footer>'''

PERSON_ID = ROOT + '/#person'
ORG_ID = ROOT + '/#organization'
SITE_ID = ROOT + '/#website'
person = {
 '@type': 'Person', '@id': PERSON_ID, 'name': 'Dr. Athmika Prakash', 'alternateName': ['Dr Athmika', 'Athmika Prakash'],
 'url': ROOT + '/about/', 'image': ROOT + '/images/dr-athmika-prakash-portrait.jpg',
 'jobTitle': 'Doctor, certified consultant medical cosmetologist and health educator',
 'description': 'Doctor, certified consultant medical cosmetologist, health educator and content creator sharing clear, everyday health education.',
 'email': EMAIL, 'worksFor': {'@id': ORG_ID},
 'address': {'@type': 'PostalAddress', 'addressLocality': 'Kannur', 'addressRegion': 'Kerala', 'addressCountry': 'IN'},
 'knowsAbout': ["Women's health", 'Gut health', 'Hormonal health', 'Skin health', 'Hair health', 'Medical cosmetology', 'Health education'],
 'sameAs': [IG, YT],
}
org = {'@type': 'Organization', '@id': ORG_ID, 'name': 'THEGLODOC', 'url': ROOT + '/', 'logo': ROOT + '/favicon.png',
       'founder': {'@id': PERSON_ID}, 'email': EMAIL, 'sameAs': [IG, YT]}
website = {'@type': 'WebSite', '@id': SITE_ID, 'url': ROOT + '/', 'name': 'THEGLODOC', 'inLanguage': 'en-IN', 'publisher': {'@id': ORG_ID}}

def crumbs_ld(trail):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': ROOT + u} for i, (n, u) in enumerate(trail)]}

def head(title, desc, path, extra_ld, og_type='website', preload=''):
    assert len(title) <= 65, (len(title), title)
    assert 70 <= len(desc) <= 160, (len(desc), desc)
    url = ROOT + path
    graph = {'@context': 'https://schema.org', '@graph': extra_ld}
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#4a5c4b">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="64x64" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:site_name" content="THEGLODOC">
<meta property="og:locale" content="en_IN">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{OG_IMG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Dr. Athmika Prakash, doctor and health educator, THEGLODOC">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title, quote=True)}">
<meta name="twitter:description" content="{html.escape(desc, quote=True)}">
<meta name="twitter:image" content="{OG_IMG}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/styles.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400&display=swap">
{preload}<script type="application/ld+json">{json.dumps(graph, ensure_ascii=False, separators=(',', ':'))}</script>
<script>window.GLODOC_LIVE=true</script>
</head>
<body>
'''
TAIL = '\n<script src="/config.js"></script>\n<script src="/app.js" defer></script>\n</body>\n</html>\n'

def pic(base, alt, w, h, cls='', lazy=True, sizes=None, srcset640=None, prio=False):
    attrs = f'width="{w}" height="{h}"' + (' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"')
    if srcset640:
        return (f'<picture><source type="image/webp" srcset="/images/{base}-640.webp 640w, /images/{base}.webp 980w" sizes="{sizes}">'
                f'<img src="/images/{base}.jpg" alt="{html.escape(alt, quote=True)}" {attrs}></picture>')
    return (f'<picture><source type="image/webp" srcset="/images/{base}.webp"><img src="/images/{base}.jpg" alt="{html.escape(alt, quote=True)}" {attrs}></picture>')

DISC = '<p class="note">This page is for general education. It is not a diagnosis or personal medical advice, and it does not replace a consultation with a doctor. If you are unwell or worried about a symptom, please see a doctor in person. In an emergency, go to the nearest hospital.</p>'

def page_hero(h1, lede, trail):
    items = ''.join((f'<li><a href="{u}">{n}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{n}</li>') for i, (n, u) in enumerate(trail))
    return (f'<header class="phero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><ol>{items}</ol></nav>'
            f'<h1>{h1}</h1><p class="lede hero-lede">{lede}</p></div></header>')

def webpage_ld(title, desc, path, kind='WebPage'):
    return {'@type': kind, '@id': ROOT + path + '#webpage', 'url': ROOT + path, 'name': title, 'description': desc,
            'isPartOf': {'@id': SITE_ID}, 'about': {'@id': PERSON_ID}, 'inLanguage': 'en-IN', 'dateModified': TODAY,
            'breadcrumb': {'@id': ROOT + path + '#breadcrumb'}}

def write(path, title, desc, hero, body, trail, kind='WebPage', extra=None, og_type='website'):
    ld = [website, org, person, webpage_ld(title, desc, path, kind)]
    bc = crumbs_ld(trail); bc['@id'] = ROOT + path + '#breadcrumb'
    ld.append(bc)
    if extra: ld += extra
    out = head(title, desc, path, ld, og_type) + header() + hero + '\n<main>\n' + body + '\n</main>\n' + FOOT + TAIL
    d = OUT + path
    os.makedirs(d, exist_ok=True)
    open(d + 'index.html', 'w', encoding='utf-8').write(out)

def form(name, kind):
    if kind == 'contact':
        sel = ('<div class="f full"><label for="c-reason">What is your enquiry about?</label><select id="c-reason" name="reason" required>'
               '<option value="">Select one</option><option>A consultation (online or offline)</option><option>A brand partnership</option>'
               '<option>Media or interview</option><option>Something else</option></select></div>')
        msg = 'How can we help?'
        ph = 'Please do not share detailed medical history or reports here. The team will tell you the next step.'
    else:
        sel = ''
        msg = 'About the product and campaign'
        ph = 'Product, key message, timeline and anything else she should know.'
    pid = 'c' if kind == 'contact' else 'p'
    extra = ''
    if kind == 'partnership':
        extra = ('<div class="f"><label for="p-company">Company or brand</label><input id="p-company" name="company" type="text" autocomplete="organization" required></div>'
                 '<div class="f"><label for="p-type">Type of partnership</label><select id="p-type" name="partnership_type" required><option value="">Select one</option>'
                 '<option>Instagram Reel</option><option>Instagram Stories</option><option>Content series</option><option>Event or appearance</option><option>Something else</option></select></div>'
                 '<div class="f"><label for="p-budget">Budget <span>(optional)</span></label><select id="p-budget" name="budget"><option value="">Prefer not to say</option>'
                 '<option>Under ₹25,000</option><option>₹25,000 to ₹75,000</option><option>₹75,000 to ₹2,00,000</option><option>Above ₹2,00,000</option></select></div>')
    return f'''<form class="enq-form" name="{name}" method="POST" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="{name}">
<p class="hp" aria-hidden="true"><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<div class="f"><label for="{pid}-name">Your name</label><input id="{pid}-name" name="name" type="text" autocomplete="name" required></div>
<div class="f"><label for="{pid}-email">Email</label><input id="{pid}-email" name="email" type="email" autocomplete="email" required></div>
{extra}{sel}
<div class="f full"><label for="{pid}-msg">{msg}</label><textarea id="{pid}-msg" name="message" rows="5" required placeholder="{ph}"></textarea></div>
<div class="f full enq-actions"><button class="btn" type="submit">Send enquiry</button><p class="enq-status" role="status" aria-live="polite"></p></div>
</form>'''

def cta_band(text, href, label):
    return (f'<section class="deep"><div class="wrap tight"><div class="row" style="justify-content:space-between"><h2 style="max-width:22ch">{text}</h2>'
            f'<a class="btn" href="{href}">{label}</a></div></div></section>')

def vid_cards(sel=None):
    out = ''
    for i, (vid, title, slug) in enumerate(VIDEOS):
        if sel and vid not in sel: continue
        out += (f'<a class="vid" href="https://www.youtube.com/shorts/{vid}" target="_blank" rel="noopener">'
                + pic('video-' + slug, f'Video thumbnail: {title}', 300, 464)
                + f'<span>{title}</span><em>Watch on YouTube</em></a>')
    return out

# ================= HOMEPAGE =================
h_title = 'Dr. Athmika Prakash | Doctor & Health Educator | THEGLODOC'
h_desc = "Meet Dr. Athmika Prakash, a doctor and health educator in Kerala sharing clear insights on women's health, gut health, skin, hair and everyday wellness."
_i = src.index('<div class="top">')
body = src[_i:src.index('<script>', _i)]
body = header() + '\n\n' + body[body.index('<header class="hero"'):]
body = body.replace('<p class="cred">BHMS, FMC · Based in India</p>', '<p class="cred">Dr. Athmika Prakash · BHMS, FMC · Kannur, Kerala</p>')
body = body.replace('<div class="portrait"><img src="images/portrait.jpg" alt="Portrait of Dr. Athmika Prakash wearing a stethoscope" width="980" height="1280"></div>',
    '<div class="portrait">' + pic('dr-athmika-prakash-portrait', 'Dr. Athmika Prakash, doctor and health educator, wearing a stethoscope', 980, 1280, lazy=False, sizes='(max-width:820px) 100vw, 540px', srcset640=True) + '</div>')
# focus areas become links
for t, href, txt in [("Everyday health", '/gut-health/', 'Gut health, hormones and routine tests.'),
                     ("Women's health", '/womens-health/', 'Periods, checkups and pregnancy myths.'),
                     ("Skin and hair", '/skin-and-hair/', "What works, and what's a myth."),
                     ("Procedures", '/medical-cosmetology/', 'What they are and who they suit.')]:
    old = f'<div><h3>{t}</h3><p>{txt}</p></div>'
    assert old in body, t
    body = body.replace(old, f'<a class="card" href="{href}"><h3>{t}</h3><p>{txt}</p><span class="more">Read more</span></a>')
body = body.replace('<div class="focus-grid">', '<div class="cards">').replace('.focus-grid', '.cards')
# videos: webp pictures + link to videos hub
def vid_swap(m):
    n = int(m.group(1)); vid, title, slug = VIDEOS[n - 1]
    return pic('video-' + slug, f'Video thumbnail: {title}', 300, 464)
body = re.sub(r'<img src="images/video-(\d)\.jpg"[^>]*>', vid_swap, body)
body = body.replace('<h2>Featured videos.</h2>', '<h2>Featured videos.</h2>')
body = body.replace('<a class="link" href="https://www.youtube.com/@The.glodoc" data-site-href="youtubeUrl" target="_blank" rel="noopener">More on YouTube</a>\n    </div>',
                    '<a class="link" href="/videos/">All videos</a>\n    </div>', 1)
body = body.replace('<a class="btn ghost" href="#enquiry">Send an enquiry</a>', '<a class="btn ghost" href="#enquiry">Send an enquiry</a> <a class="link" href="/partnerships/">Partnership details</a>')
body = body.replace('<a class="btn" href="https://www.instagram.com/the.glodoc/" data-site-href="instagramUrl" target="_blank" rel="noopener">Follow on Instagram</a>\n        <div class="ig-count">',
                    '<a class="btn" href="https://www.instagram.com/the.glodoc/" data-site-href="instagramUrl" target="_blank" rel="noopener">Follow on Instagram</a>\n        <div class="ig-count">')
body = body.replace('<h2>Available for online and offline consultations.</h2>', '<h2>Available for online and offline consultations.</h2>\n      <p><a class="link" href="/consultations/">How consultations work</a></p>', 1)
# form: replace id-based single form with class-based (names kept)
body = body.replace('id="partnership-form" ', '')
body = body.replace('<button class="btn" id="f-submit" type="submit">', '<button class="btn" type="submit">').replace('<p class="enq-status" id="f-status"', '<p class="enq-status"')
body = re.sub(r'<footer>.*?</footer>', FOOT, body, flags=re.S)
body = body.replace('<main>', '<main>')
hp_ld = [website, org, person,
         {'@type': 'ProfilePage', '@id': ROOT + '/#webpage', 'url': ROOT + '/', 'name': h_title, 'description': h_desc, 'inLanguage': 'en-IN',
          'isPartOf': {'@id': SITE_ID}, 'mainEntity': {'@id': PERSON_ID}, 'dateModified': TODAY}]
preload = '<link rel="preload" as="image" type="image/webp" href="/images/dr-athmika-prakash-portrait-640.webp" imagesrcset="/images/dr-athmika-prakash-portrait-640.webp 640w, /images/dr-athmika-prakash-portrait.webp 980w" imagesizes="(max-width:820px) 100vw, 540px" fetchpriority="high">\n'
home = head(h_title, h_desc, '/', hp_ld, preload=preload) + body + TAIL
assert 'images/portrait.jpg' not in home and 'images/video-1.jpg' not in home
open(OUT + '/index.html', 'w', encoding='utf-8').write(home)

# ================= ABOUT =================
t = [('Home', '/'), ('About', '/about/')]
about_body = f'''<section><div class="wrap tight"><div class="prose">
<h2>Who she is</h2>
<p>Dr. Athmika Prakash is a doctor, certified consultant medical cosmetologist and health educator based in Kannur, Kerala. She shares clear, everyday health education through short videos on Instagram and YouTube under the name THEGLODOC.</p>
<p>Her work focuses on questions people ask every day: women's health, gut and general health, skin and hair, and what medical cosmetology procedures involve and who they suit.</p>
<h2>Qualifications</h2>
<ul><li><strong>BHMS</strong>, Bachelor of Homoeopathic Medicine and Surgery</li><li><strong>Certified Consultant Medical Cosmetologist</strong></li></ul>
<h2>Experience</h2>
<ul><li><strong>4,000+</strong> patient consultations completed, online and offline</li><li>Health educator and content creator on <a href="{IG}" target="_blank" rel="noopener" data-site-href="instagramUrl">Instagram</a> (<span data-site="instagramFollowers">12.3K</span> followers) and <a href="{YT}" target="_blank" rel="noopener" data-site-href="youtubeUrl">YouTube</a></li></ul>
<h2>What she covers</h2>
<ul><li><a href="/womens-health/">Women's health</a>: periods, hormones, checkups and pregnancy myths</li><li><a href="/gut-health/">Gut and everyday health</a>: digestion, routine tests and common deficiencies</li><li><a href="/skin-and-hair/">Skin and hair</a>: common concerns, myths and what to ask a doctor</li><li><a href="/medical-cosmetology/">Medical cosmetology</a>: what procedures are and who they suit</li></ul>
<h2>Work with her</h2>
<p>Patients can <a href="/consultations/">enquire about a consultation</a>. Health, wellness, skincare and haircare brands can read about <a href="/partnerships/">partnerships</a>. Everyone can <a href="/videos/">watch her videos</a> or follow along on Instagram.</p>
{DISC}
</div></div></section>
{cta_band('Questions about a consultation or collaboration?', '/contact/', 'Contact')}'''
write('/about/', 'About Dr. Athmika Prakash | Doctor & Health Educator',
      'Dr. Athmika Prakash is a doctor, certified consultant medical cosmetologist and health educator in Kerala, sharing clear everyday health education as THEGLODOC.',
      page_hero('About Dr. Athmika Prakash', 'Doctor, certified consultant medical cosmetologist, health educator and content creator.', t),
      about_body, t, kind='ProfilePage', extra=None)

# ================= CONSULTATIONS =================
t = [('Home', '/'), ('Consultations', '/consultations/')]
c_body = f'''<section><div class="wrap tight"><div class="prose">
<ul class="fact-list" style="max-width:none"><li><strong data-site="consultations">4,000+</strong><span>patient consultations completed</span></li><li><strong>Online</strong><span>from wherever you are</span></li><li><strong>Offline</strong><span>in person, by appointment</span></li></ul>
<h2>Online consultation</h2>
<p>Speak with Dr. Athmika remotely about a health, skin or hair concern. It suits questions that can be discussed and guided without a physical examination.</p>
<h2>Offline consultation</h2>
<p>Meet Dr. Athmika in person when a concern needs to be examined. Details of where and when are shared when you enquire.</p>
<h2>What you can discuss</h2>
<ul><li>Everyday health questions and routine checks</li><li>Women's health concerns</li><li>Skin and hair concerns</li><li>Medical cosmetology procedures: what they involve and whether they suit you</li></ul>
<h2>Limits of online consultation</h2>
<ul><li>A video or phone call cannot replace a physical examination or tests. You may be asked to visit in person, or to see another specialist.</li><li>It is not for emergencies. If you have severe symptoms, go to the nearest hospital.</li><li>Please do not rely on videos or website content as personal medical advice.</li></ul>
<h2>How to enquire</h2>
<ol style="margin:0;padding-left:1.2em;display:flex;flex-direction:column;gap:8px"><li>Send an enquiry on the <a href="/contact/">contact page</a>, or message <a href="{IG}" target="_blank" rel="noopener" data-site-href="instagramUrl">@the.glodoc</a> on Instagram.</li><li>Tell us whether you prefer online or offline, and what you would like to discuss in a line or two.</li><li>The team replies with availability and the next step. Fees are shared on enquiry.</li></ol>
{DISC}
</div></div></section>
{cta_band('Ready to book a consultation?', '/contact/', 'Send an enquiry')}'''
write('/consultations/', 'Online & Offline Consultation | Dr. Athmika Prakash',
      'Consult Dr. Athmika Prakash, a doctor and certified consultant medical cosmetologist, online or in person. 4,000+ consultations completed. See how to enquire.',
      page_hero('Consultations with Dr. Athmika', 'Online and offline consultations for everyday health, women\'s health, skin and hair.', t),
      c_body, t)

# ================= HEALTH EDUCATION HUB =================
t = [('Home', '/'), ('Health education', '/health-education/')]
he_body = f'''<section><div class="wrap tight">
<div class="prose" style="margin-bottom:40px"><p>Dr. Athmika explains health in short, clear videos. This section brings her topics together so you can find what you are looking for.</p></div>
<div class="cards">
<a class="card" href="/womens-health/"><h3>Women's health</h3><p>Periods, hormones, checkups and pregnancy myths.</p><span class="more">Read more</span></a>
<a class="card" href="/gut-health/"><h3>Gut and everyday health</h3><p>Digestion, routine tests, vitamins and thyroid.</p><span class="more">Read more</span></a>
<a class="card" href="/skin-and-hair/"><h3>Skin and hair</h3><p>Common concerns, myths and when to see a doctor.</p><span class="more">Read more</span></a>
<a class="card" href="/medical-cosmetology/"><h3>Medical cosmetology</h3><p>What procedures are and who they suit.</p><span class="more">Read more</span></a>
</div></div></section>
<section class="tint"><div class="wrap tight"><div class="vids-head"><h2>Watch</h2><a class="link" href="/videos/">All videos</a></div><div class="vids grid">{vid_cards()}</div></div></section>
{cta_band('Have a question for Dr. Athmika?', '/contact/', 'Get in touch')}'''
write('/health-education/', "Health Education by Dr. Athmika | Women's, Gut, Skin",
      "Clear health education from Dr. Athmika Prakash: women's health, gut and everyday health, skin and hair, and medical cosmetology. Watch her videos.",
      page_hero('Health education, explained clearly', "Women's health, gut and everyday health, skin and hair, and medical cosmetology.", t),
      he_body, t, kind='CollectionPage')

# ================= TOPIC HUBS =================
def topic(path, title, desc, name, h1, lede, intro, questions, vsel, related):
    t = [('Home', '/'), ('Health education', '/health-education/'), (name, path)]
    qs = ''.join(f'<li>{q}</li>' for q in questions)
    rel = ''.join(f'<li><a href="{h}">{n}</a></li>' for h, n in related)
    vids = f'<section class="tint"><div class="wrap tight"><div class="vids-head"><h2>Related videos</h2><a class="link" href="/videos/">All videos</a></div><div class="vids grid">{vid_cards(vsel)}</div></div></section>' if vsel else ''
    b = f'''<section><div class="wrap tight"><div class="prose">
{intro}
<h2>Questions this section covers</h2><ul>{qs}</ul>
<p>Dr. Athmika's articles on these questions are written and reviewed by her before they are published here. In the meantime you can <a href="{IG}" target="_blank" rel="noopener" data-site-href="instagramUrl">follow her on Instagram</a> or <a href="/consultations/">enquire about a consultation</a>.</p>
<h2>Also explore</h2><ul>{rel}</ul>
{DISC}
</div></div></section>{vids}{cta_band('Want to talk to a doctor about this?', '/consultations/', 'See consultations')}'''
    write(path, title, desc, page_hero(h1, lede, t), b, t, kind='CollectionPage')

topic('/womens-health/', "Women's Health Education | Dr. Athmika Prakash",
      "Women's health explained by Dr. Athmika Prakash: periods, hormones, health checks before marriage, pregnancy myths and when to see a doctor.",
      "Women's health", "Women's health, explained clearly.", 'Periods, hormones, checkups and pregnancy myths, in plain language.',
      "<p>Women's health questions are often surrounded by myths and embarrassment. Dr. Athmika answers them in plain language, so you know what is common, what deserves attention, and when to see a doctor.</p>",
      ['What are the common causes of irregular periods?', 'What is PCOS, and how is it different from PCOD?', 'What are the signs of a hormonal imbalance?', 'Which health checks are worth doing before marriage?', 'What are the common myths about pregnancy?', 'What should a routine women\'s health checkup include?'],
      ['pfNJ9mEm_Ak'], [('/gut-health/', 'Gut and everyday health'), ('/skin-and-hair/', 'Skin and hair'), ('/consultations/', 'Consultations')])
topic('/gut-health/', 'Gut & Everyday Health Education | Dr. Athmika Prakash',
      'Gut health, digestion, routine tests, vitamin levels and thyroid explained in simple language by Dr. Athmika Prakash, a doctor and health educator.',
      'Gut and everyday health', 'Gut and everyday health, explained clearly.', 'Digestion, routine tests, vitamins and thyroid, without the jargon.',
      "<p>Good everyday health starts with understanding your own body. This section covers digestion, the routine tests many people are unsure about, and common concerns such as vitamin deficiencies and thyroid symptoms.</p>",
      ['What does gut health mean, and why does it matter?', 'What are the common causes of bloating and acidity?', 'What are the signs of vitamin D and B12 deficiency?', 'What are the common symptoms of thyroid problems?', 'Which routine health tests are worth doing, and how often?', 'What lifestyle habits affect digestion and energy?'],
      None, [('/womens-health/', "Women's health"), ('/skin-and-hair/', 'Skin and hair'), ('/consultations/', 'Consultations')])
topic('/skin-and-hair/', 'Skin & Hair Health Education | Dr. Athmika Prakash',
      'Skin and hair concerns explained by Dr. Athmika Prakash, a certified consultant medical cosmetologist: pigmentation, hair fall, myths and what to ask a doctor.',
      'Skin and hair', 'Skin and hair, explained clearly.', "What works, what's a myth, and when to see a doctor.",
      "<p>Skin and hair advice online is full of quick fixes. Dr. Athmika, a certified consultant medical cosmetologist, explains common skin and hair concerns and separates what is evidence-based from what is not.</p>",
      ['Why does skin pigmentation happen?', 'What are the common causes of hair fall?', 'Do skin whitening treatments really work, and are they safe?', 'What is a sensible, simple skincare routine?', 'When should a skin or hair concern be seen by a doctor?', 'How do everyday habits affect skin and hair?'],
      ['AzWIMHtlgk0', 'lvnbt2G5gy8'], [('/medical-cosmetology/', 'Medical cosmetology'), ('/womens-health/', "Women's health"), ('/consultations/', 'Consultations')])
topic('/medical-cosmetology/', 'Medical Cosmetology Education | Dr. Athmika Prakash',
      'Understand medical cosmetology with Dr. Athmika Prakash, a certified consultant medical cosmetologist: what procedures involve, who they suit and what to ask.',
      'Medical cosmetology', 'Medical cosmetology, explained honestly.', 'What procedures are, who they suit, and what to ask before you decide.',
      "<p>Medical cosmetology covers skin and hair procedures carried out by trained doctors. Dr. Athmika, a certified consultant medical cosmetologist, explains what a procedure involves and who it suits. Every person's skin and hair are different, so suitability is decided after an assessment, and no result is guaranteed.</p>",
      ['What is medical cosmetology, and how is it different from a salon treatment?', 'How do I know whether a procedure suits my skin or hair?', 'What questions should I ask before any procedure?', 'What are the risks and recovery for common procedures?', 'How do I choose a qualified practitioner?'],
      None, [('/skin-and-hair/', 'Skin and hair'), ('/consultations/', 'Consultations'), ('/about/', 'About Dr. Athmika')])

# ================= VIDEOS =================
t = [('Home', '/'), ('Videos', '/videos/')]
v_body = f'''<section><div class="wrap tight">
<div class="prose" style="margin-bottom:40px"><p>Short health videos by Dr. Athmika. Each opens on YouTube. For daily videos, follow <a href="{IG}" target="_blank" rel="noopener" data-site-href="instagramUrl">@the.glodoc on Instagram</a> or subscribe on <a href="{YT}" target="_blank" rel="noopener" data-site-href="youtubeUrl">YouTube</a>.</p></div>
<div class="vids grid">{vid_cards()}</div></div></section>
{cta_band('Prefer to ask a doctor directly?', '/consultations/', 'See consultations')}'''
write('/videos/', 'Health Videos by Dr. Athmika Prakash | YouTube Shorts',
      'Watch short health videos by Dr. Athmika Prakash on women\'s health, health checks, skin and everyday wellness. Follow THEGLODOC on YouTube and Instagram.',
      page_hero('Health videos', 'Short, clear videos by Dr. Athmika on everyday health, women\'s health and skin.', t), v_body, t, kind='CollectionPage')

# ================= PARTNERSHIPS =================
t = [('Home', '/'), ('Partnerships', '/partnerships/')]
p_body = f'''<section><div class="wrap tight"><div class="prose">
<p>THEGLODOC is a doctor-led health education brand. Dr. Athmika partners with health, wellness, skincare and haircare brands to explain what a product does and who it suits, in her own voice.</p>
<ul class="fact-list" style="max-width:none"><li><strong data-site="instagramFollowers">12.3K</strong><span>Instagram followers</span></li><li><strong data-site="consultations">4,000+</strong><span>patient consultations</span></li></ul>
<h2>Content formats</h2>
<ul><li><strong>Instagram Reels:</strong> a short video explaining what the product does and who it suits.</li><li><strong>Stories:</strong> a Story set with a link, for launches and offers.</li><li><strong>Series:</strong> several videos for products that need more explanation.</li></ul>
<h2>Where the content appears</h2>
<p><a href="{IG}" target="_blank" rel="noopener" data-site-href="instagramUrl">Instagram @the.glodoc</a> and <a href="{YT}" target="_blank" rel="noopener" data-site-href="youtubeUrl">YouTube @The.glodoc</a>.</p>
<h2>How a partnership works</h2>
<p>Because this is health content, product details and claims are reviewed with the brand before anything is published. Rates are shared on request.</p>
</div></div></section>
<section class="tint" id="enquiry"><div class="wrap tight enq"><div class="enq-intro"><h2>Send a partnership enquiry</h2><p class="lede">Tell us about your brand and campaign. Or write to <a class="link" href="mailto:{EMAIL}" data-site="email" data-site-mailto="email">{EMAIL}</a>.</p></div>
{form('partnership', 'partnership')}</div></section>'''
write('/partnerships/', 'Brand Collaborations with Doctor Creator | THEGLODOC',
      'Partner with Dr. Athmika Prakash (THEGLODOC), a doctor and health creator, for health, wellness, skincare and haircare campaigns on Instagram and YouTube.',
      page_hero('Partner with THEGLODOC', 'For health, wellness, skincare and haircare brands. Rates on request.', t), p_body, t)

# ================= CONTACT =================
t = [('Home', '/'), ('Contact', '/contact/')]
ct_body = f'''<section><div class="wrap tight contact-grid"><div class="contact-list">
<p>For consultations, brand partnerships or media enquiries, use the form or contact her directly.</p>
<p><strong>Email</strong><br><a class="link" href="mailto:{EMAIL}" data-site="email" data-site-mailto="email">{EMAIL}</a></p>
<p><strong>Instagram</strong><br><a class="link" href="{IG}" target="_blank" rel="noopener" data-site-href="instagramUrl"><span data-site="instagramHandle">@the.glodoc</span></a></p>
<p><strong>YouTube</strong><br><a class="link" href="{YT}" target="_blank" rel="noopener" data-site-href="youtubeUrl"><span data-site="youtubeHandle">@The.glodoc</span></a></p>
<p><strong>Based in</strong><br>Kannur, Kerala, India</p>
<p class="note">Please do not send detailed medical history or reports through this form. This site cannot handle medical emergencies.</p></div>
<div>{form('contact', 'contact')}</div></div></section>'''
write('/contact/', 'Contact Dr. Athmika Prakash | Consultations & Partnerships',
      'Contact Dr. Athmika Prakash (THEGLODOC) to enquire about a consultation, a brand partnership or a media request. Email, Instagram and enquiry form.',
      page_hero('Contact', 'Consultations, partnerships and media enquiries.', t), ct_body, t, kind='ContactPage')

# ================= 404 =================
nf = head('Page not found | THEGLODOC', 'The page you are looking for could not be found. Go back to the THEGLODOC homepage for Dr. Athmika Prakash.', '/404.html',
          [website]).replace('index, follow, max-image-preview:large', 'noindex, follow')
nf = re.sub(r'<link rel="canonical"[^>]*>\n', '', nf)
nf += header() + '''<header class="phero"><div class="wrap"><h1>This page could not be found.</h1><p class="lede hero-lede">It may have moved, or the link may be wrong.</p>
<div class="row"><a class="btn" href="/">Go to the homepage</a><a class="link" href="/health-education/">Browse health education</a></div></div></header>''' + FOOT + TAIL
open(OUT + '/404.html', 'w', encoding='utf-8').write(nf)

# ================= robots / sitemap / headers / redirects =================
pages = ['/', '/about/', '/consultations/', '/health-education/', '/womens-health/', '/gut-health/', '/skin-and-hair/', '/medical-cosmetology/', '/videos/', '/partnerships/', '/contact/']
pri = {'/': '1.0', '/about/': '0.8', '/consultations/': '0.9', '/partnerships/': '0.8', '/contact/': '0.6'}
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in pages:
    sm += f'  <url>\n    <loc>{ROOT}{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>\n'
sm += '</urlset>\n'
open(OUT + '/sitemap.xml', 'w').write(sm)
open(OUT + '/robots.txt', 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {ROOT}/sitemap.xml\n')
open(OUT + '/_headers', 'w').write('''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()
/images/*
  Cache-Control: public, max-age=2592000
/favicon.*
  Cache-Control: public, max-age=2592000
''')
open(OUT + '/_redirects', 'w').write('/index.html  /  301\n/home  /  301\n')

# ================= zip =================
if os.path.exists('glodoc-seo-deploy.zip'): os.remove('glodoc-seo-deploy.zip')
with zipfile.ZipFile('glodoc-seo-deploy.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for r, _, fs in os.walk(OUT):
        for f in fs:
            full = os.path.join(r, f); z.write(full, os.path.relpath(full, OUT))
print(sorted((i.filename, i.file_size) for i in zipfile.ZipFile('glodoc-seo-deploy.zip').infolist()))
