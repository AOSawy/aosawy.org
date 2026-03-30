# Design System Remediation — aosawy.org

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make all 14 pages visually coherent — same fonts, colors, spacing, animations, navigation, and fully responsive on desktop + mobile.

**Architecture:** Two modification strategies based on build pipeline:
- **Pipeline A** (index.html, portfolio.html, research-showcase.html, teaching-showcase.html): Edit inline JS/CSS directly — these are readable source.
- **Pipeline B** (10 showcase pages): Inject `<head>` CSS, `<title>` fixes, and post-root HTML (floating nav) without touching the minified Vite bundle.

A shared `design-system.css` file will be created and linked from all 14 pages, providing tokens, responsive breakpoints, and standardized animations as CSS custom properties and utility classes. Page-specific overrides use `!important` where the bundle's inline styles conflict.

**Tech Stack:** Pure CSS (custom properties, @media queries, @keyframes), HTML injection, no build tools needed.

**Branch:** `dev` — all work happens here, merged to `main` when verified.

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `public/design-system.css` | **CREATE** | Shared CSS: custom properties, fonts, responsive breakpoints, animations, nav, utility classes |
| `public/index.html` | MODIFY | Link design-system.css, fix nav hamburger, add responsive, harmonize SectionTitle |
| `public/portfolio.html` | MODIFY | Link design-system.css, fix nav hamburger, add responsive, harmonize spacing |
| `public/research-showcase.html` | MODIFY | Link design-system.css, fix font override, add scroll-reveal, harmonize SectionTitle |
| `public/teaching-showcase.html` | MODIFY | Link design-system.css, fix font override, add scroll-reveal, harmonize SectionTitle |
| `public/thesis-showcase.html` | MODIFY `<head>` + post-root | Link design-system.css, fix title, add floating nav, font override fix |
| `public/design-ii-showcase.html` | MODIFY `<head>` + post-root | Same pattern as thesis |
| `public/fem-showcase.html` | MODIFY `<head>` + post-root | Same pattern |
| `public/naca0024-cfd-showcase.html` | MODIFY `<head>` + post-root | Same pattern |
| `public/failure-analysis-showcase.html` | MODIFY `<head>` + post-root | Same pattern |
| `public/system-dynamics-showcase.html` | MODIFY `<head>` + post-root | Same pattern |
| `public/am-showcase.html` | MODIFY `<head>` + post-root | Same pattern |
| `public/ise507-showcase.html` | MODIFY `<head>` + post-root | Same pattern |
| `public/ise530-showcase.html` | MODIFY `<head>` + post-root | Same pattern |
| `public/ise694-showcase.html` | MODIFY `<head>` + post-root | Same pattern |

---

## Task 1: Create Shared Design System CSS

**Fixes:** I-01, I-04, I-05, I-06, I-07, I-09, A-01, A-03, G-04, G-05, C-01, L-02 (partial)
**Files:**
- Create: `public/design-system.css`

This is the foundation — every other task depends on it.

- [ ] **Step 1: Create `public/design-system.css` with CSS custom properties, font imports, and standardized animations**

