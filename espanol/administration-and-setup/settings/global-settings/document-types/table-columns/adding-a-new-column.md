# Añadir una nueva columna

Añada una columna cuando deba capturarse por línea un valor que las columnas predeterminadas no cubren: un centro de coste, un número de proyecto, un número de artículo interno.

## Antes de empezar

* Decida a qué **tabla** pertenece la columna. La mayoría de los tipos de documento tienen una tabla (por ejemplo, `INVOICE_TABLE`). Si la lista está vacía, haga clic primero en **Create new table**; el cuadro de diálogo solo pide un nombre de tabla.
* Decida el **tipo**: `AMOUNT` para dinero, `NUMBER` para cantidades, `DATE`, `BOOLEAN` para sí/no, `CURRENCY` para un código de moneda ISO y `STRING` para todo lo demás. El tipo no se puede cambiar después de guardar.
* Compruebe si ya existe una **columna predeterminada** con el mismo significado pero oculta. Las columnas ocultas aparecen en la lista con el indicador _Hidden_ activado; muéstrela en lugar de crear un duplicado.

## Pasos

1. Abra **Settings → Global Settings → Document Types → Table Columns**.
2. Haga clic en **Add new table column**.

<figure><img src="../../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Cuadro de diálogo Add new table column con Title, Is column required, Select column type y Select Table"><figcaption><p>Add new table column</p></figcaption></figure>

3. Rellene el cuadro de diálogo:

| Campo                   | Qué introducir                                                                                                                                                              |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Title**               | Etiqueta que ve el usuario en la pantalla de validación, por ejemplo `Cost Centre`. Solo letras y números. DocBits deriva de ella el _Column name_ técnico (`COST_CENTRE`). |
| **Is column required?** | Márquela cuando el documento no deba aprobarse mientras la columna esté vacía en alguna fila.                                                                               |
| **Select column type**  | Consulte la lista de tipos anterior.                                                                                                                                        |
| **Select Table**        | La tabla que recibe la columna.                                                                                                                                             |

4. Haga clic en **Proceed**. La columna aparece en la lista con _Read Only_, _Hidden_ y _Use AI_ sin marcar. Cambie esos indicadores en la lista si es necesario; consulte [Editar y eliminar columnas](editing-and-deleting-columns.md).

## Después de añadirla

* La columna está **vacía en los documentos existentes**. Se rellena en los documentos cargados o reiniciados después del cambio.
* En el caso de proveedores con **reglas entrenadas**, abra uno de sus documentos en el entrenamiento de tablas y asigne la nueva columna; de lo contrario, la columna permanece vacía para ese proveedor. Consulte [Defining tables and columns](../../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Con la **extracción de tablas con IA**, la IA rellena la columna si el valor es reconocible en el documento. Marque la columna con _Use AI_ si el proveedor tiene reglas entrenadas pero esta columna debe seguir procediendo de la IA.
* Añada la columna al **mapeo de exportación** si el ERP debe recibirla; consulte [Export](../../../document-processing/export/).

## Mensajes

| Mensaje                                                                    | Significado                                                                                                       |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| _Column name already exists_                                               | Ya hay una columna con este nombre técnico en la tabla. Elija otro título.                                        |
| _Column name already exists – Please activate it in Table Column settings_ | Una columna predeterminada oculta tiene este nombre. Desmarque su indicador _Hidden_ en lugar de crear una nueva. |
| _No table exists. Please create table before creating columns._            | El tipo de documento aún no tiene tabla: haga clic primero en **Create new table**.                               |
