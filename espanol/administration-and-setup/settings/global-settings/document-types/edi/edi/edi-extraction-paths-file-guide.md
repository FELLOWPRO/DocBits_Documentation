# Guía de Archivos de Rutas de Extracción EDI

## 1. Visión general

El **Archivo de Rutas de Extracción** define cómo se extraen los datos del **XML estructurado** en campos y tablas específicos dentro de la interfaz. Mapea los **IDs de campo** a **expresiones XPath**, que se evalúan para extraer valores del XML en los campos de documento correspondientes. Este archivo desempeña un papel crítico en garantizar que los datos extraídos aparezcan correctamente durante la validación de campos y el procesamiento posterior.

## 2. Propósito y Función

* Mapea cada campo de documento y columna de tabla a una ubicación específica en el XML estructurado utilizando expresiones XPath.
* Asegura que los valores correctos se populen en campos como `order_number`, `supplier_name` y `total_amount`.
* Admite tanto **campos individuales** (a través de un objeto `fields`) como **tablas** (a través de una matriz `tables` con rutas de fila y mapeos de columnas).
* Permite un control preciso sobre cómo se recuperan los datos del XML, incluido el uso de funciones XPath como `sum()`.

Mapeo de campo de ejemplo:

Copy

```
"order_number": "//PURCHASE_ORDER/PURCHASE_ORDER/text()"
```

## 3. Acceso y Edición Básica

#### **Acceder al Archivo:**

1.  Ve a **Configuración** → **Tipo de Documento** → _\[Tu Documento (por ejemplo, Orden de Compra)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. En la pestaña **E-Doc**, selecciona tu formato (por ejemplo, **EDI**).
3.  Haz clic en **Rutas de Extracción** para ver o editar el archivo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FawwG5QnErp1yy1eYHrlX%252Fimage.png%3Falt%3Dmedia%26token%3D46a6d8b3-52d2-4c13-bc72-1a74955efd9f\&width=768\&dpr=4\&quality=100\&sign=e612882b\&sv=2)

#### **Gestión de Borradores:**

* **Crear un Borrador:** Haz clic en el icono de lápiz ✏️.
* **Eliminar Borradores:** Utiliza el icono de papelera 🗑️ para eliminar borradores no utilizados.
* **Activar Cambios:** Haz clic en la marca de verificación ✅ para publicar una versión.
  * **Nota**: Activar una nueva versión **desactivará automáticamente** la anterior.

## 4. Editor y Sintaxis

El Archivo de Rutas de Extracción está escrito en **JSON** y contiene dos componentes principales:

* **fields**: Un diccionario donde cada clave es un ID de campo y cada valor es una expresión XPath que define cómo extraer los datos.
* **tables**: Una lista de definiciones de tabla que incluyen:
  * `name`: El ID de la tabla.
  * `row_path`: Un XPath que identifica cada fila de la tabla.
  * `columns`: Una lista de mapeos de columnas (`name`, `path`).

También puedes usar funciones XPath (por ejemplo, `sum()`) y expresiones para calcular valores dinámicamente a partir de elementos repetidos.

Copy

```
jsonCopyEdit"total_net_amount": "sum(//PURCHASE_ORDER/ORDER_LINES/ORDER_LINE/SUB_TOTAL)"
```

## 5. Función de Vista Previa (Evaluar Extracción)

La **Función de Vista Previa** te permite simular cómo se comportarán las rutas de extracción con un documento cargado real.

**Uso:**

* Carga un archivo EDI a través del proceso de carga estándar.
* Copia el **ID del Documento**.
* Ve a la interfaz de **Rutas de Extracción**.
* Abre la **Función de Vista Previa**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Ingresa el ID del Documento y haz clic en **Probar**.
* El resultado mostrará cómo se poblaron cada campo y tabla basados en las rutas configuradas.

Esta función es esencial para verificar que tus expresiones XPath estén correctamente definidas y extraigan los valores esperados antes de activar el borrador.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F81uvH6FFVBJsSZucanWY%252Fimage.png%3Falt%3Dmedia%26token%3Dde3ba545-1ee3-44b2-a629-9660d80174f2\&width=768\&dpr=4\&quality=100\&sign=43c8b507\&sv=2)

## 6. Video Tutorial

Una guía en video para este tipo de archivo está disponible en la [página de Videos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Úsala para seguir la configuración, edición y vista previa.
