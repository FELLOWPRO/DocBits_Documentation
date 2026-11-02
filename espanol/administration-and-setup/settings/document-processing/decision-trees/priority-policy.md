# Prioridad

Al elegir esta opción puedes establecer prioridades para cada regla. Cuanto menor sea el número seleccionado, mayor será la prioridad (es decir, la prioridad 1 tiene la prioridad más alta). Las reglas se evalúan según su orden de prioridad. Se aplicará la regla coincidente de mayor prioridad.

**Ejemplo:**

<table><thead><tr><th width="137">Regla</th><th width="110">Prioridad</th><th width="268">Condición</th><th>Grupo devuelto</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Si el importe total es **1500**, las reglas evaluadas serán:

* **Regla 1**: Total Amount <= 1000 (no coincide)
* **Regla 2**: Total Amount <= 2000 (coincide)
* **Regla 3**: Total Amount <= 3000 (coincide)
* **Regla 4**: Total Amount <= 4000 (coincide)
* **Regla 5**: Total Amount <= 5000 (coincide)

Dado que la prioridad se aplica en el orden **5, 4, 3, 2, 1**, la regla coincidente de mayor prioridad será la **Regla 5** (**GROUP_5**). El árbol de decisión devolverá **GROUP_5** porque la **Regla 5** tiene la prioridad más alta (prioridad 1).
