# 采购订单容差设置 / 其他采购订单容差

## 配置采购订单匹配规则和容差

本教程打开“发票”文档类型，检查已发布的规则版本，并将其克隆为未激活的草稿。内容包括规则类型、匹配阶段内的优先级、比较列、数量基准、匹配模式以及容差计算。仅保存教程草稿；活动版本和全局容差保持不变。百分之五的计算只是示例，并不修改当前容差。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-rules-admin/v3/zh.mp4" %}

[观看带字幕的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-rules-admin/v3/zh.html)

## **配置采购订单容差的设置**

前往 **Settings → General Settings → Document Types → More Settings → Purchase Order Section → PO Tolerance Setting**

### **工作原理**

启用此设置后，您可以为**数量**和/或**单价**定义容差。容差可以按百分比或固定值设置。这意味着发票与采购订单（PO）之间的差异只要在指定的容差范围内，就不会被标记为不匹配，从而在确保顺畅处理的同时提供灵活性。

<mark style="color:red;">**注意**</mark>**：**容差适用于两个方向；也就是说，在允许范围内，发票值可以高于或低于 PO 值。

### **设置方法**

1. **启用设置：**
   * 使用切换按钮打开 PO Tolerance Setting。
2. **配置容差：**
   * 页面上会显示四个字段：
     * 一个用于设置**数量容差金额**。
     * 一个用于设置**单价容差金额**。
   * 每个字段旁边都有一个下拉菜单，可用于选择容差类型：
     * **Percent：**表示按百分比设置容差。
     * **Value：**表示按固定金额设置容差，规定数值可产生的差异。

<figure><img src="../../../../../../.gitbook/assets/image (407).png" alt="Purchase Order 部分的设置页面，包含 PO Tolerance Setting 选项"><figcaption></figcaption></figure>

### **示例场景：**

* 假设**单价容差**设置为 **5%**。
* 采购订单包含两个行项目：
  * **行项目 1：**单价 = **$5.00**
  * **行项目 2：**单价 = **$2.00**
* 发票上：
  * **行项目 1：**单价调整为 **$4.80**（在 5% 容差范围内）。
  * **行项目 2：**单价调整为 **$2.20**（超出 5% 容差范围）。
* **结果：**
  * 行项目 1**不会被标记**为不匹配，因为 $4.80 与 $5.00 的差异在 5% 以内。
  * 行项目 2**会被标记**为不匹配，因为 $2.20 与 $2.00 的差异超过了允许的 5% 范围。此时，用户需要采取措施解决不匹配问题，然后才能继续处理发票。

<figure><img src="../../../../../../.gitbook/assets/image (408).png" alt="PO Tolerance 表格，包含 UNIT、PO: QUANTITY、INVOICE: QUANTITY、PO: UNITPRICE 和 INVOICE: UNIT PRICE 列"><figcaption></figcaption></figure>

## 配置其他采购订单容差设置的设置 <a id="setting-to-configure-additional-purchase-order-tolerance-settings"></a>

前往 **Settings → General Settings → Document Types → More Settings → Purchase Order Section → Additional PO Tolerance Setting**

### **工作原理**

启用此设置后，您可以为**运费**、**费用**和/或**税费**定义容差。容差可以按百分比或固定值设置，使发票与 PO 值之间的小幅差异不会被标记为不匹配。这样可以提供更大的灵活性，并确保细微差异不会中断工作流。

<mark style="color:red;">**注意**</mark>**：**与标准容差设置一样，这些容差也适用于两个方向——在设定的限值内，数值可以增加或减少。

### **设置方法**

1. **启用设置：**
   * 使用切换按钮打开 Additional PO Tolerance Setting。
2. **配置容差：**
   * 页面上会显示六个字段：
     * 分别用于设置**运费**、**费用**和**税费**的容差金额。
   * 每个字段旁边都有一个下拉菜单，可用于选择容差类型：
     * **Percent：**按百分比定义容差。
     * **Value：**按固定金额定义容差。

<figure><img src="../../../../../../.gitbook/assets/image (409).png" alt="Freight Tolerance % 和 Additional PO Tolerance Setting 的设置字段，包含百分比值和一个开关"><figcaption></figcaption></figure>
