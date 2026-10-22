# Comparar campo con tolerancias

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-4ee291b0848d-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## Cuándo utilizar esta tarjeta

Utilice esta condición para comparar un campo numérico del documento con un valor de referencia fijo y permitir una desviación definida. Por ejemplo, un importe total puede considerarse coincidente con la referencia 100 si la diferencia no supera 5.

## Dónde encontrarla

En el diseñador de flujos estándar, añada una tarjeta en **Y**, abra **Campo del documento** y seleccione la comparación de un campo con una referencia y tolerancias. El ejemplo siguiente utiliza la versión 2.

## Configuración

Utilice un campo numérico configurado en su organización. El valor del campo, la referencia y la tolerancia se evalúan numéricamente. Mantenga las mismas unidades.

| Ajuste | Significado |
| --- | --- |
| Nombre del campo | El campo configurado, por ejemplo `total_amount`. |
| Operador | La comparación: `eq`, `neq`, `gt`, `ge`, `lt` o `le`. |
| Valor de referencia | El número fijo con el que se compara el campo. |
| Tolerancia | La desviación numérica permitida. |
| Tipo de tolerancia | **Valor** (`value`) para una cantidad absoluta o **Por ciento** (`percent`) para una desviación relativa. |

Con una referencia positiva de 200, una tolerancia porcentual de 5 permite una desviación de 10. Una tolerancia absoluta de 5 permite una desviación de 5. Compruebe los límites relevantes para el operador y los valores elegidos.

## Cómo modifica la tolerancia la comparación

Con una referencia de **100** y una tolerancia absoluta de **5**, el límite inferior es **95** y el superior es **105**.

| Operador | La condición se cumple cuando el valor del campo… |
| --- | --- |
| `eq` (=) | Está entre 95 y 105, incluidos ambos límites. |
| `neq` (≠) | Es inferior a 95 o superior a 105. |
| `gt` (>) | Es superior a 105. |
| `ge` (≥) | Es al menos 95. |
| `lt` (<) | Es inferior a 95. |
| `le` (≤) | Es como máximo 105. |

La tarjeta devuelve el resultado de una condición. Los pasos posteriores dependen del desencadenante, las demás condiciones y las acciones configuradas en el flujo.

<!-- workflow-card-complete-example-20261021 condition_docfield_operator_value_tolerances -->

## Ejemplo práctico

1. Seleccione el campo numérico configurado **Importe total factura** (`total_amount`).
2. Seleccione **Es igual a** (`eq`).
3. Introduzca la referencia **100** y la tolerancia **5**.
4. Seleccione el tipo de tolerancia **Valor** (`value`).

| Valor del campo | Diferencia absoluta respecto a 100 | Resultado esperado |
| --- | --- | --- |
| 103 | 3 | Condición cumplida. |
| 110 | 10 | Condición no cumplida. |
| 95 o 105 | 5 | Condición cumplida: la igualdad incluye los límites de tolerancia. |

Estos son los resultados de cálculo esperados para una configuración de ejemplo. No se ejecutó ningún flujo para este ejemplo.

## Antes de activar la regla

Compruebe un caso coincidente, uno no coincidente y los límites con datos de prueba adecuados. Investigue por separado los campos ausentes, los valores no numéricos y los errores de configuración. Consulte en el registro de ejecución los valores, el operador, la tolerancia y el resultado realmente utilizados.

Si ambos importes proceden de campos del documento, utilice la tarjeta independiente de [comparación de dos campos con tolerancia](compare-two-fields-with-tolerance.md).
