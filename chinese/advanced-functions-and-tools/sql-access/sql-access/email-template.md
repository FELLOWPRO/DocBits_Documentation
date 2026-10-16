# 电子邮件模板

## 列

* `id`：内部字段
* `org_id`：组织 ID
* `name`：内部字段
* `email_type`：内部字段
* `value`：文本
* `created_by`：整数
* `created_on`：带时区的时间戳
* `last_modified_on`：带时区的时间戳
* `is_deleted`：布尔值
* `deleted_on`：带时区的时间戳
* `subject`：内部字段
* `last_modified_by`：内部字段
* `deleted_by`：内部字段
* `doc_type`：文档类型

## 分析与说明

```markdown
# Technical Documentation for `public.email_template` Table

## Introduction

The `public.email_template` table is designed to store email templates used within the system. These templates are associated with different organizations and are likely used to send standardized email communications. The table contains metadata about the templates, including creation and modification details, and it also tracks whether a template has been deleted.

## Column Descriptions

### id
- **Meaning**: Unique identifier for each email template.
- **Role**: Primary key.
- **Typical Contents**: A UUID string such as `da34c6ed-e659-4392-91ea-3c89f9602198`.
- **Note**: This serves as the main identifier for the template record.

### org_id
- **Meaning**: Identifier for the organization associated with the email template.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string.
- **Note**: Links the template to a specific organization.

### name
- **Meaning**: The name of the email template.
- **Role**: Descriptive field.
- **Typical Contents**: Descriptive text like `Supplier Magic Link Email`.
- **Note**: Used to identify the template purpose.

### email_type
- **Meaning**: Type or category of the email template.
- **Role**: Descriptive field.
- **Typical Contents**: Strings such as `supplier_invite`.
- **Note**: Indicates the context or usage of the template.

### value
- **Meaning**: The content of the email template, typically in HTML format.
- **Role**: Content field.
- **Typical Contents**: HTML string containing email layout and content.
- **Note**: This is the actual template used in emails.

### created_by
- **Meaning**: Identifier for the user who created the template.
- **Role**: Metadata field.
- **Typical Contents**: An integer representing a user ID.
- **Note**: Tracks who created the template.

### created_on
- **Meaning**: Timestamp for when the template was created.
- **Role**: Metadata field.
- **Typical Contents**: A timestamp like `2024-07-18 13:29:59 UTC`.
- **Note**: Records the creation date and time.

### last_modified_on
- **Meaning**: Timestamp for the last modification of the template.
- **Role**: Metadata field.
- **Typical Contents**: A timestamp.
- **Note**: Tracks the most recent update to the template.

### is_deleted
- **Meaning**: Indicates whether the template is marked as deleted.
- **Role**: Technical field.
- **Typical Contents**: Boolean value, `True` or `False`.
- **Note**: Used to soft-delete the template.

### deleted_on
- **Meaning**: Timestamp for when the template was marked as deleted.
- **Role**: Metadata field.
- **Typical Contents**: A timestamp or `None` if not deleted.
- **Note**: Records when the template was deleted.

### subject
- **Meaning**: The subject line of the email template.
- **Role**: Content field.
- **Typical Contents**: Text like `Welcome to Testing Ruiz Foods Supplier Portal. Let's help you get set up`.
- **Note**: Used as the email subject when the template is sent.

### last_modified_by
- **Meaning**: Identifier for the user who last modified the template.
- **Role**: Metadata field.
- **Typical Contents**: A user identifier.
- **Note**: Tracks who last modified the template.

### deleted_by
- **Meaning**: Identifier for the user who marked the template as deleted.
- **Role**: Metadata field.
- **Typical Contents**: A user identifier.
- **Note**: Records who deleted the template.

### doc_type
- **Meaning**: Type or format of the document related to the template.
- **Role**: Descriptive field.
- **Typical Contents**: Strings indicating the document type.
- **Note**: Could relate to the format or category of the email content.
```
