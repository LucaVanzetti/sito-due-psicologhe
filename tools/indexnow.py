#!/usr/bin/env python3
"""Avvisa Bing (e gli altri motori IndexNow) delle pagine modificate.

Uso, dopo che la modifica è online:
  python3 tools/indexnow.py            # tutte le URL della sitemap
  python3 tools/indexnow.py faq.html   # solo le pagine indicate

La chiave è il file <chiave>.txt nella radice del sito: deve restare pubblicato.
Google non usa IndexNow: per Google resta la richiesta di indicizzazione in Search Console.
"""
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = (ROOT / 'CNAME').read_text().strip()
BASE = f'https://{HOST}'
NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'


def key():
    keys = [p for p in ROOT.glob('*.txt') if p.stem == p.read_text().strip() and len(p.stem) >= 8]
    if len(keys) != 1:
        sys.exit('Errore: serve un solo file chiave IndexNow (<chiave>.txt) nella radice')
    return keys[0].stem


def urls(pages):
    sitemap = [e.text for e in ET.parse(ROOT / 'sitemap.xml').iter(NS + 'loc')]
    if not pages:
        return sitemap
    chosen = [f'{BASE}/{"" if p == "index.html" else p}' for p in pages]
    unknown = set(chosen) - set(sitemap)
    if unknown:
        sys.exit(f'Errore: pagine non presenti nella sitemap: {sorted(unknown)}')
    return chosen


def main():
    k = key()
    body = {'host': HOST, 'key': k, 'keyLocation': f'{BASE}/{k}.txt', 'urlList': urls(sys.argv[1:])}
    request = urllib.request.Request(
        'https://api.indexnow.org/indexnow', data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json; charset=utf-8'}, method='POST')
    with urllib.request.urlopen(request, timeout=30) as response:
        print(f'IndexNow: {response.status}, {len(body["urlList"])} URL inviate')


if __name__ == '__main__':
    main()
