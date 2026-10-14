# Ephesoft PO matching

## Tabelle `public.ephesoft_po_matching`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `ephesoft_doc_id`: internal
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technical Documentation for `public.ephesoft_po_matching` Table

### Introduction

The `public.ephesoft_po_matching` table is designed to store and manage data related to the matching of purchase orders with documents, such as invoices, processed by the Ephesoft system. This table captures various details about the documents, their extraction process, and the match status with purchase orders.

### Column Descriptions

#### id

* **Meaning**: A unique identifier for each record in the table, likely representing a specific document or transaction processed.
* **Role**: Primary key.
* **Typical Contents**: Universally unique identifier (UUID) in string format, e.g., `ea587c89-0d4f-4a47-a3ac-89cfb2bed9cb`.

#### org\_id

* **Meaning**: Identifier for the organization associated with the document or transaction.
* **Role**: Foreign key, possibly linking to an organization table.
* **Typical Contents**: UUID in string format, e.g., `23f3d697-7411-4c95-981d-faf089d266be`.

#### doc\_id

* **Meaning**: Identifier for the document processed by the system.
* **Role**: Foreign key, linking to a document table or similar.
* **Typical Contents**: UUID in string format, e.g., `f46c6c90-568b-42ee-ae71-c5a3c22211de`.

#### doc\_type

* **Meaning**: Type of the document processed, indicating the nature of the document (e.g., INVOICE).
* **Role**: Descriptive field.
* **Typical Contents**: String indicating document type, e.g., `INVOICE`.

#### ephesoft\_doc\_id

* **Meaning**: Identifier used by the Ephesoft system to track the document.
* **Role**: Descriptive field.
* **Typical Contents**: Short string, possibly an identifier, e.g., `DOC1`.

#### extracted\_data

* **Meaning**: JSON data containing extracted information from the document, including fields, tables, and metadata.
* **Role**: Data storage field for extracted document content.
* **Typical Contents**: JSON structure with details like document type, fields, tables, and metadata.

#### created\_by

* **Meaning**: Identifier of the user or system that created the record.
* **Role**: Foreign key, possibly linking to a users table.
* **Typical Contents**: Integer representing user ID, e.g., `1`.

#### created\_on

* **Meaning**: Timestamp of when the record was created.
* **Role**: Technical field for record tracking.
* **Typical Contents**: Timestamp with timezone, e.g., `2022-02-19 10:43:37 UTC`.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification to the record.
* **Role**: Technical field for record tracking.
* **Typical Contents**: Timestamp with timezone, can be null if not modified since creation.

#### is\_deleted

* **Meaning**: Flag indicating whether the record is marked as deleted.
* **Role**: Technical field for soft deletion.
* **Typical Contents**: Boolean, `true` if the record is deleted, `false` otherwise.
