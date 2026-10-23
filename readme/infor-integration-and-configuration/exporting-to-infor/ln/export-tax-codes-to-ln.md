# 将税码导出到 LN

## **概述：**

\
本指南将带您完成设置流程，确保税码能够从 DocBits 正确导出到 LN。

## **单个税码**

### **步骤 1：设置值列表**

1.  前往 **Settings** -> **Document Processing** -> **List of Values**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt="DocBits的List of Values页面，位于Settings下Document Processing部分，从Settings侧边栏打开"><figcaption></figcaption></figure>
2.  点击 **New**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="List of Values页面，工具栏中New按钮被高亮显示"><figcaption></figcaption></figure>
3.  创建名为 `Tax_Country` 的列表，然后点击 **Save**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="New List of Values对话框，输入了名称Tax_Country并可见Save按钮" width="375"><figcaption></figcaption></figure>
4.  再创建以下三个列表：

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="List of Values页面，列表中已创建Tax_Code_Full条目"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="List of Values页面，列表中已创建Tax_Code_Reduced条目"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="List of Values页面，列表中已创建Tax_Code_Free条目"><figcaption></figcaption></figure></div>
5.  点击其中一个新建的列表以打开它。然后点击 **Add Row** 按钮添加新行。

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Tax_Country的List of Values页面，工具栏中可见Add Row按钮"><figcaption></figcaption></figure>
6.  输入 LN 中相应的所需值，然后点击 **Save** 保存更改。

    * 如果有多个值，可以点击 **Add More Values** 添加。

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Tax_Country值列表，包含一个新行条目和Save按钮"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt="Tax_Country值列表，包含多个值行以及Add More Values按钮"><figcaption></figcaption></figure></div>

    * **注意：**您可以在 LN 中通过以下路径找到税码：**Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Common、Taxation、Master Data下的LN Tax Codes by Country屏幕，显示税码概览"><figcaption></figcaption></figure>

### **步骤 2：在 DocBits 中添加字段**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="DocBits的Global Settings页面，导航中Document Types菜单已打开"><figcaption></figcaption></figure>
2.  在要添加字段的文档类型对应的菜单中选择 **Fields**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Document Types页面，菜单中某个文档类型的Fields选项已打开"><figcaption></figcaption></figure>
3.  在 **VAT & Amounts** 下，按如下方式创建六个新字段：

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="文档类型的字段设置页面，VAT and Amounts部分已展开"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>名称</strong></td><td><strong>标题</strong></td><td><strong>字段类型</strong></td><td><strong>值列表</strong></td></tr><tr><td><code>tax_country</code></td><td>税务国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>税务国家/地区（减免）</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>免税国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>税码</td><td>下拉列表</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>减免税码</td><td>下拉列表</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>免税税码</td><td>下拉列表</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt="字段设置页面，其中包含新的下拉字段Tax Country和值列表Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt="Fields settings页面，包含新的下拉字段Tax Country Reduced和值列表Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="字段设置页面，包含新的下拉字段Tax Country Free以及值列表Tax_Country"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt="Fields settings页面，包含新的下拉字段Tax Code和值列表Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt="Fields设置页面，包含新的下拉字段Tax Code Reduced和值列表Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt="Fields settings页面，包含新的下拉字段Tax Code Free和List of Values Tax_Code_Free"><figcaption></figcaption></figure></div>

4.  保存每个字段后，点击 **Save Settings** 应用更改。

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Fields settings页面，显示新建的税字段并突出显示Save Settings按钮"><figcaption></figcaption></figure>

### **步骤 3：编辑布局**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="DocBits的Global Settings页面，导航中Document Types菜单已打开"><figcaption></figcaption></figure>
2.  打开要编辑的文档类型对应的 **Edit Layout** 菜单。

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Document Types页面，菜单中某个文档类型的Edit Layout选项已打开"><figcaption></figcaption></figure>
3.  选择要应用税码的 **Document Origin**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="布局编辑器，Document Origin下拉列表已打开，用于选择相应的来源"><figcaption></figcaption></figure>
4.  向下滚动到 **Tax Details** 部分。

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="布局编辑器已向下滚动到文档模板的Tax Details部分"><figcaption></figcaption></figure>
5. 展开 **Form Elements** 下拉菜单。
6.  在 **Tax Details** 部分使用 **Horizontal Separator Tool**。将其拖放到税务部分的子部分之间，以便清楚地分隔各部分并减少混淆。

    <figure><img src="../../../.gitbook/assets/TaxCodes_22 (1).png" alt="布局编辑器，Form Elements下拉菜单已展开，Horizontal Separator工具高亮显示"><figcaption></figcaption></figure>
