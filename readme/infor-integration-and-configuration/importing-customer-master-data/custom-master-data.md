---
description: "如何在 DocBits 中直接导入主数据。"
---

# 自定义主数据

#### 激活自定义主数据 <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

在仪表板中，依次前往“设置” → “文档处理” → “模块”。

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-modules-document-integration-zh.png" alt="中文文档集成模块：脚本、扫描、条码及自定义主数据等选项；Select 仍为英文。未改动任何开关。"><figcaption><p>中文文档集成模块：脚本、扫描、条码及自定义主数据等选项；Select 仍为英文。未改动任何开关。</p></figcaption></figure></div>

在“模块”中，按下方所示启用“自定义主数据”滑块。

<div align="left"></div>

#### 功能概览 <a href="#feature-overview" id="feature-overview"></a>

要将自己的主数据添加到 DocBits 中，请前往“设置”中的“主数据查找”。

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-master-data-overview-zh.png" alt="中文主数据页面；已隐藏供应商及组织数据，所示配置的英语列标题保留原文。"><figcaption><p>中文主数据页面；已隐藏供应商及组织数据，所示配置的英语列标题保留原文。</p></figcaption></figure></div>

点击“Custom Master Data”。

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="Master Data Lookup 设置页面，包含 Additional charge Costing Element、Purchase order、Purchase order Header 和 Supplier 等查找项" width="375"><figcaption></figcaption></figure></div>

随后，您可以选择创建模板或端点。

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="Custom Master Data 面板，包含 Create Template 和 Create Endpoint 按钮" width="375"><figcaption></figcaption></figure></div>

#### 创建模板 <a href="#create-a-template" id="create-a-template"></a>

首先，选择使用组织的 ION API 文件，或使用 OAuth2 并输入所需数据。

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="Master Data Lookup 向导的 Select Preset 步骤，包含问题 What API do you want to use 以及 ION API 和 OAUTH2 选项" width="375"><figcaption></figcaption></figure></div>

接下来，我们将配置预设。在此处输入主数据表名称和 API 调用 URL。

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="Master Data Lookup 向导的 Configure Preset 步骤，包含 Preset Name、Application Type、GET URL 字段以及 PARAMS、HEADERS、AUTHORIZATION 和 BODY 标签页" width="375"><figcaption></figcaption></figure></div>

随后，您需要使用点表示法输入 JSON 路径。有关点表示法的更多信息，请点击[此处](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/)。

最后，您需要将数据映射到要创建的列中，如下例所示。

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="Master Data Lookup 向导，包含 Select Table Columns、左侧的 JSON 响应以及 Column Name、Spaltenwert Name 和 Test Extraction 映射列" width="375"><figcaption></figcaption></figure></div>

完成后，点击“Done”以创建并填充新的主数据。

#### 创建端点 <a href="#create-an-endpoint" id="create-an-endpoint"></a>

首先，选择使用组织的 ION API 文件、使用 OAuth2，或将此项留空并输入所需数据。

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="Master Data Lookup 端点向导的 Select Preset 步骤，包含 Choose a preset for your endpoint 以及 BLANK、ION API 和 OAUTH2 选项" width="375"><figcaption></figcaption></figure></div>

接下来，我们将配置预设。在此处输入主数据表名称和 API 调用 URL。

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="Master Data Lookup 向导的 Configure Preset 步骤，包含 Preset Name、Application Type、GET URL 字段以及 PARAMS、HEADERS、AUTHORIZATION 和 BODY 标签页" width="375"><figcaption></figcaption></figure></div>

随后，您需要使用点表示法输入 JSON 路径。有关点表示法的更多信息，请点击[此处](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/)。

最后，您需要将数据映射到要创建的列中，如下例所示。

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="Master Data Lookup 向导，包含 Select Table Columns、左侧的 JSON 响应以及 Column Name、Spaltenwert Name 和 Test Extraction 映射列" width="375"><figcaption></figcaption></figure></div>

完成后，点击“Done”以创建并填充新的主数据。
