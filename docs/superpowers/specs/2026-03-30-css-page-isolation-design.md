# CSS Page Isolation Architecture — Design Spec

**Date:** 2026-03-30
**Status:** Approved
**Branch:** dev2

## Problem

`design-system.css` contains mobile responsive rules using broad CSS attribute selectors (e.g., `[style*="grid-template-columns"]`, `[style*="height: 100vh"]`) that were added to fix Pipeline B Vite-bundled pages but also match elements on Pipeline A pages (homepage, research, portfolio, teaching). Research showcase mobile fixes in Session 3 broke the homepage mobile layout because nothing scopes rules to specific pages.

## Solution: Page-Scoped Body Classes

Add a unique class to `<body>` on each page. Prefix all page-specific mobile rules with that class.

### Body Class Mapping

| Page | File | Body Class | Pipeline |
|------|------|-----------|----------|
| Homepage | index.html | `page-home` | A |
| Research | research-showcase.html | `page-research` | A |
| Portfolio | portfolio.html | `page-portfolio` | A |
| Teaching | teaching-showcase.html | `page-teaching` | A |
| Thesis | thesis-showcase.html | `page-showcase` | B |
| Design II | design-ii-showcase.html | `page-showcase` | B |
| FEM | fem-showcase.html | `page-showcase` | B |
| CFD | naca0024-cfd-showcase.html | `page-showcase` | B |
| Failure Analysis | failure-analysis-showcase.html | `page-showcase` | B |
| System Dynamics | system-dynamics-showcase.html | `page-showcase` | B |
| Additive Mfg | am-showcase.html | `page-showcase` | B |
| Data Analytics | ise507-showcase.html | `page-showcase` | B |
| Forecasting | ise530-showcase.html | `page-showcase` | B |
| Data Mining | ise694-showcase.html | `page-showcase` | B |

All 10 Pipeline B pages share `page-showcase` since they share the same Vite-bundled structure and need the same mobile overrides.

### CSS File Structure (design-system.css)

```
SECTION 1-8: SHARED (unchanged)
  - Tokens, fonts, animations, scrollbar, header/nav, scroll indicator
  - Desktop-first defaults (hamburger hidden, drawer hidden)

SECTION 9: TABLET BREAKPOINT (640-1024px)
  - Shared tablet rules (hamburger, drawer, grid collapse)

SECTION 10: MOBILE BREAKPOINT (max-width: 639px)
  10a. SHARED MOBILE — truly universal rules
       - Variable overrides (font sizes, spacing)
       - Class-based rules (.ds-grid-*, .ds-hero-*, .ds-hamburger, .ds-mobile-drawer)
       - Navigation drawer
       - Back-nav sizing
       - Overflow prevention (body, #root overflow-x: clip)
       - Text wrapping
       - Scroll indicator positioning
       - Footer mobile

  10b. PAGE-HOME MOBILE — .page-home scoped
       - #hero flex-direction: column
       - Journey grid
       - Commencement photo
       - Degree card logos
       - People row stacking
       - Stats grid
       - Hero buttons
       - Hero CTA sizing

  10c. PAGE-RESEARCH MOBILE — .page-research scoped
       - Research hero (flex column, video bg, stats, content)
       - Tab bar wrapping
       - Grid minmax rules (2-per-row vs 1-per-row by minmax value)
       - Dataset cards, monospace filenames
       - Sponsor logos
       - Tables horizontal scroll
       - SVG/canvas/figures
       - Research-specific footer margin

  10d. PAGE-PORTFOLIO MOBILE — .page-portfolio scoped
       - (Placeholder — to be filled during portfolio mobile optimization)

  10e. PAGE-TEACHING MOBILE — .page-teaching scoped
       - Teaching stats stacking
       - Teaching stats grid
       - Contact cards single column

  10f. PAGE-SHOWCASE MOBILE — .page-showcase scoped
       - Pipeline B inline-style overrides (attribute selectors + !important)
       - Grid columns → single column
       - Large paddings → reduced
       - 100vh sections → auto height
       - Large font-sizes → clamped
       - Wide-gap flex → column stack
       - Buttons full width
       - Resume/CV card glow
       - Section padding
       - Canvas/model-viewer constraints
       - Background images
       - Tab nav scroll

SECTION 11: SITE FOOTER (unchanged, outside media queries)
```

