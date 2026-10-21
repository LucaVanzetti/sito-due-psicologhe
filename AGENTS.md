# Repository Guidelines

## Start of every session (read first)

The project is worked on from several devices, and GitHub (`origin`, branch `main`) is the single source of truth. **Before doing anything else, check that the local copy is aligned:**

```sh
git fetch origin && git status -sb && git pull --ff-only origin main
```

- If the pull is not a clean fast-forward (diverged history, local uncommitted changes that conflict), stop and tell the user before touching any file.
- Finish every task with a focused commit and `git push origin main`; never leave work only on one device.
- `private/` is git-ignored, so it is **not** synchronised between devices (client checklist, briefing, original images and fonts live there). If a file in `private/` is needed and missing, ask the user instead of recreating it.

## Project Structure & Module Organization

This is a lightweight static website for **Allieri & Pagliari — Psicologhe**. Keep the site dependency-free unless a new requirement clearly justifies a build tool.

- `index.html` contains the page structure and Italian content.
- `styles.css` contains the complete responsive visual system: CSS variables, layout, typography, illustrations, and media queries.
- `script.js` contains small progressive-enhancement interactions: the accessible mobile navigation toggle and the fixed mobile WhatsApp bar ("Scrivi a Valentina" / "Scrivi a Silvia"), injected on every page and hidden from 768 px up.
- Pages: `index.html`, `lo-studio.html`, `come-lavoriamo.html`, `aree-intervento.html`, `chi-siamo.html`, `valentina-allieri.html`, `silvia-pagliari.html`, `contatti.html`, `faq.html`, `privacy.html`, plus `404.html` (served at any address, so it uses root-relative paths and stays `noindex` even after launch). Every page has a skip link ("Vai al contenuto") targeting `<main>`.
- `tools/prepara-lancio.py <https://dominio>` is the one-shot launch script (stdlib only, re-runnable): removes `noindex`, adds canonical/Open Graph image/JSON-LD, writes `sitemap.xml` and `robots.txt`, optionally `CNAME`. It refuses to run while `privacy.html` still has placeholders. Do not hand-edit canonical/sitemap before the domain is confirmed.
- `faq.html` contains only facts already published elsewhere on the site (plus the professional-secrecy statement, to be validated by the client). Tariffe confermate: colloquio individuale 60 €, di coppia 70 €, familiare 80 €. Do not add other unconfirmed data to it.
- The six topics listed on the homepage ("Ansia e stress", "Difficoltà relazionali", "Autostima", "Momenti di crisi", "Problemi di coppia", "Cambiamenti e transizioni") are deliberately **static topics without a dedicated page**, per the client. Do not turn them back into links or add description pages unless asked.
- `privacy.html` is a draft privacy information page. It contains explicit placeholders and must not be treated as publish-ready until the indicated legal and operational data are confirmed.
- La checklist delle conferme del cliente e i materiali di briefing sono conservati localmente in `private/` e non devono essere aggiunti al repository pubblico.
- `README.md` documents the current project status, local preview, checks, and deployment prerequisites.

Place future static assets in an `assets/` directory, grouped by purpose (for example, `assets/images/` and `assets/icons/`). Use relative paths.

### Fonts and icons

- Fonts are local **woff2** subsets (Outfit, Nunito Sans; latin only) in `assets/fonts/`, preloaded in every `<head>`. Originals are in `private/originals/fonts/`. Do not add font files that are not referenced in `styles.css`.
- The logo is the "archi" mark (`assets/images/logo-archi-96.webp` / `-192.webp`, transparent background, 54×45 px in the header). Favicons are in `assets/icons/` and `favicon.ico`; `assets/images/og-allieri-pagliari.jpg` (1200×630) is the social preview and is referenced only by the launch script because Open Graph needs an absolute URL.

### Images

