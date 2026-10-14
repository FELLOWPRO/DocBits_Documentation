# Conectar a través de ClickHouse

Esta guía te lleva a través de la conexión de **ClickHouse** a **Power BI Desktop** usando el **controlador ODBC**. Cubre la instalación del controlador, la configuración ODBC, la integración con Power BI y la configuración de actualización de datos.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Instalar el Controlador ODBC de ClickHouse

* Descarga el último **Controlador ODBC de ClickHouse** desde:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Ejecuta el instalador y sigue el asistente de configuración.

### 2. Configurar la Fuente de Datos ODBC

* Abre **Administrador de Fuentes de Datos ODBC (64 bits)** a través del Panel de Control o la Búsqueda de Windows.
* Ve a la pestaña **DSN del Sistema** y haz clic en **Agregar**.
* Selecciona **Controlador ODBC de ClickHouse** de la lista y haz clic en **Finalizar**.
*   Completa los campos requeridos. Puedes encontrar la información necesaria en:

    **DocBits** → **Configuración** → **Procesamiento de Documentos** → **Módulo** → **Tablero de AI** → **Acceso Directo a ClickHouse**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNkgb8IJ4dQVRnJ4gpqH0%252Fimage.png%3Falt%3Dmedia%26token%3D27d97e71-dd81-488a-851f-e7d659ad4992\&width=768\&dpr=4\&quality=100\&sign=88a4a589\&sv=2)

    **Campos Requeridos:**

    * **Nombre**: Un nombre para la conexión (por ejemplo, `ClickHouse_Prod`)
    * **Descripción**: Una descripción breve para tu referencia (opcional)
    * **Host**: Copia el valor del host de DocBits
    * **Puerto**: Copia el valor del puerto de DocBits
    * **Base de Datos**: Copia el nombre de la base de datos de DocBits
    * **Nombre de Usuario**: Copia el nombre de usuario de DocBits
    * **Contraseña**: Copia la contraseña de DocBits

### 3. Conectar ClickHouse a Power BI

* Abre **Power BI Desktop**.
*   Selecciona **Obtener Datos** → **ODBC** → **Conectar**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252/Screenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
*   Desde la lista de DSN, selecciona tu fuente configurada (por ejemplo, `ClickHouse_Prod`).

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgDWq5vmtqfAGAQEY0SAX%252/Screenshot%25202025-05-19%2520163823.png%3Falt%3Dmedia%26token%3D443435ac-82ba-40de-a4d1-17611afebb6a\&width=768\&dpr=4\&quality=100\&sign=c0c7d7ae\&sv=2)
* Haz clic en **Aceptar**. Ingresa las credenciales nuevamente si se te solicita.

### 4. Cargar y Transformar Datos

* En el panel **Navegador**, navega y selecciona las tablas o vistas a importar.
* Elige:
  * **Cargar**: para importar directamente
  *   **Transformar Datos**: para abrir Power Query y dar forma a los datos

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2lrWi9PduJgVQGHQMmhX%252/Screenshot%25202025-05-19%2520164134.png%3Falt%3Dmedia%26token%3D135c45ad-a7ca-4f01-a2f0-07998397f4d9\&width=768\&dpr=4\&quality=100\&sign=e27f4d93\&sv=2)

### 5. Visualiza tus Datos

* Utiliza el lienzo del informe para construir visualizaciones.
* Arrastra campos, agrega segmentadores, elige tipos de gráficos y usa expresiones **DAX** según sea necesario.
* Aprovecha el **Editor de Power Query** para limpiar o pivotar tus datos de ClickHouse antes de construir visuales.
* Documentación de PowerBI: [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

### 6. Habilitar Actualización Programada (Opcional)

**Nota:** **Requiere Power BI Pro o Premium + Gateway**

* Para mantener tus informes sincronizados con ClickHouse:
* Publica tu archivo `.pbix` en **Power BI Service**.
* Instala el **Gateway de Power BI** (modo estándar) en una máquina con acceso a la red de ClickHouse.
* En Power BI Service:
  * Ve a tu conjunto de datos → **Configuración** → **Actualización Programada**
  * Mapea tu DSN y proporciona credenciales
* Más información [aquí](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Ejemplo de Tableros y Vistas de Datos

![](<../../.gitbook/assets/example_4 (1).avif>) ![](<../../.gitbook/assets/example_3 (1).avif>) ![](<../../.gitbook/assets/example_2 (1).avif>) ![](<../../.gitbook/assets/example_1 (1).avif>)
