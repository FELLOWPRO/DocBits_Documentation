# Lookup table

## Table `public.lookup_table`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `data_key`: internal
* `rec_id`: internal
* `prop_name`: internal
* `prop_value`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `prop_value_clean`: internal
* `version`: integer
* `deleted_on`: timestamp with time zone
* `sub_org_id`: internal

### Analyse & Beschreibung

## Technical Documentation for `public.lookup_table`

### Introduction

The `public.lookup_table` is designed to store metadata about various properties associated with organizational data. It likely serves as a key-value store for different attributes related to customers or other entities within the organization. The table captures information such as property names, values, and the context (e.g., organization and sub-organization they belong to) along with audit information like creation and modification timestamps.

### Column Descriptions

#### `id`

* **Meaning**: Unique identifier for each record in the table.
* **Role**: Primary key.
* **Typical Contents**: A UUID string that uniquely identifies each entry.

#### `org_id`

* **Meaning**: Identifier for the organization to which the data belongs.
* **Role**: Foreign key, likely linking to an organization table.
* **Typical Contents**: A UUID string representing the organization.

#### `data_key`

* **Meaning**: A key representing a specific dataset or context within the organization.
* **Role**: Contextual identifier for grouping related properties.
* **Typical Contents**: Alphanumeric string indicating a category, such as `customer_amier`.

#### `rec_id`

* **Meaning**: Identifier for a specific record within the dataset.
* **Role**: Contextual identifier, possibly a foreign key to another table.
* **Typical Contents**: Alphanumeric string or null for records without a specific identifier.

#### `prop_name`

* **Meaning**: Name of the property or attribute.
* **Role**: Descriptive field indicating what the property value represents.
* **Typical Contents**: Strings like 'Kundennummer', 'Versandanschrift', 'Kundenname', etc.

#### `prop_value`

* **Meaning**: Value of the property described by `prop_name`.
* **Role**: Descriptive field containing the actual data or value.
* **Typical Contents**: Strings or numbers representing the value of the property.

#### `created_by`

* **Meaning**: Identifier for the user or system that created the record.
* **Role**: Technical field for audit purposes.
* **Typical Contents**: Integer representing a user ID.

#### `created_on`

* **Meaning**: Timestamp indicating when the record was created.
* **Role**: Technical field for audit purposes.
* **Typical Contents**: Date and time with time zone information.

#### `last_modified_on`

* **Meaning**: Timestamp indicating the last time the record was modified.
* **Role**: Technical field for audit purposes.
* **Typical Contents**: Date and time with time zone information, potentially null if not modified.

#### `is_deleted`

* **Meaning**: Flag indicating whether the record is deleted.
* **Role**: Technical field indicating logical deletion.
* **Typical Contents**: Boolean value (`True` or `False`).

#### `prop_value_clean`

* **Meaning**: Cleaned or processed version of `prop_value`.
* **Role**: Descriptive field for storing a normalized or standardized value.
* **Typical Contents**: Similar to `prop_value`, potentially null if not applicable.

#### `version`

* **Meaning**: Version number of the record.
* **Role**: Technical field for version control.
* **Typical Contents**: Integer representing the version of the record.

#### `deleted_on`

* **Meaning**: Timestamp indicating when the record was marked as deleted.
* **Role**: Technical field for audit purposes.
* **Typical Contents**: Date and time with time zone information, potentially null if not deleted.

#### `sub_org_id`

* **Meaning**: Identifier for a sub-organization within the main organization.
* **Role**: Foreign key, potentially linking to a sub-organization table.
* **Typical Contents**: A UUID string representing the sub-organization, potentially null if not applicable.
