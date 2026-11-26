import re
src=open('glodoc-site.before-refine.html',encoding='utf-8').read()
uris=re.findall(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+',src); assert len(uris)==6
P,T=uris[0],uris[1:]
LOGO='<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="16" fill="#4a5c4b"/><path fill="#ffffff" d="M16 5c.7 6.6 3.7 9.6 11 11-7.3 1.4-10.3 4.4-11 11-.7-6.6-3.7-9.6-11-11 7.3-1.4 10.3-4.4 11-11z"/></svg>'
IG='https://www.instagram.com/the.glodoc/'; YT='https://www.youtube.com/@The.glodoc'
vids=[("5NUlKnJgj9U","Gizele, Bigg Boss Malayalam 7"),("s0Oc1AWgpJc","Gizele Thakral, part 2"),("pfNJ9mEm_Ak","Health checks before marriage"),("lvnbt2G5gy8","Straw bottles and ageing"),("AzWIMHtlgk0","Skin whitening treatment")]
cards="\n".join(f'      <a class="vid" href="https://www.youtube.com/shorts/{i}" target="_blank" rel="noopener"><img src="{T[n]}" alt="Video thumbnail: {t}" loading="lazy"><span>{t}</span></a>' for n,(i,t) in enumerate(vids))
h1='<h1 class="reveal" aria-label="Real health talk. With Dr. Athmika."><span aria-hidden="true"><span class="w"><i>Real</i></span> <span class="w"><i>health</i></span> <span class="w"><i>talk.</i></span> <span class="w"><i>With</i></span> <span class="nm"><span class="w"><i>Dr.</i></span> <span class="w"><i>Athmika.</i></span></span></span></h1>'
form=re.search(r'<form class="enq-form".*?</form>',src,re.S).group(0)
form=re.sub(r'\s*<div class="f"><label for="f-phone">.*?</div>','',form,flags=re.S)
form=form.replace('<option>Reel or Short</option>','<option>Instagram Reel</option>').replace('class="pill solid" id="f-submit"','class="btn" id="f-submit"')
assert 'class="btn" id="f-submit"' in form
assert 'f-phone' not in form and 'WhatsApp' not in form
formjs=re.search(r'<script>\n\(function\(\)\{\nvar form=document.getElementById\("partnership-form"\).*?</script>',src,re.S).group(0)
formjs=formjs.replace('message @the.glodoc on Instagram.";','message "+((window.SITE&&SITE.instagramHandle)||"@the.glodoc")+" on Instagram.";')
assert 'SITE.instagramHandle' in formjs, formjs[-600:]

html=f'''<title>THEGLODOC</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="THEGLODOC is Dr. Athmika Prakash, a doctor, creator and vlogger sharing everyday health education on Instagram. 4,000+ patient consultations completed; available for online and offline consultations.">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400&display=swap">
<script id="site-config">
/* theglodoc site settings. Edit these values to update them everywhere on the site. */
window.SITE = {{
  instagramFollowers: "12.3K",
  instagramHandle: "@the.glodoc",
  instagramUrl: "{IG}",
  youtubeUrl: "{YT}",
  consultations: "4,000+",
  email: "drathmika999@gmail.com",
  youtubeHandle: "@The.glodoc"
}};
</script>
<style>
/* Layout: full-width calm sections alternating white and pale sage; one serif family; generous whitespace, almost no rules or borders. */
:root{{
  --paper:#ffffff; --sage-50:#f3f5f0; --sage-100:#e3e9dd; --sage:#4a5c4b; --sage-dark:#384639;
  --ink:#1d261e; --muted:#5d685d; --line:rgba(29,38,30,.12);
  --serif:"Times New Roman",Tinos,Times,serif;
  --r:20px;
}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{background:var(--paper);color:var(--ink);font-family:var(--serif);font-size:18px;line-height:1.6}}
a{{color:inherit}}
a:focus-visible,button:focus-visible{{outline:2px solid var(--sage);outline-offset:3px}}
img{{max-width:100%}}
.wrap{{max-width:1160px;margin:0 auto;padding-block:112px;padding-left:max(24px,env(safe-area-inset-left,0px));padding-right:max(24px,env(safe-area-inset-right,0px))}}
.tint{{background:var(--sage-50)}}
.deep{{background:var(--sage);color:var(--paper)}}
h1,h2,h3{{font-family:var(--serif);font-weight:400;margin:0;text-wrap:balance;letter-spacing:-.01em}}
h1{{font-size:clamp(42px,5.4vw,68px);line-height:1.04}}
h2{{font-size:clamp(32px,3.8vw,48px);line-height:1.1}}
h3{{font-size:24px;line-height:1.2}}
p{{margin:0}}
.eyebrow{{font-size:13px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}}
.deep .eyebrow{{color:rgba(255,255,255,.75)}}
.lede{{font-size:20px;color:var(--muted);max-width:38ch}}
.hero-lede{{max-width:46ch}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:50px;padding:0 28px;border-radius:999px;border:1px solid var(--sage);background:var(--sage);color:var(--paper);font:inherit;font-size:16px;text-decoration:none;cursor:pointer;transition:background .2s,color .2s,border-color .2s}}
.btn:hover{{background:var(--sage-dark);border-color:var(--sage-dark)}}
.btn.ghost{{background:transparent;color:var(--sage)}}
.btn.ghost:hover{{background:var(--sage);color:var(--paper)}}
.deep .btn{{background:var(--paper);color:var(--sage);border-color:var(--paper)}}
.deep .btn:hover{{background:var(--sage-100);border-color:var(--sage-100)}}
.link{{text-decoration:none;border-bottom:1px solid currentColor;padding-bottom:2px}}
.link:hover{{color:var(--sage)}}

/* header */
.top{{position:absolute;inset:0 0 auto;z-index:5}}
.top .wrap{{padding-block:26px;display:flex;align-items:center;justify-content:space-between;gap:20px}}
.logo{{display:inline-flex;align-items:center;gap:12px;text-decoration:none;font-size:22px;letter-spacing:.08em}}
.logo svg{{width:32px;height:32px;flex:none}}
.nav{{display:flex;align-items:center;gap:34px}}
.nav a:not(.btn){{text-decoration:none;font-size:15px;color:var(--muted)}}
.nav a:not(.btn):hover{{color:var(--ink)}}
.nav .btn{{min-height:42px;padding:0 20px;font-size:15px}}

/* hero */
.hero{{background:var(--sage-100)}}
.hero .wrap{{padding-top:150px;padding-bottom:110px;display:grid;grid-template-columns:1.05fr .95fr;gap:72px;align-items:center}}
.hero .wrap>*{{min-width:0}}
.hero-copy{{display:flex;flex-direction:column;gap:28px}}
.hero .cred{{font-size:15px;letter-spacing:.06em;color:var(--muted)}}
.ig-row{{display:flex;flex-wrap:wrap;align-items:center;gap:18px 24px;margin-top:8px}}
.ig-count{{display:flex;flex-direction:column;line-height:1.2}}
.ig-count strong{{font-weight:400;font-size:28px}}
.ig-count span{{font-size:14px;color:var(--muted)}}
.portrait{{border-radius:var(--r);overflow:hidden;aspect-ratio:4/5;max-width:100%;background:var(--sage-50);animation:portraitup 1.4s cubic-bezier(.19,1,.22,1) .2s both}}
.portrait img{{width:100%;height:100%;object-fit:cover;object-position:50% 14%;display:block}}

/* name animation (only the name moves) */
.reveal .w{{display:inline-block;white-space:nowrap}}
.reveal .w i{{font-style:normal}}
.reveal .l{{display:inline-block}}
.reveal .nm .l{{color:var(--sage);animation:chrise 1s cubic-bezier(.19,1,.22,1) both,glint 6s ease-in-out infinite;animation-delay:calc(var(--c)*40ms + .2s),calc(var(--c)*110ms + 2.4s)}}
@keyframes chrise{{from{{transform:translateY(110%) rotate(6deg);opacity:0}}to{{transform:none;opacity:1}}}}
@keyframes glint{{0%,9%,100%{{transform:none;text-shadow:none}}4.5%{{transform:translateY(-6%);text-shadow:0 0 22px rgba(255,255,255,.95)}}}}
@keyframes portraitup{{from{{opacity:0;transform:translateY(28px)}}to{{opacity:1;transform:none}}}}

/* consultations */
.consult .wrap{{display:grid;grid-template-columns:.9fr 1.1fr;gap:72px;align-items:center}}
.consult .wrap>*{{min-width:0}}
.bignum{{font-size:clamp(84px,11vw,148px);line-height:.9;letter-spacing:-.03em;color:var(--sage);font-variant-numeric:tabular-nums;white-space:nowrap}}
.bignum+p{{margin-top:14px;font-size:20px;color:var(--muted)}}
.consult-copy{{display:flex;flex-direction:column;gap:22px}}
.modes{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:10px}}
.modes div{{background:var(--sage-50);border-radius:16px;padding:26px 24px}}
.modes p{{margin-top:6px;font-size:16px;color:var(--muted)}}

/* instagram */
.ig .wrap{{text-align:center;display:flex;flex-direction:column;align-items:center;gap:22px}}
.ig .handle{{font-size:clamp(40px,6vw,76px);line-height:1;letter-spacing:-.02em}}
.ig .followers{{font-size:20px;color:rgba(255,255,255,.85)}}
.ig .also{{font-size:15px;color:rgba(255,255,255,.75)}}

/* focus */
.section-head{{display:flex;flex-direction:column;gap:14px;max-width:40ch;margin-bottom:56px}}
.focus-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:40px}}
.focus-grid>div{{min-width:0}}
.focus-grid p{{margin-top:10px;font-size:16px;color:var(--muted)}}

/* videos */
.vids-head{{display:flex;flex-wrap:wrap;align-items:end;justify-content:space-between;gap:16px;margin-bottom:40px}}
.vids{{display:grid;grid-template-columns:repeat(5,1fr);gap:18px}}
.vid{{display:flex;flex-direction:column;gap:12px;text-decoration:none;min-width:0}}
.vid img{{width:100%;aspect-ratio:2/3;object-fit:cover;border-radius:14px;display:block;transition:transform .5s cubic-bezier(.2,.8,.2,1)}}
.vid:hover img{{transform:translateY(-4px)}}
.vid span{{font-size:16px;line-height:1.3}}

/* partnerships */
.partner .wrap{{display:grid;grid-template-columns:.9fr 1.1fr;gap:72px}}
.partner .wrap>*{{min-width:0}}
.partner-copy{{display:flex;flex-direction:column;gap:22px;align-items:flex-start}}
.stats{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:44px}}
.stats div{{background:var(--sage-50);border-radius:16px;padding:22px}}
.stats strong{{display:block;font-weight:400;font-size:clamp(28px,3vw,36px);line-height:1.1;color:var(--sage)}}
.stats span{{font-size:15px;color:var(--muted)}}
.formats{{display:grid;gap:26px}}
.formats p{{margin-top:4px;font-size:16px;color:var(--muted)}}

/* enquiry form */
.enq{{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px}}
.enq>*{{min-width:0}}
.enq-intro{{display:flex;flex-direction:column;gap:16px}}
.enq-form{{display:grid;grid-template-columns:1fr 1fr;gap:22px 24px}}
.enq-form .f{{display:flex;flex-direction:column;gap:8px;min-width:0}}
.enq-form .full{{grid-column:1/-1}}
.enq-form label{{font-size:14px;color:var(--muted)}}
.enq-form label span{{opacity:.8}}
.enq-form input,.enq-form select,.enq-form textarea{{font:inherit;font-size:17px;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:13px 15px;width:100%;min-width:0}}
.enq-form textarea{{resize:vertical;min-height:130px}}
.enq-form input:focus,.enq-form select:focus,.enq-form textarea:focus{{outline:none;border-color:var(--sage);box-shadow:0 0 0 3px var(--sage-100)}}
.enq-form button{{font-size:16px}}
.enq-form button[disabled]{{opacity:.6;cursor:progress}}
.enq-actions{{flex-direction:row!important;flex-wrap:wrap;align-items:center;gap:16px!important}}
.enq-status{{margin:0;font-size:16px;color:var(--sage)}}
.enq-status.err{{color:#9b2c2c}}
.hp{{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}}

/* footer */
footer .wrap{{padding-block:64px 40px;display:grid;grid-template-columns:1fr auto;gap:28px 40px;align-items:start}}
footer .wrap>*{{min-width:0}}
.foot-brand{{display:flex;flex-direction:column;gap:12px}}
.foot-brand p{{font-size:16px;color:var(--muted)}}
.foot-brand .foot-email a{{color:var(--ink);user-select:all;overflow-wrap:anywhere}}
.foot-links{{display:flex;flex-wrap:wrap;gap:12px 28px;font-size:16px}}
.fine{{grid-column:1/-1;display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;font-size:14px;color:var(--muted);padding-top:24px;border-top:1px solid var(--line)}}

@media (max-width:980px){{
  .focus-grid{{grid-template-columns:1fr 1fr}}
  .vids{{grid-template-columns:repeat(5,minmax(150px,1fr));overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:6px}}
  .vid{{scroll-snap-align:start}}
}}
@media (max-width:820px){{
  .wrap{{padding-block:76px}}
  .nav a:not(.btn){{display:none}}
  .hero .wrap{{grid-template-columns:1fr;padding-top:112px;padding-bottom:72px;gap:44px}}
  .consult .wrap,.partner .wrap,.enq{{grid-template-columns:1fr;gap:40px}}
  .enq-form{{grid-template-columns:1fr}}
  footer .wrap{{grid-template-columns:1fr}}
}}
@media (max-width:480px){{
  .modes,.focus-grid{{grid-template-columns:1fr}}
  .stats{{grid-template-columns:1fr}}
  .logo{{font-size:18px}}
  .nav .btn{{padding:0 16px;font-size:14px}}
}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}html{{scroll-behavior:auto}}}}
</style>

<div class="top">
  <div class="wrap">
    <a class="logo" href="#top" aria-label="theglodoc home">{LOGO}<span>THEGLODOC</span></a>
    <nav class="nav" aria-label="Main">
      <a href="#consultations">Consultations</a>
      <a href="#focus">Focus</a>
      <a href="#partnerships">Partnerships</a>
      <a class="btn" href="{IG}" data-site-href="instagramUrl" target="_blank" rel="noopener">Follow on Instagram</a>
    </nav>
  </div>
</div>

<header class="hero" id="top">
  <div class="wrap">
    <div class="hero-copy">
      {h1}
      <p class="lede hero-lede">Doctor, certified consultant medical cosmetologist, health educator and content creator, sharing clear, everyday health advice. People's most viewed and favourite health influencer.</p>
      <p class="cred">BHMS, FMC · Based in India</p>
      <div class="ig-row">
        <a class="btn" href="{IG}" data-site-href="instagramUrl" target="_blank" rel="noopener">Follow on Instagram</a>
        <div class="ig-count"><strong data-site="instagramFollowers">12.3K</strong><span>followers on Instagram</span></div>
      </div>
    </div>
    <div class="portrait"><img src="{P}" alt="Portrait of Dr. Athmika Prakash wearing a stethoscope" width="980" height="1280"></div>
  </div>
</header>

<main>
<section class="consult" id="consultations">
  <div class="wrap">
    <div>
      <p class="bignum" data-site="consultations">4,000+</p>
      <p>patient consultations completed</p>
    </div>
    <div class="consult-copy">
      <p class="eyebrow">Consultations</p>
      <h2>Available for online and offline consultations.</h2>
      <div class="modes">
        <div><h3>Online</h3><p>Consult from wherever you are.</p></div>
        <div><h3>Offline</h3><p>Meet in person for a consultation.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="ig deep" id="instagram">
  <div class="wrap">
    <p class="eyebrow">Instagram</p>
    <p class="handle" data-site="instagramHandle">@the.glodoc</p>
    <p class="followers"><span data-site="instagramFollowers">12.3K</span> followers</p>
    <a class="btn" href="{IG}" data-site-href="instagramUrl" target="_blank" rel="noopener">Follow on Instagram</a>
    <p class="also">Also on <a class="link" href="{YT}" data-site-href="youtubeUrl" target="_blank" rel="noopener">YouTube</a></p>
  </div>
</section>

<section id="focus">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Focus</p>
      <h2>What she talks about.</h2>
    </div>
    <div class="focus-grid">
      <div><h3>Everyday health</h3><p>Gut health, hormones and routine tests.</p></div>
      <div><h3>Women's health</h3><p>Periods, checkups and pregnancy myths.</p></div>
      <div><h3>Skin and hair</h3><p>What works, and what's a myth.</p></div>
      <div><h3>Procedures</h3><p>What they are and who they suit.</p></div>
    </div>
  </div>
</section>

<section class="tint" id="videos">
  <div class="wrap">
    <div class="vids-head">
      <h2>Featured videos.</h2>
      <a class="link" href="{YT}" data-site-href="youtubeUrl" target="_blank" rel="noopener">More on YouTube</a>
    </div>
    <div class="vids">
{cards}
    </div>
  </div>
</section>

<section class="partner" id="partnerships">
  <div class="wrap">
    <div class="partner-copy">
      <p class="eyebrow">Partnerships</p>
      <h2>Partner with THEGLODOC.</h2>
      <p class="lede">For health, wellness, skincare and haircare brands. Rates on request.</p>
      <a class="btn ghost" href="#enquiry">Send an enquiry</a>
    </div>
    <div>
      <div class="stats">
        <div><strong data-site="instagramFollowers">12.3K</strong><span>Instagram followers</span></div>
        <div><strong data-site="consultations">4,000+</strong><span>patient consultations</span></div>
      </div>
      <div class="formats">
        <div><h3>Instagram Reels</h3><p>A short video explaining what the product does and who it suits.</p></div>
        <div><h3>Stories</h3><p>A Story set with a link, for launches and offers.</p></div>
        <div><h3>Series</h3><p>Several videos for products that need more explanation.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="tint" id="enquiry">
  <div class="wrap enq">
    <div class="enq-intro">
      <p class="eyebrow">Enquiry</p>
      <h2>Work with Dr. Athmika.</h2>
      <p class="lede">Tell us about your brand and campaign.</p>
    </div>
    {form}
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <div class="foot-brand">
      <a class="logo" href="#top" aria-label="theglodoc home">{LOGO}<span>THEGLODOC</span></a>
      <p>Health education by Dr. Athmika Prakash.</p>
      <p class="foot-email">Email <a class="link" href="mailto:drathmika999@gmail.com" data-site="email" data-site-mailto="email">drathmika999@gmail.com</a></p>
      <p class="foot-email">YouTube <a class="link" href="{YT}" data-site-href="youtubeUrl" target="_blank" rel="noopener"><span data-site="youtubeHandle">@The.glodoc</span></a></p>
    </div>
    <div class="foot-links">
      <a class="link" href="{IG}" data-site-href="instagramUrl" target="_blank" rel="noopener">Instagram <span data-site="instagramHandle">@the.glodoc</span></a>
      <a class="link" href="#enquiry">Partnership enquiry</a>
    </div>
    <div class="fine"><span>Videos are for general education and do not replace a medical consultation.</span><span>© 2026 THEGLODOC</span></div>
  </div>
</footer>

<script>
(function(){{
  var S=window.SITE||{{}};
  document.querySelectorAll("[data-site]").forEach(function(el){{var v=S[el.getAttribute("data-site")];if(v)el.textContent=v;}});
  document.querySelectorAll("[data-site-href]").forEach(function(el){{var v=S[el.getAttribute("data-site-href")];if(v)el.href=v;}});
  document.querySelectorAll("[data-site-mailto]").forEach(function(el){{var v=S[el.getAttribute("data-site-mailto")];if(v)el.href="mailto:"+v;}});
  /* count-up for the consultations figure, runs once when it scrolls into view */
  var big=document.querySelector(".bignum");
  if(big&&!matchMedia("(prefers-reduced-motion: reduce)").matches&&"IntersectionObserver" in window){{
    var full=big.textContent.trim(),target=parseInt(full.replace(/[^0-9]/g,""),10),suffix=full.replace(/^[0-9,]+/,"");
    if(target>1){{
      var io=new IntersectionObserver(function(es){{
        if(!es[0].isIntersecting)return;io.disconnect();
        var t0=null,dur=1400;
        function step(t){{
          if(t0===null)t0=t;var k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,3);
          var n=Math.max(1,Math.round(1+(target-1)*e));
          big.textContent=n.toLocaleString("en-US")+(k===1?suffix:"");
          if(k<1)requestAnimationFrame(step);else big.textContent=full;
        }}
        big.textContent="1";requestAnimationFrame(step);
      }},{{threshold:.4}});
      io.observe(big);
    }}
  }}
  var c=0;
  document.querySelectorAll(".reveal .w i").forEach(function(w){{
    var inName=!!w.closest(".nm"),t=w.textContent;w.textContent="";
    t.split("").forEach(function(ch){{var s=document.createElement("span");s.className="l";if(inName)s.style.setProperty("--c",c++);s.textContent=ch;w.appendChild(s);}});
  }});
}})();
</script>
{formjs}
'''
open('glodoc-site.html','w',encoding='utf-8').write(html)
print(len(html))
