# Research Showcase Mobile Optimization Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the research showcase page's broken mobile hero, optimize all sections for mobile viewport (440×956), and add the dark branded footer from the homepage.

**Architecture:** CSS-first approach — add targeted mobile rules in `design-system.css` for the hero section's absolute-positioned elements, converting them to normal flow on mobile. Replace the inline text footer with the `ds-site-footer` component (CSS already exists in design-system.css). Minor HTML changes to research-showcase.html for hero structure and footer replacement.

**Tech Stack:** React 18 UMD (vanilla `React.createElement`), CSS media queries, shared `design-system.css`

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `public/design-system.css` | Modify | Add mobile CSS rules for research hero section |
| `public/research-showcase.html` | Modify | Fix hero structure, replace footer, minor mobile adjustments |

---

### Task 1: Fix Hero Section Mobile Layout

The hero section (lines 11595-11882) uses `height: 100vh` with all content absolutely positioned for desktop. On mobile (≤639px), the video doesn't autoplay, the poster renders but content floats off-screen. Fix by converting to normal flow on mobile.

**Files:**
- Modify: `public/design-system.css` (mobile breakpoint section, after line ~710)
- Modify: `public/research-showcase.html` (lines 11595-11882, hero section — add IDs/classes for CSS targeting)

- [ ] **Step 1: Add CSS class hooks to the hero section in research-showcase.html**

Add `id="research-hero"` to the hero `<section>` element and class names to the stat chips container and content card for CSS targeting.

At line 11595, change:
```js
), /*#__PURE__*/React.createElement("section", {
    style: {
      position: 'relative',
      height: '100vh',
      overflow: 'hidden',
      fontFamily: "'Inter', -apple-system, sans-serif"
    }
```
To:
```js
), /*#__PURE__*/React.createElement("section", {
    id: 'research-hero',
    style: {
      position: 'relative',
      height: '100vh',
      overflow: 'hidden',
      fontFamily: "'Inter', -apple-system, sans-serif"
    }
```

At line 11642 (stat chips container), add className:
```js
  }), /*#__PURE__*/React.createElement("div", {
    className: 'research-hero-stats',
    style: {
      position: 'absolute',
      top: '5%',
      right: '5%',
```

At line 11688 (content card container), add className:
```js
  })))), /*#__PURE__*/React.createElement("div", {
    className: 'research-hero-content',
    style: {
      position: 'absolute',
      bottom: '12%',
      left: '5%',
```

- [ ] **Step 2: Add mobile CSS rules for research hero in design-system.css**

Add these rules inside the existing `@media (max-width: 639px)` block in design-system.css, after the `#hero` rule (around line 710):

```css
  /* -- Research showcase hero: stack on mobile -- */
  #research-hero {
    height: auto !important;
    min-height: 100vh;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-end !important;
    padding: 80px 20px 24px !important;
    overflow: visible !important;
  }

  #research-hero video,
  #research-hero > div:first-child,
  #research-hero > div:nth-child(2) {
    position: absolute !important;
    inset: 0 !important;
    width: 100% !important;
    height: 100% !important;
  }

  .research-hero-stats {
    position: static !important;
    order: 1;
    display: flex !important;
    justify-content: center !important;
    gap: 8px !important;
    margin-bottom: 16px;
    z-index: 5;
  }

  .research-hero-stats > div {
    padding: 8px 12px !important;
    flex: 1;
    max-width: 110px;
  }

  .research-hero-stats > div > div:first-child {
    font-size: 1rem !important;
  }

  .research-hero-stats > div > div:last-child {
    font-size: 0.55rem !important;
  }

  .research-hero-content {
    position: static !important;
    order: 2;
    z-index: 5;
    max-width: 100% !important;
    text-align: center !important;
  }

  .research-hero-content > div:first-child {
    padding: 1.25rem !important;
    border-radius: 16px !important;
  }

  /* Center logo links row on mobile */
  .research-hero-content > div:first-child > div:first-child {
    justify-content: center !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    margin-bottom: 1rem !important;
  }

  .research-hero-content h1 {
    font-size: 1.5rem !important;
    text-align: center !important;
  }

  .research-hero-content p {
    text-align: center !important;
    font-size: 0.85rem !important;
  }

  /* Author/metadata row: center and wrap */
  .research-hero-content > div:first-child > div:nth-child(4) {
    justify-content: center !important;
  }

  /* Institution line */
  .research-hero-content > div:first-child > div:last-child {
    text-align: center !important;
  }

  /* Scroll indicator in research hero */
  #research-hero .ds-scroll-indicator {
    position: static !important;
    order: 3;
    margin: 16px auto 0 !important;
    bottom: auto !important;
    left: auto !important;
    transform: none !important;
    width: fit-content !important;
  }
```

