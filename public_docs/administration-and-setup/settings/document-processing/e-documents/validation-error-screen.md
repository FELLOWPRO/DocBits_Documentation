# La pantalla de error de una factura electrónica rechazada

> En esta versión, algunos textos de la interfaz pueden seguir en inglés o contener traducciones incorrectas. La guía explica su significado; las capturas muestran la interfaz sin modificar.

> El botón «Crear billete» de algunas versiones abre un ticket de soporte.

Cuando carga una factura electrónica incorrecta, DocBits no la pierde. El documento recibe el estado **Error** y la pantalla de error le indica qué está mal, dónde y qué hacer a continuación. Esta página muestra dos ejemplos: un archivo XML que no está bien formado y una factura que infringe una regla de negocio.

> Una factura recibe el estado **Error** solo cuando la validación está **activada** y **bloquea** para su tipo de documento. Consulte [Validación para cada tipo de documento](validation-per-document-type.md).

## Ejemplo 1: el archivo XML está dañado

Un proveedor envía un archivo XML en el que una etiqueta de cierre no coincide con su etiqueta de apertura. El archivo no se puede leer, por lo que DocBits se detiene en la primera comprobación, **L1 · Bien formado**.

<figure><img src="../../../../.gitbook/assets/einvoice-error-xml-malformed-es-20261104-v2.png" alt="Pantalla de error de un XML ficticio con una etiqueta de cierre dañada intencionadamente. En esta versión, algunos textos de la interfaz pueden seguir en inglés o contener traducciones incorrectas. La guía explica su significado; las capturas muestran la interfaz sin modificar."><figcaption><p>Pantalla de error de un XML ficticio con una etiqueta de cierre dañada intencionadamente. En esta versión, algunos textos de la interfaz pueden seguir en inglés o contener traducciones incorrectas. La guía explica su significado; las capturas muestran la interfaz sin modificar.</p></figcaption></figure>

La pantalla tiene dos lados:

* **Izquierda: el archivo XML.** DocBits muestra el archivo con números de línea. La línea con el problema está marcada en rojo. Use los botones situados sobre el archivo para copiar el XML o abrirlo en una pestaña nueva.
* **Derecha: la explicación.** La tarjeta **Rechazado por** indica la comprobación que detuvo el archivo (aquí **L1 · Bien formado**) y el código de la regla (aquí `XML-PARSE`). Debajo verá un título en lenguaje claro (*El XML no está bien formado*), una breve explicación y el bloque **Siguiente paso**.

Seleccione **Ver detalles de validación** para abrir el [informe de validación](validation-report.md) completo.

<figure><img src="../../../../.gitbook/assets/einvoice-report-xml-malformed-es-20261104-v2.png" alt="Informe del archivo XML ficticio dañado."><figcaption><p>Informe del archivo XML ficticio dañado.</p></figcaption></figure>

El informe indica la posición exacta (la línea y la columna figuran en el informe) y el mensaje técnico del analizador XML. Seleccione **Mostrar en XML** para saltar a esa línea. La indicación **Cómo solucionarlo** le dice que solicite al remitente un archivo corregido.

## Ejemplo 2: la factura infringe una regla de negocio

El XML es correcto, pero falta un campo obligatorio. Por ejemplo, no se puede identificar al vendedor porque no hay identificador del vendedor, identificador de registro ni identificador de IVA (regla `BR-CO-26`).

<figure><img src="../../../../.gitbook/assets/einvoice-error-view-es-20261104-v2.png" alt="Pantalla de error de una factura de ejemplo totalmente ficticia. En esta versión, algunos textos de la interfaz pueden seguir en inglés o contener traducciones incorrectas. La guía explica su significado; las capturas muestran la interfaz sin modificar."><figcaption><p>Pantalla de error de una factura de ejemplo totalmente ficticia. En esta versión, algunos textos de la interfaz pueden seguir en inglés o contener traducciones incorrectas. La guía explica su significado; las capturas muestran la interfaz sin modificar.</p></figcaption></figure>

La tarjeta muestra el primer resultado bloqueante. El informe completo también incluye el código `BR-CO-26` y los demás resultados de la factura.

## Los botones debajo de la tarjeta

| Botón | Qué hace |
| --- | --- |
| **Reiniciar procesamiento** | Ejecuta de nuevo el procesamiento del documento, por ejemplo después de cambiar un ajuste. La comprobación usa los ajustes actuales. |
| **Ver DocFlow** | Muestra el flujo de trabajo del documento. |
| **Copiar detalles** | Copia los detalles del error, por ejemplo para un mensaje a su administrador. |
| **Crear ticket de soporte** | Abre un ticket de soporte con los detalles del error. |

Seleccione **Mostrar detalles técnicos** en la tarjeta para ver la información técnica sin procesar.

## Qué hacer a continuación

* **Errores:** solicite al remitente una factura corregida o [rechace el documento](validation-next-step-and-reject.md). Una factura corregida es un documento nuevo.
* **Solo advertencias:** el documento no está bloqueado. Puede continuar.

## Páginas relacionadas

* [Informe de validación](validation-report.md): todos los hallazgos, nivel por nivel.
* [Siguiente paso y rechazar un documento](validation-next-step-and-reject.md)
* [Validación para cada tipo de documento](validation-per-document-type.md): active la validación y defina el bloqueo.
