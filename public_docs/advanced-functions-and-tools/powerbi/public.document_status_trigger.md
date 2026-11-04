# public.document\_status\_trigger

## Tabelle `public.document_status_trigger`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `trigger_doc_type`: internal
* `trigger_doc_status`: internal
* `trigger_url`: internal
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technical Documentation for `public.document_status_trigger` Table

### Introduction

The `public.document_status_trigger` table is designed to manage and track the status of documents within an organization. This table appears to handle triggers related to document processing, likely in a workflow system. It captures information about document types and their status changes, potentially triggering actions or workflows through specified URLs.

### Column Descriptions

#### id

* **Meaning**: This column stores a unique identifier for each record in the table.
* **Role**: Primary key.
* **Typical Contents**: A UUID string, e.g., `8103b700-c03c-40cb-9322-e9e1ddbe0cb1`.

#### org\_id

* **Meaning**: Represents the unique identifier for an organization.
* **Role**: Foreign key, linking to an organization entity.
* **Typical Contents**: A UUID string, e.g., `23f3d697-7411-4c95-981d-faf089d266be`.

#### trigger\_doc\_type

* **Meaning**: Specifies the type of document associated with the trigger.
* **Role**: Descriptive field indicating the document type.
* **Typical Contents**: Document type names, such as `INVOICE`.

#### trigger\_doc\_status

* **Meaning**: Denotes the specific status of the document that activates the trigger.
* **Role**: Descriptive field detailing the document status.
* **Typical Contents**: Status descriptions, like `approved_pending_second_approval`.

#### trigger\_url

* **Meaning**: URL that is triggered when the document status meets certain conditions.
* **Role**: Technical field for workflow automation.
* **Typical Contents**: URLs, e.g., `https://test-wf-stage.workflow.polydocs.io/webhook/3c3ab41b-a1d9-40a9-8e33-2968d33c989e/webhook`.

#### is\_active

* **Meaning**: Indicates whether the trigger is currently active.
* **Role**: Technical field for managing trigger states.
* **Typical Contents**: Boolean values, `True` or `False`.

#### created\_by

* **Meaning**: Identifies the user who created the record.
* **Role**: Foreign key to a user entity.
* **Typical Contents**: Integer user IDs, e.g., `1`.

#### created\_on

* **Meaning**: Timestamp of when the record was created.
* **Role**: Technical field for auditing and tracking changes.
* **Typical Contents**: Timestamps with timezone, e.g., `2022-09-16 07:26:55 UTC`.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification to the record.
* **Role**: Technical field for auditing and tracking changes.
* **Typical Contents**: Timestamps with timezone, can be `None` if not modified.

#### is\_deleted

* **Meaning**: Marks whether the record is considered deleted or inactive.
* **Role**: Technical field for soft deletion.
* **Typical Contents**: Boolean values, `True` or `False`.

This table provides a structured approach to managing document statuses and associated triggers within an organization's workflow system, ensuring that actions can be taken automatically as documents progress through various states.
