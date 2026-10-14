# Training data

## Tabelle `public.training_data`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `doc_origin`: Doc Origin
* `doc_locale`: Doc Locale
* `doc_language`: Language
* `first_page_content`: text
* `supplier_name`: Supplier Name
* `supplier_vat`: internal
* `doc_created_on`: timestamp with time zone
* `is_training_sample`: boolean
* `sample_doc_id`: internal
* `sample_file_name`: internal
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_table_training_sample`: boolean

### Analyse & Beschreibung

## Technical Documentation for `public.training_data` Table

### Introduction

The `public.training_data` table appears to be designed for storing various document-related data, likely used for training models or systems that process and analyze document contents. The table includes information about the document type, origin, language, supplier details, and timestamps related to the creation and modification of records, among other attributes. It seems particularly focused on invoices and medical receipts, which suggests its use in financial or healthcare data processing applications.

### Column Descriptions

#### id

* **Meaning**: Unique identifier for each record in the table.
* **Role**: Primary key.
* **Typical Contents**: A universally unique identifier (UUID) in character format.
* **Note**: Essential for uniquely identifying each entry.

#### org\_id

* **Meaning**: Identifier for the organization associated with the document.
* **Role**: Foreign key that links to an organization record.
* **Typical Contents**: UUID representing an organization.
* **Note**: Helps in associating documents with specific organizations.

#### doc\_type

* **Meaning**: Type of document stored in the record.
* **Role**: Descriptive field.
* **Typical Contents**: Values such as 'INVOICE' or 'MEDICAL\_RECEIPT'.
* **Note**: Useful for categorizing the documents.

#### doc\_origin

* **Meaning**: Origin or source country code of the document.
* **Role**: Descriptive field.
* **Typical Contents**: Country code like 'DE' for Germany.
* **Note**: Indicates the geographical origin of the document.

#### doc\_locale

* **Meaning**: Locale information of the document.
* **Role**: Descriptive field.
* **Typical Contents**: Locale code such as 'en\_DE'.
* **Note**: Combines language and region for localization purposes.

#### doc\_language

* **Meaning**: Language in which the document is written.
* **Role**: Descriptive field.
* **Typical Contents**: Language code like 'en' or 'de'.
* **Note**: Indicates the primary language used in the document.

#### first\_page\_content

* **Meaning**: Content of the first page of the document.
* **Role**: Descriptive field.
* **Typical Contents**: Text data containing the document's first page content.
* **Note**: May be used for text analysis or processing.

#### supplier\_name

* **Meaning**: Name of the supplier associated with the document.
* **Role**: Descriptive field.
* **Typical Contents**: Supplier's name in text format.
* **Note**: Important for identifying the source or creator of the document.

#### supplier\_vat

* **Meaning**: VAT identification number of the supplier.
* **Role**: Descriptive field.
* **Typical Contents**: VAT ID, e.g., 'DE 129375678'.
* **Note**: Useful for fiscal and tax-related processes.

#### doc\_created\_on

* **Meaning**: Timestamp when the document was created.
* **Role**: Descriptive field.
* **Typical Contents**: Date and time in UTC format.
* **Note**: Provides temporal context for the document creation.

#### is\_training\_sample

* **Meaning**: Indicator of whether the record is used as a training sample.
* **Role**: Technical field.
* **Typical Contents**: Boolean value (`True` or `False`).
* **Note**: Identifies records specifically marked for training purposes.

#### sample\_doc\_id

* **Meaning**: Identifier for the sample document.
* **Role**: Descriptive field or possible foreign key.
* **Typical Contents**: UUID linking to another document.
* **Note**: May reference a related or original document used for sampling.

#### sample\_file\_name

* **Meaning**: Name of the file associated with the document sample.
* **Role**: Descriptive field.
* **Typical Contents**: File name in text format.
* **Note**: Useful for file management or retrieval processes.

#### created\_on

* **Meaning**: Timestamp when the record was created.
* **Role**: Technical field.
* **Typical Contents**: Date and time in UTC format.
* **Note**: Indicates when the record was added to the database.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification of the record.
* **Role**: Technical field.
* **Typical Contents**: Date and time in UTC format.
* **Note**: Tracks when the record was last updated.

#### is\_deleted

* **Meaning**: Indicator of whether the record has been marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Boolean value (`True` or `False`).
* **Note**: Supports soft delete functionality.

#### is\_table\_training\_sample

* **Meaning**: Indicator of whether the record is a table-specific training sample.
* **Role**: Technical field.
* **Typical Contents**: Boolean value (`True` or `False`).
* **Note**: Differentiates from general training samples, focusing on table data.