```css
/* ============================================
   aosawy.org — Design System
   Apple Liquid Glass + Academic Authority
   ============================================ */

/* --- Google Fonts --- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;600;700&display=swap');

/* --- Design Tokens as CSS Custom Properties --- */
:root {
  /* Colors */
  --color-bg: #f5f5f7;
  --color-text: #1d1d1f;
  --color-secondary: #6e6e73;
  --color-tertiary: #86868b;
  --color-accent: #0071e3;
  --color-accent-light: rgba(0, 113, 227, 0.06);
  --color-accent-border: rgba(0, 113, 227, 0.15);
  --color-border: rgba(0, 0, 0, 0.06);

  /* Glass */
  --glass-card-bg: rgba(255, 255, 255, 0.65);
  --glass-card-blur: saturate(180%) blur(20px);
  --glass-card-border: 0.5px solid rgba(0, 0, 0, 0.06);
  --glass-card-radius: 16px;
  --glass-card-shadow: 0 1px 4px rgba(0, 0, 0, 0.03);
  --glass-nav-bg: rgba(255, 255, 255, 0.72);
  --glass-surface-bg: rgba(255, 255, 255, 0.45);
  --glass-surface-blur: saturate(120%) blur(12px);

  /* Typography */
  --font-heading: 'Playfair Display', Georgia, serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif;
  --font-math: 'Cambria Math', 'Latin Modern Math', 'STIX Two Math', Georgia, 'Times New Roman', serif;

  /* Standardized font sizes */
  --fs-h1: clamp(2.4rem, 5.5vw, 3.8rem);
  --fs-h2: 2rem;
  --fs-h3: 1.1rem;
  --fs-body: 0.95rem;
  --fs-label: 0.73rem;
  --fs-pill: 0.73rem;
  --fs-button: 0.85rem;
  --fs-nav: 0.82rem;

  /* Spacing */
  --section-padding: 80px 24px;
  --card-padding: 24px;
  --container-max: 1200px;

  /* Transitions */
  --transition-fast: all 0.2s ease;
  --transition-normal: all 0.3s ease;

  /* Button */
  --button-radius: 12px;
  --pill-radius: 100px;
}

/* --- Font Override (fixes I-04, I-05) ---
   Pipeline B pages inject body { font-family: -apple-system... } via useEffect.
   This overrides it back to Inter. */
body {
  font-family: var(--font-body) !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: var(--color-bg);
  color: var(--color-text);
  line-height: 1.6;
}

/* --- Standardized Animations (fixes A-01, A-03) --- */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-40px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes slideInRight {
  from { opacity: 0; transform: translateX(40px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.85); }
  to { opacity: 1; transform: scale(1); }
}

@keyframes pulseGlow {
  0%, 100% { box-shadow: 0 0 20px rgba(0, 113, 227, 0.15); }
  50% { box-shadow: 0 0 40px rgba(0, 113, 227, 0.25); }
}

@keyframes heroFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

/* --- Scroll Reveal Utility --- */
.scroll-reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}
.scroll-reveal.revealed {
  opacity: 1;
  transform: translateY(0);
}

/* --- Floating Back-Navigation (fixes N-04, N-05) --- */
.site-back-nav {
  position: fixed;
  top: 16px;
  left: 16px;
  z-index: 9999;
  display: flex;
  gap: 8px;
}
.site-back-nav a {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: var(--glass-nav-bg);
  backdrop-filter: var(--glass-card-blur);
  -webkit-backdrop-filter: var(--glass-card-blur);
  border: var(--glass-card-border);
  border-radius: 10px;
  color: var(--color-text);
  text-decoration: none;
  font-family: var(--font-body);
  font-size: 0.8rem;
  font-weight: 500;
  transition: var(--transition-fast);
  box-shadow: var(--glass-card-shadow);
}
.site-back-nav a:hover {
  background: rgba(255, 255, 255, 0.88);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
}

/* --- Custom Scrollbar --- */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.15);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover { background: rgba(0, 0, 0, 0.25); }

/* ============================================
   RESPONSIVE BREAKPOINTS (fixes R-01)
   ============================================ */

/* --- Mobile: < 640px --- */
@media (max-width: 639px) {
  :root {
    --fs-h1: clamp(1.6rem, 8vw, 2.4rem);
    --fs-h2: 1.5rem;
    --fs-h3: 1rem;
    --fs-body: 0.9rem;
    --section-padding: 48px 16px;
    --card-padding: 16px;
  }

  /* Stack grids to single column */
  .ds-grid-2, .ds-grid-3, .ds-grid-4 {
    grid-template-columns: 1fr !important;
  }

  /* Hide desktop nav links, show hamburger */
  .ds-nav-links { display: none !important; }
  .ds-hamburger { display: flex !important; }

  /* Mobile nav drawer */
  .ds-mobile-drawer {
    display: flex !important;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: saturate(180%) blur(20px);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 24px;
    z-index: 10000;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
  }
  .ds-mobile-drawer.open {
    opacity: 1;
    pointer-events: auto;
  }
  .ds-mobile-drawer a {
    font-family: var(--font-heading);
    font-size: 1.4rem;
    color: var(--color-text);
    text-decoration: none;
  }

  /* Floating back-nav: smaller on mobile */
  .site-back-nav {
    top: 8px;
    left: 8px;
  }
  .site-back-nav a {
    padding: 6px 12px;
    font-size: 0.75rem;
  }

  /* Stats bar: 2 columns on mobile */
  .ds-stats-grid {
    grid-template-columns: 1fr 1fr !important;
  }

  /* Hero: stack photo below text */
  .ds-hero-flex {
    flex-direction: column !important;
    text-align: center;
  }
  .ds-hero-photo {
    order: -1;
    margin: 0 auto;
  }
  .ds-hero-buttons {
    justify-content: center !important;
  }
}

/* --- Tablet: 640px–1024px --- */
@media (min-width: 640px) and (max-width: 1024px) {
  :root {
    --fs-h1: clamp(2rem, 5vw, 3rem);
    --fs-h2: 1.75rem;
    --section-padding: 64px 24px;
  }

  .ds-grid-3, .ds-grid-4 {
    grid-template-columns: 1fr 1fr !important;
  }

  .ds-nav-links { display: none !important; }
  .ds-hamburger { display: flex !important; }
}

/* --- Desktop: > 1024px --- */
@media (min-width: 1025px) {
  .ds-hamburger { display: none !important; }
  .ds-mobile-drawer { display: none !important; }
}
```

