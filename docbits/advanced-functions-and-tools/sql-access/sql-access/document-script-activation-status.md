# Document Script activation status

## Tabelle `public.document_script_activation_status`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `sort_order`: integer
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `script_id`: internal

### Analyse & Beschreibung

## Table Documentation: `public.document_script_activation_status`

### Introduction

The `public.document_script_activation_status` table is designed to manage the activation status of scripts associated with documents within an organization. Each entry in the table corresponds to a specific script and its current activation status, potentially allowing organizations to control and organize the execution of scripts in relation to their documents.

### Column Descriptions

#### id

* **Meaning**: This column stores a unique identifier for each entry in the table.
* **Role**: Primary key.
* **Typical Contents**: Universally unique identifier (UUID) such as `c599a3fa-a784-446a-a48e-cf37b95d93cd`.
* **Note**: Ensures that each record is uniquely identifiable.

#### org\_id

* **Meaning**: Represents the identifier for an organization.
* **Role**: Foreign key, likely referencing an organization table.
* **Typical Contents**: UUID that identifies the organization, e.g., `23f3d697-7411-4c95-981d-faf089d266be`.
* **Note**: Links the script activation status to a specific organization.

#### sort\_order

* **Meaning**: Indicates the order in which scripts should be executed or displayed.
* **Role**: Technical field.
* **Typical Contents**: Integer values representing the sequence, such as `0`.
* **Note**: May be used to prioritize or organize scripts.

#### is\_active

* **Meaning**: Denotes whether a script is currently active.
* **Role**: Technical field.
* **Typical Contents**: Boolean values, `True` or `False`.
* **Note**: Determines if the associated script should be executed.

#### created\_by

* **Meaning**: Identifier of the user who created the record.
* **Role**: Foreign key, likely referencing a user table.
* **Typical Contents**: Integer value representing a user ID, such as `1`.
* **Note**: Tracks the creator of the record for auditing purposes.

#### created\_on

* **Meaning**: Timestamp of when the record was created.
* **Role**: Technical field.
* **Typical Contents**: Date and time with timezone, e.g., `2023-11-20 10:44:14.685170+00:00`.
* **Note**: Provides a creation timestamp for record-keeping.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification to the record.
* **Role**: Technical field.
* **Typical Contents**: Date and time with timezone, or `None` if never modified.
* **Note**: Useful for tracking changes over time.

#### is\_deleted

* **Meaning**: Indicates whether the record is marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Boolean values, `True` or `False`.
* **Note**: Allows soft deletion of records without physical removal from the database.

#### script\_id

* **Meaning**: Identifier for the script associated with the record.
* **Role**: Foreign key, likely referencing a script table.
* **Typical Contents**: UUID that identifies the script, e.g., `4edc8cd7-e1bc-443a-9a23-dc490a09e80b`.
* **Note**: Links the activation status to a specific script.
