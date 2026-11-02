# Propósito y uso

Una columna de tabla es un campo de la tabla de líneas. Todo lo que DocBits hace con una tabla (extracción, validación, PO matching, exportación) funciona sobre las columnas configuradas aquí.

## Dónde aparece una columna

| Lugar | Qué hace la columna allí |
|---|---|
| **Pantalla de validación** | Una columna en la tabla de líneas. El *Title* es el encabezado, el *Column Type* decide el editor (importe, fecha, texto, sí/no). Las columnas ocultas no se muestran. |
| **Table training** | Cuando entrena la tabla de un proveedor, asigna cada columna de tabla detectada a una de estas columnas configuradas. Solo se pueden asignar columnas configuradas. |
| **Extracción de tablas con IA** | La IA rellena las columnas configuradas. Una columna marcada con *Use AI* la rellena la IA incluso para proveedores con reglas entrenadas. |
| **Reglas de validación** | Las comprobaciones de líneas, como *cantidad × precio unitario = total de línea*, se ejecutan sobre las columnas predeterminadas `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO matching** | Necesita las columnas predeterminadas número de artículo, precio unitario, cantidad e importe total. Sin ellas, el documento muestra *Line Item Table is missing Mandatory column for PO*. |
| **Exportación** | Cada columna no oculta forma parte de los datos de líneas enviados al ERP. El mapeo de exportación hace referencia al *Column name*. |
| **Scripts** | Los scripts leen y escriben columnas por *Column name*, por ejemplo `row["TOTAL_AMOUNT"]`. |

## Alcance

* Las columnas de tabla se configuran **por tabla**, y una tabla pertenece a un **tipo de documento**. Las columnas de factura no afectan a los albaranes.
* La configuración es **por organización**. Las suborganizaciones la heredan.
* Qué columnas se *rellenan* para un proveedor determinado lo decide el entrenamiento de ese proveedor o la IA; la configuración de columnas solo indica qué columnas existen.

## Motivos habituales para cambiar la configuración

* Debe capturarse un valor específico del cliente por línea (centro de coste, número de proyecto, número de artículo interno) → añada una columna.
* Una columna predeterminada nunca se utiliza y sobrecarga la pantalla de validación → ocúltela.
* Una columna siempre debe estar rellenada antes de la exportación → márquela como *Required*.
* Un valor procede de la consulta al ERP y los usuarios no deben editarlo → márquelo como *Read Only*.
* La IA captura mejor una columna que las reglas entrenadas (por ejemplo, descripciones de texto libre) → márquela como *Use AI*.

## Páginas relacionadas

* [Añadir una nueva columna](adding-a-new-column.md)
* [Editar y eliminar columnas](editing-and-deleting-columns.md)
* [Solución de problemas de extracción de tablas](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
