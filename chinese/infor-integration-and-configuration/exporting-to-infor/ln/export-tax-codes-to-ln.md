# 将税码导出到 LN

## **概述：**

\
本指南将带您完成设置流程，确保税码能够从 DocBits 正确导出到 LN。

## **单个税码**

### **步骤 1：设置值列表**

1.  前往 **Settings** -> **Document Processing** -> **List of Values**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt=""><figcaption></figcaption></figure>
2.  点击 **New**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt=""><figcaption></figcaption></figure>
3.  创建名为 `Tax_Country` 的列表，然后点击 **Save**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="" width="375"><figcaption></figcaption></figure>
4.  再创建以下三个列表：

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt=""><figcaption></figcaption></figure></div>
5.  点击其中一个新建的列表以打开它。然后点击 **Add Row** 按钮添加新行。

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt=""><figcaption></figcaption></figure>
6.  输入 LN 中相应的所需值，然后点击 **Save** 保存更改。

    * 如果有多个值，可以点击 **Add More Values** 添加。

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt=""><figcaption></figcaption></figure></div>

    * **注意：**您可以在 LN 中通过以下路径找到税码：**Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt=""><figcaption></figcaption></figure>

### **步骤 2：在 DocBits 中添加字段**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  在要添加字段的文档类型对应的菜单中选择 **Fields**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt=""><figcaption></figcaption></figure>
3.  在 **VAT & Amounts** 下，按如下方式创建六个新字段：

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt=""><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>名称</strong></td><td><strong>标题</strong></td><td><strong>字段类型</strong></td><td><strong>值列表</strong></td></tr><tr><td><code>tax_country</code></td><td>税务国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>税务国家/地区（减免）</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>免税国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>税码</td><td>下拉列表</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>减免税码</td><td>下拉列表</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>免税税码</td><td>下拉列表</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt=""><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt=""><figcaption></figcaption></figure></div>

4.  保存每个字段后，点击 **Save Settings** 应用更改。

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt=""><figcaption></figcaption></figure>

### **步骤 3：编辑布局**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  打开要编辑的文档类型对应的 **Edit Layout** 菜单。

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt=""><figcaption></figcaption></figure>
3.  选择要应用税码的 **Document Origin**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt=""><figcaption></figcaption></figure>
4.  向下滚动到 **Tax Details** 部分。

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt=""><figcaption></figcaption></figure>
5. 展开 **Form Elements** 下拉菜单。
6.  在 **Tax Details** 部分使用 **Horizontal Separator Tool**。将其拖放到税务部分的子部分之间，以便清楚地分隔各部分并减少混淆。

    <figure><img src="../../../.gitbook/assets/TaxCodes_22 (1).png" alt=""><figcaption></figcaption></figure>
7. 展开 **Form Fields** 下拉菜单。
8.  搜索 **Tax Country**，然后将该字段拖放到相应区域。

    <figure><img src="../../../.gitbook/assets/TaxCodes_23 (2).png" alt=""><figcaption></figcaption></figure>
9.  搜索 **Tax Code**，然后将该字段拖放到对应区域。

    <figure><img src="../../../.gitbook/assets/TaxCodes_24 (1).png" alt=""><figcaption></figcaption></figure>
10. 保存模板。

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt=""><figcaption></figcaption></figure>

### 步骤 4：验证配置是否生效

在 DocBits 中上传新文档并选择正确的文档设置后，您现在应该可以选择在步骤 1 的列表中添加的税码。

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt=""><figcaption></figcaption></figure>

## 多个税码

### **步骤 1：设置值列表**

1.  前往 **Settings** -> **Document Processing** -> **List of Values**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt=""><figcaption></figcaption></figure>
2.  点击 **New**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt=""><figcaption></figcaption></figure>
3.  创建名为 `Tax_Country` 的列表，然后点击 **Save**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="" width="375"><figcaption></figcaption></figure>
4.  再创建以下三个列表：

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt=""><figcaption></figcaption></figure></div>
5.  点击其中一个新建的列表以打开它。然后点击 **Add Row** 按钮添加新行。

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt=""><figcaption></figcaption></figure>
6.  输入 LN 中相应的所需值，然后点击 **Save** 保存更改。

    * 如果有多个值，可以点击 **Add More Values** 添加。

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt=""><figcaption></figcaption></figure></div>

    * **注意：**您可以在 LN 中通过以下路径找到税码：**Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt=""><figcaption></figcaption></figure>

### **步骤 2：在 DocBits 中添加字段**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  在要添加字段的文档类型对应的菜单中选择 **Fields**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt=""><figcaption></figcaption></figure>
3.  在 **VAT & Amounts** 下，按如下方式创建六个新字段：

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt=""><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>名称</strong></td><td><strong>标题</strong></td><td><strong>字段类型</strong></td><td><strong>值</strong></td></tr><tr><td><code>tax_country</code></td><td>税务国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>税务国家/地区（减免）</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>免税国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>税码</td><td>下拉列表</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>减免税码</td><td>下拉列表</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>免税税码</td><td>下拉列表</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt=""><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt=""><figcaption></figcaption></figure></div>

4.  保存每个字段后，点击 **Save Settings** 应用更改。

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt=""><figcaption></figcaption></figure>

### **步骤 3：编辑布局**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  打开要编辑的文档类型对应的 **Edit Layout** 菜单。

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt=""><figcaption></figcaption></figure>
3.  选择要应用税码的 **Document Origin**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt=""><figcaption></figcaption></figure>
4.  向下滚动到 **Tax Details** 部分。

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt=""><figcaption></figcaption></figure>
5. 展开 **Form Elements** 下拉菜单。
6.  在 **Tax Details** 部分使用 **Sub Group** 工具。将其拖放到现有字段旁边。

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt=""><figcaption></figcaption></figure>
7.  要为子组命名，请点击该子组，并在 **Label** 字段中输入所需名称。

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt=""><figcaption></figcaption></figure></div>
8.  将与此组对应的字段拖放到 **Sub Group** 字段中。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt=""><figcaption></figcaption></figure>
9. 展开 **Fields** 下拉菜单。
10. 搜索 **Tax**，然后将相应字段（例如 **Tax Country** 和 **Tax Code**）拖放到对应的子组中。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt=""><figcaption></figcaption></figure>
11. 将步骤 5 到 10 重复两次，直到达到以下状态：

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt=""><figcaption></figcaption></figure>
12. 保存模板。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt=""><figcaption></figcaption></figure>

### 步骤 4：验证配置是否生效以及结果变化

在 DocBits 中上传新文档并选择正确的文档设置后，您可以选择在步骤 1 中添加的税码，并添加在步骤 3 中配置的多个税码。

* 文档将显示三个不同的部分：分别用于完整税额、减免税额和免税额。
* 点击某个部分中的加号按钮会创建副本，以便按选定的税率添加多笔申报。

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt=""><figcaption></figcaption></figure>

* 点击移除按钮即可删除部分。

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt=""><figcaption></figcaption></figure>

* 总金额将按所有部分的金额之和计算。
* 总金额的验证将根据所有税务部分进行调整。
* 只有在视图中添加字段后，才能对新部分应用脚本。

### LN 说明：

在 **LN** 中，USt Position 将根据税码/税务国家（地区）下拉菜单中的位置编号填写。导出时只会发送位置编号。

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt=""><figcaption></figcaption></figure>

#### **导出映射**

要将税行关联到成本行：

1. 将 `TaxLine` 添加到 **InvoiceCostFields** 列表。
2. 按照以下示例添加条目：\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt=""><figcaption></figcaption></figure>
