# HANDOFF: aosawy.org Website — Session 4

## What This Is
You are continuing work on the professional academic website at `C:\Users\aosaw\Claude\AOSAWY.ORG Website Project`. The site is LIVE at aosawy.org. You are on the `dev2` branch. Previous sessions built all pages; Session 4 polished all 4 Pipeline A pages to production quality.

## What Was Done in Session 4 (2026-03-30 to 2026-03-31)

### Architecture: CSS Page Isolation
- Added body classes to all 14 pages (`page-home`, `page-research`, `page-portfolio`, `page-teaching`, `page-showcase`)
- Restructured `design-system.css` mobile media query into labeled scoped sections
- Established defensive rule pattern for images: `img[style*="width: 100%"]:not([alt*="RIA"])` caps at 240px
- Each page's mobile rules are isolated — changes to one page never affect another

### Site-Wide Infrastructure
- **Favicon:** Full set (favicon.svg, favicon.ico, PNGs 16-512, apple-touch-icon, site.webmanifest) — sigma logo with blue→purple gradient
- **OG Image:** og-image.png (1200x630) with sigma logo + text, full OG + Twitter card meta tags on all 14 pages
- **Clean URLs:** `_redirects` file maps 13 clean paths. Homepage + portfolio links already updated. Research/teaching static headers updated.
- **Local dev server:** `public/serve.py` — Python HTTP server that reads `_redirects` and handles rewrites (run from `public/` directory)
- **WhatsApp → Phone:** All references changed to `tel:+18482097088` with phone icon
- **Footer white gap fix:** `html { background: #1d1d1f }` + `:has()` selector zeros parent padding-bottom + footer padding-bottom: 80px
- **All heroes standardized:** 100vh on all pages

### Homepage (index.html) — COMPLETE
- Favicon + OG tags, clean URLs (33 links updated), SARIMA-X typo fixed
- Scroll-reveal class aligned (.visible + .revealed alias)
- 0 console errors, 0 warnings