### Rule Migration Plan

Each existing mobile rule gets categorized:

**SHARED (stays unscoped):**
- `:root` variable overrides
- `.ds-*` class-based rules (grid, hero, hamburger, drawer, buttons, scroll indicator, footer)
- `body { overflow-x: hidden }`
- `#root { overflow-x: clip }` and `main, section, article { overflow-x: hidden }`
- `h1-h6, p, span, a, li { word-wrap }` text wrapping
- `img, video, canvas, svg { max-width: 100% }` media overflow prevention

**PAGE-HOME (.page-home):**
- `#hero { flex-direction: column }`
- `.ds-journey-grid` rules
- `img[alt*="Commencement"]` etc.
- `[alt*="AUC School"], [alt*="Rutgers ISE"]` logo sizing
- `.ds-people-row` stacking
- `[alt="RIA Lab"]` sizing

**PAGE-RESEARCH (.page-research):**
- `#research-hero` and all sub-rules
- `.research-hero-stats` and `.research-hero-content`
- `#root .research-hero-content` specificity rules
- `#root [style*="display: grid"][style*="minmax("]` grid rules
- Tab bar rules `[style*="position: sticky"][style*="top: 56px"]`
- `#root [style*="justify-content: space-between"]` dataset layout
- `#root h4[style*="Courier"]` monospace filenames
- `#root [style*="display: grid"][style*="1fr 1fr 1fr"]` detail grids
- `#root [style*="overflow"]` scroll containers and tables
- `#root svg[viewBox]`, image figures, overflow containers
- Sponsor logos `[style*="gap: 2.5rem"]`
- `img[alt*="RIA - Renewables"]` logo cap
- `.ds-site-footer { margin-top: 0 }` research-specific

**PAGE-TEACHING (.page-teaching):**
- `.ds-teaching-stats` rules
- `.ds-teaching-stats-grid` rules
- `[style*="gridTemplateColumns: 'repeat(4"]` grid override
- `[style*="gridTemplateColumns: 'repeat(4, 1fr)'"]` contact cards

**PAGE-SHOWCASE (.page-showcase):**
- ALL broad `[style*="..."]` attribute selectors currently at lines 618-693:
  - `[style*="grid-template-columns"]`
  - `[style*="padding: Xrem/px"]`
  - `[style*="height: 100vh"]`
  - `[style*="font-size: 2/3"]`
  - `[style*="display: flex"][style*="gap: 3/4"]`
- `[style*="background-image"]`
- `[style*="borderRadius: '980px'"]` buttons
- `[style*="boxShadow"][style*="rgba(0,113,227"]` resume glow
- `section > div[style*="maxWidth"]` section padding
- `[style*="position: sticky"] button/a` tab nav
- `canvas` and `model-viewer` constraints

### HTML Changes

**Pipeline A (direct edit):**
- `index.html`: Change `<body>` to `<body class="page-home">`
- `research-showcase.html`: Change `<body>` to `<body class="page-research">`
- `portfolio.html`: Change `<body>` to `<body class="page-portfolio">`
- `teaching-showcase.html`: Change `<body>` to `<body class="page-teaching">`

**Pipeline B (injection script):**
- Create `add_body_classes.py` script that:
  1. Reads each Pipeline B HTML file
  2. Replaces `<body>` with `<body class="page-showcase">`
  3. Handles cases where `<body>` already has attributes
- Run once, verify, commit

### Safety Protocol

1. All work on `dev2` branch
2. No rules deleted — only moved and scoped
3. Desktop layout untouched (all changes inside mobile media query)
4. Verify each page at localhost:3000 at 440x956 (mobile) AND 1440x900 (desktop)
5. Only merge to main after full verification

### Success Criteria

- Homepage mobile view matches its pre-Session-3 state (degree cards readable, journey images correct, commencement photo full-width)
- Research showcase mobile view unchanged from Session 3 fixes
- No desktop regressions on any page
- Every mobile rule is scoped to exactly the pages it should affect
- Future page additions only need: add body class + add scoped section in CSS
