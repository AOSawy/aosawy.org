# aosawy.org — Professional Academic Website Design Spec

**Author:** Abdelrahman O. Sawy
**Date:** 2026-03-27
**Status:** Approved
**Domain:** aosawy.org
**Hosting:** Cloudflare Pages (free tier)
**Framework:** Astro

---

## 1. Purpose & Audience

A long-term professional academic website supporting the career trajectory: PhD student → candidate → distinguished professor/researcher in Industrial & Systems Engineering.

**Primary audiences (research-weighted):**

1. **Hiring/admissions committees** — publications, CV, research statement, institutional affiliation
2. **Research collaborators & conference peers** — active research, code repos, contact
3. **Students (current/prospective)** — teaching, course materials, mentorship
4. **Broad professional network** — competitions, entrepreneurship, full breadth

**Relationship to The Agentic Lab®:** Completely separate. aosawy.org is purely academic/professional. A single professional link to theagenticlab.net appears in the footer. No cross-content, no blog duplication.

---

## 2. Site Architecture

Hybrid Academic Architecture — research-weighted with curated highlights and a deep archive.

```
├── Home (hero + stats + featured work + news)
├── Research
│   ├── Interests & Groups
│   └── Publications
├── Portfolio
│   ├── Projects & Competitions (curated)
│   └── Industry Experience
├── Teaching
├── CV (rendered + download)
├── News & Updates
├── Archive
│   ├── AUC (2020–2024)
│   └── Rutgers (2024–present)
└── Contact
```

**Content strategy:** Curated highlights on main pages (what visitors see first). Full archive accessible for depth. Static portfolio pages form the backbone; lightweight News/Updates feed for announcements; occasional longer research write-ups when significant.

---

## 3. Page Designs

### 3.1 Homepage

Scrolling single-page layout combining three patterns:

| Section | Source Pattern | Content |
|---------|--------------|---------|
| Hero | Classic Academic + Scrolling Narrative | Name (Playfair serif), research mission, photo side-by-side, action buttons (CV, Scholar, GitHub, LinkedIn) |
| Stats Bar | Hero Statement | 4 glass cards: 4.0 GPA, Top 0.6% Kaggle, 2 TA Positions, 3 Degrees |
| Research Interests | Classic Academic | Pill/tag chips for focus areas |
| Featured Work | Scrolling Narrative | 2×2 glass card grid with category labels (Research, Competition, Thesis) |
| Latest News | Classic Academic | Timeline list with dates, "View all →" link |
| Footer | — | Copyright, professional link to The Agentic Lab®, email |

### 3.2 Research Page (`/research`)

- **Affiliations:** Research group cards (RIA Group, advisor info)
- **Interests:** Narrative paragraph describing research focus
- **Publications:** List entries with title, authors, venue, year, and action pills (PDF, Code, BibTeX). Placeholder message until first publication. Sourced from `publications.yaml`
- **Active Research Projects:** Glass cards with status badges (Active/Completed). Sourced from `projects/` collection

### 3.3 Portfolio Page (`/portfolio`)

- **Filter tabs:** All / Competitions / Engineering / Industry (pill-shaped toggles)
- **Project cards:** Image + category tag + title + description. Grid layout. Each card links to a detail page. Images from `assets/images/projects/` (SolidWorks renders, competition screenshots, etc.)
- **Industry Experience:** Timeline list below projects (B.Tech, MTI Automotive)
- Sourced from `projects/` collection and `experience.yaml`

### 3.4 Teaching Page (`/teaching`)

- **Current courses:** Highlighted with "Current" badge, topic list, course details
- **Past courses:** Listed below without badge
- Sourced from `courses.yaml` with `current: true/false` flag

### 3.5 CV Page (`/cv`)

- Rendered HTML version of CV on the page
- Prominent "Download PDF" button
- Links to relevant sections of the site (Research, Teaching, etc.)

### 3.6 News & Updates Page (`/news`)

