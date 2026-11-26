const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch();const root=path.resolve('t');
const serve=async p=>{await p.route('http://glodoc.test/**',r=>{const u=new URL(r.request().url());if(r.request().method()==='POST'){global.posted=r.request().postData();return r.fulfill({status:200,body:'ok'})}let f=u.pathname==='/'?'/index.html':u.pathname;const fp=path.join(root,f);if(!fs.existsSync(fp))return r.fulfill({status:404});r.fulfill({path:fp})});};
for(const [w,h,n] of [[1440,900,'d'],[820,1100,'tab'],[390,844,'m']]){
 const p=await b.newPage({viewport:{width:w,height:h}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});p.on('response',r=>{if(r.status()>=400)errs.push(r.status()+' '+r.url())});
 await serve(p);await p.goto('http://glodoc.test/',{waitUntil:'load'});await p.waitForTimeout(2600);
 const info=await p.evaluate(()=>({sw:document.documentElement.scrollWidth,iw:innerWidth,imgs:[...document.images].every(i=>i.complete&&i.naturalWidth>0),f:[...document.querySelectorAll('[data-site="instagramFollowers"]')].map(e=>e.textContent),title:document.title,igLinks:[...document.querySelectorAll('a[href*="instagram.com"]')].length,anchors:[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h!=='#top'&&!document.querySelector(h))}));
 console.log(n,JSON.stringify(info),errs);
 await p.screenshot({path:'shot-'+n+'.png',fullPage:true});await p.close();}
const p=await b.newPage();await serve(p);await p.goto('http://glodoc.test/');
await p.fill('#f-name','Test');await p.fill('#f-company','Brand');await p.fill('#f-email','t@example.com');await p.selectOption('#f-type','Instagram Reel');await p.fill('#f-msg','Hi');await p.click('#f-submit');await p.waitForTimeout(400);
console.log('posted',global.posted,'|',await p.textContent('#f-status'));
await b.close()})();