- [ ] **Step 2: Commit**

```bash
git add public/design-system.css
git commit -m "feat: create shared design-system.css with tokens, responsive, animations"
```

---

## Task 2: Link Design System CSS to All 14 Pages + Fix Titles

**Fixes:** I-01, N-06
**Files:**
- Modify `<head>` of all 14 HTML files

- [ ] **Step 1: Write a Python script to inject the CSS link and fix titles into all pages**

Create `fix-heads.py`:

```python
"""
Inject design-system.css link and fix <title> tags on all 14 pages.
"""
import re
from pathlib import Path

PUBLIC = Path(r"C:\Users\aosaw\Claude\AOSAWY.ORG Website Project\public")

# Page titles (fixes N-06)
TITLES = {
    "index.html": "Abdelrahman O. Sawy — PhD Student, ISE, Rutgers University",
    "portfolio.html": "Portfolio — Abdelrahman O. Sawy",
    "research-showcase.html": "Research — Abdelrahman O. Sawy",
    "teaching-showcase.html": "Teaching — Abdelrahman O. Sawy",
    "thesis-showcase.html": "BSc Thesis: Energy-Generating Turnstile — A.O. Sawy",
    "design-ii-showcase.html": "Mechanical Design II — A.O. Sawy",
    "fem-showcase.html": "Finite Element Methods — A.O. Sawy",
    "naca0024-cfd-showcase.html": "CFD: NACA 0024 Airfoil — A.O. Sawy",
    "failure-analysis-showcase.html": "Failure Analysis — A.O. Sawy",
    "system-dynamics-showcase.html": "System Dynamics — A.O. Sawy",
    "am-showcase.html": "Additive Manufacturing — A.O. Sawy",
    "ise507-showcase.html": "ISE 507: Data Analytics — A.O. Sawy",
    "ise530-showcase.html": "ISE 530: Forecasting Analytics — A.O. Sawy",
    "ise694-showcase.html": "ISE 694: Data Mining — A.O. Sawy",
}

CSS_LINK = '<link rel="stylesheet" href="design-system.css">'

for filename, title in TITLES.items():
    path = PUBLIC / filename
    if not path.exists():
        print(f"  SKIP {filename} — not found")
        continue

    content = path.read_text(encoding='utf-8', errors='replace')

    # Fix <title>
    content = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', content, count=1)

    # Inject CSS link after <meta viewport> if not already present
    if 'design-system.css' not in content:
        content = content.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0" />',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  ' + CSS_LINK
        )
        # Also try without self-closing slash
        content = content.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n  ' + CSS_LINK
        )

    path.write_text(content, encoding='utf-8')
    print(f"  OK   {filename}")

print("Done.")
```

