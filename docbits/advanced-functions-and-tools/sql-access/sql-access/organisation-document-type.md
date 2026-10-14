# Organisation document type

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `document_type_id`: internal
* `document_type_key`: internal
* `document_locale`: internal
* `classification_method`: internal
* `is_active`: boolean
* `extraction_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: internal

## Analyse & Beschreibung

```markdown
# Technical Documentation for Table `public.organisation_document_type`

## Introduction

The `public.organisation_document_type` table is designed to manage and store information about various document types associated with organizations. This includes details such as the document type key, locale, classification methods, and the status of the document type (active, deleted, etc.). It appears to serve as a mapping between organizations and the types of documents they utilize or manage, alongside metadata about these documents.

## Column Descriptions

### id
- **Meaning**: Unique identifier for each record in the table.
- **Role**: Primary key.
- **Typical Contents**: A UUID string that uniquely identifies a document type entry.
- **Note**: Essential for distinguishing each record.

### org_id
- **Meaning**: Identifier for the organization related to the document type.
- **Role**: Foreign key, likely referencing an organization table.
- **Typical Contents**: A UUID string.
- **Note**: Connects the document type to a specific organization.

### document_type_id
- **Meaning**: Identifier for the document type.
- **Role**: Foreign key, possibly linked to a document types reference table.
- **Typical Contents**: A UUID string.
- **Note**: Allows mapping to specific document types.

### document_type_key
- **Meaning**: A key or code representing the document type.
- **Role**: Descriptive field for document type classification.
- **Typical Contents**: A string that acts as an identifier or label for the document type.
- **Note**: Used to identify the document type in a human-readable form.

### document_locale
- **Meaning**: Locale or language setting for the document type.
- **Role**: Descriptive field for locale specification.
- **Typical Contents**: A string, often 'auto', indicating automatic determination of locale.
- **Note**: Useful for internationalization and localization purposes.

### classification_method
- **Meaning**: Method used for classifying the document type.
- **Role**: Descriptive field indicating how the document is classified.
- **Typical Contents**: A string, often 'auto', suggesting automatic classification.
- **Note**: Important for understanding the classification process.

### is_active
- **Meaning**: Status indicating if the document type is active.
- **Role**: Boolean status field.
- **Typical Contents**: `True` or `False`.
- **Note**: Determines whether the document type is currently in use.

### extraction_type
- **Meaning**: Type of extraction method used for the document.
- **Role**: Descriptive field for extraction process.
- **Typical Contents**: Strings like 'FIX_COORDINATES', 'FLEX_COORDINATES', or `None`.
- **Note**: Provides insight into how data is extracted from documents.

### created_by
- **Meaning**: Identifier for the user who created the record.
- **Role**: Technical field for auditing purposes.
- **Typical Contents**: An integer representing a user ID.
- **Note**: Useful for tracking changes and accountability.

### created_on
- **Meaning**: Timestamp of when the record was created.
- **Role**: Technical field for auditing purposes.
- **Typical Contents**: A timestamp with time zone.
- **Note**: Important for tracking the creation date and time of the record.

### last_modified_on
- **Meaning**: Timestamp of the last modification to the record.
- **Role**: Technical field for auditing purposes.
- **Typical Contents**: A timestamp with time zone.
- **Note**: Useful for tracking updates and changes to the record.

### is_deleted
- **Meaning**: Status indicating if the record has been marked as deleted.
- **Role**: Boolean status field.
- **Typical Contents**: `True` or `False`.
- **Note**: Helps in implementing soft-delete functionality.

### sub_org_id
- **Meaning**: Identifier for a sub-organization related to the document type.
- **Role**: Possible foreign key, adding hierarchical organization structure.
- **Typical Contents**: A UUID string or `None`.
- **Note**: Provides additional context for organization structure.

```
