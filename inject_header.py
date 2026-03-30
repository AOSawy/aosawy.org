"""
Inject unified site header into all showcase/research/teaching pages.
Skips index.html and portfolio.html (they have their own React-rendered nav).
"""
import os

PUBLIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public')

# Pages that already have React-rendered nav bars — skip these
SKIP_FILES = {'index.html', 'portfolio.html'}

HEADER_HTML = '''<!-- Unified Site Header -->
<nav class="ds-site-header" id="siteHeader">
  <div class="ds-header-inner">
    <a href="index.html" class="ds-header-logo">A. Sawy</a>
    <div class="ds-nav-links">
      <a href="index.html">Home</a>
      <a href="research-showcase.html">Research</a>
      <a href="portfolio.html">Portfolio</a>
      <a href="teaching-showcase.html">Teaching</a>
    </div>
    <button class="ds-hamburger" onclick="document.getElementById('siteMobileDrawer').classList.toggle('open'); this.classList.toggle('open');">
      <div class="ds-hamburger-lines"><span></span><span></span><span></span></div>
    </button>
  </div>
</nav>
<div class="ds-mobile-drawer" id="siteMobileDrawer">
  <button class="ds-drawer-close" onclick="document.getElementById('siteMobileDrawer').classList.remove('open'); document.querySelector('.ds-hamburger').classList.remove('open');">&times;</button>
  <a href="index.html" onclick="document.getElementById('siteMobileDrawer').classList.remove('open');">Home</a>
  <a href="research-showcase.html" onclick="document.getElementById('siteMobileDrawer').classList.remove('open');">Research</a>
  <a href="portfolio.html" onclick="document.getElementById('siteMobileDrawer').classList.remove('open');">Portfolio</a>
  <a href="teaching-showcase.html" onclick="document.getElementById('siteMobileDrawer').classList.remove('open');">Teaching</a>
</div>
'''

MARKER = '<!-- Unified Site Header -->'


def inject_header(filepath: str) -> bool:
    """Inject header after <body> tag. Returns True if file was modified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if header already injected
    if MARKER in content:
        print(f"  SKIP (already has header): {os.path.basename(filepath)}")
        return False

    # Find <body> tag (could be <body> or <body ...>)
    body_idx = content.find('<body>')
    if body_idx == -1:
        body_idx = content.find('<body ')
    if body_idx == -1:
        print(f"  ERROR (no <body> tag): {os.path.basename(filepath)}")
        return False

    # Find the end of the <body...> tag
    end_of_body_tag = content.index('>', body_idx) + 1

    # Insert header right after <body>
    new_content = content[:end_of_body_tag] + '\n' + HEADER_HTML + content[end_of_body_tag:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  INJECTED: {os.path.basename(filepath)}")
    return True


def main() -> None:
    html_files = sorted(f for f in os.listdir(PUBLIC_DIR) if f.endswith('.html'))
    modified = 0

    print(f"Found {len(html_files)} HTML files in {PUBLIC_DIR}")
    print(f"Skipping: {', '.join(sorted(SKIP_FILES))}\n")

    for fname in html_files:
        if fname in SKIP_FILES:
            print(f"  SKIP (React nav): {fname}")
            continue
        filepath = os.path.join(PUBLIC_DIR, fname)
        if inject_header(filepath):
            modified += 1

    print(f"\nDone. Modified {modified} files.")


if __name__ == '__main__':
    main()
