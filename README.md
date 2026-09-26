# Allieri & Pagliari — Psicologhe

Sito statico dello studio di Valentina Allieri e Silvia Pagliari. Il progetto non usa dipendenze né build tool.

## Pagine

- `index.html` — homepage
- `lo-studio.html` — studio e modalità degli incontri
- `come-lavoriamo.html` — approccio e servizi
- `aree-intervento.html` — aree di intervento
- `chi-siamo.html` — presentazione delle professioniste
- `valentina-allieri.html` e `silvia-pagliari.html` — profili individuali
- `contatti.html` — contatti e informazioni pratiche
- `privacy.html` — **bozza non pronta alla pubblicazione**: contiene informazioni e placeholder da validare

## Avvio locale

```sh
python3 -m http.server 8000
```

Aprire `http://localhost:8000` e verificare almeno:

- homepage e pagine interne a desktop;
- viewport stretto, circa 375 px;
- apertura/chiusura del menu tramite mouse, tastiera ed `Esc`;
- visibilità del focus da tastiera;
- collegamenti, CTA telefoniche e email.

## Controlli disponibili

```sh
node --check script.js
```

Non è presente una suite automatica. Prima di ogni pubblicazione eseguire i controlli manuali indicati sopra e verificare che tutti i dati professionali e legali siano confermati.

## Stato di pubblicazione

Il sito è una base funzionale, ma non è pronto alla pubblicazione finché non saranno completati i punti presenti in [`DOMANDE_E_DUBBI.md`](DOMANDE_E_DUBBI.md), in particolare:

- recapito privacy comune/dedicato, hosting, conservazione e validazione dell’informativa;
- email e orari definitivi;
- scelta del contatto condiviso allo studio;
- fotografie autorizzate;
- dominio pubblico, Google Business Profile e configurazione SEO tecnica.

## SEO e ricerche AI

Il sito contiene testo HTML indicizzabile, pagine tematiche e meta description. Per aumentare la trovabilità locale servono dominio pubblico, sitemap, Search Console, Google Business Profile e dati strutturati coerenti con i contenuti visibili.

Non esiste un markup speciale che garantisca apparizioni nelle risposte AI: la priorità è pubblicare contenuti originali, accurati, locali e utili, con struttura tecnica chiara e pagine accessibili.

## Repository

Il branch principale è `main` e il remote configurato è `origin`:

```text
https://github.com/LucaVanzetti/sito-due-psicologhe.git
```
