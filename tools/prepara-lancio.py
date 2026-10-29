#!/usr/bin/env python3
"""Prepara le pagine per la pubblicazione sul dominio definitivo.

Uso:
  python3 tools/prepara-lancio.py https://www.esempio.it [--cname] [--force] [--dry-run]

Cosa fa (solo libreria standard, può essere rieseguito):
  - rimuove noindex/nofollow/noarchive da tutte le pagine (404.html resta noindex);
  - aggiunge canonical, og:url, og:image, Twitter card e dati strutturati JSON-LD;
  - crea sitemap.xml e riscrive robots.txt;
  - con --cname scrive il file CNAME richiesto da GitHub Pages.

Si ferma se privacy.html contiene ancora segnaposto, a meno di --force.
I dati strutturati contengono solo informazioni già pubbliche e confermate sul sito:
orari e telefono dello studio vanno aggiunti solo dopo la conferma delle professioniste.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
START, END = '<!-- seo:start -->', '<!-- seo:end -->'
# Le pagine di servizio restano noindex e non devono comparire nella sitemap.
# chi-siamo.html è un redirect HTML permanente verso lo-studio.html.
SKIP_PAGES = {'404.html', 'chi-siamo.html'}
OG_IMAGE = 'assets/images/og-allieri-pagliari.jpg'

ADDRESS = {
    '@type': 'PostalAddress',
    'streetAddress': 'Via Giacomo Matteotti 11',
    'postalCode': '20877',
    'addressLocality': 'Roncello',
    'addressRegion': 'MB',
    'addressCountry': 'IT',
}


def die(message):
    sys.exit(f'Errore: {message}')


def parse_args(argv):
    flags = {a for a in argv if a.startswith('--')}
    args = [a for a in argv if not a.startswith('--')]
    if len(args) != 1 or not flags <= {'--cname', '--force', '--dry-run'}:
        die(__doc__)
    url = urlparse(args[0])
    if url.scheme != 'https' or not url.netloc or url.path not in ('', '/') or url.query or url.fragment:
        die('indica solo il dominio, con https (es. https://www.esempio.it)')
    return f'https://{url.netloc}', flags


def structured_data(page, base):
    org = {
        '@type': 'ProfessionalService',
        '@id': f'{base}/#studio',
        'name': 'Allieri & Pagliari — Psicologhe',
        'url': f'{base}/',
        'image': f'{base}/{OG_IMAGE}',
        'address': ADDRESS,
        'areaServed': 'Roncello (MB) e online',
    }
    people = {
        'valentina-allieri.html': {
            '@type': 'Person', 'name': 'Valentina Allieri', 'jobTitle': 'Psicologa clinica',
            'url': f'{base}/valentina-allieri.html', 'worksFor': {'@id': f'{base}/#studio'},
            'sameAs': ['https://www.miodottore.it/profilo/valentina-allieri'],
        },
        'silvia-pagliari.html': {
            '@type': 'Person', 'name': 'Silvia Pagliari', 'jobTitle': 'Psicologa clinica',
            'url': f'{base}/silvia-pagliari.html', 'worksFor': {'@id': f'{base}/#studio'},
            'telephone': '+39 353 425 9158',
        },
    }
    if page == 'index.html':
        return {'@context': 'https://schema.org', **org}
    if page in people:
        return {'@context': 'https://schema.org', **people[page]}
    return None


def seo_block(page, base, head):
    path = '' if page == 'index.html' else page
    page_url = f'{base}/{path}'
    title = re.search(r'<meta content="([^"]*)" property="og:title"/>', head)
    lines = [
        START,
        f'<link href="{page_url}" rel="canonical"/>',
        f'<meta content="{page_url}" property="og:url"/>',
        f'<meta content="{base}/{OG_IMAGE}" property="og:image"/>',
        '<meta content="1200" property="og:image:width"/>',
        '<meta content="630" property="og:image:height"/>',
        '<meta content="Allieri &amp; Pagliari — Psicologhe a Roncello e online" property="og:image:alt"/>',
        '<meta content="summary_large_image" name="twitter:card"/>',
    ]
    data = structured_data(page, base)
    if data:
        lines.append('<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>')
    lines.append(END)
    return '\n    '.join(lines) + '\n    ' if title else None


def main():
    base, flags = parse_args(sys.argv[1:])
    dry = '--dry-run' in flags
    privacy = (ROOT / 'privacy.html').read_text(encoding='utf-8')
    if 'privacy-placeholder' in privacy and '--force' not in flags:
        die('privacy.html contiene ancora segnaposto da completare. Usa --force solo per una prova.')

    pages = sorted(p.name for p in ROOT.glob('*.html') if p.name not in SKIP_PAGES)
    for page in pages:
        file = ROOT / page
        text = file.read_text(encoding='utf-8')
        text = re.sub(r'[ \t]*<meta[^>]*name="robots"[^>]*noindex[^>]*>\n?', '', text)
        text = re.sub(rf'[ \t]*{re.escape(START)}.*?{re.escape(END)}\n?', '', text, flags=re.S)
        block = seo_block(page, base, text)
        if block is None:
            die(f'{page}: meta og:title mancante, esegui prima la preparazione delle pagine')
        text = text.replace('</head>', '    ' + block.rstrip() + '\n  </head>', 1)
        if not dry:
            file.write_text(text, encoding='utf-8')

    urls = ''.join(
        f'  <url><loc>{base}/{"" if p == "index.html" else p}</loc></url>\n' for p in pages
    )
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'
    robots = f'User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n'
    if not dry:
        (ROOT / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
        (ROOT / 'robots.txt').write_text(robots, encoding='utf-8')
        if '--cname' in flags:
            (ROOT / 'CNAME').write_text(urlparse(base).netloc + '\n', encoding='utf-8')
    print(f'{"[prova] " if dry else ""}{len(pages)} pagine pronte per {base}')
    print('Prossimi passi: provare il sito in locale, pubblicare, inviare sitemap.xml a Search Console.')


if __name__ == '__main__':
    main()
