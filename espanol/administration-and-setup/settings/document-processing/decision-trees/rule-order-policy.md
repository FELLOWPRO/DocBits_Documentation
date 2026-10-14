# Regla Orden

Esta política aplica las reglas en el orden en que aparecen en el árbol de decisión y devuelve el resultado de la regla que coincide primero.

**Ejemplo:**

| Regla | Condición            | Grupo devuelto |
| ----- | -------------------- | -------------- |
| 1     | Total Amount <= 1000 | GROUP\_1       |
| 2     | Total Amount <= 2000 | GROUP\_2       |
| 3     | Total Amount <= 3000 | GROUP\_3       |
| 4     | Total Amount <= 4000 | GROUP\_4       |
| 5     | Total Amount <= 5000 | GROUP\_5       |

Dado que el valor de entrada es **Total Amount = 2500**, la evaluación de las reglas sería:

* **Regla 1**: Total Amount <= 1000 (no coincide)
* **Regla 2**: Total Amount <= 2000 (no coincide)
* **Regla 3**: Total Amount <= 3000 (coincide)
* **Regla 4**: Total Amount <= 4000 (coincide)
* **Regla 5**: Total Amount <= 5000 (coincide)

Con **Regla Orden**, el árbol procesará las reglas en el orden en que están enumeradas. Así, las reglas coincidentes serán:

* **Regla 3**: GROUP\_3
* **Regla 4**: GROUP\_4
* **Regla 5**: GROUP\_5

**Resultado**: **GROUP\_3**, **GROUP\_4**, **GROUP\_5**
