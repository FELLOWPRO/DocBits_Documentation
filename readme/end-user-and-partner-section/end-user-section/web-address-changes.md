# Web 地址变更

您用于访问 DocBits 页面的网址（URL）已经过整理并统一。本页将介绍发生了哪些变化、为什么旧链接仍然有效，以及如何通过新地址查找页面。

## 发生了哪些变化

DocBits 中的网址现在遵循一种清晰的模式：先写您正在处理的对象，再写它的视图。例如，文档的验证页面现在是：

```
/documents/<document-id>/validation
```

而不是旧地址：

```
/field_validation_v1/<document-id>
```

随着时间推移，一些页面出现了多个不同版本和地址。例如，审批页面曾分别使用不同地址对应首次审批、第二次审批，以及各自的旧版本。现在这些页面共用一个地址，DocBits 会根据您所在的组织自动显示正确的版本。您无需再了解或猜测哪个版本适用于您。

现在的网址也统一使用小写单词，并且只用连字符分隔，不再混用下划线、大写字母和缩写。

## 旧链接仍然有效

您无需立即更改任何内容。书签、电子邮件中保存的链接以及保存在其他位置的链接都会像以前一样正常使用。打开旧地址时，DocBits 会自动将您转到新地址，包括保留原链接中的筛选条件或选项。

转到新地址后，浏览器地址栏会显示新地址。这是正常现象，表示转向成功。我们建议您逐步更新已保存的书签，使其直接指向新地址，这样就无需经过额外的转向步骤。不过没有截止期限：旧地址会继续有效。

## 查找页面

如果您不确定某个页面的新地址，或者想直接跳转到某个页面，可以通过以下三种方式查找：

* **站点地图。** [站点地图](sitemap.md)页面按区域列出 DocBits 中的所有页面，并提供搜索框和筛选器。您可以从侧边栏打开站点地图，也可以在全局快速搜索中选择**查看所有结果**。
* **全局快速搜索。** 在 DocBits 的任意位置，Mac 上按 <kbd>Cmd</kbd> + <kbd>K</kbd>，或 Windows 上按 <kbd>Ctrl</kbd> + <kbd>K</kbd>，然后输入要查找的内容名称。详情请参阅[全局快速搜索](global-quick-search.md)。
* **页面未找到界面。** 如果您只输入或粘贴地址的开头部分（例如 `/documents` 或 `/analytics`），而没有输入其余部分，DocBits 会显示一个页面未找到界面，并列出该地址下的所有页面。它相当于这组页面的索引，并且提供与全局快速搜索相同的搜索框，您也可以直接在此处搜索。

## 旧地址和新地址

下表按区域列出所有发生变更的地址。如果多个旧地址现在都指向同一个新地址，则每个旧地址都会单独列出。仅供开发人员使用的地址（例如调试或演示页面）不会列出，因为它们不会影响日常使用。

表中的占位符代表实际值：

* `<document-id>` — 文档 ID
* `<task-id>` — 任务 ID
* `<workflow-id>` — 工作流 ID
* `<document-type>` — 文档类型，例如发票或采购订单
* `<file-name>` — 文件名
* `<order-number>` / `<sales-order-id>` — 采购订单或销售订单编号
* `<organisation-id>` — 组织 ID
* `<layout-type>` — 布局类型
* `<supplier-id>` — 供应商 ID
* `<page>` — 页码

### 文档

| 旧地址 | 新地址 |
|---|---|
| `/document/<document-id>` | `/documents/<document-id>` |
| `/field_validation_v1/<document-id>` | `/documents/<document-id>/validation` |
| `/field_validation/<document-id>` | `/documents/<document-id>/validation` |
| `/medi_order_v3/<document-id>` | `/documents/<document-id>/validation` |
| `/ready_for_approval_v3/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-approval-v2/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-approval/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval-v3/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval-v2/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval/<document-id>` | `/documents/<document-id>/approval` |
| `/in_review/<document-id>` | `/documents/<document-id>/review` |
| `/in-review-v2/<document-id>` | `/documents/<document-id>/review` |
| `/rejected/<document-id>` | `/documents/<document-id>/rejected` |
| `/summary/<document-id>` | `/documents/<document-id>/summary` |
| `/tbl_ext_v3/<document-id>` | `/documents/<document-id>/table-extraction` |
| `/tbl_training/<document-id>` | `/documents/<document-id>/table-training` |
| `/table_train_v3` | `/table-training` |
| `/doc_flow/<document-id>` | `/documents/<document-id>/flow` |
| `/document_pdf/<file-name>/<document-id>` | `/documents/<document-id>/pdf/<file-name>` |
| `/document_error/<document-id>` | `/documents/<document-id>/error` |
| `/document_classifiy/<document-id>` | `/documents/<document-id>/classify` |
| `/accounting/<document-id>` | `/documents/<document-id>/accounting` |
| `/quote-details/<document-id>` | `/documents/<document-id>/quote` |
| `/vertex-details/<document-id>` | `/documents/<document-id>/vertex` |
| `/po-matching/<document-id>` | `/documents/<document-id>/po-matching` |
| `/po-matching-v3/<document-id>` | `/documents/<document-id>/po-matching-v3` |
| `/ocr-document/<document-id>/<page>` | `/documents/<document-id>/ocr/<page>` |
| `/fields_sep_comp_v3/<document-id>` | `/documents/<document-id>/window/medi-fields` |
| `/simple_fields_comp/<document-id>` | `/documents/<document-id>/window/fields` |
| `/show_pdf/<document-id>` | `/documents/<document-id>/window/pdf` |

### 任务

| 旧地址 | 新地址 |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### 工作流

| 旧地址 | 新地址 |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### 订单和发票

| 旧地址 | 新地址 |
|---|---|
| `/purchase-order` | `/supplier/purchase-orders` |
| `/purchase-order-detail/<order-number>` | `/supplier/purchase-orders/<order-number>` |
| `/sales_order_detail/<sales-order-id>` | `/sales-orders/<sales-order-id>` |
| `/asn_shipment` | `/shipments/asn` |
| `/asn_shipment/dashboard` | `/shipments/asn` |
| `/shipment-order` | `/shipments/orders` |
| `/invoice/dashboard` | `/invoices` |
| `/invoice/details/<document-id>` | `/invoices/<document-id>` |
| `/accounting_range` | `/accounting/range` |

### 分析和搜索

| 旧地址 | 新地址 |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### 共享链接

| 旧地址 | 新地址 |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### 账户和登录

| 旧地址 | 新地址 |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### 布局

| 旧地址 | 新地址 |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
