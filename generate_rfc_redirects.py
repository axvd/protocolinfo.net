from pathlib import Path

RFC_DIR = Path("static/rfc")
OUT = Path("static/_redirects")

lines = []

for html in sorted(RFC_DIR.glob("rfc*.html")):
    name = html.stem
    lines.append(f"/rfc/{name} /rfc/{name}.html 200")

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"Generated {OUT} with {len(lines)} redirects")
