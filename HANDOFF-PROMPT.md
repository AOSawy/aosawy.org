# aosawy.org — Complete Project Context for Claude Code Terminal

Paste everything below this line into your Claude Code terminal session:

---

## CONTEXT: aosawy.org Website Project — Current State as of 2026-03-29

You are continuing work on my professional academic website at `C:\Users\aosaw\Claude\AOSAWY.ORG Website Project`. This project has been built across multiple Claude Cowork sessions. Here is the complete state of what exists, how it was built, and what remains.

### WHO I AM
Abdelrahman O. Sawy. PhD student in Industrial & Systems Engineering at Rutgers University. BSc in Mechanical Engineering from AUC (Cairo, 2024). Research focus: stochastic optimization, ML, and AI-driven decision systems for offshore wind energy (POSYDON framework, RIA Lab under Dr. Ezzat). Also a TA (ISE 338 + ISE 540), Kaggle competitor (top 0.6%), and founder of The Agentic Lab.

### DESIGN SYSTEM: Apple Liquid Glass
Every page uses the same design tokens — do NOT deviate:
- **Background:** `#f5f5f7`
- **Text:** `#1d1d1f`, Secondary: `#6e6e73`, Tertiary: `#86868b`
- **Accent:** `#0071e3` (Apple blue)
- **Glass card:** `rgba(255,255,255,0.65)`, `saturate(180%) blur(20px)`, `0.5px solid rgba(0,0,0,0.06)`, `border-radius: 16px`
- **Glass nav:** `rgba(255,255,255,0.72)`, same backdrop
- **Glass surface:** `rgba(255,255,255,0.45)`, `saturate(120%) blur(12px)`
- **Fonts:** Playfair Display (headings), Inter (body), Cambria Math (equations)
- **Animations:** fadeInUp, slideInLeft, heroFloat, pulseGlow, scaleIn via CSS keyframes
- **Components:** GlassCard, SectionTitle, Pill, StatChip, LinkButton — all defined in each JSX file

### WHAT HAS BEEN BUILT (all in `public/` directory)

**4 main pages (COMPLETED):**

1. **`index.html`** (Homepage) — 60.8 KB. Source: `public/home.jsx`. 9 sections: Hero (dark bg with wireframe image, stat chips, CTAs), About/Journey (3-image triptych: auc.jpg → CoreBuilding.jpeg → Weeks Hall + graduation photo), Resume/CV (view + download card), Research (POSYDON + RIA Lab cards), Portfolio (filterable grid of all 10 showcases + "View Full Portfolio Story" CTA → portfolio.html), Teaching (ISE 338 + ISE 540 cards), Publications (placeholder "Coming Soon"), Awards (placeholder "Coming Soon"), Contact (Email/LinkedIn/GitHub cards). Fixed glass nav bar with `ProfilePicCircle.jpg` avatar + "A. Sawy" branding.

2. **`portfolio.html`** (Portfolio) — 47.9 KB. Source: `public/portfolio.jsx`. Storytelling format with 3 chronological chapters: Chapter I "The Foundation" (AUC, 6 mechanical engineering showcases + AM companion), Chapter II "The Transition" (Rutgers ISE, 3 showcases with awards), Chapter III "The Frontier" (PhD research, POSYDON). Vertical timeline spine per chapter. Narrative transition bridges between chapters (italic Playfair quotes). Resume/CV card under hero. Epilogue with CTAs. Nav links to Home + all chapters + Resume.

3. **`research-showcase.html`** — 11.1 MB self-contained. 7 immersive tabs covering POSYDON framework, RIA Lab, HOST→STOCHOS→POSYDON evolution, deep dive, contributions, research pipeline, publications. Built via Vite pipeline (different from homepage/portfolio). Has floating "← Home" + "Portfolio" glass buttons injected into HTML.

4. **`teaching-showcase.html`** — ~100 KB. 7 tabs: Overview, ISE 338, ISE 540, Lecture Slides, Mathematical Foundations, Advanced Topics, Impact & Growth. Built via Babel UMD pipeline. Has floating "← Home" + "Portfolio" glass buttons.

