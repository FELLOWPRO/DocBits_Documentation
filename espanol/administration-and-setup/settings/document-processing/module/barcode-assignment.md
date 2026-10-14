# Asignación por código de barras

### Descripción general

La opción **Asignación por código de barras** (Barcode Assignment) añade una herramienta de códigos de barras a la **pantalla de validación de documentos**. Lee los códigos de barras y códigos QR encontrados en un documento y le permite **asignar sus valores a los campos del documento** — por ejemplo, rellenar un número de pedido, de referencia o de albarán a partir de un código de barras en lugar de escribirlo.

Esta opción está **desactivada de forma predeterminada**.

### Qué obtiene al activarla

Una vez activada la opción, aparece un nuevo **botón de código de barras** (un icono de código QR) en la barra de herramientas del lado derecho de la **pantalla de validación** (`/field_validation_v1/…`). Este botón es el punto de entrada a toda la función — sin la opción, el icono permanece oculto.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_icon.png" alt="El icono de código de barras (QR) en la barra de herramientas de validación"><figcaption><p>Con la opción activada, el icono de código de barras aparece en la barra de herramientas de validación.</p></figcaption></figure>

Aquí está el icono en su contexto, en la pantalla de validación, junto al documento que se está revisando:

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_screen.png" alt="Pantalla de validación con el icono de código de barras disponible"><figcaption><p>La pantalla de validación — el icono de código de barras (resaltado, barra de herramientas derecha) solo se muestra cuando la Asignación por código de barras está activada.</p></figcaption></figure>

### Cómo se leen los códigos de barras

DocBits detecta los códigos de barras durante el procesamiento del documento y ofrece sus valores decodificados para la asignación. Un mismo documento puede llevar varios tipos de código de barras — por ejemplo, un **código QR**, un **Code 128** y un **EAN-13** — cada uno codificando un valor distinto, como un número de pedido, un número de factura o un GLN de proveedor.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_demo_invoice.png" alt="Factura de demostración con varios tipos de código de barras"><figcaption><p>Factura de demostración de DocBits con tres tipos de código de barras (código QR → número de pedido, Code 128 → número de factura, EAN-13 → GLN de proveedor), cada uno codificando un valor que puede asignar a un campo.</p></figcaption></figure>

{% hint style="info" %}
Qué tipos de código de barras se detectan lo controla la opción **Bar-Code / QR Code Extraction** (`Barcode Extraction Types`). Si el diálogo muestra *«no barcodes extracted found»*, asegúrese de que la extracción de códigos de barras está activada y de que los tipos esperados (p. ej., `QRCODE`, `CODE128`, `EAN13`) están seleccionados. Consulte [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Uso del diálogo de Asignación por código de barras

1. Abra un documento en la **pantalla de validación**.
2. Haga clic en el **icono de código de barras** de la barra de herramientas derecha.
3. El diálogo **Asignación por código de barras** lista cada código de barras que DocBits detectó en el documento, mostrado como `Barcode <n> : <valor>`.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_dialog.png" alt="Diálogo de Asignación por código de barras con los códigos detectados"><figcaption><p>El diálogo de Asignación por código de barras lista cada código detectado con una lista desplegable para elegir el campo de destino.</p></figcaption></figure>

4. Para cada código de barras, abra su lista desplegable y elija el campo al que debe ir el valor.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_options.png" alt="Elegir el campo de destino para un código de barras"><figcaption><p>Cada código de barras puede asignarse a cualquier campo del documento — p. ej., Número de pedido, Número de factura, ID de proveedor.</p></figcaption></figure>

5. En cuanto selecciona un campo, este se rellena con el valor del código de barras.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_mapped.png" alt="Código de barras asignado al campo Número de pedido"><figcaption><p>Tras seleccionar un campo (aquí Número de pedido), el campo se rellena con el valor del código de barras.</p></figcaption></figure>

### Cómo activarla

1. Vaya a **Configuración**.
2. Seleccione **Procesamiento de documentos**.
3. Seleccione **Módulo**.
4. Abra la sección **Tipo de documento**.
5. Busque **Asignación por código de barras** y active el interruptor.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_toggle.png" alt="Interruptor de Asignación por código de barras"><figcaption><p>El interruptor de Asignación por código de barras en Configuración → Procesamiento de documentos → Módulo.</p></figcaption></figure>

### Beneficios

* **Entrada más rápida y sin errores**: Tome los valores directamente de un código de barras en lugar de leerlos y escribirlos a mano.
* **Menos errores tipográficos**: Un valor escaneado es exactamente lo que está codificado en el código de barras.
* **Mantiene el control**: Usted decide qué código de barras va en qué campo durante la validación.

### Cuándo usar esta función

* **Documentos con códigos de barras**: Cuando sus documentos llevan códigos de barras/QR cuyos valores pertenecen a campos específicos (p. ej., números de pedido o de referencia).
* **Flujos de validación manual**: Cuando una persona revisa documentos y quiere rellenar campos rápidamente a partir de códigos de barras.
* **Déjela desactivada** si sus documentos no tienen códigos de barras útiles, o si solo necesita la **extracción** automática de códigos de barras/QR — consulte [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).

{% hint style="info" %}
**Esto sirve para leer un valor de código de barras/QR y asignarlo a un campo durante la validación.** La extracción automática de datos estructurados de códigos de pago (como Swiss QR Bill o GiroCode) — y la división de un archivo de varias páginas en las páginas separadoras con código de barras — las gestiona una opción **diferente**: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}
