# public.custom\_classification\_document

## Tabelle `public.custom_classification_document`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `first_page_content`: text
* `content`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technical Documentation for `public.custom_classification_document` Table

### Introduction

The `public.custom_classification_document` table is designed to store detailed information about document classifications within an organization. This includes metadata about the document, such as its content, creation details, and organizational context. The table's structure suggests its use in managing documents related to organizational processes, possibly involving invoices or order forms, as inferred from the example data.

### Column Descriptions

#### id

* **Meaning**: This column likely stores a unique identifier for each document entry.
* **Role**: Primary Key
* **Typical Contents**: A UUID representing a unique document identifier.

#### org\_id

* **Meaning**: This column stores the identifier of the organization associated with the document.
* **Role**: Foreign Key
* **Typical Contents**: A UUID that links the document to a specific organization.

#### first\_page\_content

* **Meaning**: This column contains the text content of the first page of the document.
* **Role**: Data Field
* **Typical Contents**: Textual representation of an organization's document, possibly including headers, addresses, and initial details of an invoice or order.

#### content

* **Meaning**: This column stores the complete text content of the document.
* **Role**: Data Field
* **Typical Contents**: Full textual content of the document, including all details present in the first page and subsequent pages.

#### created\_by

* **Meaning**: This column indicates the user who created the document entry.
* **Role**: Data Field
* **Typical Contents**: An integer representing the user ID of the creator.

#### created\_on

* **Meaning**: This column records the date and time when the document entry was created.
* **Role**: Technical Field
* **Typical Contents**: A timestamp with time zone information, indicating the creation date and time.

#### last\_modified\_on

* **Meaning**: This column stores the date and time of the last modification of the document entry.
* **Role**: Technical Field
* **Typical Contents**: A timestamp with time zone information, indicating the last modification date and time. It is sometimes `None` if no modifications have occurred post-creation.

#### is\_deleted

* **Meaning**: This column indicates whether the document entry has been marked as deleted.
* **Role**: Technical Field
* **Typical Contents**: A boolean value (`True` or `False`) showing the deletion status of the document entry.

This table provides a robust structure for managing document data, ensuring each document can be uniquely identified, associated with an organization, and tracked through its lifecycle of creation and modification.
