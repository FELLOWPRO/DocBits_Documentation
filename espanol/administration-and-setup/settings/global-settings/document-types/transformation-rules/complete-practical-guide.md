# Reglas de transformación: panorama práctico completo

> Limitación conocida de la vista previa (comprobada el 29 de octubre de 2026, versión 11.15.2): al añadir el prefijo `INV-`, la vista previa cambia incorrectamente `INV-4711` a `INV-INV-4711`. La prueba independiente del servidor conserva `INV-4711`. Comprueba también la ejecución repetida mediante una prueba del servidor; un resultado correcto en la vista previa por sí solo no demuestra la ejecución completa al guardar.

Estado de verificación: 28 de octubre de 2026. Los ejemplos se verificaron con valores sintéticos de formación en Dev NOVA. Una previsualización no es prueba de un cambio de documento guardado, de una conciliación de pedido ni de una exportación ERP.


## Nombres visibles en el editor

Algunas etiquetas de la interfaz actual presentan traducciones imprecisas. La tabla indica el texto que aparece realmente para que puedas encontrar el paso correcto; la explicación funcional usa terminología técnica. Las capturas muestran la interfaz sin modificar.

| Operación | Etiqueta visible |
| --- | --- |
| case | Cambiar mayúsculas/minúsculas |
| trim | Recortar |
| pad | Almohadilla |
| truncate | Truncado |
| affix | Afijo |
| sanitize | Limpiar |
| substring | Toma una rebanada |
| regex_extract | Extracto |
| regex_replace | Buscar y reemplazar |
| value_map | Valores del mapa |
| date_format | Fecha de reformateo |
| number_format | Número de formato |
| fix_value | Valor fijo |
| clear | Borrar |
| clear_rows | Borrar todas las filas |
| add_row | Añadir fila |


## Cuatro ámbitos de aplicación

| Ámbito | Entrada y objetivo | Tarea típica |
| --- | --- | --- |
| Campo de cabecera | Un campo por documento; la fuente puede ser otro campo de cabecera | Limpiar número de factura, adoptar número de pedido |
| Columna de tabla | La columna seleccionada por fila de la tabla seleccionada | Uniformizar números de artículo o códigos de unidad |
| Filas de tabla | Tabla completa | Eliminar filas o añadir posiciones definidas |
| Routing | Atributo de documento `sub_org_id` | Asignar suborganización existente |

Los ámbitos se ejecutan **Campo de cabecera → Routing → Filas de tabla → Columna de tabla**. Dentro de un ámbito, la prioridad y la clave de regla determinan el orden. Los pasos de una regla se ejecutan de arriba abajo. Una regla posterior puede por tanto leer valores ya modificados. El orden de los ámbitos no se invierte por la prioridad de una regla individual.

## Todos los pasos del editor

El editor verificado ofrece 14 pasos de valor para cabecera/columna, dos pasos para tablas completas y una asignación fija en Routing. `fix_value` y la asignación fija de Routing utilizan ambos `set_value` en el servidor. Adicionalmente, la interfaz conoce `default`; este paso no se ofrece en el menú de pasos normales verificado.

