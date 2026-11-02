# Gestión de cargos con Infor M3

## Descripción general

Este documento ofrece información detallada sobre cómo DocBits se integra con Infor M3 para gestionar los cargos asociados a facturas y órdenes de compra (PO). Incluye escenarios de cargos externos y las soluciones esperadas.

## Escenarios de gestión de cargos

| ID de escenario | Descripción                                                                          | Caso de negocio                                                                                                                        | Solución esperada                                                                                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1           | Cargos externos que no están en la PO pero sí en la factura (aceptados)              | Los cargos externos aparecen en la factura pero no figuran en la PO. Estos cargos se aceptan.                                          | Los cargos se contabilizarán con la regla contable PP20-228 según el elemento de coste enviado por DocBits.                                                                                                                               |
| 2           | Cargos externos que no están en la PO pero sí en la factura (no aceptados)           | Los cargos externos aparecen en la factura pero no figuran en la PO. Estos cargos no se aceptan ni se aprueban.                        | El valor total de la factura se registra con un cargo de cabecera por los cargos no aprobados. Además, se crea una nota de débito por estos cargos.                                                                                       |
| 3           | Cargos externos de la factura superiores o inferiores a los de la PO (dentro de la tolerancia) | Los cargos externos de la factura son superiores o inferiores a los de la PO, pero están dentro de la tolerancia aceptada.             | Los cargos adicionales se contabilizan con la regla contable PP20-228 según el elemento de coste enviado por DocBits.                                                                                                                     |
| 4           | Cargos externos de la factura superiores a los de la PO (fuera de la tolerancia, no aprobados) | Los cargos externos de la factura son superiores a los de la PO y están fuera de la tolerancia aceptada, y no están aprobados.        | La factura se registra con el importe total de la factura. Se añade un cargo adicional no aprobado como cargo de cabecera y se crea una nota de débito por este cargo adicional.                                                          |
| 5           | Cargos externos de la factura superiores a los de la PO (fuera de la tolerancia, aprobados en DocBits) | Los cargos externos de la factura son superiores a los de la PO y están fuera de la tolerancia aceptada, y están aprobados en DocBits. | Los cargos adicionales se contabilizan en PP20-228. Se consideran dos opciones:\<br>- Si la tolerancia de APS900 > DocBits, los cargos adicionales se contabilizan automáticamente.\<br>- Si la tolerancia de APS900 = DocBits, los cargos adicionales se contabilizan con nuevos elementos de cargo que no están en la PO. |
| 6           | Cargos externos de la factura inferiores a los de la PO (fuera de la tolerancia, no aprobados) | Los cargos externos de la factura son inferiores a los de la PO y están fuera de la tolerancia aceptada, y no están aprobados.        | La factura se contabiliza como no aprobada en APS110. El equipo de cuentas a pagar (AP) ajusta los cargos mediante la opción Invoice Control de APS110, que llama a APS360.                                                               |
| 7           | Cargos externos en la PO y ningún cargo en la factura                                | Los cargos externos figuran en la PO, pero no hay cargos en la factura.                                                                | La factura se contabiliza como no aprobada en APS110. El equipo de cuentas a pagar (AP) ajusta los cargos mediante la opción Invoice Control de APS110, que llama a APS360.                                                               |

## Ejemplo del escenario 5

| Campo          | Valor de la PO | Valor de la factura del proveedor |
| -------------- | -------------- | --------------------------------- |
| Línea 1        | $6000          | $6000                             |
| Flete (E001)   | $1000          | $3000                             |
| **Total**      | $7000          | $9000                             |

**Tolerancia del flete:** $100 aprobados automáticamente en M3 (APS900) y DocBits. Valor total de la factura de $9000 aprobado (con cargos) manualmente.

**APS451 (línea de factura):**

* Tipo de línea 1 (línea de factura): $9000
* Tipo de línea 5 (cargo de línea): $1000 (elemento: E001 para el flete de la PO de $1000)
* Tipo de línea 5 (cargo de línea): $2000 (elemento: E101 para el flete de la PO de $0)

### Campos y valores importantes para la gestión de cargos en DocBits

| Campo                       | Descripción                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| Sequence Number             | Identificador único de cada escenario de cargo                       |
| Costing Element ID          | Identificador del elemento de coste                                  |
| Costing Element Description | Descripción del elemento de coste                                    |
| Charge Type                 | Normalmente, "External"                                              |
| Charge Invoicing            | Hay que determinar su relevancia                                     |
| Distribution Method         | Método utilizado para distribuir los cargos                          |
| Gross Weight                | Aplicable si el peso bruto figura en la factura                      |
| Volume                      | Hay que definir los casos aplicables                                 |
| Net Amount                  | Hay que definir los casos aplicables                                 |
| 3rd Party Charge            | Presencia en la factura y requisitos de procesamiento                |
| Invoice Charge Quantity     | Requiere aclaración                                                  |
| Markup                      | Se asume que es la diferencia entre el cargo y el descuento          |
| Charge Category             | Hay que definir su relevancia                                        |
| Costing Operator            | Hay que definir su relevancia                                        |

\
