# 文档

## 列

* `id`：内部字段
* `org_id`：组织 ID
* `batch_id`：内部字段
* `doc_path`：内部字段
* `doc_type`：文档类型
* `status`：内部字段
* `message`：文本
* `export_attempts`：整数
* `last_attempted_on`：带时区的时间戳
* `next_attempt_on`：带时区的时间戳
* `assigned_to`：整数
* `created_by`：整数
* `created_on`：带时区的时间戳
* `last_modified_on`：带时区的时间戳
* `is_deleted`：布尔值
* `task_id`：内部字段
* `filename`：内部字段
* `assigned_on`：带时区的时间戳
* `pages`：整数
* `auto_processed`：布尔值
* `exception_info`：文本
* `doc_language`：语言
* `is_trimmed`：布尔值
* `doc_origin`：文档来源
* `doc_locale`：文档区域设置
* `is_doc2landing_doc`：布尔值
* `extraction_time`：双精度浮点数
* `export_time`：双精度浮点数
* `po_all_matched`：布尔值
* `restart_allowed`：布尔值
* `table_version`：内部字段
* `force_ocr`：布尔值
* `locked_by`：整数
* `locked_on`：带时区的时间戳
* `lock_renewed_on`：带时区的时间戳
* `lock_key`：内部字段
* `last_saved_by`：整数
* `last_saved_on`：带时区的时间戳
* `document_version`：整数
* `lock_session_key`：内部字段
* `sub_org_id`：内部字段
* `doc_source`：内部字段
* `sub_doc_type`：内部字段
* `assigned_to_group`：内部字段
* `status_changed_on`：带时区的时间戳
* `improve_quality`：布尔值
* `priority`：整数
* `metadata_field`：json
* `doc_classification_label`：内部字段
* `doc_start_page`：整数
* `doc_classification_class`：内部字段
* `celery_task_token`：内部字段
* `celery_task_attempt`：整数
* `celery_task_priority`：整数
* `has_zugferd`：布尔值
* `has_peppol`：布尔值
* `timestamp_for_validation`：带时区的时间戳
* `exception_details`：文本
* `has_annotated_version`：布尔值
* `po_match_status`：内部字段
* `tr_ocr_extracted_data`：文本
* `pending_workflow_execution`：布尔值
* `extracted_document_id`：内部字段
* `extracted_supplier_id`：内部字段
* `classification_manually_corrected`：布尔值
* `supplier_as_org_id`：内部字段
* `extracted_data_basic`：jsonb
* `celery_task_queue`：内部字段
* `extracted_data`：jsonb
* `extracted_data_jsonb`：jsonb
* `warnings`：jsonb

## 分析与说明

