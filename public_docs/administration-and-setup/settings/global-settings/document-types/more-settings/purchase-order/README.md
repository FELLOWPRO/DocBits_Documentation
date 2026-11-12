# Orden de compra

La tarjeta **Orden de compra** en **Más ajustes** de un tipo de documento controla cómo se comparan los documentos de ese tipo con las órdenes de compra. Los ajustes se aplican a un tipo de documento a la vez, así que abra primero el tipo de documento que desea cambiar en **Ajustes → Tipos de Documento**.

Para encontrar los ajustes de una factura:

1. Abra **Ajustes → Tipos de Documento**.
2. Busque la tarjeta **Factura** y seleccione su icono de engranaje (**Más ajustes**).
3. Abra la sección **Orden de compra** para revisar sus opciones de coincidencia y validación.

<figure><img src="../../../../../../.gitbook/assets/purchase-order-invoice-card-es-20261112.png" alt="Tarjeta Factura de un tipo de documento con el engranaje de Más ajustes arriba a la derecha"><figcaption><p>La tarjeta <strong>Factura</strong> en la versión actual de la sandbox en español. El engranaje abre Más ajustes; los demás controles de la tarjeta se aplican al tipo de documento.</p></figcaption></figure>

En la tarjeta también aparecen **Activar**, **Extracción** y los enlaces situados bajo el nombre del documento. Estos controles afectan al propio tipo de documento y se explican en la página [Tipos de documentos](../../README.md), en «Controles en una tarjeta de tipo de documento». Qué son las tarjetas plegables de Más ajustes se describe en [Más ajustes](../README.md).

<figure><img src="../../../../../../.gitbook/assets/purchase-order-po-section-es-20261112.png" alt="Sección Orden de compra cerrada con el subtítulo Coincidencia y validación de órdenes de compra"><figcaption><p>La sección <strong>Orden de compra</strong> en Más ajustes, cerrada. Abra su cabecera para ver las opciones; para esta captura no se cambió ningún ajuste.</p></figcaption></figure>

Empiece por las reglas de coincidencia y las tolerancias, y después ajuste el comportamiento tras una coincidencia y en la exportación:

* [Reglas de Coincidencia de Órdenes de Compra](purchase-order-matching-rules.md) y [Ajuste de tolerancias de órdenes de compra / Tolerancia adicional de órdenes de compra](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) definen cómo se comparan las líneas de factura y de orden de compra.
* [Opciones de Auto Match & Export](auto-match-and-export-options.md), [Exportar líneas de PO no coincidentes](export-not-matched-po-lines.md) y [Exportación alternativa](alternate-export.md) cubren lo que ocurre después de una coincidencia.
* [Tabla de PO en el Constructor de Diseño](po-table-in-layout-builder.md), [Estado de la línea de pedido consumida](consumed-po-line-status.md) y [Calcular el precio unitario del pedido](calculate-po-unit-price.md) cambian lo que los usuarios ven en la vista de coincidencia.
* [Verificación automática de actualizaciones de OC](auto-check-for-po-updates.md), [Estados de pedidos excluidos de la conciliación](purchase-order-disable-statuses.md) y [Actualizar Estado de Orden de Compra de Documentos](update-document-purchase-order-status.md) controlan cómo se mantienen actualizados los datos y los estados de las órdenes de compra.
* [Mapa de Números de Artículos de Proveedores - Documentación para Administradores](supplier-item-number-map-admin-documentation.md) y la página general [Orden de compra](purchase-order.md) ofrecen más contexto.

Los ajustes pueden afectar a documentos en curso. Compruebe los cambios con un documento de prueba antes de guardarlos en producción.

Esta descripción general muestra dónde se encuentran los ajustes. No confirma una coincidencia de OC ni una exportación ya realizadas.
