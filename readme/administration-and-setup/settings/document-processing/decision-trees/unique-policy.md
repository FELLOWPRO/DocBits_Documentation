# Política Única (Unique)

Garantiza que solo coincida una única regla. Si coinciden varias reglas, el árbol de decisión devolverá false.

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
* **Regla 2**: Total Amount <= 2000 (coincide)
* **Regla 3**: Total Amount <= 5000 (coincide)
* **Regla 4**: Total Amount <= 4000 (coincide)
* **Regla 5**: Total Amount <= 3000 (coincide)

Dado que coinciden varias reglas (**Regla 2**, **Regla 3**, **Regla 4**, **Regla 5**), el árbol de decisión devolverá **false** porque la política **Única** garantiza que solo pueda coincidir una regla.