- [ ] **Step 2: Run the script**

```bash
cd "C:/Users/aosaw/Claude/AOSAWY.ORG Website Project"
python fix-heads.py
```

Expected: All 14 files updated with correct titles and CSS link.

- [ ] **Step 3: Verify by checking a Pipeline B page**

```bash
head -10 public/ise507-showcase.html
```

Expected: `<title>ISE 507: Data Analytics — A.O. Sawy</title>` and `<link rel="stylesheet" href="design-system.css">`.

- [ ] **Step 4: Commit**

```bash
git add public/*.html fix-heads.py
git commit -m "feat: link design-system.css to all pages, fix page titles"
```

---

## Task 3: Inject Floating Back-Navigation on All Showcase Pages

**Fixes:** N-04, N-05
**Files:**
- Modify: all 10 Pipeline B showcase pages + research-showcase.html + teaching-showcase.html (standardize existing)

- [ ] **Step 1: Write a Python script to inject uniform floating back-nav**

Create `fix-nav.py`:

```python
"""
Inject uniform floating back-navigation on all showcase pages.
Standardizes the existing home-nav on research/teaching and adds
it to all 10 Pipeline B pages.
"""
import re
from pathlib import Path

PUBLIC = Path(r"C:\Users\aosaw\Claude\AOSAWY.ORG Website Project\public")

# The standard floating nav HTML
FLOATING_NAV = '''
<!-- Site Back-Navigation -->
<div class="site-back-nav" id="siteBackNav">
  <a href="index.html">&larr; Home</a>
  <a href="portfolio.html">Portfolio</a>
</div>
'''

# Pages that need floating nav (NOT index.html or portfolio.html — they have their own nav)
SHOWCASE_PAGES = [
    "thesis-showcase.html",
    "design-ii-showcase.html",
    "fem-showcase.html",
    "naca0024-cfd-showcase.html",
    "failure-analysis-showcase.html",
    "system-dynamics-showcase.html",
    "am-showcase.html",
    "ise507-showcase.html",
    "ise530-showcase.html",
    "ise694-showcase.html",
]

# Pages with EXISTING home-nav to replace (standardize)
REPLACE_PAGES = [
    "research-showcase.html",
    "teaching-showcase.html",
]

for filename in SHOWCASE_PAGES:
    path = PUBLIC / filename
    if not path.exists():
        print(f"  SKIP {filename}")
        continue

    content = path.read_text(encoding='utf-8', errors='replace')

    if 'site-back-nav' in content:
        print(f"  SKIP {filename} — already has site-back-nav")
        continue

    # Insert after </body> opening or before </body>
    # For Pipeline B pages: insert right after <div id="root"></div>
    if '<div id="root"></div>' in content:
        content = content.replace(
            '<div id="root"></div>',
            '<div id="root"></div>' + FLOATING_NAV
        )
    elif '</body>' in content:
        content = content.replace('</body>', FLOATING_NAV + '</body>')

    path.write_text(content, encoding='utf-8')
    print(f"  OK   {filename}")

# Standardize existing home-nav on research/teaching
for filename in REPLACE_PAGES:
    path = PUBLIC / filename
    if not path.exists():
        continue

    content = path.read_text(encoding='utf-8', errors='replace')

    # Remove old home-nav div (it's raw HTML after the React app)
    # Pattern: <div class="home-nav" ... > ... </div>
    old_nav_pattern = r'<div\s+class="home-nav"[^>]*>.*?</div>\s*</div>'
    content = re.sub(old_nav_pattern, '', content, flags=re.DOTALL)

    # Also remove any existing style block for .home-nav
    content = re.sub(r'<style>\s*\.home-nav\s*\{[^}]*\}[^<]*</style>', '', content, flags=re.DOTALL)

    # Insert new standard nav before </body>
    if 'site-back-nav' not in content:
        content = content.replace('</body>', FLOATING_NAV + '</body>')

    path.write_text(content, encoding='utf-8')
    print(f"  OK   {filename} (replaced old home-nav)")

print("Done.")
```

