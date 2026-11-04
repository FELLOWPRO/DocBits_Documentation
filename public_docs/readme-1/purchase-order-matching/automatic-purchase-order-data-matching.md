# Coincidencia Automática de Datos de Órdenes de Compra

Docbits es un sistema avanzado diseñado para automatizar la coincidencia de datos de órdenes de compra (POs) con documentos de facturas entrantes. Esta herramienta está específicamente diseñada para la gestión eficiente y el procesamiento de datos de facturas dentro de los sistemas ERP. Esta documentación explica los conceptos básicos de la coincidencia automática a través de Docbits y define las reglas específicas necesarias para una coincidencia exitosa.

## **Principios Fundamentales de la Coincidencia Automática en Docbits**

**Extracción de Datos:** Docbits inicia el proceso extrayendo datos relevantes de los documentos de facturas digitalizadas. Típicamente, estos datos incluyen números de ítems, cantidades y precios unitarios de cada línea de factura. La precisión de esta extracción es crucial, ya que forma la base para el proceso de coincidencia posterior.

**Comparación con Datos de PO:** Los datos extraídos se comparan con la información correspondiente en las órdenes de compra almacenadas. Docbits verifica si los números de ítems, cantidades y precios coinciden con los de las PO. Para una coincidencia exitosa, los datos en las facturas deben corresponder a los datos en las órdenes de compra, considerando los umbrales de tolerancia definidos.

**Coincidencia Automática:** Basándose en los resultados de la comparación, Docbits realiza la coincidencia. El sistema verifica si los criterios de coincidencia se encuentran dentro de los límites de tolerancia establecidos. Si se cumplen estos criterios, la coincidencia se considera exitosa.

**Reportes:** Después de completar el proceso de coincidencia, Docbits genera informes que muestran el estado de las coincidencias. Estos informes informan sobre las facturas coincidentes exitosamente e identifican aquellas con discrepancias.

## **Definición de Reglas de Coincidencia**

**Número de Ítem:** El número de ítem en la factura debe coincidir exactamente con el número de ítem en la orden de compra. No se toleran desviaciones en los números de ítem.

**Cantidades:** La cantidad de bienes entregados en la factura puede variar dentro de un rango de tolerancia predefinido. Típicamente, una tolerancia de ±5% podría ser aceptable para tener en cuenta las diferencias menores en las cantidades de entrega.

**Precios:** Las desviaciones de precios son tolerables hasta un umbral establecido. Una tolerancia común podría ser de ±2% del precio para aceptar diferencias ligeras en las declaraciones de precios que surgen de diferencias de redondeo o fluctuaciones de moneda.

## **Estado de Coincidencia:**

* **Coincidencia Completa:** Todos los puntos de datos (número de ítem, cantidad y precio) se encuentran dentro de los límites de tolerancia establecidos.
* **Coincidencia Parcial:** Uno o más puntos de datos se desvían fuera de los límites de tolerancia, pero las desviaciones son mínimas y requieren una revisión manual.
* **Sin Coincidencia:** Desviaciones significativas en uno o más puntos de datos que requieren corrección inmediata o una investigación adicional.

La definición precisa de estas reglas y la configuración de los límites de tolerancia son cruciales para la eficiencia de la coincidencia automática y la reducción de intervenciones manuales. Docbits permite la configuración flexible de estos parámetros para satisfacer las necesidades de diversas empresas e industrias.