7. 展开 **Form Fields** 下拉菜单。
8.  搜索 **Tax Country**，然后将该字段拖放到相应区域。

    <figure><img src="../../../.gitbook/assets/TaxCodes_23 (2).png" alt="布局编辑器，Form Fields下拉列表已展开，正在搜索Tax Country字段"><figcaption></figcaption></figure>
9.  搜索 **Tax Code**，然后将该字段拖放到对应区域。

    <figure><img src="../../../.gitbook/assets/TaxCodes_24 (1).png" alt="布局编辑器，Form Fields下拉列表已展开，正在搜索Tax Code字段"><figcaption></figcaption></figure>
10. 保存模板。

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="布局编辑器，放置税额字段后Save按钮突出显示"><figcaption></figcaption></figure>

### 步骤 4：验证配置是否生效

在 DocBits 中上传新文档并选择正确的文档设置后，您现在应该可以选择在步骤 1 的列表中添加的税码。

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="已上传文档的验证屏幕，税码下拉列表的值已展开"><figcaption></figcaption></figure>

## 多个税码

### **步骤 1：设置值列表**

1.  前往 **Settings** -> **Document Processing** -> **List of Values**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt="DocBits的List of Values页面，位于Settings下Document Processing部分，从Settings侧边栏打开"><figcaption></figcaption></figure>
2.  点击 **New**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="List of Values页面，工具栏中New按钮被高亮显示"><figcaption></figcaption></figure>
3.  创建名为 `Tax_Country` 的列表，然后点击 **Save**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="New List of Values对话框，输入了名称Tax_Country并可见Save按钮" width="375"><figcaption></figcaption></figure>
4.  再创建以下三个列表：

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="List of Values页面，列表中已创建Tax_Code_Full条目"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="List of Values页面，列表中已创建Tax_Code_Reduced条目"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="List of Values页面，列表中已创建Tax_Code_Free条目"><figcaption></figcaption></figure></div>
5.  点击其中一个新建的列表以打开它。然后点击 **Add Row** 按钮添加新行。

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Tax_Country的List of Values页面，工具栏中可见Add Row按钮"><figcaption></figcaption></figure>
6.  输入 LN 中相应的所需值，然后点击 **Save** 保存更改。

    * 如果有多个值，可以点击 **Add More Values** 添加。

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Tax_Country值列表，包含一个新行条目和Save按钮"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt="Tax_Country值列表，包含多个值行以及Add More Values按钮"><figcaption></figcaption></figure></div>

    * **注意：**您可以在 LN 中通过以下路径找到税码：**Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Common、Taxation、Master Data下的LN Tax Codes by Country屏幕，显示税码概览"><figcaption></figcaption></figure>

### **步骤 2：在 DocBits 中添加字段**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="DocBits的Global Settings页面，导航中Document Types菜单已打开"><figcaption></figcaption></figure>
2.  在要添加字段的文档类型对应的菜单中选择 **Fields**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Document Types页面，菜单中某个文档类型的Fields选项已打开"><figcaption></figcaption></figure>
3.  在 **VAT & Amounts** 下，按如下方式创建六个新字段：

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="文档类型的字段设置页面，VAT and Amounts部分已展开"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>名称</strong></td><td><strong>标题</strong></td><td><strong>字段类型</strong></td><td><strong>值</strong></td></tr><tr><td><code>tax_country</code></td><td>税务国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>税务国家/地区（减免）</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>免税国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>税码</td><td>下拉列表</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>减免税码</td><td>下拉列表</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>免税税码</td><td>下拉列表</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt="字段设置页面，其中包含新的下拉字段Tax Country和值列表Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt="Fields settings页面，包含新的下拉字段Tax Country Reduced和值列表Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="字段设置页面，包含新的下拉字段Tax Country Free以及值列表Tax_Country"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt="Fields settings页面，包含新的下拉字段Tax Code和值列表Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt="Fields设置页面，包含新的下拉字段Tax Code Reduced和值列表Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt="Fields settings页面，包含新的下拉字段Tax Code Free和List of Values Tax_Code_Free"><figcaption></figcaption></figure></div>

