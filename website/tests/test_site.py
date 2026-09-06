from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

ROOT=Path(__file__).resolve().parents[1]
HTML=sorted(ROOT.glob('*.html'))
REQUIRED={'index.html','framework.html','research.html','publications.html','cases.html','about.html','participate.html','404.html'}
VERIFIED_EXTERNAL={
'https://github.com/Kasho-Minhena/lex-cybernetica',
'https://github.com/Kasho-Minhena/lex-cybernetica/releases/tag/v2.0.0',
'https://github.com/Kasho-Minhena/lex-cybernetica/releases/download/v2.0.0/Lex-Cybernetica-v2.0.pdf',
'https://github.com/Kasho-Minhena/lex-cybernetica/releases/download/v2.0.0/Lex-Cybernetica-v2.0.docx',
'https://duck-14.gitbook.io/lex-cybernetica',
'https://zenodo.org/records/22234758',
'https://doi.org/10.5281/zenodo.22234758',
'https://www.linkedin.com/feed/update/urn:li:ugcPost:7500589433096794115/?actorCompanyId=143609964',
'https://github.com/Kasho-Minhena/lex-cybernetica/blob/main/docs/SUMMARY.md',
'https://github.com/Kasho-Minhena/the-measure-of-mira-chen',
'https://github.com/Kasho-Minhena/seven-minutes',
'https://github.com/Kasho-Minhena/the-dependence-protocol',
'https://github.com/Kasho-Minhena/the-attitude-clause',
}

def soup(path): return BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')

def test_required_files_exist():
    assert REQUIRED == {p.name for p in HTML}
    for p in ['assets/css/site.css','assets/js/site.js','CNAME','robots.txt','sitemap.xml','docs/ARCHITECTURE.md','docs/ALGORITHM.md']:
        assert (ROOT/p).exists(), p

def test_cname_exact():
    assert (ROOT/'CNAME').read_text().strip()=='lex-cybernetica.com'

def test_page_semantics_and_metadata():
    titles=[]
    for path in HTML:
        s=soup(path)
        assert s.html and s.html.get('lang')=='en', path.name
        assert s.find('meta',attrs={'name':'viewport'}), path.name
        d=s.find('meta',attrs={'name':'description'})
        assert d and len(d.get('content',''))>=50, path.name
        assert s.title and 'Lex-Cybernetica' in s.title.get_text(), path.name
        titles.append(s.title.get_text(strip=True))
        assert s.find('main',id='main'), path.name
        assert s.find('header'), path.name
        assert s.find('nav',attrs={'aria-label':'Primary'}), path.name
        assert s.find('footer'), path.name
        assert s.find('h1'), path.name
        skip=s.find('a',class_='skip-link')
        assert skip and skip.get('href')=='#main', path.name
        assert s.find('meta',attrs={'http-equiv':'Content-Security-Policy'}), path.name
    assert len(titles)==len(set(titles)), 'Page titles must be unique'

def test_internal_links_resolve():
    for path in HTML:
        s=soup(path)
        for a in s.find_all('a',href=True):
            href=a['href']
            if href.startswith(('#','mailto:','tel:')): continue
            parsed=urlparse(href)
            if parsed.scheme: continue
            target=(ROOT/href.split('#',1)[0])
            assert target.exists(), f'{path.name}: broken link {href}'

def test_external_links_are_verified_and_hardened():
    for path in HTML:
        s=soup(path)
        for a in s.find_all('a',href=True):
            href=a['href']
            if href.startswith('https://'):
                assert href in VERIFIED_EXTERNAL, f'{path.name}: unverified external URL {href}'
                if a.get('target')=='_blank':
                    rel=set(a.get('rel',[]))
                    assert {'noopener','noreferrer'} <= rel, f'{path.name}: unsafe target blank {href}'
            elif '://' in href:
                raise AssertionError(f'{path.name}: non-HTTPS external URL {href}')

def test_no_forms_trackers_or_remote_scripts():
    for path in HTML:
        s=soup(path)
        assert not s.find('form'), path.name
        for script in s.find_all('script',src=True):
            assert not urlparse(script['src']).scheme, f'{path.name}: remote script {script["src"]}'
        assert not s.find('iframe'), path.name
    text='\n'.join(p.read_text(encoding='utf-8') for p in HTML)
    forbidden=['google-analytics','googletagmanager','facebook.com/tr','hotjar','segment.com','mixpanel']
    assert not any(x in text.lower() for x in forbidden)

def test_legal_status_on_every_page():
    for path in HTML:
        text=soup(path).get_text(' ',strip=True).lower()
        assert 'consultation draft' in text, path.name
        assert 'not enacted law' in text, path.name

def test_no_placeholders_or_secrets():
    all_text='\n'.join(p.read_text(encoding='utf-8') for p in ROOT.rglob('*') if p.is_file() and 'docs' not in p.parts and 'tests' not in p.parts and p.suffix in {'.html','.css','.js','.txt','.xml'})
    for token in ['TODO','TBD','CHANGEME','YOUR_EMAIL','API_KEY','SECRET_KEY','PASSWORD=','localhost','127.0.0.1']:
        assert token.lower() not in all_text.lower(), token
    # Public copy may name Lex Studio but must not expose internal route/host/repo/path details.
    assert not re.search(r'Lex Studio.{0,120}(https?://|[A-Z]:\\|/api/|github\.com)',all_text,re.I|re.S)

def test_canonical_urls():
    for path in HTML:
        s=soup(path)
        link=s.find('link',rel='canonical')
        assert link and link['href'].startswith('https://lex-cybernetica.com/'), path.name

def test_sitemap_contains_public_pages():
    xml=(ROOT/'sitemap.xml').read_text(encoding='utf-8')
    for name in ['framework.html','research.html','publications.html','cases.html','about.html','participate.html']:
        assert f'https://lex-cybernetica.com/{name}' in xml
    assert '404.html' not in xml

def test_accessible_mobile_menu_hooks():
    for path in HTML:
        s=soup(path)
        btn=s.find('button',attrs={'data-nav-toggle':True})
        nav=s.find('nav',attrs={'data-nav':True})
        assert btn and btn.get('aria-controls')=='primary-nav' and btn.get('aria-expanded')=='false'
        assert nav and nav.get('id')=='primary-nav'

def test_active_nav_present_on_public_pages():
    for path in HTML:
        if path.name=='404.html': continue
        s=soup(path)
        active=s.find('nav').find('a',attrs={'aria-current':'page'})
        assert active and active.get('href')==path.name

def test_size_budget():
    total=sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file() and 'tests' not in p.parts and 'docs' not in p.parts)
    assert total < 250_000, total
