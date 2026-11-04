# Por Encima del Monto Máximo

<figure><img src="../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Factura 2"><figcaption></figcaption></figure>

Este título indica que la regla está diseñada para gestionar casos en los que el total de la factura es mayor que el monto máximo que un aprobador está autorizado a manejar.

#### Configuración de la Regla:

1. **Cuando…**
* **El Tipo de Documento es Factura**: Esta condición asegura que la regla se aplique solo a facturas, lo cual es esencial para dirigir el flujo de trabajo correctamente.
2. **Y…**
* **El Estado del Documento es Pendiente de Aprobación**: La factura debe estar en estado de "Pendiente de Aprobación". Este estado es crucial para garantizar que la regla se aplique a facturas que aún se están procesando y que aún no se han finalizado.
* **Comparar dos campos: Monto Total Mayor que el Monto Máximo del Aprobador**: Esta condición verifica si el monto total de la factura excede el monto máximo que un aprobador puede manejar. Esta comparación también puede incluir una configuración de tolerancia, permitiendo variaciones menores basadas en criterios predefinidos.

#### Acción (Entonces…):

* **Asignar usuario del campo Próximo Aprobador Nivel, usar usuario Usuario como alternativa**: Si la factura excede el monto máximo especificado, se asigna automáticamente a un aprobador de nivel superior, indicado por el campo 'Próximo Aprobador Nivel'. Si este campo no está completado o el usuario especificado no está disponible, se utiliza un usuario predeterminado (probablemente un administrador u otro miembro del personal designado) como alternativa para garantizar que la factura se revise sin demoras.

#### Elementos de la Interfaz:

* **Agregar Tarjeta**: Esta opción permite agregar condiciones o acciones adicionales a la regla, brindando flexibilidad para abordar escenarios complejos.
* **Guardar**: Este botón guarda la configuración de la regla en el sistema.

#### Propósito de Esta Regla:

El propósito de esta regla es garantizar que las facturas que exceden ciertos umbrales financieros sean revisadas por aprobadores con los niveles de autorización adecuados. Esto ayuda a mantener el control financiero y la supervisión, asegurando que los gastos sean revisados por personal con los límites de aprobación necesarios, protegiendo así a la organización contra gastos no autorizados o inapropiados.

Esta regla, al igual que la anterior, ayuda a automatizar el flujo de trabajo, reduciendo el esfuerzo manual y mejorando el cumplimiento de las políticas financieras de la organización. Es un ejemplo de cómo la automatización del flujo de trabajo puede utilizarse de manera efectiva para gestionar procesos financieros complejos dentro de una empresa.
