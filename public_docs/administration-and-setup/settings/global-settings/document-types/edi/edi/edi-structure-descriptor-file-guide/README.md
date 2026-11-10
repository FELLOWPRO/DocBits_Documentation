# EDI Structure Descriptor 文件指南

## 1. 概述

**Structure Descriptor 文件**是一个 **JSON** 文件，用于定义如何把重复的 EDI 段（例如 `N1`–`N4`）分组为结构化输出。它是 EDI 处理的第一步：

* 将相关段作为单个单元进行**准确解析**。
* 为 [Transformation](../edi-transformation-file-guide.md) 及下游系统提供**一致的输出**。

_如需包含段详细信息的完整示例，请参见_ [_Structure Descriptor Example_](edi-structure-descriptor.md)_。_

## 2. 访问与基本编辑

#### **访问该文件**

1. 转到 **Settings** → **Document Types**，并为要配置的文档类型打开 **E-Doc**（例如 _Purchase Order_）。你需要拥有所在组织的管理员权限才能编辑这些文件。

    <!-- dbdc-139-edi-sd-list-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-list-en.png" alt="英文版 Sandbox 的 E-Doc 页面，EDI 格式已展开，STRUCTURE DESCRIPTOR 的 JSON 行列在 TRANSFORMATION、PREVIEW 和 EXTRACTION PATHS 上方"><figcaption>为你的文档类型打开 E-Doc；EDI 格式会列出其配置文件。</figcaption></figure>

2. 展开 **EDI** 格式。其配置文件会集中列出：**STRUCTURE DESCRIPTOR**、**TRANSFORMATION**、**PREVIEW** 和 **EXTRACTION PATHS**。
3. 点击标记为 **JSON** 的 **STRUCTURE DESCRIPTOR** 行，将其打开。

#### **草稿管理**

左侧列显示文件的 **Version** 列表。标记为 **Active** 的版本就是 DocBits 当前使用的版本。

* **创建草稿**：点击当前活动版本旁边的 ✏️ 铅笔图标开始编辑。活动文件本身无法直接编辑。
* **删除草稿**：使用 🗑️ 垃圾桶图标删除未使用的草稿。
* **激活更改**：点击草稿上的 ✅ 对勾图标，以批准并发布你的更改。
  * <mark style="color:red;">**Note**</mark>：激活新版本会**自动停用**先前的版本。

<!-- dbdc-139-edi-sd-detail-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-detail-en.png" alt="英文版 Sandbox 的 Structure Descriptor JSON 编辑器，左侧版本列表显示版本 1 标记为 Active，并有一个用于创建草稿的铅笔图标"><figcaption>Structure Descriptor 文件及其版本列表；铅笔图标用于创建可编辑的草稿。</figcaption></figure>

## 3. Preview 功能（预览解析输出）

借助 **Preview 功能**，你可以在激活任何更改之前，测试上传的 EDI 文件在当前显示的 Structure Descriptor 下会如何被解析。

#### 使用方法

* 通过标准上传流程上传一个 EDI 文件。
* 复制所上传文件的 **Document ID**。
* 按上文所述打开 **Structure Descriptor** 文件。
* 点击右上角的 **Preview**，打开测试面板。

    <div align="left"><!-- dbdc-139-edi-sd-preview-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-preview-en.png" alt="英文版 Sandbox 的 Structure Descriptor 页面，Preview 测试面板已打开，显示 Document Id 输入表单字段和 Test 按钮" width="560"><figcaption>测试面板：输入 Document ID 并按下 Test。</figcaption></figure></div>

* 在该表单字段中输入 **Document ID**，然后按 **Test**。
* 生成的**结构化输出**会显示在编辑器旁边。

这对于实时调试映射、验证结构分组尤为有用。你需要一份自己格式的具有代表性的 EDI 文档；显示的结果取决于所上传的文件。

## 4. 视频演示

此文件类型的视频指南位于 [Videos page.](../edi-videos.md)\
可以用它来跟随操作设置、编辑和预览的步骤。

这些视图展示的是已有的配置和版本。具体设置因文档类型和格式而异。请在激活前于草稿中验证更改。