- [ ] **Step 2: Run the script**

```bash
python fix-nav.py
```

- [ ] **Step 3: Verify by opening a page in browser**

Open `public/ise507-showcase.html` in a browser. Should see floating glass nav buttons at top-left: "← Home" + "Portfolio".

- [ ] **Step 4: Commit**

```bash
git add public/*.html fix-nav.py
git commit -m "feat: add uniform floating back-nav to all showcase pages"
```

---

## Task 4: Fix Font Consistency on Pipeline A Pages

**Fixes:** I-04, I-06, I-07, I-09, G-03, G-04, G-05
**Files:**
- Modify: `public/index.html`
- Modify: `public/portfolio.html`
- Modify: `public/research-showcase.html`
- Modify: `public/teaching-showcase.html`

These are the 4 readable source pages where we can directly edit inline styles.

- [ ] **Step 1: Fix research-showcase.html — remove useEffect font override, fix Playfair fallback, fix SectionTitle**

In `research-showcase.html`, find and modify:
1. The `useEffect` that injects `body { font-family: -apple-system...` → remove the font-family line (design-system.css handles it)
2. All instances of `'Playfair Display', serif` → `'Playfair Display', Georgia, serif`
3. SectionTitle letter-spacing from `-0.5px` → `-0.02em`

- [ ] **Step 2: Fix teaching-showcase.html — same pattern**

1. Remove `useEffect` body font-family injection
2. Fix Playfair fallback to include Georgia
3. Fix SectionTitle letter-spacing from `-0.5px` → `-0.02em`
4. Standardize `fadeInUp` translateY to `30px` (currently `20px`)
5. Standardize `slideInLeft` translateX to `40px` (currently `20px`)

- [ ] **Step 3: Fix index.html — harmonize SectionTitle to 2rem**

Change `SectionTitle` h2 `fontSize` from `'2.4rem'` to `'2rem'` to match other pages.

- [ ] **Step 4: Fix portfolio.html — harmonize container maxWidth**

Change chapter section `maxWidth` from `'1100px'` to `'1200px'`.

- [ ] **Step 5: Verify all 4 pages load correctly in browser**

Open each page, check:
- Fonts render as Inter (body) and Playfair Display (headings)
- No visual regressions
- Animations still work

- [ ] **Step 6: Commit**

```bash
git add public/index.html public/portfolio.html public/research-showcase.html public/teaching-showcase.html
git commit -m "fix: harmonize fonts, SectionTitle, spacing across Pipeline A pages"
```

---

## Task 5: Add Responsive Layout to index.html

**Fixes:** R-01 (for homepage), N-01 (hamburger menu)
**Files:**
- Modify: `public/index.html`

The homepage is the most important page to make responsive. It needs a working hamburger menu and stacked layouts for mobile.

- [ ] **Step 1: Add CSS class markers to key layout elements**

