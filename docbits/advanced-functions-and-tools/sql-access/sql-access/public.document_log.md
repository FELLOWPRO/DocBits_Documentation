# public.document\_log

## Tabelle `public.document_log`

### Spalten

* `id`: integer
* `org_id`: ID to organisation
* `doc_id`: internal
* `action_type`: internal
* `action_description`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_hidden`: boolean
* `previous_status`: internal
* `current_status`: internal

### Analyse & Beschreibung

## Technical Documentation: `public.document_log` Table

### Introduction

The `public.document_log` table is designed to track the history and status changes of documents within an organization. It records actions performed on documents, such as status updates, along with details about the user who performed the action and timestamps indicating when these actions took place. This table is crucial for auditing document processing workflows and understanding the lifecycle of each document.

### Column Descriptions

#### id

* **Meaning**: Unique identifier for each log entry.
* **Role**: Primary key. This column serves as the unique identifier for each record in the table.
* **Typical Contents**: Integer values that increment with each new entry.

#### org\_id

* **Meaning**: Identifier for the organization associated with the document.
* **Role**: Foreign key. Links to an organization entity, though not explicitly defined in this context.
* **Typical Contents**: Character strings, likely UUIDs, representing organization identifiers.

#### doc\_id

* **Meaning**: Identifier for the document associated with the log entry.
* **Role**: Foreign key. This column references a specific document within the system.
* **Typical Contents**: Character strings, likely UUIDs, representing document identifiers.

#### action\_type

* **Meaning**: Type of action logged.
* **Role**: Descriptive field. Indicates the category of the action performed.
* **Typical Contents**: Strings such as `STATUS_CHANGE`, indicating the nature of the action.

#### action\_description

* **Meaning**: Detailed description of the action performed.
* **Role**: Descriptive field. Provides context or details about the action.
* **Typical Contents**: Text descriptions, e.g., "Data extraction started", "Error occurred processing document".

#### created\_by

* **Meaning**: Identifier of the user who created the log entry.
* **Role**: Foreign key. Links to a user entity, indicating who performed the action.
* **Typical Contents**: Integer values representing user identifiers.

#### created\_on

* **Meaning**: Timestamp of when the log entry was created.
* **Role**: Technical field. Records the exact time an action was logged.
* **Typical Contents**: Timestamps with time zone information, e.g., `2025-04-01 13:07:51.291193 UTC`.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification of the log entry.
* **Role**: Technical field. Indicates the last update time for the log entry.
* **Typical Contents**: Timestamps, potentially null if not modified after creation.

#### is\_deleted

* **Meaning**: Flag indicating if the log entry is marked as deleted.
* **Role**: Technical field. Used for logical deletion of entries.
* **Typical Contents**: Boolean values, `False` indicating active entries and `True` for deleted ones.

#### is\_hidden

* **Meaning**: Flag indicating if the log entry is hidden from normal view.
* **Role**: Technical field. Used to control visibility of log entries.
* **Typical Contents**: Boolean values, `False` indicating visible entries and `True` for hidden ones.

#### previous\_status

* **Meaning**: Status of the document before the action was performed.
* **Role**: Descriptive field. Provides the state of the document prior to the logged action.
* **Typical Contents**: Strings such as `new`, `validating`, `running`, representing document states.

#### current\_status

* **Meaning**: Status of the document after the action was performed.
* **Role**: Descriptive field. Indicates the updated state of the document following the action.
* **Typical Contents**: Strings such as `running`, `ready_for_validation`, `error`, representing document states.

This documentation provides an overview of the `public.document_log` table, detailing the purpose and structure of each column, which is critical for developers managing document workflows and maintaining audit trails.
