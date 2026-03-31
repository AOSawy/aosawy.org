"""Local dev server with Cloudflare Pages-style _redirects support."""
import http.server
import os

REWRITES = {}

def load_redirects():
    path = os.path.join(os.path.dirname(__file__), '_redirects')
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split()
                if len(parts) >= 3 and parts[2] == '200':
                    REWRITES[parts[0]] = parts[1]

class RewriteHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        clean = self.path.split('?')[0].split('#')[0]
        if clean in REWRITES:
            self.path = REWRITES[clean]
        return super().do_GET()

if __name__ == '__main__':
    load_redirects()
    print(f"Loaded {len(REWRITES)} rewrites from _redirects")
    for src, dst in REWRITES.items():
        print(f"  {src} -> {dst}")
    print("\nServing at http://localhost:3000")
    server = http.server.HTTPServer(('', 3000), RewriteHandler)
    server.serve_forever()
