# Omitir la extracción de XML de PDF híbridos

### Descripción general

La opción **Omitir la extracción de XML de PDF híbridos** (Skip Hybrid PDF XML Extraction) controla cómo DocBits procesa los **PDF híbridos**: facturas en PDF que llevan una factura electrónica estructurada incrustada (ZUGFeRD / Factur-X). Decide si el **XML estructurado dentro del PDF** es el documento principal para el procesamiento automático, o si se procesa el **propio PDF** mediante OCR como documento principal.

Esta opción es especialmente relevante para los **clientes de EE. UU.**. A diferencia de la UE/Alemania, Estados Unidos no tiene una obligación general de facturación electrónica B2B, por lo que las organizaciones estadounidenses suelen querer que el PDF se trate como la factura principal y legible para personas, incluso cuando una contraparte envía un archivo ZUGFeRD/Factur-X con XML incrustado.

### ¿Qué hace?

Un archivo ZUGFeRD/Factur-X es un único PDF que también contiene una factura XML legible por máquina. De forma predeterminada, DocBits detecta ese XML incrustado y lo utiliza como fuente principal para la extracción (ruta electrónica estructurada).

* **Desactivada (predeterminado)** — DocBits detecta el XML de la factura electrónica incrustado y procesa el documento por la **ruta electrónica estructurada**. El XML es la factura principal. Este es el comportamiento legalmente correcto para la UE/Alemania, donde la factura electrónica estructurada es la factura relevante y el PDF es solo una visualización / copia de lectura.
* **Activada** — DocBits **ignora el XML incrustado** y envía el documento al **procesador de PDF (OCR)**. El PDF se convierte en el documento de procesamiento principal. Esta es la opción habitual para las **organizaciones de EE. UU.** que desean un procesamiento centrado en el PDF.

{% hint style="info" %}
Esta opción solo afecta a los **PDF híbridos** (ZUGFeRD / Factur-X = un `.pdf` con XML incrustado). Un archivo XRechnung/EDI puro cargado como `.xml` siempre se procesa por la ruta electrónica estructurada: no hay ningún PDF que pueda convertirse en el documento principal.
{% endhint %}

### Auditoría y cumplimiento: el original siempre se conserva

Activar esta opción **no descarta** la factura electrónica. El artefacto original siempre se conserva:

* El **PDF** ZUGFeRD/Factur-X original, **incluido su XML incrustado, permanece almacenado** y descargable. No se elimina nada de la copia almacenada del documento.
* El procesamiento solo cambia **qué contenido impulsa la extracción** (PDF/OCR frente al XML incrustado), no lo que se archiva.

Así, una organización de EE. UU. puede procesar el PDF como principal mientras la factura electrónica estructurada permanece disponible para auditoría.

{% hint style="warning" %}
Para las organizaciones de la UE/Alemania, deje esta opción **desactivada**. Según las normas de facturación electrónica de 2025, una factura electrónica estructurada (ZUGFeRD/Factur-X, XRechnung) es la factura legalmente relevante; un PDF simple es solo una copia de lectura. Procesar el PDF como principal en lugar de los datos estructurados no es apropiado cuando existe una factura electrónica válida.
{% endhint %}

### Cómo usarla

1. **Abrir la opción**:
   * Vaya a **Configuración**.
   * Seleccione **Procesamiento de documentos**.
   * Seleccione **Módulo**.
   * Abra la sección **Tipo de documento**.
   * Busque **Omitir la extracción de XML de PDF híbridos** y active el interruptor.
2. **Elegir el modo**:
   * **Organizaciones de EE. UU. / centradas en PDF** → active el interruptor para que los PDF ZUGFeRD/Factur-X se procesen mediante OCR como documento principal.
   * **Organizaciones de la UE/Alemania** → deje el interruptor desactivado para que la factura electrónica estructurada siga siendo el documento principal.
3. **Verificar**:
   * Cargue un PDF ZUGFeRD/Factur-X y compruebe el resultado del procesamiento: con el interruptor activado se trata como un PDF normal (OCR); con él desactivado se extraen los datos de la factura electrónica incrustada.

### Cuándo usar esta función

* **Clientes de EE. UU. / sin obligación de factura electrónica**: actívela para que el PDF habitual sea el documento de procesamiento principal mientras la factura electrónica incrustada permanece archivada.
* **Flujos de trabajo mixtos/centrados en PDF**: actívela cuando los procesos posteriores, la validación o la revisión dependan del diseño del PDF en lugar del XML.
* **Cumplimiento UE/Alemania**: déjela desactivada para que los datos estructurados de la factura electrónica impulsen el procesamiento, como se exige.