**10 individual showcase pages (all COMPLETED, self-contained HTML):**
- AUC (6): `thesis-showcase.html`, `design-ii-showcase.html`, `fem-showcase.html`, `naca0024-cfd-showcase.html`, `failure-analysis-showcase.html`, `system-dynamics-showcase.html`
- Rutgers ISE (3): `ise507-showcase.html` (Most Innovative), `ise530-showcase.html` (1st Place), `ise694-showcase.html` (Most Innovative)
- AM (1): `am-showcase.html`

### BUILD PIPELINES (TWO DIFFERENT ONES)

**Pipeline A — Babel UMD (used for homepage, portfolio, teaching):**
JSX file → Babel transpile (`@babel/preset-react` + `@babel/plugin-transform-modules-umd`) → UMD JS → Python build script wraps in HTML template with React 18 CDN from unpkg. Critical: must add `window.react = window.React;` alias because UMD looks for lowercase `global.react` but React CDN sets `window.React`.

**Pipeline B — Vite (used for 10 AUC/ISE showcases + research):**
JSX → copy to Vite project `src/App.jsx` → `npx vite build` → Python script (`rebuild_all.py`) inlines JS/CSS + base64-encodes all images/PDFs into single self-contained HTML. Uses React 19. Script at: `showcase-build/rebuild_all.py`.

### ASSETS (in `public/assets/Home/`)
- `An_abstract,_futuristic_202603292141.png` — hero background (wireframe network)
- `ProfilePicCircle.jpg` — nav bar profile pic (32px circle)
- `auc.jpg` — AUC campus photo (journey triptych)
- `CoreBuilding.jpeg` — Rutgers CoRE building (journey triptych)
- `Rutgers-Weeks-Hall_30-sm.webp` — Richard Weeks Hall lab (journey triptych)
- `grad.jpeg` — AUC graduation ceremony photo
- `Abdelrahman_O_Sawy_Resume.pdf` — resume/CV (linked in homepage + portfolio)
- Also a top-level `RESUME.pdf` copy for easy updates

### NAVIGATION AUDIT (verified 2026-03-29)
- Homepage → all 10 showcases, portfolio.html, research, teaching
- Portfolio → index.html, all 10 showcases, research, teaching
- Research → floating nav to index.html + portfolio.html
- Teaching → floating nav to index.html + portfolio.html

### WHAT REMAINS / KNOWN ISSUES
1. **Homepage needs tweaking** — user said "it needs some tweaks but this is for now"
2. **Teaching showcase needs tweaks** — same note from user
3. **Publications & Awards sections** — currently placeholders ("Coming Soon") on homepage
4. **Contact page** — deferred ~1 month post-launch; homepage has Get in Touch section for now
5. **News / Archive** — left out for now
6. **Original design spec** envisioned Astro + Tailwind + Cloudflare Pages, but implementation used React 18 UMD + self-contained HTML instead. The original spec is at `docs/specs/2026-03-27-aosawy-org-design.md` — treat it as design intent reference, not technical truth
7. **Deployment** — domain is aosawy.org on Cloudflare. Planned: GitHub repo → Cloudflare Pages auto-deploy. Not yet set up.
8. **CV integration** — resume PDF is linked but not embedded/rendered as HTML

### KEY TECHNICAL NOTES
- All charts in showcases: pure inline SVG (Recharts fails on `file://` protocol)
- Unicode math in JSX: avoid `\u{1D7D9}` and similar multi-byte code points — use JSX string expressions `{'\u03A3'}` instead
- React 18 UMD (React 19 removed UMD support) for homepage/portfolio/teaching
- React 19 via Vite for the 10 showcase pages + research
- `<script type="module">` required on Vite-built HTML (without it → React error #299)
- Babel UMD wrapper exports module name based on filename (e.g., `home.jsx` → `window.home`, `portfolio.jsx` → `window.portfolio`)

You now have the full picture. Ask me what you'd like to do — tweaks, deployment setup, or anything else.
