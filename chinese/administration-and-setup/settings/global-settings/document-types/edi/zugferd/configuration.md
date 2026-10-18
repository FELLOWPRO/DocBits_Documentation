# ZUGFeRD 配置

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits 电子发票教程：处理 XRechnung / ZUGFeRD (Factur-X)、验证数据并自动化工作流
{% endembed %}

## **ZUGFeRD 支持的版本**

DocBits 支持所有主要的 ZUGFeRD 版本，包括：

* **1.0**
* **2.0**
* **2.1**（符合 FACTUR-X 1.0.05）
* **2.2**
* **2.3**（符合 FACTUR-X 1.07.2）
* **2.3.2**

#### 标准的启用与修改

ZUGFeRD 标准默认始终处于启用状态，但您可以根据需要进行修改。

### **修改 ZUGFeRD 设置的步骤：**

1. 前往 **Settings → Global Settings → Document Types → Invoice**。
2. 点击 **E-Doc**。\\
3. 系统将显示所有可用电子文档的列表。
4. 找到要修改的 **ZUGFeRD** 版本。\\

## **转换与 XML 路径配置：**

在**转换设置**中，您可以定义 XML 文件中特定信息的位置，并将其保存为新的结构，以便更轻松地访问数据。\
<mark style="color:red;">**注意**</mark>：如果使用此功能，请在 **Preview** 和 **Extraction Path** 中使用新创建的 XML 路径，而不是原始 XML 路径。

### **修改转换文件的步骤：**

1. 打开 **Transformation**。
2. 点击**铅笔图标**创建新草稿。
3. 选择新创建的草稿。
4. 创建新字段或修改现有字段。
5. 设置所需的数据提取路径。
6. 点击 **Save**。

### 重要说明：

* **预览文件**仅用于 **FACTUR-X**，不用于 **ZUGFeRD**。ZUGFeRD 将使用原始 **PDF**。

## 预览 PDF 配置

**预览 PDF 配置**用于生成便于用户阅读的文档版本。您可以使用 HTML 对其进行自定义，以满足您的需求。

### **修改预览文件的步骤：**

1. 打开 **Preview**。
2. 点击**铅笔图标**创建新草稿。
3. 选择新创建的草稿。
4. 创建新字段或修改现有字段。
5. 设置所需的数据提取路径。
6. 点击 **Save**。

## 提取路径配置

**提取路径配置**用于提取数据并填充**验证界面**中的字段，例如发票表格或发票布局中配置的字段。

### **修改** **提取路径**的步骤：

1. 打开 **Extraction Paths**。
2. 点击**铅笔图标**创建新草稿。
3. 选择新创建的草稿。
4. 创建新字段或修改现有字段。
5. 左侧表示 **DocBits 字段 ID**，可在 **Settings → Global Settings → Document Types → Invoice → Fields** 中找到。\\
6. 右侧表示在 Transformation 中创建的**字段路径**。
7. 点击 **Save**。

按照这些步骤，您可以确保准确提取和验证 ZUGFeRD 发票数据。

## 实际生效的规则与激活

对于检测出的 eDoc 格式，组织专属规则优先于默认规则。请检查活动的 TRANSFORMATION，并确认转换后 XML 中哪个节点提供 invoice_type；路径取决于格式。Save 只保存草稿；测试后需使用勾号激活。渲染后的 Preview 不能证明已保存的文档类型正确。有关代码 381/261、后续脚本和重新处理的注意事项，请参阅[分类故障排查指南](../credit-note-recognized-as-invoice.md)。