| Paso | Variantes y parámetros | Ejemplo | Límite y contraprueba |
| --- | --- | --- | --- |
| Cambiar mayúsculas/minúsculas (`case`) | upper, lower, title, capitalize | `inv-4711` → `INV-4711` | Title: `acme gmbh` → `Acme Gmbh`; capitalize: `aCME GMBH` → `Acme gmbh`. Los nombres propios/abreviaturas pueden cambiar de forma técnicamente no deseada. En `capitalize`, la previsualización del navegador verificada deja el resto sin cambios, mientras que el servidor lo escribe en minúsculas; verificar el valor del servidor separadamente. |
| Recortar (`trim`) | ambos / izquierda / derecha; carácter vacío = espacio en blanco | `  4711  ` → `4711` | Se conserva `47 11`. Carácter izquierda `0`: `004711` → `4711`, pero `000` → vacío. Los caracteres son un conjunto, no un texto prefijo completo. |
| Rellenar (`pad`) | longitud mínima, un carácter de relleno, izquierda/derecha | Longitud 10, izquierda `0`: `4711` → `0000004711` | Ya con 11 caracteres permanece en 11 caracteres. Derecha `_`, longitud 6: `ABC` → `ABC___`. |
| Truncar (`truncate`) | longitud máxima | Longitud 10: `ABCDEFGHIJKL` → `ABCDEFGHIJ` | `ABC` permanece `ABC`. El corte pierde información y puede hacer coincidir números. |
| Afijo (`affix`) | añadir/eliminar prefijo/sufijo | `INV-` + `4711` → `INV-4711` | Un afijo exacto existente no se añade dos veces. La eliminación solo actúa en el borde correspondiente y respeta las mayúsculas. |
| Limpiar caracteres (`sanitize`) | conservar alfanumérico / letras / dígitos / alfanumérico + espacio; alternativamente eliminar clase de caracteres | `DE 123.456.789` → `DE123456789` | Los signos pueden ser portadores de significado. Al eliminar, la entrada es una clase de caracteres de expresión regular; proteger correctamente el guion, p. ej. `.\-/`. |
| Fragmento (`substring`) | inicio + longitud **o** inicio + fin; índices negativos posibles | Inicio 3, fin 7: `DE-4711-X` → `4711` | El inicio cuenta desde 0, el fin es exclusivo. Inicio −4: últimos cuatro caracteres. Se requiere fuente original separada. |
| Extraer (`regex_extract`) | expresión regular, grupo de captura | `PO[- ]?(\d+)`, grupo 1: `Order PO-45001234` → `45001234` | Primera coincidencia; grupo 0 = coincidencia completa. Sin coincidencia: vacío. Se requiere fuente separada. |
| Buscar y reemplazar (`regex_replace`) | patrón, reemplazo, cantidad | `\s+` → espacio: `ACME    GmbH` → `ACME GmbH` | Cantidad 0 = todas, 1 = primera coincidencia. Se requiere fuente separada. Verificar expresiones regulares de navegador/servidor separadamente para patrones complejos. |
| Asignar valores (`value_map`) | pares completos de→para; ignorar mayúsculas; reemplazo sin coincidencia | `stk` → `PCE` con `STK→PCE` y mayúsculas ignoradas | Reemplazo vacío significa **conservar entrada**. `BOX` permanece `BOX`; un reemplazo fijo `C62` sobrescribiría `BOX`. El recorte no se realiza automáticamente. |
| Formatear fecha (`date_format`) | patrón de salida, p. ej. `%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y` | `2026-10-28` → `28.10.2026` en destino de texto | En campos de cabecera DATE, el valor guardado puede permanecer en ISO y solo cambiar la representación. El texto ilegible permanece sin cambios; la prueba del servidor indica el motivo. |
| Formatear número (`number_format`) | de_DE / en_US / en_GB / fr_FR; decimales mín./máx. | `1234.5` → `1234,50` o `1234.50` en el resultado del servidor verificado | Sin separador de miles en el resultado del servidor verificado. Sin conversión de moneda o cantidad. Verificar redondeo y reprocesamiento separadamente. |
| Valor fijo (`fix_value` en el editor, `set_value` en la API) | un valor fijo | `USD` → `EUR` | También sobrescribe valores existentes. No confundir con un valor por defecto. |
| Vaciar (`clear`) | sin parámetros | `Altwert` → `""` | Vacía el valor; no elimina ni la definición de campo ni el documento. |
| Eliminar todas las filas (`clear_rows`) | solo filas de tabla | 2 posiciones → 0 | Puede invalidar referencias de filas y la conciliación de pedido existente. |
| Añadir fila (`add_row`) | inicio/fin; por columna valor fijo o fuente de cabecera | Cantidad `1`, importe neto de `header.total_net_amount` | Sin eliminación previa solo con ejecución única adecuada. Sin agregación automática de posiciones existentes. |
| Suborganización fija (`set_value`, Routing) | destino existente del selector de suborganizaciones | Proveedor A → Suborganización Norte | No es un atributo de estado/usuario/permiso arbitrario. Alternativamente asignación mediante `value_map` y fuente. |

