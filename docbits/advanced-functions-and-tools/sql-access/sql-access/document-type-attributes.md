# Document type attributes

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_key`: internal
* `sub_doc_type_key`: internal
* `attribute_key`: internal
* `attribute_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: internal

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.document_type_attributes` Table

## Introduction

The `public.document_type_attributes` table appears to be designed for managing attributes related to various document types within an organizational context. This table likely supports configuration or metadata management for different types of documents, such as invoices or delivery notes, by associating specific attributes to each document type.

## Column Descriptions

### id
- **Meaning**: A unique identifier for each record in the table.
- **Role**: Primary key.
- **Typical Contents**: A UUID string that uniquely identifies a row in the table.

### org_id
- **Meaning**: Represents the organization to which the document type attribute belongs.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string referencing an organization.

### doc_type_key
- **Meaning**: The type of document to which the attribute applies (e.g., INVOICE, DELIVERY_NOTE).
- **Role**: Descriptive field.
- **Typical Contents**: A string representing a document type.

### sub_doc_type_key
- **Meaning**: A more specific categorization within the document type, if applicable.
- **Role**: Descriptive field.
- **Typical Contents**: Typically `None`, indicating it may not always be used.

### attribute_key
- **Meaning**: The specific attribute or property key related to the document type.
- **Role**: Descriptive field.
- **Typical Contents**: A string representing an attribute key, such as `SECOND_APPROVAL_BEFORE_EXPORT`.

### attribute_value
- **Meaning**: The value associated with the attribute key for the document type.
- **Role**: Descriptive field.
- **Typical Contents**: A string or numeric value that provides the value of the attribute, e.g., `true`, `123`.

### created_by
- **Meaning**: The identifier of the user who created the record.
- **Role**: Descriptive field.
- **Typical Contents**: An integer representing a user ID.

### created_on
- **Meaning**: The timestamp when the record was created.
- **Role**: Technical field.
- **Typical Contents**: A timestamp with time zone indicating when the record was created.

### last_modified_on
- **Meaning**: The timestamp of the last modification made to the record.
- **Role**: Technical field.
- **Typical Contents**: A timestamp with time zone indicating the last update time.

### is_deleted
- **Meaning**: Indicates whether the record is marked as deleted.
- **Role**: Technical field.
- **Typical Contents**: A boolean value, `false` implying the record is active.

### sub_org_id
- **Meaning**: Represents a sub-organization within the main organization, if applicable.
- **Role**: Foreign key.
- **Typical Contents**: Typically `None`, indicating it may not always be used.
```

This documentation provides a structured overview of the `public.document_type_attributes` table, allowing developers to understand the purpose and usage of each column.
