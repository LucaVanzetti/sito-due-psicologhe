# Repository Guidelines

## Project Structure & Module Organization

This is a lightweight static website for **Allieri & Pagliari — Psicologhe**. Keep the site dependency-free unless a new requirement clearly justifies a build tool.

- `index.html` contains the page structure and Italian content.
- `styles.css` contains the complete responsive visual system: CSS variables, layout, typography, illustrations, and media queries.
- `script.js` contains small progressive-enhancement interactions, currently the mobile navigation toggle.
- `Questionario operativo per il sito dello studio.docx` is the client brief. Treat its professional details and contact information as source material; do not edit it unless explicitly asked.

Place future static assets in an `assets/` directory, grouped by purpose (for example, `assets/images/` and `assets/icons/`). Use relative paths.

## Build, Test, and Development Commands

There is no package manager, build system, or automated test suite at present. Preview locally with a static HTTP server, for example:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`. Check the homepage at desktop and mobile widths, test every navigation link, and verify the menu opens and closes on small screens.

## Coding Style & Naming Conventions

Use two-space indentation in HTML, CSS, and JavaScript. Prefer semantic HTML (`header`, `main`, `section`, `nav`, `article`) and preserve accessible labels, landmarks, and meaningful heading order.

Use lowercase kebab-case for CSS classes, filenames, and asset names: `.contact-card`, `portrait-valentina.svg`. Keep design tokens in `:root` and reuse existing palette variables rather than introducing raw color values. Keep JavaScript small, dependency-free, and scoped to a clear UI behavior.

All visitor-facing copy is Italian and uses a professional, formal tone (`Lei`). Avoid unsupported clinical claims and verify professional credentials, prices, hours, and contact details with the client before publishing.

## Testing Guidelines

Manual testing is required for each change. Test Chrome/Firefox and a narrow viewport (around 375 px). Confirm keyboard focus remains visible, buttons work by keyboard, text has adequate contrast, and no horizontal scrolling is introduced.

## Commit & Pull Request Guidelines

The repository has no established commit history or convention. Use concise imperative commits, such as `Add contact section` or `Improve mobile navigation`. Keep each commit focused. Pull requests should describe the user-facing change, identify any placeholder content, and include desktop and mobile screenshots for visual changes.
