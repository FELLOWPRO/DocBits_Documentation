# Cualquier

Pueden ser verdaderas varias reglas, pero el resultado de esas reglas debe ser el mismo.

**Ejemplo:**

| Regla | Condición            | Grupo devuelto |
| ----- | -------------------- | -------------- |
| 1     | Total Amount <= 1000 | GROUP\_1       |
| 2     | Total Amount <= 2000 | GROUP\_2       |
| 3     | Total Amount <= 3000 | GROUP\_3       |
| 4     | Total Amount <= 4000 | GROUP\_4       |
| 5     | Total Amount <= 5000 | GROUP\_5       |

Si el importe total es **2500**, las reglas evaluadas serán:

* **Regla 1**: Total Amount <= 1000 (no coincide)
* **Regla 2**: Total Amount <= 2000 (no coincide)
* **Regla 3**: Total Amount <= 3000 (coincide)
* **Regla 4**: Total Amount <= 4000 (coincide)
* **Regla 5**: Total Amount <= 5000 (coincide)

Para que **Cualquier** se aplique, todas las reglas coincidentes deben devolver el mismo **Return Group**. Dado que los grupos no coinciden entre las distintas reglas, el resultado sería **false**.
