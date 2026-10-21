# Tarjetas de comparación de cotizaciones

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-4a7af1d99c73-es.png" alt="Tarjetas disponibles en la categoría seleccionada. Configure los campos antes de utilizarlas. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos."><figcaption><p>Tarjetas disponibles en la categoría seleccionada. Configure los campos antes de utilizarlas. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

Estas condiciones Y utilizan la cotización o los datos del artículo del proveedor disponibles en el documento. Configúrelos y pruébelos después de que se hayan cargado los datos de cotización requeridos. Un identificador de artículo coincidente no prueba por sí solo que su precio o unidad de medida sea correcto.

## Seleccione el cheque

| Tipo de tarjeta | Verificación y configuración |
| --- | --- |
| `CONDITION_QUOTES_ITEM_NUMBER_COMPARISON` | Comprueba el identificador del artículo con los datos del precio del artículo. Seleccione los campos de comparación y Cualquiera/Todos que ofrece la tarjeta. |
| `CONDITION_SPECIFY_SUPPLIER_TYPE` | Compara el tipo de proveedor de los datos de la cotización con `supplier_type`. Se trata de una verificación de clasificación de proveedores, no de una comparación de precios. |
| `CONDITION_QUOTE_SUPPLIER_ITEM_NUMBER_EXISTS` | Comprueba si el ID del artículo del proveedor está presente o no en los datos del precio del artículo; elija el operador y Cualquiera/Todos. Los datos faltantes de cotizaciones o artículos deben investigarse en el registro. |
| `CONDITION_QUOTE_PRICE_MATCH` | Compara un precio unitario con el precio del proveedor seleccionado: `ManagedPrice` o `LastPrice`. Elija Cualquiera/Todos y el operador de comparación numérica. Las líneas sin un número comparable en ambos lados se omiten y registran; si ninguna línea es comparable, la tarjeta informa que faltan datos del documento. |
| `CONDIITON_UNIT_OF_MEASURE_EQUAL` | Comprueba la unidad de medida con los datos relacionados. El tipo técnico contiene un error ortográfico retenido; no lo cambie en el JSON del flujo de trabajo almacenado. Un precio expresado por diferentes unidades necesita una atención especial. |
| `CONDITION_ITEM_QUOTES_TO_CONTRACTED_PRICE` | Compara precios cotizados y contratados. La versión 3 agrega Cualquiera/Todos; vea abajo. |

Las etiquetas visibles pueden diferir según la versión y el idioma de la interfaz de usuario. Seleccione mediante la verificación real, no solo por el nombre de la categoría. Por ejemplo, el precio del artículo cotizado puede aparecer en Lógica mientras que las otras comprobaciones de cotización aparecen en Comparar con precio de cotización.

## Precio del artículo cotizado: versión 3

Elija el operador de igualdad o desigualdad y si cualquier línea comparada o cada línea comparada debe satisfacerlo:

- `match_any`: una línea comparable exitosa es suficiente.
- `match_all`: cada línea comparada debe satisfacer el operador seleccionado.

La versión 2 conserva el comportamiento Todo. Una configuración Cualquiera/Todo no configurada en v3 vuelve a ser Todos y se registra. Una tarjeta sin líneas comparables informa que faltan datos; La ausencia de un precio no es prueba de igualdad o desigualdad. Inspeccione las líneas omitidas y el lado que falta en el registro.

Por ejemplo, dos líneas comparables producen resultados verdaderos y falsos para la igualdad. Cualquier pase; Todo falla. Con la desigualdad, el resultado de la comparación para cada línea cambia primero y luego Cualquiera/Todos combina esos resultados. No invierte el resultado final de Todos para implementar Cualquiera.

## Casos de prueba

Utilice los ID exactos de artículos y proveedores, la fuente de precios prevista y las unidades coincidentes. Pruebe que todas las líneas coincidan, obtendrá un resultado mixto, no hay precios comparables, faltan datos de cotización y una identificación de proveedor incorrecta. Verifique tanto el resultado de la comparación como las líneas que se omitieron. Mantener la aprobación o exportación detrás de los controles comerciales que realmente se requieren; una verificación exitosa del identificador no es una validación completa de la adquisición.

Consulte [Coincidencia de órdenes de compra](../and/compare-with-purchase-order/po-matching-complete-guide.md) para comparar comparaciones de órdenes de compra y [Registros de flujo de trabajo](../workflow-logs.md)] para solucionar problemas.
