# Plantillas de correo electrónico

## **Visión general**

Las plantillas de correo electrónico (Email Templates) le permiten personalizar los correos electrónicos automáticos que envía DocBits, por ejemplo recordatorios de aprobación o notificaciones de error. Una plantilla define la línea de asunto y el cuerpo, y puede incluir campos dinámicos (p. ej. `{{InvoiceNumber}}`), imágenes y formato de texto enriquecido.

## **Acceso a las plantillas de correo electrónico**

Vaya a **Settings → Communication & Notifications → Email Templates**. La lista muestra cada plantilla con su **Name**, **Subject**, **Document Type**, la fecha de **Last Modified** y **Actions** (editar o eliminar).

<figure><img src="../../../.gitbook/assets/email_templates_dashboard_list.png" alt="Lista de Email Templates"><figcaption><p>La lista de Email Templates</p></figcaption></figure>

## **Crear una plantilla**

1. Haga clic en **+ New** en la esquina superior derecha.
2. Rellene los campos:
   * **Name** — un identificador descriptivo (p. ej. "Document Error Notification").
   * **Document Type** — el tipo de documento al que se aplica la plantilla (p. ej. `INVOICE`).
   * **Include Document As Attachment** — active este interruptor para adjuntar el documento de origen al correo electrónico.
   * **Subject** — la línea de asunto del correo. Haga clic en el botón **+** situado junto al campo para insertar un campo dinámico, o escriba `{{FieldID}}` directamente.
3. Diseñe el cuerpo en el editor de texto enriquecido: dé formato al texto (negrita, cursiva, listas, alineación), inserte imágenes con **Upload**, edite el HTML sin procesar con el botón `<>` y use el botón **+** para insertar campos dinámicos.
4. Haga clic en **Save**.

<figure><img src="../../../.gitbook/assets/email_templates_4.png" alt="Editor de plantillas de correo electrónico"><figcaption><p>El editor de plantillas: nombre, tipo de documento, interruptor de adjunto, asunto y cuerpo de texto enriquecido</p></figcaption></figure>

## **Campos dinámicos**

Los campos dinámicos se sustituyen por los datos del documento cuando se envía el correo electrónico. Insértelos con el botón **+**, o escríbalos manualmente con dobles llaves:

* `{{invoice_id}}` — el número de factura
* `{{supplier_name}}` — el nombre del proveedor
* `{{total_amount}}` — el importe total
* `{{status}}` — el estado actual del documento

## **Enviar un correo electrónico de prueba**

Haga clic en **Send Test** en el editor, introduzca una dirección en **Receiver Email** y haga clic en **Send**. DocBits envía una vista previa de la plantilla para que pueda comprobar el diseño y verificar que los campos dinámicos se resuelven correctamente antes de guardar.

<figure><img src="../../../.gitbook/assets/test_email_configuration_dialog.png" alt="Cuadro de diálogo Send Test"><figcaption><p>El cuadro de diálogo Send Test</p></figcaption></figure>

## **Uso de plantillas en las notificaciones**

Las plantillas guardadas se pueden vincular a los flujos de trabajo de [**Email Notification**](email-notification/), por ejemplo recordatorios de aprobación o actualizaciones de cambio de estado.
