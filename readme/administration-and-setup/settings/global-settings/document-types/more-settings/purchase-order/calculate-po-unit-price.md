# Calcular el precio unitario del pedido

## **Resumen**

Puede elegir calcular automáticamente el **precio unitario** de cada línea de orden de compra a partir del **importe** y la **cantidad** de la línea, en lugar de usar el precio unitario que viene con la orden de compra. Esto es especialmente útil cuando el precio unitario en la orden de compra (en Infor ERP / SAP) difiere del precio en el documento. Tales discrepancias pueden surgir si se aplica un descuento al precio unitario en la orden de compra, mientras que el documento solo aplica el descuento al importe neto.

## Encontrar el ajuste

1. Abra **Ajustes → Tipos de Documento** y el engranaje del tipo correspondiente.

<figure><img src="../../../../../../.gitbook/assets/site-extra-document-types-es.png" alt="Tipos de documentos predeterminados con enlaces a Campos y engranajes de configuración. No se modificó ningún interruptor Activar o Extracción."><figcaption><p>Tipos de documentos predeterminados con enlaces a Campos y engranajes de configuración. No se modificó ningún interruptor Activar o Extracción.</p></figcaption></figure>

2. Despliegue **Orden de compra** y localice **Calcular el precio unitario del pedido**.

<figure><img src="../../../../../../.gitbook/assets/site-complete-invoice-po-settings-es.png" alt="Configuración actual de Orden de compra, incluido Calcular el precio unitario del pedido. Los valores privados están ocultos; no se cambió la configuración ni se ejecutó una conciliación."><figcaption><p>Configuración actual de Orden de compra, incluido Calcular el precio unitario del pedido. Los valores privados están ocultos; no se cambió la configuración ni se ejecutó una conciliación.</p></figcaption></figure>

Revise el efecto de la configuración antes de cambiarla. Para la imagen no se modificó el interruptor ni se ejecutó una conciliación.

## Cómo se calcula el precio

Una vez activada la configuración, el precio unitario de una línea de orden de compra se calcula como:

**`Precio unitario = Importe de línea ÷ Cantidad × Precio unitario por`**

donde el **importe de línea** se elige así:

| La línea de orden de compra contiene                                                           | Importe de línea usado                 |
| ---------------------------------------------------------------------------------------------- | ------------------------------------ |
| un **importe neto** (`extended_amount`) que es mayor que 0 y no supera el total de la línea    | el importe neto                       |
| no hay importe neto, o el importe neto supera el total de la línea                             | el **total** de la línea (`total_amount`) |
| no hay importe positivo, o no hay cantidad positiva                                           | no se calcula nada, el precio de OC se mantiene |

Por qué el importe neto viene primero: las fuentes ERP (Infor BODs) envían el importe neto de la línea como `extended_amount` y llevan **impuestos y cargos adicionales** en `total_amount`. Dividir un total con impuestos por la cantidad da un precio unitario bruto, y cada factura que se valora neta entonces aparece como _precio unitario subestimado_ aunque sea correcto. Ejemplo de una línea real de orden de compra: cantidad 9, importe neto 879.84, total 954.63 (8.5 % de impuesto) — el precio basado en neto es 97.76 y coincide con la factura; el precio basado en total sería 106.07.

Si el importe neto es **mayor** que el total de la línea, esta regla utiliza el total. Un `Precio unitario por` de 0 o vacío cuenta como 1.

{% hint style="info" %}
El precio calculado se escribe en la instantánea de la orden de compra que se almacena en el documento, y se **recalcula cada vez que el documento se concilia** (Conciliación automática de OC, conciliación manual, conciliación al guardar). Un documento que fue conciliado antes de cambiar la configuración, por lo tanto, toma el nuevo precio en su próxima conciliación — no es necesario recargar la orden de compra.
{% endhint %}

## Ejemplo:

En este caso, el precio unitario (sin el descuento) se extrae del documento, mientras que la orden de compra en el ERP almacena el precio unitario con el descuento aplicado. Esto resulta en una discrepancia en el precio unitario. Con la configuración activada, la regla utiliza el importe y la cantidad de la línea para obtener el precio efectivo. Compruebe las unidades, la base de precio y las tolerancias: el cálculo no garantiza por sí solo una coincidencia.

## Configuraciones relacionadas

* [Reglas de conciliación de órdenes de compra](purchase-order-matching-rules.md) — las reglas comparan el precio unitario **efectivo**, que es este precio calculado cuando la configuración está activada.
* [Configuración de tolerancia de órdenes de compra](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — cuánto puede desviarse el precio de la factura del precio calculado.

Ejemplo con cantidad 9 y base de precio 1: 879,84 ÷ 9 × 1 = 97,76 de precio unitario neto. Un total de 954,63 con el 8,5 % de impuesto produce 106,07. Compare una factura con precios netos usando el importe neto.
