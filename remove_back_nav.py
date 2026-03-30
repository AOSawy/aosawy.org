"""Remove <div class="site-back-nav" id="siteBackNav">...</div> from all showcase HTML files.

The persistent site header now handles navigation, so these floating back-nav
buttons are redundant. The CSS rules have already been hidden via display:none,
but this script removes the HTML entirely for a clean codebase.
"""

import re
from pathlib import Path


PUBLIC = Path(__file__).parent / "public"

# Pattern matches the full back-nav block:
#   <!-- Site Back-Navigation -->
#   <div class="site-back-nav" id="siteBackNav">
#     <a href="index.html">&larr; Home</a>
#     <a href="portfolio.html">Portfolio</a>
#   </div>
PATTERN = re.compile(
    r'<!-- Site Back-Navigation -->\s*'
    r'<div class="site-back-nav" id="siteBackNav">.*?</div>\s*',
    re.DOTALL,
)


def main() -> None:
    html_files = sorted(PUBLIC.glob("*-showcase.html")) + [PUBLIC / "portfolio.html"]
    removed = 0
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        new_text, n = PATTERN.subn("", text)
        if n:
            path.write_text(new_text, encoding="utf-8")
            print(f"  Removed site-back-nav from {path.name}")
            removed += 1
    if removed:
        print(f"\nDone — removed back-nav from {removed} files.")
    else:
        print("No site-back-nav blocks found.")


if __name__ == "__main__":
    main()