- Reverse-chronological list of all news entries
- Each entry: date, title, short description, optional "Read more" for longer posts
- Sourced from `news/` Markdown collection

### 3.7 Archive Page (`/archive`)

- **Institution filter:** All / AUC (2020–2024) / Rutgers (2024–present)
- **Category filter:** Coursework / Projects / Leadership / Activities
- **Expandable course lists** organized by institution and semester
- Each course entry: code, title, description/tags, year
- Sourced from `auc-courses.yaml` and `rutgers-courses.yaml`

### 3.8 Contact Page (`/contact`)

- Email, institutional address, office hours (when applicable)
- Links: Google Scholar, GitHub, LinkedIn
- Simple, clean — no contact form needed initially

---

## 4. Visual Design System

**Design philosophy:** Light Academic foundation with heavy Apple website and iOS 26 Liquid Glass influence.

### 4.1 Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--bg` | `#f5f5f7` | Page background (Apple's signature gray) |
| `--surface` | `#ffffff` | Card backgrounds |
| `--glass` | `rgba(255,255,255,0.65)` | Translucent glass surfaces |
| `--glass-blur` | `saturate(180%) blur(20px)` | Frosted glass backdrop filter |
| `--text-primary` | `#1d1d1f` | Headings, primary text |
| `--text-secondary` | `#6e6e73` | Body text |
| `--text-tertiary` | `#86868b` | Labels, dates, meta text |
| `--accent` | `#0071e3` | Links, buttons, pills (Apple's link blue) |
| `--accent-light` | `rgba(0,113,227,0.06)` | Pill backgrounds, hover states |
| `--border` | `rgba(0,0,0,0.06)` | Hairline borders (0.5px) |
| `--shadow` | `0 1px 4px rgba(0,0,0,0.03)` | Subtle card shadows |

### 4.2 Typography

| Element | Font | Weight | Size |
|---------|------|--------|------|
| Name / Page titles | Playfair Display (serif) | 600 | 2.2em / 1.8em |
| Section headings | Playfair Display | 600 | 1.3em |
| Card titles | Inter | 600 | 0.95em |
| Body text | Inter | 400 | 1em |
| Labels / Meta | Inter | 500 | 0.65–0.7em, uppercase, letter-spacing: 2.5px |
| Buttons | Inter | 500 | 0.82em |
| Fallback stack | -apple-system, BlinkMacSystemFont, sans-serif | — | — |

### 4.3 Components

**Glass Nav:**
- Sticky top, `backdrop-filter: saturate(180%) blur(20px)`
- `rgba(255,255,255,0.72)` background
- Hairline bottom border
- Logo (Playfair) left, nav links (Inter) right

**Glass Cards:**
- `rgba(255,255,255,0.65)` background with `backdrop-filter: saturate(120%) blur(12px)`
- `border-radius: 14px`, 0.5px border
- Subtle shadow, hover: `translateY(-2px)` + deeper shadow

**Pill Buttons:**
- Primary: `#0071e3` bg, white text, `border-radius: 980px`
- Secondary: transparent, `#0071e3` text, no border

**Interest/Tag Pills:**
- `rgba(0,113,227,0.06)` bg, `#0071e3` text, `border-radius: 980px`
- 0.5px accent-tinted border

**Stat Cards:**
- Glass surface, centered number (1.6em bold) + uppercase label below

**Status Badges:**
- Active: green-tinted pill
- Current: green-tinted pill
- Category tags: muted uppercase text

### 4.4 Interactions

- Card hover: `translateY(-2px)` + shadow deepen, 0.2s ease
- Scroll-triggered fade-in animations (Intersection Observer)
- Filter tabs: instant content filtering (client-side JS island)
- Smooth scrolling for anchor links
- Mobile: responsive breakpoints, stacked layouts, hamburger nav

---

## 5. Data Model & Content Structure

Astro Content Collections with typed schemas. Hybrid maintenance model: code structure with data-driven content (YAML/JSON/Markdown).

```
src/
├── content/
│   ├── config.ts              ← Astro content collection schemas (Zod)
│   ├── publications/
│   │   └── publications.yaml  ← All publications in one file
│   ├── projects/              ← One .md per project (frontmatter + write-up)
│   │   ├── posydon.md
│   │   ├── kaggle-loan-default.md
│   │   ├── energy-turnstile.md
│   │   └── solidworks-designs.md
│   ├── teaching/
│   │   └── courses.yaml       ← All courses, current flag
│   ├── news/                  ← One .md per news/update entry
│   │   ├── 2026-03-ta-computational-methods.md
│   │   └── 2025-kaggle-top-06.md
│   ├── experience/
│   │   └── experience.yaml    ← Internships, industry roles
│   └── archive/
│       ├── auc-courses.yaml   ← 40+ AUC courses
│       └── rutgers-courses.yaml
├── assets/
│   ├── images/
│   │   ├── profile/           ← Headshot
│   │   ├── projects/          ← SolidWorks renders, screenshots
│   │   └── archive/           ← Course project images
│   └── papers/                ← Publication PDFs
└── data/
    └── site.yaml              ← Global: name, bio, links, stats
```

### 5.1 Schema Examples

**publications.yaml:**
```yaml
- title: "Paper Title"
  authors: ["A.O. Sawy", "A.A. Ezzat"]
  venue: "Conference/Journal Name"
  year: 2026
  type: "conference"  # conference | journal | preprint | thesis
  links:
    pdf: "/papers/paper-title.pdf"
    code: "https://github.com/AOSawy/repo"
    bibtex: |
      @inproceedings{sawy2026..., ...}
  featured: true
  abstract: "Brief abstract text..."
```

**Project frontmatter (e.g., posydon.md):**
```yaml
---
title: "POSYDON Framework"
category: "research"  # research | competition | engineering | thesis
year: 2025
image: "../assets/images/projects/posydon-cover.png"
tags: ["optimization", "offshore wind", "simulation"]
featured: true
links:
  github: "https://github.com/..."
status: "active"  # active | completed
---
Project write-up in Markdown...
```

**courses.yaml:**
```yaml
- code: "16-540-540"
  title: "Computational Methods in Industrial Engineering"
  institution: "Rutgers University"
  level: "graduate"
  semester: "Spring 2026"
  role: "Graduate Teaching Assistant"
  current: true
  topics: ["PCA", "regression", "MCMC", "graph mining"]
```

**site.yaml:**
```yaml
name: "Abdelrahman O. Sawy"
shortName: "A.O. Sawy"
title: "PhD Student"
department: "Industrial & Systems Engineering"
university: "Rutgers University"
email: "a.sawy@rutgers.edu"
bio: "Developing mathematical optimization and machine learning methods..."
photo: "/images/profile/headshot.jpg"
links:
  scholar: "https://scholar.google.com/..."
  github: "https://github.com/AOSawy"
  linkedin: "https://linkedin.com/in/..."
  agenticlab: "https://theagenticlab.net"
stats:
  - value: "4.0"
    label: "GPA · MS in ISE"
  - value: "Top 0.6%"
    label: "Kaggle · 3,724 teams"
  - value: "2"
    label: "TA Positions"
  - value: "3"
    label: "Degrees"
```

---

## 6. Technical Architecture

### 6.1 Stack

| Layer | Technology |
|-------|-----------|
| Framework | Astro (latest stable) |
| Styling | Tailwind CSS |
| Fonts | Google Fonts: Inter + Playfair Display |
| Content | Astro Content Collections (Zod schemas) |
| Interactivity | Astro Islands — vanilla JS for filters, no React/Vue needed |
| Build | Static output (SSG) |
| Hosting | Cloudflare Pages |
| Repo | GitHub (public or private) |
| Domain | aosawy.org (Cloudflare DNS) |
| CI/CD | Cloudflare Pages auto-deploy on push to `main` |

### 6.2 Project Structure

```
aosawy.org/
├── astro.config.mjs
├── tailwind.config.mjs
├── package.json
├── tsconfig.json
├── public/
│   ├── favicon.ico
│   ├── robots.txt
│   └── papers/              ← Publication PDFs (static)
├── src/
│   ├── content/             ← (see Section 5)
│   ├── data/
│   │   └── site.yaml
│   ├── assets/
│   │   └── images/
│   ├── layouts/
│   │   └── BaseLayout.astro ← Glass nav, footer, meta tags, fonts
│   ├── components/
│   │   ├── GlassNav.astro
│   │   ├── Footer.astro
│   │   ├── HeroSection.astro
│   │   ├── StatsBar.astro
│   │   ├── GlassCard.astro
│   │   ├── PillTag.astro
│   │   ├── NewsTimeline.astro
│   │   ├── FilterTabs.astro   ← JS island for client-side filtering
│   │   ├── ProjectGrid.astro
│   │   └── PublicationEntry.astro
│   └── pages/
│       ├── index.astro        ← Homepage
│       ├── research.astro
│       ├── portfolio.astro
│       ├── portfolio/[slug].astro  ← Project detail pages
│       ├── teaching.astro
│       ├── cv.astro
│       ├── news.astro
│       ├── news/[slug].astro  ← Individual news posts
│       ├── archive.astro
│       └── contact.astro
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-03-27-aosawy-org-design.md
```

### 6.3 Performance Targets

- Lighthouse: 95+ across all categories
- Zero client-side JS by default (Astro ships none)
- JS islands only for: filter tabs on Portfolio/Archive pages
- Image optimization via Astro's built-in `<Image>` component
- Font display: swap (no FOIT)

### 6.4 SEO & Meta

- Open Graph tags on all pages (title, description, image)
- Structured data: Person schema (Google Knowledge Panel eligibility)
- Sitemap auto-generated by Astro
- Canonical URLs
- `robots.txt` allowing all crawlers

### 6.5 Responsive Breakpoints

- Mobile: < 640px — stacked layout, hamburger nav, single-column cards
- Tablet: 640–1024px — 2-column grids, condensed nav
- Desktop: > 1024px — full layout as designed

---

## 7. Content Sources

Initial content populated from these local directories:

| Source | Maps To |
|--------|---------|
| `C:\Users\aosaw\OneDrive - aucegypt.edu\AUC MENG BS\` | Archive → AUC courses, Portfolio → engineering projects |
| `C:\Users\aosaw\OneDrive - aucegypt.edu\AUC THESIS\` | Portfolio → Energy-Generating Turnstile project |
| `C:\Users\aosaw\OneDrive - Rutgers University\Rutgers ISE PhD\` | Research, Teaching, Archive → Rutgers, News entries |
| `C:\Users\aosaw\...\RESUME - CV\Claude LaTeX\Abdelrahman_O_Sawy_Resume.pdf` | CV page, site.yaml global data |

---

## 8. Update Workflow

| Action | Steps |
|--------|-------|
| Add publication | Append entry to `publications.yaml` → push → auto-deploy |
| Add project | Create `projects/new-project.md` + add images → push |
| Post news | Create `news/YYYY-MM-title.md` → push |
| Update teaching | Edit `courses.yaml`, toggle `current` flag → push |
| Update CV | Replace PDF in `public/papers/`, update `cv.astro` if needed → push |
| Update stats | Edit `site.yaml` → push |
| Add archive content | Append to `auc-courses.yaml` or `rutgers-courses.yaml` → push |

---

## 9. Scope Boundaries

**In scope:**
- All pages listed in Section 3
- Visual design system (Section 4)
- Data model and content collections (Section 5)
- Initial content population from OneDrive folders
- Cloudflare Pages deployment
- Custom domain setup (aosawy.org)
- Responsive design (mobile, tablet, desktop)

**Out of scope (for now):**
- Blog CMS or admin panel
- Contact form backend
- Analytics dashboard (can add Cloudflare Web Analytics later — free, privacy-respecting)
- Dark mode toggle (light-only for v1; can add later)
- Search functionality
- RSS feed
- Multi-language support
