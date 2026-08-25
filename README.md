# fraude_clv

Notas y notebooks de aprendizaje sobre modelos BTYD/CLV (BG/NBD, Pareto-NBD, distribuciones NBD)
en el contexto de un modelo de fuga de clientes.

Este repo contiene únicamente material de aprendizaje: teoría en Markdown y notebooks de
exploración. No incluye datos, credenciales, entornos ni el código de producción del proyecto.

## Contenido

- `notas/` — apuntes teóricos en Markdown:
  - `Teoría Distribuciones Base.md`
  - `NBD - Poisson, Gamma y Binomial Negativa.md`
  - `BG-NBD y Pareto-NBD.md`
  - `Estimación Puntual - Momentos y Máxima Verosimilitud.md`
  - `Ejemplos y ejercicios.md`
- `notebooks/` — notebooks de exploración (outputs limpiados, sin datos reales):
  - `descargar.ipynb`
  - `EDA.ipynb`
  - `exploracion.ipynb`
  - `01_eda_fuga.ipynb`

## Entorno

- Python 3.13.9 (Anaconda)

Librerías principales usadas en los notebooks:

- `polars`
- `numpy`
- `pandas`
- `scipy`
- `matplotlib`
- `seaborn`
- `pyarrow`
- `sqlalchemy` / `psycopg2` (conexión a base de datos, no incluida en este repo)
- `jupyter` / `jupyterlab`

## Nota

Los notebooks referencian rutas de datos y una conexión de base de datos internas que no
forman parte de este repositorio; se incluyen solo por su valor como ejercicio de
aprendizaje y análisis exploratorio.
