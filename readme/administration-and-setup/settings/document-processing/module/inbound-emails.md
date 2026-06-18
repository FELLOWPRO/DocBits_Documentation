# Correos electrónicos entrantes

### Descripción general

DocBits puede recoger documentos directamente del correo electrónico, sin necesidad de subirlos manualmente. Hay **dos formas** de incorporar documentos por correo, ambas en **Configuración → Procesamiento de documentos → Importar**:

| Método | Cómo funciona | Ideal para |
|--------|---------------|------------|
| **Cuenta de importación de correo** | DocBits se conecta a un buzón de su propiedad (**IMAP**, **OAuth Office365** u **OAuth Office365 – Tenant**) e importa los documentos que encuentra. | Un buzón dedicado que ya recibe sus documentos (p. ej. `facturas@suempresa.com`). |
| **Reenvío de correos (Correos entrantes)** | DocBits le proporciona una dirección única; cualquier remitente autorizado puede **reenviar** documentos a ella. | Reenvío puntual desde muchos remitentes sin compartir credenciales del buzón. |

Puede usar cada método por separado o ambos a la vez.

### Método 1 — Conectar un buzón (Importación de correo)

Vaya a **Configuración → Procesamiento de documentos → Importar** y abra la sección **Importación de correo**. Haga clic en **Nuevo** para añadir una conexión de buzón.

<figure><img src="../../../../.gitbook/assets/inbound_emails_email_import_entry.png" alt="Sección de importación de correo con el botón Nuevo"><figcaption><p>En la sección Importación de correo, haga clic en <strong>Nuevo</strong> para conectar un buzón.</p></figcaption></figure>

Se abre el asistente de configuración. El primer campo, **Protocolo**, determina cómo se conecta DocBits: elija **IMAP**, **OAuth Office365** u **OAuth Office365 – Tenant**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_protocol_select.png" alt="Lista desplegable de Protocolo con IMAP, OAuth Office365 y OAuth Office365 - Tenant"><figcaption><p>La lista <strong>Protocolo</strong> ofrece los tres tipos de conexión.</p></figcaption></figure>

#### IMAP

Para un buzón estándar, elija **IMAP** y rellene los datos del servidor y las credenciales de la cuenta:

* **Nombre del servidor** y **Puerto** (por defecto `993`) de su servidor de correo.
* **Encriptación**: `SSL`, `TLS` o `None`.
* **Nombre de usuario**, **correo electrónico** y **contraseña** del buzón.

<figure><img src="../../../../.gitbook/assets/inbound_emails_imap.png" alt="Formulario de conexión IMAP con servidor, puerto, encriptación y credenciales"><figcaption><p>El formulario IMAP: la conexión al servidor de correo más las credenciales del buzón.</p></figcaption></figure>

#### OAuth Office365

Para un único buzón de usuario de Microsoft 365, elija **OAuth Office365**. En lugar de una contraseña, autoriza a DocBits a través de Microsoft: elija el destino de **Enrutamiento de documentos**, luego haga clic en **Autenticar** y complete el inicio de sesión de Microsoft.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365.png" alt="Formulario OAuth Office365 con Enrutamiento de documentos y un botón Autenticar"><figcaption><p>OAuth Office365 se conecta mediante el inicio de sesión de Microsoft: en DocBits no se almacena ninguna contraseña.</p></figcaption></figure>

#### OAuth Office365 – Tenant

Para conectar a nivel de inquilino (organización) mediante un registro de aplicación de Azure, elija **OAuth Office365 – Tenant** e introduzca las credenciales de Azure: **ID de inquilino** (Tenant ID), **ID de aplicación cliente** (Client App ID) y **Valor de aplicación cliente** (secreto de cliente). Use **Probar conexión** para verificar y luego **Guardar**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365_tenant.png" alt="Configuración del inquilino de Azure con ID de inquilino, ID de aplicación cliente y Valor de aplicación cliente"><figcaption><p>OAuth Office365 – Tenant usa un registro de aplicación de Azure (ID de inquilino, ID de aplicación cliente, secreto de cliente).</p></figcaption></figure>

