# Document Report

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `sub_doc_type`: internal
* `time_spent`: internal
* `fields_total`: integer
* `fields_correct`: integer
* `checkbox_fields_total`: integer
* `checkbox_fields_correct`: integer
* `table_values_total`: integer
* `table_values_correct`: integer
* `detail_report`: text
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `validated_by`: integer
* `sub_org_id`: internal

## Analyse & Beschreibung

```markdown
# Document Report Table Documentation

## Introduction
The `public.document_report` table is designed to store detailed information about document processing reports, specifically related to the validation and extraction of fields from documents such as invoices. The table captures metadata about the document, processing metrics, and the validation outcomes, which can be used for auditing, tracking, and improving document processing workflows.

## Column Descriptions

### id
- **Meaning**: Unique identifier for each document report entry.
- **Role**: Primary Key
- **Typical Contents**: A UUID representing the unique document report.

### org_id
- **Meaning**: Identifier for the organization associated with the document.
- **Role**: Foreign Key
- **Typical Contents**: A UUID linking to an organization.

### doc_id
- **Meaning**: Identifier for the specific document being reported.
- **Role**: Foreign Key
- **Typical Contents**: A UUID representing the unique document.

### doc_type
- **Meaning**: Type of the document being processed, such as an invoice.
- **Role**: Descriptive Field
- **Typical Contents**: Values like `INVOICE`.

### sub_doc_type
- **Meaning**: Subtype of the document, providing further categorization.
- **Role**: Descriptive Field
- **Typical Contents**: Could be `null` or specific subtypes like "Cost Invoice".

### time_spent
- **Meaning**: Time spent on the validation of the document.
- **Role**: Metric Field
- **Typical Contents**: Typically '0', measuring time in predefined units.

### fields_total
- **Meaning**: Total number of fields extracted from the document.
- **Role**: Metric Field
- **Typical Contents**: An integer representing total fields, e.g., 13.

### fields_correct
- **Meaning**: Number of fields correctly extracted and validated.
- **Role**: Metric Field
- **Typical Contents**: An integer representing correctly processed fields, e.g., 12.

### checkbox_fields_total
- **Meaning**: Total number of checkbox fields processed.
- **Role**: Metric Field
- **Typical Contents**: Usually `0`, indicating checkbox fields processed.

### checkbox_fields_correct
- **Meaning**: Number of checkbox fields correctly validated.
- **Role**: Metric Field
- **Typical Contents**: Usually `0`, indicating correctly validated checkbox fields.

### table_values_total
- **Meaning**: Total number of table values extracted from the document.
- **Role**: Metric Field
- **Typical Contents**: Usually `0`, indicating total table values processed.

### table_values_correct
- **Meaning**: Number of table values correctly validated.
- **Role**: Metric Field
- **Typical Contents**: Usually `0`, indicating correctly validated table values.

### detail_report
- **Meaning**: JSON content providing detailed report of the document fields and their validation status.
- **Role**: Descriptive/Technical Field
- **Typical Contents**: JSON string containing detailed field information.

### created_on
- **Meaning**: Timestamp when the document report entry was created.
- **Role**: Technical Field
- **Typical Contents**: Timestamp in UTC, e.g., `2025-03-10 08:07:24+00`.

### last_modified_on
- **Meaning**: Timestamp of the last modification to the document report.
- **Role**: Technical Field
- **Typical Contents**: Timestamp in UTC, indicating the last update time.

### is_deleted
- **Meaning**: Indicates whether the document report has been marked as deleted.
- **Role**: Technical Field
- **Typical Contents**: Boolean value; `False` if not deleted.

### validated_by
- **Meaning**: Identifier of the user who validated the document.
- **Role**: Foreign Key
- **Typical Contents**: Integer representing the validator's ID, e.g., `1`.

### sub_org_id
- **Meaning**: Identifier for a sub-organization related to the document.
- **Role**: Foreign Key
- **Typical Contents**: A UUID linking to a sub-organization.
```
