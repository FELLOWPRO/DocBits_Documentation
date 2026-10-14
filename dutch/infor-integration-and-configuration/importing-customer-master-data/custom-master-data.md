---
description: How to Import Master Data directly within DocBits.
---

# Custom Master Data

#### Activating Custom Master Data <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

From the Dashboard navigate to Settings → Document Processing → Module.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/docbits_cmd_activate_slider.png" alt="Docbits Cmd Activate Slider" width="375"><figcaption></figcaption></figure></div>

In Module, activate Custom Master Data by pressing the slider as shown below.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_3.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Feature Overview <a href="#feature-overview" id="feature-overview"></a>

In order to add your own master data into DocBits, navigate to Master Data Lookup in Settings.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_4.png" alt="" width="375"><figcaption></figcaption></figure></div>

Click on “Custom Master Data”

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="" width="375"><figcaption></figcaption></figure></div>

You then have the option to create a Template or an Endpoint.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Create a Template <a href="#create-a-template" id="create-a-template"></a>

The first step is to choose between using your organizations ION API file or to use OAuth2 and enter the necessary data.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="" width="375"><figcaption></figcaption></figure></div>

Next, we will configure the presets. Here you will enter the Master Data table name the API call URL.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

You will then be required to enter the JSON path using dot notation, for more information on dot notation click [here](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Lastly, you will need to map the data to the columns you would like to create like in the example below.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

After you have done this, click on Done for your new master data to be created and populated .

#### Create an Endpoint <a href="#create-an-endpoint" id="create-an-endpoint"></a>

The first step is to choose between using your organizations ION API file, to use OAuth2 or to leave this blank and enter the necessary data.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="" width="375"><figcaption></figcaption></figure></div>

Next, we will configure the presets. Here you will enter the Master Data table name the API call URL.

<div align="left"><figure><img src="../../.gitbook/assets/docbits_cmd_presets_config.png" alt="Docbits Cmd Presets Config" width="375"><figcaption></figcaption></figure></div>

You will then be required to enter the JSON path using dot notation, for more information on dot notation click [here](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Lastly, you will need to map the data to the columns you would like to create like in the example below.

<div align="left"><figure><img src="../../.gitbook/assets/docbits_cmd_map_columns.png" alt="Docbits Cmd Map Columns" width="375"><figcaption></figcaption></figure></div>

After you have done this, click on Done for your new master data to be created and populated .
