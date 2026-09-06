from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
HTML=sorted(ROOT.glob('*.html'))

DANGEROUS_SCHEMES=('javascript:','data:text/html','vbscript:','file:')
EVENT_RE=re.compile(r'^on[a-z]+$',re.I)
PRIVATE_PATTERNS=[
    r'[A-Z]:\\[^\s<]+',
    r'localhost(?::\d+)?',
    r'127\.0\.0\.1',
    r'0\.0\.0\.0',
    r'api[_-]?key',
    r'bearer\s+[A-Za-z0-9._-]+',
    r'password\s*=',
    r'secret\s*=',
]

def parse(p): return BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')

def test_no_executable_url_schemes_or_inline_handlers():
    for path in HTML:
        s=parse(path)
        for tag in s.find_all(True):
            for attr,val in tag.attrs.items():
                assert not EVENT_RE.match(attr), f'{path.name}: inline handler {attr}'
                values=val if isinstance(val,list) else [val]
                for x in values:
                    if isinstance(x,str):
                        low=x.strip().lower()
                        assert not low.startswith(DANGEROUS_SCHEMES), f'{path.name}: dangerous URL/value {x}'
        for script in s.find_all('script'):
            assert script.get('src'), f'{path.name}: inline script not allowed'

def test_csp_denies_network_and_plugins():
    for path in HTML:
        s=parse(path)
        meta=s.find('meta',attrs={'http-equiv':'Content-Security-Policy'})
        csp=meta.get('content','')
        for directive in ["default-src 'self'","connect-src 'none'","object-src 'none'","base-uri 'self'","form-action 'self'"]:
            assert directive in csp, f'{path.name}: missing CSP directive {directive}'
        assert '*' not in csp
        assert 'unsafe-inline' not in csp
        assert 'unsafe-eval' not in csp

def test_no_private_infrastructure_or_credentials():
    text='\n'.join(p.read_text(encoding='utf-8') for p in ROOT.rglob('*') if p.is_file() and 'docs' not in p.parts and 'tests' not in p.parts and p.suffix in {'.html','.js','.css','.xml','.txt'})
    for pat in PRIVATE_PATTERNS:
        assert not re.search(pat,text,re.I), f'possible private/secret pattern: {pat}'

def test_no_user_data_collection_surface():
    for path in HTML:
        s=parse(path)
        assert not s.find('form')
        assert not s.find('input')
        assert not s.find('textarea')
        assert not s.find('select')
        assert not s.find(attrs={'contenteditable':True})

def test_external_navigation_has_no_opener_leak():
    for path in HTML:
        s=parse(path)
        for a in s.find_all('a',href=True):
            if a['href'].startswith('https://') and a.get('target')=='_blank':
                rel=set(a.get('rel',[]))
                assert 'noopener' in rel and 'noreferrer' in rel

def test_sitemap_is_well_formed_and_same_origin_only():
    tree=ET.parse(ROOT/'sitemap.xml')
    ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    locs=[x.text for x in tree.findall('.//s:loc',ns)]
    assert len(locs)==7
    for loc in locs:
        u=urlparse(loc)
        assert u.scheme=='https' and u.netloc=='lex-cybernetica.com'

def test_css_has_required_responsive_and_reduced_motion_guards():
    css=(ROOT/'assets/css/site.css').read_text(encoding='utf-8')
    assert '@media (max-width:980px)' in css
    assert '@media (max-width:650px)' in css
    assert '@media (prefers-reduced-motion:reduce)' in css
    assert css.count('{')==css.count('}'), 'unbalanced CSS braces'
    assert 'width:100vw' not in css.replace(' ','').lower(), '100vw can create horizontal overflow'

def test_no_http_mixed_content():
    for path in HTML:
        text=path.read_text(encoding='utf-8').lower()
        assert 'http://' not in text

def test_404_has_recovery_route():
    s=parse(ROOT/'404.html')
    assert s.find('a',href='index.html')
