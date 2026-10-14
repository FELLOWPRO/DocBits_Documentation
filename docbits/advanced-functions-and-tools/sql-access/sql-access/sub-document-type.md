# Sub document type

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_key`: internal
* `sub_doc_type_key`: internal
* `name`: internal
* `title`: internal
* `translation_key`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analyse & Beschreibung

```markdown
# Table `public.sub_document_type`

## Introduction

The `sub_document_type` table is designed to store detailed information about various sub-document types within an organization. This includes unique identifiers, organizational associations, descriptive names, and metadata related to the creation and modification of these sub-document types. The table also maintains soft deletion status for records.

## Column Descriptions

### id
- **Meaning**: This column stores the unique identifier for each sub-document type.
- **Role**: Primary Key.
- **Typical Contents**: A UUID string that uniquely identifies a sub-document type record (e.g., `'c2cc2d62-e4be-491b-a43e-c4123dff5aa6'`).

### org_id
- **Meaning**: This column indicates the organization to which the sub-document type belongs.
- **Role**: Foreign Key.
- **Typical Contents**: A UUID string that references an organization (e.g., `'23f3d697-7411-4c95-981d-faf089d266be'`).

### doc_type_key
- **Meaning**: Represents the document type key that is associated with the sub-document type.
- **Role**: Foreign Key (implied by naming convention).
- **Typical Contents**: A string key that links to a broader document type (e.g., `'TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### sub_doc_type_key
- **Meaning**: Denotes a specific key for the sub-document type within a document category.
- **Role**: Unique identifier for sub-document type within the scope of a document type.
- **Typical Contents**: A string key that uniquely identifies a sub-document type (e.g., `'TEST_SUB_TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### name
- **Meaning**: Stores a short name or code for the sub-document type.
- **Role**: Descriptive.
- **Typical Contents**: A succinct identifier or code (e.g., `'TEST_SUB_TEST'`).

### title
- **Meaning**: Contains a human-readable title for the sub-document type.
- **Role**: Descriptive.
- **Typical Contents**: A descriptive title for user interfaces or reports (e.g., `'Test Sub Test'`).

### translation_key
- **Meaning**: Key used for internationalization and localization to translate the sub-document type name.
- **Role**: Technical.
- **Typical Contents**: A string used in translation files (e.g., `'test_sub_test'`).

### created_by
- **Meaning**: Identifies the user who created the sub-document type entry.
- **Role**: Technical.
- **Typical Contents**: An integer representing the user ID (e.g., `8`).

### created_on
- **Meaning**: Timestamp indicating when the sub-document type was created.
- **Role**: Technical.
- **Typical Contents**: A timestamp with timezone (e.g., `2022-12-13 08:34:13.932893+00:00`).

### last_modified_on
- **Meaning**: Timestamp indicating when the sub-document type was last modified.
- **Role**: Technical.
- **Typical Contents**: A timestamp with timezone, possibly `None` if never modified after creation.

### is_deleted
- **Meaning**: Boolean flag indicating whether the sub-document type has been soft deleted.
- **Role**: Technical.
- **Typical Contents**: `True` or `False` indicating deletion status (e.g., `False`).
```
