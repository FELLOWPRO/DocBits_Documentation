# FTP 导入配置

## 列

* `id`：内部字段
* `org_id`：组织 ID
* `sub_org_id`：内部字段
* `server_url`：内部字段
* `username`：内部字段
* `password`：内部字段
* `is_active`：布尔值
* `created_by`：整数
* `created_on`：带时区的时间戳
* `last_modified_on`：带时区的时间戳
* `is_deleted`：布尔值
* `deleted_on`：带时区的时间戳
* `port`：整数
* `default_directory`：内部字段
* `ftp_type`：内部字段
* `token`：内部字段
* `file_name_matching_patterns`：内部字段
* `last_mtime`：内部字段
* `auth_failed_count`：整数
* `auth_message`：文本
* `ignore_certificate`：布尔值
* `move_after_import`：布尔值
* `destination_directory`：内部字段
* `import_directory`：内部字段
* `include_subfolder_content`：布尔值

## 分析与说明

```markdown
# FTP Import Configurations Table Documentation

## Introduction

The `public.ftp_import_configurations` table is designed to store configuration details for FTP import processes. This table includes information necessary for connecting to FTP servers, managing authentication, and handling file imports. It supports both FTP and SFTP protocols and includes fields for FTP server details, authentication credentials, and operational settings, such as whether to move files after import and whether to include subfolder content.

## Column Descriptions

### id
- **Meaning**: Unique identifier for each FTP import configuration record.
- **Role**: Primary key.
- **Typical Contents**: UUID format, e.g., `9862d8c6-bb61-4373-9616-d5f8c125eeb8`.

### org_id
- **Meaning**: Identifier for the organization associated with this configuration.
- **Role**: Foreign key.
- **Typical Contents**: UUID format.

### sub_org_id
- **Meaning**: Identifier for a sub-organization, if applicable.
- **Role**: Foreign key.
- **Typical Contents**: UUID format or `null` if not applicable.

### server_url
- **Meaning**: The URL or IP address of the FTP server.
- **Role**: Descriptive field.
- **Typical Contents**: Domain name or IP address, e.g., `sftp.it.doxee.com`.

### username
- **Meaning**: Username used for authentication with the FTP server.
- **Role**: Descriptive field.
- **Typical Contents**: Plain text username.

### password
- **Meaning**: Password used for authentication with the FTP server.
- **Role**: Descriptive field.
- **Typical Contents**: Encrypted password string.

### is_active
- **Meaning**: Indicates if the configuration is currently active.
- **Role**: Status flag.
- **Typical Contents**: `True` or `False`.

### created_by
- **Meaning**: Identifier for the user who created the configuration.
- **Role**: Foreign key.
- **Typical Contents**: Integer representing user ID.

### created_on
- **Meaning**: Timestamp when the configuration was created.
- **Role**: Audit field.
- **Typical Contents**: Datetime with timezone information.

### last_modified_on
- **Meaning**: Timestamp of the last modification of the configuration.
- **Role**: Audit field.
- **Typical Contents**: Datetime with timezone information.

### is_deleted
- **Meaning**: Indicates if the configuration has been marked as deleted.
- **Role**: Status flag.
- **Typical Contents**: `True` or `False`.

### deleted_on
- **Meaning**: Timestamp when the configuration was marked as deleted.
- **Role**: Audit field.
- **Typical Contents**: Datetime with timezone information or a default date for non-deleted records.

### port
- **Meaning**: Port number used to connect to the FTP server.
- **Role**: Descriptive field.
- **Typical Contents**: Integer, e.g., `22` for SFTP.

### default_directory
- **Meaning**: The default directory path on the FTP server.
- **Role**: Descriptive field.
- **Typical Contents**: Directory path string.

### ftp_type
- **Meaning**: Type of FTP protocol used (e.g., FTP, SFTP).
- **Role**: Descriptive field.
- **Typical Contents**: `FTP` or `SFTP`.

### token
- **Meaning**: Security token for additional authentication or identification.
- **Role**: Descriptive field.
- **Typical Contents**: Encrypted or encoded string.

### file_name_matching_patterns
- **Meaning**: Patterns used to match file names for import.
- **Role**: Descriptive field.
- **Typical Contents**: Pattern strings or `null`.

### last_mtime
- **Meaning**: Last modification time of files, used for filtering imports.
- **Role**: Descriptive field.
- **Typical Contents**: String representing a timestamp or `null`.

### auth_failed_count
- **Meaning**: Counter for failed authentication attempts.
- **Role**: Descriptive field.
- **Typical Contents**: Integer, e.g., `0` or `5`.

### auth_message
- **Meaning**: Message describing the result of the last authentication attempt.
- **Role**: Descriptive field.
- **Typical Contents**: Text message or `null`.

### ignore_certificate
- **Meaning**: Indicates if SSL certificate validation should be ignored.
- **Role**: Status flag.
- **Typical Contents**: `True` or `False`.

### move_after_import
- **Meaning**: Indicates if files should be moved after import is complete.
- **Role**: Status flag.
- **Typical Contents**: `True` or `False`.

### destination_directory
- **Meaning**: Directory path where files should be moved after import.
- **Role**: Descriptive field.
- **Typical Contents**: Directory path string or `null`.

### import_directory
- **Meaning**: Directory path from which files are imported.
- **Role**: Descriptive field.
- **Typical Contents**: Directory path string or `null`.

### include_subfolder_content
- **Meaning**: Indicates if content from subfolders should be included in the import.
- **Role**: Status flag.
- **Typical Contents**: `True` or `False`.
```

本文档根据给定的数据和列名，全面说明 `public.ftp_import_configurations` 表中每一列的用途、作用和典型内容。
