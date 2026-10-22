# 将税码导出到 LN

## **概述：**

\
本指南将带您完成设置流程，确保税码能够从 DocBits 正确导出到 LN。

## **单个税码**

### **步骤 1：设置值列表**

1.  前往 **Settings** -> **Document Processing** -> **List of Values**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt="已打开的 Settings 菜单，显示 Document Processing 分组和 List of Values 条目"><figcaption>Settings：Document Processing > List of Values</figcaption></figure>
2.  点击 **New**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="List of Values 页面，显示已有列表和 New 按钮"><figcaption>List of Values 页面及已有列表</figcaption></figure>
3.  创建名为 `Tax_Country` 的列表，然后点击 **Save**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Create New list 对话框，名称已填写为 Tax_Country" width="375"><figcaption>创建列表 Tax_Country</figcaption></figure>
4.  再创建以下三个列表：

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Create New list 对话框，名称已填写为 Tax_Code_Full"><figcaption>创建列表 Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Create New list 对话框，名称已填写为 Tax_Code_Reduced"><figcaption>创建列表 Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Create New list 对话框，名称已填写为 Tax_Code_Free"><figcaption>创建列表 Tax_Code_Free</figcaption></figure></div>
5.  点击其中一个新建的列表以打开它。然后点击 **Add Row** 按钮添加新行。

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="List of Values 页面，打开列表下方有 Add Row 按钮"><figcaption>在打开的列表中添加一行</figcaption></figure>
6.  输入 LN 中相应的所需值，然后点击 **Save** 保存更改。

    * 如果有多个值，可以点击 **Add More Values** 添加。

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Create values 对话框，Name 字段已填写 LN 税码"><figcaption>在 Name 字段中输入 LN 税码</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt="Create values 对话框，通过 Add More Values 添加了值 800"><figcaption>通过 Add More Values 添加第二个值</figcaption></figure></div>

    * **注意：**您可以在 LN 中通过以下路径找到税码：**Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN 的 Tax Codes by Country 会话，显示奥地利及 Tax Code 和 Kind of Tax 列"><figcaption>LN：Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **步骤 2：在 DocBits 中添加字段**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="已打开的 Global Settings 菜单，显示 Document Types 条目"><figcaption>Settings：Global Settings > Document Types</figcaption></figure>
2.  在要添加字段的文档类型对应的菜单中选择 **Fields**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Document Types 页面，每个文档类型下方有 Fields 菜单"><figcaption>打开文档类型的 Fields 菜单</figcaption></figure>
3.  在 **VAT & Amounts** 下，按如下方式创建六个新字段：

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Fields 选项卡，显示 VAT &amp; Amounts 分组和 Create New 按钮"><figcaption>Fields 选项卡：VAT &amp; Amounts 分组</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>名称</strong></td><td><strong>标题</strong></td><td><strong>字段类型</strong></td><td><strong>值列表</strong></td></tr><tr><td><code>tax_country</code></td><td>税务国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>税务国家/地区（减免）</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>免税国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>税码</td><td>下拉列表</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>减免税码</td><td>下拉列表</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>免税税码</td><td>下拉列表</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt="tax_country 的 Document field details 对话框，字段类型 Dropdown，列表 Tax_Country"><figcaption>字段 tax_country：Dropdown，列表 Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt="tax_country_2 的 Document field details 对话框，标题为 Tax Country Reduced"><figcaption>字段 tax_country_2：Dropdown，列表 Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="tax_country_3 的 Document field details 对话框，标题为 Tax Country Free"><figcaption>字段 tax_country_3：Dropdown，列表 Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt="tax_code_without_country 的 Document field details 对话框，列表 Tax_Code_Full"><figcaption>字段 tax_code_without_country：Dropdown，列表 Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt="tax_code_without_country_2 的 Document field details 对话框，列表 Tax_Code_Reduced"><figcaption>字段 tax_code_without_country_2：Dropdown，列表 Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt="tax_code_without_country_3 的 Document field details 对话框，列表 Tax_Code_Free"><figcaption>字段 tax_code_without_country_3：Dropdown，列表 Tax_Code_Free</figcaption></figure></div>

4.  保存每个字段后，点击 **Save Settings** 应用更改。

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Fields 选项卡，字段列表上方有 Save Settings 按钮"><figcaption>点击 Save Settings 应用新字段</figcaption></figure>

### **步骤 3：编辑布局**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="已打开的 Global Settings 菜单，显示 Document Types 条目"><figcaption>Settings：Global Settings > Document Types</figcaption></figure>
2.  打开要编辑的文档类型对应的 **Edit Layout** 菜单。

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Document Types 页面，每个文档类型下方有 Edit layout 链接"><figcaption>打开文档类型的 Edit layout</figcaption></figure>
3.  选择要应用税码的 **Document Origin**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder，显示 Document Origin 选择器和模板工具栏"><figcaption>Layout Builder：选择 Document Origin</figcaption></figure>
4.  向下滚动到 **Tax Details** 部分。

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder，元素树中显示 Tax Details 分组及其字段"><figcaption>滚动到 Tax Details 分组</figcaption></figure>
5. 展开 **Form Elements** 下拉菜单。
6.  在 **Tax Details** 部分使用 **Horizontal Separator Tool**。将其拖放到税务部分的子部分之间，以便清楚地分隔各部分并减少混淆。

    <figure><img src="../../../.gitbook/assets/TaxCodes_22 (1).png" alt="Layout Builder，Form Elements 下拉菜单已展开"><figcaption>展开 Form Elements</figcaption></figure>
