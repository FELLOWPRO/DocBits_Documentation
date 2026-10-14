# Conectar a través de la base de datos de solo lectura

Esta guía le explica cómo conectar la **base de datos de solo lectura de DocBits a Power BI Desktop** mediante el **controlador ODBC de PostgreSQL**. Abarca la instalación del controlador, la configuración de ODBC, la integración con Power BI y la actualización programada.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

#### 1. Instalar el controlador ODBC de PostgreSQL

* Descargue la última versión del controlador ODBC de PostgreSQL (**psqlODBC**) desde el sitio oficial:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Ejecute el instalador y siga el asistente de configuración.

#### 2. Configurar el origen de datos ODBC

* Abra el **Administrador de orígenes de datos ODBC (64 bits)** desde el Panel de control o la búsqueda de Windows.
* Vaya a la pestaña **DSN de sistema** y haga clic en **Agregar**.
* Seleccione el controlador **PostgreSQL Unicode(x64)** en la lista y haga clic en **Finalizar**.
* Rellene los campos obligatorios con las credenciales de:\n  **DocBits → Settings → Document Processing → Module → AI Dashboard → Read-Only DB Access**

<figure><img src="../../.gitbook/assets/connect_read_only_4.png" alt=""><figcaption></figcaption></figure>

**Campos obligatorios:**

* **Name:** Un nombre para la conexión (p. ej., `Sandbox-Read_Only`)
* **Server:** Copie el valor del host de DocBits
* **Port:** Copie el valor del puerto de DocBits
* **Database:** Copie el nombre de la base de datos de DocBits
* **Username:** Copie el nombre de usuario de DocBits
* **Password:** Copie la contraseña de DocBits
* **SSL Mode:** Establézcalo en **Require** (garantiza una comunicación cifrada)

#### 3. Conectar la base de datos de solo lectura a Power BI

* Abra **Power BI Desktop**.
*   Seleccione **Obtener datos** → **ODBC** → **Conectar**.

    <figure><img src="../../.gitbook/assets/powerbi_get_data_odbc.png" alt="Power BI Obtener datos ODBC"><figcaption></figcaption></figure>
* En la lista de DSN, seleccione el origen que ha configurado (p. ej., `Sandbox-Read_Only`).

<figure><img src="../../.gitbook/assets/connect_read_only_3.png" alt=""><figcaption></figcaption></figure>

* Haga clic en **Aceptar**. Introduzca de nuevo las credenciales si se le solicita.
  * <mark style="color:red;">**Nota:**</mark> Si aparece el error **"password authentication failed for user"**, intente introducir su contraseña entre **llaves `{}`**.

#### 4. Cargar y transformar los datos

* En el panel **Navegador**, despliegue la lista de esquemas.
* Abra el esquema **`public`**.
* Seleccione las tablas que desea importar.

![](../../.gitbook/assets/connect_read_only_1.png)        ![](../../.gitbook/assets/connect_read_only_2.png)

* Elija:
  * **Cargar** → Importar directamente en Power BI
  * **Transformar datos** → Abrir Power Query para dar forma a los datos y filtrarlos antes de cargarlos

#### 5. Visualizar sus datos

* Utilice el lienzo de informes de Power BI para crear paneles.
* Arrastre campos, añada segmentaciones de datos, elija tipos de gráfico y aplique cálculos DAX.
* Utilice el **Editor de Power Query** para limpiar o combinar datos antes de crear los elementos visuales.
* Referencia: [Documentación de Power BI](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

#### 6. Habilitar la actualización programada (opcional)

<mark style="color:red;">**Nota:**</mark> **Requiere Power BI Pro o Premium + Gateway**

* Para mantener sus informes sincronizados con ClickHouse:
* Publique su archivo `.pbix` en **Power BI Service**.
* Instale el **Power BI Gateway** (modo Standard) en una máquina con acceso de red a ClickHouse.
* En Power BI Service:
  * Vaya a su conjunto de datos → **Configuración** → **Actualización programada**
  * Asigne su DSN e indique las credenciales
* Más información [aquí](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).&#x20;

#### 7. Ejemplos de paneles y vistas de datos&#x20;

<div><figure><img src="../../.gitbook/assets/powerbi_dashboard_example_1.png" alt="Ejemplo de panel de Power BI 1"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_2.png" alt="Ejemplo de panel de Power BI 2"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_3.png" alt="Ejemplo de panel de Power BI 3"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_4.png" alt="Ejemplo de panel de Power BI 4"><figcaption></figcaption></figure></div>