- The site serves **WebP only**, in several widths per image, named `<name>-<width>.webp` (for example `assets/images/portraits/silvia-pagliari-800.webp`). Original PNG/JPEG files are kept locally in `private/originals/images/` (git-ignored) and must not be re-added to `assets/`.
- Every `<img>` needs `width`/`height` (intrinsic size of the largest variant), `srcset` + `sizes`, and `alt` (empty only for purely decorative art). Use `loading="lazy" decoding="async"` for everything below the first screen; the homepage hero uses `fetchpriority="high"`.
- To add or replace an image: put the original in `private/originals/images/`, resize with Pillow (`Image.resize(..., LANCZOS)`, `save(..., 'WEBP', quality=80, method=6)`) to the widths needed (typically 480/800, plus 1200 for large hero-like art), then reference it as above. Illustrations are shown at roughly 2× their CSS size; check the result at 375 px and 1440 px.
- `uomo-con-binocolo-*` (Aree di intervento, "Momenti di cambiamento") is a retouched version of the original "ragazza con binocolo" illustration (short hair, shirt and trousers); the edited full-size file is `private/originals/images/illustrations/uomo-con-binocolo-collage.png`. `teste-sovrapposte-*` is cropped to the artwork (no empty top margin) and is shown with its own aspect ratio on Come lavoriamo.
- Illustrations that contain text (e.g. "Ogni storia merita uno sguardo attento") must keep a descriptive `alt`.

## Build, Test, and Development Commands

There is no package manager, build system, or automated test suite at present. Preview locally with a static HTTP server, for example:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`. Check the homepage at desktop and mobile widths, test every navigation link, and verify the menu opens and closes on small screens.

## Coding Style & Naming Conventions

Use two-space indentation in HTML, CSS, and JavaScript. Prefer semantic HTML (`header`, `main`, `section`, `nav`, `article`) and preserve accessible labels, landmarks, and meaningful heading order.

Use lowercase kebab-case for CSS classes, filenames, and asset names: `.contact-card`, `portrait-valentina.svg`. Keep design tokens in `:root` and reuse existing palette variables rather than introducing raw color values. Keep JavaScript small, dependency-free, and scoped to a clear UI behavior.

All visitor-facing copy is Italian and professional. The current copy mixes `Lei` (e.g. hero CTA) with `tu` and impersonal forms (e.g. "raccontaci la tua storia", "ti ha portato"); the client asked to keep it as it is, so do not harmonise the register unless requested, and keep new copy consistent with the section it lands in. Avoid unsupported clinical claims and verify professional credentials, prices, hours, contact details, and legal/privacy text with the client before publishing. Do not invent placeholder contact data, domains, legal bases, or retention periods.

## Current Site State

- Review preview only: every page carries `noindex, nofollow, noarchive` and `robots.txt` blocks crawlers. Remove both before the public launch.
- Contact policy: both psychologists are contacted by **WhatsApp** as the main channel (Valentina `393669539230`, Silvia `393466519968`; the latter is also her phone number and is shown as a secondary `tel:` link on the contact page). Valentina also has a MioDottore link. The client confirmed that Silvia's number is correct and active on WhatsApp.
- Tariffe confermate: colloquio individuale 60 €, di coppia 70 €, familiare 80 €.
- Homepage hero: the tree illustration is full-bleed; the dark overlay is a gradient only behind the text (from the bottom on mobile, from the left on desktop), not over the whole image.
- Mobile layout: profile cards on the homepage stack in one column; topic chips use a two-column grid; the fixed WhatsApp bar needs `padding-bottom` on `body` (already set below 768 px).
- Focus ring is `--ink` (and `--soft` on dark areas) to keep a 3:1 contrast; `--accent` is currently unused.
- `privacy.html` is still a draft with placeholders; the studio entrance photo (one of the psychologists) is authorised by the client.

## Testing Guidelines

Manual testing is required for each change. Test Chrome/Firefox and a narrow viewport (around 375 px). Confirm keyboard focus remains visible, buttons work by keyboard, text has adequate contrast, and no horizontal scrolling is introduced.

## Commit & Pull Request Guidelines

The repository has no established commit history or convention. Use concise imperative commits, such as `Add contact section` or `Improve mobile navigation`. Keep each commit focused. Pull requests should describe the user-facing change, identify any placeholder content, and include desktop and mobile screenshots for visual changes.
