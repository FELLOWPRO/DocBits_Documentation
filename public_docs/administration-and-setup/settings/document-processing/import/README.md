# Importar

## Descripción general

Para crear una conexión se necesita una cuenta de administrador. Use **Import** para configurar la importación automática de documentos desde un servidor FTP/SFTP, un buzón conectado o la dirección de correo entrante de DocBits. Compruebe la organización y el entorno actuales antes de introducir los datos de conexión.

<figure><img src="../../../../.gitbook/assets/import-settings-overview-es-20261109.png" alt="Página de ajustes Import con el diagrama Import Pipeline, la lista FTP Import con un botón New y la lista Email Import con un botón New"><figcaption><p>La página Import: el diagrama Import Pipeline de solo lectura, la lista FTP Import y la lista Email Import, cada una con su propio botón <strong>New</strong>.</p></figcaption></figure>

## Cómo acceder

1. Vaya a **Settings** → **Document Processing** → **Import**.
2. Despliegue la sección necesaria. **FTP Import** y **Email Import** tienen cada una su propio botón **New**.

## **Document Settings**

La página Import actual contiene **Import Pipeline**, **FTP Import**, **Email Import** y, cuando está habilitada, **Inbound Emails**. El recorte de páginas, los plazos de pago predeterminados y los campos de patrón de fecha no son controles de esta vista Import.

**Import Pipeline** muestra la topología de enrutamiento FTP/SFTP, incluidas las regiones de origen y destino. Revise cualquier aviso mostrado antes de cambiar una conexión. La pestaña de pipeline **Email** muestra actualmente un mensaje de próxima disponibilidad; no muestra ningún diagrama de procesamiento de correo.

## **FTP Import**

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-overview-en-20261030.png" alt="Tabla FTP Import con el botón New y columnas para tipo, servidor, nombre de usuario, puerto, suborganización y directorio"><figcaption><p>Use New en FTP Import para añadir una conexión de servidor. En este ejemplo, las filas de conexiones existentes están ocultas.</p></figcaption></figure>

### Requisitos

* Un servidor FTP, FTPS o SFTP accesible por el servicio de importación.
* La dirección del servidor, el protocolo, el puerto, el nombre de usuario y la contraseña facilitados por su administrador.
* Un directorio de importación y, si se requiere archivado, un directorio de archivo aprobado.

### Añadir nueva conexión

1. Haga clic en **New** en **FTP Import**.
2. Introduzca los ajustes de conexión. Un formulario nuevo comienza con **SFTP** y el puerto **22**; sustituya estos valores cuando su servidor use otro protocolo o puerto.

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-blank-form-en-20261030.png" alt="Formulario de nueva conexión FTP con SFTP, puerto 22, campos de directorio, ajustes de reintento y Save y Cancel"><figcaption><p>Introduzca los datos del servidor y de inicio de sesión y, a continuación, compruebe los directorios, el enrutamiento y los ajustes de reintento. Los campos de contraseña y de clave API están ocultos; este ejemplo no se ha guardado.</p></figcaption></figure>

* **Type**, **Server name**, **Port**, **Username** y **Password** identifican y autentican la conexión con el servidor.
* **Primary Directory** define el directorio base. **Import Directory** selecciona la carpeta que se va a procesar; la selección de carpetas está disponible una vez guardada la conexión.
* **Document Type** y **Sub-Organizations** controlan la asignación. **File name matching patterns** limita los nombres de archivo que se tienen en cuenta.
* **Archive after Import** permite mover los archivos procesados al directorio de archivo indicado. **Include Subfolder Files** amplía el procesamiento a las subcarpetas.
* **Retry interval (min)**, **Retry duration (hours)** y **Notification emails (comma-separated)** controlan el comportamiento de reintento y de notificación. Los valores predeterminados de la ilustración son 60 minutos y 48 horas.
* **API Key** usa la clave de suscripción de aplicación existente de la organización. El icono del ojo muestra u oculta esa clave; el icono de copia la copia al portapapeles. Estos controles no crean una clave nueva. Manténgala confidencial; no la incluya en capturas de pantalla ni en mensajes de soporte.

