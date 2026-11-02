# Descripción de la estructura EDI

El objetivo principal del descriptor de estructura es delinear los elementos de un mensaje EDI de manera lógica y organizada, facilitando la gestión y análisis de los datos. Reflejando con precisión la jerarquía del mensaje.

### Elementos del descriptor de estructura

**N1** – Contiene los siguientes campos:

* **N1** – Nombre o Identificador de la entidad (por ejemplo, parte, organización).
* **N2** – Información adicional de nombre (generalmente un nombre secundario para la entidad).
* **N3** – Información de dirección (típicamente la dirección postal).
* **N4** – Ubicación geográfica (ciudad, estado, código postal, país).

**N9** – Contiene el siguiente campo:

* **N9** – Identificador de referencia (por ejemplo, número de orden de compra o número de control).
* **Bucles:**
  * **MSG01** – Contiene el siguiente campo:
    * **MSG01** – Texto de mensaje de forma libre (generalmente una nota o instrucción especial relacionada con la transacción).

**IT1** – Contiene los siguientes campos:

* **IT1** – Identificador de ítem de línea (por ejemplo, número de ítem o código de producto).
* **QTY** – Cantidad del ítem en la transacción (por ejemplo, unidades ordenadas o enviadas).
* **TXI** – Información de impuestos (por ejemplo, tasas de impuestos, cantidades o clasificaciones para el ítem).
* **REF** – Información de referencia (por ejemplo, número de lote, número de serie u otros identificadores relacionados con el ítem).
* **Bucles:**
  * **SAC** – Puede repetirse y contiene los siguientes campos:
    * **SAC** – Información de servicio, promoción, descuento o cargo (por ejemplo, costos adicionales o descuentos relacionados con el ítem).
    * **TXI** – Información de impuestos relacionada con SAC (por ejemplo, impuestos sobre cargos o descuentos).

**SAC** – Contiene los siguientes campos:

* **SAC** – Información de servicio, promoción, descuento o cargo (puede usarse de forma independiente o dentro del bucle IT1 para representar cargos/descuentos adicionales).
* **TXI** – Información de impuestos relacionada con SAC (por ejemplo, impuestos sobre cargos o descuentos).

### Aquí tienes el ejemplo completo de un descriptor de estructura en formato JSON:

```
{
    "N1": {
        "fields": [
            "N1",  
            "N2",   
            "N3",   
            "N4"    
        ]
    },
    "N9": {
        "fields": [
            "N9"    
        ],
        "loops": {
            "MSG01": {
                "fields": [
                    "MSG01"   
            }
        }
    },
    "IT1": {
        "fields": [
            "IT1",   
            "QTY",   
            "TXI",   
            "REF"    
        "loops": {
            "SAC": {
                "fields": [
                    "SAC",   
                    "TXI"    
        }
    },
    "SAC": {
        "fields": [
            "SAC",   
            "TXI"    
        ]
    }
}
```
