# Tabelle custom\_classification\_tag

## Tabelle `public.custom_classification_tag`

### Spalten

* `id`: integer
* `org_id`: ID to organisation
* `name`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technical Documentation for `public.custom_classification_tag` Table

### Introduction

The `public.custom_classification_tag` table is designed to manage custom classification tags within an organization. It captures essential information about each tag, including its association with an organization, its creation and modification details, and its lifecycle status.

### Column Descriptions

#### id

* **Meaning**: A unique identifier for each classification tag.
* **Role**: Primary key.
* **Typical Contents**: An integer value that uniquely identifies each record in the table.

#### org\_id

* **Meaning**: The identifier of the organization to which the classification tag belongs.
* **Role**: Foreign key.
* **Typical Contents**: A character string, likely a UUID, representing the organization's unique ID.

#### name

* **Meaning**: The name or label of the classification tag.
* **Role**: Descriptive field.
* **Typical Contents**: A string that denotes the tag's name or description. It can be an empty string if the name is not provided.

#### created\_by

* **Meaning**: The identifier of the user who created the classification tag.
* **Role**: Foreign key.
* **Typical Contents**: An integer representing the user ID of the creator.

#### created\_on

* **Meaning**: The timestamp indicating when the classification tag was created.
* **Role**: Technical field.
* **Typical Contents**: A timestamp with time zone, capturing the exact date and time of creation.

#### last\_modified\_on

* **Meaning**: The timestamp of the last modification made to the classification tag.
* **Role**: Technical field.
* **Typical Contents**: A timestamp with time zone, which may be `None` if no modifications have occurred since creation.

#### is\_deleted

* **Meaning**: A flag indicating whether the classification tag has been marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: A boolean value (`True` or `False`), where `False` means the tag is active and `True` indicates it has been deleted or deactivated.