- [ ] **Step 3: Start local server and verify hero mobile rendering**

Run: `cd public && python -m http.server 3000`
Open Playwright at 440×956, navigate to `http://localhost:3000/research-showcase.html`
Force scroll-reveal visibility, then screenshot the hero.

Expected: Hero stacks vertically — video background visible, stat chips centered at top, content card centered below, scroll indicator at bottom. All text readable.

- [ ] **Step 4: Verify desktop hero is unchanged**

Resize Playwright to 1440×900, reload page.
Expected: Hero still renders with absolute positioning (media query only applies ≤639px). Video background, stat chips top-right, content card bottom-left.

---

### Task 2: Replace Footer with Dark Branded Footer

Replace the simple 3-line text footer (lines 11912-11941) with the `ds-site-footer` component matching the homepage. The CSS classes (`ds-site-footer`, `ds-footer-inner`, `ds-footer-heading`, `ds-footer-links`, `ds-footer-bar`) are already defined in design-system.css with responsive rules.

**Files:**
- Modify: `public/research-showcase.html` (lines 11912-11941)

- [ ] **Step 1: Replace the footer element**

Find the existing footer (line 11912):
```js
}, tabContent[activeTab]), /*#__PURE__*/React.createElement("footer", {
    style: {
      marginTop: '4rem',
      paddingTop: '2rem',
      borderTop: `0.5px solid ${color.border}`,
      textAlign: 'center',
      color: color.secondary,
      fontSize: '0.875rem',
      maxWidth: '1200px',
      margin: '4rem auto 0',
      paddingLeft: '1.5rem',
      paddingRight: '1.5rem'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      marginBottom: '0.5rem'
    }
  }, /*#__PURE__*/React.createElement("strong", null, "Abdelrahman Sawy"), " \xB7 Rutgers University \xB7 Industrial & Systems Engineering"), /*#__PURE__*/React.createElement("p", {
    style: {
      marginBottom: '0.5rem'
    }
  }, "Under supervision of ", /*#__PURE__*/React.createElement("strong", null, "Dr. Ahmed Aziz Ezzat"), " \xB7 ", /*#__PURE__*/React.createElement("a", {
    href: PROJECT_META.researchGroupUrl,
    target: "_blank",
    rel: "noopener noreferrer",
    style: {
      color: color.accent,
      textDecoration: 'none'
    }
  }, "RIA Group")), /*#__PURE__*/React.createElement("p", null, "Spring 2025 \u2013 Present \xB7 Offshore Wind Farm Operations Research")));
```

Replace the entire `React.createElement("footer", ...)` block with the dark branded footer using `ds-site-footer` CSS classes. Note: this page uses `React.createElement` (not `_react.default.createElement` like the homepage).

