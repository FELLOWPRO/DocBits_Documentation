# Regla Orden

Esta política aplica las reglas en el orden en que aparecen en el árbol de decisión y devuelve el resultado de la regla que coincide primero.

**Ejemplo:**

| Regla | Condición            | Grupo devuelto |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Dado que el valor de entrada es **Total Amount = 2500**, la evaluación de las reglas sería:

* **Regla 1**: Total Amount <= 1000 (no coincide)
* **Regla 2**: Total Amount <= 2000 (no coincide)
* **Regla 3**: Total Amount <= 3000 (coincide)
* **Regla 4**: Total Amount <= 4000 (coincide)
* **Regla 5**: Total Amount <= 5000 (coincide)

Con **Regla Orden**, el árbol procesará las reglas en el orden en que están enumeradas. Así, las reglas coincidentes serán:

* **Regla 3**: GROUP_3
* **Regla 4**: GROUP_4
* **Regla 5**: GROUP_5

**Resultado**: **GROUP_3**, **GROUP_4**, **GROUP_5**