Use **Cancel** o el icono de cierre para salir de un formulario de conexión nueva sin guardarlo.

3. Revise los valores y haga clic en **Save** cuando la conexión esté lista para crearse.
4. En el menú **Actions** de la fila guardada, elija **Activate** cuando las importaciones estén autorizadas a ejecutarse.

### Acciones para FTP

El menú **Actions** de la conexión guardada ofrece:

* **Test Connection**: contacta con el servidor configurado para comprobar la conexión.
* **Connection Logs**: inspeccione los intentos de conexión y los errores.
* **Activate/Deactivate**: habilita o detiene el procesamiento automático de esta conexión.
* **Edit**: cambia su configuración.
* **Delete**: elimina la conexión.

Las pruebas, la activación, la edición y la eliminación afectan a una conexión real. Verifique la fila y la organización seleccionadas antes de usarlas.

## **Email Import**

Un buzón conectado es distinto de la dirección de correo entrante de DocBits que se describe en el tutorial siguiente. Elija el método que se ajuste a su proceso.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-overview-en-20261030.png" alt="Tabla Email Import con New, el icono del registro de importación y columnas de configuración del buzón"><figcaption><p>Use New para una conexión de buzón o el icono de registro para revisar las importaciones. En este ejemplo, las filas de conexiones existentes y el enlace informativo están ocultos.</p></figcaption></figure>

<mark style="color:red;">**Note**</mark>: Solo se importarán documentos con los siguientes tipos de archivo:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

{% hint style="info" %}
**Cómo se reconocen los archivos adjuntos**

Además de las extensiones de archivo indicadas arriba, DocBits también identifica un documento por su **contenido real** (firma de archivo), no solo por el tipo de contenido declarado por el sistema de correo emisor. Esto es relevante en los correos **reenviados**: los servidores y pasarelas de correo intermedios suelen reetiquetar un archivo adjunto con un tipo genérico (`application/octet-stream`) en lugar de, por ejemplo, `application/pdf` o `application/xml`. DocBits sigue reconociendo e importando estos archivos adjuntos correctamente.

* Los mensajes **`.eml` reenviados** y los archivos adjuntos **`winmail.dat`** (TNEF) de Outlook se descomprimen y los documentos que contienen se importan.
* **Codificación XML:** cuando una factura XML se reetiqueta con un tipo genérico (`application/octet-stream`), DocBits la reconoce por su declaración `<?xml`, tolerando una marca de orden de bytes (BOM) inicial **UTF-8** o **UTF-16** (LE/BE); actualmente solo estas codificaciones BOM se detectan automáticamente a partir del contenido. Un archivo adjunto que conserva un nombre de archivo `.xml` se importa independientemente de su codificación.
* **Ignorados:** las imágenes en línea que viajan en un correo (logotipos de firma o gráficos incrustados: PNG, JPG, GIF, BMP) se omiten de forma silenciosa y **no** se cuentan como importaciones fallidas.

Si un archivo adjunto no se puede importar y la opción **“Reply to this email if import can not be done”** está habilitada para la dirección de entrada, se notifica a la dirección de respuesta configurada.
{% endhint %}

### Añadir nueva conexión IMAP

1. Haga clic en **New** en **Email Import** y seleccione **IMAP** en **Protocol**.
2. En **Email Server Setup**, introduzca el nombre del servidor, el puerto, el cifrado, el nombre de usuario, la dirección de correo y la contraseña. Use los valores que exija su proveedor de correo; el 993 mostrado es un ejemplo de puerto, no un ajuste completado.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-step1-en-20261030.png" alt="Email Server Setup de IMAP con protocolo, servidor, puerto, cifrado, credenciales de cuenta y Next"><figcaption><p>Complete los campos necesarios de servidor y cuenta antes de Next. El área de contraseña está oculta; en este ejemplo no se han enviado credenciales de buzón.</p></figcaption></figure>