In index.html's React components, add className attributes so design-system.css responsive rules can target them:
- Nav links container: add `className: 'ds-nav-links'`
- Stats grid: add `className: 'ds-stats-grid'`
- Portfolio showcase grid: add `className: 'ds-grid-3'`
- Hero flex container: add `className: 'ds-hero-flex'`
- Hero photo: add `className: 'ds-hero-photo'`
- Hero buttons row: add `className: 'ds-hero-buttons'`

- [ ] **Step 2: Implement the hamburger button and mobile drawer**

Add a hamburger button component that:
- Renders only on mobile (hidden by `.ds-hamburger { display: none }` on desktop via design-system.css)
- Toggles `mobileOpen` state (already declared but unused)
- Opens a full-screen mobile nav drawer with glass backdrop

The hamburger button goes inside the nav bar. The mobile drawer is a sibling div.

- [ ] **Step 3: Add mobile-specific adjustments for section content**

Ensure each section's grid uses the `ds-grid-*` classes so they stack on mobile.

- [ ] **Step 4: Test at 375px viewport width (iPhone SE)**

Open index.html, use browser DevTools → toggle device toolbar → iPhone SE (375×667).
Verify:
- Hamburger icon visible, nav links hidden
- Tapping hamburger opens full-screen drawer
- Hero stacks photo above text
- Stats grid shows 2 columns
- All sections single-column
- No horizontal overflow

- [ ] **Step 5: Commit**

```bash
git add public/index.html
git commit -m "feat: add responsive layout and hamburger menu to homepage"
```

---

## Task 6: Add Responsive Layout to portfolio.html

**Fixes:** R-01 (for portfolio), N-02
**Files:**
- Modify: `public/portfolio.html`

Same pattern as Task 5 but for portfolio's chapter-based layout.

- [ ] **Step 1: Add CSS class markers and hamburger menu**

Same hamburger/drawer pattern as index.html. Chapter nav scrolls horizontally on mobile.

- [ ] **Step 2: Make showcase cards stack on mobile**

The showcase cards within chapters should stack in a single column at <640px.

- [ ] **Step 3: Test at 375px viewport**

- [ ] **Step 4: Commit**

```bash
git add public/portfolio.html
git commit -m "feat: add responsive layout and hamburger menu to portfolio"
```

---

## Task 7: Add Responsive Accommodations to Research + Teaching Showcases

**Fixes:** R-01 (for research/teaching), A-04, A-05
**Files:**
- Modify: `public/research-showcase.html`
- Modify: `public/teaching-showcase.html`

These pages use sticky tab navigation which already wraps on mobile. Main changes:
- Add scroll-reveal to content sections (they lack it, unlike index/portfolio)
- Add responsive padding and font size adjustments via CSS classes
- Ensure tab bar scrolls horizontally on mobile (already does via `overflowX: 'auto'`)

- [ ] **Step 1: Add scroll-reveal to research-showcase.html content sections**

Inject a small `<script>` after the React app that initializes IntersectionObserver on `.scroll-reveal` elements:

```html
<script>
(function() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('revealed'); observer.unobserve(e.target); } });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.scroll-reveal').forEach(el => observer.observe(el));
})();
</script>
```

Note: The scroll-reveal class needs to be added to elements by the React components inside the bundle. Since we can't modify the bundle, this script will only work on elements that we inject outside the bundle (like the floating nav). For full scroll-reveal on Pipeline A research/teaching pages, we modify their readable source directly.

- [ ] **Step 2: Add responsive CSS overrides for tab nav and content**

In design-system.css or a page-specific `<style>` block, ensure tabs wrap gracefully and content sections use responsive padding.

- [ ] **Step 3: Test at 375px viewport**

- [ ] **Step 4: Commit**

```bash
git add public/research-showcase.html public/teaching-showcase.html
git commit -m "feat: add responsive layout and scroll-reveal to research + teaching"
```

---

## Task 8: Add Responsive CSS for All Pipeline B Showcase Pages

