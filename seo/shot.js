const {chromium}=require('playwright');const http=require('http');const fs=require('fs');const path=require('path');
const root=path.resolve('site-seo');const types={'.html':'text/html','.css':'text/css','.js':'text/javascript','.jpg':'image/jpeg','.webp':'image/webp','.png':'image/png','.svg':'image/svg+xml'};
const srv=http.createServer((q,r)=>{let f=path.join(root,q.url.split('?')[0]);if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');if(!fs.existsSync(f)){r.writeHead(404);return r.end()}r.writeHead(200,{'content-type':types[path.extname(f)]||'text/plain'});r.end(fs.readFileSync(f))});
(async()=>{await new Promise(r=>srv.listen(8098,r));const b=await chromium.launch();
for(const [n,p,w,h,full] of [['sd-home','/',1280,800,false],['sd-about','/about/',1280,800,true],['sm-womens','/womens-health/',390,800,true],['sm-menu','/contact/',390,700,false]]){
 const c=await b.newContext({viewport:{width:w,height:h}});const pg=await c.newPage();await pg.goto('http://localhost:8098'+p,{waitUntil:'networkidle'});await pg.waitForTimeout(1800);
 if(n==='sm-menu')await pg.click('.menu summary');await pg.screenshot({path:'seo/'+n+'.png',fullPage:full});await c.close();}
await b.close();srv.close();})();
