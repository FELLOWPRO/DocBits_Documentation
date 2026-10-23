# 使用主数据配置模糊数据

### **概述**

每种文档类型都有自己的默认配置，必须分别进行设置。本示例介绍 **发票** 的设置流程，但同样适用于所有文档类型。

### 配置模糊数据的路径：

设置 → 全局设置 → 文档类型 → 发票 → 字段 → 主数据设置 → 查找主数据

<div align="center"><figure><img src="../../../.gitbook/assets/fuzzy_data_config_1.png" alt="字段设置页面，其中的Master Data Settings部分显示Lookup Master Data和LOV Master Data" width="454"><figcaption></figcaption></figure></div>

### **默认查找组**

发票有 **四个默认查找组**：

1. **公司数据**
2. **采购订单抬头**
3. **供应商**
4. **税码**

<figure><img src="../../../.gitbook/assets/fuzzy_data_config_2.png" alt="Lookup Master Data页面，列出Company Data、Purchase Order Header、Supplier、Taxcode和Test组并带有Default标签" width="563"><figcaption></figcaption></figure>

每个组都包含特定字段。点击一个组即可将其**展开**并查看字段。默认查找组带有 **"Default" 标签**。

### **查找配置状态**

* **已激活的配置**带有 **"Activated" 标签**。
* **已停用的配置**带有 **"Deactivated" 标签**。

### **前提条件：导入主数据**

要使模糊数据正常工作，必须导入相关的**主数据**。如果没有主数据，系统就没有可用的参考数据。以下介绍如何导入主数据：

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

### **管理查找组**

每个查找组默认均为**已激活**，但可以点击三个点进行修改：

* **Deactivate** → 停用一个组。_(仅适用于已激活的组)_
* **Activate** → 激活一个组。_(仅适用于已停用的组)_
* **Duplicate** → 创建副本，修改副本不会影响原始组。
* **View** → 显示该组所属的**文档类型**以及所用的**查找表**等信息。_(仅适用于默认组)_
* **Edit** → 适用于**非默认**组，可修改组的详细信息。
* **Delete** → 完全移除该组。_(仅适用于非默认组)_

### **创建新的查找配置**

创建查找配置有**两种方式**：

1. **复制现有查找配置**



    <figure><img src="../../../.gitbook/assets/fuzzy_data_config_3.png" alt="Purchase Order Header的Lookup Master Data菜单已展开，显示Deactivate、Duplicate和View选项"><figcaption></figcaption></figure>

    * 这会复制现有组的所有信息和字段。
    * 你只需提供一个**新名称**。
