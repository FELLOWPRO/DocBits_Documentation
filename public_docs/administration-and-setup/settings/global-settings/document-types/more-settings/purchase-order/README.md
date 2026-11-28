# Orden de compra

La tarjeta **Purchase Order** de **More Settings** de un tipo de documento controla cómo se comparan los documentos de ese tipo con los pedidos de compra. La configuración se aplica a un tipo de documento cada vez, así que abra primero el tipo de documento que desea cambiar en **Settings → Document Types**.

Para encontrar la configuración de una factura:

1. Abra **Settings → Document Types**.
2. Busque la tarjeta **Invoice** y seleccione su icono de engranaje (**More Settings**).
3. Abra la sección **Purchase Order** para revisar sus opciones de coincidencia y validación.

<figure><img src="../../../../../../.gitbook/assets/dbdc226228-invoice-card-en-20261030.png" alt="English Invoice document type card with the More Settings gear at the upper right"><figcaption><p>La tarjeta Invoice en el entorno de prueba Dev inglés actual. Use el icono de engranaje para abrir More Settings; los demás controles se aplican al tipo de documento.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/dbdc226-po-section-en-20261030.png" alt="Closed Purchase Order section labelled PO Matching and Validation"><figcaption><p>La sección Purchase Order en More Settings, mostrada cerrada. Despliegue su encabezado para ver las opciones; no se modificó ningún ajuste para esta captura.</p></figcaption></figure>

Empiece por las reglas de coincidencia y las tolerancias y después ajuste el comportamiento en torno a la coincidencia y la exportación:

* [Reglas de Coincidencia de Órdenes de Compra](purchase-order-matching-rules.md) y [Ajuste de tolerancias de órdenes de compra / Tolerancia adicional de órdenes de compra](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) definen cómo se comparan las líneas de factura y de pedido.
* [Opciones de Auto Match & Export](auto-match-and-export-options.md), [Exportar líneas de PO no coincidentes](export-not-matched-po-lines.md) y [Exportación alternativa](alternate-export.md) cubren lo que ocurre después de una coincidencia.
* [Cantidad exportada en la unidad de medida base](export-quantity-in-base-unit-of-measure.md) convierte la cantidad y el precio unitario exportados a la unidad de medida base, para la exportación a Infor LN.
* [Tabla de PO en el Constructor de Diseño](po-table-in-layout-builder.md), [Estado de la línea de pedido consumida](consumed-po-line-status.md) y [Calcular el precio unitario del pedido](calculate-po-unit-price.md) cambian lo que los usuarios ven en la vista de coincidencia.
* [Verificación automática de actualizaciones de OC](auto-check-for-po-updates.md), [Estados de pedidos excluidos de la conciliación](purchase-order-disable-statuses.md) y [Actualizar Estado de Orden de Compra de Documentos](update-document-purchase-order-status.md) controlan cómo se mantienen actualizados los datos y los estados del pedido de compra.
* [Mapa de Números de Artículos de Proveedores - Documentación para Administradores](supplier-item-number-map-admin-documentation.md) y la página general [Orden de compra](purchase-order.md) ofrecen más contexto.

La configuración puede afectar a documentos en producción. Compruebe los cambios con un documento de prueba antes de guardarlos en producción.

Esta descripción general muestra dónde encontrar la configuración. No verifica una coincidencia de PO ni una exportación completadas.
