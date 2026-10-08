# Then: elige una tarjeta de acción

Una tarjeta **Then** le indica al flujo de trabajo qué hacer después de su disparador **When** y de cualquier condición **And**. En el **Constructor de flujo de trabajo**, selecciona **Añadir tarjeta** bajo **Entonces...**. Elige una categoría a la izquierda o escribe un nombre en **Buscar tarjeta**. Selecciona una vista previa de tarjeta para añadirla, rellena los campos que muestra la tarjeta y guarda el flujo de trabajo. Desplázate dentro del selector para ver más tarjetas. Selecciona **×** para cerrarlo sin añadir ninguna tarjeta. Consulta [Flujo de trabajo](../README.md) para ver la secuencia completa.

Las vistas previas siguientes muestran acciones disponibles, no configuraciones completadas. Elige la acción que corresponda al resultado que buscas.

## Campo del documento

Establece o invierte una casilla de verificación, escribe texto en un campo o copia el contenido de un campo a otro. Elige los nombres de campo y el valor que solicita la tarjeta. Consulta [Campo del documento](document-field/README.md).

<figure><img src="../../../.gitbook/assets/then-category-document-field-es.png" alt="Selector de tarjetas Then en español con Campo del documento seleccionado; las vistas previas muestran acciones de casilla, texto y copia de campo."><figcaption>Cambia un campo o copia su contenido.</figcaption></figure>

## Documento

Elige **Aprobar el documento** o **Rechazar el documento** cuando el flujo de trabajo deba tomar esa decisión. Usa primero una condición **And** si la aprobación debe depender de una comprobación. Consulta [Documento](document/README.md).

<figure><img src="../../../.gitbook/assets/then-category-document-es.png" alt="Selector de tarjetas Then en español con Documento seleccionado; se ven las vistas previas Aprobar el documento y Rechazar el documento."><figcaption>Aprueba o rechaza el documento actual.</figcaption></figure>

## Lógica

Usa estas tarjetas para convertir valores entre formatos de número, texto y booleano, o para leer un valor de JSON. Elige los campos de entrada y salida en la tarjeta seleccionada.

<figure><img src="../../../.gitbook/assets/then-category-logic-es.png" alt="Selector de tarjetas Then en español con Lógica seleccionado; las vistas previas visibles convierten tipos de datos y leen valores de JSON."><figcaption>Transforma valores para un paso posterior del flujo de trabajo.</figcaption></figure>

## Estado

Elige **Cambiar estado** para mover el documento a un estado seleccionado. La tarjeta también puede desencadenar otro flujo de trabajo. Consulta [Estado](status/README.md).

<figure><img src="../../../.gitbook/assets/then-category-status-es.png" alt="Selector de tarjetas Then en español con Estado seleccionado; la vista previa Cambiar estado incluye un campo de estado y un disparador de flujo de trabajo opcional."><figcaption>Mueve el documento a otro estado.</figcaption></figure>

## Indicaciones y guiones

Elige esta categoría para ejecutar un guion de indicación de DocOperator. Selecciona el guion y las variables que solicita la tarjeta. La tarjeta también ofrece ajustes de ejecución como reintentos.

<figure><img src="../../../.gitbook/assets/then-category-prompts-scripts-es.png" alt="Selector de tarjetas Then en español con Indicaciones y guiones seleccionado; se ve una vista previa de guion de indicación de DocOperator."><figcaption>Ejecuta un guion de indicación de DocOperator configurado.</figcaption></figure>

## Exportar

Inicia una exportación, exporta con una configuración elegida o pone en cola una exportación final. Elige la configuración de exportación y la opción de tarea pendiente que muestra tu tarjeta. Consulta [Exportar](export/README.md).

<figure><img src="../../../.gitbook/assets/then-category-export-es.png" alt="Selector de tarjetas Then en español con Exportar seleccionado; las vistas previas muestran exportaciones inicial, configurada, en cola y alternativa."><figcaption>Elige cuándo y cómo se exporta el documento.</figcaption></figure>

## Tarea

Crea una tarea o notificación y asígnala a un usuario o grupo. Introduce el título, la descripción, la prioridad y los ajustes de notificación que solicita la tarjeta. Algunas tarjetas asignan de forma secuencial. Consulta [Tarea](task/README.md).

<figure><img src="../../../.gitbook/assets/then-category-task-es.png" alt="Selector de tarjetas Then en español con Tarea seleccionado; las vistas previas visibles crean o asignan tareas y notificaciones."><figcaption>Crea trabajo de seguimiento para una persona o grupo.</figcaption></figure>

## Correo electrónico

Envía un correo electrónico con una plantilla seleccionada, ya sea a destinatarios o a grupos. Elige la plantilla y el destino en la tarjeta.

<figure><img src="../../../.gitbook/assets/then-category-email-es.png" alt="Selector de tarjetas Then en español con Correo electrónico seleccionado; las vistas previas envían un correo con plantilla a destinatarios o grupos."><figcaption>Envía un correo electrónico con plantilla.</figcaption></figure>

## Cuadro

Cambia entradas o calcula valores en un cuadro del documento. Selecciona el cuadro, las columnas, el operador y la columna de resultado que solicita la tarjeta. Consulta [Cuadro](table/README.md).

<figure><img src="../../../.gitbook/assets/then-category-table-es.png" alt="Selector de tarjetas Then en español con Cuadro seleccionado; las vistas previas cambian entradas y calculan columnas de resultado."><figcaption>Actualiza o calcula datos del cuadro.</figcaption></figure>

## Asignado a

Asigna el documento a un usuario, grupo, destinatario o suborganización. Algunas tarjetas usan un campo o una tabla de decisiones y ofrecen una alternativa. Elige el destino y la alternativa correctos en la tarjeta seleccionada. Consulta [Asignado a](assignee/README.md).

<figure><img src="../../../.gitbook/assets/then-category-assignee-es.png" alt="Selector de tarjetas Then en español con Asignado a seleccionado; las vistas previas visibles asignan un usuario, destinatario, grupo o contacto de proveedor."><figcaption>Envía el documento a la siguiente persona o grupo responsable.</figcaption></figure>

## Action

Ejecuta otro flujo de trabajo, envía una petición HTTPS, llama a una API o usa la tarjeta de cálculo de aumento de costes. Estas acciones pueden afectar a otros sistemas; pregunta a tu administrador qué endpoint y ajustes usar. Consulta [Action](action/README.md).

<figure><img src="../../../.gitbook/assets/then-category-action-es.png" alt="Selector de tarjetas Then en español con Action seleccionado; las vistas previas muestran Ejecutar flujo de trabajo, petición HTTPS, llamada a API y cálculo de aumento de costes."><figcaption>Inicia otro flujo de trabajo o una acción de integración.</figcaption></figure>
