# Comparaciones de PO: dirección, tolerancia y versiones de tarjeta

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-72e8f3204ac8-es.png" alt="Tarjetas disponibles en la categoría seleccionada. Configure los campos antes de utilizarlas."><figcaption><p>Tarjetas disponibles en la categoría seleccionada. Configure los campos antes de utilizarlas.</p></figcaption></figure>

Las tarjetas de comparación de PO comparan un lado elegido con un lado de referencia. La referencia determina la base para una tolerancia porcentual. Primero complete la conciliación de la orden de compra, luego seleccione la comparación, el operador, Cualquiera/Todo y la tolerancia solicitada por la tarjeta específica.

## Direcciones de comparación

| Opción almacenada | Lado comparado | Lado de referencia |
| --- | --- | --- |
| `po_document` | orden de compra | Documento |
| `received_document` | Datos recibidos | Documento |
| `po_received` | orden de compra | Datos recibidos |
| `document_po` | Documento | orden de compra |
| `document_received` | Documento | Datos recibidos |
| `received_po` | Datos recibidos | orden de compra |

El lado recibido se deriva de los datos del pedido de compra conciliado. Una comparación recibida en la tarjeta de precio unitario puede utilizar cantidades para obtener una cantidad comparable; no es una comparación directa de una cantidad con el precio de una moneda. Utilice los valores registrados por esa tarjeta en el registro al verificar el cálculo.

## Por qué es importante la dirección

Para una referencia de `100` y un valor comparado de `110`, una tolerancia porcentual de `5` corresponde a `5` alrededor de la referencia. Si el documento es la referencia y su valor es editable, cambiar el documento también cambia esa base de tolerancia. Elija la referencia deliberadamente, especialmente para la aprobación automática.

Al invertir los lados se invierte el orden de los operadores: `>` se convierte en `<`, `>=` se convierte en `<=` y viceversa. La igualdad y la desigualdad conservan su significado. No dé marcha atrás a un operador sin inspeccionar también los lados elegidos.

Las publicaciones que contienen el movimiento de migración de comparación afectaron a las tarjetas guardadas de `po_document` a `document_po`, y de `received_document` a `document_received`, al tiempo que se invierte el operador de pedido. Las versiones afectadas son la tolerancia de cantidad v4, la confirmación de pedido hasta el pedido v4 y el precio unitario v4/v5. El precio combinado de la diferencia de cantidad está excluido de esa migración de tarjeta guardada. Inspeccionar la configuración guardada y probar su resultado comercial después de un lanzamiento; no lo invierta manualmente por segunda vez.

## Versiones de tarjetas de precio unitario

| Versión | Configuración |
| --- | --- |
| v3 | Utiliza el comportamiento de comparación anterior. No asuma que expone los campos de dirección y tolerancia más nuevos. |
| v4 | Agrega la selección del lado de comparación. |
| v5 | Incluye Cualquiera/Todo, operador, cantidad de tolerancia, tipo de tolerancia y selección del lado de comparación. |

Elija una tolerancia absoluta para un importe fijo y una tolerancia porcentual para una variación relativa a la referencia seleccionada. Utilice el operador que ofrece la tarjeta; la igualdad exacta y estar dentro de una tolerancia son decisiones diferentes. No existe una tolerancia empresarial universal adecuada para cada proveedor o tipo de documento.

## Ejemplo de verificación

1. Utilice una referencia de orden de compra coincidente de `100` y el valor del documento `110`.
2. Seleccione Documento a orden de compra, una comparación dentro de la tolerancia cuando se ofrezca y `5` por ciento. Espere una comparación fuera de banda.
3. Pruebe el límite de tolerancia exacto, los valores en ambos lados y un PO coincidente que falta.
4. Con varias líneas, verifique Cualquiera versus Todos usando una línea de aprobación y otra de falla.
5. Inspeccione los valores comparados del registro, los lados seleccionados, el operador y la tolerancia, luego verifique la rama del flujo de trabajo resultante.

Una orden de compra inigualable, un valor no numérico y una condición comercial falsa son resultados diferentes. No trate los datos faltantes como una coincidencia exitosa. Para los cargos, utilice [Cualquier/Todos los cargos](../and/compare-with-purchase-order/any-all-charges.md), que explica por separado el comportamiento de los cargos faltantes y v2/v3.

Continúe con la [Guía de coincidencia de PO](../and/compare-with-purchase-order/po-matching-complete-guide.md) y la referencia de tarjeta individual para los campos restantes.
