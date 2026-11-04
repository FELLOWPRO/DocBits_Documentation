# Solución de problemas

Si falta un valor en la pantalla de validación, compruebe primero si el texto es visible en el documento y si DocBits lo ha reconocido. Esto le ayuda a distinguir un problema de lectura de un problema de campo o de regla.

1. Abra el documento afectado en **Validation**.
2. Compare el documento original con **OCR view**. Revise la misma página y la misma zona donde debería aparecer el valor.
3. Si el texto no aparece en OCR view, siga [Missing Text in OCR Extraction](missing-text-in-ocr-extraction.md).
4. Si el texto aparece en OCR view pero el campo sigue vacío, pida a un administrador que revise la configuración de campos del tipo de documento. Indique el tipo de documento, el nombre del campo, la página y un ejemplo de prueba seguro.

<figure><img src="../../../../.gitbook/assets/dbdc238-validation-ocr-en.png" alt="Vista OCR en inglés de una factura sintética en Validation"><figcaption>Vista OCR actual en inglés de Sandbox de una factura sintética Test A. El ejemplo sirve de orientación; no muestra una extracción fallida.</figcaption></figure>

No incluya documentos de clientes ni datos personales en una captura de pantalla para soporte. La [descripción general de la pantalla de validación](../README.md) explica los controles principales si es la primera vez que usa esta pantalla.
