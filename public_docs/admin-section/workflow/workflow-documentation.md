# Documentación del Flujo de Trabajo

**Documentación del Flujo de Trabajo**

Para mantener una visión general, puedes dar a los flujos de trabajo diferentes encabezados para que puedas saber de inmediato de qué tarea se trata este flujo de trabajo.

Crear un nuevo Flujo de Trabajo: Haz clic en + AÑADIR FLUJO DE TRABAJO

![](<../../.gitbook/assets/0 (1).png>)

Puedes utilizar estos flujos de trabajo (Test 1, 2, 3) para asignar automáticamente varios documentos al empleado adecuado en la empresa.

![](<../../.gitbook/assets/1 (1).png>)

Si una factura u otro documento supera cierta cantidad total que requiere revisión y aprobación previa, estos documentos pueden asignarse inmediatamente a la persona correcta.

<figure><img src="../../.gitbook/assets/docbits_export_sftp.png" alt="DocBits Exportar Sftp"><figcaption></figcaption></figure>

**Test 1:              Tarjeta Lógica**

Cuando:             **El asignado es:**                    Amier Haider

Y:                **El tipo de documento es:**        Factura

Entonces:              **Asignar documento a:**   Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2:              Tarjeta Lógica**

Cuando:              **El asignado es:**                    Amier Haider

Y:                 **El tipo de documento es:**        Nota de Entrega

Entonces:               **Asignar documento a:**   James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3:             Tarjeta Lógica**

**Cuando:**             **El asignado es:**                    Amier Haider

**Y:**                **El tipo de documento es:**        Confirmación de Pedido

**Entonces:**              **Asignar documento a:**   Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)





También es posible, si el documento no se asigna a una sola persona, asignarlo a un empleado específico desde el principio.

<figure><img src="../../.gitbook/assets/docbits_db_access_creation.png" alt="Docbits Db Access Creation" width="375"><figcaption></figcaption></figure>





Para tener una visión más clara de lo que debe suceder con un documento, puedes establecer el estado de los documentos entrantes en este flujo de trabajo. Este flujo de trabajo permite ver de inmediato si hay, por ejemplo, una aprobación pendiente.



**Test 4:             Tarjeta Lógica**

**Cuando:**             **El tipo de documento es:**         Nota de Entrega

**Y:**                **El asignado es:**                     Amier Haider

**Entonces:**              **Cambiar Estado a:**         Aprobación Pendiente

<figure><img src="../../.gitbook/assets/docbits_export_smb.png" alt="DocBits Exportar Smb"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)



**Test 5:                Tarjeta Lógica**

Cuando:                **El tipo de documento es:**           Factura

Y:                   **El asignado es:**                       Stefan Reppermund

Entonces:                 **Cambiar Estado a:**           Segunda Aprobación Pendiente

<figure><img src="../../.gitbook/assets/docbits_workflow_test_9_replacement.png" alt="Docbits Workflow Test 9 Replacement"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)





Si una factura u otro documento supera cierta cantidad total que requiere revisión y aprobación previa, estos documentos pueden asignarse inmediatamente a la persona adecuada.

![](<../../.gitbook/assets/11 (1).png>)



**Test 6:                    Tarjeta Lógica**

Cuando:                   **El asignado es:**                   Amier Haider

Y:                      Campo de Documento        **total\_amount**     es      **Mayor que       500**

Entonces:                    **Asignar documento a:**   Asad Usman Khan

<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)



También es posible ingresar el estado en el flujo de trabajo, para que la persona asignada pueda ver de inmediato en qué estado se encuentra este documento y qué debe suceder a continuación.



**Test 7:                 Tarjeta Lógica**

**Cuando:** **El asignado es:**                     Amier Haider

**Y:**                   Campo de Documento           **total\_amount**      es        **Mayor que      500**

**Entonces:**                 **Asignar documento a:**     Asad Usman Khan

&#x20;                            **Cambiar Estado a:**          Aprobación Pendiente

<figure><img src="../../.gitbook/assets/docbits_approval_2.png" alt="DocBits Aprobación 2"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits_workflow_purchase_order_2.png" alt="DocBits Flujo de trabajo Compra Pedido 2"><figcaption></figcaption></figure>





Por ejemplo, si falta cierta información importante en un documento, pero es importante y debe incluirse para su procesamiento posterior, puedes configurar el flujo de trabajo para que estos documentos se envíen de inmediato al comprador y a un sustituto.

<figure><img src="../../.gitbook/assets/docbits_workflow_5.png" alt="DocBits Flujo de trabajo 5"><figcaption></figcaption></figure>



**Test 9:**

