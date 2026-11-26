import re,shutil,zipfile,os
from PIL import Image
s=open('glodoc-site.html',encoding='utf-8').read()
a='<title>THEGLODOC</title>\n<meta name="claude:viewport-fit-sides" content="cover">'
assert s.count(a)==1
s=s.replace(a,'<title>Dr. Athmika Prakash | THEGLODOC</title>')
# central config -> config.js
m=re.search(r'<script id="site-config">\n(.*?)</script>',s,re.S); assert m
cfg=m.group(1)
s=s.replace(m.group(0),'<script src="config.js"></script>')
names=['portrait.jpg','video-1.jpg','video-2.jpg','video-3.jpg','video-4.jpg','video-5.jpg']
srcs=['photos/portrait.jpg']+[f'thumbs/short-{i}.jpg' for i in range(1,6)]
it=iter(names)
s,n=re.subn(r'src="data:image/jpeg;base64,[^"]+"',lambda m:'src="images/'+next(it)+'"',s); assert n==6
shutil.rmtree('site',ignore_errors=True); os.makedirs('site/images')
for a,b in zip(srcs,names):
    Image.open(a).convert('RGB').save('site/images/'+b,quality=82,optimize=True,progressive=True)
for f in ['favicon.svg','favicon.png','apple-touch-icon.png']: shutil.copy('icons/'+f,'site/'+f)
open('site/config.js','w',encoding='utf-8').write(cfg)
open('site/robots.txt','w').write('User-agent: *\nAllow: /\n\nSitemap: https://theglodoc.in/sitemap.xml\n')
import datetime
open('site/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url>\n    <loc>https://theglodoc.in/</loc>\n    <lastmod>'+datetime.date.today().isoformat()+'</lastmod>\n  </url>\n</urlset>\n')
head=('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
 '<link rel="icon" type="image/svg+xml" href="favicon.svg">\n<link rel="icon" type="image/png" sizes="64x64" href="favicon.png">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
 '<link rel="canonical" href="https://theglodoc.in/">\n<meta property="og:url" content="https://theglodoc.in/">\n<meta property="og:type" content="website">\n<meta property="og:title" content="Dr. Athmika Prakash | THEGLODOC">\n'
 '<meta property="og:description" content="Doctor, creator and vlogger. 4,000+ patient consultations completed. Follow @the.glodoc on Instagram.">\n'
 '<meta property="og:image" content="https://theglodoc.in/images/portrait.jpg">\n'
 '<style>html{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style>\n'
 '<script>window.GLODOC_LIVE=true</script>\n')
open('site/index.html','w',encoding='utf-8').write(head+s+'\n</body>\n</html>\n')
if os.path.exists('glodoc-deploy.zip'): os.remove('glodoc-deploy.zip')
with zipfile.ZipFile('glodoc-deploy.zip','w',zipfile.ZIP_DEFLATED) as z:
    for root,_,files in os.walk('site'):
        for f in files:
            full=os.path.join(root,f); z.write(full,os.path.relpath(full,'site'))
zz=zipfile.ZipFile('glodoc-deploy.zip'); print(zz.testzip(), sorted((i.filename,i.file_size) for i in zz.infolist()))
