# CSS Page Isolation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scope all mobile CSS rules to their target pages via body classes, fixing homepage regression and preventing future cross-page bleeding.

**Architecture:** Add `page-xxx` class to each page's `<body>` tag. Restructure the mobile media query in `design-system.css` into labeled subsections: shared (universal), then one scoped block per page. Each block's rules are prefixed with the page's body class.

**Tech Stack:** CSS (design-system.css), HTML (14 pages), Python (injection script for Pipeline B)

**Spec:** `docs/superpowers/specs/2026-03-30-css-page-isolation-design.md`

---

### Task 1: Add body classes to Pipeline A pages

**Files:**
- Modify: `public/index.html` (line 22)
- Modify: `public/research-showcase.html` (line 38)
- Modify: `public/portfolio.html` (line 19)
- Modify: `public/teaching-showcase.html` (line 34)

- [ ] **Step 1: Add class to index.html**

Change line 22 from:
```html
<body>
```
to:
```html
<body class="page-home">
```

- [ ] **Step 2: Add class to research-showcase.html**

Change line 38 from:
```html
<body>
```
to:
```html
<body class="page-research">
```

- [ ] **Step 3: Add class to portfolio.html**

Change line 19 from:
```html
<body>
```
to:
```html
<body class="page-portfolio">
```

- [ ] **Step 4: Add class to teaching-showcase.html**

Change line 34 from:
```html
<body>
```
to:
```html
<body class="page-teaching">
```

- [ ] **Step 5: Commit**

```bash
git add public/index.html public/research-showcase.html public/portfolio.html public/teaching-showcase.html
git commit -m "feat: add page-scoped body classes to Pipeline A pages"
```

---

### Task 2: Add body classes to Pipeline B pages

**Files:**
- Modify: `public/thesis-showcase.html` (line 4196)
- Modify: `public/design-ii-showcase.html` (line 4124)
- Modify: `public/fem-showcase.html` (line 235)
- Modify: `public/naca0024-cfd-showcase.html` (line 136)
- Modify: `public/failure-analysis-showcase.html` (line 136)
- Modify: `public/system-dynamics-showcase.html` (line 163)
- Modify: `public/am-showcase.html` (line 68)
- Modify: `public/ise507-showcase.html` (line 164)
- Modify: `public/ise530-showcase.html` (line 162)
- Modify: `public/ise694-showcase.html` (line 171)

- [ ] **Step 1: Replace `<body>` with `<body class="page-showcase">` in all 10 files**

In each file, change:
```html
<body>
```
to:
```html
<body class="page-showcase">
```

Files (all in `public/`): `thesis-showcase.html`, `design-ii-showcase.html`, `fem-showcase.html`, `naca0024-cfd-showcase.html`, `failure-analysis-showcase.html`, `system-dynamics-showcase.html`, `am-showcase.html`, `ise507-showcase.html`, `ise530-showcase.html`, `ise694-showcase.html`

- [ ] **Step 2: Verify body classes are present**

```bash
grep -n "<body" public/*-showcase.html public/index.html public/portfolio.html public/teaching-showcase.html
```

Expected: Every file shows `<body class="page-xxx">`.

- [ ] **Step 3: Commit**

```bash
git add public/*-showcase.html
git commit -m "feat: add page-showcase body class to Pipeline B pages"
```

---

### Task 3: Restructure mobile CSS — shared rules

**Files:**
- Modify: `public/design-system.css` (lines 514-1158, plus lines 1225-1235)

This is the main task. Rewrite the `@media (max-width: 639px)` block with proper scoping. The complete replacement follows.

**IMPORTANT:** Sections 1-9 (lines 1-508) and Section 11 footer (lines 1160-1223) remain UNTOUCHED. Only the mobile media query block and the orphaned footer media query are replaced.

- [ ] **Step 1: Replace the entire mobile media query**

Delete everything from line 514 (`@media (max-width: 639px) {`) through line 1158 (closing `}`), AND the orphaned footer mobile query at lines 1225-1235.

