# Preferences

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `pref_key`: internal
* `pref_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `user_id`: integer
* `sub_org_id`: internal

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.preferences` Table

## Introduction
The `public.preferences` table is designed to store configuration settings and preferences for various organizational entities within a system. Each entry in the table represents a specific preference key and its corresponding value, associated with an organization or sub-organization. This configuration data may include settings related to VAT numbers, extraction settings, module activation, and more.

## Column Descriptions

### id
- **Meaning**: This column stores the unique identifier for each preference entry.
- **Role**: Primary key.
- **Typical Contents**: A UUID string that uniquely identifies each row, such as `23f3d697-7411-4c95-981d-faf089d266be`.

### org_id
- **Meaning**: This column stores the identifier of the organization that the preference is associated with.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string matching an organization, similar to `23f3d697-7411-4c95-981d-faf089d266be`.

### pref_key
- **Meaning**: This column represents the key or name of the preference setting.
- **Role**: Descriptive field.
- **Typical Contents**: Strings representing configuration keys, such as `VAT_NUMBERS`, `TABLE_EXTRACTION_SETTING`.

### pref_value
- **Meaning**: This column contains the value of the preference corresponding to the `pref_key`.
- **Role**: Descriptive field.
- **Typical Contents**: Varies depending on the `pref_key`, examples include comma-separated VAT numbers or boolean values like `true` or `false`.

### created_by
- **Meaning**: This column indicates the user ID of the person who created the preference entry.
- **Role**: Descriptive field.
- **Typical Contents**: An integer representing a user ID, e.g., `1`.

### created_on
- **Meaning**: This column records the timestamp when the preference was created.
- **Role**: Technical field.
- **Typical Contents**: A timestamp with time zone, e.g., `2021-11-09 11:04:18+00`.

### last_modified_on
- **Meaning**: This column captures the last modification timestamp of the preference.
- **Role**: Technical field.
- **Typical Contents**: A timestamp with time zone indicating the last update time, such as `2023-12-04 10:10:26+00`.

### deleted_on
- **Meaning**: This column notes the timestamp when the preference was marked as deleted.
- **Role**: Technical field.
- **Typical Contents**: Typically `null` unless the row is marked for deletion.

### is_deleted
- **Meaning**: This column indicates whether the preference has been marked as deleted.
- **Role**: Technical field.
- **Typical Contents**: A boolean value, typically `false`.

### user_id
- **Meaning**: This column stores the user ID associated with the preference.
- **Role**: Descriptive field, potentially a foreign key.
- **Typical Contents**: An integer or `null` if not applicable.

### sub_org_id
- **Meaning**: This column identifies the sub-organization associated with the preference.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string or `null` if not applicable.

The `public.preferences` table provides a flexible and comprehensive way to manage configuration settings across different organizational entities, ensuring that preferences can be dynamically adjusted and tracked over time.
```