```markdown
# `public.documents` 表技术文档

## 简介

`public.documents` 表用于存储和管理组织内文档处理相关的元数据和处理信息，包括跟踪文档状态、处理尝试次数、语言及其他管理详情。该表的结构支持文档分类、处理工作流和用户分配，是文档管理系统的重要组成部分。

## 字段说明

### id
- **含义**：每份文档的唯一标识符。
- **作用**：主键。
- **典型内容**：表示文档的 UUID 字符串。

### org_id
- **含义**：与文档关联的组织标识符。
- **作用**：外键。
- **典型内容**：表示组织的 UUID 字符串。

### batch_id
- **含义**：文档处理所在批次的标识符。
- **作用**：外键。
- **典型内容**：表示批次的 UUID 字符串。

### doc_path
- **含义**：文档的存储路径。
- **作用**：技术字段。
- **典型内容**：文档文件的路径，例如 `documents/{id}/{id}.pdf`。

### doc_type
- **含义**：所存储文档的类型（例如发票）。
- **作用**：文档分类。
- **典型内容**：例如 `INVOICE` 这样的字符串。

### status
- **含义**：文档当前的处理状态。
- **作用**：工作流指示字段。
- **典型内容**：表示状态的字符串，例如 `ready_for_validation`。

### message
- **含义**：有关文档处理状态或错误的信息。
- **作用**：描述性字段。
- **典型内容**：描述文档处理相关错误或消息的文本。

### export_attempts
- **含义**：针对该文档尝试导出的次数。
- **作用**：处理跟踪。
- **典型内容**：导出尝试次数的整数计数。

### last_attempted_on
- **含义**：最近一次尝试处理或导出文档的时间戳。
- **作用**：时间戳字段。
- **典型内容**：带时区的日期和时间。

### next_attempt_on
- **含义**：计划进行下一次文档处理或导出的时间戳。
- **作用**：调度字段。
- **典型内容**：带时区的日期和时间。

### assigned_to
- **含义**：分配给该文档的用户标识符。
- **作用**：外键。
- **典型内容**：表示用户 ID 的整数。

### created_by
- **含义**：创建或上传文档的用户标识符。
- **作用**：外键。
- **典型内容**：表示用户 ID 的整数。

### created_on
- **含义**：文档创建或上传的时间戳。
- **作用**：时间戳字段。
- **典型内容**：带时区的日期和时间。

### last_modified_on
- **含义**：文档记录最近一次修改的时间戳。
- **作用**：时间戳字段。
- **典型内容**：带时区的日期和时间。

### is_deleted
- **含义**：指示文档是否已标记为删除。
- **作用**：逻辑删除标记。
- **典型内容**：布尔值（True 或 False）。

### task_id
- **含义**：与文档处理相关任务的标识符。
- **作用**：外键。
- **典型内容**：表示任务的 UUID 字符串。

### filename
- **含义**：文档的原始文件名。
- **作用**：描述性字段。
- **典型内容**：文件名，例如 `document.pdf`。

### assigned_on
- **含义**：文档分配给用户的时间戳。
- **作用**：时间戳字段。
- **典型内容**：带时区的日期和时间。

### pages
- **含义**：文档的页数。
- **作用**：描述性字段。
- **典型内容**：表示页数的整数。

### auto_processed
- **含义**：指示文档是否经过自动处理。
- **作用**：处理状态标记。
- **典型内容**：布尔值（True 或 False）。

### exception_info
- **含义**：处理期间遇到的任何异常信息。
- **作用**：描述性字段。
- **典型内容**：描述处理异常的文本。

### doc_language
- **含义**：文档内容的语言。
- **作用**：语言分类。
- **典型内容**：ISO 语言代码，例如 `en`、`de`。

### is_trimmed
- **含义**：指示文档是否经过裁切或剪裁。
- **作用**：文档修改标记。
- **典型内容**：布尔值（True 或 False）。

### doc_origin
- **含义**：文档的来源，可能表示国家或源系统。
- **作用**：描述性字段。
- **典型内容**：国家代码或来源标识符，例如 `DE`。

### doc_locale
- **含义**：文档的区域设置，表示语言和地区。
- **作用**：区域设置分类。
- **典型内容**：区域设置字符串，例如 `de_DE.ISO8859-1`。

### is_doc2landing_doc
- **含义**：指示文档是否与特定处理工作流（Doc2Landing）相关。
- **作用**：工作流标记。
- **典型内容**：布尔值（True 或 False）。

### extraction_time
- **含义**：从文档中提取数据所用的时间。
- **作用**：性能指标。
- **典型内容**：表示提取耗时的双精度值。

### export_time
- **含义**：导出文档所用的时间。
- **作用**：性能指标。
- **典型内容**：表示导出耗时的双精度值。

### po_all_matched
- **含义**：指示与文档相关的所有采购订单是否均已匹配。
- **作用**：匹配状态标记。
- **典型内容**：布尔值（True 或 False）。

### restart_allowed
- **含义**：指示是否允许重新启动文档处理。
- **作用**：工作流控制标记。
- **典型内容**：布尔值（True 或 False）。

### table_version
- **含义**：该文档使用的表结构版本。
- **作用**：版本控制。
- **典型内容**：表示版本的字符串，例如 `v3`。

### force_ocr
- **含义**：指示是否强制对文档执行 OCR 处理。
- **作用**：处理控制标记。
- **典型内容**：布尔值（True 或 False）。

### locked_by
- **含义**：锁定文档以进行编辑的用户标识符。
- **作用**：外键。
- **典型内容**：表示用户 ID 的整数。

### locked_on
- **含义**：文档被锁定以进行编辑的时间戳。
- **作用**：时间戳字段。
- **典型内容**：带时区的日期和时间。

### lock_renewed_on
- **含义**：文档锁最近一次续期的时间戳。
- **作用**：时间戳字段。
- **典型内容**：带时区的日期和时间。

### lock_key
- **含义**：与文档锁关联的密钥。
- **作用**：锁控制。
- **典型内容**：表示锁密钥的字符串。

### last_saved_by
- **含义**：最近一次保存文档的用户标识符。
- **作用**：外键。
- **典型内容**：表示用户 ID 的整数。

### last_saved_on
- **含义**：文档最近一次保存的时间戳。
- **作用**：时间戳字段。
- **典型内容**：带时区的日期和时间。

### document_version
- **含义**：文档的版本号。
- **作用**：版本跟踪。
- **典型内容**：表示文档版本的整数。

### lock_session_key
- **含义**：与文档锁关联的会话密钥。
- **作用**：锁控制。
- **典型内容**：表示会话密钥的字符串。

### sub_org_id
- **含义**：与文档关联的子组织标识符。
- **作用**：外键。
- **典型内容**：表示子组织的 UUID 字符串。

### doc_source
- **含义**：文档的源系统或来源。
- **作用**：描述性字段。
- **典型内容**：表示来源的字符串，例如 `doc2app`。

### sub_doc_type
- **含义**：文档的子类型分类。
- **作用**：文档分类。
- **典型内容**：表示子类型的字符串。

### assigned_to_group
- **含义**：文档所分配到的组的标识符。
- **作用**：分配跟踪。
- **典型内容**：表示组的 UUID 字符串。

### status_changed_on
- **含义**：文档状态最近一次变更的时间戳。
- **作用**：时间戳字段。
- **典型内容**：带时区的日期和时间。

### improve_quality
- **含义**：指示是否对文档应用了质量改进流程。
- **作用**：质量控制标记。
- **典型内容**：布尔值（True 或 False）。

### priority
- **含义**：文档的处理优先级。
- **作用**：工作流控制。
- **典型内容**：表示优先级的整数。

### metadata_field
- **含义**：包含文档相关元数据的 JSON 字段。
- **作用**：元数据存储。
- **典型内容**：包含多个元数据字段的 JSON 结构。

### doc_classification_label
- **含义**：表示文档分类的标签。
- **作用**：分类标签。
- **典型内容**：表示分类的字符串，例如 `INVOICE`。

### doc_start_page
- **含义**：文档内容开始的页码。
- **作用**：描述性字段。
- **典型内容**：表示起始页的整数。

### doc_classification_class
- **含义**：表示文档详细分类的类别。
- **作用**：分类详情。
- **典型内容**：表示分类类别的字符串。

### celery_task_token
- **含义**：用于跟踪与文档相关的 Celery 任务的令牌。
- **作用**：任务跟踪。
- **典型内容**：表示任务令牌的字符串。

### celery_task_attempt
- **含义**：Celery 任务的尝试次数。
- **作用**：任务跟踪。
- **典型内容**：任务尝试次数的整数计数。

### celery_task_priority
- **含义**：Celery 任务的优先级。
- **作用**：任务控制。
- **典型内容**：表示任务优先级的整数。

### has_zugferd
- **含义**：指示文档是否采用 ZUGFeRD 格式。
- **作用**：格式指示字段。
- **典型内容**：布尔值（True 或 False）。

### has_peppol
- **含义**：指示文档是否采用 PEPPOL 格式。
- **作用**：格式指示字段。
- **典型内容**：布尔值（True 或 False）。

### timestamp_for_validation
- **含义**：文档经过验证的时间戳。
- **作用**：验证跟踪。
- **典型内容**：带时区的日期和时间。

### exception_details
- **含义**：处理期间异常的详细信息。
- **作用**：描述性字段。
- **典型内容**：包含异常详情的文本。

### has_annotated_version
- **含义**：指示文档是否有注释版本。
- **作用**：版本指示字段。
- **典型内容**：布尔值（True 或 False）。

### po_match_status
- **含义**：采购订单匹配状态。
- **作用**：匹配状态指示字段。
- **典型内容**：表示匹配状态的字符串。

### tr_ocr_extracted_data
- **含义**：通过 OCR 从文档中提取的数据。
- **作用**：数据存储。
- **典型内容**：包含提取数据的文本。

### pending_workflow_execution
- **含义**：指示是否有待执行的工作流。
- **作用**：工作流状态标记。
- **典型内容**：布尔值（True 或 False）。

### extracted_document_id
- **含义**：提取文档的标识符。
- **作用**：提取跟踪。
- **典型内容**：表示提取文档的 UUID 字符串。

### extracted_supplier_id
- **含义**：提取供应商的标识符。
- **作用**：提取跟踪。
- **典型内容**：表示供应商的 UUID 字符串。

### classification_manually_corrected
- **含义**：指示文档分类是否经过人工更正。
- **作用**：分类状态标记。
- **典型内容**：布尔值（True 或 False）。

### supplier_as_org_id
- **含义**：作为组织处理的供应商的标识符。
- **作用**：外键。
- **典型内容**：表示供应商组织的 UUID 字符串。

### extracted_data_basic
- **含义**：以 JSONB 格式存储的基础提取数据。
- **作用**：数据存储。
- **典型内容**：包含提取数据字段的 JSONB 结构。

### celery_task_queue
- **含义**：Celery 任务队列的名称。
- **作用**：任务管理。
- **典型内容**：表示队列名称的字符串。

### extracted_data
- **含义**：以 JSONB 格式存储的文档提取数据。
- **作用**：数据存储。
- **典型内容**：包含提取数据字段的 JSONB 结构。

### extracted_data_jsonb
- **含义**：包含详细提取数据的 JSONB 字段。
- **作用**：数据存储。
- **典型内容**：包含提取数据字段的 JSONB 结构。

### warnings
- **含义**：以 JSONB 格式存储的文档处理相关警告。
- **作用**：警告存储。
- **典型内容**：包含警告消息的 JSONB 结构。
```
