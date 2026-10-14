# API credentials

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `title`: internal
* `credentials_type`: internal
* `credentials_json`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `last_modified_by`: internal
* `deleted_by`: internal

## Analyse & Beschreibung

```markdown
# Table Documentation: `public.api_credentials`

## Introduction

The `public.api_credentials` table is designed to store and manage API credential information. This table is crucial for organizations to handle their API authentication details securely, ensuring that various services can interact with each other using the correct credentials. It includes information about the type of credentials, the organization to which they belong, and metadata about their creation and modification.

## Column Descriptions

### id
- **Meaning**: A unique identifier for each entry in the table.
- **Role**: Primary key.
- **Typical Contents**: A universally unique identifier (UUID) representing a specific set of API credentials.

### org_id
- **Meaning**: Identifier for the organization that owns the credentials.
- **Role**: Foreign key.
- **Typical Contents**: A UUID that links to the organization's record in another table.

### sub_org_id
- **Meaning**: Identifier for a sub-organization within the main organization.
- **Role**: Foreign key (optional).
- **Typical Contents**: May contain a UUID linking to a sub-organization, or `None`.

### title
- **Meaning**: A descriptive title for the API credentials.
- **Role**: Descriptive field.
- **Typical Contents**: A string such as "supplier_auth" indicating the purpose or usage of the credentials.

### credentials_type
- **Meaning**: Specifies the type of credentials stored.
- **Role**: Descriptive field.
- **Typical Contents**: A string like "ionapi" indicating the format or protocol used by the credentials.

### credentials_json
- **Meaning**: A JSON object containing detailed credential information.
- **Role**: Technical field.
- **Typical Contents**: JSON string with various key-value pairs detailing authentication parameters.

### created_by
- **Meaning**: User ID of the individual who created the credentials record.
- **Role**: Technical field.
- **Typical Contents**: An integer representing the user ID.

### created_on
- **Meaning**: Timestamp indicating when the credentials were created.
- **Role**: Technical field.
- **Typical Contents**: A datetime value with timezone, e.g., `2024-04-08 11:54:55 UTC`.

### last_modified_on
- **Meaning**: Timestamp indicating the last modification time of the credentials.
- **Role**: Technical field.
- **Typical Contents**: A datetime value with timezone, or `None` if never modified.

### is_deleted
- **Meaning**: Flag indicating whether the credentials are marked as deleted.
- **Role**: Technical field.
- **Typical Contents**: A boolean value, where `False` indicates active credentials.

### deleted_on
- **Meaning**: Timestamp indicating when the credentials were marked as deleted.
- **Role**: Technical field.
- **Typical Contents**: A datetime value with timezone, or `None` if not deleted.

### last_modified_by
- **Meaning**: Identifier of the user who last modified the credentials.
- **Role**: Technical field.
- **Typical Contents**: A character string representing the user's ID, or `None`.

### deleted_by
- **Meaning**: Identifier of the user who marked the credentials as deleted.
- **Role**: Technical field.
- **Typical Contents**: A character string representing the user's ID, or `None`.
```
