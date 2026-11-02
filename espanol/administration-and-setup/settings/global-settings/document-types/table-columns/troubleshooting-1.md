# Solución de problemas

## La nueva columna no aparece en la pantalla de validación

* El documento se procesó antes de añadir la columna. Los cambios se aplican a los documentos cargados o reiniciados después; **reinicie el documento** (Dashboard → menú del documento → Restart).
* La columna está **Hidden**. Compruebe el indicador en la lista de Table Columns.
* La columna se añadió a una **tabla distinta** de la que se muestra. La pantalla de validación muestra las tablas del tipo de documento; compare la columna *Table name*.
* El documento no es del tipo de documento que configuró.

## La columna existe pero siempre está vacía

* El proveedor tiene **reglas entrenadas** y la nueva columna no está asignada en ellas. Abra uno de los documentos del proveedor en el entrenamiento de tablas y asigne la columna, o active *Use AI* en la columna.
* Con la extracción con IA, el valor no es reconocible en el documento (sin encabezado, abreviado, en otro idioma). Añada una [etiqueta de tabla de IA](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) que nombre la columna, o asígnela en el entrenamiento.

## "Column name already exists"

Ya hay una columna con el mismo nombre técnico en la tabla. Si no aparece en la lista, es una columna predeterminada oculta: el mensaje dice *Please activate it in Table Column settings*. Desmarque *Hidden* en esa columna en lugar de crear una nueva.

## La aprobación está bloqueada por una columna obligatoria

El mensaje de la tabla nombra la columna. Rellene la celda en todas las filas o, si el valor no existe en este documento, desmarque *Is Required* para la columna, reinicie el documento e inténtelo de nuevo. Valore si la columna debería ser obligatoria (consulte [Buenas prácticas](best-practices-2.md)).

## La IA rellena una columna con el valor incorrecto

Caso típico: `CHARGES` recibe el total de línea y, entonces, todas las filas fallan la comprobación del total de línea con *Line total does not match quantity x unit price (expected …, got …)*, porque los cargos forman parte de la fórmula `cantidad × precio unitario + cargos`.

* Desmarque *Use AI* en la columna si las reglas entrenadas la capturan correctamente.
* Si el proveedor no tiene reglas, entrene la tabla una vez (Table training) para que la columna quede vinculada a la posición correcta, o oculte la columna si el proveedor nunca imprime ese valor.
* Como último recurso, *Skip table validation* en More Settings del tipo de documento desactiva todas las comprobaciones de tabla para todo el tipo de documento; entonces ya no se detecta la discrepancia, ni tampoco las columnas obligatorias vacías.

## PO matching: "Line Item Table is missing Mandatory column"

El PO matching necesita las columnas predeterminadas número de artículo, precio unitario, cantidad e importe total. Una de ellas está oculta o fue sustituida por una columna personalizada. Muestre la columna predeterminada o asigne el valor a ella en el entrenamiento de tablas.

## Un script o una exportación falla tras eliminar una columna

El script o el mapeo de exportación sigue haciendo referencia al *Column name* eliminado. Elimine la referencia o vuelva a añadir la columna con el mismo título; el nombre técnico se deriva del título y vuelve a coincidir.

## Dónde buscar más

* [Solución de problemas de extracción de tablas](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): calidad de extracción, OCR, E-Text
* [Campos de línea de entrenamiento / Entrenamiento de tabla](../../../../setup/document-training/training-line-fields-table-training/README.md)
