# Importing Supplier and Purchase Order Data into DocBits from CSV Files

## Overview

This Page describes how to import Supplier and Purchase Order data into DocBits using a Comma Separated Values (.csv) file.

**Important:** Before importing any data, it is crucial to **review the .csv file thoroughly** to ensure data accuracy and proper configuration. Importing incorrect data can lead to inconsistencies. Refer to the [**CSV Specifications for Purchase Order**](importing-supplier-and-purchase-order-data-into-docbits-from-csv-files.md#csv-specifications-for-purchase-order) or [**CSV Specifications for Supplier**](importing-supplier-and-purchase-order-data-into-docbits-from-csv-files.md#csv-specifications-for-supplier) sections for details on required and optional fields. If required fields are missing, the import process will fail.

**Validation:** Always verify that your .csv file contains all the necessary columns as outlined in the respective specifications section before attempting the import.

## Generall Requirements:

**Date Format:**

All dates provided in the .csv sheet **must** adhere to the following format:

YYYY-MM-DD HH:MM:SS

**Required Fields:**

For both Supplier and Purchase Order imports, all columns marked as "Required" in their respective specifications **must exist in the .csv file and must contain a value in each row**. If any required field is missing or empty for a row, the import process will fail.

### CSV Specifications for Purchase Order

**Fields which are Required** - (column with name must exist & must contain data)

* `purchase_order_number`

**Fields which can be included**

* `warehouse_id`
* `location_id`
* `supplier_id`
* `supplier_name`
* `order_date`
* `requested_shipment_date`
* `promised_delivery_date`
* `payment_terms_code`
* `total_amount`
* `buyer_contact_id`
* `buyer_contact_name`
* `order_last_modified_by`
* `order_last_modified_on`
* `ship_to_party_id`
* `ship_to_party_name`
* `ship_to_address_id`
* `disponent_id`
* `disponent_name`
* `extended_amount`
* `extended_base_amount`
* `extended_report_amount`
* `canceled_amount`
* `canceled_base_amount`
* `canceled_reporting_amount`
* `geo_code`
* `preview_path`
* `type_code`
* `type_description`
* `custom_field_1`
* `custom_field_2`
* `custom_field_3`
* `custom_field_4`
* `custom_field_5`
* `status`
* `line_number`
* `sub_line_number`
* `item_id`
* `supplier_item_id`
* `description`
* `note`
* `quantity`
* `open_quantity`
* `confirmed_quantity`
* `received_quantity`
* `received_base_mou_quantity`
* `promised_delivery_date`
* `requested_ship_date`
* `unit_code`
* `unit_code_price`
* `unit_price`
* `unit_price_per`
* `extended_amount`
* `total_amount`
* `currency`
* `status`
* `buyer_id`
* `buyer_name`
* `geo_code`
* `delivery_method`

### CSV Specifications for Supplier

**Fields which are Required** - (column with name must exist & must contain data)

* `customer_number`
* `supplier_number`
* `supplier_name`
* `country_code`

**Fields which can be included**

* `address_1`
* `address_2`
* `address_3`
* `address_4`
* `town_city`
* `zip_code`
* `supplier_phone`
* `supplier_vat`
* `payment_term_id`
* `payment_method_code`
* `buyer_person_reference_id`
* `buyer_person_reference`
* `supplier_category`
* `supplier_group`
* `discount_term`
* `discount_term_description`
* `bank_id`
* `custom_field_1`
* `custom_field_2`
* `custom_field_3`
* `custom_field_4`
* `custom_field_5`
* `custom_field_6`
* `custom_field_7`
* `custom_field_8`
* `custom_field_9`
* `custom_field_10`
* `status`
* `account_number`
* `financial_partner_id`
* `financial_partner_name`
* `iban`
* `currency`

## Access Endpoint

To import data, follow these steps:

1. Visit: [https://api.docbits.com/](https://api.docbits.com/)
2.  Click the **"Authorize"** button.

    <figure><img src="../.gitbook/assets/import_csv_1.png" alt=""><figcaption></figcaption></figure>
3.  Enter the API-Key and click **"Authorize"**

    * The API-Key can be found in DocBits in Settings -> Global Settings -> Integration&#x20;
    * **Note:** The API key provided in your request determines the target organization and the user context under which the data will be imported.



    <figure><img src="../.gitbook/assets/import_csv_api.png" alt=""><figcaption></figcaption></figure>



    <figure><img src="../.gitbook/assets/import_csv_2.png" alt="" width="563"><figcaption></figcaption></figure>



1. Press **CTRL + F** (or **CMD + F** on Mac) to open the search function, and search for `/master_data_lookup/import_data`.
2.  Click on the request to view its details, then click on "**Try it out"** to proceed.

    <figure><img src="../.gitbook/assets/import_csv_3.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../.gitbook/assets/import_csv_6.png" alt=""><figcaption></figcaption></figure>
3.  You can now enter the required parameters in the Request Body.\


    **Request Parameters:**

    When making the import request, the following parameters need to be specified:

    * **sub\_org\_id:** Remove any text from the text field to ensure the "Send empty value" option is enabled.
    * **data\_type:** This parameter specifies the type of data being imported. It can be either `supplier` or `purchase_order` depending on the content of your .csv file.
    * **replace\_all:** This boolean parameter determines whether all existing data in the respective database table (`supplier` or `purchase_order`) for the specified organization should be deleted before inserting the new data from the .csv file. Set this to `true` to replace all existing data or `false` to append or update with the new data.
    *   **delimiter:** This parameter specifies the character used to separate the individual values within each row of your data file. **It is essential to identify the correct delimiter used in your file.** Common delimiters are the comma (`,`) and the semicolon (`;`).

        **How to check the delimiter:**

        1. Open your data file (e.g., the `.csv` file) with a plain text editor (like Notepad on Windows, TextEdit on Mac, or similar).
        2. Examine the first few rows of data. Look for the character that consistently appears between the different pieces of information in each row. This character is your delimiter.
        3. Set the `delimiter` parameter in your import request to this identified character (either `,` or `;`). Using the wrong delimiter will prevent the data from being parsed correctly and will result in a failed import.
    * **on\_conflict & auto\_generate\_id:** The functionality for handling data conflicts (`on_conflict`) and automatically generating IDs (`auto_generate_id`) is currently **not implemented** for these data types.

    <figure><img src="../.gitbook/assets/import_csv_4.png" alt=""><figcaption></figcaption></figure>
4.  If you have verified that all the information is correct, you can initiate the import process by clicking the **"Execute"** button.

    <figure><img src="../.gitbook/assets/import_csv_5.png" alt=""><figcaption></figcaption></figure>
