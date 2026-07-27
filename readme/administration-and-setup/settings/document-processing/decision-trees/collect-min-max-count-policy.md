# Recoger (Min/Max/Recuento)

Esta política recopila todas las reglas coincidentes y selecciona el **mínimo**, el **máximo** o **cuenta** las apariciones. Solo funciona con **Return Type Value**.

**Ejemplo:**

| Regla | Condición            | Valor devuelto |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Si se selecciona la opción **Recoger (Min)**, el resultado devolverá el valor **mínimo** de los **Return Values** de las reglas coincidentes.
   * Para el valor de entrada **Total Amount = 2500**, la evaluación de las reglas sería:
     * **Regla 1**: Total Amount <= 1000 (no coincide)
     * **Regla 2**: Total Amount <= 2000 (no coincide)
     * **Regla 3**: Total Amount <= 3000 (coincide, Return Value = 3)
     * **Regla 4**: Total Amount <= 4000 (coincide, Return Value = 4)
     * **Regla 5**: Total Amount <= 5000 (coincide, Return Value = 5)
   * Las **reglas coincidentes** son la Regla 3, la Regla 4 y la Regla 5, con **Return Values** de **3, 4 y 5**.
   * Dado que se aplica la política **Recoger (Min)**, el resultado será el **valor mínimo**, que es **3**.
   * **Resultado**: **3**
2. Si se selecciona la opción **Recoger (Max)**, el resultado devolverá el valor **máximo** de los **Return Values** de las reglas coincidentes.
   * Para la misma evaluación anterior, el resultado será:
   * **Resultado**: **5**
3. Si se selecciona la opción **Recoger (Recuento)**, el resultado contará el **número de reglas coincidentes**.
   * Para la misma evaluación anterior, el resultado será:
   * **Resultado**: **3** (ya que coincidieron 3 reglas).
