# Ejemplos: precio y cantidad

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo del vídeo (versión de revisión):** [Seguir un documento](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## Ejemplo completo: extracción correcta, datos de Infor diferentes

Este es un caso ilustrativo, independiente de las capturas. La factura muestra **10 unidades a 10,00 € cada una**, total **100,00 €**. DocBits extrae los tres valores correctamente. El pedido de Infor importado muestra **10 unidades a 9,00 € cada una**, total **90,00 €**. Supongamos que las comprobaciones de coincidencia configuradas bloquean esta diferencia de precio.

1. **Compruebe la extracción:** compare la factura original con la cantidad, el precio unitario y el importe de línea extraídos. Coinciden, así que no hay un error de extracción demostrado para estos valores.
2. **Compruebe la fuente:** compare el pedido importado con el pedido actual de Infor, incluidos la unidad de precio y el momento de la importación. Una importación desactualizada y un pedido de Infor incorrecto requieren correcciones distintas.
3. **Aclare el valor de negocio:** en este ejemplo, compras confirma que se acordaron 10,00 € y corrige el pedido de Infor. Si el precio acordado hubiera sido 9,00 €, habría que aclarar la factura del proveedor.
4. **Verifique la importación corregida:** compruebe que los valores correctos del pedido han llegado realmente a DocBits antes de reintentar.
5. **Registre la acción de AP:** AP reinicia manualmente esta factura en DocBits; tras finalizar con éxito, es **AP assisted**. Una extracción correcta y un proceso no touchless pueden ser ciertos a la vez.
6. **Compruebe facturas posteriores:** verifique que la coincidencia y la exportación terminan ahora sin otra corrección ni reinicio. La factura ya intervenida sigue intervenida; las facturas posteriores aportan pruebas de la mejora.

{% hint style="warning" %}
No cambie un valor de 10,00 € extraído correctamente a 9,00 € solo para que coincida con un pedido incorrecto, ni amplíe una tolerancia únicamente para ocultar la discrepancia. Confirme el valor acordado y corrija los datos o la configuración responsables. Un bloqueo de coincidencia identifica dónde se detuvo el proceso, no quién lo causó.
{% endhint %}

Véase [Touchless Intelligence](./) para el ejemplo separado de calidad de extracción y el cálculo de AP touchless, y [Seguimiento del documento](touchless-document-trace.md) para las pruebas que comparar.

## Tres pedidos de demostración propios: valores coincidentes, precio y cantidad

Estos pedidos se crearon específicamente en **Dev**. El proveedor, el artículo y las facturas son ficticios. Cada factura contiene **10 unidades × 10 € = 100 € netos**. Las tarjetas contienen capturas reales de la interfaz en inglés y detalles numéricos ampliados. No muestran una conexión Infor de un cliente en producción, una extracción demostrada ni un proceso automático de facturas finalizado correctamente.

| Caso | Factura | Pedido importado | Qué establece la comparación |
| --- | --- | --- | --- |
| PO01 / RE01: valores coincidentes | 10 × 10 € = 100 € | 10 × 10 € = 100 € | Los valores de origen coinciden; Pure Touchless sigue necesitando una extracción correcta y una finalización confirmada sin intervención ni aprobación |
| PO02 / RE02: discrepancia de precio | 10 × 10 € = 100 € | 10 × 9 € = 90 € | Diferencia de 10 € en la línea; el precio unitario difiere en torno al 11,11 % respecto al precio del pedido. Las reglas activas reales deciden si bloquea |
| PO03 / RE03: discrepancia de cantidad | 10 × 10 € = 100 € | 8 × 10 € = 80 € | 2 unidades adicionales, el 25 % respecto a la cantidad pedida. Compruebe la cantidad abierta/recibida y la cantidad de comparación configurada |

<figure><img src="../../../.gitbook/assets/touchless-owned-po-match-es.png" alt="Tarjeta explicativa de FELLOW con el pedido de compra real de Dev PO01 en inglés, que muestra cantidad diez, precio unitario diez e importe cien"><figcaption><p>Valores coincidentes en el PO01 ficticio. La fila nativa ampliada muestra cantidad, precio unitario e importe. La coincidencia por sí sola no demuestra ni una extracción correcta ni Pure Touchless.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-es.png" alt="Tarjeta explicativa de FELLOW con el pedido de compra real de Dev PO02 en inglés, que muestra diez unidades a nueve y un importe de noventa frente a un importe de factura de cien"><figcaption><p>Ejemplo de precio PO02: el pedido importado muestra realmente 10 × 9 = 90, frente a 10 × 10 = 100 en la factura ficticia. Compruebe el precio acordado, la unidad de precio y la importación. Una intervención humana registrada seguida de una finalización correcta es AP Assisted.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-quantity-es.png" alt="Tarjeta explicativa de FELLOW con el pedido de compra real de Dev PO03 en inglés, que muestra ocho unidades a diez e importe ochenta, frente a diez unidades facturadas"><figcaption><p>Ejemplo de cantidad PO03: el pedido importado contiene 8 unidades y la factura 10. La cantidad recibida está vacía en esta prueba y no acredita ninguna entrega. Estas tarjetas explican la comparación; no demuestran una coincidencia correcta.</p></figcaption></figure>

## Páginas relacionadas

* [Touchless Intelligence](./)
* [Métricas y cálculo](touchless-metrics.md)
* [Usar el panel](touchless-dashboard.md)
* [Touchless Intelligence: Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Diagnóstico de la coincidencia con la OC](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Seguimiento del documento](touchless-document-trace.md)
* [Touchless Intelligence: Propuestas de cambio e informes](touchless-change-proposals.md)
* [Explicar y mejorar Touchless con MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
