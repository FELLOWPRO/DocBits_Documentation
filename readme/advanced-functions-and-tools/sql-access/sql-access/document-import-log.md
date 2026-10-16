# 文档导入日志

## 列

* `id`：整数
* `org_id`：组织 ID
* `sub_org_id`：内部字段
* `original_filename`：内部字段
* `filename`：内部字段
* `imported_on`：内部字段
* `source_type`：内部字段
* `source`：内部字段
* `success`：布尔值
* `created_by`：整数
* `created_on`：带时区的时间戳
* `last_modified_on`：带时区的时间戳
* `is_deleted`：布尔值
* `import_id`：文本
* `extra_data`：文本
* `doc_id`：内部字段
* `email_connection_id`：整数
* `subject`：内部字段
* `body`：文本
* `sender`：内部字段
* `error_resp`：内部字段
* `source_received_on`：带时区的时间戳

## 分析与说明

```markdown
# Technical Documentation for `public.document_import_log` Table

## Introduction

The `public.document_import_log` table is designed to log the details of document imports into the system. It captures information about each document, including its origin, import status, and related metadata. This table is essential for tracking document import activities and diagnosing any issues that may arise during the import process.

## Column Descriptions

### id
- **Meaning**: A unique identifier for each import log entry.
- **Role**: Primary Key
- **Typical Contents**: Sequential integer values that uniquely identify each record.

### org_id
- **Meaning**: The identifier for the organization associated with the import.
- **Role**: Foreign Key
- **Typical Contents**: UUID or similar unique string identifier representing the organization.

### sub_org_id
- **Meaning**: The identifier for a sub-organization or department within the main organization.
- **Role**: Foreign Key
- **Typical Contents**: UUID or similar unique string identifier; may be `None` if not applicable.

### original_filename
- **Meaning**: The original name of the document file as it was uploaded.
- **Role**: Descriptive Field
- **Typical Contents**: String representing the filename, e.g., `anton_invoice-1.pdf`.

### filename
- **Meaning**: The name of the document file after it has been processed or stored in the system.
- **Role**: Descriptive Field
- **Typical Contents**: String representing the filename, often identical to `original_filename`.

### imported_on
- **Meaning**: The date and time when the document was imported.
- **Role**: Descriptive Field
- **Typical Contents**: ISO 8601 formatted timestamp.

### source_type
- **Meaning**: The type of source from which the document was imported.
- **Role**: Descriptive Field
- **Typical Contents**: String, e.g., `EMAIL`, indicating the source type.

### source
- **Meaning**: Detailed information about the source of the import.
- **Role**: Descriptive Field
- **Typical Contents**: String detailing the source, e.g., `Email:O365:demo@fellow-digital.de:Tini Test`.

### success
- **Meaning**: Indicates whether the import was successful.
- **Role**: Status Field
- **Typical Contents**: Boolean value (`True` or `False`).

### created_by
- **Meaning**: The identifier of the user who initiated the import.
- **Role**: Foreign Key
- **Typical Contents**: Integer representing user ID.

### created_on
- **Meaning**: The date and time when the import log entry was created.
- **Role**: Technical Field
- **Typical Contents**: Timestamp with timezone.

### last_modified_on
- **Meaning**: The date and time when the import log entry was last modified.
- **Role**: Technical Field
- **Typical Contents**: Timestamp with timezone; may be `None` if not modified.

### is_deleted
- **Meaning**: Indicates whether the import log entry has been marked as deleted.
- **Role**: Status Field
- **Typical Contents**: Boolean value (`True` or `False`).

### import_id
- **Meaning**: A unique identifier for the import process.
- **Role**: Technical Field
- **Typical Contents**: String or text representing a unique process ID.

### extra_data
- **Meaning**: Additional metadata related to the import.
- **Role**: Descriptive Field
- **Typical Contents**: JSON string containing extra data, such as date, sender, subject, and count.

### doc_id
- **Meaning**: The identifier for the document.
- **Role**: Foreign Key
- **Typical Contents**: UUID or similar unique string identifier; may be `None`.

### email_connection_id
- **Meaning**: The identifier for the email connection used in the import.
- **Role**: Foreign Key
- **Typical Contents**: Integer representing email connection ID; may be `None`.

### subject
- **Meaning**: The subject line of the email from which the document was imported.
- **Role**: Descriptive Field
- **Typical Contents**: String representing the email subject.

### body
- **Meaning**: The body content of the email from which the document was imported.
- **Role**: Descriptive Field
- **Typical Contents**: Text containing the email body content; may be `None`.

### sender
- **Meaning**: The email address of the sender of the document.
- **Role**: Descriptive Field
- **Typical Contents**: String containing the sender's email address.

### error_resp
- **Meaning**: Error response or message if the import failed.
- **Role**: Status Field
- **Typical Contents**: String containing error details; may be `None`.

### source_received_on
- **Meaning**: The date and time when the document was received from the source.
- **Role**: Descriptive Field
- **Typical Contents**: Timestamp with timezone.

This documentation provides a detailed overview of the `public.document_import_log` table and its columns, which are essential for understanding and managing document imports within the system.
```