El icono de copia junto a **Password** copia al portapapeles la contraseña introducida. **Cancel** o el icono de cierre abandonan este asistente de conexión nueva sin guardarla.

3. Haga clic en **Next** para abrir **Options**. Elija si desea **Merge attached documents** o **Block duplicate filename import**. **Email Notification** habilita un correo de confirmación tras la importación; actívelo solo cuando ese comportamiento sea el deseado.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-options-en-20261030.png" alt="Paso Options de IMAP con Merge attached documents, filtrado de nombres de archivo duplicados, Email Notification, Back y Next"><figcaption><p>Options separa el comportamiento de importación de la notificación por correo. En este ejemplo sin guardar, ambas casillas y el conmutador de notificación están desactivados.</p></figcaption></figure>

4. Haga clic en **Next** para abrir **Config**. Seleccione las **Sub-Organizations** necesarias, revise la **API Key** existente, defina el destinatario de los errores de importación y compruebe **Document Routing**. Despliegue **Advanced Settings** solo cuando el proceso necesite opciones adicionales.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-config-en-20261030.png" alt="Paso Config de IMAP con organización, clave API oculta, notificaciones de error, Document Routing, Advanced Settings y Save"><figcaption><p>Config reúne la asignación de organización, la clave existente, las notificaciones de error y el enrutamiento. La clave está oculta y no se ha usado Save.</p></figcaption></figure>

En **Config**, el icono del ojo muestra u oculta la **API Key** existente, y **Copy** la copia al portapapeles. Ninguno de los dos controles genera una clave nueva.

5. Haga clic en **Save** cuando la configuración esté lista. A continuación, use **Activate** en el menú **Actions** de la conexión guardada para iniciar el procesamiento automático.

En una conexión IMAP guardada, **Edit** ofrece opciones de carpeta y de tratamiento posterior a la importación. Seleccione la carpeta de origen y la carpeta de destino de los correos movidos solo después de crear la conexión y de que se puedan cargar las carpetas disponibles.

### Acciones para IMAP

El menú **Actions** de la conexión guardada ofrece **Test Connection**, **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** y **Delete**. La prueba de conexión contacta con el buzón configurado; la activación habilita el procesamiento. Revise los registros antes de reintentar una importación fallida.

### Añadir nueva conexión OAuth Office365

1. Haga clic en **New** en **Email Import** y seleccione **OAuth Office365** en **Protocol**. Para una aplicación de inquilino gestionada por el administrador, seleccione **OAuth Office365 - Tenant** y siga [O365 Tenant](o365-tenant.md).
2. Revise **Document Routing** antes de la autenticación.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-oauth-before-authentication-en-20261030.png" alt="Configuración de OAuth Office365 con Document Routing y el botón Authenticate antes de la autenticación de Microsoft"><figcaption><p>Seleccione la ruta antes de Authenticate. Esta vista es anterior al inicio de sesión; no se ha iniciado ninguna autenticación de Microsoft.</p></figcaption></figure>

3. Haga clic en **Authenticate** cuando la conexión del buzón esté autorizada. Complete el inicio de sesión de Microsoft con código de dispositivo usando el código que muestra DocBits y, después, vuelva y seleccione **Finish Authentication**.
4. Tras la autenticación, revise las opciones de organización, carpeta, buzón compartido, carpeta de destino y notificación de errores que se ofrecen para la conexión. Use **Next** para continuar a **Config** cuando esté disponible y, a continuación, guarde los ajustes deseados.
5. Active la conexión guardada cuando deban ejecutarse importaciones automáticas. **Import**, cuando se ofrece para una conexión guardada, inicia una importación real; úselo de forma deliberada.

### Acciones para OAuth Office365

El menú **Actions** de la conexión guardada ofrece **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** y **Delete**. La desactivación detiene el procesamiento automático; la eliminación suprime la configuración.

### Import Log

