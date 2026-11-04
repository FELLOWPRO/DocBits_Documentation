# Configuración de Orden de Envío de PO

## **Resumen**

La sección de **Orden de Envío de PO** proporciona un desglose del estado de entrega y facturación de los elementos de la Orden de Compra coincidentes. Esta sección aparece dentro de la pantalla de **Coincidencia de Orden de Compra** cuando la función está habilitada.

## **Cómo Habilitar**

Para activar esta función:

1. Ve a **Ajustes** → **Módulo**.
2. Abre la sección **Orden de compra** (*Coincidencia y validación de órdenes de compra*).
3.  Activa la opción **PO Orden de envío**.

    <div align="left"><figure><img src="../../../../.gitbook/assets/po-shipment-order-module-setting-es.png" alt="Sección Orden de compra en Ajustes → Módulo con el interruptor PO Orden de envío" width="563"><figcaption><p>Ajustes → Módulo → Orden de compra</p></figcaption></figure></div>

Esta misma sección incluye otros dos interruptores: **Cuadro de mandos PO** añade a la navegación un cuadro de mandos de órdenes de compra, y **Panel de órdenes de envío** añade un panel que lista las entregas entrantes por posición de la orden de compra.

## **Dónde Aparece**

Una vez habilitada, la sección de PO Orden de envío se hace visible en la interfaz de Coincidencia de Orden de Compra.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2R9tB3JySdIMk8meRSVZ%252FPO-Shipment-Order-1.jpg%3Falt%3Dmedia%26token%3D70aa50f4-84cd-4a55-b580-037b893d1f5b\&width=768\&dpr=4\&quality=100\&sign=e4619335\&sv=2)

### **PO Orden de envío – Descripción de Campos**

* **ID de Artículo** Identifica el artículo específico en la orden de compra.
* **Número de Entrega** Número de referencia para el envío o entrega.
* **Cantidad Enviada** Cantidad que ha sido entregada o recibida.
* **Cantidad Facturada** Cantidad que ya ha sido facturada.
* **Cantidad Abierta en Factura** Cantidad aún pendiente de facturación (calculada como _Cantidad Enviada - Cantidad Facturada_).
* **Barra de Progreso y Porcentaje**
  * Muestra cuánto de la cantidad enviada ha sido coincidente con facturas.
  * Comienza en 0% para nuevas POs.
  * Se actualiza acumulativamente a través de múltiples facturas.
  * Refleja el progreso total de artículos facturados vs. enviados.
* **Fecha de Entrega Prometida** La fecha de entrega esperada para el artículo de la PO.
*   **Indicador de Retraso**

    Muestra el número de días que la entrega se retrasa según la **Fecha de Entrega Prometida**.
