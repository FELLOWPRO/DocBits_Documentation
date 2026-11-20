# Comparar un campo de documento con un valor de referencia

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_operator_value_v1-es-es.png" alt="Comparar un campo de documento con un valor de referencia, Versión 1" width="634"><figcaption><p>Versión 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_operator_value_v2-es-es.png" alt="Comparar un campo de documento con un valor de referencia, Versión 2" width="634"><figcaption><p>Versión 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/es.mp4" %}

**Vídeo:** Tarjeta: Campo del documento comparado con un valor · 0:44 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/es.vtt)

<details>

<summary>Transcripción</summary>

**Campo del documento comparado con un valor** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/es.mp4#t=0.25)

La tarjeta Campo del documento compara un campo del documento con un valor que usted introduce. Elija el campo, por ejemplo Importe total, luego el operador, aquí Mayor que, y el valor, diez mil.

**Texto, números, fechas** · [0:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/es.mp4#t=18.916)

Los campos de texto solo pueden ser iguales o distintos, y las mayúsculas no importan. Los números y las fechas también pueden ser mayores o menores que el valor. Si el campo no está en el documento, la tarjeta toma su camino de error.

**Ejemplo: las facturas grandes necesitan una segunda aprobación** · [0:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/es.mp4#t=32.483)

Por ejemplo, una segunda aprobación para facturas grandes: Importe total mayor que diez mil, luego la tarjeta de asignación para finanzas. Las facturas menores no llegan a este paso.

</details>

## **Propósito:**

Esta tarjeta compara un campo del documento con un valor que usted introduce en la tarjeta. Úsela para enviar los documentos por caminos distintos según el valor de un campo, por ejemplo una segunda aprobación para facturas grandes o una ruta especial para unos pocos proveedores.

La tarjeta dice: **Campo del documento** [Field Name] [Operator] [Field Value].

## **Componentes de la tarjeta:**

1. **Field Name**
   * El campo del documento que se comprueba, elegido entre los campos del tipo de documento.
2. **Operator**
   * Cómo se compara el valor del campo con el **Field Value**. Qué operadores tienen sentido depende del tipo del campo, consulte **Operadores** más abajo.
3. **Field Value**
   * El valor con el que se compara. Según el operador, es un valor único, una lista separada por comas o una expresión regular.

## **Operadores:**

| Operador | Se cumple cuando | Tipos de campo |
| --- | --- | --- |
| **Es igual a** (=) | el valor del campo es igual al Field Value | texto, número, importe, fecha |
| **No es igual a** (≠) | el valor del campo es distinto del Field Value | texto, número, importe, fecha |
| **Mayor Que** (>) | el valor del campo es mayor que el Field Value | número, importe, fecha |
| **Mayor o igual que** (≥) | el valor del campo es mayor o igual que el Field Value | número, importe, fecha |
| **Menor que** (<) | el valor del campo es menor que el Field Value | número, importe, fecha |
| **Menos o igual** (≤) | el valor del campo es menor o igual que el Field Value | número, importe, fecha |
| **Es uno de** | el valor del campo es igual a un elemento de una lista separada por comas | texto |
| **No es uno de** | el valor del campo no es igual a ninguno de los elementos de la lista | texto |
| **Coincide con regex** | la expresión regular se encuentra en el valor del campo | texto, número, importe, fecha |
| **No coincide con regex** | la expresión regular no se encuentra en el valor del campo | texto, número, importe, fecha |

Esta tarjeta no admite campos booleanos (casillas de verificación). Para ellos, use **Checkbox is checked**.

### Es igual a y No es igual a en campos de texto

El texto se compara sin tener en cuenta las mayúsculas, y un espacio cuenta igual que un guion bajo: `Acme Freight` es igual a `acme_freight`. Los espacios al principio y al final se ignoran.

### Es uno de e No es uno de

Use estos operadores para comprobar un campo de texto frente a varios valores a la vez, por ejemplo una lista de ID de proveedor.

* Introduzca los valores como lista separada por comas: `40321,40322,40388`.
* El valor del campo tiene que ser exactamente igual a un elemento. Un valor parcial no coincide: `4032` no está en `40321,40322,40388`, y tampoco un valor más largo como `403210`.
* Las mayúsculas no importan, y un espacio cuenta igual que un guion bajo. Los espacios alrededor de los elementos se ignoran, y los elementos vacíos, como el de `a,,b`, se omiten.
* Para usar una coma dentro de un valor, escríbala como `\,`. `Acme Freight\, LLC,Riverside Supply` es una lista de dos elementos: `Acme Freight, LLC` y `Riverside Supply`.
* Un valor de campo vacío no está en ninguna lista. Entonces **Es uno de** no se cumple e **No es uno de** se cumple.
* Estos operadores solo funcionan con campos de texto. En un campo de número, importe o fecha, o con una lista sin ningún elemento (por ejemplo, solo comas), la tarjeta termina con un error.

### Coincide con regex y No coincide con regex

Use estos operadores cuando decide un patrón, por ejemplo "empieza por" o "consta solo de dígitos".

* El **Field Value** es una expresión regular con sintaxis de Python. Se busca en cualquier parte del valor del campo: `Freight` coincide con `Acme Freight, LLC`.
* Use `^` y `$` para comprobar el valor completo: `^33` significa "empieza por 33", y `^(40321|40322|40388)$` significa "exactamente uno de estos valores".
* El patrón distingue entre mayúsculas y minúsculas. Empiécelo con `(?i)` para ignorar las mayúsculas: `(?i)freight` también coincide con `Acme Freight, LLC`.
* `^` y `$` se refieren al valor completo del campo. Empiece el patrón con `(?m)` para aplicarlos a cada línea de un valor con varias líneas.
* El patrón se usa exactamente como lo escribe. No se recortan espacios y se conservan las mayúsculas, de modo que `\D` (cualquier carácter que no sea un dígito) mantiene su significado, y un patrón que consta de un solo espacio busca un espacio.
* Los caracteres con un significado especial en las expresiones regulares deben escaparse para buscarlos literalmente: `\(copy\)` coincide con el texto `(copy)`, mientras que `(copy)` es un grupo que encuentra la palabra `copy`.
* Los números, importes y fechas se comparan como el texto con el que están almacenados: un importe de 997.60 coincide con `^997\.60$`.
* Un valor de campo vacío se compara como texto vacío, por lo que `^$` coincide con él.
* Un patrón no válido, por ejemplo `(20` con un paréntesis que falta, termina la tarjeta con un error. Lo mismo ocurre cuando un patrón tarda demasiado con un valor (más de 0,05 segundos), lo que solo sucede con patrones mal construidos como `(a|aa)+$`. En ambos casos la tarjeta no se cumple ni deja de cumplirse, de modo que **No coincide con regex** nunca pasa por un patrón defectuoso.

## **Funcionamiento de la tarjeta:**

* **Campo que no está en el documento:** si el documento no tiene ningún campo con el nombre elegido, la tarjeta se detiene e informa de que no se encontró el campo, sea cual sea el operador.
* **Condición cumplida:** el Workflow continúa con la siguiente tarjeta (en el Advanced Workflow, por la salida de éxito).
* **Condición no cumplida:** el Workflow se detiene en esta tarjeta (en el Advanced Workflow, toma la salida de condición no cumplida).
* **Error:** un operador que no corresponde al tipo de campo, un Field Value que falta, una lista vacía o un patrón inutilizable terminan la tarjeta con un error. El registro de la tarjeta muestra el motivo.

## **Configuración:**

Elija el campo en **Field Name**, el operador en **Operator** e introduzca el valor en **Field Value**. Para números e importes, introduzca el valor sin símbolo monetario y con punto decimal, por ejemplo `1000.50`.

Para probar una configuración sin esperar a un documento, abra el menú de la tarjeta en el Workflow Builder, elija **Test Card**, seleccione un documento y pulse **Test on Document**. El registro de la tarjeta muestra el valor del campo, el operador y el resultado.

## **Ejemplos:**

| Objetivo | Field Name | Operator | Field Value | Valor del campo en el documento | Resultado |
| --- | --- | --- | --- | --- | --- |
| Segunda aprobación para facturas grandes | Importe total | Mayor Que | `10000` | 12500.00 | se cumple |
| Dirigir a unos pocos proveedores | ID de proveedor | Es uno de | `40321,40322,40388` | 40322 | se cumple |
| | | | | 4032 | no se cumple |
| Omitir un proveedor con una coma en su nombre | Nombre del proveedor | No es uno de | `Acme Freight\, LLC` | Acme Freight, LLC | no se cumple |
| Números de pedido que empiezan por 33 | Número de pedido | Coincide con regex | `^33` | 33012 | se cumple |
| | | | | 13301 | no se cumple |
| Referencia con letras | Referencia | Coincide con regex | `\D` | AB-1204 | se cumple |
| Copias de facturas | Número de factura | No coincide con regex | `\(copy\)` | INV-1204 (copy) | no se cumple |

## **Conclusión:**

La tarjeta comprueba un único campo del documento frente a un valor, una lista o un patrón. Use **Es uno de** para listas fijas de valores y **Coincide con regex** para patrones como prefijos o formatos.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo utilizar:** Revisar las facturas que superen un monto definido.

**Configuración:** Seleccionar campo numérico `total_amount`, operador `>` y valor de referencia `1000`.

**Resultado esperado y contraejemplo:** Un valor de `1200` cumple la condición. `1000` y `900` no la cumplen: el operador `>` exige un valor estrictamente mayor que `1000`.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
