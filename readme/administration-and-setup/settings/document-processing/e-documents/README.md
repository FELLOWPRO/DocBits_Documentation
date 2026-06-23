# Documentos electrónicos

DocBits valida las facturas electrónicas entrantes (e-invoices) según los estándares oficiales —**XRechnung**, **ZUGFeRD** y **Factur-X**— y enruta cualquier problema que detecte al responsable adecuado. El grupo de ajustes **Documentos electrónicos** (en **Procesamiento de documentos**) tiene dos páginas:

* **[Reglas de validación](validation-rules.md)**: elija qué versiones y perfiles de factura electrónica acepta y establezca la gravedad de cada regla de validación para su organización.
* **[Enrutamiento de notificaciones](notification-routing.md)**: asigne los hallazgos de validación al agente de AI Workforce que debe gestionarlos.

Juntas le permiten decidir **qué se considera un problema** en una factura electrónica entrante y **quién se encarga de ello**.

## Activar o desactivar la validación de facturas electrónicas

Las dos páginas de Documentos electrónicos solo surten efecto una vez que la **validación de facturas electrónicas está activada para el tipo de documento**. El interruptor se encuentra en el propio tipo de documento, no en el menú Documentos electrónicos.

Vaya a **Ajustes → Tipos de documento → Factura → Ajustes avanzados** y abra la sección **Validación de facturas electrónicas**.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="Los interruptores de validación de facturas electrónicas en el tipo de documento Factura"><figcaption><p>Active o desactive la validación de facturas electrónicas por tipo de documento, con notificación opcional al proveedor</p></figcaption></figure>

* **Validar facturas electrónicas entrantes**: el interruptor principal. Cuando está **activado**, cada factura cargada se comprueba con las reglas Schematron de KoSIT XRechnung más las comprobaciones semánticas L0 (PDF/A-3) y L4 (IBAN/IVA), usando las gravedades que haya definido en la página [Reglas de validación](validation-rules.md). Las facturas no válidas se bloquean. Cuando está **desactivado**, las facturas omiten por completo la validación de facturas electrónicas y las páginas Reglas de validación y Enrutamiento de notificaciones no tienen efecto.
* **Notificar al proveedor en caso de rechazo**: aparece una vez activada la validación. Cuando está **activado**, una factura rechazada genera un correo al proveedor con los campos faltantes o incorrectos para que pueda volver a emitirla. Quién recibe y gestiona cada hallazgo se configura en la página [Enrutamiento de notificaciones](notification-routing.md).

> La validación de facturas electrónicas se configura **por tipo de documento**. Actualmente se aplica al tipo de documento **Factura**; actívela en cada tipo de documento que deba validarse.