7. 展开 **Form Fields** 下拉菜单。
8.  搜索 **Tax Country**，然后将该字段拖放到相应区域。

    <figure><img src="../../../.gitbook/assets/TaxCodes_23 (2).png" alt="Layout Builder，Tax Country 字段已拖入 Tax Details 区域"><figcaption>将 Tax Country 拖入 Tax Details 区域</figcaption></figure>
9.  搜索 **Tax Code**，然后将该字段拖放到对应区域。

    <figure><img src="../../../.gitbook/assets/TaxCodes_24 (1).png" alt="Layout Builder，Tax Code 字段已放在 Tax Country 下方"><figcaption>将 Tax Code 拖入 Tax Details 区域</figcaption></figure>
10. 保存模板。

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Layout Builder，模板已保存，Tax Details 分组中有两个税务字段"><figcaption>保存的模板及两个税务字段</figcaption></figure>

### 步骤 4：验证配置是否生效

在 DocBits 中上传新文档并选择正确的文档设置后，您现在应该可以选择在步骤 1 的列表中添加的税码。

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="发票的字段验证视图，Tax Country 和 Tax Code 下拉框已填写"><figcaption>字段验证视图中的新下拉框</figcaption></figure>

## 多个税码

### **步骤 1：设置值列表**

1.  前往 **Settings** -> **Document Processing** -> **List of Values**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt="已打开的 Settings 菜单，显示 Document Processing 分组和 List of Values 条目"><figcaption>Settings：Document Processing > List of Values</figcaption></figure>
2.  点击 **New**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="List of Values 页面，显示已有列表和 New 按钮"><figcaption>List of Values 页面及已有列表</figcaption></figure>
3.  创建名为 `Tax_Country` 的列表，然后点击 **Save**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Create New list 对话框，名称已填写为 Tax_Country" width="375"><figcaption>创建列表 Tax_Country</figcaption></figure>
4.  再创建以下三个列表：

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Create New list 对话框，名称已填写为 Tax_Code_Full"><figcaption>创建列表 Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Create New list 对话框，名称已填写为 Tax_Code_Reduced"><figcaption>创建列表 Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Create New list 对话框，名称已填写为 Tax_Code_Free"><figcaption>创建列表 Tax_Code_Free</figcaption></figure></div>
5.  点击其中一个新建的列表以打开它。然后点击 **Add Row** 按钮添加新行。

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="List of Values 页面，打开列表下方有 Add Row 按钮"><figcaption>在打开的列表中添加一行</figcaption></figure>
6.  输入 LN 中相应的所需值，然后点击 **Save** 保存更改。

    * 如果有多个值，可以点击 **Add More Values** 添加。

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Create values 对话框，Name 字段已填写 LN 税码"><figcaption>在 Name 字段中输入 LN 税码</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt="Create values 对话框，通过 Add More Values 添加了值 800"><figcaption>通过 Add More Values 添加第二个值</figcaption></figure></div>

    * **注意：**您可以在 LN 中通过以下路径找到税码：**Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN 的 Tax Codes by Country 会话，显示奥地利及 Tax Code 和 Kind of Tax 列"><figcaption>LN：Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **步骤 2：在 DocBits 中添加字段**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="已打开的 Global Settings 菜单，显示 Document Types 条目"><figcaption>Settings：Global Settings > Document Types</figcaption></figure>
2.  在要添加字段的文档类型对应的菜单中选择 **Fields**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Document Types 页面，每个文档类型下方有 Fields 菜单"><figcaption>打开文档类型的 Fields 菜单</figcaption></figure>
3.  在 **VAT & Amounts** 下，按如下方式创建六个新字段：

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Fields 选项卡，显示 VAT &amp; Amounts 分组和 Create New 按钮"><figcaption>Fields 选项卡：VAT &amp; Amounts 分组</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>名称</strong></td><td><strong>标题</strong></td><td><strong>字段类型</strong></td><td><strong>值</strong></td></tr><tr><td><code>tax_country</code></td><td>税务国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>税务国家/地区（减免）</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>免税国家/地区</td><td>下拉列表</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>税码</td><td>下拉列表</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>减免税码</td><td>下拉列表</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>免税税码</td><td>下拉列表</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt="tax_country 的 Document field details 对话框，字段类型 Dropdown，列表 Tax_Country"><figcaption>字段 tax_country：Dropdown，列表 Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt="tax_country_2 的 Document field details 对话框，标题为 Tax Country Reduced"><figcaption>字段 tax_country_2：Dropdown，列表 Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="tax_country_3 的 Document field details 对话框，标题为 Tax Country Free"><figcaption>字段 tax_country_3：Dropdown，列表 Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt="tax_code_without_country 的 Document field details 对话框，列表 Tax_Code_Full"><figcaption>字段 tax_code_without_country：Dropdown，列表 Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt="tax_code_without_country_2 的 Document field details 对话框，列表 Tax_Code_Reduced"><figcaption>字段 tax_code_without_country_2：Dropdown，列表 Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt="tax_code_without_country_3 的 Document field details 对话框，列表 Tax_Code_Free"><figcaption>字段 tax_code_without_country_3：Dropdown，列表 Tax_Code_Free</figcaption></figure></div>

