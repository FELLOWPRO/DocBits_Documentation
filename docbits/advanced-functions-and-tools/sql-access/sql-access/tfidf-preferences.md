# Tfidf preferences

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `tfidf_id`: internal
* `pref_key`: internal
* `pref_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_by`: internal
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_by`: internal
* `deleted_on`: timestamp with time zone
* `supplier_id`: internal

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.tfidf_preferences` Table

## Introduction

The `public.tfidf_preferences` table appears to be designed to store preferences related to TF-IDF (Term Frequency-Inverse Document Frequency) configurations or models. This table contains information about specific preferences set by organizations, including preference keys and their corresponding values, along with metadata about creation, modification, and deletion activities.

## Column Descriptions

### id
- **Meaning**: A unique identifier for each record in the table.
- **Role**: Primary Key.
- **Typical Contents**: A UUID string representing the unique ID of a preference entry.

### org_id
- **Meaning**: Identifier for the organization associated with the preference.
- **Role**: Foreign Key.
- **Typical Contents**: A UUID string that links the preference to a specific organization.

### tfidf_id
- **Meaning**: Identifier for the specific TF-IDF configuration or model.
- **Role**: Foreign Key.
- **Typical Contents**: A UUID string representing the linked TF-IDF configuration.

### pref_key
- **Meaning**: The key or name of the preference setting.
- **Role**: Descriptive Field.
- **Typical Contents**: A string representing the name of the preference, such as 'USE_ETEXT_IF_AVAILABLE' or 'AI_MODEL'.

### pref_value
- **Meaning**: The value associated with the preference key.
- **Role**: Descriptive Field.
- **Typical Contents**: A string or text value that corresponds to the preference key, e.g., 'true', 'false', or 'Full'.

### created_by
- **Meaning**: Identifier for the user who created the preference entry.
- **Role**: Descriptive Field.
- **Typical Contents**: An integer representing the user ID of the creator.

### created_on
- **Meaning**: Timestamp of when the preference entry was created.
- **Role**: Technical Field.
- **Typical Contents**: A timestamp with timezone indicating the creation date and time.

### last_modified_by
- **Meaning**: Identifier for the user who last modified the preference entry.
- **Role**: Descriptive Field.
- **Typical Contents**: A UUID representing the user ID of the last person who modified the entry, if applicable.

### last_modified_on
- **Meaning**: Timestamp of the last modification to the preference entry.
- **Role**: Technical Field.
- **Typical Contents**: A timestamp with timezone showing the last modification date and time.

### is_deleted
- **Meaning**: Flag indicating whether the preference entry has been marked as deleted.
- **Role**: Technical Field.
- **Typical Contents**: A boolean value; `True` if the entry is deleted, otherwise `False`.

### deleted_by
- **Meaning**: Identifier for the user who marked the preference entry as deleted.
- **Role**: Descriptive Field.
- **Typical Contents**: A UUID representing the user ID who deleted the entry, if applicable.

### deleted_on
- **Meaning**: Timestamp of when the preference entry was marked as deleted.
- **Role**: Technical Field.
- **Typical Contents**: A timestamp with timezone indicating when the entry was deleted.

### supplier_id
- **Meaning**: Identifier for the supplier associated with the preference.
- **Role**: Foreign Key.
- **Typical Contents**: A UUID string representing the supplier linked to the preference.

This documentation provides a detailed overview of the purpose and structure of the `public.tfidf_preferences` table, assisting developers in understanding how to interact with and utilize this data effectively.
```
