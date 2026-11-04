# Tabelle public.document\_import\_log

## Spalten

* `id`: integer
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `original_filename`: internal
* `filename`: internal
* `imported_on`: internal
* `source_type`: internal
* `source`: internal
* `success`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `import_id`: text
* `extra_data`: text
* `doc_id`: internal
* `email_connection_id`: integer
* `subject`: internal
* `body`: text
* `sender`: internal
* `error_resp`: internal
* `source_received_on`: timestamp with time zone

## Analyse & Beschreibung

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