### Valor por defecto mediante la interfaz

`default` complementa su valor solo con entrada ausente/vacía. Con valor por defecto `1`, `null` y `""` dan el valor `1`; `0` permanece `0`, `100` permanece `100`. Esto está verificado en el servidor. El editor normal no tiene para ello un paso propio en el estado verificado. El caso sencillo técnicamente equivalente se puede representar frecuentemente con **destino vacío → valor fijo**. Es una condición de regla con asignación, no un punto de menú oculto.

## Nueve secuencias prácticas detalladas

- [01 · Fundamentos, ámbitos de aplicación y pruebas seguras](01-foundations.md)
- [02 · Limpiar texto: escritura, recorte y caracteres](02-text-cleaning.md)
- [03 · Dar forma a números: rellenar, acortar, prefijo y sufijo](03-numbers-and-affixes.md)
- [04 · Fragmentos y patrones: cortar, extraer, reemplazar](04-substrings-and-patterns.md)
- [05 · Asignaciones de valor y reglas por fila de tabla](05-value-mapping.md)
- [06 · Formatear fechas y números correctamente](06-dates-and-numbers.md)
- [07 · Adoptar campos, valores fijos, vaciar y valores por defecto](07-field-copy-and-defaults.md)
- [08 · Reconstruir filas de tabla](08-table-rows.md)
- [09 · Routing, orden, datos maestros y repeticiones](09-routing-and-execution.md)

| Secuencia | Contenido | Punto de verificación concreto |
| --- | --- | --- |
| 01 Fundamentos | Objetivo, fuente, cuatro ámbitos, pipeline, condiciones, previsualización, guardado | Caso adecuado, caso contrario, regla guardada reabierta |
| 02 Limpieza de texto | Las cuatro escrituras, recorte, todos los modos de limpieza | Espacios internos, secuencia pura de ceros, caracteres portadores de significado |
| 03 Números | Rellenar, acortar, las cuatro variantes de afijo | Número demasiado largo, prefijo ya existente, prefijos dobles |
| 04 Patrones | Fragmento, índices negativos, extracción/grupos, reemplazo/cantidad | Fuente separada, sin coincidencia, varias coincidencias |
| 05 Asignación | Pares, mayúsculas, reemplazo, aplicación por fila | `STK→PCE`, `BOX` desconocido, reaplicación sobre `PCE` |
| 06 Formatos | Fecha, DATE frente a texto, fecha ilegible, formatos numéricos | Valor real del servidor en lugar de representación del navegador supuesta |
| 07 Adopción de campo | Otra fuente, destino vacío, valor fijo, vaciar, valor por defecto de API | Proteger número de pedido correcto existente; cero permanece cero |
| 08 Tablas | Eliminar, añadir, valores de columna estáticos y dinámicos | Orden, repetición, número de filas y referencias de pedido |
| 09 Interacción | Routing, fases, lookup, ejecución única, protocolos | Fuente de cabecera limpiada, condición omitida, segundo guardado |

## Condiciones y fuentes

Con "Siempre" la regla aplica sin restricción técnica para el tipo de documento. "Solo si…" la limita mediante condiciones. Los valores de cabecera están en el contexto `header.*`, las características del documento en `doc.*`; `row.*` solo está disponible en el contexto de fila de una regla de columna. Los grupos anidados de Y/O permiten criterios combinados. Para los operadores individuales aplica la documentación separada de las condiciones de regla.

**Ejemplo de adopción de campo:** Destino `purchase_order`, fuente `header.invoice_id`, condición `header.purchase_order` está vacío, pasos Recortar → Mayúsculas. `  po-4711  ` da `PO-4711`. Un número de pedido ya correctamente relleno debe permanecer sin cambios. No vaciar la fuente incorrecta: copiar con procesamiento no mueve la fuente.

