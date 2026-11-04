# Conectar a través de la base de datos de solo lectura

Esta guía te lleva a través de la conexión de la **base de datos de solo lectura de DocBits a Power BI Desktop** utilizando el **controlador ODBC de PostgreSQL**. Cubre la instalación del controlador, configuración de ODBC, integración con Power BI y actualización programada.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Instalar el controlador ODBC de PostgreSQL

* Descarga el último controlador ODBC de PostgreSQL (**psqlODBC**) desde el sitio oficial:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Ejecuta el instalador y sigue el asistente de configuración.

### 2. Configurar la fuente de datos ODBC

* Abre **Administrador de origen de datos ODBC (64 bits)** a través del Panel de Control o la Búsqueda de Windows.
* Ve a la pestaña **DSN del sistema** y haz clic en **Agregar**.
* Selecciona el controlador **PostgreSQL Unicode(x64)** de la lista y haz clic en **Finalizar**.
* Completa los campos requeridos con las credenciales de: **DocBits → Configuración → Procesamiento de documentos → Módulo → Panel de AI → Acceso a la base de datos de solo lectura**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FupCHowPUuMJ8hO9Y36EY%252Fconnect_read_only_4.png%3Falt%3Dmedia%26token%3D3eb69744-6696-41e2-90be-63295b9b6f6d\&width=768\&dpr=4\&quality=100\&sign=647db68c\&sv=2)

**Campos requeridos:**

* **Nombre:** Un nombre para la conexión (por ejemplo, `Sandbox-Read_Only`)
* **Servidor:** Copia el valor del host de DocBits
* **Puerto:** Copia el valor del puerto de DocBits
* **Base de datos:** Copia el nombre de la base de datos de DocBits
* **Nombre de usuario:** Copia el nombre de usuario de DocBits
* **Contraseña:** Copia la contraseña de DocBits
* **Modo SSL:** Establece en **Requerido** (asegura comunicación encriptada)

### 3. Conectar la base de datos de solo lectura a Power BI

* Abre **Power BI Desktop**.
*   Selecciona **Obtener datos** → **ODBC** → **Conectar**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
* Desde la lista de DSN, selecciona tu fuente configurada (por ejemplo, `Sandbox-Read_Only`).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKPDLjfDw2SRYvzvFKWXq%252Fconnect_read_only_3.png%3Falt%3Dmedia%26token%3Dc67c1362-7f63-479e-a373-974d198f5eb7\&width=768\&dpr=4\&quality=100\&sign=f001e759\&sv=2)

* Haz clic en **Aceptar**. Ingresa las credenciales nuevamente si se solicita.
  * **Nota:** Si ves el error **“autenticación de contraseña fallida para el usuario”**, intenta ingresar tu contraseña entre **llaves** `**{}**`.

### 4. Cargar y transformar datos

* En el panel **Navegador**, expande la lista de esquemas.
* Abre el esquema `**public**`.
* Selecciona las tablas que deseas importar.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSmtEspL1H6ieOJhtDwYb%252Fconnect_read_only_1.png%3Falt%3Dmedia%26token%3Dd402a928-175e-4904-bd21-592ff114fad7\&width=300\&dpr=4\&quality=100\&sign=464e3a3d\&sv=2) ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3Phea1Pf3ZBJtMzw3rxi%252Fconnect_read_only_2.png%3Falt%3Dmedia%26token%3D94037886-57e3-440d-bf08-61cd37c65b98\&width=300\&dpr=4\&quality=100\&sign=5ead9fe9\&sv=2)

* Elige:
  * **Cargar** → Importar directamente a Power BI
  * **Transformar datos** → Abrir Power Query para dar forma y filtrar antes de cargar

### 5. Visualiza tus datos

* Utiliza el lienzo de informe de Power BI para construir paneles.
* Arrastra campos, agrega segmentadores, elige tipos de gráficos y aplica cálculos DAX.
* Utiliza el **Editor de Power Query** para limpiar o unir datos antes de crear visuales.
* Referencia: [Documentación de Power BI](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

### 6. Habilitar actualización programada (Opcional)

**Nota:** **Requiere Power BI Pro o Premium + Gateway**

* Para mantener tus informes sincronizados con ClickHouse:
* Publica tu archivo `.pbix` en **Power BI Service**.
* Instala el **Gateway de Power BI** (modo estándar) en una máquina con acceso a la red de ClickHouse.
* En Power BI Service:
  * Ve a tu conjunto de datos → **Configuración** → **Actualización programada**
  * Mapea tu DSN y proporciona credenciales
* Más información [aquí](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Ejemplos de paneles y vistas de datos

![](<../../.gitbook/assets/example_4 (1).avif>)![](<../../.gitbook/assets/example_3 (1).avif>)![](<../../.gitbook/assets/example_2 (1).avif>)![](<../../.gitbook/assets/example_1 (1).avif>)
