# 如何为特定组织用户创建数据库访问权限

### **1. 登录 DocBits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. 前往应用登录页面。
2. 输入凭据（用户名和密码）以登录。

### **2. 访问设置** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. 登录后，在左侧边栏中找到 **设置** 图标（齿轮 ⚙️）。
2. 点击 **设置**，打开系统配置面板。

### **3. 打开文档处理模块** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. 在 **设置** 中找到 **文档处理** 部分。
2. 在 **文档处理** 下，找到并点击 **模块** 选项。
   * 这将打开相应的模块配置页面，您可以在此创建数据库用户。

### 4. 启用和访问 AI 文档及数据库用户的步骤： <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **切换功能**：
   * 使用右侧的切换开关启用或禁用特定功能：
     * **AI 文档仓库**：切换此选项以启用 AI 相关功能的访问权限。
     * **数据库访问**：切换此选项以授予用户数据库访问权限。
2. **数据库凭据**：
   * 仪表板会提供以下数据库连接详细信息：
     * **用户名**：显示一个唯一的用户名
     * **密码**：请确保安全保存或复制密码。
     * **数据库**：数据库的名称
     * **主机**：主机名
     * **端口**：端口号
     * **SSL 模式：**连接需要使用 `sslmode=require` 进行安全通信。
3. **复制凭据**：
   * 使用各字段旁边的复制图标，快速复制凭据，以便在数据库客户端或应用程序中使用。
4. **通过 DBeaver 连接**：
   * 通过主机连接
     * 选择 PostgreSQL
     * 填写所需信息
     * 切换到 SSL 标签页并勾选 Use SSL。向下滚动到 SSL mode，然后选择 require
   * 通过 URL 连接
     * 填写所需信息：\n - 将 Host 替换为提供的主机信息\n - 将 Port 替换为提供的端口信息\n - 将 Database 替换为提供的数据库信息\n - 在 Username 中选择提供的用户名信息\n - 在 Password 中选择提供的密码信息
5. **测试连接**：
   * 点击 **"Test Connection"** 按钮，确认凭据和连接详细信息正确。
   * 如果测试成功，请继续连接。
6. **浏览数据库**：
   * 连接成功后，在数据库客户端中导航到 **架构** 或 **表** 部分。
   * 检查可用的表。