New footer code:
```js
}, tabContent[activeTab]),
/*#__PURE__*/React.createElement("footer", {
  className: 'ds-site-footer'
},
  React.createElement("div", { className: 'ds-footer-inner' },
    // Column 1 — About
    React.createElement("div", null,
      React.createElement("div", {
        className: 'ds-footer-heading',
        style: { fontFamily: "'Playfair Display', Georgia, serif" }
      }, "A. Sawy"),
      React.createElement("p", { className: 'ds-footer-text' },
        "PhD Student, Industrial & Systems Engineering"),
      React.createElement("p", { className: 'ds-footer-text' },
        "Rutgers University, New Brunswick, NJ")
    ),
    // Column 2 — Quick Links
    React.createElement("div", null,
      React.createElement("div", { className: 'ds-footer-heading' }, "Quick Links"),
      React.createElement("ul", { className: 'ds-footer-links' },
        React.createElement("li", null,
          React.createElement("a", { href: "index.html" }, "Home")),
        React.createElement("li", null,
          React.createElement("a", { href: "research-showcase.html" }, "Research")),
        React.createElement("li", null,
          React.createElement("a", { href: "portfolio.html" }, "Portfolio")),
        React.createElement("li", null,
          React.createElement("a", { href: "teaching-showcase.html" }, "Teaching"))
      )
    ),
    // Column 3 — Connect
    React.createElement("div", null,
      React.createElement("div", { className: 'ds-footer-heading' }, "Connect"),
      React.createElement("ul", { className: 'ds-footer-links' },
        React.createElement("li", null,
          React.createElement("a", { href: "mailto:a.sawy@rutgers.edu" },
            React.createElement("svg", { width: 14, height: 14, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: 2, style: { verticalAlign: "middle", marginRight: "6px" } },
              React.createElement("rect", { x: 2, y: 4, width: 20, height: 16, rx: 2 }),
              React.createElement("path", { d: "M22 4L12 13 2 4" })
            ), "a.sawy@rutgers.edu")),
        React.createElement("li", null,
          React.createElement("a", { href: "https://www.linkedin.com/in/aosawy/", target: "_blank", rel: "noopener noreferrer" },
            React.createElement("svg", { width: 14, height: 14, viewBox: "0 0 24 24", fill: "currentColor", style: { verticalAlign: "middle", marginRight: "6px" } },
              React.createElement("path", { d: "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" })
            ), "LinkedIn")),
        React.createElement("li", null,
          React.createElement("a", { href: "https://github.com/aosawy", target: "_blank", rel: "noopener noreferrer" },
            React.createElement("svg", { width: 14, height: 14, viewBox: "0 0 24 24", fill: "currentColor", style: { verticalAlign: "middle", marginRight: "6px" } },
              React.createElement("path", { d: "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12" })
            ), "GitHub")),
        React.createElement("li", null,
          React.createElement("a", { href: "https://wa.me/18482097088", target: "_blank", rel: "noopener noreferrer",
            style: { display: "inline-flex", alignItems: "center", gap: "8px" } },
            React.createElement("svg", { width: 16, height: 16, viewBox: "0 0 24 24", fill: "currentColor", style: { opacity: 0.7 } },
              React.createElement("path", { d: "M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" })
            ), "(848) 209-7088"))
      )
    )
  ),
  // Bottom bar
  React.createElement("div", { className: 'ds-footer-bar' },
    React.createElement("span", null, "\u00A9 2026 Abdelrahman O. Sawy. Built with purpose."),
    React.createElement("span", null, "Founder, ",
      React.createElement("a", { href: "mailto:sales@theagenticlab.net", target: "_blank", rel: "noopener noreferrer" }, "The Agentic Lab\u00AE"))
  )
));
```

- [ ] **Step 2: Verify footer renders on mobile and desktop**

Reload both viewports. Expected: Dark footer with 3 columns on desktop, stacked single column on mobile, matching the homepage exactly.

---

### Task 3: Mobile Polish & Verification

Final pass on tab navigation, spacing, and comprehensive mobile testing.

**Files:**
- Modify: `public/design-system.css` (if needed for tab nav polish)

- [ ] **Step 1: Verify tab navigation doesn't overflow**

Check the existing CSS at lines 21-34 of research-showcase.html for sticky nav mobile handling. Verify in Playwright that horizontal scroll works cleanly.

- [ ] **Step 2: Full mobile scroll-through verification**

Playwright at 440×956: Force scroll-reveal visibility, then screenshot at each major section:
1. Hero (top of page)
2. Overview tab content (RIA logo, title, info cards)
3. Research at a Glance stats
4. Research Mission text
5. Wind Farm Configuration cards
6. Footer

Compare against the user's reference screenshots to ensure quality matches or exceeds.

- [ ] **Step 3: Desktop regression check**

Playwright at 1440×900: Verify hero, tab content, and footer all render correctly. Take screenshot of hero and footer for comparison.

- [ ] **Step 4: Iterate on CSS if needed**

Based on visual inspection, adjust spacing, font sizes, or layout rules. Common adjustments:
- Stat card padding/font size
- Content card border-radius
- Author metadata wrapping
- Logo link sizes

- [ ] **Step 5: Commit all changes**

```bash
git add public/design-system.css public/research-showcase.html
git commit -m "fix: research showcase mobile optimization + dark footer

- Fix hero section layout on mobile (convert absolute to flow)
- Add branded ds-site-footer matching homepage
- Add CSS class hooks for mobile targeting
- Responsive stat chips, content card, scroll indicator"
```
