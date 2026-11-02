---
hidden: true
noIndex: true
---

# M3\_OLD

## 在 Infor M3 中导入 API 连接模板

本指南介绍如何导入 API 连接模板，以快速配置与 Infor M3 集成所需的关键设置。使用模板可以建立预定义的连接配置，从而简化流程并确保配置一致。

<mark style="color:red;">**注意**</mark>：有关自动会计、供应商集成、采购订单或成本要素表格提取等特定领域的详细配置，请参阅相应文档：

* [自动会计](m3/auto-accounting.md)
* [供应商和采购订单](m3/suppliers-and-purchase-orders.md)
* [如何导入所有供应商](m3/how-to-import-all-suppliers.md)
* [成本要素表格提取](m3/table-extraction-for-costing-element.md)

### **下载模板**

导入前，请使用以下文件下载所需的连接模板：

{% file src="../../.gitbook/assets/DocBits-Dev-Import-Template (1).xml" %}

### 导入模板

#### 导入连接模板的步骤

1. **访问 Infor ION Desk：**
   *   前往 **InforOS** → **ION Desk** → **Connect** → **Connection Points**。

       ![Infor ION Desk导航菜单，其中包含Home、Data Flows、API Flows和Mappings条目](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **导入模板：**
   *   点击 **Import** 按钮。

       <figure><img src="../../.gitbook/assets/m3_import_2.png" alt="Infor ION Desk 的 Connect 页面，显示 Connection Points 视图及其搜索栏和工具栏"><figcaption></figcaption></figure>
   * 从本地系统中选择相应的 **Template File**。
   *   点击 **OK** 开始导入。

       <figure><img src="../../.gitbook/assets/m3_import_3.png" alt="Infor ION Desk 中的 Upload Local File 对话框，已选择文件 DocBits-Dev-Prod-Import-Template 进行上传" width="327"><figcaption></figcaption></figure>
3. **确认：**
   *   如果导入成功，系统将显示确认消息。

       <figure><img src="../../.gitbook/assets/m3_import_4.png" alt="Infor ION Desk 中的导入确认，显示 DocBits-Dev-Prod-Import-Template 的导入已成功"><figcaption></figcaption></figure>
4. **导入后配置：**
   * 导入模板后，您可以根据需要自定义特定的连接设置。
   * 请记得导入或配置用于身份验证和访问控制的 **Service Account**。

<figure><img src="../../.gitbook/assets/m3_import_5.png" alt="DocBits-Dev-Prod-Import-Template 的 API Connection Point 页面，显示其名称、逻辑 ID 和身份验证详情"><figcaption></figcaption></figure>
