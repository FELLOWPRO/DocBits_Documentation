# Instalación de WatchDog

<figure><img src="../../.gitbook/assets/watchdog-infographic-es.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

### Configurando WatchDog en DocBits

1. **Acceder a la Configuración de WatchDog**
   * Navegar a **Configuración → Procesamiento de Documentos → WatchDog**.
2. **Configuración de Carpetas**
   * Definir las rutas donde WatchDog encuentra y procesa documentos.
   *   Las rutas de las carpetas deben coincidir con las creadas durante la instalación:

       * `C:/WatchDog/Read`
       * `C:/WatchDog/Processed`

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG1EFmtSO4AxZjWir401%252Fimage.png%3Falt%3Dmedia%26token%3Dc356e023-8cfb-4f45-b863-b27c5af1d9df\&width=768\&dpr=4\&quality=100\&sign=1b1ae0c4\&sv=2)
   * <mark style="color:red;">**Nota:**</mark>**&#x20;Se recomienda utilizar rutas locales. Estas deben coincidir con las carpetas en la Instalación de DocBits**
3. **Configuración General**
   *   Seleccionar los tipos de documentos a procesar marcando las casillas correspondientes.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZbCt5UHd37PdNZsVItdt%252Fimage.png%3Falt%3Dmedia%26token%3Db3c3f203-0f60-42a0-bd56-ee70c204f5e8\&width=768\&dpr=4\&quality=100\&sign=becd5e31\&sv=2)
   * **Divisor de Código de Barras:** Cuando está activado, habilita la división de códigos de barras.
   * **Operador DocBits:** Cuando está habilitado, abre un navegador Chrome en segundo plano para el Operador DocBits.
   * **Destino de Exportación:** Establece el destino de exportación.
     * **Infor:** Los documentos se exportan a Infor.
     * **Carpeta de Exportación:** Los documentos se exportan a una carpeta definida que se puede configurar a continuación.
4. **Configuraciones de Exportación**
   * Muestra todas las exportaciones configuradas para **procesamiento local**.
   *   Muestra la marca de tiempo de la **última conexión exitosa** para cada configuración.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FRvK5qn6EggWJxcSYNP5J%252Fimage.png%3Falt%3Dmedia%26token%3D195b9cc6-c5ac-4ee6-90da-b3ee9696ee30\&width=768\&dpr=4\&quality=100\&sign=3bc11ec5\&sv=2)
5. **Configuración de bod\_mapping (Opcional)**
   * <mark style="color:red;">**Campos requeridos:**</mark> Antes de agregar asignaciones de metadatos personalizados, debe definir los siguientes dos valores
     * **`file_name`**
     * **`pdf_path`**
   *   Haga clic en **Agregar Fila** para definir mapeos de metadatos.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlzUqcr51kq18OrmYAR8X%252Fimage.png%3Falt%3Dmedia%26token%3D3035122b-f1d3-44cc-bfe6-5230943bd77d\&width=768\&dpr=4\&quality=100\&sign=e98d5a1b\&sv=2)
   * **Valor:** Especifica el nombre del campo para los metadatos.
   * **Ruta:** La expresión XPath que apunta a los datos XML que deben asignarse al campo.
   * **Icono de Papelera:** Se utiliza para eliminar una fila específica.
6. **Descargar la Configuración**
   * Guardar la configuración
   *   Descargar la configuración\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZXiz4KB7QpnaqD9XwX3o%252Fimage.png%3Falt%3Dmedia%26token%3D04c9f8dc-7d79-443f-9ce4-6d4214edc98b\&width=768\&dpr=4\&quality=100\&sign=574a4218\&sv=2)

### Guía de Instalación de WatchDog

1. **Crear Carpetas Requeridas**
   * Crear un directorio principal: `C:/WatchDog`
   * Dentro de `C:/WatchDog`, crear las siguientes subcarpetas: **Nota:** estas deben coincidir con las carpetas en DocBits.
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Nota:**</mark>**&#x20;Se recomienda utilizar rutas locales. Estas deben coincidir con las carpetas en la Configuración de DocBits**
2. **Descargar WatchDog**
   * Descargar la última versión de `WatchDog.exe` desde: [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Colocar el archivo `WatchDog.exe` descargado en `C:/WatchDog`.
   * Colocar el archivo `watchdog-config.json` descargado en `C:/WatchDog`.
   * Abrir el `watchdog-config.json` y cambiar el **config\_path.**
   * En este ejemplo:
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **Instalar WatchDog**
   * Abrir **Símbolo del sistema (CMD)** con **derechos de administrador**.
   * Navegar a la carpeta de WatchDog.
   *   Ejecutar el siguiente comando para instalar WatchDog:

       `WatchDog.exe install`
4. **Iniciar el Servicio WatchDog**
   *   Ejecutar el siguiente comando en CMD:

       `WatchDog.exe start`
5. **Establecer Tipo de Inicio**
   * Abrir **Servicios** (Presione `Win + R`, escriba `services.msc` y presione **Enter**).
   * Localizar **WatchDog** en la lista de servicios.
   * Hacer doble clic para abrir sus propiedades.
   * Establecer **Tipo de Inicio** en **Automático (Inicio Retrasado)**.
   * Hacer clic en **Aceptar**.
