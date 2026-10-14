# Document type

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `document_key`: internal
* `document_name`: internal
* `title`: internal
* `translation_key`: internal
* `extraction_type`: internal
* `document_type_category`: internal
* `has_table`: boolean
* `sort_order`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analyse & Beschreibung

```markdown
# Table: public.document_type

## Introduction
The `public.document_type` table is designed to store information related to various types of documents within an organization. It includes identifiers and metadata for document categorization, management, and processing, such as document keys, names, titles, translation keys, and other attributes that facilitate document handling and retrieval. The table also tracks the creation and modification of these entries, supporting both active and deleted states.

## Column Descriptions

### id
- **Meaning**: A unique identifier for each document type entry.
- **Role**: Primary Key.
- **Typical Contents**: A UUID string that uniquely identifies a document type entry.

### org_id
- **Meaning**: Identifier for the organization to which the document type belongs.
- **Role**: Foreign Key.
- **Typical Contents**: A UUID string referencing an organization.

### document_key
- **Meaning**: A unique key for identifying the document type, potentially used in document storage or processing systems.
- **Role**: Identifier.
- **Typical Contents**: A string that combines document type information with the organization ID.

### document_name
- **Meaning**: The internal name for the document type.
- **Role**: Descriptive Field.
- **Typical Contents**: An uppercase string representing the document type name.

### title
- **Meaning**: The display title of the document type for user interfaces.
- **Role**: Descriptive Field.
- **Typical Contents**: A string in title case that is human-readable and descriptive of the document type.

### translation_key
- **Meaning**: A key used for localizing the document title or name into different languages.
- **Role**: Internationalization Support.
- **Typical Contents**: A lowercase string that serves as a reference for translation systems.

### extraction_type
- **Meaning**: Indicates the method or process by which data is extracted from the document.
- **Role**: Metadata Field.
- **Typical Contents**: Currently not populated in the example data.

### document_type_category
- **Meaning**: Categorizes the document type into broader categories or classifications.
- **Role**: Categorization Field.
- **Typical Contents**: Currently not populated in the example data.

### has_table
- **Meaning**: Indicates whether the document type involves tabular data.
- **Role**: Metadata Field.
- **Typical Contents**: Boolean value (`True` or `False`) indicating the presence of tabular data.

### sort_order
- **Meaning**: Defines the order in which document types are sorted or displayed.
- **Role**: Sorting Field.
- **Typical Contents**: An integer representing the sequence for sorting.

### created_by
- **Meaning**: Identifier for the user who created the document type entry.
- **Role**: Metadata Field.
- **Typical Contents**: An integer referencing a user ID.

### created_on
- **Meaning**: Timestamp indicating when the document type entry was created.
- **Role**: Audit Field.
- **Typical Contents**: Date and time with timezone information.

### last_modified_on
- **Meaning**: Timestamp indicating the last modification date of the document type entry.
- **Role**: Audit Field.
- **Typical Contents**: Date and time with timezone information, `None` if never modified.

### is_deleted
- **Meaning**: Indicates whether the document type entry is marked as deleted.
- **Role**: Status Field.
- **Typical Contents**: Boolean value (`True` or `False`) indicating the deletion status.
```
