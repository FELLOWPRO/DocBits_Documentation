# PO match tolerance

## Table `public.po_match_tolerance`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `item_number`: internal
* `supplier_item_number`: internal
* `description`: internal
* `unit_price_tolerance`: double precision
* `quantity_tolerance`: double precision
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `unit_price_tolerance_type`: internal
* `quantity_tolerance_type`: internal

### Analyse & Beschreibung

## Technical Documentation for `public.po_match_tolerance` Table

### Introduction

The `public.po_match_tolerance` table is designed to manage and store tolerance levels associated with purchase order (PO) matching processes. This typically involves the allowable discrepancies in unit prices and quantities between ordered and received goods. Each entry in the table represents tolerance settings for specific items, potentially helping organizations ensure consistency and accuracy in their procurement processes.

### Column Descriptions

#### id

* **Meaning**: A unique identifier for each entry in the table.
* **Role**: Primary key.
* **Typical Contents**: A UUID string that uniquely identifies each tolerance setting record.

#### org\_id

* **Meaning**: Identifier for the organization associated with the tolerance settings.
* **Role**: Foreign key.
* **Typical Contents**: A UUID string linking to the organization within the system.

#### item\_number

* **Meaning**: The specific item number for which tolerance settings are defined.
* **Role**: Business identifier.
* **Typical Contents**: A string representing the code or number of the item in the organization's inventory.

#### supplier\_item\_number

* **Meaning**: The item number as provided by the supplier.
* **Role**: Business identifier.
* **Typical Contents**: A string which may be `None` if not provided, representing the supplier's code or number for the item.

#### description

* **Meaning**: A textual description of the item.
* **Role**: Descriptive field.
* **Typical Contents**: A string providing details about the item, which may be `None`.

#### unit\_price\_tolerance

* **Meaning**: The allowable variance in unit price for the item.
* **Role**: Business rule.
* **Typical Contents**: A numeric value indicating the percentage or absolute value tolerance in unit pricing.

#### quantity\_tolerance

* **Meaning**: The allowable variance in quantity for the item.
* **Role**: Business rule.
* **Typical Contents**: A numeric value indicating the percentage or absolute value tolerance in quantity.

#### created\_by

* **Meaning**: Identifier for the user who created the entry.
* **Role**: Audit/logging field.
* **Typical Contents**: An integer typically referencing a user ID in the system.

#### created\_on

* **Meaning**: The timestamp when the entry was created.
* **Role**: Audit/logging field.
* **Typical Contents**: A datetime value with timezone indicating the creation date and time.

#### last\_modified\_on

* **Meaning**: The timestamp of the last modification to the entry.
* **Role**: Audit/logging field.
* **Typical Contents**: A datetime value with timezone indicating when the record was last updated, which may be `None` if not modified.

#### is\_deleted

* **Meaning**: Indicates whether the entry is logically deleted.
* **Role**: Technical/soft delete indicator.
* **Typical Contents**: A boolean value where `False` means active and `True` means logically deleted.

#### unit\_price\_tolerance\_type

* **Meaning**: Defines the type of unit price tolerance (e.g., percentage or absolute value).
* **Role**: Business rule.
* **Typical Contents**: A string, often 'value' indicating the type of tolerance measure.

#### quantity\_tolerance\_type

* **Meaning**: Defines the type of quantity tolerance (e.g., percentage or absolute value).
* **Role**: Business rule.
* **Typical Contents**: A string, often 'value' indicating the type of tolerance measure.

This documentation provides a detailed overview of each field within the `public.po_match_tolerance` table, offering insights into their potential contents and roles in the context of purchase order management.
