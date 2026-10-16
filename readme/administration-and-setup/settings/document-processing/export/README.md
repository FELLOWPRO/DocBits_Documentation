# 导出

## 概述

“导出”页面会显示所有已配置的导出设置，以及这些设置处于启用还是停用状态。在此页面中，用户可以：

* 查看和管理现有导出配置
* 创建新的导出连接（例如 **Infor**、**Infor & IDM**、**Webhook** 或 **SFTP**）
* 编辑或删除现有导出配置

## 查找位置

路径：**Settings** → **Document Processing** → **Export**

<figure><img src="../../../../.gitbook/assets/export_list_view.png" alt="导出设置菜单入口"><figcaption></figcaption></figure>

## **使用导出页面**

打开“导出”页面后，会看到所有现有导出配置的列表。

列表中的每一行显示：

* **状态指示器**
  * **绿色**表示导出已启用
  * **红色**表示导出已停用
* **名称** – 导出配置的名称
* **文档类型** – 此导出配置适用的文档类型
* **子组织** – 如果导出仅适用于特定子组织，此处会显示该子组织
* **导出方式** – 文档的发送位置（例如 Infor、IDM、SFTP）
* **操作** – 用于**编辑、删除**或**启用/停用**配置的按钮

<figure><img src="../../../../.gitbook/assets/export_list_view.png" alt="导出列表视图"><figcaption></figcaption></figure>

#### **导出配置的重要规则**

对于给定组织或子组织中的每种**文档类型**，适用以下规则：

* 只能有**一个已启用的 Infor 导出**
* 只能有**一个已启用的非 Infor 导出**（例如 Webhook、SFTP）

不过，同一文档类型可以同时拥有：

* **一个已启用的 Infor 导出**_以及_**一个已启用的非 Infor 导出**
* **不同子组织各自的导出配置**——例如，子组织 A 使用一个 Infor 导出，子组织 B 使用另一个 Infor 导出

## **创建新的导出配置**

创建新的导出配置：

1. 点击 **“New”** 按钮。 ![](../../../../.gitbook/assets/export_create_new_button.png)
2. 选择要配置的**导出类型**（例如 Infor、IDM、SFTP）。
3. 根据导出类型填写必填字段。
4. 保存配置。

## 导出选项

#### Webhook

<details>

<summary>Webhook</summary>

<figure><img src="../../../../.gitbook/assets/image (11).png" alt="Webhook 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **Export URL** 导出文档的目标 URL。

</details>

#### SFTP

<details>

<summary>SFTP</summary>

<figure><img src="../../../../.gitbook/assets/export_sftp_configuration.png" alt="SFTP 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **Username** 用于向 SFTP 服务器进行身份验证的用户名。
* **Password** 对应的 SFTP 账户密码。请确保该账户对指定文件夹具有写入权限。
* **Server URL** 目标 SFTP 服务器的主机名或 IP 地址。
* **Port** 连接到 SFTP 服务器所使用的端口。
* **Folder** 在 SFTP 服务器上上传文档的路径（例如 `/incoming/invoices/`）。该路径必须已存在且可写入。
*   **XSLT File (Optional)**

    **XSLT 文件**可用于转换 DocBits 的默认导出格式。

    * **使用场景：**仅当接收系统要求采用不同于 DocBits 默认格式的结构或特定格式时使用。
    * 如果默认导出格式符合要求，请**留空**。

**高级设置：**

* **Filename Export Mode** 指定导出的文件保留原文件名，还是使用 DocBits 文档 ID 重新命名。
* **Include Document History** 启用后，导出文件将包含根据仪表板上可用日志生成的文档历史记录。

<figure><img src="../../../../.gitbook/assets/export_sftp_2.png" alt="" width="316"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/export_sftp_3.png" alt=""><figcaption></figcaption></figure>

</details>

#### Infor 导出到 SFTP

<details>

<summary>Infor Export to SFTP</summary>

