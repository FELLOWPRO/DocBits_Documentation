---
description: Cómo importar datos maestros directamente en DocBits.
---

# Custom Master Data

#### Activar Custom Master Data <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

Desde el Dashboard, navegue a Settings → Document Processing → Module.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_2.png" alt="" width="375"><figcaption></figcaption></figure></div>

En Module, active Custom Master Data pulsando el control deslizante, como se muestra a continuación.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_3.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Descripción general de la función <a href="#feature-overview" id="feature-overview"></a>

Para añadir sus propios datos maestros a DocBits, navegue a Master Data Lookup en Settings.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_4.png" alt="" width="375"><figcaption></figcaption></figure></div>

Haga clic en “Custom Master Data”.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="" width="375"><figcaption></figcaption></figure></div>

A continuación, tendrá la opción de crear una plantilla (Template) o un endpoint (Endpoint).

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Crear una plantilla <a href="#create-a-template" id="create-a-template"></a>

El primer paso es elegir entre utilizar el archivo ION API de su organización o utilizar OAuth2 e introducir los datos necesarios.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="" width="375"><figcaption></figcaption></figure></div>

A continuación, configuraremos los valores predefinidos. Aquí introducirá el nombre de la tabla de datos maestros y la URL de la llamada a la API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Después deberá introducir la ruta JSON mediante notación de puntos; para obtener más información sobre la notación de puntos, haga clic [aquí](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Por último, deberá asignar los datos a las columnas que desea crear, como en el ejemplo siguiente.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Una vez hecho esto, haga clic en Done para que se cree y se rellene su nuevo dato maestro.

#### Crear un endpoint <a href="#create-an-endpoint" id="create-an-endpoint"></a>

El primer paso es elegir entre utilizar el archivo ION API de su organización, utilizar OAuth2 o dejarlo en blanco e introducir los datos necesarios.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="" width="375"><figcaption></figcaption></figure></div>

A continuación, configuraremos los valores predefinidos. Aquí introducirá el nombre de la tabla de datos maestros y la URL de la llamada a la API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Después deberá introducir la ruta JSON mediante notación de puntos; para obtener más información sobre la notación de puntos, haga clic [aquí](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Por último, deberá asignar los datos a las columnas que desea crear, como en el ejemplo siguiente.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Una vez hecho esto, haga clic en Done para que se cree y se rellene su nuevo dato maestro.
