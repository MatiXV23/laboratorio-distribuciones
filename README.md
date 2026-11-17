# Laboratorio de distribuciones

Página de estudio de Probabilidad y Estadística: distribuciones de probabilidad discretas (Lección 7) y continuas (Lección 8).

Cada pestaña corresponde a un video e incluye:

- Introducción al tema
- Ecuaciones del video comentadas
- Animaciones interactivas (simulaciones con histograma y valores teóricos)
- Ejercicios del video resueltos paso a paso
- Requisitos previos explicados de forma simple

Es un único archivo `index.html` sin dependencias de compilación; se publica con GitHub Pages.

## Cómo se actualiza

1. Editar `src/laboratorio.html` (es la fuente; también se publica como artifact en claude.ai).
2. Generar la página: `python3 build.py` (escribe `index.html`).
3. Commit y push a `main`: GitHub Pages se vuelve a publicar solo.
