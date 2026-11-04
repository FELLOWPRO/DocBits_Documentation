# public.sales\_order

## Tabelle `public.sales_order`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `location_id`: internal
* `order_number`: internal
* `customer_purchase_order`: internal
* `customer_id`: internal
* `customer_name`: internal
* `warehouse_id`: internal
* `warehouse_name`: internal
* `transportation_method`: internal
* `requested_delivery_date`: timestamp with time zone
* `order_date`: timestamp with time zone
* `sales_person_id`: internal
* `sales_person_name`: internal
* `ship_to_party_id`: internal
* `ship_to_party_name`: internal
* `ship_to_party_city`: internal
* `ship_to_party_state`: internal
* `ship_to_party_country`: internal
* `ship_to_party_zip`: internal
* `status`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `preview_path`: internal
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse & Beschreibung

## Technical Documentation for `public.sales_order` Table

### Introduction

The `public.sales_order` table is designed to capture and store information related to sales orders within a business context. This includes details about the order, the customer, the logistics, and various metadata associated with the order's lifecycle. The table serves as a central repository for tracking the status and history of sales transactions.

### Column Descriptions

#### id

* **Meaning**: Unique identifier for each sales order.
* **Role**: Primary key.
* **Typical Contents**: A UUID string (e.g., `'6ffe4673-7563-44dc-8e71-855e8f25534a'`).

#### org\_id

* **Meaning**: Identifier for the organization that created the sales order.
* **Role**: Foreign key.
* **Typical Contents**: A UUID string representing the organization (e.g., `'23f3d697-7411-4c95-981d-faf089d266be'`).

#### sub\_org\_id

* **Meaning**: Identifier for a sub-organization, if applicable.
* **Role**: Foreign key.
* **Typical Contents**: May be `NULL` if not applicable.

#### location\_id

* **Meaning**: Identifier for the location associated with the sales order.
* **Role**: Foreign key.
* **Typical Contents**: A string code representing a location (e.g., `'028'`).

#### order\_number

* **Meaning**: Unique number assigned to the sales order.
* **Role**: Technical field for order tracking.
* **Typical Contents**: A string (e.g., `'0010174175'`).

#### customer\_purchase\_order

* **Meaning**: Reference number for the customer's purchase order.
* **Role**: Technical field for cross-referencing.
* **Typical Contents**: A string (e.g., `'1YFNC3'`).

#### customer\_id

* **Meaning**: Identifier for the customer placing the order.
* **Role**: Foreign key.
* **Typical Contents**: A string code (e.g., `'35623000'`).

#### customer\_name

* **Meaning**: Name of the customer.
* **Role**: Descriptive field.
* **Typical Contents**: A string (e.g., `'DOLLAR GENERAL'`).

#### warehouse\_id

* **Meaning**: Identifier for the warehouse responsible for fulfilling the order.
* **Role**: Foreign key.
* **Typical Contents**: A string code (e.g., `'028'`).

#### warehouse\_name

* **Meaning**: Name of the warehouse.
* **Role**: Descriptive field.
* **Typical Contents**: A string (e.g., `'USCS - DENTON, TX'`).

#### transportation\_method

* **Meaning**: Method of transportation for delivering the order.
* **Role**: Descriptive field.
* **Typical Contents**: A string code (e.g., `'001'`).

#### requested\_delivery\_date

* **Meaning**: Date the customer requested for delivery.
* **Role**: Descriptive field.
* **Typical Contents**: A timestamp (e.g., `None`).

#### order\_date

* **Meaning**: Date when the order was placed.
* **Role**: Descriptive field.
* **Typical Contents**: A timestamp (e.g., `datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`).

#### sales\_person\_id

* **Meaning**: Identifier for the salesperson handling the order.
* **Role**: Foreign key.
* **Typical Contents**: A string (e.g., `'ROBERTDOCK'`).

#### sales\_person\_name

* **Meaning**: Name of the salesperson.
* **Role**: Descriptive field.
* **Typical Contents**: A string (e.g., `'ROBERT DOCKINS'`).

#### ship\_to\_party\_id

* **Meaning**: Identifier for the party to whom the order is shipped.
* **Role**: Foreign key.
* **Typical Contents**: A string (e.g., `'35623000 009'`).

#### ship\_to\_party\_name

* **Meaning**: Name of the party to whom the order is shipped.
* **Role**: Descriptive field.
* **Typical Contents**: A string (e.g., `'DOLLAR GENERAL DC 98061/96460'`).

#### ship\_to\_party\_city

* **Meaning**: City of the shipping address.
* **Role**: Descriptive field.
* **Typical Contents**: A string (e.g., `'SAN ANTONIO'`).

#### ship\_to\_party\_state

* **Meaning**: State of the shipping address.
* **Role**: Descriptive field.
* **Typical Contents**: May be `NULL`.

#### ship\_to\_party\_country

* **Meaning**: Country of the shipping address.
* **Role**: Descriptive field.
* **Typical Contents**: A string (e.g., `'US'`).

#### ship\_to\_party\_zip

* **Meaning**: ZIP code of the shipping address.
* **Role**: Descriptive field.
* **Typical Contents**: A string (e.g., `'78218'`).

#### status

* **Meaning**: Current status of the sales order.
* **Role**: Descriptive field.
* **Typical Contents**: A string (e.g., `'Allocated'`).

#### created\_by

* **Meaning**: Identifier of the user who created the entry.
* **Role**: Technical field.
* **Typical Contents**: An integer (e.g., `1`).

#### created\_on

* **Meaning**: Timestamp when the entry was created.
* **Role**: Technical field.
* **Typical Contents**: A timestamp (e.g., `datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`).

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification.
* **Role**: Technical field.
* **Typical Contents**: A timestamp (e.g., `datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`).

#### is\_deleted

* **Meaning**: Flag indicating if the order is marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: A boolean (e.g., `False`).

#### deleted\_on

* **Meaning**: Timestamp when the order was marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Default date if not deleted (e.g., `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`).

#### preview\_path

* **Meaning**: Path to a preview document for the sales order.
* **Role**: Descriptive field.
* **Typical Contents**: A string representing a file path (e.g., `'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`).

#### last\_modified\_by

* **Meaning**: Identifier of the user who last modified the entry.
* **Role**: Technical field.
* **Typical Contents**: May be `NULL`.

#### deleted\_by

* **Meaning**: Identifier of the user who marked the entry as deleted.
* **Role**: Technical field.
* **Typical Contents**: May be `NULL`.
