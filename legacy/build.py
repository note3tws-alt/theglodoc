s=open('glodoc-site.html',encoding='utf-8').read()
a='<title>Glodoc Website</title>\n<meta name="claude:viewport-fit-sides" content="cover">'
assert s.count(a)==1
s=s.replace(a,'<title>Dr. Athmika Prakash | Glodoc</title>\n<meta name="description" content="Dr. Athmika Prakash (Glodoc) is a health educator and certified consultant medical cosmetologist. Media kit and partnership details for brands.">\n<style>html{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>')
open('netlify/glodoc-site/index.html','w',encoding='utf-8').write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'+s+'\n</body>\n</html>\n')
