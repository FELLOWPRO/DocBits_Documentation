# Actualizar Estado de Orden de Compra de Documentos



## Resumen

Cuando está habilitado, la columna **Estado de OC** en el panel se actualiza automáticamente cada vez que cambia el estado de la orden de compra.

## Dónde Activar

1. Ir a: **Configuración** → **Configuración Global** → **Tipo de Documento**
2.  Seleccionar el tipo de documento deseado y hacer clic en **Más Configuraciones**.\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fsd3ebb3IETh7wNSA5flh%252Fimage.png%3Falt%3Dmedia%26token%3D6f1d286b-e006-4b23-9866-9ed37bf2bdaa\&width=768\&dpr=4\&quality=100\&sign=b0f0b121\&sv=2)
3.  En la sección **Orden de Compra**, navegar hasta la opción **Actualizar Estado de Orden de Compra de Documentos**.\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSsFkQ46Jd4tn0WGqNSjk%252Fimage.png%3Falt%3Dmedia%26token%3D51ee4f2d-76ae-42b4-a748-f0e9d340b329\&width=768\&dpr=4\&quality=100\&sign=e0f4b1af\&sv=2)

## Cómo Funciona

Cuando esta configuración está habilitada, la columna **Estado de OC** en el panel reflejará automáticamente el estado actual de la orden de compra. Por ejemplo, si el estado de la OC se actualiza a _Recibido_ o _Facturado_, la columna del panel se actualizará en consecuencia para mostrar este nuevo estado.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmWZIOi5pqWyeagCfiXgy%252FStatus%2520on%2520Dashboard.jpg%3Falt%3Dmedia%26token%3D3aad59e7-d249-4f07-afa3-c68429128cec&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6cde440e&#x26;sv=2" alt="" width="375"></div>

## Configuración

1. **Habilitar la Configuración** Navegar a la ubicación mencionada anteriormente y activar la configuración.
2. **Agregar la Columna de Estado de OC (si no es visible)** Si la columna **Estado de OC** no es visible en el panel:
   *   Ir a: **Configuración Avanzada** → **Establecer Columnas de Tabla para Organizaciones**\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6GyECCtvUeKLYd6FkEH%252Fimage.png%3Falt%3Dmedia%26token%3Da023deba-748f-4140-bb33-17483c91f2cf\&width=768\&dpr=4\&quality=100\&sign=164eb544\&sv=2)
   * Agregar el campo del tipo de documento buscando **Estado de OC**
3. **Configurar la configuración de búsqueda**
   *   Configurar el campo de Estado en la búsqueda de encabezado de orden de compra de esta manera:\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Folrh285NuJO787Udc80C%252Fimage.png%3Falt%3Dmedia%26token%3Def5abe46-fe94-4946-a893-66f7ca21322b\&width=768\&dpr=4\&quality=100\&sign=415e657e\&sv=2)
   * **Nota:** **La orden de compra debe estar en Activación Automática de lo contrario las actualizaciones de estado pueden no realizarse correctamente**
   * ¿No sabes cómo **Configurar la configuración de búsqueda? Aquí tienes la** [**guía de configuración de búsqueda**](../../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
4. **Verificar** Recibir o facturar una OC, luego verificar en el panel para confirmar que el estado se ha actualizado correctamente.
