# public.purchase\_order\_line

## Tabelle `public.purchase_order_line`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `purchase_order_id`: internal
* `purchase_order_number`: internal
* `line_number`: internal
* `item_id`: internal
* `supplier_item_id`: internal
* `description`: internal
* `quantity`: double precision
* `unit_code`: internal
* `unit_price`: double precision
* `total_amount`: double precision
* `currency`: internal
* `status`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `open_quantity`: double precision
* `received_quantity`: double precision
* `confirmed_quantity`: double precision
* `note`: text
* `sub_org_id`: internal
* `sub_line_number`: internal
* `unit_price_per`: double precision
* `buyer_id`: internal
* `buyer_name`: internal
* `unit_code_price`: internal
* `geo_code`: internal
* `promised_delivery_date`: timestamp with time zone
* `delivery_method`: internal
* `requested_ship_date`: date
* `received_base_mou_quantity`: double precision
* `extended_amount`: double precision

### Analyse & Beschreibung

## Technical Documentation for `public.purchase_order_line` Table

### Introduction

The `public.purchase_order_line` table is designed to store detailed information about each line item within a purchase order. It captures various attributes of a purchase order line such as item details, quantities, prices, and statuses. This table is integral for managing and tracking purchase orders and their fulfillment status within an organizational context.

### Column Descriptions

#### id

* **Meaning**: Unique identifier for each purchase order line item.
* **Role**: Primary Key.
* **Typical Contents**: A UUID string uniquely identifying the purchase order line.

#### org\_id

* **Meaning**: Identifier for the organization associated with the purchase order.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID string referencing an organization.

#### purchase\_order\_id

* **Meaning**: Identifier for the purchase order to which the line item belongs.
* **Role**: Foreign Key.
* **Typical Contents**: A UUID string referencing a purchase order.

#### purchase\_order\_number

* **Meaning**: The number assigned to the purchase order.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing the purchase order number.

#### line\_number

* **Meaning**: The line number of the item within the purchase order.
* **Role**: Descriptive field.
* **Typical Contents**: A string denoting the line sequence in the purchase order.

#### item\_id

* **Meaning**: Identifier for the item being ordered.
* **Role**: Foreign Key.
* **Typical Contents**: A string representing the item code.

#### supplier\_item\_id

* **Meaning**: Supplier-specific identifier for the item.
* **Role**: Descriptive field.
* **Typical Contents**: A string, may be null if not provided by the supplier.

#### description

* **Meaning**: Description of the item.
* **Role**: Descriptive field.
* **Typical Contents**: A text description of the item.

#### quantity

* **Meaning**: The number of units ordered.
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value indicating ordered quantity.

#### unit\_code

* **Meaning**: Code representing the unit of measurement for the item.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing units, e.g., 'EA' for each.

#### unit\_price

* **Meaning**: Price per unit of the item.
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value representing the price per unit.

#### total\_amount

* **Meaning**: Total amount for the line item (quantity \* unit price).
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value representing the total amount.

#### currency

* **Meaning**: Currency in which the purchase is made.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing the currency code, e.g., 'USD'.

#### status

* **Meaning**: Current status of the purchase order line.
* **Role**: Descriptive field.
* **Typical Contents**: A string indicating status, e.g., 'Received', 'Invoiced'.

#### created\_by

* **Meaning**: Identifier for the user who created the entry.
* **Role**: Foreign Key.
* **Typical Contents**: An integer representing the user ID.

#### created\_on

* **Meaning**: Timestamp of when the entry was created.
* **Role**: Technical field.
* **Typical Contents**: A timestamp with timezone information.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification.
* **Role**: Technical field.
* **Typical Contents**: A timestamp with timezone information, may be null if never modified.

#### deleted\_on

* **Meaning**: Timestamp of when the entry was marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: A timestamp with timezone information, may be null if not deleted.

#### is\_deleted

* **Meaning**: Indicates if the entry has been marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Boolean value (true/false).

#### open\_quantity

* **Meaning**: Quantity not yet received or invoiced.
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value, typically zero if fully received.

#### received\_quantity

* **Meaning**: Quantity that has been received.
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value indicating received quantity.

#### confirmed\_quantity

* **Meaning**: Quantity confirmed by supplier.
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value, may be null if not confirmed.

#### note

* **Meaning**: Additional notes regarding the purchase order line.
* **Role**: Descriptive field.
* **Typical Contents**: Text, may include special instructions or comments.

#### sub\_org\_id

* **Meaning**: Identifier for the sub-organization associated with the purchase order line.
* **Role**: Foreign Key.
* **Typical Contents**: A string, potentially null if not applicable.

#### sub\_line\_number

* **Meaning**: Sub-line number within the purchase order.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing sub-line sequence.

#### unit\_price\_per

* **Meaning**: Base unit price for the item.
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value representing the base unit price.

#### buyer\_id

* **Meaning**: Identifier for the buyer responsible for the purchase.
* **Role**: Foreign Key.
* **Typical Contents**: A string representing the buyer ID.

#### buyer\_name

* **Meaning**: Name of the buyer responsible.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing the buyer's name.

#### unit\_code\_price

* **Meaning**: Unit code related to pricing.
* **Role**: Descriptive field.
* **Typical Contents**: A string, similar to unit\_code.

#### geo\_code

* **Meaning**: Geographical code for delivery.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing a geographic location.

#### promised\_delivery\_date

* **Meaning**: Date promised for delivery.
* **Role**: Descriptive field.
* **Typical Contents**: A timestamp with timezone information.

#### delivery\_method

* **Meaning**: Method of delivery for the purchase order line.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing delivery method.

#### requested\_ship\_date

* **Meaning**: Date requested for shipment.
* **Role**: Descriptive field.
* **Typical Contents**: A date value.

#### received\_base\_mou\_quantity

* **Meaning**: Quantity received in base measurement units.
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value indicating base MOU quantity received.

#### extended\_amount

* **Meaning**: Extended amount for the line item.
* **Role**: Descriptive field.
* **Typical Contents**: A numeric value representing the extended amount, which may be equal to total\_amount if no discounts or additional charges apply.
