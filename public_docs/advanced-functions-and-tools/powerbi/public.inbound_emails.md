# public.inbound\_emails

## Tabelle `public.inbound_emails`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `is_active`: boolean
* `email_senders`: internal
* `email_receiver`: internal
* `token`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_by`: internal
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_by`: internal
* `deleted_on`: timestamp with time zone

### Analyse & Beschreibung

## Technical Documentation: `public.inbound_emails` Table

### Introduction

The `public.inbound_emails` table is designed to store and manage information about emails received by an organization. This table keeps track of the sender and receiver details, the status of the email, and various metadata related to the creation, modification, and deletion of records. It appears to be part of an email management system within an organization, possibly used for tracking inbound email communications.

### Column Descriptions

#### id

* **Meaning**: Unique identifier for each record in the table.
* **Role**: Primary key.
* **Typical Contents**: A unique string, likely a UUID, such as `'42bf9383-73bf-4b46-9862-3c3a1d97ac80'`.

#### org\_id

* **Meaning**: Identifier for the organization associated with the inbound email.
* **Role**: Foreign key, linking to another table that holds organization details.
* **Typical Contents**: A unique string, likely a UUID, such as `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### is\_active

* **Meaning**: Indicates whether the email record is currently active.
* **Role**: Status indicator.
* **Typical Contents**: A boolean value, either `True` or `False`.

#### email\_senders

* **Meaning**: Stores information about the sender(s) of the email.
* **Role**: Data field.
* **Typical Contents**: A JSON-like string containing details of senders, e.g., `"[{'email': '', 'sub_org': ''}]"`.

#### email\_receiver

* **Meaning**: Email address of the primary recipient.
* **Role**: Data field.
* **Typical Contents**: A string with an email address. In the example, it is empty, suggesting optional or varying use.

#### token

* **Meaning**: A token associated with the email, possibly for authentication or identification.
* **Role**: Authentication or tracking field.
* **Typical Contents**: A long, randomly generated string.

#### created\_by

* **Meaning**: Identifier for the user who created the record.
* **Role**: Foreign key, linking to a user or employee table.
* **Typical Contents**: An integer representing a user ID, such as `1`.

#### created\_on

* **Meaning**: Timestamp for when the record was created.
* **Role**: Metadata field.
* **Typical Contents**: A datetime value with timezone information, e.g., `datetime.datetime(2024, 11, 25, 7, 43, 54, 266771, tzinfo=datetime.timezone.utc)`.

#### last\_modified\_by

* **Meaning**: Identifier for the user who last modified the record.
* **Role**: Foreign key, linking to a user or employee table.
* **Typical Contents**: Could be a user ID or null if no modifications have been made.

#### last\_modified\_on

* **Meaning**: Timestamp for when the record was last modified.
* **Role**: Metadata field.
* **Typical Contents**: A datetime value indicating the last modification time, e.g., `datetime.datetime(2024, 11, 25, 7, 44, 48, 505384, tzinfo=datetime.timezone.utc)`.

#### is\_deleted

* **Meaning**: Indicates whether the email record has been marked as deleted.
* **Role**: Status indicator.
* **Typical Contents**: A boolean value, either `True` or `False`.

#### deleted\_by

* **Meaning**: Identifier for the user who marked the record as deleted.
* **Role**: Foreign key, linking to a user or employee table.
* **Typical Contents**: Could be a user ID or null if the record is not deleted.

#### deleted\_on

* **Meaning**: Timestamp for when the record was marked as deleted.
* **Role**: Metadata field.
* **Typical Contents**: A datetime value indicating the deletion time, or a default date if not applicable, e.g., `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`.
