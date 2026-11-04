# Batch instance

## Tabelle `public.batch_instance`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Table Documentation: `public.batch_instance`

### Introduction

The `public.batch_instance` table is designed to store information about various batch instances within an organization. It contains key metadata about each instance, including its unique identification, the organization it belongs to, and its creation and modification details. This table is essential for tracking the lifecycle and management of batch instances, likely in a software application dealing with batch processing.

### Columns

#### `id`

* **Meaning**: This column stores the unique identifier for each batch instance.
* **Role**: Primary Key (`id`).
* **Typical Contents**: A UUID string that uniquely identifies each batch instance, e.g., `'e9aa9ad7-6c36-4d7c-b31c-6e10bb8fbd87'`.

#### `org_id`

* **Meaning**: This column stores the identifier of the organization associated with the batch instance.
* **Role**: Foreign Key (`org_id`).
* **Typical Contents**: A UUID string representing the organization, e.g., `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### `created_by`

* **Meaning**: This column indicates the user or system entity that created the batch instance.
* **Role**: Possibly a Foreign Key, referencing a user table or similar.
* **Typical Contents**: An integer representing the ID of the creator, e.g., `1`.

#### `created_on`

* **Meaning**: This column records the timestamp of when the batch instance was created.
* **Role**: Technical field for auditing and tracking purposes.
* **Typical Contents**: A timestamp with time zone, e.g., `2021-09-22 10:55:59.755627+00`.

#### `last_modified_on`

* **Meaning**: This column captures the timestamp of the last modification made to the batch instance.
* **Role**: Technical field for auditing changes.
* **Typical Contents**: Typically null or a timestamp with time zone if modifications have occurred.

#### `is_deleted`

* **Meaning**: This column indicates whether the batch instance is marked as deleted.
* **Role**: Technical field for soft deletion purposes.
* **Typical Contents**: A boolean value, typically `False` if the instance is active, e.g., `False`.

This documentation provides a comprehensive overview of the `public.batch_instance` table, detailing the purpose and structure of each column, which is crucial for developers working with this data model.
