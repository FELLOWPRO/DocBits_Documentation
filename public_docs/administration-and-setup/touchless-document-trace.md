# Touchless Intelligence: Seguimiento del documento

Introduzca un ID de documento en **Document ID**, o abra un documento de muestra de un clúster, para ver **qué le ocurrió a este documento**.

La cabecera muestra el archivo, su estado (por ejemplo **En proceso**), la ejecución que está consultando y su primer bloqueador, además de un botón **Documento** con el ID del documento.

<figure><img src="../.gitbook/assets/touchless-nova-trace-overview-es.png" alt="Dev NOVA: recorrido y valores registrados en la primera ejecución de prueba"><figcaption><p>Nueva captura de Dev NOVA 11.0.3, del 4 de noviembre de 2026. La factura ficticia se detiene en la validación de campos. Clasificación, búsqueda de proveedor y extracción de cabecera y tabla contienen valores realmente registrados. Las tarjetas muestran el documento y su historial. Es la interfaz del producto en funcionamiento.</p></figcaption></figure>

La **Ruta de la tubería** muestra 14 etapas: Intake, Classification, E-Document Validation, Supplier Identification, Text Recognition, Header Extraction, Table Extraction, Field Validation, PO Lookup, PO Line Match, Approval, Workflow Routing, Export, ERP Acknowledgement. Cada etapa lleva un solo estado:

| Estado | Significado |
| --- | --- |
| **Aprobado** (verde) | La etapa se ejecutó sin problemas |
| **Me detuve aquí** (naranja) | La etapa bloqueó el documento |
| **No alcanzado** | Paso posterior al primer bloqueo en el recorrido; compruebe en el registro si hay ejecuciones adicionales registradas |
| **No se registró nada** (discontinuo) | No se registraron datos para esta etapa |
| **No aplicable** | La etapa no se aplica a este documento |

### Registro de etapas

El **registro de etapas** bajo la ruta enumera las mismas etapas con lo que cada una registró. Un punto de estado y la palabra de estado aparecen a izquierda y derecha de cada fila.

* Cada valor es una **etiqueta de valor**: un número con su unidad, por ejemplo **Confianza 100 %**, **Umbral 60 %**, **Reglas fallidas 0**, **8 campos faltantes** o **0 brechas de asignación**. Los porcentajes se muestran como `97 %`, nunca como `0.97`.
* **Detalles** abre la lista completa de valores que registró una etapa, incluidas las alternativas que consideró.
* La etapa que bloqueó el documento indica el motivo, por ejemplo **Validación de campos fallida**.
* Un valor que ninguna etapa registró se muestra como **No registrado**, nunca como un valor inventado. Los valores son números y términos fijos, nunca texto del documento.
* **Mostrar diagnósticos sin procesar** activa los datos en bruto cuando el soporte los solicita.

<figure><img src="../.gitbook/assets/touchless-nova-trace-stage-log-es.png" alt="Dev NOVA: registro con confianza, valores de extracción y validación bloqueada"><figcaption><p>Primera ejecución real: confianza de clasificación del 100 %, 0 proveedores candidatos, 1 fila y 7 brechas de asignación. Un paso aprobado confirma su ejecución, no la identificación del proveedor ni la exactitud de todos los valores. La validación indica un campo obligatorio ausente.</p></figcaption></figure>

### Ejecuciones y cambios

El selector permite elegir un intento; el historial muestra su resultado y primer bloqueo. Las diferencias registradas comparan la ejecución seleccionada con su predecesora, no automáticamente con la actual. Cada diferencia incluye su unidad; los valores idénticos permanecen sin cambios.

La tarjeta Documento muestra tipo, proveedor, número de factura, pedido, páginas y método de análisis registrado. Aquí Manual corresponde al tipo indicado durante la importación de prueba. El 100 % no demuestra de forma independiente la precisión de una clasificación automática.

### Interpretar los detalles de proveedor y tabla

<figure><img src="../.gitbook/assets/touchless-nova-trace-supplier-es.png" alt="Dev NOVA: identificadores encontrados, búsqueda en datos maestros y asignación del proveedor"><figcaption><p>Se encuentra el nombre en la factura y se busca en los datos maestros, pero no se asigna ningún proveedor. Esta factura no contiene NIF-IVA, IBAN, correo electrónico ni GLN. No encontrar una coincidencia en los datos maestros es distinto de no encontrar un valor en la factura.</p></figcaption></figure>

Compruebe por separado si el identificador estaba en el documento, si se buscó y si se asignó un proveedor. Un paso verde no responde por sí solo a estas tres preguntas.

