# Política de Recopilación con suma (Collect (sum))

Esta política recopila todas las reglas coincidentes y suma los resultados. Solo funciona con **Return Type Value**.

**Ejemplo:**

| Regla | Condición            | Valor devuelto |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Para el valor de entrada **Total Amount = 3500**, la evaluación de las reglas sería:

* **Regla 1**: Total Amount <= 1000 (no coincide)
* **Regla 2**: Total Amount <= 2000 (no coincide)
* **Regla 3**: Total Amount <= 3000 (coincide, Return Value = 3)
* **Regla 4**: Total Amount <= 4000 (coincide, Return Value = 4)
* **Regla 5**: Total Amount <= 5000 (coincide, Return Value = 5)

Dado que se aplica la política **Collect (sum)**, sumamos los **Return Values** de las reglas coincidentes, que son **3, 4, 5**.

**Al sumar estos valores** obtenemos:

* 5 + 4 + 3 = **12**

Por lo tanto, el resultado devuelto por el árbol de decisión sería **12**, que es la suma de todos los valores de retorno coincidentes.
