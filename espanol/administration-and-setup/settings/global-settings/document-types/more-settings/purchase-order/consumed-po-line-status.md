# Estado de la línea de pedido consumida

**Consumed PO line status** colorea las líneas de la orden de compra en la vista de coincidencia según la cantidad de cada línea que ya se ha casado. Actívelo para el tipo de documento de factura si su equipo necesita detectar rápidamente las líneas de OC sin usar, parcialmente usadas y totalmente usadas. El color es una ayuda visual; compruebe la **Matched Quantity** y la columna de cantidad de OC seleccionada antes de decidir si una línea puede volver a casarse.

## Activar la configuración

1. Abra **Configuración → Tipos de documento**. Localice el tipo de documento utilizado para sus facturas y seleccione el engranaje de su tarjeta para abrir **More Settings**. La captura muestra la tarjeta **Invoice**. Deje los interruptores **Activate** y **Extraction** como están.

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-document-types-en.png" alt="Página Document Types con la tarjeta Invoice y su engranaje More Settings"><figcaption><p>Abra More Settings desde la tarjeta Invoice.</p></figcaption></figure>

2. Expanda **Purchase Order** si está contraído. Localice **Consumed PO line status** y active su interruptor. Es una configuración independiente de **Update Document Purchase Order Status**, que se encuentra más abajo en la misma sección.

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-settings-en.png" alt="Sección Purchase Order de More Settings, con el interruptor Consumed PO line status visible"><figcaption><p>Elija el interruptor Consumed PO line status.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-toggle-en.png" alt="Vista cercana de la etiqueta y el interruptor Consumed PO line status"><figcaption><p>En este ejemplo el interruptor está desactivado; actívelo para mostrar los colores de coincidencia.</p></figcaption></figure>

3. Abra una factura con coincidencia de orden de compra e inspeccione sus líneas de OC. Los ejemplos siguientes muestran cómo se relacionan los colores de las líneas con el estado de coincidencia. Para conocer los pasos de la coincidencia, consulte [Coincidencia de órdenes de compra](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Interpretar los colores de las líneas de OC

| Aspecto | Significado | Qué comprobar |
| --- | --- | --- |
| Liso o blanco | Todavía no se ha casado ninguna cantidad de esta línea de OC. | Compruebe la cantidad de la OC y la línea de la factura antes de casar. |
| Tinte azul | Ha seleccionado la línea en la vista de coincidencia actual. | La selección es temporal; no significa que la línea esté totalmente casada. |
| Naranja pálido | Se ha casado parte de la cantidad, pero la cantidad casada es inferior a la cantidad de OC seleccionada. | Compruebe cuánta cantidad queda. |
| Violeta pálido | La cantidad casada es igual o superior a la cantidad de OC seleccionada. | No dé por hecho que hay más cantidad disponible. |

<figure><img src="../../../../../../.gitbook/assets/image (470).png" alt="Línea de OC con cantidad casada cero y sin color de estado"><figcaption><p>Todavía no se ha casado ninguna cantidad.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (472).png" alt="Línea de OC con un tinte azul de selección en la vista de coincidencia"><figcaption><p>La línea está seleccionada para la coincidencia actual.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/consumed_po_line_status.png" alt="Línea de OC con fondo naranja pálido y una cantidad casada inferior a la cantidad de la OC"><figcaption><p>La línea está parcialmente usada.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (473).png" alt="Línea de OC con fondo violeta pálido y una cantidad casada igual a la cantidad de la OC"><figcaption><p>La línea está totalmente usada.</p></figcaption></figure>

Una línea tachada tiene un significado distinto: su estado de OC puede estar excluido por los [estados de desactivación de OC](purchase-order-disable-statuses.md). Compruebe esa configuración si no se puede seleccionar una línea.
