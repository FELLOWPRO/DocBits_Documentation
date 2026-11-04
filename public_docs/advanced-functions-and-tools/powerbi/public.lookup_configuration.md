# public.lookup\_configuration

## Tabelle `public.lookup_configuration`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `lookup_dataset_name`: internal
* `lookup_name`: internal
* `conflict_handle`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `match_all`: boolean
* `last_modified_by`: internal
* `deleted_by`: internal
* `context`: internal
* `context_detail`: internal

### Analyse & Beschreibung

## Technical Documentation for `public.lookup_configuration` Table

### Introduction

The `public.lookup_configuration` table is designed to store configuration settings for various data lookup operations within an organization. It includes information about the organization, the type of documents involved, and specific datasets and names used for lookups. The table also tracks the creation and modification of these configurations, as well as their current status (active or deleted).

### Column Descriptions

#### id

* **Meaning**: A unique identifier for each lookup configuration entry in the table.
* **Role**: Primary key that uniquely identifies each row.
* **Typical Contents**: UUID values, e.g., `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Meaning**: Represents the organization associated with the lookup configuration.
* **Role**: Foreign key, linking to an organization in another table.
* **Typical Contents**: UUID values indicating organization identifiers, e.g., `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Meaning**: Specifies the type of document that the lookup configuration applies to.
* **Role**: Descriptive field indicating the context of the configuration.
* **Typical Contents**: Strings like `'MEDI_ORDER'`, `'INVOICE'`, etc.

#### lookup\_dataset\_name

* **Meaning**: The name of the dataset used for performing lookups.
* **Role**: Descriptive field used to identify datasets.
* **Typical Contents**: Descriptive strings such as `'customer_tini'`, `'supplier'`.

#### lookup\_name

* **Meaning**: The specific name or alias used for the lookup operation.
* **Role**: Descriptive field indicating the operational name.
* **Typical Contents**: Strings like `'customer_tini'`, `'supplier (copy)'`.

#### conflict\_handle

* **Meaning**: Indicates the strategy to handle conflicts during lookups.
* **Role**: Descriptive field for conflict resolution strategy.
* **Typical Contents**: Values such as `'BEST_SCORE'`, `'RETURN_NONE'`.

#### created\_by

* **Meaning**: The ID of the user who created the lookup configuration.
* **Role**: Technical field for tracking the creator of the entry.
* **Typical Contents**: Integer values representing user IDs, e.g., `1`.

#### created\_on

* **Meaning**: Timestamp when the lookup configuration was created.
* **Role**: Technical field for tracking creation time.
* **Typical Contents**: Timestamps, e.g., `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification made to the lookup configuration.
* **Role**: Technical field for tracking the last update time.
* **Typical Contents**: Timestamps, usually `None` if not modified.

#### is\_deleted

* **Meaning**: Indicates whether the lookup configuration has been marked as deleted.
* **Role**: Boolean field for status tracking.
* **Typical Contents**: Boolean values, `False` for active entries.

#### deleted\_on

* **Meaning**: Timestamp of when the lookup configuration was marked as deleted.
* **Role**: Technical field for tracking deletion time.
* **Typical Contents**: Often default to a placeholder date, e.g., `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Meaning**: Specifies if the lookup should match all conditions.
* **Role**: Boolean field for configuration settings.
* **Typical Contents**: Boolean values, typically `False`.

#### last\_modified\_by

* **Meaning**: The ID of the user who last modified the lookup configuration.
* **Role**: Technical field for tracking the user who last updated the entry.
* **Typical Contents**: UUID or identifier of the modifying user, often `None`.

#### deleted\_by

* **Meaning**: The ID of the user who marked the lookup configuration as deleted.
* **Role**: Technical field for tracking the user responsible for deletion.
* **Typical Contents**: UUID or identifier, often `None`.

#### context

* **Meaning**: The context in which the lookup is applied, such as a section of a document.
* **Role**: Descriptive field for operational context.
* **Typical Contents**: Strings like `'header'`.

#### context\_detail

* **Meaning**: Additional details about the context for the lookup.
* **Role**: Descriptive field for extended context information.
* **Typical Contents**: Often `None`, used for additional context description.
