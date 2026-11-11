# 全文搜索设置

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="沙盒中的全文搜索设置，显示一个说明该模块为必需的对话框，以及 Go to Modules 和 Enable Now 按钮"><figcaption><p>当全文搜索被禁用时，此对话框说明后续步骤。</p></figcaption></figure>

全文搜索设置用于配置 DocBits 索引哪些内容，以及如何让这些内容在文档、ERP 主数据和模板中可搜索。在启用 **Fulltext Search module** 之前，设置页面会显示要求对话框——有关面向用户的查询语言，请参阅 [Fulltext Search](../document-processing/module/fulltext-search.md)。

## 前提条件

必须在 **Settings → Module → Dashboards & Analytics → Full text search** 中激活 Fulltext Search 模块。如果未启用该模块，对话框会提供三个操作:

* **Help (?)** — 在更改任何设置之前，在新标签页中打开全文搜索文档。
* **Go to Modules** — 打开 Dashboards & Analytics 模块设置以检查配置。
* **Enable Now** — 打开订阅对话框。在启用模块之前，请检查并确认该对话框；仅点击此按钮不会启用它。

模块激活后，设置页面本身才可用。

## 页面布局

设置页面分为三个标签页: **Documents**、**ERP** 和 **Templates**。每个标签页限定全文搜索可索引的一种不同内容类型。

### Documents 标签页

Documents 标签页涵盖与索引已处理文档相关的所有内容:

* **Indexing statistics** — 已索引和待处理文档的总数，按需刷新。
* **Vector preferences** — 三个组织级开关，用于控制文档是否在文本索引之外同时运行向量索引。向量索引为 `vector:` 查询模式和 "Find Similar" 功能提供支持。
* **Reindex actions** — 启动完整或增量重新索引。重新索引运行期间，您可以看到实时进度（每分钟文档数、预计剩余时间）、当前流状态以及最近一次失败（如有）。
* **Sync diagnostics** — 当索引似乎与底层文档存储不同步时，按需运行诊断。

<mark>重新索引是非破坏性的——在新索引重建期间，现有搜索继续工作。</mark>

### ERP 标签页

ERP 标签页控制 ERP 主数据的索引——供应商、客户、物料及类似实体。每个实体都有自己的开关:

* **Indexing** — 为该实体建立文本索引，使其可从仪表板中搜索。
* **Vector** — 为该实体建立向量索引，使其可通过语义查询进行匹配。

使用列表顶部的 **Toggle all** 操作一次性为所有实体应用相同的开启或关闭状态。索引在后台启动；每行上的指示器显示其是否正在进行。

### Templates 标签页

Templates 标签页列出全文索引已知的模板版本。重新部署后，使用此视图确认所依赖的模板版本是否存在于索引中。

## 索引内容

启用并完成配置后，全文搜索让用户可以:

* 搜索所有文档内容（不仅是元数据字段）。
* 按上传文件中包含的文本查找文档。
* 使用高级搜索运算符进行精确查询。
* 直接从仪表板访问搜索结果。
* 在该内容类型启用向量索引时使用语义搜索（`vector:` 前缀）。

有关完整查询语言参考（包括范围查询、智能筛选器和 AI 搜索模式），请参阅 [Fulltext Search](../document-processing/module/fulltext-search.md) 模块页面。
