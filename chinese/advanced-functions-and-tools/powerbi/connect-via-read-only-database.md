# 通过只读数据库连接

本指南将介绍如何使用 **PostgreSQL ODBC 驱动程序**将 **DocBits 只读数据库连接到 Power BI Desktop**。内容涵盖驱动程序安装、ODBC 配置、Power BI 集成和计划刷新。

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

#### 1. 安装 PostgreSQL ODBC 驱动程序

* 从官方网站下载最新的 PostgreSQL ODBC 驱动程序（**psqlODBC**）：
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* 运行安装程序并按照安装向导操作。

#### 2. 配置 ODBC 数据源

* 通过控制面板或 Windows 搜索打开 **ODBC 数据源管理器（64 位）**。
* 转到 **系统 DSN** 选项卡，然后点击 **添加**。
* 从列表中选择 **PostgreSQL Unicode(x64)** 驱动程序，然后点击 **完成**。
* 使用以下位置提供的凭据填写必填字段：\n  **DocBits → 设置 → 文档处理 → 模块 → AI 仪表板 → 只读数据库访问**

<figure><img src="../../.gitbook/assets/connect_read_only_4.png" alt=""><figcaption></figcaption></figure>

**必填字段：**

* **名称：** 连接名称（例如，`Sandbox-Read_Only`）
* **服务器：** 从 DocBits 复制主机值
* **端口：** 从 DocBits 复制端口值
* **数据库：** 从 DocBits 复制数据库名称
* **用户名：** 从 DocBits 复制用户名
* **密码：** 从 DocBits 复制密码
* **SSL 模式：** 设置为 **Require**（确保通信加密）

#### 3. 将只读数据库连接到 Power BI

* 打开 **Power BI Desktop**。
*   选择 **获取数据** → **ODBC** → **连接**。

    <figure><img src="../../.gitbook/assets/powerbi_get_data_odbc.png" alt="Power BI 获取数据 ODBC"><figcaption></figcaption></figure>
* 在 DSN 列表中，选择已配置的数据源（例如，`Sandbox-Read_Only`）。

<figure><img src="../../.gitbook/assets/connect_read_only_3.png" alt=""><figcaption></figcaption></figure>

* 点击 **确定**。如果系统提示，请再次输入凭据。
  * <mark style="color:red;">**注意：**</mark> 如果看到错误 **“password authentication failed for user”**，请尝试将密码用**花括号 `{}`**括起来后输入。

#### 4. 加载和转换数据

* 在 **导航器**窗格中展开架构列表。
* 打开 **`public`** 架构。
* 选择要导入的表。

![](../../.gitbook/assets/connect_read_only_1.png)        ![](../../.gitbook/assets/connect_read_only_2.png)

* 选择：
  * **加载** → 直接导入 Power BI
  * **转换数据** → 打开 Power Query，在加载前整理和筛选数据

#### 5. 可视化数据

* 使用 Power BI 报表画布构建仪表板。
* 拖动字段、添加切片器、选择图表类型并应用 DAX 计算。
* 创建可视化内容前，使用 **Power Query 编辑器**清理或联接数据。
* 参考：[Power BI 文档](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

#### 6. 启用计划刷新（可选）

<mark style="color:red;">**注意：**</mark> **需要 Power BI Pro 或 Premium 以及网关**

* 若要使报表与 ClickHouse 保持同步：
* 将 `.pbix` 文件发布到 **Power BI Service**。
* 在可访问 ClickHouse 网络的计算机上以标准模式安装 **Power BI Gateway**。
* 在 Power BI Service 中：
  * 转到数据集 → **设置** → **计划刷新**
  * 映射 DSN 并提供凭据
* 更多信息请参阅[此处](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance)。&#x20;

#### 7. 仪表板和数据视图示例&#x20;

<div><figure><img src="../../.gitbook/assets/powerbi_dashboard_example_1.png" alt="Power BI 仪表板示例 1"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_2.png" alt="Power BI 仪表板示例 2"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_3.png" alt="Power BI 仪表板示例 3"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_4.png" alt="Power BI 仪表板示例 4"><figcaption></figcaption></figure></div>
