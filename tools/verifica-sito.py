#!/usr/bin/env python3
"""Controlla il sito locale senza rete o dipendenze esterne."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://' + (ROOT / 'CNAME').read_text().strip()
errors = []


class Page(HTMLParser):
  def __init__(self, path):
    super().__init__(convert_charrefs=True)
    self.path = path
    self.ids = set()
    self.links = []
    self.canonicals = []
    self.noindex = False
    self.h1 = 0

  def handle_starttag(self, tag, attrs):
    a = dict(attrs)
    if a.get('id'):
      if a['id'] in self.ids:
        errors.append(f'{self.path.name}: id duplicato {a["id"]}')
      self.ids.add(a['id'])
    self.h1 += tag == 'h1'
    if tag == 'meta' and a.get('name', '').lower() == 'robots':
      self.noindex |= 'noindex' in a.get('content', '').lower()
    if tag == 'link' and 'canonical' in a.get('rel', '').split():
      self.canonicals.append(a.get('href'))
    for key in ('href', 'src'):
      if a.get(key):
        self.links.append(a[key])
    if a.get('srcset'):
      self.links.extend(part.strip().split()[0] for part in a['srcset'].split(','))
    if tag == 'img':
      missing = {'alt', 'width', 'height'} - a.keys()
      if missing:
        errors.append(f'{self.path.name}: img priva di {sorted(missing)}')
      if re.search(r'\s[0-9]+w(?:\s*,|\s*$)', a.get('srcset', '')) and 'sizes' not in a:
        errors.append(f'{self.path.name}: srcset in larghezza senza sizes')


pages = {}
for path in ROOT.glob('*.html'):
  page = Page(path)
  page.feed(path.read_text())
  pages[path.name] = page

expected = set()
for name, page in pages.items():
  service = name in ('404.html', 'chi-siamo.html')
  canonical = BASE + '/' + ('' if name == 'index.html' else name)
  if not service:
    expected.add(canonical)
    if page.noindex or page.canonicals != [canonical] or page.h1 != 1:
      errors.append(f'{name}: controllare robots, canonical e H1')
  elif not page.noindex:
    errors.append(f'{name}: pagina di servizio senza noindex')
  for link in page.links:
    u = urlsplit(link)
    if u.scheme or u.netloc:
      continue
    target = (ROOT / unquote(u.path).lstrip('/')) if u.path.startswith('/') else page.path.parent / unquote(u.path)
    if not u.path:
      target = page.path
    if target.is_dir():
      target /= 'index.html'
    if not target.is_file():
      errors.append(f'{name}: destinazione mancante {link}')
    elif u.fragment and target.name in pages and unquote(u.fragment) not in pages[target.name].ids:
      errors.append(f'{name}: frammento mancante {link}')
    if u.path in ('index.html', '/index.html'):
      errors.append(f'{name}: link homepage da uniformare {link}')

actual = [e.text for e in ET.parse(ROOT / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
if set(actual) != expected or len(actual) != len(expected):
  errors.append('Sitemap diversa dall’insieme delle pagine canoniche')
robots = (ROOT / 'robots.txt').read_text()
if 'Disallow: /' in robots or f'Sitemap: {BASE}/sitemap.xml' not in robots:
  errors.append('Controllare robots.txt')
for error in errors:
  print('ERRORE:', error)
print(f'{len(pages)} pagine, {len(actual)} URL sitemap, {len(errors)} errori')
sys.exit(bool(errors))
