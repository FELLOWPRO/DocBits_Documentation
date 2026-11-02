# Supplier address

## Spalten

* `org_id`: ID to organisation
* `customer_number`: internal
* `supplier_number`: internal
* `address_id`: internal
* `supplier_name`: Supplier Name
* `address_1`: internal
* `address_2`: internal
* `address_3`: internal
* `address_4`: internal
* `zip_code`: internal
* `town_city`: internal
* `country_code`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: internal
* `id`: internal

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.supplier_address` Table

## Introduction

The `public.supplier_address` table is designed to store information related to the addresses of suppliers. It contains various fields that capture details such as organizational IDs, customer and supplier numbers, multiple address lines, contact details, creation and modification metadata, and deletion status. This table is likely used in a system to manage supplier information and their respective addresses, which can be critical for logistics, billing, and contact purposes.

## Column Descriptions

### org_id
- **Meaning**: This column stores the unique identifier for the organization.
- **Role**: Foreign key, possibly linking to an organization table.
- **Typical Contents**: UUID representing an organization.

### customer_number
- **Meaning**: This column may store a unique number assigned to customers.
- **Role**: Identifier for customers.
- **Typical Contents**: Alphanumeric string representing customer numbers.

### supplier_number
- **Meaning**: This column stores a unique number assigned to suppliers.
- **Role**: Identifier for suppliers.
- **Typical Contents**: Numeric string representing supplier numbers.

### address_id
- **Meaning**: This column likely stores the type of address, such as 'Discrete' or 'Text'.
- **Role**: Descriptive field for address categorization.
- **Typical Contents**: Values like 'Discrete', 'Text'.

### supplier_name
- **Meaning**: This column stores the name of the supplier.
- **Role**: Descriptive field for supplier identification.
- **Typical Contents**: Name of the supplier, e.g., "Cake Corp. GmbH Qualitätsstrawberrys".

### address_1
- **Meaning**: This column stores the primary line of the supplier's address.
- **Role**: Descriptive field for address information.
- **Typical Contents**: Street address, e.g., "Irrweg. 42, D-12345 Blastadt".

### address_2
- **Meaning**: This column stores the second line of the supplier's address, if applicable.
- **Role**: Supplementary field for address information.
- **Typical Contents**: Additional address details, often left empty.

### address_3
- **Meaning**: This column stores the third line of the supplier's address, if applicable.
- **Role**: Supplementary field for address information.
- **Typical Contents**: Additional address details, often left empty.

### address_4
- **Meaning**: This column stores the fourth line of the supplier's address, if applicable.
- **Role**: Supplementary field for address information.
- **Typical Contents**: Additional address details, often left empty.

### zip_code
- **Meaning**: This column stores the postal code for the supplier's address.
- **Role**: Descriptive field for geographical identification.
- **Typical Contents**: Numeric postal code, e.g., "06449".

### town_city
- **Meaning**: This column stores the town or city name for the supplier's address.
- **Role**: Descriptive field for geographical identification.
- **Typical Contents**: Name of the town or city, e.g., "Aschersleben".

### country_code
- **Meaning**: This column stores the ISO country code for the supplier's address.
- **Role**: Descriptive field for country identification.
- **Typical Contents**: Two-letter country code, e.g., "DE".

### created_by
- **Meaning**: This column stores the identifier of the user or system that created the record.
- **Role**: Technical field for tracking record creation.
- **Typical Contents**: Integer representing a user ID.

### created_on
- **Meaning**: This column stores the timestamp of when the record was created.
- **Role**: Technical field for tracking record creation time.
- **Typical Contents**: Timestamp with timezone, e.g., "2021-11-25 11:24:33 UTC".

### last_modified_on
- **Meaning**: This column stores the timestamp of the last modification of the record.
- **Role**: Technical field for tracking the last update time.
- **Typical Contents**: Timestamp with timezone, often left as `None`.

### is_deleted
- **Meaning**: This column indicates whether the record is marked as deleted.
- **Role**: Technical field for soft delete functionality.
- **Typical Contents**: Boolean value, e.g., `False`.

### sub_org_id
- **Meaning**: This column stores an identifier for a sub-organization, if applicable.
- **Role**: Foreign key or identifier for sub-organizations.
- **Typical Contents**: UUID, often left empty.

### id
- **Meaning**: This column stores the unique identifier for the record.
- **Role**: Primary key for the table.
- **Typical Contents**: UUID representing the record.

```
