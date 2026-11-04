# Menos que la Cantidad Máxima

<figure><img src="../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Factura"><figcaption></figcaption></figure>

Este título sugiere que la regla o condición que se está estableciendo está diseñada para manejar facturas donde el monto total es menor o igual a una cantidad máxima especificada.

#### Configuración de la Regla:

1. **Cuando…**
* **El Tipo de Documento es Factura**: Esta condición verifica si el documento que se está procesando es una factura. Esto es crucial para garantizar que la regla solo se aplique a facturas y no a otros tipos de documentos.
2. **Y…**
* **El Estado del Documento es Pendiente de Aprobación**: Esto especifica que la factura debe estar en estado de "Pendiente de Aprobación". Esta verificación de estado asegura que la regla se aplique solo a facturas que esperan aprobación.
* **Comparar dos campos: Monto Total Menor o Igual al Monto Máximo del Aprobador**: Esta condición compara el monto total de la factura con el monto máximo autorizado de un aprobador. Si el monto total de la factura es menor o igual a este monto máximo, la regla continúa con el siguiente paso. Esto probablemente incluye un nivel de tolerancia que permite desviaciones menores dentro de límites especificados.

#### Acción (Entonces…):

* **Asignar usuario del campo Nombre del Aprobador, usar usuario Usuario como alternativa**: Si se cumplen las condiciones especificadas, la factura se asigna automáticamente a un aprobador cuyo nombre está especificado en un campo. Si este campo está vacío o no está disponible, se asigna un usuario predeterminado (probablemente un administrador u otro miembro del personal designado) como alternativa para manejar la aprobación.

#### Elementos de la Interfaz:

* **Agregar Tarjeta**: Este botón probablemente permite a los usuarios agregar más condiciones o acciones a la regla, mejorando la flexibilidad y especificidad del flujo de trabajo.
* **Guardar**: Guarda la regla configurada en el sistema.

#### Propósito de Esta Regla:

Esta configuración está diseñada para agilizar el proceso de aprobación de facturas al dirigir automáticamente las facturas al aprobador adecuado según el monto y garantizar que solo aquellas dentro de un cierto umbral se manejen de esta manera automatizada. Ayuda en la gestión de controles financieros y acelera el flujo de trabajo al reducir las verificaciones manuales para cada factura.