2. **从头创建查找配置**\


    <figure><img src="../../../.gitbook/assets/fuzzy_data_config_4.png" alt="Lookup Master Data页面，Company Data和Purchase Order Header分组已展开"><figcaption></figcaption></figure>

    * 点击 **"Create Lookup Configuration"**。
    * 填写所需详细信息：
      * **Configuration Name**
      * **Lookup Table**（要使用的主数据表）
      * **Conflict Handler**（选择一项：Best Score、Return None、Return First）
      * **Context Type** → 定义应用查找的位置：
        * **Header** → 用于文档级字段，例如发票编号、日期等。
        * **Line** → 用于发票表格中的行项目字段。如果选择 **Line**，用户还必须指定要使用的**发票表格**。
      * **Match All** → 启用后，供应商必须匹配所有已使用字段；停用后，匹配一个字段即可。请参阅[DocBits 如何选择一个供应商](#how-docbits-picks-one-supplier)。

### **管理查找组中的字段**

每个组都包含可**添加、移除、编辑或查看**的字段，具体取决于这些字段是默认字段还是自定义字段。

#### **默认字段**

* 带有 **"Default" 标签**。\


    <div align="left"><figure><img src="../../../.gitbook/assets/fuzzy_data_config_5.png" alt="查找组字段行，其中字段Supplier带有Default标记和一个查看图标" width="251"><figcaption></figcaption></figure></div>
* **只能查看**，不能编辑或删除。

#### **非默认字段**

* 点击三个点并选择 **Edit** 或 **Remove**，即可编辑或删除。

#### **添加新字段**

<mark style="color:red;">**注意：**</mark>你可以在默认查找配置中创建字段。

要在组中添加新字段：

1. 点击相关组中的 **"Create"**。\


    <figure><img src="../../../.gitbook/assets/fuzzy_data_config_6.png" alt="展开的Purchase Order Header组，包含Lookup Field、Validation Field、Parent Field、Searchable、Auto Trigger和Actions列"><figcaption></figcaption></figure>
2. 提供以下详细信息：
   * **Lookup Field** → 主数据查找表中的列名。
   * **Validation Field** → 对应的 DocBits 字段。
   * **Parent Field** →&#x20;
   * **Search Operator** → 选择一项：
     * Smart
     * Contains
     * Exact
     * Starts with
     * Ends with
   * **复选框：**
     * **Auto Trigger** → 启用后，该字段会在提取期间自动触发查找流程。也就是说，只要相关 DocBits 字段有值，系统就会**自动**填充其余字段。
     * **Searchable** → 将此字段添加到**自动**供应商搜索中，**并且**使其可作为手动搜索的**模糊数据**字段（验证界面中的蓝色图标）。请参阅[DocBits 如何选择一个供应商](#how-docbits-picks-one-supplier)。

### **DocBits 如何选择一个供应商** <a id="how-docbits-picks-one-supplier"></a>

收到文档后，DocBits 会在主数据中搜索供应商。三个设置决定搜索结果。本节将通过示例逐步说明这些设置。

#### **第 1 步 — 搜索会使用哪些字段**

只有同时满足以下两点，DocBits 才会使用某个字段进行搜索：

* 在查找配置中，该字段已勾选 **Searchable** 或 **Auto Trigger**；并且
* 文档中的该字段有值。

字段中的值如何产生并不重要。经过训练的字段、由 AI 填充的字段和用户手动输入的值，都会以相同方式处理。

{% hint style="warning" %}
**Searchable 有两种作用。**它会在验证界面中显示蓝色搜索图标，**并且**将该字段添加到自动供应商搜索中。如果你只想手动搜索某个字段，请不要勾选它。
{% endhint %}

#### **第 2 步 — 执行一次搜索，而不是每个字段各搜索一次**

DocBits **不会**分别搜索每个字段，而是根据所有已使用字段执行**一次**搜索。**Match All** 决定这些字段如何组合：

* **关闭 Match All**（默认）→“查找匹配税号**或**供应商名称的所有供应商”。这样得到的列表会**更长**。
* **开启 Match All** →“查找匹配税号**且**供应商名称的所有供应商”。这样得到的列表会**更短**。

请注意，搜索运算符 **Smart** 和 **Contains** 会查找文本的一部分。名称 "Meier" 也会找到 "Meier Bau GmbH" 和 "Meier & Sons Ltd"。因此，供应商名称通常会匹配多个供应商。

#### **第 3 步 — 供应商列表中有多个结果时会怎样**

**Conflict Handler** 决定如何处理：

* **Best Score** → 选择匹配字段最多的供应商。不会将供应商留空。
* **Return None** → 将供应商留空，由用户选择。
* **Return First** → 选择列表中的第一个供应商。

#### **示例**

以下所有示例中，文档都包含税号和供应商名称，并且两个字段均已勾选 **Searchable**。

<table><thead><tr><th width="150">税号匹配</th><th width="150">名称匹配</th><th width="150">关闭 Match All + Return None</th><th width="150">开启 Match All + Return None</th><th width="150">关闭 Match All + Best Score</th></tr></thead><tbody>
<tr><td>仅 A</td><td>A 和 B</td><td>空</td><td><strong>A</strong></td><td><strong>A</strong></td></tr>
<tr><td>A 和 B</td><td>仅 B</td><td>空</td><td><strong>B</strong></td><td><strong>B</strong></td></tr>
<tr><td>A、B 和 C</td><td>C、D 和 E</td><td>空</td><td><strong>C</strong></td><td><strong>C</strong></td></tr>
<tr><td>A、B 和 C</td><td>B、C 和 D</td><td>空</td><td>空</td><td>B 或 C，不可靠</td></tr>
<tr><td>仅 A</td><td>无</td><td><strong>A</strong></td><td>空</td><td><strong>A</strong></td></tr>
</tbody></table>

表格的读法：

* **第 1 至 3 行**是常见情况：一个字段匹配唯一结果，另一个字段则不唯一。关闭 **Match All** 时，列表中会有多个供应商，**Return None** 会将字段留空。开启 **Match All** 后，只保留同时匹配两个字段的供应商，并找到该供应商。
* **第 4 行**没有唯一匹配的供应商。将字段留空是正确的。**Best Score** 仍会选择其中一个，但可能选错供应商。
* **第 5 行**展示了开启 **Match All** 的风险。请参阅下方警告。

{% hint style="warning" %}
**Match All 可能会漏掉供应商。**开启 **Match All** 后，每个已使用字段都必须匹配。如果某个字段中的值在主数据中不存在——例如拼写错误、旧公司名称或从页面识别出的值——整个搜索将不会返回任何结果，因此找不到供应商，即使仅凭税号本可以找到正确的供应商。
{% endhint %}

#### **之前能识别某个供应商，现在却无法识别**

几乎总是因为有另一个字段开始产生值。请按以下顺序检查：

1. 打开文档。查找组中的哪个字段现在有值，而之前为空？
2. 打开查找配置。该字段是否勾选了 **Searchable** 或 **Auto Trigger**？如果是，它现在会参与搜索，并使结果列表变长。
3. 选择以下三种处理方式之一：
   * **该字段不应参与搜索** → 取消勾选该字段的 **Searchable** 和 **Auto Trigger**。该字段会继续保留文档中的值，用户仍然可以看到它。这是改动最小的方式。
   * **该字段应参与搜索** → 开启 **Match All**，但请先阅读上方警告。
   * **无论如何都要选出一个供应商** → 将 **Conflict Handler** 设置为 **Best Score**。请接受它可能会选错供应商，而不是将字段留空。

### **最后一步：将字段添加到布局**

配置模糊数据字段后，**请务必使用 Layout Builder 将它们添加到布局中**。如果字段未添加到布局，就无法使用。

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}
