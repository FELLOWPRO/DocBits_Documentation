---
description: Cómo importar datos maestros directamente en DocBits.
---

# Datos maestros personalizados

#### Activar Custom Master Data <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

Desde el Panel de control, navegue a Configuración → Procesamiento de documentos → Módulo.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_2.png" alt="Navegación de ajustes de DocBits con entradas como Classification and Extraction, Master Data Lookup y Custom Values" width="375"><figcaption></figcaption></figure></div>

En Module, active Custom Master Data pulsando el control deslizante, como se muestra a continuación.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_3.png" alt="Página de ajustes del módulo que muestra interruptores de funciones como Run Workflows in Celery, Annotation Mode, Models and Labels, Document script y QRCode extraction" width="375"><figcaption></figcaption></figure></div>

#### Descripción general de la función <a href="#feature-overview" id="feature-overview"></a>

Para añadir sus propios datos maestros a DocBits, navegue a Master Data Lookup en Settings.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_4.png" alt="Navegación de ajustes de DocBits en la organización TEST6 con las entradas Document, Import, Rule Management, Global Settings y Classification and Extraction" width="375"><figcaption></figcaption></figure></div>

Haga clic en “Custom Master Data”.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="Página de configuración de Master Data Lookup con los lookups Additional charge Costing Element, Purchase order, Purchase order Header y Supplier" width="375"><figcaption></figcaption></figure></div>

A continuación, tendrá la opción de crear una plantilla (Template) o un endpoint (Endpoint).

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="Panel Custom Master Data con los botones Create Template y Create Endpoint" width="375"><figcaption></figcaption></figure></div>

#### Crear una plantilla <a href="#create-a-template" id="create-a-template"></a>

El primer paso es elegir entre utilizar el archivo ION API de su organización o utilizar OAuth2 e introducir los datos necesarios.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="Paso Select Preset del asistente de Master Data Lookup con la pregunta What API do you want to use y las opciones ION API y OAUTH2" width="375"><figcaption></figcaption></figure></div>

A continuación, configuraremos los valores predefinidos. Aquí introducirá el nombre de la tabla de datos maestros y la URL de la llamada a la API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="Paso Configure Preset del asistente de Master Data Lookup con Preset Name, Application Type, campo GET URL y las pestañas PARAMS, HEADERS, AUTHORIZATION y BODY" width="375"><figcaption></figcaption></figure></div>

Después deberá introducir la ruta JSON mediante notación de puntos; para obtener más información sobre la notación de puntos, haga clic [aquí](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Por último, deberá asignar los datos a las columnas que desea crear, como en el ejemplo siguiente.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="Asistente de Master Data Lookup con Select Table Columns, una respuesta JSON a la izquierda y las columnas de mapeo Column Name, Spaltenwert Name y Test Extraction" width="375"><figcaption></figcaption></figure></div>

Una vez hecho esto, haga clic en Done para que se cree y se rellene su nuevo dato maestro.

#### Crear un endpoint <a href="#create-an-endpoint" id="create-an-endpoint"></a>

El primer paso es elegir entre utilizar el archivo ION API de su organización, utilizar OAuth2 o dejarlo en blanco e introducir los datos necesarios.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="Paso Select Preset del asistente de endpoints de Master Data Lookup con Choose a preset for your endpoint y las opciones BLANK, ION API y OAUTH2" width="375"><figcaption></figcaption></figure></div>

A continuación, configuraremos los valores predefinidos. Aquí introducirá el nombre de la tabla de datos maestros y la URL de la llamada a la API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="Paso Configure Preset del asistente de Master Data Lookup con Preset Name, Application Type, campo GET URL y las pestañas PARAMS, HEADERS, AUTHORIZATION y BODY" width="375"><figcaption></figcaption></figure></div>

Después deberá introducir la ruta JSON mediante notación de puntos; para obtener más información sobre la notación de puntos, haga clic [aquí](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Por último, deberá asignar los datos a las columnas que desea crear, como en el ejemplo siguiente.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="Asistente de Master Data Lookup con Select Table Columns, una respuesta JSON a la izquierda y las columnas de mapeo Column Name, Spaltenwert Name y Test Extraction" width="375"><figcaption></figcaption></figure></div>

Una vez hecho esto, haga clic en Done para que se cree y se rellene su nuevo dato maestro.
