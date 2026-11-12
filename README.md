# Darwin Agent Research Website

This project is a responsive static research-team website for Darwin Agent.

- `DA.pptx` — the Darwin Agent keynote deck
- `mimem.pdf` — the Mi-Memory technical report and related memory notes

The page positions the team around continuously learning, self-evolving agents
across digital and physical worlds and links to the public Darwin-Agent GitHub
organization. It keeps the original editorial layout, with new-project shortcuts,
research directions, and project-specific resource links.

Live site: <https://shaokun91.github.io/darwin-agent-website/>

## Files

- `index.html` — research homepage
- `styles.css` — visual design and layout
- `script.js` — responsive navigation and interactive evolution visualization
- `assets/darwin-agent-qr-da.svg` — self-contained DA-branded homepage QR for the footer
- `assets/darwin-agent-qr-da.png` — 1176 × 1176 downloadable QR
- `assets/darwin-mark-da-orange.png` — 1024 × 1024 transparent DA monogram
- `assets/darwin-mark-da-white.png` — matching white transparent DA monogram
- `scripts/build_qr.py` — deterministic QR asset generator (development only)

## Featured research

- [HarnessPAI](https://darwin-agent.github.io/HarnessPAI/) — an evolving executable harness for Physical AI; [paper](https://arxiv.org/abs/2609.29166) · [code](https://github.com/Darwin-Agent/HarnessPAI)
- [WIA](https://darwin-agent.github.io/WIA/) — world modeling and action learning across seven digital environments; [code](https://github.com/Darwin-Agent/WIA) · [demos](https://darwin-agent.github.io/WIA/demos.html)
- [HarnessX](https://github.com/Darwin-Agent/HarnessX) — composable and evolvable agent harnesses
- [Mi-Memory](https://github.com/Darwin-Agent/Mi-Memory) — composable, evolvable multi-source memory
- [CAR-bench TRACE](https://github.com/Darwin-Agent/Car-bench-TRACE) — trajectory-driven skill-bank evolution
- [Topological Collapse](https://github.com/Darwin-Agent/topological-collapse-agent-societies) — higher-order structure in agent societies
- [Digital Agents Meet World Models](https://github.com/Darwin-Agent/awesome-world-models-for-digital-agents) — survey and research collection

## How to view

Open `index.html` directly in a browser, or run a local server:

```bash
cd darwin-agent-website
python3 -m http.server 8000
```

Then visit:

```text
http://localhost:8000
```

## Content themes

- Harness as a first-class, evolvable behavior object
- Memory as a lifecycle framework with provenance and governance
- World modeling and action learning across digital environments
- Physical AI through programs that stay fixed within a rollout and evolve between rollouts
- Multi-agent systems as a topology problem

## Checks and publishing

Run the dependency-free content and link-structure checks:

```bash
python3 -m unittest discover -s tests -v
```

Before publishing, also check desktop and mobile layouts, keyboard navigation,
reduced-motion behavior, and new external resource links in a browser. The static
checks do not make network requests or replace browser QA.

GitHub Pages publishes the repository root from `main`; no build step or client
dependencies are required. Push reviewed changes to `main`, wait for the Pages
deployment, and verify the live site.

## Content sources

HarnessPAI and WIA descriptions are grounded in their official project pages,
checked on 2026-11-12. The homepage summarizes their mechanisms and scope rather
than reproducing benchmark rankings or implying that every advertised artifact
is bundled with the public code. Project resources should link to verified public
destinations.

### Publication dates

Dates were checked on 2026-11-12. **First preprint** means the initial arXiv
submission (v1), not a later revision, conference acceptance, or repository
creation date. **Report published** follows an explicit dated announcement from
the project. Keep the source's date precision: do not invent a day when only a
month is documented. Each displayed date uses a semantic `time` element; its
parent's `data-date-source` records the evidence URL without nesting links inside
clickable project cards.

| Project | First preprint / report date | Primary evidence |
| --- | --- | --- |
| HarnessX | 2026-06-12 | [arXiv v1](https://arxiv.org/abs/2606.14249v1) |
| HarnessPAI | 2026-09-24 | [arXiv v1](https://arxiv.org/abs/2609.29166v1) |
| Mi-Memory | 2026-07-21 | [arXiv v1](https://arxiv.org/abs/2607.18975v1) |
| CAR-bench TRACE | 2026-08-24 | [arXiv v1](https://arxiv.org/abs/2608.22793v1) |
| Topological Collapse | 2026-08-16 | [arXiv v1](https://arxiv.org/abs/2608.15519v1) |
| Digital Agents Meet World Models | 2026-05 | [Official report announcement](https://github.com/Darwin-Agent/awesome-world-models-for-digital-agents#-news--updates); distinct from the April repository launch |
| WIA | Not displayed; no verified first-publication date | Official project page and repository do not currently state one |

The hero's `evolve.` highlight uses Xiaomi orange (`#ff6900`), matching the
HarnessPAI project page. Other existing color accents are retained.

### Homepage QR code

The page ends with a scan-and-share section linking directly to
`https://shaokun91.github.io/darwin-agent-website/`. There is no redirect service,
tracking URL, third-party image dependency, or runtime QR library. The center
uses an image-generated, interlocking DA monogram, normalized to exact Xiaomi
orange (`#ff6900`) on white. The same transparent mark appears in the header,
footer, and favicon. The previous D-only assets remain available at their old
paths; no existing downloadable asset was deleted.

The QR uses version 6, H error correction, a four-module white quiet zone, and a
small central logo plate clear of finder, timing, and alignment patterns. The
SVG embeds its logo and is independently portable; the PNG download is 1176 px.

To rebuild, install `qrcode==8.2` and `Pillow` in a development virtual environment
and run `python scripts/build_qr.py`. To run image-decoding tests as well, install
`zxing-cpp==2.3.0` and run `python -m unittest discover -s tests -v`. The tests check
the decoded URL at several sizes, after rotation, JPEG compression, and grayscale
conversion. Recheck the decoded URL and layout whenever the destination or logo
changes. The generator intentionally rejects a different QR version so logo
placement cannot silently cover a function pattern.

### DA identity

The monogram combines D (Darwin) and A (Agent) into one compact silhouette. The
rounded D provides a stable, enclosing structure; the angular A emerges from it,
with a shared connection and clear negative-space channels keeping both letters
legible. This visual direction evokes accumulated experience becoming action,
consistent with the team's emphasis on memory, feedback, and self-evolving agent
systems. These are design intentions, not technical claims about the symbol.

Use the orange transparent PNG on light or dark neutral backgrounds and the
white variant where a reversed mark is needed. Preserve the clear space baked
into the asset, do not stretch it, and do not add the old square border. Use the
monogram alone at small sizes; pair it with the existing Darwin Agent wordmark
for larger website and presentation applications. A 40 px mark is used in the
website navigation; the QR logo remains within its tested central safe area.