### Research Showcase (research-showcase.html) — COMPLETE (all 7 tabs)
- **Hero card:** Logos at bottom with dark bg + white glow animation (ALL viewports via CSS outside media queries)
- **Tab bar:** Wraps centered on all viewports (no scrollbar) via global CSS rule
- **Tab persistence:** URL hash (#ria, #evolution, etc.) + sessionStorage scroll position + hashchange listener
- **Title:** Changed to "Offshore Wind Farm Operations & Maintenance Research" (both hero h1 and overview h1 at 2.2rem)
- **Tab arrow:** ▶ (U+25B6) in "HOST ▶ POSYDON"
- **prop-types:** Added before Recharts to eliminate 3 console errors
- **RIA logo:** Capped at 120px (all viewports). Two different images: `alt="RIA - Renewables & Industrial Analytics"` (standalone, 120px) and `alt="RIA Lab"` (button, 28px)
- **Thrust images:** Fixed border-radius mismatch (8px vs 10px container selectors)
- **Wind Farm Assumptions + MILP + Rolling Horizon + Experiment Pipeline:** Alt-text overrides for full-width display
- **Sensitivity Analysis cards:** 3-col `1fr 2fr 1fr` grid → single column on mobile
- **Pipeline Overview:** Vertical HTML card layout on mobile (SVG hidden), horizontal SVG on desktop
- **Framework Evolution Timeline:** Redesigned as responsive HTML/CSS (3 circles, horizontal desktop, vertical mobile, 160px arrows)
- **Research Interconnections:** Redesigned as 3-column grid (feeds | arrows | core circle 210px)
- **Framework Comparison:** 3rem spacer added above section
- **Dr. Ezzat profile photo:** Preserved at 90px circle on mobile
- **0 console errors, 0 warnings**

### Portfolio (portfolio.html) — COMPLETE
- **Institution colors:** AUC blue (#003366) for all Chapter I showcases, Rutgers scarlet (#CC0033) for Chapters II & III
- **Dark footer:** Full branded ds-site-footer (3-column) matching all other pages
- **Hero:** 100vh, dark navy gradient, white stat values, scroll indicator as direct child of section
- **Mobile:** Stats column layout, #hero flex-direction: column, showcase grid single column
- **Chapters:** 7 projects in Chapter I (AM integrated), 30 Credits + 2026 Graduated in Chapter II, RIA Lab clickable stat in Chapter III
- **Clean URLs:** All 14+ internal links updated
- **0 console errors**

### Teaching Showcase (teaching-showcase.html) — COMPLETE (all 7 tabs)
- **Hero:** Dark navy gradient (matching portfolio/homepage), 100vh, scroll indicator fixed
- **Tab bar:** Matches research page exactly (wrap, center, glass, sticky)
- **Tab persistence:** URL hash + scroll position
- **2-color system:** Rutgers Scarlet #CC0033 + navy text only — no blue/green/orange/purple
- **Dark footer:** Full branded ds-site-footer
- **Clean URLs + OG/meta descriptions + float1/float2 keyframes**
- **Design alignment:** All stat grids responsive, all pills aligned, color tokens unified
- **Math equations:** 341 double-escaped Unicode sequences fixed, 3 bugs fixed (Eigenvector &nbsp;, Katz subscript, Exponential CDF formula)
- **ISE 338:** Grading Breakdown removed, "Course Grader" → "Teaching Assistant", Assessments/Sections lines removed
- **Mobile:** All 2-col/3-col grids → single column, math content smaller font + word-break
- **0 console errors**

## Current State (as of 2026-03-31)
- `main` branch = LIVE at aosawy.org (Session 3 state)
- `dev2` branch = ALL Session 4 work (ready to merge to main and push)
- All 4 Pipeline A pages: DONE, production-ready
- 10 Pipeline B pages: NOT YET POLISHED

## What Remains — The Big Task

### 10 Pipeline B Showcase Pages (Vite-bundled, minified)
These are the individual project showcase pages. They need:

1. **Dark footer injection** — Add ds-site-footer HTML after the React #root div
2. **Mobile QA** — Apply all mobile patterns established in Session 4
3. **3D interactive models NOT rendering** — CRITICAL bug, models show blank/broken
4. **Internal links** — Update to clean URLs where possible (limited since minified)
5. **Favicon/OG tags** — Already added in Session 4 ✓

**Pipeline B constraints:** These are Vite-bundled (minified JS). You can only:
- Add CSS in `<head>` (via design-system.css or inline `<style>`)
- Add HTML after `<div id="root"></div>` (for footer injection)
- Modify the `<head>` section
- You CANNOT modify the minified JS bundle

**Pages:**
| # | File | Clean URL | Content |
|---|------|-----------|---------|
| 1 | thesis-showcase.html | /thesis | BSc Thesis — Electricity-Generating Tripod Turnstile |
| 2 | design-ii-showcase.html | /design | 2-Stage Planetary Reduction Gearbox |
| 3 | fem-showcase.html | /fem | FEM Analysis of Cooled Turbine Blade |
| 4 | naca0024-cfd-showcase.html | /cfd | NACA 0024 Airfoil CFD Analysis |
| 5 | failure-analysis-showcase.html | /failure-analysis | Camshaft Support Cap Failure |
| 6 | system-dynamics-showcase.html | /dynamics | AEB Suspension System Dynamics |
| 7 | am-showcase.html | /additive | Additive Manufacturing |
| 8 | ise507-showcase.html | /data-analytics | Data Analytics (Mental Health) |
| 9 | ise530-showcase.html | /forecasting | Forecasting (Electricity Prices) |
| 10 | ise694-showcase.html | /data-mining | Data Mining (Loan Payback) |

### Key Design Patterns to Apply (from Session 4)

**Hero sections:**
- 100vh, dark gradient or video background
- Scroll indicator as direct child of section (not inside content div)
- Mobile: #hero { flex-direction: column }
- Stat cards: white values, column on mobile

**Tab/sticky bars:**
- Glass nav: position sticky, top 56px, zIndex 100
- Inner div: overflowX auto, whiteSpace nowrap (CSS overrides to wrap)
- Tab persistence: URL hash + sessionStorage scroll

**Cards and images:**
- GlassCard: rgba(255,255,255,0.65), blur 20px, border-radius 16px, padding 1.5rem
- Images inside cards: centered, object-fit contain, not cropped
- Target images by EXACT alt text for mobile overrides
- Defensive rule catches all img[style*="width: 100%"]

**Mobile grids:**
- All 2-col/3-col grids → single column on mobile
- Stat grids: repeat(auto-fit, minmax(180px, 1fr))
- Tables: horizontal scroll with min-width 600px

**Footer:**
- Dark ds-site-footer with 3 columns (About, Quick Links, Connect)
- :has() selector zeros parent padding-bottom
- html background matches footer dark color

### Other Items
- Publications & Awards: still placeholders on homepage
- FEM showcase PDF (41MB): needs Cloudflare R2 hosting
- Contact page: deferred

## Technical Reference

### Git Identity
- `user.name "Abdelrahman O. Sawy"`, `user.email "a.sawy@rutgers.edu"` (repo-local)

### Local Preview
```bash
cd public && python serve.py
```
Serves at http://localhost:3000 with clean URL rewrite support.
iPad preview: http://10.0.0.81:3000/

### CSS Architecture (design-system.css, ~1700 lines)
```
Sections 1-8: SHARED (tokens, fonts, animations, scrollbar, header/nav)
Section 9a: TABLET (640-1024px)
Section 9a-post: ALL-VIEWPORT rules (RIA logo cap, hero card logos, tab bar wrap, stat link hover, pipeline mobile card, fw-timeline, ri-network)
Section 9b: MOBILE (<640px)
  - SHARED MOBILE (variables, grids, hero, hamburger, drawer, overflow, text, scroll indicator, footer)
  - PAGE-HOME MOBILE
  - PAGE-RESEARCH MOBILE (50+ rules)
  - PAGE-PORTFOLIO MOBILE
  - PAGE-TEACHING MOBILE
  - PAGE-SHOWCASE MOBILE (broad attribute selectors for Pipeline B)
Section 10: SITE FOOTER
Section 11: FOOTER :has() fix
```

### Key Rule
When making changes: NEVER break existing animations, 3D viewers, videos, or immersive flow. Test at both desktop (1440x900) and mobile (440x956) before committing. NEVER add broad img/video !important rules outside the mobile media query.
