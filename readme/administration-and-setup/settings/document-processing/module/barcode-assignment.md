# Asignación por código de barras

### Descripción general

La opción **Asignación por código de barras** (Barcode Assignment) permite que DocBits utilice los **códigos de barras dentro de un archivo para separarlo en documentos individuales**. Resulta útil cuando se escanean varios documentos juntos en un único PDF grande y un código de barras marca dónde termina un documento y comienza el siguiente.

Esta opción está **desactivada de forma predeterminada**.

### ¿Qué hace?

Cuando esta opción está activada, DocBits busca códigos de barras en un archivo entrante de varias páginas y lo divide en documentos separados en las posiciones marcadas. Cada documento resultante se procesa después por separado.

* **Activada** — DocBits detecta los códigos de barras y separa automáticamente un archivo combinado en documentos individuales según ellos.
* **Desactivada** — El archivo se procesa como un único documento; los códigos de barras no se utilizan para dividirlo.

{% hint style="info" %}
Esto trata de **dividir y asignar** páginas según los códigos de barras. La lectura de los datos codificados en un código de barras (por ejemplo, para códigos QR de pago) se gestiona por separado en **Bar-Code / QR Code Extraction**.
{% endhint %}

### Beneficios

* **Escaneo por lotes más rápido**: Escanee una pila completa de documentos en una sola pasada, separados por hojas con código de barras, en lugar de escanear cada documento individualmente.
* **Menos clasificación manual**: DocBits crea los documentos individuales por usted, por lo que nadie tiene que dividir el PDF a mano.
* **Menos errores**: Los documentos se separan exactamente en las posiciones marcadas cada vez.

### Cómo usarla

1. Vaya a **Configuración**.
2. Seleccione **Procesamiento de documentos**.
3. Seleccione **Módulo**.
4. Abra la sección **Tipo de documento**.
5. Busque **Asignación por código de barras** y active el interruptor.

### Cuándo usar esta función

* **Escaneo de gran volumen**: Cuando escanea muchos documentos juntos y utiliza hojas separadoras con código de barras entre ellos.
* **Lotes mixtos**: Cuando un único archivo entrante contiene varios documentos distintos que deben procesarse por separado.
* **Déjela desactivada** si sus documentos siempre llegan como archivos separados: en ese caso no es necesario dividir.
