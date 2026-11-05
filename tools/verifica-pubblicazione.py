#!/usr/bin/env python3
"""Attende che le pagine della sitemap corrispondano alla copia pubblicata."""
import os
import time
import urllib.error
import urllib.parse
import urllib.request

import indexnow


def published():
    pages = [(url, indexnow.ROOT / (urllib.parse.urlsplit(url).path.lstrip('/') or 'index.html'))
             for url in indexnow.urls([])]
    key_file = indexnow.key() + '.txt'
    files = [(f'{indexnow.BASE}/sitemap.xml', indexnow.ROOT / 'sitemap.xml'),
             (f'{indexnow.BASE}/{key_file}', indexnow.ROOT / key_file), *pages]
    for url, path in files:
        query = urllib.parse.urlencode({'v': os.environ.get('GITHUB_SHA', 'local')})
        try:
            with urllib.request.urlopen(f'{url}?{query}', timeout=5) as response:
                if response.read() != path.read_bytes():
                    print(f'In attesa: {url}', flush=True)
                    return False
        except (OSError, urllib.error.URLError) as error:
            print(f'In attesa: {url} ({error})', flush=True)
            return False
    return True


if __name__ == '__main__':
    for attempt in range(30):
        if published():
            print('Pagine, sitemap e chiave pubblicate correttamente')
            break
        if attempt < 29:
            time.sleep(10)
    else:
        raise SystemExit('Pubblicazione non ancora aggiornata: IndexNow non inviato')
