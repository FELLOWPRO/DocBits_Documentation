# EDI 预览文件指南

## 1. 概述

**Preview File（预览文件）**定义了如何将结构化 XML 数据渲染为易于阅读、类似 PDF 的格式。它结合使用 **HTML 和 CSS** 进行视觉呈现，并通过 **XSLT `select` 语句**动态插入来自 Custom XML 的数据。\
此预览会在**字段验证**期间显示，也会随文档一起导出到 **IDM**。

## 2. 用途和功能

* 将机器可读的 Custom XML 转换为经过视觉排版的预览（PDF）。
* 便于用户查看和验证提取的数据。
* 确保文档中的关键字段（如标题、表格、总计等）以一致的方式呈现。
* 使用 **HTML + CSS** 构建布局和设计，并使用 **XSLT** 将数据绑定到布局中。

## 3. 访问和基本编辑

#### **访问文件：**

1. 进入 **Settings（设置）** → **Document Type（文档类型）** → _\[Your Document (e.g., Purchase Order)]_ → **E-Doc**。\\

    <figure><img src="../../../../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
2. 在 **E-Doc** 选项卡下，选择所需格式（例如 **EDI**）。
3. 点击 **Preview（预览）**以查看或编辑文件。\\

    <figure><img src="../../../../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

#### **草稿管理：**

* **创建草稿：**点击 ✏️ 铅笔图标。
* **删除草稿：**使用 🗑️ 垃圾桶图标删除不再使用的草稿。
* **激活更改：**点击 ✅ 勾选图标以发布一个版本。
  * <mark style="color:red;">**注意**</mark>：激活新版本会**自动停用**之前的版本。

## 4. HTML/XSLT/CSS 编辑器

**Preview File（预览文件）**在专用编辑器中编辑，该编辑器支持 HTML、XSLT 和 CSS。

* **HTML** 定义输出文档的结构（例如表格、div、布局）。
* **CSS** 控制样式（例如字体、间距、颜色、对齐方式）。
*   **XSLT `select` 语句**用于从 Custom XML 动态填充字段，例如：

    ```xml
    <xsl:value-of select="/PURCHASE_ORDER/PURCHASE_ORDER_NUMBER/text()" />
    ```
* 你还可以使用 **XSLT 逻辑**（`<xsl:if>`、`<xsl:for-each>` 等）来处理条件显示或遍历行项目。

## 5. 预览功能（渲染输出）

预览功能可用于测试和验证当前 Preview File 如何渲染 EDI 文档。

#### **使用方法：**

* 通过标准上传流程上传 EDI 文件。
* 复制所上传文件的 **Document ID（文档 ID）**。
* 前往 **Preview（预览）**界面。
* 打开 **Preview Function（预览功能）**。\
  \
  ![](<../../../../../../.gitbook/assets/image (21).png>)
* 输入 Document ID，然后点击 **Test（测试）**。
* 系统将使用当前 HTML/CSS/XSLT 设置显示渲染后的类 PDF 预览。

此功能对于调试数据绑定、改进布局，以及确保文档准确且便于用户阅读，并能供下游系统（如 **IDM**）使用至关重要。

<figure><img src="../../../../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

## 6. 视频演示

此文件类型的视频指南可在[视频页面](edi-videos.md)中查看。\
可跟随视频了解设置、编辑和预览的操作流程。
