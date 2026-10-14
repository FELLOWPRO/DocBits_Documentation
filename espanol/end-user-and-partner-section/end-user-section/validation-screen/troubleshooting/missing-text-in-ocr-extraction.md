# Texto faltante en la extracción de OCR

## **Problema**

En algunos casos, el texto puede parecer estar faltante en la **Vista de OCR**, lo que impide que se extraiga utilizando la función de extracción.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_5.png)

Para verificar esto, haga clic en el botón **Vista de OCR** en la barra de herramientas a la derecha. Si el texto no aparece allí, significa que no está disponible para la extracción.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_6.png)

## **Causa**

La causa más probable es que el texto que está intentando extraer es parte de una imagen (por ejemplo, un logo o una sección escaneada) dentro del documento.\
Cuando la función E-Text está habilitada, el texto que aparece en imágenes o logos no se incluye en la capa de texto extraído. Como resultado, este texto no puede ser accedido o extraído a través de la lógica de extracción estándar.

## **Solución**

Para resolver este problema, desactive la función E-Text—ya sea para el [proveedor específico](missing-text-in-ocr-extraction.md#desactivar-e-text-para-un-proveedor-especifico) o para [toda la organización](missing-text-in-ocr-extraction.md#desactivar-e-text-para-toda-la-organizacion). Una vez que E-Text esté desactivado, DocBits dependerá únicamente de OCR, que es capaz de extraer texto de imágenes y logos dentro del documento.

### **Desactivar E-Text para un Proveedor Específico**

1. Abra un documento del proveedor específico en la **Validación de Campo**.
2.  Haga clic en el menú de tres puntos en la barra de herramientas a la derecha.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_2.png)
3.  Desmarque **Utilice E-Text si está disponible**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_3.png)
4.  Haga clic en **Confirmar** para reiniciar el procesamiento del documento.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_4.png)

### Desactivar E-Text para toda la Organización

1.  Vaya a **Ajustes → Procesamiento de documentos → Configuración de OCR**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)
2.  En **Configuración general del OCR**, desmarque la opción **Utilice E-Text si está disponible**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_1.png)
