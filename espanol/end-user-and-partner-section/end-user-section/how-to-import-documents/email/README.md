---
hidden: true
noIndex: true
---

# Correo electrónico

DocBits puede importar documentos desde el correo electrónico de dos maneras. Ambas se configuran en **Configuración → Importar** (Procesamiento de documentos).

## Método 1 — Importación por correo (conectar un buzón)

Conecte una cuenta de correo y DocBits importará los documentos automáticamente a medida que lleguen nuevos correos. En la página de Importación, abra la sección **Importación por correo** y haga clic en **+ Nuevo**.

<figure><img src="../../../../.gitbook/assets/email_import_section.png" alt="Sección Importación por correo"><figcaption>Importación por correo: conecte un buzón para la importación automática de documentos</figcaption></figure>

A continuación, elija el protocolo de su buzón:

* **IMAP** — consulte [IMAP](imap.md)
* **OAuth (Office 365)** — consulte [OAuth Office365](oauth-office365.md)

## Método 2 — Correos entrantes (reenviar a DocBits)

Reenvíe —o envíe directamente— los correos a la dirección de entrada única de su organización y DocBits importará los archivos adjuntos automáticamente. No se requiere conectar ningún buzón. Abra la sección **Correos entrantes** en la página de Importación.

<figure><img src="../../../../.gitbook/assets/inbound_emails_section.png" alt="Sección Correos entrantes"><figcaption>Correos entrantes: reenvíe documentos a su dirección de DocBits</figcaption></figure>

* **Info / Correo** — la dirección de entrada única de su organización (formato `<org-id>@inbound.docbits.com`). Reenvíe sus documentos a esta dirección; use el icono de copiar para copiarla.
* **Importar documentos solo desde correos predefinidos** — cuando está activado, solo se importan los correos de los remitentes que añada a la lista blanca; los correos de cualquier otro remitente se ignoran.
* **Responder a este correo si la importación no es posible** — envía una respuesta automática al remitente cuando la importación falla.
* **Notificar al remitente cuando la importación falle** — notifica al remitente si su correo no se pudo importar.
* **Registros** — abre el registro de procesamiento de correos entrantes. Haga clic en **Guardar** para aplicar los cambios.

## Documentos adjuntos admitidos

Ambos métodos de importación por correo aceptan estos documentos adjuntos:

| Formato | Extensiones de archivo | Uso habitual |
| --- | --- | --- |
| PDF | `.pdf` | Facturas y otros documentos PDF |
| TIFF | `.tif`, `.tiff` | Documentos escaneados |
| XML | `.xml` | Documentos electrónicos estructurados |
| EDI / datos de pedidos | `.edi`, `.purchaseorder` | Intercambio electrónico de datos y pedidos de compra |

Si un servicio de reenvío etiqueta un archivo PDF, TIFF o XML como adjunto genérico, DocBits puede identificarlo por el contenido del archivo o una extensión conocida. Los mensajes `.eml` reenviados también pueden contener documentos admitidos; DocBits extrae esos adjuntos internos antes de la importación.

Las imágenes como PNG, JPG, GIF y BMP no se importan como documentos. Las imágenes de firma y los logotipos insertados en los correos reenviados se omiten. Los archivos de Office como Word, Excel y PowerPoint no son compatibles con estos métodos de importación por correo.

En los correos reenviados, consulte **Registros** en **Correos entrantes** si falta un documento. Cuando **Notificar al remitente cuando la importación falle** está activado, el remitente recibe una explicación y un enlace a esta página. Para un buzón conectado, use la guía de configuración de [IMAP](imap.md) o [OAuth (Office 365)](oauth-office365.md).
