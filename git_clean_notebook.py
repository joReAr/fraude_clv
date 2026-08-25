"""Filtro 'clean' de git para notebooks: lee un .ipynb por stdin,
borra outputs y contadores de ejecución, y lo escribe por stdout.
Configurado en .gitattributes + git config filter.stripoutputs.*
No modifica el archivo en disco: solo afecta lo que git graba."""
import sys

import nbformat

nb = nbformat.read(sys.stdin, as_version=4)
for cell in nb.cells:
    if cell.get("cell_type") == "code":
        cell["outputs"] = []
        cell["execution_count"] = None
    cell.get("metadata", {}).pop("execution", None)

nbformat.write(nb, sys.stdout)
