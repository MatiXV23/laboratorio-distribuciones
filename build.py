"""Genera index.html (GitHub Pages) a partir de src/laboratorio.html (fuente del artifact).

La fuente no tiene <!doctype>, <html>, <head> ni <body>: el artifact de claude.ai
los agrega al publicar. Este script los agrega para la versión de GitHub Pages.

Uso: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src" / "laboratorio.html"
OUT = ROOT / "index.html"

s = SRC.read_text(encoding="utf-8")
i = s.index('<div class="wrap">')
head, body = s[:i], s[i:]
OUT.write_text(
    "<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<meta name=\"description\" content=\"Animaciones interactivas, ecuaciones comentadas y ejercicios resueltos de distribuciones discretas y continuas.\">\n"
    + head.rstrip()
    + "\n<style>html{color-scheme:light}body{margin:0}</style>\n</head>\n<body>\n"
    + body.rstrip()
    + "\n</body>\n</html>\n",
    encoding="utf-8",
)
print(f"index.html generado ({OUT.stat().st_size} bytes)")
