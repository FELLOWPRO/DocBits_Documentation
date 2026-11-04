# Tabelle additional\_charge\_costing\_element

## Tabelle `public.additional_charge_costing_element`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `costing_element`: internal
* `description`: internal
* `charge_type`: internal
* `distribution_method`: internal
* `distribution_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `sub_org_id`: internal
* `charge_count`: integer
* `charge_icon`: internal
* `charge_category`: internal
* `charge_sequence_number`: integer
* `charge_operator`: integer
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse & Beschreibung

## Table Documentation: `public.additional_charge_costing_element`

### Introduction

The `public.additional_charge_costing_element` table is designed to manage and store information about various additional charge costing elements within an organization. This includes data about the type of charges, how they are distributed, and administrative metadata like creation and modification details. This table is likely used for financial and operational management within an organization, focusing on additional costs that need to be tracked and analyzed.

### Column Descriptions

#### id

* **Meaning**: This column stores a unique identifier for each record in the table.
* **Role**: Primary Key.
* **Typical Contents**: A unique alphanumeric string that identifies each costing element record.

#### org\_id

* **Meaning**: The identifier of the organization to which this costing element belongs.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID representing the organization.

#### costing\_element

* **Meaning**: An identifier or code for the costing element.
* **Role**: Descriptive field.
* **Typical Contents**: An alphanumeric string that represents the specific costing element.

#### description

* **Meaning**: A textual description of the costing element.
* **Role**: Descriptive field.
* **Typical Contents**: A brief textual explanation of the costing element.

#### charge\_type

* **Meaning**: The type of charge associated with this costing element.
* **Role**: Descriptive field.
* **Typical Contents**: A code or short text indicating the charge type.

#### distribution\_method

* **Meaning**: Method by which the charge is distributed.
* **Role**: Descriptive field.
* **Typical Contents**: A code or short text indicating the distribution method.

#### distribution\_type

* **Meaning**: Type of distribution for the charge.
* **Role**: Descriptive field.
* **Typical Contents**: A code or short text indicating the distribution type.

#### created\_by

* **Meaning**: Identifier of the user who created the record.
* **Role**: Administrative field.
* **Typical Contents**: An integer representing the user ID.

#### created\_on

* **Meaning**: Timestamp indicating when the record was created.
* **Role**: Administrative field.
* **Typical Contents**: A timestamp with time zone information.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification made to the record.
* **Role**: Administrative field.
* **Typical Contents**: A timestamp with time zone information.

#### is\_deleted

* **Meaning**: Indicates whether the record is marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Boolean value (`True` or `False`).

#### deleted\_on

* **Meaning**: Timestamp when the record was marked as deleted.
* **Role**: Administrative field.
* **Typical Contents**: A timestamp with time zone information or `None` if not deleted.

#### sub\_org\_id

* **Meaning**: Identifier for a sub-organization related to the costing element.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID representing the sub-organization.

#### charge\_count

* **Meaning**: The number of charges associated with the costing element.
* **Role**: Descriptive field.
* **Typical Contents**: An integer representing the count of charges.

#### charge\_icon

* **Meaning**: Icon or symbol associated with the charge.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing the icon, likely a path or identifier.

#### charge\_category

* **Meaning**: The category under which the charge falls.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing the charge category.

#### charge\_sequence\_number

* **Meaning**: Sequence number for ordering charges.
* **Role**: Descriptive field.
* **Typical Contents**: An integer used to sequence charges.

#### charge\_operator

* **Meaning**: Identifier for the operator responsible for the charge.
* **Role**: Descriptive field.
* **Typical Contents**: An integer representing the operator ID.

#### last\_modified\_by

* **Meaning**: Identifier of the user who last modified the record.
* **Role**: Administrative field.
* **Typical Contents**: A string representing the user ID, potentially `None` if never modified.

#### deleted\_by

* **Meaning**: Identifier of the user who marked the record as deleted.
* **Role**: Administrative field.
* **Typical Contents**: A string representing the user ID, potentially `None` if not deleted.
