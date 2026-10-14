# And: elegir una tarjeta de condición

Utilice una tarjeta **And** para decidir si un flujo de trabajo debe continuar después de su disparador **When**. Añada las comprobaciones que necesite antes de la acción **Then**. Cada tarjeta muestra campos que hay que rellenar, como **Operator**, **Field Name** o **Value**; las capturas de pantalla muestran las plantillas de tarjeta disponibles, no reglas ya completadas.

En el **Workflow Builder**, seleccione **Add Card** bajo **And...**. Elija una categoría a la izquierda o escriba el nombre de una tarjeta en **Search Card**. Seleccione la vista previa de una tarjeta para añadirla al flujo de trabajo. Puede desplazarse por la lista de vistas previas para ver más tarjetas. Utilice **×** para cerrar el selector sin elegir otra tarjeta. Después de configurar las tarjetas, guarde el flujo de trabajo. Consulte [Workflow](../README.md) para ver los pasos **When**, **And** y **Then** que lo rodean.

## Compare with Purchase Order

Utilice estas tarjetas para comparar datos de un pedido o de una factura con una orden de compra, como el precio unitario, la fecha de entrega prometida, los cargos o la cantidad. Elija los campos, el operador y la tolerancia que solicite la tarjeta seleccionada. Consulte [Compare with Purchase Order](compare-with-purchase-order/README.md) para ver cada tarjeta.

<figure><img src="../../../.gitbook/assets/and-category-po-comparison-en.png" alt="Selector de tarjetas And en inglés con Compare with Purchase Order seleccionado; las vistas previas visibles incluyen comparaciones de precio unitario, fecha de entrega, cargos y cantidad."><figcaption>Categoría Compare with Purchase Order en el Sandbox en inglés.</figcaption></figure>

## Document Field

Elija esta categoría para comprobar una casilla de verificación o el estado de un campo, comparar un campo con un valor o comparar dos campos. Rellene los marcadores **Field Name** y **Operator** de la tarjeta elegida. Algunas comparaciones también solicitan una tolerancia. Consulte [Document Field](document-field/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-field-en.png" alt="Selector de tarjetas And en inglés con Document Field seleccionado; las vistas previas visibles comprueban una casilla de verificación, el estado de un campo, valores de campo y comparaciones de dos campos."><figcaption>Las comprobaciones de Document Field usan valores del documento actual.</figcaption></figure>

## Date & Time

Utilice **Date & Time** para comparar una fecha o una hora con un intervalo, o para comparar **Today** con una fecha elegida. Seleccione el **Operator** y los valores de fecha en la tarjeta. Consulte [Date & Time](date-and-time/README.md).

<figure><img src="../../../.gitbook/assets/and-category-date-time-en.png" alt="Selector de tarjetas And en inglés con Date & Time seleccionado; dos vistas previas comparan una fecha o una hora con un intervalo y comparan Today con una fecha."><figcaption>Date & Time ofrece una comprobación de intervalo y una comprobación frente a la fecha de hoy.</figcaption></figure>

## Document

Utilice estas tarjetas cuando un flujo de trabajo deba depender del **tipo de documento** o de la **suborganización**. Elija el tipo o la organización que indica la tarjeta. Consulte [Document](document/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-en.png" alt="Selector de tarjetas And en inglés con Document seleccionado; las vistas previas comprueban el tipo de documento y la pertenencia a una suborganización."><figcaption>Las condiciones de Document comprueban el tipo o la suborganización.</figcaption></figure>

## Logic

Esta categoría incluye comprobaciones mediante una tabla de decisión, una respuesta HTTPS, la disponibilidad de un módulo, un precio cotizado de un artículo, un valor de probabilidad o dos valores. Abra la tarjeta concreta y rellene sus marcadores; por ejemplo, la tarjeta HTTPS solicita una URL, un método y un código de estado aceptado. Consulte [Logic](logic/README.md).

<figure><img src="../../../.gitbook/assets/and-category-logic-en.png" alt="Selector de tarjetas And en inglés con Logic seleccionado; las vistas previas incluyen tarjetas de tabla de decisión, solicitud HTTPS, módulo activo, precio cotizado, probabilidad y comparación de valores."><figcaption>Logic ofrece varios tipos de condición; elija el que corresponda a su regla.</figcaption></figure>

## Status

Utilice **Status** para comprobar si un documento tiene un estado elegido o si su estado está dentro de un conjunto seleccionado. Elija el **Operator** y el **Status** en la tarjeta. Consulte [Status](status/README.md).

<figure><img src="../../../.gitbook/assets/and-category-status-en.png" alt="Selector de tarjetas And en inglés con Status seleccionado; dos vistas previas comparan el estado del documento con un estado o con un conjunto de estados."><figcaption>Las condiciones de Status comprueban el estado actual del documento.</figcaption></figure>

## Table

Estas tarjetas examinan las filas de las tablas del documento. Las opciones visibles incluyen comprobaciones de fecha, patrones de texto, vida útil y comparaciones entre columnas. Seleccione el **Table name** y el **Column Name** antes de elegir un operador o un patrón. Consulte [Table](table/README.md).

<figure><img src="../../../.gitbook/assets/and-category-table-en.png" alt="Selector de tarjetas And en inglés con Table seleccionado; las vistas previas visibles incluyen fecha, patrón regex, vida útil y comparaciones de columnas de tabla."><figcaption>Las condiciones de Table usan filas y columnas de una tabla del documento.</figcaption></figure>

## Compare with Quote Price

Utilice estas tarjetas para comparar un artículo con datos de precios cotizados. Las opciones visibles cubren el ID de artículo, el tipo de proveedor, el ID de artículo del proveedor, el precio unitario y la unidad de medida. El **Operator** y los marcadores de datos dependen de la tarjeta que seleccione.

<figure><img src="../../../.gitbook/assets/and-category-quote-price-en.png" alt="Selector de tarjetas And en inglés con Compare with Quote Price seleccionado; cinco vistas previas cubren el ID de artículo, el tipo de proveedor, el ID de artículo del proveedor, el precio unitario y la unidad de medida."><figcaption>Compare with Quote Price es una categoría independiente en el selector de tarjetas actual.</figcaption></figure>

## Assignee

Utilice **Assignee** cuando la condición dependa del usuario o del grupo asignado. Elija si desea comparar con un usuario o grupo o con un conjunto seleccionado. Consulte [Assignee](assignee/README.md).

<figure><img src="../../../.gitbook/assets/and-category-assignee-en.png" alt="Selector de tarjetas And en inglés con Assignee seleccionado; las vistas previas comparan el usuario o grupo asignado con una o varias opciones."><figcaption>Las condiciones de Assignee comprueban el usuario o grupo asignado al documento.</figcaption></figure>
