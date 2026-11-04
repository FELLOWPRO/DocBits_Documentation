# En primer lugar

Se aplica la primera regla que coincide y no se evalúan más reglas.

**Ejemplo:**

| Regla | Condición            | Grupo devuelto |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Si el importe total es **1500**, las reglas evaluadas serán:

* **Regla 1**: Total Amount <= 1000 (no coincide)
* **Regla 2**: Total Amount <= 2000 (coincide) → El árbol de decisión deja de evaluar más reglas y aplica **GROUP_2**.
