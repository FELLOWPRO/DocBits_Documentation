# Less than Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Factura"><figcaption></figcaption></figure>

Este título sugiere que la regla o condición que se está configurando está diseñada para gestionar las facturas cuyo importe total es menor o igual que un importe máximo especificado.

#### Configuración de la regla:

1. **When…**
   * **Document Type is Invoice**: Esta condición comprueba si el documento que se está procesando es una factura. Esto es crucial para garantizar que la regla se aplique únicamente a las facturas y no a otros tipos de documentos.
2. **And…**
   * **Document Status is Pending Approval**: Esto especifica que la factura debe estar en estado "Pending Approval". Esta comprobación de estado garantiza que la regla se aplique únicamente a las facturas pendientes de aprobación.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: Esta condición compara el importe total de la factura con el importe máximo autorizado de un aprobador. Si el importe total de la factura es menor o igual que este importe máximo, la regla continúa con el siguiente paso. Esto probablemente incluye un nivel de tolerancia que permite desviaciones menores dentro de los límites especificados.

#### Acción (Then…):

* **Assign user from field Approver Name, use user User as fallback**: Si se cumplen las condiciones especificadas, la factura se asigna automáticamente a un aprobador cuyo nombre se especifica en un campo. Si este campo está vacío o no está disponible, se asigna un usuario predeterminado (probablemente un administrador u otro miembro del personal designado) como alternativa para gestionar la aprobación.

#### Elementos de la interfaz:

* **Add Card**: Este botón probablemente permite a los usuarios añadir más condiciones o acciones a la regla, mejorando la flexibilidad y especificidad del flujo de trabajo.
* **Save**: Guarda la regla configurada en el sistema.

#### Propósito de esta regla:

Esta configuración está diseñada para agilizar el proceso de aprobación de facturas dirigiéndolas automáticamente al aprobador adecuado según el importe y garantizando que solo las que se encuentran dentro de un determinado umbral se gestionen de esta manera automatizada. Ayuda a gestionar los controles financieros y acelera el flujo de trabajo al reducir las comprobaciones manuales de cada factura.

\
