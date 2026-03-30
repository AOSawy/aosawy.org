"""
patch_html.py — Tasks 2 & 3 in one pass
- Fix <title> tags
- Add design-system.css link after viewport meta
- Remove old home-nav (research/teaching only)
- Inject standardized site-back-nav before </body> (all except index/portfolio)
"""

import re
from pathlib import Path

PUBLIC = Path("C:/Users/aosaw/Claude/AOSAWY.ORG Website Project/public")

TITLES = {
    "index.html":                   "Abdelrahman O. Sawy — PhD Student, ISE, Rutgers University",
    "portfolio.html":               "Portfolio — Abdelrahman O. Sawy",
    "research-showcase.html":       "Research — Abdelrahman O. Sawy",
    "teaching-showcase.html":       "Teaching — Abdelrahman O. Sawy",
    "thesis-showcase.html":         "BSc Thesis: Energy-Generating Turnstile — A.O. Sawy",
    "design-ii-showcase.html":      "Mechanical Design II — A.O. Sawy",
    "fem-showcase.html":            "Finite Element Methods — A.O. Sawy",
    "naca0024-cfd-showcase.html":   "CFD: NACA 0024 Airfoil — A.O. Sawy",
    "failure-analysis-showcase.html": "Failure Analysis — A.O. Sawy",
    "system-dynamics-showcase.html": "System Dynamics — A.O. Sawy",
    "am-showcase.html":             "Additive Manufacturing — A.O. Sawy",
    "ise507-showcase.html":         "ISE 507: Data Analytics — A.O. Sawy",
    "ise530-showcase.html":         "ISE 530: Forecasting Analytics — A.O. Sawy",
    "ise694-showcase.html":         "ISE 694: Data Mining — A.O. Sawy",
}

CSS_LINK = '<link rel="stylesheet" href="design-system.css">'

BACK_NAV = """<!-- Site Back-Navigation -->
<div class="site-back-nav" id="siteBackNav">
  <a href="index.html">&larr; Home</a>
  <a href="portfolio.html">Portfolio</a>
</div>"""

# Pages that get no back-nav injection
SKIP_BACKNAV = {"index.html", "portfolio.html"}

# Pages that need old home-nav removed
REMOVE_OLD_NAV = {"research-showcase.html", "teaching-showcase.html"}


def fix_title(html: str, new_title: str) -> str:
    return re.sub(r"<title>[^<]*</title>", f"<title>{new_title}</title>", html, count=1)


def add_css_link(html: str) -> str:
    if CSS_LINK in html:
        return html  # already present
    # Insert after the viewport meta tag line
    viewport_pattern = r'(<meta\s+name=["\']viewport["\'][^>]*>)'
    replacement = r'\1\n    ' + CSS_LINK
    result, n = re.subn(viewport_pattern, replacement, html, count=1, flags=re.IGNORECASE)
    if n == 0:
        # Fallback: insert before </head>
        result = html.replace("</head>", f"    {CSS_LINK}\n</head>", 1)
    return result


def remove_old_home_nav(html: str) -> str:
    """
    Remove the old inline-styled floating nav (id="home-nav") and its preceding comment.
    These appear as inline-styled fixed divs injected after the React root.
    Pattern: <!-- Floating Home Navigation -->\n  <div id="home-nav" ...>...</div>
    """
    # Remove comment + div#home-nav block
    html = re.sub(
        r'<!--\s*Floating Home Navigation\s*-->\s*<div\s+id=["\']home-nav["\'][^>]*>.*?</div>',
        '',
        html,
        flags=re.DOTALL
    )
    # Also handle class="home-nav" variant (fallback)
    html = re.sub(
        r'<!--\s*Floating Home Navigation\s*-->\s*<div\s+class=["\']home-nav["\'][^>]*>.*?</div>',
        '',
        html,
        flags=re.DOTALL
    )
    # Remove any orphaned style blocks for .home-nav
    html = re.sub(
        r'<style[^>]*>\s*\.home-nav\s*\{[^}]*\}[^<]*</style>\s*',
        '',
        html,
        flags=re.DOTALL
    )
    return html


def inject_back_nav(html: str) -> str:
    if 'id="siteBackNav"' in html:
        return html  # already present
    return html.replace("</body>", f"{BACK_NAV}\n</body>", 1)


def patch_file(filename: str) -> dict:
    path = PUBLIC / filename
    html = path.read_text(encoding="utf-8", errors="replace")
    original_len = len(html)

    # 1. Fix title
    html = fix_title(html, TITLES[filename])

    # 2. Add CSS link
    html = add_css_link(html)

    # 3. Remove old home-nav (research/teaching only)
    if filename in REMOVE_OLD_NAV:
        html = remove_old_home_nav(html)

    # 4. Inject back-nav before </body>
    if filename not in SKIP_BACKNAV:
        html = inject_back_nav(html)

    path.write_text(html, encoding="utf-8", errors="replace")

    return {
        "file": filename,
        "size_before": original_len,
        "size_after": len(html),
    }


if __name__ == "__main__":
    results = []
    for filename in TITLES:
        result = patch_file(filename)
        results.append(result)
        print(f"  [OK] {result['file']}  ({result['size_before']} -> {result['size_after']} chars)")

    print(f"\nDone. Patched {len(results)} files.")