**Ejemplo de número de artículo:** Tabla `INVOICE_TABLE`, columna `ITEM_NUMBER`, eliminar prefijo `Art.-Nr. ` → conservar alfanumérico → mayúsculas. `Art.-Nr. ab-12/3` da `AB123`. Solo adecuado si el sistema destino espera exactamente esta forma.

**Ejemplo de fila total:** Para un proveedor claramente delimitado primero `clear_rows`, luego `add_row`; `POSITION=001`, `QUANTITY=1`, `NET_AMOUNT` del importe neto de la cabecera. Si una conciliación de pedido sobre el total es correcta desde el punto de vista del negocio, se decide mediante la configuración adicional de pedido y una prueba de conciliación separada.

## Repetición y ejecución única

Las reglas pueden ejecutarse en varios ciclos de procesamiento y al guardar de nuevo. Verifique siempre **toda la pipeline**, no solo la estabilidad de un paso individual.

* `substring`, `regex_extract` y `regex_replace` no pueden leer su propio valor de destino en el contrato de servidor verificado. Se requiere una fuente separada; `run_once` no levanta esta restricción.
* Añadir un afijo exacto ya existente es estable. Eliminar un prefijo múltiples veces presente puede, en cambio, seguir eliminando en cada ejecución.
* `A→B` y `B→C` en la misma asignación de valor pueden, en dos ejecuciones, convertir finalmente `A` en `C`. Pruebe las salidas de nuevo como entradas.
* `clear_rows → add_row` reconstruye una tabla de forma limitada. `add_row` sin eliminación previa requiere una ejecución única adecuada, de lo contrario la tabla crece en cada guardado.
* "Solo una vez por documento" marca una regla realmente aplicada. Las condiciones no cumplidas no consumen la aplicación. Sin prueba de documento/aplicación legible fiable, la ejecución de una regla de una sola vez se aplaza.

## Después del lookup y antes de la conciliación de pedido

"También ejecutar después de la búsqueda de datos maestros" añade una fase tras el llenado del lookup y antes de la conciliación de pedido. Solo las reglas marcadas correspondientemente se ejecutan en esta fase adicional. Los demás ciclos permanecen. Combinado con ejecución única, la regla espera en el primer ciclo de extracción a la fase posterior; si la fase de lookup falla, entra en consideración un ciclo regular posterior. La visualización de fases del editor actual muestra estas diferencias.

## Una prueba de aceptación robusta

1. Definir objetivo técnico, formato del sistema destino y ámbito de aplicación.
2. Preparar un valor bruto adecuado, un caso contrario, un valor vacío y un resultado ya procesado.
3. Verificar condiciones y todos los valores intermedios en la previsualización.
4. Ejecutar prueba en el servidor contra el mismo ejemplo; comparar especialmente patrones complejos y formatos de número/fecha.
5. Guardar regla y reabrirla. Una regla activa solo utilizar en el alcance de prueba previsto.
6. En un documento aislado, guardar, recargar y verificar valor y visualización; en tablas también número de filas y valores de columna.
7. Guardar una vez más. El resultado no debe modificarse o multiplicarse de forma no deseada.
8. Si es necesario para el objetivo de negocio, verificar adicionalmente la conciliación de pedido y la recepción real en el sistema destino. Un protocolo de transformación por sí solo no prueba estos resultados.

## Lo que una transformación no realiza automáticamente

Ningún nuevo reconocimiento OCR, ninguna conversión matemática de unidades o moneda, ninguna agregación arbitraria de tablas y ninguna contabilización ERP completa. El Routing está limitado al atributo de documento ofrecido. La disponibilidad y la visualización exacta dependen de la versión desplegada, el tipo de documento y la configuración de la organización.

## Documento de ejercicio continuo

{% file src="../../../../../.gitbook/assets/transformation-training-invoice-es-20261028.pdf" %}
Descargar factura de formación
{% endfile %}

El documento ficticio contiene dos posiciones, diferentes escrituras de la unidad y una referencia de pedido en el texto libre. Para pruebas de regla reproducibles, los valores iniciales se preparan deliberadamente; esto no es prueba de una extracción OCR automáticamente libre de errores.
