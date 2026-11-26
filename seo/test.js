const {chromium}=require('playwright');const http=require('http');const fs=require('fs');const path=require('path');
const root=path.resolve('site-seo');
const types={'.html':'text/html','.css':'text/css','.js':'text/javascript','.jpg':'image/jpeg','.webp':'image/webp','.png':'image/png','.svg':'image/svg+xml','.xml':'text/xml','.txt':'text/plain'};
const srv=http.createServer((q,r)=>{let u=decodeURIComponent(q.url.split('?')[0]);let f=path.join(root,u);
 if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
 if(!fs.existsSync(f)){r.writeHead(404,{'content-type':'text/html'});return r.end(fs.readFileSync(path.join(root,'404.html')));}
 r.writeHead(200,{'content-type':types[path.extname(f)]||'application/octet-stream'});r.end(fs.readFileSync(f));});
(async()=>{await new Promise(r=>srv.listen(8099,r));
const b=await chromium.launch();const pages=['/','/about/','/consultations/','/health-education/','/womens-health/','/gut-health/','/skin-and-hair/','/medical-cosmetology/','/videos/','/partnerships/','/contact/','/nope'];
const bad=[];const seen=new Set();
for(const vp of [{width:1280,height:800},{width:390,height:800}]){
 const ctx=await b.newContext({viewport:vp});
 for(const p of pages){const pg=await ctx.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));
  pg.on('requestfailed',r=>{if(r.url().startsWith('http://localhost'))errs.push('reqfail '+r.url())});
  pg.on('response',r=>{if(r.url().startsWith('http://localhost')&&r.status()>=400&&p!=='/nope')errs.push(r.status()+' '+r.url())});
  await pg.goto('http://localhost:8099'+p,{waitUntil:'networkidle'});
  const d=await pg.evaluate(()=>{const j=[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>{try{JSON.parse(s.textContent);return 1}catch(e){return 0}});
   return {title:document.title,desc:(document.querySelector('meta[name=description]')||{}).content,canon:(document.querySelector('link[rel=canonical]')||{}).href,h1:document.querySelectorAll('h1').length,h2:document.querySelectorAll('h2').length,
   ov:document.documentElement.scrollWidth>innerWidth+1,ld:j,noalt:[...document.images].filter(i=>!i.getAttribute('alt')).length,broken:[...document.images].filter(i=>i.complete&&!i.naturalWidth).length,
   links:[...document.querySelectorAll('a[href^="/"]')].map(a=>a.getAttribute('href')),forms:[...document.forms].map(f=>f.name)}});
  if(vp.width===1280){console.log(p.padEnd(24),String(d.title.length).padStart(3),String((d.desc||'').length).padStart(4),'h1:'+d.h1,'h2:'+d.h2,'ld:'+d.ld.join(''),'forms:'+d.forms.join(','),d.canon||'-');d.links.forEach(l=>seen.add(l.split('#')[0]||'/'));}
  if(d.ov)bad.push(vp.width+' overflow '+p);if(d.noalt)bad.push('noalt '+p);if(d.broken)bad.push('broken img '+p);if(d.h1!==1)bad.push('h1 count '+p+' '+d.h1);errs.forEach(e=>bad.push(p+' '+e));
  await pg.close();}
 await ctx.close();}
// link check
const ctx=await b.newContext();for(const l of seen){const r=await ctx.request.get('http://localhost:8099'+l);if(r.status()!==200)bad.push('link '+l+' '+r.status());}
// form submission check (live flag) 
const pg=await ctx.newPage();let posted=null;await pg.route('**/',r=>{if(r.request().method()==='POST'){posted=r.request().postData();r.fulfill({status:200,body:'ok'})}else r.continue()});
await pg.goto('http://localhost:8099/contact/');await pg.fill('#c-name','Test');await pg.fill('#c-email','a@b.co');await pg.selectOption('#c-reason','A brand partnership');await pg.fill('#c-msg','hello');await pg.click('button[type=submit]');await pg.waitForTimeout(600);
console.log('form posted:',posted);console.log('status:',await pg.textContent('.enq-status'));
// mobile menu
const m=await b.newContext({viewport:{width:390,height:800}});const mp=await m.newPage();await mp.goto('http://localhost:8099/about/');await mp.click('.menu summary');console.log('menu links visible:',await mp.locator('.menu nav a:visible').count());
// homepage animation hooks still present
await pg.goto('http://localhost:8099/');console.log('letters:',await pg.locator('.reveal .l').count(),'bignum:',await pg.textContent('.bignum'));
console.log('PROBLEMS:',bad.length?bad:'none');await b.close();srv.close();})();
