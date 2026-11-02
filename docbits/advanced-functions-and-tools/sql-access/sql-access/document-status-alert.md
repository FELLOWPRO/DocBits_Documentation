# Document Status alert

## Table `public.document_status_alert`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_id`: internal
* `doc_type_key`: internal
* `doc_status`: internal
* `email_address`: text
* `send_to_assigned_user`: boolean
* `delay_delta`: integer
* `delay_delta_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `name`: internal
* `is_recursive`: boolean
* `is_active`: boolean
* `priority`: internal
* `email_template_id`: internal

### Analyse & Beschreibung

## Table Documentation: `public.document_status_alert`

### Introduction

The `public.document_status_alert` table appears to be designed for managing alerts related to document statuses within an organization. Based on the column names, the table stores information about various document types and their statuses, including details about notifications and timing for alerts. This table is likely used to trigger alerts based on certain document statuses and conditions, possibly to notify users or escalate processes.

### Column Descriptions

#### `id`

* **Meaning**: Unique identifier for each alert record.
* **Role**: Primary key.
* **Typical Contents**: A UUID string that uniquely identifies each row in the table.

#### `org_id`

* **Meaning**: Identifier for the organization associated with the alert.
* **Role**: Foreign key.
* **Typical Contents**: A UUID string linking to an organization record.

#### `doc_type_id`

* **Meaning**: Identifier for the document type.
* **Role**: Foreign key (assumed).
* **Typical Contents**: Typically a UUID, though the example data shows `None`, indicating this field might be optional.

#### `doc_type_key`

* **Meaning**: Key representing the type of document.
* **Role**: Descriptive field.
* **Typical Contents**: A string such as 'INVOICE' or 'XML\_INVOICE'.

#### `doc_status`

* **Meaning**: Current status of the document.
* **Role**: Descriptive field.
* **Typical Contents**: Descriptive status strings like 'validated\_pending\_approval' or 'error'.

#### `email_address`

* **Meaning**: Email address where alerts are sent.
* **Role**: Notification field.
* **Typical Contents**: An email address; can be `None` if no email is specified.

#### `send_to_assigned_user`

* **Meaning**: Indicates if the alert should be sent to the user assigned to the document.
* **Role**: Boolean field.
* **Typical Contents**: `True` or `False`.

#### `delay_delta`

* **Meaning**: Amount of time to delay the alert.
* **Role**: Timing field.
* **Typical Contents**: Integer representing the delay duration.

#### `delay_delta_type`

* **Meaning**: Unit of time for `delay_delta`.
* **Role**: Timing field.
* **Typical Contents**: Typically 'minutes'.

#### `created_by`

* **Meaning**: Identifier of the user who created the alert record.
* **Role**: Foreign key (assumed).
* **Typical Contents**: Integer representing a user ID.

#### `created_on`

* **Meaning**: Timestamp when the alert record was created.
* **Role**: Technical field.
* **Typical Contents**: Datetime with timezone information.

#### `last_modified_on`

* **Meaning**: Timestamp of the last modification to the alert record.
* **Role**: Technical field.
* **Typical Contents**: Datetime with timezone information; can be `None` if not modified.

#### `is_deleted`

* **Meaning**: Indicates if the alert record is marked as deleted.
* **Role**: Boolean field.
* **Typical Contents**: `True` or `False`.

#### `name`

* **Meaning**: Name or label for the alert.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing the alert name.

#### `is_recursive`

* **Meaning**: Indicates if the alert should recur at set intervals.
* **Role**: Boolean field.
* **Typical Contents**: `True` or `False`.

#### `is_active`

* **Meaning**: Indicates if the alert is currently active.
* **Role**: Boolean field.
* **Typical Contents**: `True` or `False`.

#### `priority`

* **Meaning**: Priority level of the alert.
* **Role**: Descriptive field.
* **Typical Contents**: Could be strings like 'High', 'Medium', 'Low'; example data shows `None`.

#### `email_template_id`

* **Meaning**: Identifier for the email template used for the alert.
* **Role**: Foreign key (assumed).
* **Typical Contents**: Typically a UUID; example data shows `None`, indicating this field might be optional.