{% hint style="info" %}
El **Enrutamiento de documentos** decide adónde van los documentos importados: **DocBits** (el panel estándar) o **AI Workforce**. Tras conectarse, los siguientes pasos del asistente le permiten elegir de qué **carpeta** importar, un **buzón compartido** opcional y si se deben **mover** los correos procesados a otra carpeta.
{% endhint %}

### Método 2 — Reenviar correos a DocBits (Correos entrantes)

Este método requiere que primero esté activado el módulo **Correos entrantes**. Vaya a **Configuración → Procesamiento de documentos → Módulo**, abra la sección **Tipo de documento**, busque **Correos entrantes** y active el interruptor.

<figure><img src="../../../../.gitbook/assets/inbound_emails_1.png" alt="Activación del módulo Correos entrantes"><figcaption><p>Active <strong>Correos entrantes</strong> en Configuración → Procesamiento de documentos → Módulo.</p></figcaption></figure>

Una vez activado, aparece una sección **Correos entrantes** en **Configuración → Procesamiento de documentos → Importar**. Contiene todo lo necesario para recibir documentos reenviados:

<figure><img src="../../../../.gitbook/assets/inbound_emails_forward.png" alt="Sección Correos entrantes: dirección de importación, remitentes predefinidos y dirección de notificación de fallos"><figcaption><p>La sección Correos entrantes: su dirección de importación, la lista de remitentes predefinidos y la dirección de notificación de fallos.</p></figcaption></figure>

* **Dirección de importación**: una dirección única generada por el sistema con el formato `org_id@environment.inbound.docbits.com`. Reenvíe o envíe documentos a esta dirección y DocBits los importará automáticamente. Use el icono de copiar para obtenerla.
* **Importar documentos solo de correos predefinidos**: cuando está activado, solo se aceptan las direcciones de remitente que aparezcan aquí; los correos de cualquier otro se ignoran. Para cada remitente puede elegir una **Suborganización** (déjelo vacío para asignarlo a la organización principal). Use **Añadir** para listar más remitentes y **Eliminar** para quitar uno.
* **Responder a este correo si no se puede realizar la importación**: cuando está activado, introduzca una dirección que deba ser notificada cada vez que falle un intento de importación, para que los problemas no pasen desapercibidos.

Haga clic en **Guardar** para aplicar los cambios.

{% hint style="info" %}
**¿Qué adjuntos se importan?** DocBits importa adjuntos **PDF**, **TIFF** y **XML** (p. ej. facturas electrónicas eCOS / EDI), y descomprime los mensajes `.eml` reenviados para importar los documentos que contienen. La detección se basa en el **contenido real del archivo**, por lo que los adjuntos a los que un servidor de correo de reenvío reasigna un tipo genérico (`application/octet-stream`) se importan igualmente de forma correcta. Las imágenes en línea (logotipos de firma / gráficos incrustados) se ignoran. Consulte [Importar → Importación de correo](../import/README.md#email-import) para ver la lista completa y su comportamiento.
{% endhint %}

### Cuándo usar cada método

* **Use una cuenta de importación de correo** cuando los documentos ya lleguen a un buzón dedicado y quiera que DocBits los recoja por sí mismo: IMAP para servidores de correo genéricos, OAuth Office365 para Microsoft 365.
* **Use el reenvío de correos** cuando las personas deban reenviar documentos según sea necesario, o cuando no quiera compartir las credenciales del buzón con DocBits.
* **Combine ambos** si algunos documentos llegan a un buzón fijo mientras que otros se reenvían de forma puntual.

{% hint style="info" %}
Restringir los remitentes (Método 2) y elegir el destino correcto de **Enrutamiento de documentos** (Método 1) son las dos formas más habituales de mantener limpia una canalización entrante: solo los documentos que espera, dirigidos adonde usted quiere.
{% endhint %}
