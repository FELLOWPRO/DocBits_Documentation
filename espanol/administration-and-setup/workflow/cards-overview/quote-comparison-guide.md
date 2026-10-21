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






<!-- workflow-card-complete-example-20261021 condition_quotes_item_number_comparison -->

### Ejemplo de comparación de número de artículo

**Configuración:** Prepare dos líneas de cotización comparables: el artículo del proveedor `DEMO-S1` se asigna al artículo `DEMO-I1` en ambos lados; El artículo del proveedor `DEMO-S2` tiene el artículo de documento `DEMO-I2` y el artículo de matriz `DEMO-I9`. Elija igualdad y `match_all`.

**Resultado esperado y contraejemplo:** El resultado de la condición es falso con `match_all`, porque un número de artículo comparable difiere. El resultado es verdadero con `match_any`, porque el primer número de artículo coincide. La búsqueda utiliza el número de artículo del proveedor. Una entrada de matriz sin un número de artículo se omite y se registra; si ninguna línea es comparable, el resultado de la condición es falso. Un registro de intervalo de fechas por sí solo no es una condición de validez independiente.

Esta es una configuración de prueba ilustrativa y el resultado esperado; no fue ejecutado. Utilice datos y destinatarios configurados en su organización de prueba.

<!-- workflow-card-complete-example-20261021 condition_quote_supplier_item_number_exists -->

### Ejemplo de existencia de artículo de proveedor

**Configuración:** El documento tiene números de artículo de proveedor `DEMO-S1` y `DEMO-S2`; los datos cargados del precio del artículo del proveedor contienen solo `DEMO-S1`. Elija el operador de presencia y `match_all`.

**Resultado esperado y contraejemplo:** El resultado de la condición es falso con `match_all` y verdadero con `match_any`. Con el operador de ausencia, la segunda línea es un resultado de ausencia positivo. La existencia no prueba que el precio del artículo, la unidad o la clasificación del proveedor sean correctos. Cargue primero los datos de cotización válidos e inspeccione los errores de datos faltantes.

Esta es una configuración de prueba ilustrativa y el resultado esperado; no fue ejecutado. Utilice datos y destinatarios configurados en su organización de prueba.

<!-- workflow-card-complete-example-20261021 condition_quote_price_match -->

### Ejemplo de precio de proveedor

**Configuración:** Para dos líneas coincidentes, elija `ManagedPrice`, igualdad y `match_all`. Los precios de los documentos son `10` y `12`; los precios gestionados correspondientes son `10` y `13`, en monedas y unidades coincidentes.

**Resultado esperado y contraejemplo:** El resultado de la condición es falso con `match_all` y verdadero con `match_any`. El cambio a `LastPrice` utiliza una fuente diferente y debe probarse de forma independiente. Una línea sin un precio numérico comparable se omite y se registra; si ninguna línea es comparable, la tarjeta informa que faltan datos del documento, no igualdad.

Esta es una configuración de prueba ilustrativa y el resultado esperado; no fue ejecutado. Utilice datos y destinatarios configurados en su organización de prueba.

<!-- workflow-card-complete-example-20261021 condition_specify_supplier_type -->

### Ejemplo de clasificación de proveedores

**Configuración:** Elija el tipo de proveedor `Contract`. Prepare dos entradas de cotización-proveedor cargadas con `managed_class` igual a `contract`.

**Resultado esperado y contraejemplo:** La condición es verdadera cuando cada entrada cargada tiene esa clasificación. La condición es falsa si una entrada tiene la clasificación `managed`. El valor `Nonmanaged` seleccionable se normaliza a `unmanaged` por el backend. Esta clasificación no tiene relación con una forma jurídica de proveedor. Los datos de cotización que faltan no coinciden.

Esta es una configuración de prueba ilustrativa y el resultado esperado; no fue ejecutado. Utilice datos y destinatarios configurados en su organización de prueba.

<!-- workflow-card-complete-example-20261021 condiiton_unit_of_measure_equal -->

### Ejemplo de unidad de medida

**Configuración:** Prepare líneas de oferta vinculadas con la unidad del documento `EA` y la unidad de comparación del proveedor `EA`. Seleccione igualdad y `match_all`. Mantenga la versión de tarjeta que está probando.

**Resultado esperado y contraejemplo:** La condición es verdadera para unidades comparables coincidentes; una segunda fila comparable que usa `KG` en lugar de `EA` hace que la condición sea falsa con `match_all`. Las unidades de comparación que faltan se omiten y registran; si ninguno es comparable, la tarjeta informa que faltan datos. La versión 3 puede aplicar la asignación de unidades configurada, así que verifique esa asignación por separado. Los precios de igualación por sí solos no establecen unidades de igualación.

Esta es una configuración de prueba ilustrativa y el resultado esperado; no fue ejecutado. Utilice datos y destinatarios configurados en su organización de prueba.