Use el icono de registro en la esquina superior derecha de **Email Import** para revisar las importaciones de todas las conexiones de buzón configuradas. Use la acción **Import Log** de una fila guardada para esa conexión. Inspeccione el asunto, el remitente, el estado y los detalles de error disponibles antes de decidir si desea reintentar.

## Inbound Emails

Las dos capturas del tutorial siguientes muestran la dirección entrante de DocBits y sus registros. Esto es independiente de las conexiones de buzón anteriores.

* Use el icono de copia junto a **E-Mail** para copiar la dirección de recepción que se muestra para la organización y el entorno actuales.
* **Add** inserta otra fila de remitente permitido en el formulario. Elija su remitente y la suborganización deseada y, a continuación, use **Save** para guardar la configuración. Añadir una fila por sí solo no la guarda.
* **Logs** abre el registro de correos entrantes. **Errors** filtra por errores; **Inbound** y **Outbound** seleccionan la dirección de los mensajes.
* Despliegue una fila del registro con su chevron para inspeccionar los detalles del archivo adjunto. El icono de copia junto al identificador de seguimiento copia ese identificador para la resolución de problemas. **Original email**, cuando está disponible para una fila de entrada, descarga el mensaje original seleccionado como archivo `.eml`; no reintenta la importación.

## Videotutorial: Inbox de correo y resolución de errores

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/es.mp4" %}
Inbox de correo y resolución de errores
{% endembed %}

[Ver con subtítulos y navegación por capítulos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/es.html)

Algunas etiquetas nativas del producto pueden permanecer en otro idioma. Se conservan los identificadores técnicos de los campos.

En ajustes e importación, en este ejemplo utilizo la dirección entrante de DocBits. Un buzón conectado directamente es un método de importación distinto. Para esta formación, trabajo en una organización de demostración dedicada con facturas sintéticas. Las notificaciones permanecen desactivadas.

Primero compruebo la dirección de recepción mostrada y el alcance. La dirección pertenece exactamente a esta organización y a su entorno. Para otra empresa o un entorno de producción, siempre utilizo la dirección que se muestra realmente allí.

Aquí restringo la Inbox a nuestro remitente de prueba aprobado. Solo selecciono la asignación a una suborganización si pertenece al proceso previsto. Guardo el ajuste y lo abro de nuevo. El remitente permitido se ha conservado; los correos de respuesta automática siguen desactivados en esta formación.

<figure><img src="../../../../.gitbook/assets/admin-save-en-accounting-email-v1.png" alt="Remitente permitido guardado con las notificaciones desactivadas"><figcaption><p>Remitente permitido guardado con las notificaciones desactivadas</p></figcaption></figure>

Para esta formación, se ha enviado un mensaje de prueba directamente al procesamiento de correos entrantes de DocBits. Esta prueba no confirma la entrega de correo externo. En el registro compruebo el asunto, el remitente y el archivo adjunto importado que coinciden. Después compruebo el documento que se ha creado realmente.

Abro el documento correspondiente y comparo el archivo adjunto PDF con la factura en DocBits. El nombre del archivo, el número de factura, el proveedor y el importe deben coincidir. Una importación correcta no dice nada sobre una aprobación ni sobre un registro en el ERP.

Una segunda prueba controlada procede de un remitente no aprobado. En el registro busco específicamente esta entrada y activo el filtro de errores. Los detalles indican el remitente rechazado. Compruebo la causa utilizando el asunto y el identificador de seguimiento, en lugar de desencadenar la importación varias veces.

En un caso real, primero aclaro si este remitente está siquiera autorizado. Un cambio aprobado en la lista de remitentes se guarda y se comprueba de nuevo. Después verifico una nueva entrada de prueba única hasta el documento creado. Para errores técnicos, entrego el identificador de seguimiento y el mensaje de error concreto.

<figure><img src="../../../../.gitbook/assets/admin-error-en-accounting-email-v1.png" alt="Importación fallida con adjunto, motivo e identificador de seguimiento"><figcaption><p>Importación fallida con adjunto, motivo e identificador de seguimiento</p></figcaption></figure>