<figure><img src="../../../../.gitbook/assets/export_infor_sftp_configuration.png" alt="Infor SFTP 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **IDM Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 IDM 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 BOD 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** 在 SFTP 服务器上上传文档的路径（例如 `/incoming/invoices/`）。该路径必须已存在且可写入。

</details>

#### **SMB**

<details>

<summary>SMB</summary>

<figure><img src="../../../../.gitbook/assets/export_smb_configuration.png" alt="SMB 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **Username** 用于连接 SMB 共享的用户名。
* **Password** 用于 SMB 身份验证的对应密码。
* **Server URL** SMB 服务器的地址。
* **Port** 用于访问 SMB 共享的端口号。
* **Folder** SMB 共享中用于保存文档的文件夹路径（例如 `/incoming/invoices/`）。该路径必须已存在且可写入。
*   **JPL Mapping File (Optional)**

    **JPL 文件**用于在导出数据写入 SMB 共享之前定义数据转换。

    * **使用场景：**仅当需要调整导出的文档数据以符合外部格式或系统要求时使用。
    * 如果不需要转换，请**留空**。

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

<figure><img src="../../../../.gitbook/assets/image (10).png" alt="Infor IDM 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **ION Mapping File** 从文件管理器中选择映射文件。
* **IDM Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 IDM 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** 用于指定 Infor 部署类型的开关：
  * **Cloud**：如果使用 Infor CloudSuite，请选择此项。
  * **On-Prem**：如果 Infor 由本地托管，请选择此项。

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

<figure><img src="../../../../.gitbook/assets/export_infor_ion_configuration.png" alt="Infor ION 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **ION Mapping File** 从文件管理器中选择映射文件。
* **BOD Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 BOD 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** 用于指定 Infor 部署类型的开关：
  * **Cloud**：如果使用 Infor CloudSuite，请选择此项。
  * **On-Prem**：如果 Infor 由本地托管，请选择此项。

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

<figure><img src="../../../../.gitbook/assets/export_infor_idm_ion_bod_configuration.png" alt="Infor IDM + ION BOD 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **ION Mapping File** 从文件管理器中选择映射文件。
* **IDM Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 IDM 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 BOD 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** 用于指定 Infor 部署类型的开关：
  * **Cloud**：如果使用 Infor CloudSuite，请选择此项。
  * **On-Prem**：如果 Infor 由本地托管，请选择此项。

</details>

### 对于 Infor CloudSuite 客户

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

<figure><img src="../../../../.gitbook/assets/export_infor_idm_ln_configuration.png" alt="Infor IDM + LN 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **ION Mapping File** 从文件管理器中选择映射文件。
* **IDM Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 IDM 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** 从文件管理器中选择映射文件。[需要帮助？请参阅 LN 导出示例](../../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

<figure><img src="../../../../.gitbook/assets/export_infor_idm_m3_configuration.png" alt="Infor IDM + M3 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **ION Mapping File** 从文件管理器中选择映射文件。
* **IDM Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 IDM 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** 从文件管理器中选择映射文件。[需要帮助？请参阅 M3 映射示例](../../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

<figure><img src="../../../../.gitbook/assets/export_infor_idm_m3_toml_configuration.png" alt="Infor IDM + M3 (toml) 导出配置"><figcaption></figcaption></figure>

**字段说明**

* **Title** 导出配置的名称。该名称会显示在导出列表中。
* **Sub-Organization** _（可选）_ 下拉菜单，列出所有可用的子组织。
  * 留空：适用于主组织。
  * 选择子组织：导出仅适用于所选子组织。
* **Document Type** 下拉菜单，列出所有可用的文档类型。此项决定此导出配置适用于哪种文档。
* **ION Mapping File** 从文件管理器中选择映射文件。
* **IDM Mapping File** 从文件管理器中选择映射文件。[需要帮助创建映射文件？请参阅 IDM 映射指南](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** 从文件管理器中选择映射文件，或选择 Toml 选项以使用通过规则管理器创建的 toml 文件。[需要帮助？请参阅规则管理器指南](../rule-manager/)

</details>