El Flujo de Trabajo con estas tarjetas lógicas está diseñado para verificar automáticamente que la cantidad, el precio unitario o el descuento detallados en una confirmación de pedido coincidan con las cifras correspondientes en la orden de compra. Esta verificación garantiza la consistencia y precisión entre lo solicitado y lo que el proveedor confirma entregar.

Puedes asignar a estos documentos un estado específico o asignarlos a un empleado específico.

<div align="center">

<figure><img src="../../.gitbook/assets/docbits_approval_permission.png" alt="DocBits Aprobación Permiso"><figcaption></figcaption></figure>

</div>

<figure><img src="../../.gitbook/assets/docbits_purchase_order_4.png" alt="DocBits Compra Pedido 4"><figcaption></figcaption></figure>

**Tarjeta Lógica: Coincidencia de Cantidad o Precio Unitario o Descuento**

Esta tarjeta lógica está diseñada para verificar automáticamente que la cantidad, el precio unitario o el descuento detallados en una confirmación de pedido coincidan con las cifras correspondientes en la orden de compra original. Esta verificación garantiza la consistencia y precisión entre lo solicitado y lo que el proveedor confirma entregar.



**Condición de Activación**

La lógica se activa cuando se cumplen cualquiera de las siguientes condiciones en una confirmación de pedido en relación con la orden de compra original:

* **Cantidad**: La cantidad de artículos pedidos coincide con la cantidad confirmada por el proveedor.
* **Precio Unitario**: El precio por artículo acordado coincide con la confirmación del proveedor.
* **Descuento**: Cualquier descuento aplicado es consistente entre la orden de compra y la confirmación del pedido.



* **Definir Parámetros de Comparación**: Configura los campos específicos (cantidad, precio unitario, descuento) que la tarjeta lógica verificará para encontrar una coincidencia.
* **Automatizar la Verificación**: Configura el sistema para comparar automáticamente estos detalles al recibir una confirmación de pedido.
* **Personalizar Alertas**: Decide sobre el flujo de trabajo para manejar discrepancias, incluida la personalización de alertas para revisión manual.

Esta tarjeta lógica es vital para garantizar que los detalles de una confirmación de pedido coincidan con la orden de compra original, salvaguardando la integridad del ciclo de adquisiciones.



**Test 10:**

Si tienes un cálculo diferente para recargos, o solo los tienes en algunos artículos, puedes utilizar las tarjetas de cálculo de tabla genéricas, algunas de ellas también permiten filtrar por expresiones regulares.

<figure><img src="../../.gitbook/assets/docbits_table_invoice.png" alt="DocBits Tabla Factura"><figcaption></figcaption></figure>

Arriba hay un ejemplo de cálculo para MTZ con un filtro para números de artículo que comienzan con 01, 06, 9, 001 o 000.



Con una configuración manual, se recomienda dividir los cálculos que dependen de nuevas columnas en un flujo de trabajo separado. Para continuar con el cálculo, puedes utilizar la tarjeta Ejecutar Flujo de Trabajo.

**Ejecutar Flujo de Trabajo**

<figure><img src="../../.gitbook/assets/docbits_workflow_2.png" alt="DocBits Flujo de trabajo 2"><figcaption></figcaption></figure>

Con esta tarjeta, puedes especificar el nombre de un flujo de trabajo que se ejecutará después del flujo de trabajo actual si se cumplen sus condiciones y después de las tarjetas then anteriores del flujo de trabajo actual. Si bien prioriza los flujos de trabajo ejecutables y activos, también te permite ejecutar flujos de trabajo desactivados si el documento cumple las condiciones de los flujos de trabajo.
### **Agregar recargos calculados en una columna existente** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Si deseas agregar todos los recargos como un descuento negativo en la columna de descuento existente, puedes utilizar la tarjeta de cálculo. Puede haber entradas en esta columna, puedes establecerla como una de las variables en la tarjeta, restarle el MTZ y agregar el resultado de vuelta en esta columna. En caso de que haya campos vacíos (recargos solo para algunos elementos), se asumirá un 0 para su cálculo.

**Notificar al usuario para autorizar la confirmación del pedido en DocBits**

Después de calcular los recargos, es posible que desees notificar a un usuario específico para autorizar la confirmación del pedido. Para esto, puedes utilizar la tarjeta de notificación.

<figure><img src="../../.gitbook/assets/docbits_settings_email.png" alt="DocBits Configuración Correo electrónico"><figcaption></figcaption></figure>

Dependiendo de la configuración, al usuario se le asigna una nueva tarea en DocBits y opcionalmente se le envía un correo electrónico para notificarle sobre su nueva tarea.
