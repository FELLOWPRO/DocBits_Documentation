# Auto test document

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `filename`: internal

## Analyse & Beschreibung

```markdown
# Table Documentation: `public.auto_test_document`

## Introduction

The `public.auto_test_document` table is designed to store metadata and extraction results from document processing within an organization. The table captures information about documents, their types, and the data extracted from them. It includes fields for document identification, processing metadata, and status flags, which are essential for managing document workflows and ensuring data integrity.

## Column Descriptions

### id
- **Meaning**: Unique identifier for each document entry in the table.
- **Role**: Primary key.
- **Typical Contents**: UUID string.
- **Note**: Serves as a unique identifier for records, ensuring each entry is distinct.

### org_id
- **Meaning**: Identifier for the organization associated with the document.
- **Role**: Foreign key.
- **Typical Contents**: UUID string.
- **Note**: Links the document to a specific organization within the system.

### doc_id
- **Meaning**: Identifier of the document being processed.
- **Role**: Foreign key.
- **Typical Contents**: UUID string.
- **Note**: Used to associate extracted data with the original document.

### doc_type
- **Meaning**: Type or category of the document.
- **Role**: Descriptive field.
- **Typical Contents**: String such as "MEDI_ORDER".
- **Note**: Helps in categorizing documents for processing and analysis.

### extracted_data
- **Meaning**: JSON structure containing detailed data extracted from the document.
- **Role**: Data field.
- **Typical Contents**: JSON text with fields, values, and extraction metadata.
- **Note**: Stores the results of the document's data extraction process.

### created_by
- **Meaning**: Identifier of the user who created the document record.
- **Role**: Descriptive field.
- **Typical Contents**: Integer representing a user ID.
- **Note**: Tracks which user initiated the document's entry into the system.

### created_on
- **Meaning**: Timestamp indicating when the document record was created.
- **Role**: Technical field.
- **Typical Contents**: Date and time with timezone information.
- **Note**: Useful for auditing and tracking the document's lifecycle.

### last_modified_on
- **Meaning**: Timestamp indicating the last modification made to the document record.
- **Role**: Technical field.
- **Typical Contents**: Date and time with timezone information.
- **Note**: Helps track changes and updates to the document record.

### is_deleted
- **Meaning**: Flag indicating if the document record has been marked as deleted.
- **Role**: Status field.
- **Typical Contents**: Boolean value.
- **Note**: Facilitates soft deletion of records, allowing for recovery if needed.

### filename
- **Meaning**: Name of the file associated with the document.
- **Role**: Descriptive field.
- **Typical Contents**: String, e.g., "7.pdf".
- **Note**: Provides a reference to the physical file associated with the document entry.

```
