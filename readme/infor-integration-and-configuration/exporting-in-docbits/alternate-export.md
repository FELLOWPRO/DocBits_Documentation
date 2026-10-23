# 备用导出

## **步骤 1：创建新的导出**

1. 前往 **设置** > **文档处理** > **导出**。
2. 点击 **创建新导出**，以定义新的导出配置。
3. 保存配置，并确保导出处于**禁用**状态。

<figure><img src="../../.gitbook/assets/image (187).png" alt="导出设置列表，包含文档类型Invoice的Alternate-Export-Invoice-LN-IDM-BOD和Export-Invoice-LN行、导出方法Infor-IoN-Cloud以及操作图标"><figcaption></figcaption></figure>

### **步骤 2：启用备用导出**

1. 前往 **设置** > **全局设置** > **文档类型** > **更多设置**。
2. 找到 **备用导出** 设置并将其切换为**开启**。
3. 配置以下内容：
   * **文档状态**：指定备用导出后文档的状态。
   * **导出配置**：选择要用于备用导出的新建导出配置。

<figure><img src="../../.gitbook/assets/image (188).png" alt="Invoice文档类型的More Settings页面，显示状态为Pending approval的Alternate Export选项以及Export Configuration Alternate-Export-Invoice-LN-IDM-BOD-8203"><figcaption></figcaption></figure>

## 使用备用导出

**在 PO 匹配界面中**

* 启用备用导出后，你可以直接在 **PO 匹配** 界面中选择备用导出。

<figure><img src="../../.gitbook/assets/image (189).png" alt="PO Matching界面，搜索采购订单号100000300，包含CONFIRM &amp;amp; EXPORT和Reject按钮以及Document Alternate Export面板"><figcaption></figcaption></figure>

**使用工作流卡片**

* 也可以使用 **备用导出** 工作流卡片自动执行此流程。根据需要配置该卡片，将备用导出逻辑应用于工作流。
