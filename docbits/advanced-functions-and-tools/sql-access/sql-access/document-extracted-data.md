# Document extracted data

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `field_name`: internal
* `field_value`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `field_type`: internal

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.document_extracted_data` Table

## Introduction

The `public.document_extracted_data` table is designed to store extracted data from various documents, likely for the purpose of document processing and analysis. Each entry in the table corresponds to a specific field extracted from a document, such as an invoice, and includes metadata about the extraction process. The table facilitates tracking and managing document data by associating it with organizations and specific documents.

## Column Descriptions

### id
- **Meaning**: A unique identifier for each extracted data entry.
- **Role**: Primary key.
- **Typical Contents**: A UUID formatted string uniquely identifying the extracted data record.

### org_id
- **Meaning**: Identifier for the organization associated with the document data.
- **Role**: Foreign key.
- **Typical Contents**: A UUID formatted string representing the organization.

### doc_id
- **Meaning**: Identifier for the document from which data has been extracted.
- **Role**: Foreign key.
- **Typical Contents**: A UUID formatted string representing the document.

### field_name
- **Meaning**: The name of the field extracted from the document.
- **Role**: Descriptive field.
- **Typical Contents**: Strings like 'invoice_id', 'invoice_date', etc., indicating the type of data extracted.

### field_value
- **Meaning**: The value associated with the extracted field.
- **Role**: Descriptive field.
- **Typical Contents**: Strings representing various data types like invoice numbers, dates, or amounts.

### created_by
- **Meaning**: The identifier of the user or process that created the data entry.
- **Role**: Technical field.
- **Typical Contents**: Integer representing a user ID or process ID.

### created_on
- **Meaning**: The timestamp when the data entry was created.
- **Role**: Technical field.
- **Typical Contents**: Timestamp with timezone data indicating the creation date and time.

### last_modified_on
- **Meaning**: The timestamp of the last modification made to the data entry.
- **Role**: Technical field.
- **Typical Contents**: Timestamp with timezone data indicating the last modification date and time (can be null if never modified).

### is_deleted
- **Meaning**: A flag indicating whether the data entry has been marked as deleted.
- **Role**: Technical field.
- **Typical Contents**: Boolean value, with `False` indicating active entries and `True` indicating deleted entries.

### field_type
- **Meaning**: The type of data stored in the `field_value` column.
- **Role**: Descriptive field.
- **Typical Contents**: Strings like 'date', 'AMOUNT', or null if the type is not specified.

This structured data model allows for efficient storage and retrieval of document-related data, supporting a range of applications from invoice processing to compliance management.
```