**Fixes:** R-01 (for all 10 showcases)
**Files:**
- The `design-system.css` already loaded in all pages handles base responsive tokens.
- Add a `<style>` block in each Pipeline B page's `<head>` for page-specific responsive overrides if needed.

Since the Pipeline B React components use inline styles (not CSS classes), the responsive CSS needs `!important` overrides on common patterns.

- [ ] **Step 1: Add responsive override block to design-system.css**

Add rules targeting common inline-style patterns from Pipeline B bundles:

```css
/* Pipeline B responsive overrides */
@media (max-width: 639px) {
  /* Force grid layouts to stack */
  [style*="grid-template-columns"] {
    grid-template-columns: 1fr !important;
  }

  /* Reduce large paddings */
  [style*="padding: 3rem"],
  [style*="padding: 4rem"],
  [style*="padding: 80px"],
  [style*="padding: 100px"] {
    padding: 24px 16px !important;
  }

  /* Hero sections: reduce height */
  [style*="min-height: 100vh"] {
    min-height: auto !important;
    padding-top: 60px !important;
    padding-bottom: 40px !important;
  }

  /* Large headings: clamp down */
  [style*="font-size: 3rem"],
  [style*="font-size: 3.5rem"],
  [style*="font-size: 4rem"] {
    font-size: clamp(1.6rem, 6vw, 2.4rem) !important;
  }

  /* Flex layouts that need stacking */
  [style*="display: flex"][style*="gap: 3rem"],
  [style*="display: flex"][style*="gap: 4rem"] {
    flex-direction: column !important;
  }
}
```

- [ ] **Step 2: Verify a Pipeline B showcase on mobile viewport**

Open `public/thesis-showcase.html` at 375px width. Check:
- Content doesn't overflow horizontally
- Grids stack to single column
- Text is readable
- 3D viewer is usable (may need specific width capping)

- [ ] **Step 3: Commit**

```bash
git add public/design-system.css
git commit -m "feat: add responsive overrides for Pipeline B showcase pages"
```

---

## Task 9: Final Visual QA Pass

**Files:** All 14 pages
**Tool:** Browser DevTools + Playwright for screenshots

- [ ] **Step 1: Desktop QA — open each page at 1440px width**

Check each page for:
- Fonts: Inter body, Playfair headings
- Colors: accent is `#0071e3`, background is `#f5f5f7`
- Glass cards: translucent with blur
- Animations: fadeInUp on scroll, pulseGlow consistent
- Navigation: back-nav on all showcases, glass nav on index/portfolio

- [ ] **Step 2: Mobile QA — open each page at 375px width**

Check each page for:
- Hamburger menu works (index/portfolio)
- Content stacks properly
- No horizontal overflow
- Floating back-nav accessible
- Text readable without zoom

- [ ] **Step 3: Cross-page navigation test**

From mobile, navigate: index → portfolio → thesis-showcase → back to index. Verify all links work and transitions feel cohesive.

- [ ] **Step 4: Fix any issues found during QA**

Address any remaining visual issues discovered during QA.

- [ ] **Step 5: Final commit**

```bash
git add .
git commit -m "fix: visual QA corrections across all pages"
```

---

## Task 10: Merge to Main and Deploy

- [ ] **Step 1: Push dev branch**

```bash
git push origin dev
```

- [ ] **Step 2: Verify Cloudflare Pages preview deployment on dev branch (if configured)**

Cloudflare Pages auto-deploys preview URLs for non-production branches.

- [ ] **Step 3: Merge to main**

```bash
git checkout main
git merge dev
git push origin main
```

- [ ] **Step 4: Verify live deployment at aosawy.org**

Wait for Cloudflare Pages to deploy (~1 min), then check:
- Desktop: aosawy.org loads correctly
- Mobile: aosawy.org on phone or DevTools mobile view

- [ ] **Step 5: Final commit tag**

```bash
git tag v1.1-design-coherence
git push origin v1.1-design-coherence
```
