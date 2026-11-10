# Guía del archivo Structure Descriptor de EDI

## 1. Descripción general

El **archivo Structure Descriptor** es un archivo **JSON** que define cómo se agrupan los segmentos EDI repetidos (por ejemplo `N1`–`N4`) en una salida estructurada. Es el primer paso del procesamiento EDI:

* **Análisis preciso** de los segmentos relacionados como unidades individuales.
* **Salida consistente** para la [Transformation](../edi-transformation-file-guide.md) y los sistemas posteriores.

_Encontrará un ejemplo completo con el detalle de los segmentos en_ [_Structure Descriptor Example_](edi-structure-descriptor.md)_._

## 2. Acceso y edición básica

#### **Acceso al archivo**

1. Vaya a **Settings** → **Document Types** y abra **E-Doc** para el tipo de documento que desea configurar (por ejemplo, _Purchase Order_). Necesita acceso de administrador en su organización para editar estos archivos.

    <!-- dbdc-139-edi-sd-list-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-list-en.png" alt="Página E-Doc del Sandbox en inglés con el formato EDI desplegado y la fila del JSON STRUCTURE DESCRIPTOR listada sobre TRANSFORMATION, PREVIEW y EXTRACTION PATHS"><figcaption>Abra E-Doc para su tipo de documento; el formato EDI enumera sus archivos de configuración.</figcaption></figure>

2. Despliegue el formato **EDI**. Sus archivos de configuración aparecen juntos: **STRUCTURE DESCRIPTOR**, **TRANSFORMATION**, **PREVIEW** y **EXTRACTION PATHS**.
3. Haga clic en la fila **STRUCTURE DESCRIPTOR**, marcada como **JSON**, para abrirla.

#### **Gestión de borradores**

La columna izquierda muestra la lista de **Version** del archivo. La versión marcada como **Active** es la que utiliza DocBits.

* **Crear un borrador**: haga clic en el icono de lápiz ✏️ que está junto a la versión activa para empezar a editar. El archivo activo no se puede editar directamente.
* **Eliminar borradores**: utilice el icono de papelera 🗑️ para quitar los borradores que no utilice.
* **Activar cambios**: haga clic en el icono de marca de verificación ✅ de un borrador para aprobar y publicar los cambios.
  * <mark style="color:red;">**Nota**</mark>: al activar una versión nueva, la anterior se **desactiva automáticamente**.

<!-- dbdc-139-edi-sd-detail-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-detail-en.png" alt="Editor JSON de Structure Descriptor del Sandbox en inglés con la lista de versiones a la izquierda, donde la versión 1 aparece marcada como Active y hay un icono de lápiz para crear un borrador"><figcaption>El archivo Structure Descriptor con su lista de versiones; el lápiz crea un borrador que puede editar.</figcaption></figure>

## 3. Función Preview (salida analizada)

La **función Preview** le permite comprobar cómo se analiza un archivo EDI cargado con el Structure Descriptor que se muestra en ese momento, antes de activar cualquier cambio.

#### Uso

* Cargue un archivo EDI mediante el proceso de carga habitual.
* Copie el **Document ID** del archivo cargado.
* Abra el archivo **Structure Descriptor** tal como se describe más arriba.
* Haga clic en **Preview**, en la esquina superior derecha, para abrir el panel de prueba.

    <div align="left"><!-- dbdc-139-edi-sd-preview-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-preview-en.png" alt="Página Structure Descriptor del Sandbox en inglés con el panel de prueba Preview abierto, donde se ven el campo Document Id y el botón Test" width="560"><figcaption>El panel de prueba: introduzca un Document ID y pulse Test.</figcaption></figure></div>

* Introduzca el **Document ID** en el campo y pulse **Test**.
* La **salida estructurada** resultante aparece junto al editor.

Esto resulta especialmente útil para depurar los mappings y validar las agrupaciones estructurales en tiempo real. Se requiere un documento EDI representativo de su propio formato; el resultado mostrado depende del archivo cargado.

## 4. Recorrido en vídeo

En la [página de vídeos](../edi-videos.md) encontrará una guía en vídeo para este tipo de archivo.\
Úsela para seguir la configuración, la edición y el uso de Preview.

Las imágenes muestran una configuración y una versión ya existentes. Los ajustes varían según el tipo de documento y el formato. Valide los cambios en un borrador antes de activarlos.