Replace with the restructured CSS below. The new block has clearly labeled subsections:

```css
/* -----------------------------------------------------------------------------
   8b. MOBILE  (< 640px)
   Structure: SHARED > PAGE-HOME > PAGE-RESEARCH > PAGE-TEACHING > PAGE-SHOWCASE
   Each page section is scoped with body.page-xxx so rules ONLY affect that page.
----------------------------------------------------------------------------- */
@media (max-width: 639px) {

  /* =========================================================================
     10a. SHARED MOBILE — applies to ALL pages
     ========================================================================= */

  /* -- Variable overrides -- */
  :root {
    --fs-h1:            clamp(1.6rem, 6vw, 2.4rem);
    --fs-h2:            1.5rem;
    --section-padding:  48px 16px;
    --card-padding:     16px;
  }

  /* -- Layout grids (class-based) -- */
  .ds-grid-2,
  .ds-grid-3,
  .ds-grid-4 {
    grid-template-columns: 1fr !important;
  }
  .ds-stats-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }

  /* -- Hero flex stacking (class-based) -- */
  .ds-hero-flex {
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
  }
  .ds-hero-photo {
    width: 140px !important;
    height: 140px !important;
    margin: 0 auto 20px !important;
  }
  .ds-hero-buttons {
    flex-direction: column !important;
    width: 100% !important;
    gap: 10px !important;
  }
  .ds-hero-buttons > * {
    width: 100% !important;
    text-align: center !important;
  }
  .ds-hero-buttons a,
  .ds-hero-buttons button {
    padding: 10px 20px !important;
    font-size: 0.8rem !important;
  }

  /* -- Navigation: hamburger visible, links hidden -- */
  .ds-hamburger {
    display: flex !important;
  }
  .ds-nav-links {
    display: none !important;
  }

  /* -- Mobile navigation drawer -- */
  .ds-mobile-drawer {
    position: fixed;
    inset: 0;
    z-index: 999;
    background: rgba(245, 245, 247, 0.92);
    backdrop-filter: saturate(180%) blur(24px);
    -webkit-backdrop-filter: saturate(180%) blur(24px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 28px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.25s ease;
  }
  .ds-mobile-drawer.open {
    opacity: 1;
    pointer-events: all;
  }
  .ds-mobile-drawer a {
    font-family: var(--font-heading);
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--color-text);
    text-decoration: none;
    letter-spacing: 0.01em;
    transition: color 0.15s ease;
  }
  .ds-mobile-drawer a:hover {
    color: var(--color-accent);
  }

  /* -- Back-nav smaller on mobile -- */
  .site-back-nav a,
  .site-back-nav button {
    padding: 6px 12px;
    font-size: 0.75rem;
  }

  /* -- Overflow prevention -- */
  #root {
    overflow-x: clip;
  }
  main, section, article, .scroll-reveal {
    overflow-x: hidden;
  }
  body {
    overflow-x: hidden;
  }

  /* -- Media overflow (images, video, etc.) -- */
  img, video, canvas, svg {
    max-width: 100% !important;
    height: auto !important;
  }

  /* -- Text wrapping -- */
  h1, h2, h3, h4, h5, h6, p, span, a, li {
    word-wrap: break-word;
    overflow-wrap: break-word;
  }

  /* -- Scroll indicator: static flow on mobile -- */
  .ds-scroll-indicator {
    position: static !important;
    bottom: auto !important;
    left: auto !important;
    transform: none !important;
    width: fit-content !important;
    margin: 24px auto 16px !important;
  }

  /* -- Footer mobile -- */
  .ds-site-footer {
    padding: 40px 16px 16px !important;
  }
  .ds-footer-inner {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  .ds-footer-bar {
    flex-direction: column;
    gap: 8px;
    text-align: center;
  }


  /* =========================================================================
     10b. PAGE-HOME MOBILE — .page-home scoped
     ========================================================================= */

  /* Hero section: stack content + scroll indicator vertically */
  .page-home #hero {
    flex-direction: column !important;
  }

  /* Journey image grid: full aspect ratio */
  .page-home .ds-journey-grid {
    grid-template-columns: 1fr !important;
    gap: 16px !important;
  }
  .page-home .ds-journey-grid > div {
    min-height: auto !important;
    border-radius: 16px !important;
    overflow: hidden !important;
  }
  .page-home .ds-journey-grid img {
    width: 100% !important;
    height: auto !important;
    max-height: none !important;
    object-fit: contain !important;
    border-radius: 16px !important;
  }

  /* Commencement photo: full width */
  .page-home img[alt*="Commencement"],
  .page-home img[alt*="commencement"],
  .page-home img[alt*="graduation"],
  .page-home img[alt*="Graduation"],
  .page-home img[alt*="Class of 2024"] {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    border-radius: 12px !important;
  }

  /* University logos in degree cards */
  .page-home [alt*="AUC School"],
  .page-home [alt*="Rutgers ISE"] {
    max-height: 60px !important;
    margin-top: 12px !important;
  }

  /* Commencement people info: stack */
  .page-home .ds-people-row {
    flex-direction: column !important;
    gap: 16px !important;
  }

  /* RIA logo button: prevent overflow */
  .page-home [alt="RIA Lab"] {
    max-height: 24px !important;
  }


  /* =========================================================================
     10c. PAGE-RESEARCH MOBILE — .page-research scoped
     ========================================================================= */

  /* -- Research hero: stack on mobile -- */
  .page-research #research-hero {
    height: auto !important;
    min-height: 100vh;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-end !important;
    padding: 56px 20px 24px !important;
    margin-top: -56px !important;
    overflow: visible !important;
  }

  .page-research #research-hero video,
  .page-research #research-hero > div:first-of-type,
  .page-research #research-hero > div:nth-of-type(2) {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
  }

  .page-research .research-hero-stats {
    position: static !important;
    order: 1;
    display: flex !important;
    justify-content: center !important;
    gap: 8px !important;
    margin-bottom: 16px;
    z-index: 5;
  }
  .page-research .research-hero-stats > div {
    padding: 8px 12px !important;
    flex: 1;
    max-width: 110px;
  }
  .page-research .research-hero-stats > div > div:first-child {
    font-size: 1rem !important;
  }
  .page-research .research-hero-stats > div > div:last-child {
    font-size: 0.55rem !important;
  }

  .page-research .research-hero-content {
    position: static !important;
    order: 2;
    z-index: 5;
    max-width: 100% !important;
    text-align: center !important;
  }
  .page-research .research-hero-content > div:first-child {
    padding: 1.25rem !important;
    border-radius: 16px !important;
    display: flex !important;
    flex-direction: column !important;
  }

  /* Logo links row — move to bottom of card */
  .page-research .research-hero-content > div:first-child > div:first-child {
    order: 10 !important;
    justify-content: center !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    margin-bottom: 0 !important;
    margin-top: 1rem !important;
  }
  /* Higher specificity version for #root override */
  .page-research #root .research-hero-content > div:first-child > div:first-child {
    order: 10 !important;
    margin-bottom: 0 !important;
    margin-top: 0.75rem !important;
    flex-direction: row !important;
    justify-content: center !important;
    align-items: center !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
  }

  /* Logo buttons — darker background + glow */
  .page-research .research-hero-content > div:first-child > div:first-child a {
    padding: 6px 12px 6px 8px !important;
    border-radius: 12px !important;
    background: rgba(0,0,0,0.55) !important;
    border: 0.5px solid rgba(255,255,255,0.2) !important;
    animation: heroButtonGlow 3s ease-in-out infinite !important;
  }
  .page-research .research-hero-content > div:first-child > div:first-child img {
    height: 26px !important;
    width: auto !important;
    filter: brightness(1.3) !important;
  }

  .page-research .research-hero-content h1 {
    font-size: 1.5rem !important;
    text-align: center !important;
  }
  .page-research .research-hero-content p {
    text-align: center !important;
    font-size: 0.85rem !important;
  }

  /* Author/metadata row: center and wrap */
  .page-research .research-hero-content > div:first-child > div:nth-child(4) {
    justify-content: center !important;
  }
  /* Institution line */
  .page-research .research-hero-content > div:first-child > div:last-child {
    text-align: center !important;
  }

  /* Cap RIA logo in overview tab */
  .page-research img[alt*="RIA - Renewables"] {
    max-width: 160px !important;
    width: auto !important;
  }

  /* Scroll indicator in research hero */
  .page-research #research-hero .ds-scroll-indicator {
    position: static !important;
    order: 3;
    margin: 16px auto 0 !important;
    bottom: auto !important;
    left: auto !important;
    transform: none !important;
    width: fit-content !important;
  }

  /* -- Research grid controls by minmax value -- */
  /* Stat/config cards (small minmax) — 2 per row */
  .page-research #root [style*="display: grid"][style*="minmax(160px"],
  .page-research #root [style*="display: grid"][style*="minmax(180px"] {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 8px !important;
  }
  .page-research #root [style*="display: grid"][style*="minmax(250px"] {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 8px !important;
  }
  /* Long-text cards (large minmax) — single column */
  .page-research #root [style*="display: grid"][style*="minmax(280px"],
  .page-research #root [style*="display: grid"][style*="minmax(320px"],
  .page-research #root [style*="display: grid"][style*="minmax(340px"] {
    grid-template-columns: 1fr !important;
    gap: 12px !important;
  }
  /* Compact stat card text */
  .page-research #root [style*="display: grid"][style*="minmax(180px"] > div,
  .page-research #root [style*="display: grid"][style*="minmax(250px"] > div {
    padding: 0.75rem !important;
  }

  /* Research-specific footer margin */
  .page-research .ds-site-footer {
    margin-top: 0 !important;
  }

  /* Tab bar — wrap buttons, not scrollable */
  .page-research [style*="position: sticky"][style*="top: 56px"] > div {
    white-space: normal !important;
    overflow-x: visible !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 6px !important;
    justify-content: center !important;
  }
  .page-research [style*="position: sticky"][style*="top: 56px"] > div > button {
    padding: 0.4rem 0.7rem !important;
    font-size: 0.7rem !important;
    margin-right: 0 !important;
    margin-bottom: 0 !important;
    white-space: nowrap !important;
  }

  /* Multi-column fixed grids — 2 per row */
  .page-research #root [style*="display: grid"][style*="repeat(5"],
  .page-research #root [style*="display: grid"][style*="repeat(6"] {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 8px !important;
  }

  /* Sponsor/funding logos — smaller */
  .page-research [style*="Supported By"] + div img,
  .page-research [style*="gap: 2.5rem"] > a img {
    height: 28px !important;
    width: auto !important;
  }
  .page-research [style*="gap: 2.5rem"] {
    gap: 1rem !important;
  }

  /* Dataset Engineering cards — stack title + pills */
  .page-research #root [style*="justify-content: space-between"][style*="align-items: flex-start"],
  .page-research #root [style*="justify-content: space-between"][style*="align-items: center"] {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 6px !important;
  }

  /* Monospace filenames: wrap + truncate */
  .page-research #root h4[style*="Courier"] {
    word-break: break-all !important;
    font-size: 0.78rem !important;
    line-height: 1.4 !important;
  }

  /* 3-column detail grids: single column */
  .page-research #root [style*="display: grid"][style*="1fr 1fr 1fr"]:not([style*="repeat"]) {
    grid-template-columns: 1fr !important;
    gap: 6px !important;
  }

  /* Overflow containers — horizontal scroll */
  .page-research #root [style*="overflow-x: auto"],
  .page-research #root [style*="overflowX"] {
    max-width: 100% !important;
    -webkit-overflow-scrolling: touch;
  }

  /* Tables — readable min-width */
  .page-research #root [style*="overflow"] table {
    min-width: 600px !important;
    font-size: 0.78rem !important;
  }
  .page-research #root [style*="overflow"] table th,
  .page-research #root [style*="overflow"] table td {
    padding: 0.6rem 0.75rem !important;
    white-space: nowrap !important;
  }
  .page-research #root table,
  .page-research #root pre,
  .page-research #root code {
    font-size: 0.7rem !important;
    word-break: break-all;
  }

  /* Multi-column grids → 2 per row */
  .page-research #root [style*="display: grid"][style*="1fr 1fr 1fr"],
  .page-research #root [style*="display: grid"][style*="repeat(3"],
  .page-research #root [style*="display: grid"][style*="repeat(4"] {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 8px !important;
  }

  /* SVG figures */
  .page-research #root svg[viewBox] {
    max-width: 100% !important;
    height: auto !important;
  }

  /* Image figures (flowcharts, diagrams) */
  .page-research #root img[alt*="framework"],
  .page-research #root img[alt*="Framework"],
  .page-research #root img[alt*="POSYDON"],
  .page-research #root img[alt*="pipeline"],
  .page-research #root img[alt*="Pipeline"] {
    width: 100% !important;
    height: auto !important;
    max-width: none !important;
  }

  /* Figure containers — scrollable */
  .page-research #root [style*="overflow: hidden"] {
    overflow: auto !important;
    -webkit-overflow-scrolling: touch;
  }


  /* =========================================================================
     10d. PAGE-PORTFOLIO MOBILE — .page-portfolio scoped
     (Placeholder — to be filled during portfolio mobile optimization)
     ========================================================================= */


  /* =========================================================================
     10e. PAGE-TEACHING MOBILE — .page-teaching scoped
     ========================================================================= */

  /* Teaching stats: stack properly */
  .page-teaching .ds-teaching-stats {
    flex-direction: column !important;
    gap: 16px !important;
    align-items: stretch !important;
  }
  .page-teaching .ds-teaching-stats-grid {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
  }
  .page-teaching [style*="gridTemplateColumns: 'repeat(4"] {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
  }

  /* Contact cards: single column */
  .page-teaching [style*="gridTemplateColumns: 'repeat(4, 1fr)'"] {
    grid-template-columns: 1fr !important;
    gap: 12px !important;
  }


  /* =========================================================================
     10f. PAGE-SHOWCASE MOBILE — .page-showcase scoped
     Pipeline B inline-style overrides (attribute selectors + !important)
     These ONLY apply to the 10 Vite-bundled showcase pages.
     ========================================================================= */

  /* Grid columns → single column */
  .page-showcase [style*="grid-template-columns"] {
    grid-template-columns: 1fr !important;
  }

  /* Large paddings → reduced */
  .page-showcase [style*="padding: 3rem"],
  .page-showcase [style*="padding:3rem"],
  .page-showcase [style*="padding: 4rem"],
  .page-showcase [style*="padding:4rem"],
  .page-showcase [style*="padding: 100px"],
  .page-showcase [style*="padding:100px"] {
    padding: 24px 16px !important;
  }
  .page-showcase [style*="padding: 80px"],
  .page-showcase [style*="padding:80px"] {
    padding: 48px 16px !important;
  }
  .page-showcase [style*="padding: 64px"],
  .page-showcase [style*="padding:64px"] {
    padding: 40px 16px !important;
  }
  .page-showcase [style*="padding: 60px"],
  .page-showcase [style*="padding:60px"] {
    padding: 36px 16px !important;
  }
  .page-showcase [style*="padding: 48px"],
  .page-showcase [style*="padding:48px"] {
    padding: 32px 16px !important;
  }

  /* 100vh sections → auto height */
  .page-showcase [style*="height: 100vh"],
  .page-showcase [style*="height:100vh"],
  .page-showcase [style*="min-height: 100vh"],
  .page-showcase [style*="min-height:100vh"] {
    height: auto !important;
    min-height: auto !important;
    padding-top: 60px !important;
    padding-bottom: 40px !important;
  }

  /* Large font-sizes → clamped */
  .page-showcase [style*="font-size: 3"],
  .page-showcase [style*="font-size:3"] {
    font-size: clamp(1.5rem, 6vw, 2.2rem) !important;
  }
  .page-showcase [style*="font-size: 2"],
  .page-showcase [style*="font-size:2"] {
    font-size: clamp(1.2rem, 5vw, 1.75rem) !important;
  }

  /* Wide-gap flex rows → column stack */
  .page-showcase [style*="display: flex"][style*="gap: 4"],
  .page-showcase [style*="display:flex"][style*="gap:4"],
  .page-showcase [style*="display: flex"][style*="gap: 3"],
  .page-showcase [style*="display:flex"][style*="gap:3"] {
    flex-direction: column !important;
  }

  /* Background images */
  .page-showcase [style*="background-image"] {
    background-size: cover !important;
    background-position: center !important;
  }

  /* Buttons: full width */
  .page-showcase [style*="borderRadius: '980px'"],
  .page-showcase [style*="border-radius: 980px"] {
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
  }

  /* Resume/CV card: tone down glow */
  .page-showcase [style*="boxShadow"][style*="rgba(0,113,227"] {
    box-shadow: 0 2px 12px rgba(0,113,227,0.15) !important;
  }

  /* Section padding tighter */
  .page-showcase section > div[style*="maxWidth"],
  .page-showcase [style*="max-width: 1200px"],
  .page-showcase [style*="maxWidth: '1200px'"] {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }

  /* Tab nav: horizontal scroll with momentum */
  .page-showcase [style*="position: sticky"] {
    padding: 8px 12px !important;
  }
  .page-showcase [style*="position: sticky"] button,
  .page-showcase [style*="position: sticky"] a {
    font-size: 0.75rem !important;
    padding: 6px 12px !important;
    white-space: nowrap;
  }

  /* 3D model viewers & canvas */
  .page-showcase canvas {
    max-width: 100% !important;
    max-height: 60vh !important;
  }
  .page-showcase model-viewer {
    max-width: 100% !important;
    max-height: 300px !important;
  }

} /* end @media (max-width: 639px) */
```

