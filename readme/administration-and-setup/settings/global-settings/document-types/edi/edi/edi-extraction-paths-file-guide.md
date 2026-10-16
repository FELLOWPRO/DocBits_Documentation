# EDI 提取路径文件指南

## 1. 概述

**提取路径文件**定义如何从**结构化 XML**中提取数据，并将其填入界面中的特定文档字段和表格。\
它将**字段 ID**映射到 **XPath 表达式**，通过计算这些表达式从 XML 中提取值，并填入相应的文档字段。\
此文件对于确保提取的数据在字段验证和后续处理中正确显示起着关键作用。

## 2. 用途和功能

* 使用 XPath 表达式，将每个文档字段和表格列映射到结构化 XML 中的特定位置。
* 确保将正确的值填入 `order_number`、`supplier_name` 和 `total_amount` 等字段。
* 同时支持**单个字段**（通过 `fields` 对象）和**表格**（通过包含行路径和列映射的 `tables` 数组）。
* 精确控制如何从 XML 中检索数据，包括使用 `sum()` 等 XPath 函数。

字段映射示例：

```json
"order_number": "//PURCHASE_ORDER/PURCHASE_ORDER/text()"
```

## 3. 访问和基本编辑

#### **访问文件：**

1.  转到**设置** → **文档类型** → _\[您的文档（例如，采购订单）]_ → **E-Doc**。\\

    <figure><img src="../../../../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
2. 在 **E-Doc** 选项卡下，选择您的格式（例如，**EDI**）。
3.  点击**提取路径**以查看或编辑文件。\\

    <figure><img src="../../../../../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

#### **草稿管理：**

* **创建草稿：**点击 ✏️ 铅笔图标。
* **删除草稿：**使用 🗑️ 垃圾桶图标删除未使用的草稿。
* **激活更改：**点击 ✅ 勾选图标发布一个版本。
  * <mark style="color:red;">**注意**</mark>：激活新版本会**自动停用**之前的版本。

## 4. 编辑器和语法

提取路径文件使用 **JSON** 编写，包含两个主要部分：

* **fields**：一个字典，其中每个键都是字段 ID，每个值都是用于定义数据提取方式的 XPath 表达式。
* **tables**：一个表格定义列表，包含：
  * `name`：表格的 ID。
  * `row_path`：用于标识表格每一行的 XPath。
  * `columns`：列映射列表（`name`、`path`）。

您还可以使用 XPath 函数（例如，`sum()`）和表达式，从重复元素中动态计算值。

```
jsonCopyEdit"total_net_amount": "sum(//PURCHASE_ORDER/ORDER_LINES/ORDER_LINE/SUB_TOTAL)"
```

## 5. 预览功能（评估提取结果）

**预览功能**可让您通过实际上传的文档模拟提取路径的运行情况。

**使用方法：**

* 通过标准上传流程上传一个 EDI 文件。
* 复制**文档 ID**。
* 前往**提取路径**界面。
* 打开**预览功能**。\
  \
  ![](<../../../../../../.gitbook/assets/image (21).png>)
* 输入文档 ID，然后点击**测试**。
* 结果将显示根据已配置的路径填入各字段和表格的内容。

此功能对于验证 XPath 表达式的定义是否正确、是否能提取预期值至关重要，您可以在激活草稿之前完成检查。

<figure><img src="../../../../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

## 6. 视频操作指南

此文件类型的视频指南可在[视频页面](edi-videos.md)查看。\
您可以按照视频步骤完成设置、编辑和预览。
