# Primero y adyacentes

Elige el resultado de la regla que es adyacente a la primera regla que es verdadera.

**Ejemplo:**

| Regla | Condición            | Grupo devuelto |
| ----- | -------------------- | -------------- |
| 1     | Total Amount <= 1000 | GROUP\_1       |
| 2     | Total Amount <= 2000 | GROUP\_2       |
| 3     | Total Amount <= 3000 | GROUP\_3       |
| 4     | Total Amount <= 4000 | GROUP\_4       |
| 5     | Total Amount <= 5000 | GROUP\_5       |

Si el importe total es **1500**, las reglas evaluadas serán:

* **Regla 1**: Total Amount <= 1000 (no coincide)
* **Regla 2**: Total Amount <= 2000 (coincide)

Dado que la **Regla 2** es la primera regla que coincide, **Primero y adyacentes** aplicaría el resultado de la **Regla 3**: **GROUP\_3**.