<figure><img src="../.gitbook/assets/touchless-nova-trace-table-es.png" alt="Dev NOVA: detalle de la primera ejecución con siete brechas de asignación"><figcaption><p>El detalle indica 7 brechas de asignación para 1 tabla y 1 fila. Compruebe la asignación de columnas antes de concluir que falló la extracción. El pie de comparación no es una base válida para la primera ejecución seleccionada, que no tiene predecesora.</p></figcaption></figure>

### Reconocer un reinicio real

<figure><img src="../.gitbook/assets/touchless-nova-trace-runs-es.png" alt="Dev NOVA: comparación de dos ejecuciones reales sin cambios en los valores registrados"><figcaption><p>La misma factura tras un reinicio manual real, sin corregir campos. Una nueva ejecución acredita otro intento, no una mejora. Los valores idénticos se muestran sin cambios; no se han inventado diferencias.</p></figcaption></figure>

Un reinicio manual es una intervención humana. Solo si el documento termina correctamente más adelante contará como AP Assisted. Mientras siga en proceso, queda fuera del denominador de documentos finalizados.

Límites de la evidencia. Este caso no demuestra aprobación de negocio, exportación correcta ni confirmación del ERP. El comparador de pedidos heredado no aporta aquí una ruta de decisión registrada; no acredita un cotejo con Infor. En NOVA 11.0.3, el registro puede mostrar una búsqueda de pedido aprobada tras la validación bloqueada mientras el recorrido la presenta como siguiente paso. Compruebe ambas vistas. El resumen también indica que el número de factura no está registrado aunque sí aparece en la extracción; compare el original con los campos extraídos.

## Separar extracción y datos de origen

1. Compare la factura original con los campos y posiciones extraídos **antes de la corrección manual**. Un valor corregido actual no prueba la extracción original.
2. Lea el primer bloqueo. Un paso de extracción aprobado confirma la ejecución del paso, no la exactitud de cada valor.
3. Compare pedido importado e Infor actual, incluidas unidades, unidades de precio y fecha de importación.
4. Distinga factura frente a extracción, extracción correcta frente a datos importados, e Infor frente a su copia. Si falta evidencia, deje abierta la causa.
5. Revise intervenciones, aprobaciones, reinicios y resultado final.

**Ejemplo:** factura y extracción indican 10,00 €; el pedido importado, 9,00 €. Hay una discrepancia de pedido, no un error de extracción demostrado. Confirme el precio acordado y corrija el origen o la importación. Un reinicio manual seguido de éxito da AP Assisted. Consulte [los ejemplos y el cálculo](touchless-metrics.md).

Varios documentos con los mismos campos faltantes demuestran un bloqueo repetido, pero no necesariamente un valor predeterminado ausente: revise extracción, contenido del original, validación y configuración.

## Acreditar la extracción original y los bloqueos sucesivos

1. Abra el documento desde su traza y compruebe ID y ejecución. Compare número de pedido, moneda, cantidades, unidades, unidades de precio, precios, importes de línea y totales relevantes.
2. Separe los valores actuales de los anteriores a una corrección. Utilice evidencia histórica de esa ejecución. Cambiar de ejecución no garantiza reconstruir todas las celdas antiguas.
3. Si falta el valor inicial, anótelo como **no evaluable**, no como correcto. Defina campos, líneas, selección y tamaño de muestra antes de informar de precisión de extracción.
4. Compare copia importada, fecha de importación e Infor actual para separar una fuente incorrecta de una copia antigua.

Una ejecución puede detenerse porque falta el pedido; tras importarlo, otra puede revelar una diferencia de precio. La primera no demuestra que llegara a esa comprobación posterior. Un reinicio humano persiste tras el éxito como AP Assisted; un rechazo ERP definitivo tiene prioridad como excepción. **No registrado** significa falta de evidencia.

Las herramientas y la clasificación de las acciones humanas se explican en [Touchless con MCP](touchless-mcp.md).

## Páginas relacionadas

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md)
* [Diagnóstico de la coincidencia con la OC](touchless-po-matching-diagnosis.md)

Las capturas de pantalla de esta página muestran la interfaz en español.

<!-- Touchless documentation alignment 2026-11-04: extraction quality is distinct from process automation. KPI definition checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4; existing native screenshots and video sources preserved except unsafe historical list images. -->

<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->

Las cinco nuevas capturas muestran la interfaz localizada de Dev NOVA 11.0.3 y la misma factura de prueba creada para la documentación. Cualquier imagen separada del original y sus campos solo ilustra esa comparación.
