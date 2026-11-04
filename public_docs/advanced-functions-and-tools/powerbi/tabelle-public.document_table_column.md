# Tabelle public.document\_table\_column

## Spalten

* `id`: internal
* `document_table_id`: internal
* `table_name`: internal
* `org_id`: ID to organisation
* `column_name`: internal
* `column_type`: internal
* `title`: internal
* `translation_key`: internal
* `sort_order`: integer
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.document_table_column`

## Introduction

The `public.document_table_column` table appears to be designed to store metadata about columns in various document-related tables, such as invoice or delivery note tables. This metadata includes information about each column's name, type, and properties, as well as organizational and technical identifiers. The table supports the dynamic generation and management of document schemas within the system.

## Column Descriptions

### id
- **Meaning**: A unique identifier for each column entry in the table.
- **Role**: Primary key.
- **Note**: Typically a UUID string that uniquely identifies a row in this table.

### document_table_id
- **Meaning**: Refers to the table that contains the document this column is part of.
- **Role**: Foreign key.
- **Note**: Likely a UUID that links to another table where document tables are defined.

### table_name
- **Meaning**: The name of the document table to which this column belongs.
- **Role**: Descriptive field.
- **Typical Contents**: Names like `INVOICE_TABLE`, `DELIVERY_NOTE_TABLE`.
- **Note**: Facilitates understanding of which document structure the column belongs to.

### org_id
- **Meaning**: Identifier for the organization that owns or manages the document table.
- **Role**: Foreign key.
- **Note**: Typically a UUID linking to an organization entity.

### column_name
- **Meaning**: The technical name of the column within its document table.
- **Role**: Descriptive field.
- **Typical Contents**: Names such as `COUNTRY_ORIGIN`, `ORDERED_QUANTITY`.
- **Note**: Represents the actual field name in the document table.

### column_type
- **Meaning**: Describes the data type of the column.
- **Role**: Descriptive field.
- **Typical Contents**: `STRING`, `DATE`.
- **Note**: Indicates the kind of data stored in the column.

### title
- **Meaning**: A human-readable title or label for the column.
- **Role**: Descriptive field.
- **Typical Contents**: `COUNTRY_ORIGIN`, `Ordered Quantity`.
- **Note**: Used for displaying column names in a user-friendly manner.

### translation_key
- **Meaning**: Key used for internationalization and localization of the column title.
- **Role**: Technical field.
- **Note**: Currently empty in example data, suggesting optional use.

### sort_order
- **Meaning**: Defines the order of columns when displayed.
- **Role**: Descriptive field.
- **Typical Contents**: Integers like `16`, `5`.
- **Note**: Determines the sequence of columns in the document table view.

### clean_field
- **Meaning**: Indicates if the column contains sanitized data.
- **Role**: Boolean flag.
- **Typical Contents**: `True` or `False`.
- **Note**: Used for data validation or cleaning status.

### alphanumeric_field
- **Meaning**: Specifies if the column should be treated as an alphanumeric field.
- **Role**: Boolean flag.
- **Typical Contents**: `True` or `False`.
- **Note**: Useful for input validation or formatting purposes.

### created_by
- **Meaning**: Identifier of the user who created this column entry.
- **Role**: Foreign key.
- **Typical Contents**: Integer values like `1`, `8`.
- **Note**: Links to a user or system entity responsible for the creation.

### created_on
- **Meaning**: Timestamp of when the column entry was created.
- **Role**: Technical field.
- **Typical Contents**: Date and time values in UTC.
- **Note**: Useful for auditing and tracking changes.

### last_modified_on
- **Meaning**: Timestamp of the last modification made to the column entry.
- **Role**: Technical field.
- **Note**: Currently `None` in example data, indicating no modification has occurred after creation.

### is_deleted
- **Meaning**: Indicates if the column entry has been logically deleted.
- **Role**: Boolean flag.
- **Typical Contents**: `True` or `False`.
- **Note**: Helps in managing soft deletions without removing data physically.

```
