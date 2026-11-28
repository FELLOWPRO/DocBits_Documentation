# Cantidad exportada en la unidad de medida base

El interruptor **Export quantity in base unit of measure** se encuentra en la sección **Purchase Order** de **More Settings** de un tipo de documento. Cambia la cantidad y el precio unitario que la exportación a Infor LN escribe para las líneas de pedido coincidentes.

Ábralo en **Settings → Document Types**, seleccione el icono de engranaje (**More Settings**) en la tarjeta del tipo de documento y despliegue **Purchase Order**.

## Qué hace el interruptor

* **Off:** DocBits exporta la cantidad y el precio unitario en la unidad de la factura.
* **On:** DocBits convierte la cantidad y el precio unitario de cada línea de pedido coincidente a la unidad de medida base de esa línea de pedido mediante su factor de conversión y escribe el código de la unidad base en lugar del código de la unidad facturada.

Una línea sin factor de conversión se exporta sin cambios, de modo que un factor ausente no bloquea la exportación.

{% hint style="info" %}
La conversión se aplica solo a la exportación a Infor LN. Los demás destinos de exportación conservan la unidad facturada.
{% endhint %}

## Cuándo usarlo

Active el interruptor cuando la instancia de Infor LN espere cantidades de pedido en la unidad de medida base. La conversión utiliza el factor almacenado en la línea de pedido, no un factor que DocBits calcule a partir del maestro de artículos.

La configuración puede afectar a documentos en uso. Compruebe el resultado con un documento de prueba antes de guardar el cambio en producción. El interruptor cambia los valores exportados; no cambia cómo se comparan las líneas de factura y de pedido.

## Páginas relacionadas

* [Orden de compra](README.md)
* [Exportar líneas de PO no coincidentes](export-not-matched-po-lines.md)
* [Exportación alternativa](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
