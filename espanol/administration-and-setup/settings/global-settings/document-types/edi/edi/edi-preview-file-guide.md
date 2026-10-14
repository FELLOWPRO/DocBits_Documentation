# Guía de Archivo de Vista Previa EDI

## 1. Visión general

El **Archivo de Vista Previa** define cómo los datos XML estructurados se representan en un formato legible por humanos, similar a un PDF. Combina **HTML y CSS** para la presentación visual y utiliza declaraciones **XSLT** `**select**` para insertar dinámicamente datos desde el XML personalizado. Esta vista previa se muestra durante la **validación de campos** y también se incluye al exportar documentos a **IDM**.

## 2. Propósito y Función

* Convierte XML personalizado legible por máquina en una vista previa formateada visualmente (PDF).
* Permite la revisión y validación amigable para humanos de los datos extraídos.
* Asegura la representación consistente de campos clave del documento como encabezados, tablas, totales, etc.
* Se construye utilizando **HTML + CSS** para diseño y diseño, y **XSLT** para vincular datos al diseño.

## 3. Acceso y Edición Básica

#### **Accediendo al Archivo:**

1.  Ve a **Configuración** → **Tipo de Documento** → _\[Tu Documento (por ejemplo, Orden de Compra)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Bajo la pestaña **E-Doc**, selecciona tu formato (por ejemplo, **EDI**).
3.  Haz clic en **Vista Previa** para ver o editar el archivo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdo1R389GeSqFuZKLD0OP%252Fimage.png%3Falt%3Dmedia%26token%3D930903d4-44af-4188-b015-c60c2dd9d9ab\&width=768\&dpr=4\&quality=100\&sign=77bbb2ce\&sv=2)

#### **Gestión de Borradores:**

* **Crear un Borrador:** Haz clic en el icono de lápiz ✏️.
* **Eliminar Borradores:** Usa el icono de papelera 🗑️ para eliminar borradores no utilizados.
* **Activar Cambios:** Haz clic en la marca de verificación ✅ para publicar una versión.
  * **Nota**: Activar una nueva versión **desactivará automáticamente** la anterior.

## 4. Editor HTML/XSLT/CSS

El **Archivo de Vista Previa** se edita en un editor dedicado que admite HTML, XSLT y CSS.

* **HTML** define la estructura del documento de salida (por ejemplo, tablas, divisiones, diseño).
* **CSS** controla el estilo (por ejemplo, fuentes, espaciado, colores, alineación).
*   Las declaraciones **XSLT** `**select**` se utilizan para poblar dinámicamente campos desde el XML personalizado, como:

    Copy

    ```
    <xsl:value-of select="/PURCHASE_ORDER/PURCHASE_ORDER_NUMBER/text()" />
    ```
* También puedes usar **lógica XSLT** (`<xsl:if>`, `<xsl:for-each>`, etc.) para manejar la visualización condicional o iterar sobre elementos de línea.

## 5. Función de Vista Previa (Renderizado de Salida)

La Función de Vista Previa te permite probar y verificar cómo se renderiza un documento EDI con el Archivo de Vista Previa actual.

#### **Uso:**

* Sube un archivo EDI a través del proceso de carga estándar.
* Copia el **ID del Documento** del archivo cargado.
* Navega hasta la interfaz de **Vista Previa**.
* Abre la **Función de Vista Previa**.\
  \
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Ingresa el ID del Documento y haz clic en **Probar**.
* La vista previa formateada en estilo PDF se mostrará utilizando la configuración HTML/CSS/XSLT.

Esta función es crucial para depurar las vinculaciones de datos, refinar el diseño y garantizar que el documento sea preciso y visualmente claro para los usuarios y sistemas descendentes como **IDM**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJH103tnbqZjuimpOniVg%252Fimage.png%3Falt%3Dmedia%26token%3D4e63cc09-b0de-488f-bdd0-ee5a9246a371\&width=768\&dpr=4\&quality=100\&sign=bfff5bba\&sv=2)

## 6. Video Tutorial

Una guía en video para este tipo de archivo está disponible en la [página de Videos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Úsala para seguir la configuración, edición y vista previa.
