# Gestor de Reglas

\


Este documento proporciona una explicación detallada de las reglas de resolución de conflictos utilizadas en el sistema de facturación DocBits. Estas reglas están diseñadas para manejar automáticamente las discrepancias entre los detalles de la factura y los datos de la orden de compra (PO), asegurando una reconciliación financiera precisa. El sistema aplica estas reglas para procesar líneas de factura, cargos e impuestos, y genera ajustes o notas apropiadas cuando es necesario.

## Estructura de las Reglas

### &#x20;1. Metadatos

• versión: Identifica la versión del archivo de mapeo.

• revisión: Número de revisión para rastrear cambios.

• autor: Indica el creador del archivo de mapeo.

• descripción: Una breve descripción del propósito del archivo.

• created\_at & updated\_at: Tiempos de creación y última actualización del archivo.

### &#x20;2. Configuración de Exportación

La sección de configuración de exportación define el mapeo entre los campos de datos en el sistema y los campos correspondientes en los archivos de exportación.

• Encabezado: Define los campos de encabezado para los datos de factura exportados.

• Líneas de Impuesto: Especifica los campos para los elementos de línea de impuesto en la exportación.

• Cargos de Encabezado de Orden: Mapea campos relacionados con cargos adicionales a nivel de encabezado de orden.

• Líneas de Recibo: Mapea campos para elementos de línea individuales en un recibo.

• Cargos de Línea de Orden: Define los campos para cargos relacionados con líneas de orden específicas.

• Líneas de Costo: Especifica campos para líneas de asignación de costos.

• Nota de Débito & Nota de Crédito: Define campos para generar notas de débito y crédito en casos de discrepancias.

### 3. Reglas de Resolución de Conflictos

Estas reglas manejan discrepancias entre los datos de la factura y los datos correspondientes de la PO. Cada regla se compone de varios componentes:

• Nombre: El nombre descriptivo de la regla, que indica el tipo de discrepancia que aborda.

• Sección: Indica qué parte de la factura (por ejemplo, receipt\_lines, line\_charges) se aplica la regla.

• Activo: Valor booleano (verdadero o falso) que indica si la regla está actualmente activa.

• Criterios de Coincidencia: Condiciones que activan la regla basadas en comparaciones entre los datos de la factura actual y los datos esperados de la PO.

• Acciones: Define lo que el sistema debe hacer cuando se activa la regla, incluyendo ajustar valores, aplicar cargos o generar notas de crédito/débito.

## Elementos Comunes en las Reglas

### Operadores de Comparación

Estos operadores definen cómo se comparan los valores reales de la factura con los valores esperados de la PO:

• igual

• mayor que

• mayor o igual que

• menor que

• menor o igual que

• dentro de la tolerancia

• fuera de la tolerancia

\


### Estado de Aprobación

Indica si una discrepancia está aprobada o no:

• aprobado

• rechazado

• cualquiera

\


### Tipos de Acción

Define acciones específicas a tomar cuando se detecta una discrepancia:

\
• línea de recibo

• línea de costo

• cargo de encabezado

• cargo de línea

• línea de impuesto

• línea de recibo de nota de débito

• línea de costo de nota de débito

• cargo de encabezado de nota de débito

• cargo de línea de nota de débito

• línea de recibo de nota de crédito

• línea de costo de nota de crédito

• cargo de encabezado de nota de crédito

• cargo de línea de nota de crédito

• línea de impuesto de nota de crédito

\


### Ejemplos de Reglas

#### [Caso 1, 2, 3: Cantidad y Precio Unitario Dentro de la Tolerancia](transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md)

\
• Propósito: Maneja escenarios donde tanto la cantidad como el precio unitario en la factura están dentro de los límites de tolerancia aceptados en comparación con la PO.

• Acción: El sistema acepta los valores de la factura y calcula el monto total.



#### [Caso 4, 5: Cantidad Dentro de la Tolerancia, Precio Unitario Fuera de la Tolerancia (Aprobado)](./#case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved)

• Propósito: Se aplica cuando la cantidad está dentro de la tolerancia pero el precio unitario está fuera de la tolerancia y ha sido aprobado.

• Acción: El sistema ajusta el precio unitario para que coincida con la PO y aplica cualquier cargo de línea necesario.

\


#### [Caso 6: Cantidad Dentro de la Tolerancia, Precio Unitario Fuera de la Tolerancia Negativa (Rechazado)](transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)&#x20;

• Propósito: Trata casos donde el precio unitario es menor de lo esperado y está fuera del rango de tolerancia, lo que lleva al rechazo.

• Acción: El sistema ajusta el precio unitario para que coincida con la PO, genera una nota de crédito por la diferencia y aplica cargos de encabezado según sea necesario.



### Manejo de Cargos e Impuestos

### Cargo por Tolerancia por Unidad

• Las reglas bajo esta categoría manejan discrepancias en los cargos por unidad, con acciones específicas basadas en si el cargo está dentro o fuera de la tolerancia y si está aprobado o rechazado.

### Ajustes de Línea de Impuesto

• Estas reglas gestionan discrepancias fiscales ajustando las líneas de impuesto o generando notas de crédito o débito correspondientes basadas en las diferencias entre los datos de impuestos de la factura y la PO.

### Enums y Opciones

• Enums: Listas predefinidas de valores que aseguran consistencia en las reglas (por ejemplo, operadores de comparación, tipos de aprobación).

• Opciones: Elecciones predefinidas para manejar cantidades o precios unitarios, ofreciendo flexibilidad en las definiciones de reglas.

## Explicación de Capturas de Pantalla

### Captura de Pantalla 1: Interfaz de Gestión de Reglas

<figure><img src="../../../../.gitbook/assets/docbits_rule_manager_interface.png" alt="Docbits Rule Manager Interface"><figcaption></figcaption></figure>

Esta captura de pantalla muestra la interfaz de Gestión de Reglas donde los administradores pueden ver y gestionar todas las reglas de resolución de conflictos. Los elementos clave incluyen:

• Botón Agregar Regla: Permite agregar nuevas reglas.

• Lista de Reglas: Muestra todas las reglas activas con detalles como nombre, sección y estado activo.

• Desplegable de Sección: Filtra las reglas según la sección a la que se aplican (por ejemplo, Líneas de Recibo, Cargos de Línea).

### Captura de Pantalla 2: Edición Detallada de Reglas

<figure><img src="../../../../.gitbook/assets/docbits_rule_editing_detail.png" alt="Docbits Rule Editing Detail"><figcaption></figcaption></figure>

Esta captura de pantalla ilustra la vista detallada de una regla específica que se está editando. Los elementos clave incluyen:

• Sección de Criterios: Define las condiciones bajo las cuales se activa la regla. Por ejemplo, los criterios pueden especificar que si la cantidad y el precio unitario difieren de la PO pero están dentro de la tolerancia, se debe aplicar la regla.

• Sección de Acciones: Especifica qué acciones deben tomarse cuando se cumplen los criterios. Esto puede incluir ajustar las líneas de la factura, generar notas de crédito o débito, o aplicar cargos adicionales.

• Tipo de Documento y Elementos de Costo: Permite al administrador mapear acciones específicas a tipos de documentos y elementos de costo, proporcionando flexibilidad en el manejo de diferentes escenarios.