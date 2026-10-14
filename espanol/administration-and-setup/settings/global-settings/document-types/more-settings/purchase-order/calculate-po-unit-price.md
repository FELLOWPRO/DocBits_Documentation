# Calcular el precio unitario de la orden de compra

## **Resumen**

Puede elegir calcular automáticamente el **precio unitario** de cada línea de orden de compra a partir del **importe** y la **cantidad** de la línea, en lugar de usar el precio unitario que viene con la orden de compra. Esto es especialmente útil cuando el precio unitario en la orden de compra (en Infor ERP / SAP) difiere del precio en el documento. Tales discrepancias pueden surgir si se aplica un descuento al precio unitario en la orden de compra, mientras que el documento solo aplica el descuento al importe neto.

## **Pasos para la activación**

1.  Navegue a **Configuración** -> **Configuración global** -> **Tipos de documento**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Seleccione el tipo de documento deseado y haga clic en **Más configuraciones**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  En la sección **Orden de compra**, active la opción **Calcular precio unitario de OC**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

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

Un importe neto que es **mayor** que el total de la línea no puede ser un importe neto, por lo que en ese caso se usa el total. Un `Precio unitario por` de 0 o vacío cuenta como 1.

{% hint style="info" %}
El precio calculado se escribe en la instantánea de la orden de compra que se almacena en el documento, y se **recalcula cada vez que el documento se concilia** (Conciliación automática de OC, conciliación manual, conciliación al guardar). Un documento que fue conciliado antes de cambiar la configuración, por lo tanto, toma el nuevo precio en su próxima conciliación — no es necesario recargar la orden de compra.
{% endhint %}

## Ejemplo:

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

En este caso, el precio unitario (sin el descuento) se extrae del documento, mientras que la orden de compra en el ERP almacena el precio unitario con el descuento aplicado. Esto resulta en una discrepancia en el precio unitario. Con la configuración activada, el precio unitario se toma del importe de la línea y la cantidad, por lo que ambas partes coinciden.

## Configuraciones relacionadas

* [Reglas de conciliación de órdenes de compra](purchase-order-matching-rules.md) — las reglas comparan el precio unitario **efectivo**, que es este precio calculado cuando la configuración está activada.
* [Configuración de tolerancia de órdenes de compra](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — cuánto puede desviarse el precio de la factura del precio calculado.