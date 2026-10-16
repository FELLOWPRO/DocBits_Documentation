# Then

Una tarjeta **Then** indica a un flujo de trabajo qué debe hacer después de su disparador **When** y de cualquier condición **And**. En el **Workflow Builder**, seleccione **Add Card** bajo **Then...**. Elija una categoría a la izquierda o escriba un nombre en **Search Card**. Seleccione la vista previa de una tarjeta para añadirla, complete los campos que muestra la tarjeta y guarde el flujo de trabajo. Desplácese dentro del selector para ver más tarjetas. Seleccione **×** para cerrarlo sin añadir ninguna tarjeta. Consulte [Flujo de trabajo](../../) para ver la secuencia completa.

Las vistas previas que aparecen a continuación muestran las acciones disponibles, no configuraciones terminadas. Elija la acción que corresponda al resultado que desea obtener.

## Document Field

Active o invierta una casilla de verificación, escriba texto en un campo o copie un campo en otro. Elija los nombres de campo y el valor que solicita la tarjeta. Consulte [Document Field](document-field/).

<figure><img src="../../../../.gitbook/assets/then-category-document-field-en.png" alt="Selector de tarjetas Then en inglés con Document Field seleccionado; las vistas previas muestran acciones de casilla de verificación, texto y copia de campo."><figcaption><p>Cambie un campo o copie su contenido.</p></figcaption></figure>

## Document

Elija **Approve the Document** o **Reject the Document** cuando el flujo de trabajo deba tomar esa decisión. Utilice primero una condición **And** si la aprobación debe depender de una comprobación. Consulte [Document](document/).

<figure><img src="../../../../.gitbook/assets/then-category-document-en.png" alt="Selector de tarjetas Then en inglés con Document seleccionado; se ven las vistas previas de Approve the Document y Reject the Document."><figcaption><p>Apruebe o rechace el documento actual.</p></figcaption></figure>

## Logic

Utilice estas tarjetas para convertir valores entre los formatos de número, texto y booleano, o para leer un valor de un JSON. Elija los campos de entrada y de salida en la tarjeta seleccionada.

<figure><img src="../../../../.gitbook/assets/then-category-logic-en.png" alt="Selector de tarjetas Then en inglés con Logic seleccionado; las vistas previas visibles convierten tipos de datos y leen valores de un JSON."><figcaption><p>Transforme valores para un paso posterior del flujo de trabajo.</p></figcaption></figure>

## Status

Elija **Change Status** para pasar el documento a un estado seleccionado. La tarjeta también puede disparar otro flujo de trabajo. Consulte [Status](status/).

<figure><img src="../../../../.gitbook/assets/then-category-status-en.png" alt="Selector de tarjetas Then en inglés con Status seleccionado; la vista previa de Change Status incluye un campo de estado y un disparador de flujo de trabajo opcional."><figcaption><p>Pase el documento a otro estado.</p></figcaption></figure>

## Prompts and Scripts

Elija esta categoría para ejecutar un script de prompt de DocOperator. Seleccione el script y las variables que solicita la tarjeta. La tarjeta también ofrece ajustes de ejecución, como los reintentos.

<figure><img src="../../../../.gitbook/assets/then-category-prompts-scripts-en.png" alt="Selector de tarjetas Then en inglés con Prompts and Scripts seleccionado; se ve la vista previa de un script de prompt de DocOperator."><figcaption><p>Ejecute un script de prompt de DocOperator configurado.</p></figcaption></figure>

## Export

Inicie una exportación, exporte con una configuración elegida o ponga en cola una exportación final. Elija la configuración de exportación y la opción de tareas pendientes que muestra su tarjeta. Consulte [Export](export/).

<figure><img src="../../../../.gitbook/assets/then-category-export-en.png" alt="Selector de tarjetas Then en inglés con Export seleccionado; las vistas previas muestran exportaciones iniciadas, configuradas, en cola y alternativas."><figcaption><p>Seleccione cuándo y cómo se exporta el documento.</p></figcaption></figure>

## Task

Cree una tarea o una notificación y asígnela a un usuario o a un grupo. Introduzca el título, la descripción, la prioridad y los ajustes de notificación que solicita la tarjeta. Algunas tarjetas asignan de forma secuencial. Consulte [Task](task/).

<figure><img src="../../../../.gitbook/assets/then-category-task-en.png" alt="Selector de tarjetas Then en inglés con Task seleccionado; las vistas previas visibles crean o asignan tareas y notificaciones."><figcaption><p>Cree trabajo de seguimiento para una persona o un grupo.</p></figcaption></figure>

## Email

Envíe un correo electrónico con una plantilla seleccionada, ya sea a destinatarios o a grupos. Elija la plantilla y el destino en la tarjeta.

<figure><img src="../../../../.gitbook/assets/then-category-email-en.png" alt="Selector de tarjetas Then en inglés con Email seleccionado; las vistas previas envían un correo con plantilla a destinatarios o a grupos."><figcaption><p>Envíe un correo electrónico con plantilla.</p></figcaption></figure>

## Table

Cambie entradas o calcule valores en una tabla del documento. Seleccione la tabla, las columnas, el operador y la columna de resultado que solicita la tarjeta. Consulte [Table](table/).

<figure><img src="../../../../.gitbook/assets/then-category-table-en.png" alt="Selector de tarjetas Then en inglés con Table seleccionado; las vistas previas cambian entradas y calculan columnas de resultado."><figcaption><p>Actualice o calcule datos de la tabla.</p></figcaption></figure>

## Assignee

Asigne el documento a un usuario, grupo, destinatario o suborganización. Algunas tarjetas utilizan un campo o una tabla de decisión y ofrecen una alternativa. Elija el destino y la alternativa adecuados en la tarjeta seleccionada. Consulte [Assignee](assignee/).

<figure><img src="../../../../.gitbook/assets/then-category-assignee-en.png" alt="Selector de tarjetas Then en inglés con Assignee seleccionado; las vistas previas visibles asignan un usuario, destinatario, grupo o contacto de proveedor."><figcaption><p>Dirija el documento a la siguiente persona o grupo responsable.</p></figcaption></figure>

## Action

Ejecute otro flujo de trabajo, envíe una solicitud HTTPS, llame a una API o utilice la tarjeta de cálculo de aumento de costes. Estas acciones pueden afectar a otros sistemas; consulte a su administrador qué endpoint y qué ajustes debe utilizar. Consulte [Action](action/).

<figure><img src="../../../../.gitbook/assets/then-category-action-en.png" alt="Selector de tarjetas Then en inglés con Action seleccionado; las vistas previas muestran Run workflow, HTTPS request, API call y cost increase calculation."><figcaption><p>Inicie otro flujo de trabajo o una acción de integración.</p></figcaption></figure>
