# Above Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Factura 2"><figcaption></figcaption></figure>

Este título indica que la regla está diseñada para gestionar los casos en los que el total de la factura es mayor que el importe máximo que un aprobador está autorizado a tramitar.

#### Configuración de la regla:

1. **When…**
   * **Document Type is Invoice**: Esta condición garantiza que la regla se aplique únicamente a las facturas, lo cual es esencial para dirigir el flujo de trabajo correctamente.
2. **And…**
   * **Document Status is Pending Approval**: La factura debe estar en estado "Pending Approval". Este estado es crucial para garantizar que la regla se aplique a las facturas que aún se están procesando y que todavía no se han finalizado.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: Esta condición comprueba si el importe total de la factura supera el importe máximo que un aprobador puede tramitar. Esta comparación también puede incluir un ajuste de tolerancia, lo que permite variaciones menores según criterios predefinidos.

#### Acción (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: Si la factura supera el importe máximo especificado, se asigna automáticamente a un aprobador de nivel superior, indicado por el campo 'Next Level Approver'. Si este campo no está completado o el usuario especificado no está disponible, se utiliza un usuario predeterminado (probablemente un administrador u otro miembro del personal designado) como alternativa para garantizar que la factura se revise sin demora.

#### Elementos de la interfaz:

* **Add Card**: Esta opción permite añadir condiciones o acciones adicionales a la regla, ofreciendo flexibilidad para abordar escenarios complejos.
* **Save**: Este botón guarda la configuración de la regla en el sistema.

#### Propósito de esta regla:

El propósito de esta regla es garantizar que las facturas que superan determinados umbrales financieros sean revisadas por aprobadores con los niveles de autorización adecuados. Esto ayuda a mantener el control y la supervisión financiera, garantizando que los gastos sean revisados por personal con los límites de aprobación necesarios, protegiendo así a la organización frente a gastos no autorizados o inapropiados.

Esta regla, al igual que la anterior, ayuda a automatizar el flujo de trabajo, reduciendo el esfuerzo manual y mejorando el cumplimiento de las políticas financieras de la organización. Es un ejemplo de cómo la automatización de flujos de trabajo puede utilizarse eficazmente para gestionar procesos financieros complejos dentro de una empresa.
