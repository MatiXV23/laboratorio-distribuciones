# Laboratorio de distribuciones

Página de estudio de Probabilidad y Estadística: distribuciones de probabilidad discretas (Lección 7) y continuas (Lección 8).

Cada pestaña corresponde a un video e incluye:

- Introducción al tema
- Ecuaciones del video comentadas
- Animaciones interactivas (simulaciones con histograma y valores teóricos)
- Ejercicios del video resueltos paso a paso
- Requisitos previos explicados de forma simple

Además, cada lección tiene dos pestañas extra:

- **Repartido**: los ejercicios propuestos del curso resueltos paso a paso, con gráfico animado por parte, simulación y comparación con la hoja de resultados.
- **Fórmulas** (L7) / **Fórmulas y tablas** (L8): la hoja de fórmulas del profe con agregados, una guía para elegir el modelo y las tablas A.1, A.2 y A.3 interactivas.

Es un único archivo `index.html` sin dependencias de compilación; se publica con GitHub Pages.

## Cómo se actualiza

1. Editar `src/laboratorio.html` (es la fuente; también se publica como artifact en claude.ai).
2. Generar la página: `python3 build.py` (escribe `index.html`).
3. Commit y push a `main`: GitHub Pages se vuelve a publicar solo.