- [ ] **Step 2: Verify the CSS is syntactically valid**

Open `http://localhost:3000` and check browser console for CSS parse errors.

- [ ] **Step 3: Commit**

```bash
git add public/design-system.css
git commit -m "refactor: scope all mobile CSS rules to page-specific body classes

Restructured the mobile media query in design-system.css:
- Shared rules: universal (nav, drawer, overflow, text, footer)
- .page-home: homepage-specific (hero, journey, commencement, logos)
- .page-research: research showcase (hero, tabs, grids, tables, figures)
- .page-teaching: teaching page (stats, contact cards)
- .page-showcase: Pipeline B broad attribute selectors

This prevents cross-page CSS bleeding that broke homepage mobile
after research showcase fixes in Session 3."
```

---

### Task 4: Visual verification

- [ ] **Step 1: Start local server**

```bash
cd public && python -m http.server 3000
```

- [ ] **Step 2: Verify homepage mobile (440x956)**

Open `http://localhost:3000/` in Chrome DevTools mobile mode (440x956).
Check: hero stacking, degree cards readable, journey images, commencement photo full-width, footer.

- [ ] **Step 3: Verify homepage desktop (1440x900)**

Same URL at 1440x900. Check: nothing changed from current live state.

- [ ] **Step 4: Verify research showcase mobile (440x956)**

Open `http://localhost:3000/research-showcase.html`. Check: hero, tabs, grids, tables, figures — all Session 3 fixes still working.

- [ ] **Step 5: Verify research showcase desktop (1440x900)**

Same URL at 1440x900. No regressions.

- [ ] **Step 6: Spot-check a Pipeline B page mobile**

Open any showcase page (e.g., `http://localhost:3000/thesis-showcase.html`) at 440x956. Check: padding, grids, fonts are properly adjusted.

- [ ] **Step 7: Spot-check Pipeline B page desktop**

Same URL at 1440x900. No regressions.
