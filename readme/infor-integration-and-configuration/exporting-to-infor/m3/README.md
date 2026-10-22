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

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_1.png" alt="Infor 应用程序连接点对话框 IMS via API Gateway，包含用法、连接和文档选项卡，名称为 DocBits_Export，未勾选选项应用程序具有 IMS 端点，包含 ION API 客户端 ID 字段，逻辑 ID 为 inforims.docbits_export"><figcaption></figcaption></figure>

4. 在 **Documents** 下添加 `Sync.CaptureDocument`。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_2.png" alt="应用程序连接点的连接选项卡，名称为 DocBits_Export，文档 sync.captureDocument 显示为从应用程序发送，逻辑 ID 为 inforims.docbits_export"><figcaption></figcaption></figure>

5. 点击 **Save**，完成配置。

## 第 2 步：上传映射

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. 下载 M3 映射文件。
2. 导航至 **Infor** > **OS** > **ION** > **Connect** > **Mappings**。
3. 点击 **Import**，并选择适用于 **M3** 的映射文件。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_3.png" alt="ION Desk 的映射页面，包含搜索字段、筛选控件和添加按钮"><figcaption></figcaption></figure>

4. 文件导入后，批准这些映射以激活它们。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_4.png" alt="已导入的映射，源为 Sync.CaptureDocument，目标为 Process.SupplierInvoice"><figcaption></figcaption></figure>

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

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_5.png" alt="ION Desk 中的数据流，顶部为节点面板，右侧为应用程序活动属性面板，名称为 DocBits-Dev-Demo-Export"><figcaption></figcaption></figure>

3. 点击应用程序节点旁的 **Document Icon**。
   * 点击 **Add**，然后选择 `Sync.CaptureDocument`。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_6.png" alt="ION Desk 中的数据流，已选中应用程序节点，文档面板已打开并显示 Sync.CaptureDocument 条目"><figcaption></figcaption></figure>

#### 映射节点

1. 在应用程序节点右侧添加一个 **Mapping Node**。
   * **Name**：`Capt2process`。
   * **Mapping**：`CaptureDocument_to_ProcessSupplierInvoice`。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_7.png" alt="ION Desk 中的数据流，已选中映射节点，右侧的映射属性面板显示名称和映射 SyncCaptDoc_SyncSuppInv"><figcaption></figcaption></figure>

#### 应用程序节点

1. 在上一个映射节点右侧添加一个 **Application Node**。
   * **Name**：`M3`。
2. 点击 **Add**，然后选择客户的 **M3 Application**。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_8.png" alt="ION Desk 中的数据流，已选中 M3 应用程序节点，右侧的应用程序活动属性面板显示 M3 BODs 条目"><figcaption></figcaption></figure>

3. 点击应用程序节点旁的 **Document Icon**。
   * 点击 **Add**，然后选择 `Acknowledge.SupplierInvoice`。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_9.png" alt="ION Desk 中的数据流，已选中 M3 应用程序节点，文档面板已打开并显示 Acknowledge.SupplierInvoice 条目"><figcaption></figcaption></figure>

#### API 节点

1. 在应用程序节点右侧添加一个 **API Node**。
   * **Name**：`DocBits-Error`。
   * **ION API Connector**：`DocBits_Import`。
   * 如果 `DocBits_Import` 不存在，请参阅从 M3 导入文档中的 **第 1 步**和**第 2 步**来创建连接点。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_10.png" alt="ION Desk 中的数据流，已选中 API 节点，右侧的 ION API 活动属性面板显示 ION API 连接器 DocBits Dev Demo-Import"><figcaption></figcaption></figure>

#### 保存并激活数据流

* 添加并配置所有节点后，点击 **Save**。
* 激活数据流以完成设置。

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_11.png" alt="ION Desk 中的数据流，节点 DocBits_Demo_to_M3、映射节点、M3 节点和错误节点依次相连，画布上方有移除连接点按钮"><figcaption></figcaption></figure>

## 第 4 步：在 DocBits 中配置导出

### 本地部署：

1. 打开 **DocBits**。
2. 导航至 **Settings > Document Processing > Export**。

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="DocBits 的设置页面，文档处理导航分组已展开，包含文档、到期、导入、规则管理、OCR 设置、分类和提取、主数据查找、值列表和模块条目"><figcaption></figcaption></figure>
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

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="DocBits 的设置页面，文档处理导航分组已展开，包含文档、到期、导入、规则管理、OCR 设置、分类和提取、主数据查找、值列表和模块条目"><figcaption></figcaption></figure>
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

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="DocBits 的设置页面，文档处理导航分组已展开，包含文档、到期、导入、规则管理、OCR 设置、分类和提取、主数据查找、值列表和模块条目"><figcaption></figcaption></figure>
3. 创建新的导出：
   * **选择**：**Infor IDM + M3 (API)**。
   * **Title**：选择一个有意义的标题。
   * **Document Type**：设置为 **Invoice**。
   * **Sub-Organization**：可以留空，也可以根据需要设置为特定子组织。
4. 上传所需文件：
   * **ION Mapping File**：可在 **Infor OS → API Gateway → Authorized Apps** 中找到。找到 **DocBits** 应用，打开并下载凭据。
   * **IDM Mapping File**：（提供相关文件路径或位置）。
   * **M3 toml Mapping File**：（提供相关文件路径或位置）。
