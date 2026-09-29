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
- `robots.txt` — istruzioni per i crawler della sola anteprima

## Avvio locale

```sh
python3 -m http.server 8000
```

Aprire `http://localhost:8000` e verificare almeno:

- homepage e pagine interne a desktop;
- viewport stretto, circa 375 px;
- apertura/chiusura del menu tramite mouse, tastiera ed `Esc`;
- visibilità del focus da tastiera;
- collegamenti, CTA WhatsApp, telefoniche ed email.

## Anteprima per la revisione

L’anteprima sarà pubblicata con GitHub Pages e condivisa alle professioniste come semplice link: non devono usare GitHub né Git per visualizzarla.

L’attuale configurazione è **solo per la revisione**:

- tutte le pagine hanno il meta tag `noindex, nofollow, noarchive`;
- `robots.txt` chiede ai crawler di non analizzare il sito;
- questi accorgimenti riducono l’indicizzazione, ma **non rendono il link privato**: chi ne entra in possesso può comunque aprirlo;
- prima della pubblicazione sul dominio definitivo vanno rimossi il meta tag `noindex` da tutte le pagine e il blocco in `robots.txt`.

### Pubblicare l’anteprima su GitHub Pages

1. In GitHub, aprire il repository e andare in **Settings → Pages**.
2. In **Build and deployment**, scegliere **Deploy from a branch**.
3. Selezionare il branch `main` e la cartella `/(root)`, quindi salvare.
4. Attendere la pubblicazione e copiare l’URL generato da GitHub Pages.
5. Condividere l’URL solo con Valentina e Silvia per raccogliere commenti via WhatsApp o email.

Per aggiornare l’anteprima, modificare i file, eseguire i controlli sotto indicati e inviare le modifiche al branch pubblicato. GitHub Pages aggiorna il link automaticamente dopo la pubblicazione.

## Contatto condiviso e servizi esterni

Il contatto condiviso previsto è un **Google Form** con notifiche a entrambe le professioniste. L’URL del modulo non è ancora disponibile, quindi non è stato inserito nel sito. Il modulo sarà aperto tramite link, non incorporato nella pagina.

Anche la posizione dello studio sarà inizialmente un semplice link a Google Maps, non una mappa incorporata. In questo modo il sito non carica Google Maps automaticamente.

L’uso di Google Form e la relativa gestione dei dati devono essere riportati e validati nell’informativa privacy prima della pubblicazione definitiva.

## Controlli disponibili

```sh
node --check script.js
```

Non è presente una suite automatica. Prima di ogni pubblicazione eseguire i controlli manuali indicati sopra e verificare che tutti i dati professionali, il form e i testi legali siano confermati.

## Stato di pubblicazione

Il sito è pronto per una **anteprima noindex**, ma non per la pubblicazione definitiva finché non saranno completati i punti presenti in [`DOMANDE_E_DUBBI.md`](DOMANDE_E_DUBBI.md), in particolare:

- URL e configurazione del Google Form, comprese le informazioni privacy;
- recapito privacy, hosting, conservazione e validazione dell’informativa;
- fotografie autorizzate e immagini con licenza d’uso adeguata;
- dominio pubblico definitivo e configurazione DNS;
- Google Business Profile e configurazione SEO tecnica;
- rimozione di `noindex` e aggiornamento di `robots.txt` al passaggio alla versione definitiva.

## SEO e ricerche AI

Il sito contiene testo HTML indicizzabile, pagine tematiche e meta description. Per aumentare la trovabilità locale dopo la pubblicazione definitiva servono dominio, sitemap, Search Console, Google Business Profile e dati strutturati coerenti con i contenuti visibili.

Non esiste un markup speciale che garantisca apparizioni nelle risposte AI: la priorità è pubblicare contenuti originali, accurati, locali e utili, con struttura tecnica chiara e pagine accessibili.

## Repository

Il branch principale è `main` e il remote configurato è `origin`:

```text
https://github.com/LucaVanzetti/sito-due-psicologhe.git
```
