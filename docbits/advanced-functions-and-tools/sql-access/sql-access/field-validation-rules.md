# Field validation rules

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `field_id`: internal
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: internal
* `field_name`: internal
* `field_length`: integer
* `field_label`: internal
* `is_required`: boolean
* `is_readonly`: boolean
* `is_hidden`: boolean
* `force_validation`: boolean
* `validation_pattern`: internal
* `confidence_threshold`: integer
* `match_score_threshold`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `additional_attributes`: text

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.field_validation_rules` Table

## Introduction

The `public.field_validation_rules` table appears to store metadata and validation rules for fields associated with various document types within an organization. It is likely used to enforce data integrity and consistency across forms or documents by specifying requirements such as whether a field is required, its length, visibility, and any validation patterns that should be applied.

## Column Descriptions

### id
- **Meaning**: A unique identifier for each field validation rule.
- **Role**: Primary key.
- **Typical Contents**: A UUID string that uniquely identifies a record.

### org_id
- **Meaning**: Identifier for the organization that the validation rule applies to.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string referencing a specific organization.

### field_id
- **Meaning**: Identifier for the specific field that the validation rule is associated with.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string referencing a specific field.

### doc_type
- **Meaning**: Specifies the document type that the field validation rule is associated with.
- **Role**: Descriptive field.
- **Typical Contents**: A string indicating the type of document (e.g., `PURCHASE_ORDER_FORM`).

### is_sub_doc_type_field
- **Meaning**: Indicates whether the field is part of a sub-document type.
- **Role**: Descriptive field.
- **Typical Contents**: Boolean value (`True` or `False`).

### profile
- **Meaning**: Represents the profile or context in which the field validation is applied.
- **Role**: Descriptive field.
- **Typical Contents**: A string such as `DEFAULT`.

### field_name
- **Meaning**: The name of the field for which the validation rule is defined.
- **Role**: Descriptive field.
- **Typical Contents**: A string representing the field name (e.g., `Test`).

### field_length
- **Meaning**: The maximum allowable length for the field's content.
- **Role**: Descriptive field.
- **Typical Contents**: An integer specifying the character limit.

### field_label
- **Meaning**: The label or display name for the field in the user interface.
- **Role**: Descriptive field.
- **Typical Contents**: Typically null in the example data.

### is_required
- **Meaning**: Indicates if the field is mandatory for the document.
- **Role**: Constraint indicator.
- **Typical Contents**: Boolean value (`True` or `False`).

### is_readonly
- **Meaning**: Specifies if the field is editable or read-only.
- **Role**: Constraint indicator.
- **Typical Contents**: Boolean value (`True` or `False`).

### is_hidden
- **Meaning**: Indicates if the field should be hidden from the user interface.
- **Role**: Constraint indicator.
- **Typical Contents**: Boolean value (`True` or `False`).

### force_validation
- **Meaning**: Determines whether validation should be enforced regardless of other conditions.
- **Role**: Constraint indicator.
- **Typical Contents**: Boolean value (`True` or `False`).

### validation_pattern
- **Meaning**: A pattern (likely regex) that the field's content must match.
- **Role**: Validation rule.
- **Typical Contents**: Typically null in the example data.

### confidence_threshold
- **Meaning**: The minimum confidence level required for the validation of the field.
- **Role**: Validation constraint.
- **Typical Contents**: An integer value representing the confidence threshold.

### match_score_threshold
- **Meaning**: The minimum match score required for field content validation.
- **Role**: Validation constraint.
- **Typical Contents**: An integer value representing the match score threshold.

### created_by
- **Meaning**: Identifier for the user who created this validation rule.
- **Role**: Descriptive field.
- **Typical Contents**: An integer representing the user ID.

### created_on
- **Meaning**: Timestamp indicating when the validation rule was created.
- **Role**: Technical field.
- **Typical Contents**: A timestamp with time zone.

### last_modified_on
- **Meaning**: Timestamp indicating the last modification of the validation rule.
- **Role**: Technical field.
- **Typical Contents**: A timestamp with time zone, can be null if never modified.

### is_deleted
- **Meaning**: Indicates if the validation rule has been marked as deleted.
- **Role**: Soft delete indicator.
- **Typical Contents**: Boolean value (`True` or `False`).

### additional_attributes
- **Meaning**: Stores extra attributes or metadata associated with the field validation rule.
- **Role**: Descriptive field.
- **Typical Contents**: Text, often null in the example data.
```
