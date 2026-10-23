# Guía del Archivo de Descriptores de Estructura EDI

## **1. Visión general**

El **Archivo de Descriptores de Estructura** define cómo se agrupan los segmentos EDI repetidos (por ejemplo, `N1`–`N4`) en JSON estructurado. Asegura:

* **Análisis preciso** de elementos relacionados como unidades individuales.
* **Salida consistente** para sistemas posteriores.

_Para un ejemplo completo con detalles de segmentos, consulte_ [_Ejemplo de Descriptor de Estructura_](edi-structure-descriptor.md)_._

## **2. Acceso y Edición Básica**

#### **Acceso al Archivo**

1.  **Configuración** → **Tipo de Documento** → \[Su Documento (por ejemplo, _Orden de Compra_)] → **E-Doc.**

    ![Editor del tipo de documento Purchase Order con las pestañas Edit layout, Document Sub Types, Table columns, Fields, Model Training, Regex, Scripts y E-Doc](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Bajo **E-Doc**, seleccione su formato (por ejemplo, _EDI_ ).
3.  Haga clic en **Descriptor de Estructura**.

    ![Sección EDI E-Doc que enumera los archivos Structure Descriptor, Transformation, Preview y Extraction Paths con marcas de tiempo](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOuNVhIuYBPJTu4PdMecy%252Fimage.png%3Falt%3Dmedia%26token%3Dd111b34e-0dd9-4436-9df4-f59490ac0d87\&width=768\&dpr=4\&quality=100\&sign=6e8e9f0e\&sv=2)

#### **Gestión de Borradores**

* **Crear un Borrador**: Haga clic en el icono de lápiz ✏️ para comenzar a editar.
* **Eliminar Borradores**: Utilice el icono de papelera 🗑️ para eliminar borradores no utilizados.
* **Activar Cambios**: Haga clic en el icono de marca de verificación ✅ para aprobar y publicar sus cambios.
  * **Nota**: Activar una nueva versión **desactivará automáticamente** la anterior.

## 3. Función de Vista Previa (Vista Previa de XML Analizado)

La **Función de Vista Previa** le permite probar y previsualizar cómo se analiza un archivo EDI cargado utilizando el Archivo de Descriptores de Estructura actual.

#### Uso

* Cargue un archivo EDI a través del flujo de carga estándar.
* Copie el **ID del Documento** del archivo cargado.
* Navegue hasta la interfaz del **Archivo de Descriptores de Estructura**.
*   Abra la **Función de Vista Previa**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="Panel de vista previa de Extraction paths con un selector de documentos que muestra 29 documentos y un botón Preview" width="375"></div>
* Ingrese el **ID del Documento** en el campo y presione **Probar**.
* La **salida XML estructurada resultante** se mostrará.

Esto es especialmente útil para depurar mapeos y validar agrupaciones estructurales en tiempo real.

![Vista de prueba JSON de Structure Descriptor con campo de ID de documento, lista de campos JSON y salida XML estructurada con elementos VALUE](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FBXU6zeFapt7ZIVFl37Iz%252Fimage.png%3Falt%3Dmedia%26token%3D9d51e329-b781-4781-a527-3258f6f933c6\&width=768\&dpr=4\&quality=100\&sign=4ca17281\&sv=2)

## 6. Video Tutorial

Una guía en video para este tipo de archivo está disponible en la [página de Videos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Úsela para seguir la configuración, edición y previsualización.


<figure><img src="../../../../../../../.gitbook/assets/site-all-edi-list-es.png" alt="Formato EDI existente con sus cuatro atributos configurados."><figcaption><p>Formato EDI existente con sus cuatro atributos configurados.</p></figcaption></figure>

<figure><img src="../../../../../../../.gitbook/assets/site-all-edi-detail-es.png" alt="Atributo STRUCTUREDESCRIPTOR activo: descriptor de estructura JSON en el editor de solo lectura."><figcaption><p>Atributo STRUCTUREDESCRIPTOR activo: descriptor de estructura JSON en el editor de solo lectura.</p></figcaption></figure>


Las vistas muestran una configuración y una versión existentes. Los ajustes varían según el tipo de documento y el formato. Valide los cambios en un borrador antes de activarlos.

Algunas etiquetas, como Custom, Default, Version y Last Modified At, siguen apareciendo en inglés en la interfaz actual del producto. Los identificadores técnicos de atributos y el código de configuración se conservan sin cambios.
