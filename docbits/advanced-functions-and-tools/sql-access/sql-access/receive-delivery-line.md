# Receive delivery line

## Table `public.receive_delivery_line`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `receive_delivery_id`: internal
* `delivery_number`: internal
* `line_number`: internal
* `item_id`: internal
* `description`: internal
* `shipped_quantity`: double precision
* `status`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `purchase_order`: internal
* `sequence_number`: internal
* `sub_org_id`: internal
* `shipped_quantity_unit_code`: internal
* `packing_slip_quantity`: double precision
* `packing_slip_quantity_unit_code`: internal
* `received_quantity`: double precision
* `received_quantity_unit_code`: internal
* `purchase_order_line_number`: internal
* `status_effective_from`: timestamp with time zone
* `purchase_order_sub_line_number`: internal
* `invoiced_quantity`: double precision
* `invoice_matching_status`: internal
* `open_quantity`: double precision
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse & Beschreibung

## Table Documentation: `public.receive_delivery_line`

### Introduction

The `public.receive_delivery_line` table appears to be a detailed record of delivery and receipt lines associated with an organization's logistics and supply chain operations. Each row in the table represents a specific line item in a delivery, capturing details such as the item description, quantities shipped and received, and various status fields. The table serves as a vital component in tracking the movement of goods from shipment to receipt, including invoicing and order management.

### Column Descriptions

#### id

* **Meaning**: Unique identifier for each delivery line item.
* **Role**: Primary Key.
* **Typical Contents**: A unique universally unique identifier (UUID).

#### org\_id

* **Meaning**: Identifier for the organization associated with the delivery.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID representing the organization.

#### receive\_delivery\_id

* **Meaning**: Identifier linking to the overall delivery transaction.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID associated with a specific delivery transaction.

#### delivery\_number

* **Meaning**: Unique number assigned to the delivery.
* **Role**: Reference Field.
* **Typical Contents**: A string representing the delivery number.

#### line\_number

* **Meaning**: Specific line number within a delivery.
* **Role**: Reference Field.
* **Typical Contents**: Numeric string indicating the sequence of the line.

#### item\_id

* **Meaning**: Identifier for the item being shipped.
* **Role**: Reference Field.
* **Typical Contents**: A numeric string corresponding to an item.

#### description

* **Meaning**: Description of the item.
* **Role**: Descriptive Field.
* **Typical Contents**: Textual description of the item, e.g., "FLOUR, WHEAT, UN-BLEACHED ENRICHED, BULK".

#### shipped\_quantity

* **Meaning**: Quantity of the item that was shipped.
* **Role**: Quantitative Field.
* **Typical Contents**: A decimal number indicating the amount shipped.

#### status

* **Meaning**: Current status of the delivery line item.
* **Role**: Status Field.
* **Typical Contents**: Text such as "Received".

#### created\_by

* **Meaning**: Identifier for the user or system that created the record.
* **Role**: Audit Field.
* **Typical Contents**: Integer representing a user ID.

#### created\_on

* **Meaning**: Timestamp when the record was created.
* **Role**: Audit Field.
* **Typical Contents**: Date and time with time zone.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification.
* **Role**: Audit Field.
* **Typical Contents**: Date and time with time zone.

#### deleted\_on

* **Meaning**: Timestamp when the record was marked as deleted.
* **Role**: Audit Field.
* **Typical Contents**: Date and time with time zone, often null unless deleted.

#### is\_deleted

* **Meaning**: Indicates if the record is marked as deleted.
* **Role**: Technical Field.
* **Typical Contents**: Boolean value, true or false.

#### purchase\_order

* **Meaning**: Reference to the associated purchase order.
* **Role**: Reference Field.
* **Typical Contents**: Alphanumeric string representing a purchase order number.

#### sequence\_number

* **Meaning**: Sequence number for the delivery line.
* **Role**: Reference Field.
* **Typical Contents**: Numeric string, often null.

#### sub\_org\_id

* **Meaning**: Identifier for a sub-organization involved.
* **Role**: Foreign Key.
* **Typical Contents**: UUID, often null.

#### shipped\_quantity\_unit\_code

* **Meaning**: Unit of measurement for shipped quantity.
* **Role**: Reference Field.
* **Typical Contents**: Code representing units, e.g., "LBP".

#### packing\_slip\_quantity

* **Meaning**: Quantity as per the packing slip.
* **Role**: Quantitative Field.
* **Typical Contents**: Decimal number, often null.

#### packing\_slip\_quantity\_unit\_code

* **Meaning**: Unit code for the packing slip quantity.
* **Role**: Reference Field.
* **Typical Contents**: Code representing units, often null.

#### received\_quantity

* **Meaning**: Quantity of items actually received.
* **Role**: Quantitative Field.
* **Typical Contents**: Decimal number indicating the amount received.

#### received\_quantity\_unit\_code

* **Meaning**: Unit code for received quantity.
* **Role**: Reference Field.
* **Typical Contents**: Code representing units, e.g., "LBP".

#### purchase\_order\_line\_number

* **Meaning**: Line number within the purchase order.
* **Role**: Reference Field.
* **Typical Contents**: Numeric string.

#### status\_effective\_from

* **Meaning**: The date and time from when the status is effective.
* **Role**: Status Field.
* **Typical Contents**: Date and time with time zone, often null.

#### purchase\_order\_sub\_line\_number

* **Meaning**: Sub-line number within the purchase order.
* **Role**: Reference Field.
* **Typical Contents**: Numeric string, often "000".

#### invoiced\_quantity

* **Meaning**: Quantity that has been invoiced.
* **Role**: Quantitative Field.
* **Typical Contents**: Decimal number.

#### invoice\_matching\_status

* **Meaning**: Status of the invoice matching process.
* **Role**: Status Field.
* **Typical Contents**: Textual status code, e.g., "9.0".

#### open\_quantity

* **Meaning**: Quantity that remains open or not yet processed.
* **Role**: Quantitative Field.
* **Typical Contents**: Decimal number.

#### last\_modified\_by

* **Meaning**: Identifier for the user who last modified the record.
* **Role**: Audit Field.
* **Typical Contents**: UUID of the user, often null.

#### deleted\_by

* **Meaning**: Identifier for the user who marked the record as deleted.
* **Role**: Audit Field.
* **Typical Contents**: UUID of the user, often null.
