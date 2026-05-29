# Asignación por código de barras

### Descripción general

La opción **Asignación por código de barras** (Barcode Assignment) añade una herramienta de códigos de barras a la **pantalla de validación de documentos**. Lee los códigos de barras y códigos QR encontrados en un documento y le permite **asignar sus valores a los campos del documento** — por ejemplo, rellenar un número de referencia, de pedido o de albarán a partir de un código de barras en lugar de escribirlo.

Esta opción está **desactivada de forma predeterminada**.

### ¿Qué hace?

Cuando esta opción está activada, aparece un pequeño **botón de código de barras** (un icono de código QR) en la barra de herramientas mientras valida un documento. Al hacer clic en él se muestran los códigos de barras que DocBits encontró en el documento, y puede asignar cada uno a un campo. El campo se rellena entonces con el valor leído del código de barras.

* **Activada** — El botón de código de barras se muestra en la pantalla de validación. Puede leer los códigos de barras del documento y asignar sus valores a los campos.
* **Desactivada** — El botón se oculta y los valores de los códigos de barras no se ofrecen para su asignación durante la validación.

{% hint style="info" %}
**Esto sirve para leer un valor de código de barras/QR y asignarlo a un campo durante la validación.** La extracción automática de datos estructurados de códigos de pago (como Swiss QR Bill o GiroCode) — y la división de un archivo de varias páginas en las páginas separadoras con código de barras — las gestiona una opción **diferente**: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Beneficios

* **Entrada más rápida y sin errores**: Tome los valores directamente de un código de barras en lugar de leerlos y escribirlos a mano.
* **Menos errores tipográficos**: Un valor escaneado es exactamente lo que está codificado en el código de barras.
* **Mantiene el control**: Usted decide qué código de barras va en qué campo durante la validación.

### Cómo usarla

1. Vaya a **Configuración**.
2. Seleccione **Procesamiento de documentos**.
3. Seleccione **Módulo**.
4. Abra la sección **Tipo de documento**.
5. Busque **Asignación por código de barras** y active el interruptor.
6. Después, al validar un documento, haga clic en el **botón de código de barras** de la barra de herramientas y asigne los valores de los códigos de barras detectados a los campos correspondientes.

### Cuándo usar esta función

* **Documentos con códigos de barras**: Cuando sus documentos llevan códigos de barras/QR cuyos valores pertenecen a campos específicos (p. ej., números de pedido o de referencia).
* **Flujos de validación manual**: Cuando una persona revisa documentos y quiere rellenar campos rápidamente a partir de códigos de barras.
* **Déjela desactivada** si sus documentos no tienen códigos de barras útiles, o si solo necesita la **extracción** automática de códigos de barras/QR — consulte [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
