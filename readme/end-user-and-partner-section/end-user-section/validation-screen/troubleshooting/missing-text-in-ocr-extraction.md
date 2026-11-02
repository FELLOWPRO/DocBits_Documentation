# Texto faltante en la extracción de OCR

## **Problema**

En algunos casos, el texto puede parecer estar faltante en la **Vista de OCR**, lo que impide que se extraiga utilizando la función de extracción.


<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_5-es.png" alt="Comprobación de campos extraídos en una factura ficticia."><figcaption><p>Comprobación de campos extraídos en una factura ficticia.</p></figcaption></figure>


Para verificar esto, haga clic en el botón **Vista de OCR** en la barra de herramientas a la derecha. Si el texto no aparece allí, significa que no está disponible para la extracción.


<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_6-es.png" alt="Vista OCR del texto reconocido de la factura ficticia."><figcaption><p>Vista OCR del texto reconocido de la factura ficticia.</p></figcaption></figure>


## **Causa**

La causa más probable es que el texto que está intentando extraer es parte de una imagen (por ejemplo, un logo o una sección escaneada) dentro del documento.\
Cuando la función E-Text está habilitada, el texto que aparece en imágenes o logos no se incluye en la capa de texto extraído. Como resultado, este texto no puede ser accedido o extraído a través de la lógica de extracción estándar.

## **Solución**

Para resolver este problema, desactive la función E-Text—ya sea para el [proveedor específico](missing-text-in-ocr-extraction.md#desactivar-e-text-para-un-proveedor-especifico) o para [toda la organización](missing-text-in-ocr-extraction.md#desactivar-e-text-para-toda-la-organizacion). Una vez que E-Text esté desactivado, DocBits dependerá únicamente de OCR, que es capaz de extraer texto de imágenes y logos dentro del documento.

### **Desactivar E-Text para un Proveedor Específico**

1. Abra un documento del proveedor específico en la **Validación de Campo**.
2.  Haga clic en el menú de tres puntos en la barra de herramientas a la derecha.



<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_2-es.png" alt="Acceso a las opciones adicionales de la validación."><figcaption><p>Acceso a las opciones adicionales de la validación.</p></figcaption></figure>


3.  Desmarque **Utilice E-Text si está disponible**.



<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_3-es.png" alt="Opción de utilizar E-Text cuando esté disponible."><figcaption><p>Opción de utilizar E-Text cuando esté disponible.</p></figcaption></figure>


4.  Haga clic en **Confirmar** para reiniciar el procesamiento del documento.



<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_4-es.png" alt="Diálogo de confirmación antes de cambiar el uso de E-Text."><figcaption><p>Diálogo de confirmación antes de cambiar el uso de E-Text.</p></figcaption></figure>


### Desactivar E-Text para toda la Organización

1.  Vaya a **Ajustes → Procesamiento de documentos → Configuración de OCR**.



<figure><img src="../../../../.gitbook/assets/s150-settings_ocr-es.png" alt="Configuración de OCR en español."><figcaption><p>Configuración de OCR en español.</p></figcaption></figure>


2.  En **Configuración general del OCR**, desmarque la opción **Utilice E-Text si está disponible**.



<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_1-es.png" alt="Configuración general de OCR y uso de E-Text."><figcaption><p>Configuración general de OCR y uso de E-Text.</p></figcaption></figure>


Las imágenes usan una factura ficticia con texto OCR disponible. Muestran comprobaciones de la interfaz, no un incidente reproducido de texto ausente.
