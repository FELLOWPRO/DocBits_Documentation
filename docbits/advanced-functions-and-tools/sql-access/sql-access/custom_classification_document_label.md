# Custom\_classification\_document\_label

## Table `public.custom_classification_document_label`

### Spalten

* `id`: integer
* `org_id`: ID to organisation
* `doc_id`: internal
* `label_id`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technical Documentation for `public.custom_classification_document_label` Table

### Introduction

The `public.custom_classification_document_label` table is designed to manage and store associations between documents and their respective labels within an organization. This table facilitates the categorization and retrieval of documents based on custom labels, providing a structured way to manage document classification for various organizational needs.

### Column Descriptions

#### id

* **Meaning**: This column serves as the unique identifier for each record in the table.
* **Role**: Primary Key
* **Typical Contents**: An integer value that uniquely identifies each row.
* **Note**: Each entry in the table has a distinct `id` to ensure data integrity and support efficient referencing.

#### org\_id

* **Meaning**: Represents the organization to which the document-label association belongs.
* **Role**: Foreign Key
* **Typical Contents**: A character string, likely a UUID, that uniquely identifies an organization.
* **Note**: Ensures the association of documents and labels is scoped to the correct organizational context.

#### doc\_id

* **Meaning**: Identifies the document being labeled.
* **Role**: Foreign Key
* **Typical Contents**: A character string, likely a UUID, that uniquely identifies a document.
* **Note**: Allows for the linkage of specific documents to labels, enabling document categorization.

#### label\_id

* **Meaning**: Refers to the label applied to the document.
* **Role**: Foreign Key
* **Typical Contents**: An integer that references a label from a separate labels table.
* **Note**: Facilitates the association between documents and their respective labels.

#### created\_by

* **Meaning**: Identifies the user who created the record.
* **Role**: Foreign Key (potentially to a users table)
* **Typical Contents**: An integer representing the user ID.
* **Note**: Tracks the origin of each document-label association for auditing and accountability.

#### created\_on

* **Meaning**: Indicates when the record was created.
* **Role**: Technical Field
* **Typical Contents**: A timestamp with time zone information.
* **Note**: Provides a temporal context for when the document-label relationship was established.

#### last\_modified\_on

* **Meaning**: Records the last modification timestamp of the record.
* **Role**: Technical Field
* **Typical Contents**: A timestamp with time zone information, can be `None` if never modified.
* **Note**: Useful for tracking the history of changes to the document-label associations.

#### is\_deleted

* **Meaning**: Flags if the record has been marked as deleted.
* **Role**: Technical Field
* **Typical Contents**: A boolean value (`True` or `False`).
* **Note**: Supports soft deletion practices, allowing logical removal of data without physical deletion from the database.
