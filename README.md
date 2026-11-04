# Allieri & Pagliari — Psicologhe

Sito statico dello studio di Valentina Allieri e Silvia Pagliari. Il progetto non usa dipendenze né build tool. I font (woff2, solo alfabeto latino) sono ospitati localmente in `assets/fonts/`, così le pagine non caricano Google Fonts dal browser del visitatore.

## Pagine

- `index.html` — homepage
- `lo-studio.html` — studio e modalità degli incontri
- `come-lavoriamo.html` — approccio e servizi
- `aree-intervento.html` — aree di intervento
- `chi-siamo.html` — redirect storico verso Lo studio
- `valentina-allieri.html` e `silvia-pagliari.html` — profili individuali
- `contatti.html` — contatti (WhatsApp per entrambe) e informazioni pratiche
- `faq.html` — domande frequenti (solo informazioni già presenti nel sito)
- `404.html` — pagina non trovata (percorsi dalla radice, resta `noindex`)
- `privacy.html` — informativa per sito e primo contatto condiviso; prima del lancio le professioniste devono sottoscrivere e applicare l’accordo operativo sulla casella comune
- `robots.txt` — scansione consentita e riferimento alla sitemap

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

## Pubblicazione attuale

Il sito pubblico è https://www.allieriepagliari.it/, su GitHub Pages da `main` nella cartella principale; DNS gestiti da OVH e HTTPS forzato. Le nove pagine della sitemap sono scansionabili. `404.html` e il redirect storico `chi-siamo.html` restano esclusi dall’indicizzazione.

I collegamenti alla homepage usano `/`; la canonical della homepage è il dominio con slash finale. GitHub Pages serve ancora `/index.html` con 200. Il redirect storico verso `lo-studio.html` usa un meta refresh immediato.

Per questa fase le modifiche restano locali: nessun push o cambio di hosting senza richiesta. Il sito pubblico non cambia con il solo salvataggio dei file.

## Contatto condiviso e servizi esterni

Il contatto condiviso è la casella `contatti@allieriepagliari.it`, raggiungibile dalla pagina Contatti. È letta da entrambe le professioniste soltanto per il primo orientamento; dopo l'eventuale assegnazione, ciascuna gestisce autonomamente il proprio contatto. Il sito invita a non inviare dettagli clinici o sanitari via email.

Anche la posizione dello studio sarà inizialmente un semplice link a Google Maps, non una mappa incorporata. In questo modo il sito non carica Google Maps automaticamente.

L’informativa descrive il contatto condiviso, i fornitori tecnici e il termine di conservazione. Prima della pubblicazione definitiva, le professioniste devono sottoscrivere e applicare l’accordo operativo conservato in `private/`, configurare gli accessi alla casella e verificare le condizioni del piano OVH.

## Controlli disponibili

```sh
node --check script.js
```

Non è presente una suite automatica. Prima di ogni pubblicazione eseguire i controlli manuali indicati sopra e verificare che tutti i dati professionali, il form e i testi legali siano confermati.

## Verifiche tecniche

Eseguire `python3 tools/verifica-sito.py` e `node --check script.js`, poi la verifica manuale desktop/mobile indicata sopra. Il controllo locale verifica collegamenti, frammenti, risorse responsive, canonical, sitemap (incluso `lastmod`) e validità dei dati strutturati JSON-LD senza rete e senza dipendenze aggiuntive. Dopo aver modificato una pagina, aggiornarne il `lastmod` in `sitemap.xml`: il controllo segnala le date più vecchie dell’ultimo commit della pagina.

La documentazione tecnica non attesta gli adempimenti operativi o legali delle professioniste. I materiali locali in `private/` non sono sincronizzati né pubblicabili.

Il generatore `tools/prepara-lancio.py` è uno strumento di manutenzione, non va eseguito per il normale aggiornamento dei contenuti: può riscrivere metadati e file di scansione. Il dominio definitivo è già configurato.

## Lavorare da più dispositivi

GitHub (`origin/main`) è la fonte unica per la versione pubblicata. Prima di modificare, verificare lo stato e sincronizzare quando consentito. Una richiesta esplicita di lavoro locale sospende commit e push fino a successiva autorizzazione.

## Approvazioni

La manutenzione tecnica locale può procedere mantenendo contenuti e aspetto attuali. Le modifiche a testi visibili, immagini, tipografia e disposizione richiedono l’approvazione di entrambe le psicologhe. La pubblicazione rimane sospesa durante la fase locale.

## Misure ancora da raccogliere

- Lighthouse mobile ripetuto e Core Web Vitals, se disponibili.
- Controllo manuale Chrome/Firefox a 375 px e desktop.
- Storico disponibilità da più reti e dettagli delle esclusioni Google/Bing.
- Catene complete di redirect, DNS autorevoli e scadenza del certificato.
- Valutazione delle condizioni d’uso dell’hosting per il sito professionale.

Non ci sono prove che l’hosting causi la mancata indicizzazione delle pagine interne. Nessuna migrazione è necessaria per applicare i miglioramenti locali.

## Repository

Il branch principale è `main` e il remote configurato è `origin`:

```text
https://github.com/LucaVanzetti/sito-due-psicologhe.git
```
