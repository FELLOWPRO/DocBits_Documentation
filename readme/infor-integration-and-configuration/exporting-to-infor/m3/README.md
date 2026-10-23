# M3

## 第 1 步：创建连接点

1. 导航至 **OS > ION > Connect > Connection Points**
2. 点击 **Add**，然后选择 **IMS via API Gateway** 作为连接类型。
3. 配置以下设置：
   * **Name**：设置为 `DocBits_Export`。
   * **Description**：设置为 `DocBits_Export`。
   * **取消勾选**：_Application has IMS End Point_。
   * **ION API Client ID**：
     * 打开 ION API 文件。
     * 在文件中搜索 `"ci"`。
     * 复制引号内的值（不包括引号）。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_1.png" alt="通过API Gateway连接IMS的Infor Application Connection Point页面，名称为DocBits_Export，包含描述和ION API Client ID字段"><figcaption></figcaption></figure>

4. 在 **Documents** 下添加 `Sync.CaptureDocument`。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_2.png" alt="Connection Point页面DocBits_Export，其Documents部分列出Sync.CaptureDocument并设置为Send from Application"><figcaption></figcaption></figure>

5. 点击 **Save**，完成配置。

## 第 2 步：上传映射

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. 下载 M3 映射文件。
2. 导航至 **Infor** > **OS** > **ION** > **Connect** > **Mappings**。
3. 点击 **Import**，并选择适用于 **M3** 的映射文件。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_3.png" alt="Infor ION Connect的Mappings页面工具栏中的添加按钮"><figcaption></figcaption></figure>

4. 文件导入后，批准这些映射以激活它们。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_4.png" alt="ION Connect 中的映射概览，显示从 Sync.CaptureDocument 到 ProcessSupplierInvoice 的已批准映射"><figcaption></figcaption></figure>

## 第 3 步：创建数据流

1. 导航至 **OS** -> **ION** -> **Connect** -> **Data Flows**。
2. 点击 **Add**，然后选择 **Document Flow**。
3. 填写详细信息：
   * **Name**：`DocBits_Export_to_M3`
4. 向数据流添加节点：

#### 应用程序节点

1. 向数据流添加一个 **Application Node**。
   * **Name**：`DocBits` 或 `DocBits-Export`。
2. 点击 **Add**，然后选择第 1 步中创建的 **Connection Point**。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_5.png" alt="Data Flow 编辑器，节点选择面板已打开，Application Activity Properties 面板显示节点名称 DocBits-Dev-Demo-Export"><figcaption></figcaption></figure>

3. 点击应用程序节点旁的 **Document Icon**。
   * 点击 **Add**，然后选择 `Sync.CaptureDocument`。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_6.png" alt="Data Flow 编辑器，显示应用程序节点的 Documents 列表，其中已添加 Sync.CaptureDocument"><figcaption></figcaption></figure>

#### 映射节点

1. 在应用程序节点右侧添加一个 **Mapping Node**。
   * **Name**：`Capt2process`。
   * **Mapping**：`CaptureDocument_to_ProcessSupplierInvoice`。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_7.png" alt="Data Flow 编辑器，Mapping Properties 面板显示该节点的名称和所选映射"><figcaption></figcaption></figure>

#### 应用程序节点

1. 在上一个映射节点右侧添加一个 **Application Node**。
   * **Name**：`M3`。
2. 点击 **Add**，然后选择客户的 **M3 Application**。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_8.png" alt="Data Flow 编辑器，Application Activity Properties 面板显示名为 M3 BODs 的 M3 应用程序节点"><figcaption></figcaption></figure>

3. 点击应用程序节点旁的 **Document Icon**。
   * 点击 **Add**，然后选择 `Acknowledge.SupplierInvoice`。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_9.png" alt="Data Flow 编辑器，显示 M3 应用程序节点的 Documents 列表，其中已添加 Acknowledge.SupplierInvoice"><figcaption></figcaption></figure>

#### API 节点

1. 在应用程序节点右侧添加一个 **API Node**。
   * **Name**：`DocBits-Error`。
   * **ION API Connector**：`DocBits_Import`。
   * 如果 `DocBits_Import` 不存在，请参阅从 M3 导入文档中的 **第 1 步**和**第 2 步**来创建连接点。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_10.png" alt="Data Flow 编辑器，ION API Activity Properties 面板显示 API 节点的连接器 DocBits-Dev-Demo-Import"><figcaption></figcaption></figure>

#### 保存并激活数据流

* 添加并配置所有节点后，点击 **Save**。
* 激活数据流以完成设置。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_11.png" alt="Data Flow 编辑器，连接点面板已打开，显示流名称 DocBits_Demo_to_M3"><figcaption></figcaption></figure>

## 第 4 步：在 DocBits 中配置导出

### 本地部署：

1. 打开 **DocBits**。
2. 导航至 **Settings > Document Processing > Export**。

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="DocBits的设置页面，Document Processing导航已展开，列出Import、OCR Settings、Classification and Extraction和Module"><figcaption></figcaption></figure>
3. 创建新的导出：
   * **选择**：**Infor IDM + ION BOD**。
   * **Title**：选择一个有意义的标题。
   * **Document Type**：设置为 **Invoice**。
   * **Sub-Organization**：可以留空，也可以根据需要设置为特定子组织。
4. 上传所需文件：
   * **ION Mapping File**：可在 **Infor OS → API Gateway → Authorized Apps** 中找到。找到 **DocBits** 应用，打开并下载凭据。
   * **IDM Mapping File**：（提供相关文件路径或位置）。
   * **BOD Mapping File**：（提供相关文件路径或位置）。

### 云端：

1. 打开 **DocBits**。
2. 导航至 **Settings > Document Processing > Export**。

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="DocBits的设置页面，Document Processing导航已展开，列出Import、OCR Settings、Classification and Extraction和Module"><figcaption></figcaption></figure>
3. 创建新的导出：
   * **选择**：**Infor IDM + M3 (API)**。
   * **Title**：选择一个有意义的标题。
   * **Document Type**：设置为 **Invoice**。
   * **Sub-Organization**：可以留空，也可以根据需要设置为特定子组织。
4. 上传所需文件：
   * **ION Mapping File**：可在 **Infor OS → API Gateway → Authorized Apps** 中找到。找到 **DocBits** 应用，打开并下载凭据。
   * **IDM Mapping File**：（提供相关文件路径或位置）。
   * **M3 Mapping File**：（提供相关文件路径或位置）。

### 使用 toml 的云端：

1. 打开 **DocBits**。
2. 导航至 **Settings > Document Processing > Export**。

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="DocBits的设置页面，Document Processing导航已展开，列出Import、OCR Settings、Classification and Extraction和Module"><figcaption></figcaption></figure>
3. 创建新的导出：
   * **选择**：**Infor IDM + M3 (API)**。
   * **Title**：选择一个有意义的标题。
   * **Document Type**：设置为 **Invoice**。
   * **Sub-Organization**：可以留空，也可以根据需要设置为特定子组织。
4. 上传所需文件：
   * **ION Mapping File**：可在 **Infor OS → API Gateway → Authorized Apps** 中找到。找到 **DocBits** 应用，打开并下载凭据。
   * **IDM Mapping File**：（提供相关文件路径或位置）。
   * **M3 toml Mapping File**：（提供相关文件路径或位置）。
