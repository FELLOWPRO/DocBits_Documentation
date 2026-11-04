# Tabelle public.field

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: internal
* `field_name`: internal
* `field_type`: internal
* `title`: internal
* `translation_key`: internal
* `hide_label`: boolean
* `input_type`: internal
* `input_size`: internal
* `icon_left`: internal
* `icon_right`: internal
* `icon_above`: internal
* `group_id`: internal
* `row_order`: integer
* `sort_order`: integer
* `fuzzy_name`: internal
* `fuzzy_field`: internal
* `fuzzy_primary_field`: boolean
* `label_align`: internal
* `calculation_formula`: text
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `placeholder`: internal
* `coordinates`: internal
* `normalized_coordinates`: internal
* `threshold`: internal
* `reference_point`: internal
* `checkbox_group`: internal
* `list_of_values`: internal
* `enforce_list_of_values`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `costing_element`: internal
* `erp_field_name`: internal

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.field` Table

## Introduction

The `public.field` table appears to be designed to manage metadata and configuration for different fields associated with documents, likely within an insurance domain. Each row in the table seems to represent a specific field configuration, including its type, label, visibility settings, and other properties that dictate how the field should be presented and processed.

## Columns

### id
- **Meaning**: Unique identifier for each field configuration.
- **Role**: Primary key.
- **Typical Contents**: A UUID string that uniquely identifies each entry in the table.

### org_id
- **Meaning**: Identifier for the organization associated with the field configuration.
- **Role**: Foreign key.
- **Typical Contents**: A UUID referencing an organization.

### doc_type
- **Meaning**: Specifies the document type that the field is associated with.
- **Role**: Possibly a foreign key or a categorical identifier.
- **Typical Contents**: A string in the format `INSURANCE_DOCUMENTS_<UUID>` indicating the document type.

### is_sub_doc_type_field
- **Meaning**: Indicates whether the field is a sub-type of the document type.
- **Role**: Technical field.
- **Typical Contents**: Boolean value (True or False).

### profile
- **Meaning**: Potentially defines the profile or scope of the field.
- **Role**: Descriptive field.
- **Typical Contents**: Often empty or a brief text description.

### field_name
- **Meaning**: The internal name of the field.
- **Role**: Descriptive field.
- **Typical Contents**: A string representing the field's name in a technical context (e.g., `Schadennummer`).

### field_type
- **Meaning**: Defines the type of data the field holds.
- **Role**: Descriptive field.
- **Typical Contents**: Descriptive strings like `STRING`, `AMOUNT`.

### title
- **Meaning**: The display title for the field.
- **Role**: Descriptive field.
- **Typical Contents**: Uppercase string used for displaying the field's label.

### translation_key
- **Meaning**: Key for translation into different languages.
- **Role**: Technical field.
- **Typical Contents**: Lowercase string representing the translation key.

### hide_label
- **Meaning**: Indicates if the field's label should be hidden in the UI.
- **Role**: Technical field.
- **Typical Contents**: Boolean value (True or False).

### input_type
- **Meaning**: Specifies the input method for the field.
- **Role**: Descriptive field.
- **Typical Contents**: Can be empty or contain strings defining the input type.

### input_size
- **Meaning**: Determines the size of the input field.
- **Role**: Descriptive field.
- **Typical Contents**: Can be empty or contain strings defining input size.

### icon_left
- **Meaning**: Icon to display on the left side of the field.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains icon identifiers.

### icon_right
- **Meaning**: Icon to display on the right side of the field.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains icon identifiers.

### icon_above
- **Meaning**: Icon to display above the field.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains icon identifiers.

### group_id
- **Meaning**: Identifier for the group of fields to which this field belongs.
- **Role**: Foreign key.
- **Typical Contents**: A UUID referencing a group of fields.

### row_order
- **Meaning**: Determines the order of the field in a list or form.
- **Role**: Technical field.
- **Typical Contents**: Integer indicating the position.

### sort_order
- **Meaning**: Specifies sorting order for the field.
- **Role**: Technical field.
- **Typical Contents**: Integer that defines sorting precedence.

### fuzzy_name
- **Meaning**: An alternate name for fuzzy matching.
- **Role**: Descriptive field.
- **Typical Contents**: Often empty or contains a string for matching purposes.

### fuzzy_field
- **Meaning**: Specifies if the field is used in fuzzy matching.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains a string.

### fuzzy_primary_field
- **Meaning**: Indicates if this is the primary field for fuzzy matching.
- **Role**: Technical field.
- **Typical Contents**: Boolean value (True or False).

### label_align
- **Meaning**: Alignment setting for the field label.
- **Role**: Descriptive field.
- **Typical Contents**: Often empty or contains alignment information (e.g., left, right, center).

### calculation_formula
- **Meaning**: Formula used for calculations involving the field.
- **Role**: Technical field.
- **Typical Contents**: Text containing a formula or calculation logic.

### clean_field
- **Meaning**: Indicates if the field should be subject to data cleaning.
- **Role**: Technical field.
- **Typical Contents**: Boolean value (True or False).

### alphanumeric_field
- **Meaning**: Specifies if the field should accept only alphanumeric characters.
- **Role**: Technical field.
- **Typical Contents**: Boolean value (True or False).

### placeholder
- **Meaning**: Placeholder text for the input field.
- **Role**: Descriptive field.
- **Typical Contents**: Often empty or contains guiding text.

### coordinates
- **Meaning**: Coordinate data associated with the field.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains coordinate information.

### normalized_coordinates
- **Meaning**: Normalized version of coordinates for consistency.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains normalized coordinate data.

### threshold
- **Meaning**: Threshold value related to field validation or processing.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains threshold values.

### reference_point
- **Meaning**: Reference point used in calculations or positioning.
- **Role**: Descriptive field.
- **Typical Contents**: Often empty or contains reference point data.

### checkbox_group
- **Meaning**: Grouping identifier for checkbox fields.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains group identifiers.

### list_of_values
- **Meaning**: Specifies a list of allowed values for the field.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains a list of values.

### enforce_list_of_values
- **Meaning**: Indicates if the list of values should be strictly enforced.
- **Role**: Technical field.
- **Typical Contents**: Boolean value (True or False).

### created_by
- **Meaning**: Identifier for the user who created the field entry.
- **Role**: Descriptive field.
- **Typical Contents**: Integer referencing a user ID.

### created_on
- **Meaning**: Timestamp of when the field was created.
- **Role**: Technical field.
- **Typical Contents**: Date and time in UTC.

### last_modified_on
- **Meaning**: Timestamp of the last modification to the field.
- **Role**: Technical field.
- **Typical Contents**: Date and time in UTC.

### is_deleted
- **Meaning**: Indicates if the field has been marked as deleted.
- **Role**: Technical field.
- **Typical Contents**: Boolean value (True or False).

### costing_element
- **Meaning**: Costing element associated with the field.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains costing element identifiers.

### erp_field_name
- **Meaning**: Name of the field as used in ERP systems.
- **Role**: Descriptive field.
- **Typical Contents**: Generally empty or contains ERP-specific field names.

This documentation provides a detailed overview of the structure and purpose of each column within the `public.field` table. It serves as a guide for developers to understand the data model and its application in the system.
```
