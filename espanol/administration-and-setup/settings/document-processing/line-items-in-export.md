# Líneas de detalle en la exportación

Lo que ocurre con la tabla de líneas de detalle cuando un documento se aprueba y se exporta depende del método de exportación. Esta página explica qué columnas salen de DocBits, cuáles son obligatorias y por qué una exportación puede mostrar menos líneas que la pantalla de validación.

## Dos tipos de exportación

| Método de exportación | Qué se envía de la tabla |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | La tabla tal como está en la pantalla de validación: todas las [columnas de tabla](../global-settings/document-types/table-columns.md) no ocultas de todas las filas, con valor, valor formateado y confianza. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (BOD de Infor ERP / SAP) | No la tabla en bruto. DocBits construye a partir de ella **líneas de recepción** y **líneas de coste** (ver más abajo) y las asigna a los campos del BOD con el mapeo configurado en [Exportación a INFOR](../../../infor-integration-and-configuration/exporting-to-infor/README.md). |

## Líneas de recepción y líneas de coste (exportaciones a Infor)

Una línea de factura en el ERP es o bien una **línea de recepción**, que liquida una recepción de orden de compra, o bien una **línea de coste**, que contabiliza un importe en una cuenta contable con dimensiones. DocBits lo decide por cada línea de la factura:

* Las **líneas de recepción** proceden de la **coincidencia de PO**. Cada línea de factura que se ha emparejado con una línea de PO (Panel → PO Match, o automáticamente con *PO auto match*) se convierte en una línea de recepción que lleva el número de PO, la línea de PO, la línea de recepción y la cantidad y el importe emparejados. Una factura sin coincidencia de PO **no tiene líneas de recepción**; la vista previa de la exportación muestra entonces `receipt_lines: []`, lo cual es correcto y no un error.
* Las **líneas de coste** proceden del **registro contable** que crea el paso de contabilidad de costes (o Auto Accounting): cuenta contable, dimensiones, importe y cantidad por línea. Una factura sin registro contable no tiene líneas de coste.
* Las **líneas de impuestos** se construyen a partir de los importes de impuestos de la cabecera, no de la tabla.

Por tanto, en las exportaciones a Infor, la tabla de líneas de detalle es la *entrada* para la coincidencia de PO y la contabilidad; lo que recibe el ERP es el resultado de esos dos pasos. Una línea que no está ni emparejada con una PO ni contabilizada no llega al ERP.

{% hint style="warning" %}
Para que la coincidencia de PO funcione, la tabla debe tener las columnas predeterminadas **número de artículo, precio unitario, cantidad e importe total**. Si una de ellas está oculta, la pantalla de validación muestra *Line Item Table is missing Mandatory column for PO* y no se pueden construir líneas de recepción.
{% endhint %}

## Columnas obligatorias y el cuadro de diálogo de aprobación

Antes de que un documento pueda aprobarse, DocBits comprueba la tabla:

1. Toda columna marcada como **Obligatoria** (*Is Required*, en Configuración → Tipos de documentos → Columnas de tabla) debe tener un valor en todas las filas.
2. Toda fila debe superar la **comprobación del total de línea**: `total = cantidad × precio unitario + cargos − descuento` con una tolerancia de 0,02. Las filas que fallan se marcan; el mensaje indica el valor esperado y el real.
3. La **suma de los totales de línea** se compara con el importe neto de la cabecera. Una diferencia es una advertencia y no bloquea la aprobación.

El cuadro de diálogo de aprobación lista lo que todavía falta. Un administrador puede desactivar todas las comprobaciones de tabla por tipo de documento con **Omitir validación de tabla** (*Skip table validation*, en Tipos de documentos → Más ajustes); los totales de línea y las columnas obligatorias dejan entonces de comprobarse, mientras que las comprobaciones de cabecera se mantienen.

Detalles de los mensajes: [Solución de problemas de extracción de tablas](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md#mensajes-en-la-tabla).

## Tabla vacía

* Las **exportaciones JSON / XML** envían el documento con `tables: []` (o la tabla con cero filas). El sistema receptor debe saber manejar una tabla vacía.
* Las **exportaciones a Infor** sin líneas de recepción ni líneas de coste envían solo la cabecera y las líneas de impuestos. La mayoría de los ERP rechazan una factura sin líneas; configura Auto Accounting o una línea de coste predeterminada para esos tipos de documento, o dirígelos a otra exportación.
* Un tipo de documento **sin tabla** (ninguna tabla configurada) nunca envía datos de líneas; es lo esperado en tipos de documento como las confirmaciones de pedido, que se emparejan a nivel de cabecera.

## Comprobar antes de aprobar

Los partners y el soporte con acceso a la API o al MCP pueden solicitar la carga útil de la exportación de un documento antes de enviarla: la herramienta MCP `get_export_preview(doc_id)` devuelve exactamente lo que la exportación va a enviar: `receipt_lines`, `cost_lines` y `tax_lines` en las exportaciones a Infor, `tables` en las exportaciones JSON. Úsala cuando el ERP informe de líneas que faltan: si `receipt_lines` está vacío, la factura no se emparejó con una PO; si `cost_lines` está vacío, no existe registro contable.

## Páginas relacionadas

* [Exportar](export.md): configuraciones y métodos de exportación
* [Columnas de tabla](../global-settings/document-types/table-columns.md)
* [Exportación a INFOR](../../../infor-integration-and-configuration/exporting-to-infor/README.md): mapeos de campos del BOD para líneas de recepción, de coste y de impuestos
