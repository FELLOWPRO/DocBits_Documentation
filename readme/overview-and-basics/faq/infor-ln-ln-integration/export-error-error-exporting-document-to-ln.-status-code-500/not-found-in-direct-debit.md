# 直接扣款中未找到

## **步骤 1：检查 LN 配置**

1. 登录 **LN CE**。
2. 前往 **Options** 菜单并选择 **Run Program**。
3. 在输入框中输入 **ACP Parameters**，然后按 Enter 键打开该程序。
4. 点击 **Actual Set** 字段旁边的箭头以展开设置。
5. 前往 **Matching** 部分。
   * **检查自动匹配设置：**
     * 如果 **Automatic Matching** 设置为 **Match to Purchase Receipt**，请继续下一步。
     * 如果未设置为 **Match to Purchase Receipt**，但您仍遇到此错误，请联系我们。

## **步骤 2：打开 DocBits 设置**

如果 **Automatic Matching** 设置为 **Match to Purchase Receipt**，请在 DocBits 中执行以下步骤：

1. 打开 **DocBits** 并前往 **Settings** 部分。
2. 前往 **Document Processing**。
3. 选择 **Export**。
4. 在 **Export** 部分，点击无法正常工作的导出项旁边的 **three dots** 图标，然后选择 **Edit**。
5. 在 **Edit Export Settings** 菜单中，点击 **Download the LN-Mapping** 文件。

## **步骤 3：编辑 LN-Mapping 文件**

1. 打开下载的 **LN-Mapping** 文件。
2. 搜索字段 **IRF\_PackingSlip**。
   * 如果存在字段 **IRF\_PackingSlip**，且其值为空（empty），请将其更新为 **TF\_packing\_slip**。
   * 如果字段 **IRF\_PackingSlip** 不存在，请将其添加到文件中，并将其值设为 **TF\_packing\_slip**。
3. 对于字段 **InvoiceReceiptFields**，请将 **PackingSlip** 添加到值中。

文件应如下所示：

<figure><img src="../../../../.gitbook/assets/image (390).png" alt="LN-Mapping文件，字段IRF_PackingSlip设置为TF_packing_slip，并将PackingSlip添加到InvoiceReceiptFields"><figcaption></figcaption></figure>

## **步骤 4：将更新后的文件添加回 DocBits**

1. 返回 DocBits 中之前下载 **LN-Mapping** 文件的 **Export** 部分。
2. 上传已编辑并包含新更新的 **LN-Mapping** 文件。

## 如果您仍遇到状态代码为 **500** 的 **Error exporting document to LN**，请联系我们