4.  保存每个字段后，点击 **Save Settings** 应用更改。

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Fields settings页面，显示新建的税字段并突出显示Save Settings按钮"><figcaption></figcaption></figure>

### **步骤 3：编辑布局**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="DocBits的Global Settings页面，导航中Document Types菜单已打开"><figcaption></figcaption></figure>
2.  打开要编辑的文档类型对应的 **Edit Layout** 菜单。

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Document Types页面，菜单中某个文档类型的Edit Layout选项已打开"><figcaption></figcaption></figure>
3.  选择要应用税码的 **Document Origin**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="布局编辑器，Document Origin下拉列表已打开，用于选择相应的来源"><figcaption></figcaption></figure>
4.  向下滚动到 **Tax Details** 部分。

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="布局编辑器已向下滚动到文档模板的Tax Details部分"><figcaption></figcaption></figure>
5. 展开 **Form Elements** 下拉菜单。
6.  在 **Tax Details** 部分使用 **Sub Group** 工具。将其拖放到现有字段旁边。

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="布局编辑器，展开Form Elements下拉菜单并突出显示Sub Group工具"><figcaption></figcaption></figure>
7.  要为子组命名，请点击该子组，并在 **Label** 字段中输入所需名称。

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="布局编辑器，Tax Details部分中新添加的Sub Group元素处于选中状态"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="布局编辑器，所选Sub Group的Label字段已打开以便命名"><figcaption></figcaption></figure></div>
8.  将与此组对应的字段拖放到 **Sub Group** 字段中。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="布局编辑器，正在将一个字段拖入Tax Details部分的新Sub Group中"><figcaption></figcaption></figure>
9. 展开 **Fields** 下拉菜单。
10. 搜索 **Tax**，然后将相应字段（例如 **Tax Country** 和 **Tax Code**）拖放到对应的子组中。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="布局编辑器，Fields下拉列表已展开，正在搜索Tax Country字段"><figcaption></figcaption></figure>
11. 将步骤 5 到 10 重复两次，直到达到以下状态：

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="布局编辑器，重复这些步骤后，税务子组已放置在Tax Details部分中"><figcaption></figcaption></figure>
12. 保存模板。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="布局编辑器，排列税务子组后突出显示Save按钮"><figcaption></figcaption></figure>

### 步骤 4：验证配置是否生效以及结果变化

在 DocBits 中上传新文档并选择正确的文档设置后，您可以选择在步骤 1 中添加的税码，并添加在步骤 3 中配置的多个税码。

* 文档将显示三个不同的部分：分别用于完整税额、减免税额和免税额。
* 点击某个部分中的加号按钮会创建副本，以便按选定的税率添加多笔申报。

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="已上传文档的验证界面，其中显示带有加号按钮的税务部分"><figcaption></figcaption></figure>

* 点击移除按钮即可删除部分。

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="已上传文档的验证界面，包含税务部分且移除按钮被高亮显示"><figcaption></figcaption></figure>

* 总金额将按所有部分的金额之和计算。
* 总金额的验证将根据所有税务部分进行调整。
* 只有在视图中添加字段后，才能对新部分应用脚本。

### LN 说明：

在 **LN** 中，USt Position 将根据税码/税务国家（地区）下拉菜单中的位置编号填写。导出时只会发送位置编号。

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="LN屏幕，显示根据税码位置编号填写的USt Position字段"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="LN屏幕，显示已导出的发票及已填写的USt Position值"><figcaption></figcaption></figure>

#### **导出映射**

要将税行关联到成本行：

1. 将 `TaxLine` 添加到 **InvoiceCostFields** 列表。
2. 按照以下示例添加条目：\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="InvoiceCostFields的List of Values，包含TaxLine条目和ICF_TaxLine映射"><figcaption></figcaption></figure>
