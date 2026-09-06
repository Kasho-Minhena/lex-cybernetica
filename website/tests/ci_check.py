#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys, re, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
PAGES=['index.html','framework.html','research.html','publications.html','cases.html','about.html','participate.html','404.html']

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[]; self.scripts=[]; self.forms=0; self.iframes=0; self.h1=0; self.main=False; self.nav=False; self.footer=False; self.title=False; self.description=False; self.csp=False; self.skip=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        for k,v in attrs:
            if k.lower().startswith('on'):
                raise AssertionError(f'inline event handler {k}')
            if isinstance(v,str) and v.strip().lower().startswith(('javascript:','vbscript:','data:text/html')):
                raise AssertionError(f'dangerous attribute value {v}')
        if tag=='a' and 'href' in a:
            self.links.append((a['href'],a.get('target'),set((a.get('rel') or '').split())))
            if a.get('class')=='skip-link' or 'skip-link' in (a.get('class') or '').split(): self.skip=True
        if tag=='script': self.scripts.append(a.get('src'))
        if tag=='form': self.forms+=1
        if tag=='iframe': self.iframes+=1
        if tag=='h1': self.h1+=1
        if tag=='main': self.main=True
        if tag=='nav': self.nav=True
        if tag=='footer': self.footer=True
        if tag=='title': self.title=True
        if tag=='meta' and a.get('name')=='description': self.description=bool(a.get('content'))
        if tag=='meta' and a.get('http-equiv')=='Content-Security-Policy':
            self.csp=True
            c=a.get('content','')
            for x in ["default-src 'self'","connect-src 'none'","object-src 'none'","base-uri 'self'"]:
                assert x in c, f'missing CSP directive: {x}'

def fail(msg):
    print('FAIL:',msg,file=sys.stderr); sys.exit(1)

for name in PAGES:
    p=ROOT/name
    if not p.exists(): fail(f'missing {name}')
    text=p.read_text(encoding='utf-8')
    parser=AuditParser()
    try: parser.feed(text)
    except AssertionError as e: fail(f'{name}: {e}')
    for needed,val in [('title',parser.title),('description',parser.description),('main',parser.main),('nav',parser.nav),('footer',parser.footer),('h1',parser.h1==1),('skip link',parser.skip),('CSP',parser.csp)]:
        if not val: fail(f'{name}: missing/invalid {needed}')
    if parser.forms or parser.iframes: fail(f'{name}: forms/iframes prohibited in v1')
    for src in parser.scripts:
        if not src or urlparse(src).scheme: fail(f'{name}: inline/remote script prohibited')
    for href,target,rel in parser.links:
        u=urlparse(href)
        if u.scheme in ('http',): fail(f'{name}: mixed content {href}')
        if u.scheme=='https' and target=='_blank' and not {'noopener','noreferrer'} <= rel: fail(f'{name}: unsafe target blank {href}')
        if not u.scheme and not href.startswith('#'):
            target_path=ROOT/href.split('#',1)[0]
            if not target_path.exists(): fail(f'{name}: broken internal link {href}')
    low=text.lower()
    for token in ['todo','tbd','changeme','api_key','secret_key','password=','localhost','127.0.0.1']:
        if token in low: fail(f'{name}: forbidden placeholder/private token {token}')

if (ROOT/'CNAME').read_text(encoding='utf-8').strip()!='lex-cybernetica.com': fail('CNAME mismatch')
try: ET.parse(ROOT/'sitemap.xml')
except Exception as e: fail(f'sitemap XML invalid: {e}')
css=(ROOT/'assets/css/site.css').read_text(encoding='utf-8')
for media in ['@media (max-width:980px)','@media (max-width:650px)','@media (prefers-reduced-motion:reduce)']:
    if media not in css: fail(f'CSS missing {media}')
if css.count('{')!=css.count('}'): fail('unbalanced CSS')
js=(ROOT/'assets/js/site.js').read_text(encoding='utf-8')
if 'eval(' in js or 'innerHTML' in js: fail('unsafe JS primitive')
print('PASS: Lex-Cybernetica static-site CI checks')
