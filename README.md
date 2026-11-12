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
