# Electronic document extraction attributes

## Table `public.electronic_document_extraction_attributes`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_key`: internal
* `sub_doc_type_key`: internal
* `electronic_document_type`: internal
* `attribute_name`: internal
* `attribute_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse & Beschreibung

## Technical Documentation for `public.electronic_document_extraction_attributes`

### Introduction

The `public.electronic_document_extraction_attributes` table appears to manage attributes related to electronic document extraction. This involves storing various characteristics and metadata about electronic document types, their processing methods, and associated organizations. The table seems to support functionalities like document type identification, transformations, previews, and structure descriptions which are essential for handling electronic documents effectively.

### Column Descriptions

#### id

* **Meaning**: A unique identifier for each record in the table.
* **Role**: Primary key.
* **Typical Contents**: A UUID string that uniquely identifies each document extraction attribute entry.
* **Note**: This serves as the unique reference for each row.

#### org\_id

* **Meaning**: Identifier for the organization related to the document attributes.
* **Role**: Foreign key.
* **Typical Contents**: A UUID string that links to the associated organization.
* **Note**: This connects the document extraction attributes to a specific organization.

#### doc\_type\_key

* **Meaning**: A key representing the type of document.
* **Role**: Identifier for categorizing documents.
* **Typical Contents**: A string that indicates the document type, such as 'INVOICE' or 'ORDER\_CONFIRMATION'.
* **Note**: Used to determine the category of the document.

#### sub\_doc\_type\_key

* **Meaning**: Represents a sub-category of the main document type.
* **Role**: Identifier for further classification.
* **Typical Contents**: Null or specific sub-type string.
* **Note**: Useful for further granularity in document classification.

#### electronic\_document\_type

* **Meaning**: The format or standard of the electronic document.
* **Role**: Descriptive field for document format.
* **Typical Contents**: Strings like 'EDI' or 'FACTURX'.
* **Note**: Indicates the standard or format of the document.

#### attribute\_name

* **Meaning**: The name of the attribute related to the document extraction process.
* **Role**: Descriptive field.
* **Typical Contents**: Strings like 'PREVIEW' or 'TRANSFORMATION'.
* **Note**: Describes the specific attribute related to the document handling.

#### attribute\_type

* **Meaning**: The type of the attribute related to the document extraction.
* **Role**: Descriptive field.
* **Typical Contents**: Strings such as 'XSLT' or 'JSON'.
* **Note**: Specifies the data format or method used for the attribute.

#### created\_by

* **Meaning**: ID of the user who created the record.
* **Role**: Foreign key.
* **Typical Contents**: Integer that represents a user ID.
* **Note**: Tracks who initially created the record.

#### created\_on

* **Meaning**: Timestamp of when the record was created.
* **Role**: Technical field.
* **Typical Contents**: Date and time in UTC.
* **Note**: Indicates the creation time of the record.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification of the record.
* **Role**: Technical field.
* **Typical Contents**: Date and time in UTC, or null if not modified.
* **Note**: Tracks the most recent update to the record.

#### is\_deleted

* **Meaning**: Indicates whether the record is marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Boolean value, `True` or `False`.
* **Note**: Helps in soft deletion handling.

#### deleted\_on

* **Meaning**: Timestamp of when the record was marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Date and time in UTC, or default ancient date if not deleted.
* **Note**: Used to track when the record was deleted.

#### last\_modified\_by

* **Meaning**: ID of the user who last modified the record.
* **Role**: Foreign key.
* **Typical Contents**: UUID string, or null if not modified.
* **Note**: Identifies the user responsible for the last modification.

#### deleted\_by

* **Meaning**: ID of the user who marked the record as deleted.
* **Role**: Foreign key.
* **Typical Contents**: UUID string, or null if not deleted.
* **Note**: Tracks who performed the deletion action.

This documentation provides a detailed overview of the table structure and its columns, facilitating better understanding and utilization by developers and database administrators.
