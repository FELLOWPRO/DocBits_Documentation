# Lookup field configuration

## Tabelle `public.lookup_field_configuration`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `lookup_rec_id`: internal
* `field_id`: internal
* `lookup_field`: internal
* `is_searchable`: boolean
* `parent_field_id`: internal
* `auto_trigger`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `search_operator`: internal
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse & Beschreibung

## Table Documentation: `public.lookup_field_configuration`

### Introduction

The `public.lookup_field_configuration` table appears to be a configuration table used to define and manage lookup fields within an application. The table includes metadata about each field, such as its identifier, associated organization, searchability, and audit information. This table is likely part of a larger system for managing dynamic or user-defined fields, allowing for complex querying and configuration capabilities.

### Column Descriptions

#### `id`

* **Meaning**: The unique identifier for each record within the table.
* **Role**: Primary Key.
* **Typical Contents**: A UUID string that uniquely identifies each configuration entry.

#### `org_id`

* **Meaning**: The organization identifier that this configuration is associated with.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID string representing the organization.

#### `lookup_rec_id`

* **Meaning**: An identifier for the specific lookup record this configuration applies to.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID string referencing a specific lookup record.

#### `field_id`

* **Meaning**: The identifier of the field being configured.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID string referencing a particular field.

#### `lookup_field`

* **Meaning**: The name or label of the field being configured.
* **Role**: Descriptive Field.
* **Typical Contents**: A string representing the field name, such as "address\_1" or "taxratefree".

#### `is_searchable`

* **Meaning**: Indicates whether the field can be included in search operations.
* **Role**: Configuration Flag.
* **Typical Contents**: A boolean value (`True` or `False`).

#### `parent_field_id`

* **Meaning**: Identifier of the parent field, if applicable.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID string or `None` if no parent field exists.

#### `auto_trigger`

* **Meaning**: Specifies if the field configuration should automatically trigger certain actions.
* **Role**: Configuration Flag.
* **Typical Contents**: A boolean value (`True` or `False`).

#### `created_by`

* **Meaning**: The identifier of the user who created the configuration entry.
* **Role**: Audit Field.
* **Typical Contents**: An integer representing the user ID.

#### `created_on`

* **Meaning**: The timestamp when the configuration entry was created.
* **Role**: Audit Field.
* **Typical Contents**: A timestamp with timezone information.

#### `last_modified_on`

* **Meaning**: The timestamp of the most recent modification to the configuration entry.
* **Role**: Audit Field.
* **Typical Contents**: A timestamp with timezone information, or `None` if never modified.

#### `is_deleted`

* **Meaning**: Indicates if the configuration entry has been marked as deleted.
* **Role**: Soft Delete Flag.
* **Typical Contents**: A boolean value (`True` or `False`).

#### `deleted_on`

* **Meaning**: The timestamp when the configuration entry was marked as deleted.
* **Role**: Audit Field.
* **Typical Contents**: A timestamp with timezone information, or `None` if not deleted.

#### `search_operator`

* **Meaning**: Defines the search operator used for the field.
* **Role**: Configuration Field.
* **Typical Contents**: A string such as "contains" indicating the type of search operation.

#### `last_modified_by`

* **Meaning**: Identifier of the user who last modified the configuration entry.
* **Role**: Audit Field.
* **Typical Contents**: A UUID string or `None` if never modified.

#### `deleted_by`

* **Meaning**: Identifier of the user who marked the entry as deleted.
* **Role**: Audit Field.
* **Typical Contents**: A UUID string or `None` if not deleted.

This documentation provides a detailed view into the structure and purpose of each column in the `public.lookup_field_configuration` table, offering developers a comprehensive understanding of how lookup fields are configured and managed within the system.