4.  保存每个字段后，点击 **Save Settings** 应用更改。

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Fields 选项卡，字段列表上方有 Save Settings 按钮"><figcaption>点击 Save Settings 应用新字段</figcaption></figure>

### **步骤 3：编辑布局**

1.  前往 **Settings** -> **Global Settings** -> **Document Types**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="已打开的 Global Settings 菜单，显示 Document Types 条目"><figcaption>Settings：Global Settings > Document Types</figcaption></figure>
2.  打开要编辑的文档类型对应的 **Edit Layout** 菜单。

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Document Types 页面，每个文档类型下方有 Edit layout 链接"><figcaption>打开文档类型的 Edit layout</figcaption></figure>
3.  选择要应用税码的 **Document Origin**。

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder，显示 Document Origin 选择器和模板工具栏"><figcaption>Layout Builder：选择 Document Origin</figcaption></figure>
4.  向下滚动到 **Tax Details** 部分。

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder，元素树中显示 Tax Details 分组及其字段"><figcaption>滚动到 Tax Details 分组</figcaption></figure>
5. 展开 **Form Elements** 下拉菜单。
6.  在 **Tax Details** 部分使用 **Sub Group** 工具。将其拖放到现有字段旁边。

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Layout Builder，Form Elements 下拉菜单中选中 Sub Group 工具"><figcaption>选择 Sub Group 工具</figcaption></figure>
7.  要为子组命名，请点击该子组，并在 **Label** 字段中输入所需名称。

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Layout Builder，现有字段旁已放入一个新的空子分组"><figcaption>将子分组拖到字段旁</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="属性面板，显示新子分组的 Label 字段"><figcaption>在 Label 字段中为子分组命名</figcaption></figure></div>
8.  将与此组对应的字段拖放到 **Sub Group** 字段中。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Layout Builder，税务字段已移入新的子分组"><figcaption>将税务字段移入子分组</figcaption></figure>
9. 展开 **Fields** 下拉菜单。
10. 搜索 **Tax**，然后将相应字段（例如 **Tax Country** 和 **Tax Code**）拖放到对应的子组中。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Layout Builder，子分组中包含 Tax Country 和 Tax Code"><figcaption>子分组中的 Tax Country 和 Tax Code</figcaption></figure>
11. 将步骤 5 到 10 重复两次，直到达到以下状态：

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Layout Builder，三个税务子分组分别对应全额、减额和免税税率"><figcaption>全额、减额和免税的三个子分组</figcaption></figure>
12. 保存模板。

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Layout Builder，多税码模板已保存"><figcaption>保存多税码模板</figcaption></figure>

### 步骤 4：验证配置是否生效以及结果变化

在 DocBits 中上传新文档并选择正确的文档设置后，您可以选择在步骤 1 中添加的税码，并添加在步骤 3 中配置的多个税码。

* 文档将显示三个不同的部分：分别用于完整税额、减免税额和免税额。
* 点击某个部分中的加号按钮会创建副本，以便按选定的税率添加多笔申报。

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="字段验证视图，显示三个独立税务区块以及加号和删除按钮"><figcaption>字段验证视图中的三个税务区块</figcaption></figure>

* 点击移除按钮即可删除部分。

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="字段验证视图，通过加号按钮复制了一个税务区块"><figcaption>使用加号按钮添加另一个区块</figcaption></figure>

* 总金额将按所有部分的金额之和计算。
* 总金额的验证将根据所有税务部分进行调整。
* 只有在视图中添加字段后，才能对新部分应用脚本。

### LN 说明：

在 **LN** 中，USt Position 将根据税码/税务国家（地区）下拉菜单中的位置编号填写。导出时只会发送位置编号。

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="Infor LN 的 Tax Lines by External Invoice 会话，显示税务位置列"><figcaption>LN：Tax Lines by External Invoice</figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="Infor LN 的 Tax Lines by External Invoice 会话，显示位置编号"><figcaption>LN：位置编号作为 USt Position 导出</figcaption></figure>

#### **导出映射**

要将税行关联到成本行：

1. 将 `TaxLine` 添加到 **InvoiceCostFields** 列表。
2. 按照以下示例添加条目：\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="导出映射文件，发票成本字段旁有 ICF_TaxLine 条目"><figcaption>导出映射：ICF_TaxLine = TF_position</figcaption></figure>
