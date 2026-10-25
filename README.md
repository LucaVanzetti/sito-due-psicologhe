# Allieri & Pagliari — Psicologhe

Sito statico dello studio di Valentina Allieri e Silvia Pagliari. Il progetto non usa dipendenze né build tool. I font (woff2, solo alfabeto latino) sono ospitati localmente in `assets/fonts/`, così le pagine non caricano Google Fonts dal browser del visitatore.

## Pagine

- `index.html` — homepage
- `lo-studio.html` — studio e modalità degli incontri
- `come-lavoriamo.html` — approccio e servizi
- `aree-intervento.html` — aree di intervento
- `chi-siamo.html` — presentazione delle professioniste
- `valentina-allieri.html` e `silvia-pagliari.html` — profili individuali
- `contatti.html` — contatti (WhatsApp per entrambe) e informazioni pratiche
- `faq.html` — domande frequenti (solo informazioni già presenti nel sito)
- `404.html` — pagina non trovata (percorsi dalla radice, resta `noindex`)
- `privacy.html` — informativa per sito e primo contatto condiviso; prima del lancio le professioniste devono sottoscrivere e applicare l’accordo operativo sulla casella comune
- `robots.txt` — istruzioni per i crawler della sola anteprima

Le sei aree della homepage (Ansia e stress, Difficoltà relazionali, Autostima, Momenti di crisi, Problemi di coppia, Cambiamenti e transizioni) sono **solo elenco di temi**, senza pagina dedicata.

## Immagini

Il sito usa solo file WebP in più larghezze (`nome-480.webp`, `nome-800.webp`, …), richiamati con `srcset` e `sizes`. Gli originali PNG/JPEG si trovano in `private/originals/images/`, cartella locale ignorata da Git. Per sostituire un’immagine: partire dall’originale, ridimensionare ed esportare in WebP (qualità ~80), aggiornare `srcset`, `sizes`, `width` e `height` nelle pagine e controllare il risultato a 375 px e 1440 px.

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

Il contatto condiviso è la casella `contatti@allieriepagliari.it`, raggiungibile dalla pagina Contatti. È letta da entrambe le professioniste soltanto per il primo orientamento; dopo l'eventuale assegnazione, ciascuna gestisce autonomamente il proprio contatto. Il sito invita a non inviare dettagli clinici o sanitari via email.

Anche la posizione dello studio sarà inizialmente un semplice link a Google Maps, non una mappa incorporata. In questo modo il sito non carica Google Maps automaticamente.

L’informativa descrive il contatto condiviso, i fornitori tecnici e il termine di conservazione. Prima della pubblicazione definitiva, le professioniste devono sottoscrivere e applicare l’accordo operativo conservato in `private/`, configurare gli accessi alla casella e verificare le condizioni del piano OVH.

## Controlli disponibili

```sh
node --check script.js
```

Non è presente una suite automatica. Prima di ogni pubblicazione eseguire i controlli manuali indicati sopra e verificare che tutti i dati professionali, il form e i testi legali siano confermati.

## Stato di pubblicazione

Il sito è pronto per una **anteprima noindex**, ma non per la pubblicazione definitiva finché non saranno completati i punti della checklist locale del progetto, in particolare:

- sottoscrizione e applicazione dell’accordo operativo per il contatto condiviso;
- verifica accessi, 2FA, inoltri e cancellazione periodica della casella OVH;
- fotografie autorizzate e immagini con licenza d’uso adeguata;
- dominio pubblico definitivo e configurazione DNS;
- Google Business Profile e configurazione SEO tecnica;
- rimozione di `noindex` e aggiornamento di `robots.txt` al passaggio alla versione definitiva.

La checklist e il questionario del cliente sono conservati solo nella cartella locale ignorata `private/`; non devono essere aggiunti al repository pubblico.

## Lavorare da più dispositivi

GitHub (`origin/main`) è la fonte unica. All'inizio di ogni sessione: `git fetch origin && git pull --ff-only origin main`; a fine lavoro: commit e `git push origin main`. La cartella `private/` non è sincronizzata (è ignorata da Git).

## Lancio sul dominio definitivo

Quando dominio e privacy sono pronti: `python3 tools/prepara-lancio.py https://www.dominio.it --cname` (aggiunge canonical, Open Graph, dati strutturati, `sitemap.xml`, `robots.txt` e rimuove `noindex`). Poi inviare la sitemap a Search Console e creare il Google Business Profile.

## SEO e ricerche AI

Il sito contiene testo HTML indicizzabile, pagine tematiche e meta description. Per aumentare la trovabilità locale dopo la pubblicazione definitiva servono dominio, sitemap, Search Console, Google Business Profile e dati strutturati coerenti con i contenuti visibili.

Non esiste un markup speciale che garantisca apparizioni nelle risposte AI: la priorità è pubblicare contenuti originali, accurati, locali e utili, con struttura tecnica chiara e pagine accessibili.

## Repository

Il branch principale è `main` e il remote configurato è `origin`:

```text
https://github.com/LucaVanzetti/sito-due-psicologhe.git
```
