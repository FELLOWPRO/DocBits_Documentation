# 将供应商和采购订单数据从 CSV 文件导入 DocBits

## 概述

本页介绍如何使用逗号分隔值（.csv）文件将供应商和采购订单数据导入 DocBits。

**重要提示：** 导入任何数据之前，务必**彻底检查 .csv 文件**，以确保数据准确且配置正确。导入错误数据可能导致数据不一致。有关必填字段和可选字段的详细信息，请参阅[**采购订单的 CSV 规范**](importing-supplier-and-purchase-order-data-into-docbits-from-csv-files.md#csv-specifications-for-purchase-order)或[**供应商的 CSV 规范**](importing-supplier-and-purchase-order-data-into-docbits-from-csv-files.md#csv-specifications-for-supplier)部分。如果缺少必填字段，导入过程将失败。

**验证：** 尝试导入之前，请务必根据相应的规范部分检查 .csv 文件是否包含所有必需的列。

## 一般要求：

**日期格式：**

.csv 表格中的所有日期**必须**遵循以下格式：

YYYY-MM-DD HH:MM:SS

**必填字段：**

对于供应商和采购订单导入，相应规范中标记为“必填”的所有列**都必须存在于 .csv 文件中，并且每一行都必须包含相应的值**。如果某一行缺少必填字段或字段值为空，导入过程将失败。

### 采购订单的 CSV 规范 <a id="csv-specifications-for-purchase-order"></a>

**必填字段** -（列名必须存在且必须包含数据）

* `purchase_order_number`

**可包含的字段**

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

### 供应商的 CSV 规范 <a id="csv-specifications-for-supplier"></a>

**必填字段** -（列名必须存在且必须包含数据）

* `customer_number`
* `supplier_number`
* `supplier_name`
* `country_code`

**可包含的字段**

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

## 访问端点

要导入数据，请按以下步骤操作：

1. 访问：[https://api.docbits.com/](https://api.docbits.com/)
2. 点击 **“Authorize”** 按钮。

    <figure><img src="../.gitbook/assets/import_csv_1.png" alt="DocBits API的Swagger页面，default列表已展开并显示healthz Healthz端点"><figcaption></figcaption></figure>
3. 输入 API-Key，然后点击 **“Authorize”**

    * API-Key 可在 DocBits 的 Settings -> Global Settings -> Integration&#x20; 中找到。
    * **注意：** 请求中提供的 API key 决定目标组织，以及导入数据时使用的用户上下文。



    <figure><img src="../.gitbook/assets/import_csv_api.png" alt="DocBits的Settings页面，Global Settings已打开，显示Company Information、Groups Users and Permissions和Integration"><figcaption></figcaption></figure>



    <figure><img src="../.gitbook/assets/import_csv_2.png" alt="Available authorizations对话框，包含APIKeyHeader apiKey条目和X-API-KEY标头值字段" width="563"><figcaption></figcaption></figure>



1. 按 **CTRL + F**（Mac 上按 **CMD + F**）打开搜索功能，然后搜索 `/master_data_lookup/import_data`。
2. 点击该请求以查看详细信息，然后点击 **“Try it out”** 继续。

    <figure><img src="../.gitbook/assets/import_csv_3.png" alt="浏览器查找栏在DocBits API页面上打开，用于搜索import_data端点"><figcaption></figcaption></figure>

    <figure><img src="../.gitbook/assets/import_csv_6.png" alt="Import Data端点页面，包含Try it out按钮以及multipart form-data请求正文字段"><figcaption></figcaption></figure>
3. 现在可以在 Request Body 中输入所需参数。\


    **请求参数：**

    发起导入请求时，需要指定以下参数：

    * **sub\_org\_id：** 删除文本字段中的所有文字，以确保启用“Send empty value”选项。
    * **data\_type：** 此参数指定要导入的数据类型。根据 .csv 文件的内容，可以是 `supplier` 或 `purchase_order`。
    * **replace\_all：** 此布尔参数用于确定是否应在插入 .csv 文件中的新数据之前，删除指定组织相应数据库表（`supplier` 或 `purchase_order`）中的所有现有数据。设为 `true` 可替换所有现有数据；设为 `false` 则追加或使用新数据更新现有数据。
    *   **delimiter：** 此参数指定用于分隔数据文件每一行中各个值的字符。**必须确认文件实际使用的分隔符。**常见分隔符包括逗号（`,`）和分号（`;`）。

        **如何检查分隔符：**

        1. 使用纯文本编辑器（例如 Windows 上的 Notepad、Mac 上的 TextEdit 或类似工具）打开数据文件（例如 `.csv` 文件）。
        2. 检查前几行数据。找到每一行中各项信息之间反复出现的字符。该字符就是分隔符。
        3. 在导入请求中，将 `delimiter` 参数设为识别出的字符（`,` 或 `;`）。使用错误的分隔符会导致数据无法正确解析，导入也会失败。
    * **on\_conflict & auto\_generate\_id：** 目前尚未为这些数据类型实现冲突处理功能（`on_conflict`）和自动生成 ID 功能（`auto_generate_id`）。

    <figure><img src="../.gitbook/assets/import_csv_4.png" alt="Import Data请求正文，包含sub_org_id、data_type、file、delimiter、replace_all、on_conflict和auto_generate_id字段"><figcaption></figcaption></figure>
4. 确认所有信息均正确后，点击 **“Execute”** 按钮即可启动导入过程。

    <figure><img src="../.gitbook/assets/import_csv_5.png" alt="已填写的Import Data请求，data_type为supplier，文件为supplier.csv，on_conflict设置为REPLACE"><figcaption></figcaption></figure>
