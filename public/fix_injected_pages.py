"""
Bulk fix for the 12 injected-header pages (Pipeline B + research/teaching showcases).

Fix 2: Add profile picture to header logo
Fix 3: Add scroll-lock (body.drawer-open) and backdrop dismiss to drawer
"""

import os
import re

PUBLIC = os.path.dirname(os.path.abspath(__file__))

# All 12 pages with the injected HTML header/drawer
PAGES = [
    "research-showcase.html",
    "teaching-showcase.html",
    "thesis-showcase.html",
    "system-dynamics-showcase.html",
    "naca0024-cfd-showcase.html",
    "ise694-showcase.html",
    "ise530-showcase.html",
    "ise507-showcase.html",
    "fem-showcase.html",
    "failure-analysis-showcase.html",
    "design-ii-showcase.html",
    "am-showcase.html",
]


def fix_page(filepath: str) -> list[str]:
    """Apply Fix 2 and Fix 3 to a single injected page. Returns list of changes made."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    changes: list[str] = []
    original = content

    # =========================================================================
    # FIX 2: Add profile picture to header logo
    # =========================================================================
    old_logo = '<a href="index.html" class="ds-header-logo">A. Sawy</a>'
    new_logo = (
        '<a href="index.html" class="ds-header-logo">'
        '<img src="assets/Home/ProfilePicCircle.jpg" alt="" class="ds-header-avatar">'
        'A. Sawy</a>'
    )

    if old_logo in content:
        content = content.replace(old_logo, new_logo)
        changes.append("Added profile picture to header logo")

    # =========================================================================
    # FIX 3a: Hamburger button — add drawer-open toggle
    # =========================================================================
    old_hamburger = (
        "document.getElementById('siteMobileDrawer').classList.toggle('open'); "
        "this.classList.toggle('open');"
    )
    new_hamburger = (
        "document.getElementById('siteMobileDrawer').classList.toggle('open'); "
        "this.classList.toggle('open'); "
        "document.body.classList.toggle('drawer-open');"
    )

    if old_hamburger in content and new_hamburger not in content:
        content = content.replace(old_hamburger, new_hamburger)
        changes.append("Added drawer-open toggle to hamburger button")

    # =========================================================================
    # FIX 3b: Close button — add drawer-open removal
    # =========================================================================
    old_close = (
        "document.getElementById('siteMobileDrawer').classList.remove('open'); "
        "document.querySelector('.ds-hamburger').classList.remove('open');"
    )
    new_close = (
        "document.getElementById('siteMobileDrawer').classList.remove('open'); "
        "document.querySelector('.ds-hamburger').classList.remove('open'); "
        "document.body.classList.remove('drawer-open');"
    )

    if old_close in content and new_close not in content:
        content = content.replace(old_close, new_close)
        changes.append("Added drawer-open removal to close button")

    # =========================================================================
    # FIX 3c: Each drawer link — add drawer-open removal
    # =========================================================================
    # Pattern: onclick="document.getElementById('siteMobileDrawer').classList.remove('open');"
    # on the <a> tags inside the drawer
    old_link_onclick = (
        """onclick="document.getElementById('siteMobileDrawer').classList.remove('open');\""""
    )
    new_link_onclick = (
        """onclick="document.getElementById('siteMobileDrawer').classList.remove('open'); """
        """document.querySelector('.ds-hamburger').classList.remove('open'); """
        """document.body.classList.remove('drawer-open');\""""
    )

    if old_link_onclick in content:
        count = content.count(old_link_onclick)
        content = content.replace(old_link_onclick, new_link_onclick)
        changes.append(f"Added drawer-open removal to {count} drawer link(s)")

    # =========================================================================
    # FIX 3d: Drawer div — add backdrop dismiss onclick
    # =========================================================================
    old_drawer_div = '<div class="ds-mobile-drawer" id="siteMobileDrawer">'
    new_drawer_div = (
        '<div class="ds-mobile-drawer" id="siteMobileDrawer" '
        """onclick="if(event.target===this){"""
        """document.getElementById('siteMobileDrawer').classList.remove('open');"""
        """document.querySelector('.ds-hamburger').classList.remove('open');"""
        """document.body.classList.remove('drawer-open');"""
        """}">\n"""
    )

    # Only apply if not already patched (check for onclick on that div)
    if old_drawer_div in content and 'onclick="if(event.target===this)' not in content:
        content = content.replace(old_drawer_div, new_drawer_div)
        changes.append("Added backdrop dismiss to drawer overlay")

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return changes


def main() -> None:
    print("=" * 60)
    print("Fixing 12 injected pages: profile pic + scroll lock")
    print("=" * 60)

    for page in PAGES:
        filepath = os.path.join(PUBLIC, page)
        if not os.path.exists(filepath):
            print(f"\n  SKIP: {page} (not found)")
            continue

        changes = fix_page(filepath)
        if changes:
            print(f"\n  {page}:")
            for c in changes:
                print(f"    + {c}")
        else:
            print(f"\n  {page}: (already up to date)")

    print("\n" + "=" * 60)
    print("Done.")


if __name__ == "__main__":
    main()
