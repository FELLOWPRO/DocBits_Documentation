# Guía de Archivo de Transformación EDI

## 1. Visión general

El **Archivo de Transformación** define cómo el XML estructurado, creado utilizando el **Archivo de Descriptores de Estructura**, se convierte en un formato XML personalizado que coincide con los requisitos específicos de documentos de su organización.

Esta transformación se realiza utilizando **XSLT (Transformaciones de Lenguaje de Hojas de Estilo Extensible)**, que se puede crear y mantener a través del **Editor XSLT** en la interfaz de DocBits.

## 2. Propósito y Función

* Transforma el **XML intermedio** (salida del Descriptor de Estructura) en un **XML final** alineado con el esquema de su documento.
* Permite flexibilidad para adaptarse a los formatos de socios EDI y los requisitos del sistema interno.
* Se construye utilizando **reglas XSLT**, que le permiten definir asignaciones, formato de valores, lógica condicional y estructura.

## 3. Acceso y Edición Básica

#### Acceder al Archivo

1.  Ir a **Configuración → Tipo de Documento** → \[Su Documento (por ejemplo, _Orden de Compra_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. En la pestaña **E-Doc**, seleccione su formato (por ejemplo, **EDI**).
3.  Haga clic en **Transformación** para ver o editar.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

#### Gestión de Borradores

* **Crear un Borrador**: Haga clic en el icono de lápiz ✏️.
* **Eliminar Borradores**: Utilice el icono de papelera 🗑️ para eliminar borradores no utilizados.
* **Activar Cambios**: Haga clic en la marca de verificación ✅ para publicar una versión.
  * **Nota**: Activar una nueva versión **desactivará automáticamente** la anterior.

## 4. Editor XSLT

El Archivo de Transformación se edita utilizando un **Editor XSLT** integrado que admite resaltado de sintaxis y validación.

* Agregue plantillas para mapear rutas específicas desde el XML de entrada a la estructura deseada.
* Utilice lógica condicional (por ejemplo, `<xsl:if>`, `<xsl:choose>`) para manejar formatos de datos opcionales o variables.
* Aplique funciones de formato según sea necesario (por ejemplo, manipulación de cadenas, formato de fechas).

## 5. Función de Vista Previa (Vista Previa del XML Transformado)

La **Función de Vista Previa** le permite probar y previsualizar cómo se procesa un archivo EDI cargado utilizando el **Archivo de Transformación** actual.

#### Uso

* Cargue un archivo EDI a través del flujo de carga estándar.
* Copie el **ID del Documento** del archivo cargado.
* Navegue hasta la interfaz del **Archivo de Transformación**.
*   Abra la **Función de Vista Previa**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Ingrese el **ID del Documento** en el campo y presione **Probar**.
* Se mostrará la **salida XML transformada** resultante.

Esto es especialmente útil para depurar mapeos XSLT y asegurarse de que la estructura XML final cumpla con sus requisitos de formato.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Video Tutorial

Una guía en video para este tipo de archivo está disponible en la [página de Videos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Úsela para seguir la configuración, edición y previsualización.

## Reglas utilizadas y activación

Las reglas específicas de la organización tienen prioridad sobre las predeterminadas para el formato eDoc detectado. Compruebe la TRANSFORMATION activa y compruebe qué nodo proporciona invoice_type en el XML transformado; la ruta depende del formato. Guardar conserva un borrador; utilice la marca de verificación para activarlo después de las pruebas. Una Preview renderizada no demuestra el tipo de documento almacenado. Consulte la [guía de resolución de problemas de clasificación](../credit-note-recognized-as-invoice.md) para conocer los códigos 381/261, los scripts posteriores y las precauciones para volver a procesar documentos.
