---
description: India GST E-Invoice electronic document support in DocBits
---

# 🇮🇳 INDIA GST E-INVOICE

| Property             | Value                                              |
| -------------------- | -------------------------------------------------- |
| **Country / Region** | India                                              |
| **Document Types**   | Invoice (INV), Credit Note (CRN), Debit Note (DBN) |
| **Format**           | XML (`<SignedInvoice>`)                            |
| **Standard**         | GST E-Invoice (GSTN Invoice Registration Portal)   |
| **Locale**           | `en_IN`                                            |

India GST E-Invoice is the mandatory electronic invoice standard under India's Goods and Services Tax (GST) regime, operated by GSTN (GST Network). Businesses above the prescribed turnover threshold must generate e-Invoices through the Invoice Registration Portal (IRP), which signs the invoice and returns an **IRN** (Invoice Reference Number — a 64-character SHA-256 hash) and a QR code.

DocBits detects GST E-Invoice documents by the presence of `<SignedInvoice>` as the root element. The format includes three GST tax components:

| Tax Component | Description                                                           |
| ------------- | --------------------------------------------------------------------- |
| IGST          | Integrated GST — applied on inter-state transactions                  |
| CGST          | Central GST — applied on intra-state transactions (Central component) |
| SGST          | State GST — applied on intra-state transactions (State component)     |

The taxpayer identifier is the **GSTIN** (Goods and Services Tax Identification Number), a 15-character alphanumeric code in the format `29AABCU9603R1ZM` (2-digit state code + 10-digit PAN + entity number + check digit). Dates use the `DD/MM/YYYY` format.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/india-gst-e-invoice-preview.png" alt="India GST E-Invoice preview in DocBits"><figcaption><p>Default DocBits preview for an India GST E-Invoice</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field          | Source XML Element                                | Notes                                           |
| ---------------------- | ------------------------------------------------- | ----------------------------------------------- |
| `invoice_id`           | `Invoice/DocDtls/No`                              | Invoice number                                  |
| `invoice_date`         | `Invoice/DocDtls/Dt`                              | Issue date (`DD/MM/YYYY`)                       |
| `invoice_type`         | `Invoice/DocDtls/Typ`                             | INV=Invoice, CRN=Credit Note, DBN=Debit Note    |
| `currency`             | Fixed: `INR`                                      | Always Indian Rupee                             |
| `net_amount`           | `Invoice/ValDtls/AssVal`                          | Assessable / taxable value                      |
| `tax_amount`           | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Total GST amount                                |
| `total_amount`         | `Invoice/ValDtls/TotInvVal`                       | Total invoice value incl. GST                   |
| `igst_amount`          | `Invoice/ValDtls/IgstVal`                         | Integrated GST amount                           |
| `cgst_amount`          | `Invoice/ValDtls/CgstVal`                         | Central GST amount                              |
| `sgst_amount`          | `Invoice/ValDtls/SgstVal`                         | State GST amount                                |
| `cess_amount`          | `Invoice/ValDtls/CesVal`                          | Cess amount (if applicable)                     |
| `supplier_name`        | `Invoice/SellerDtls/LglNm`                        | Seller legal name                               |
| `supplier_id`          | `Invoice/SellerDtls/Gstin`                        | Seller GSTIN (15 chars, e.g. `29AABCU9603R1ZM`) |
| `supplier_trade_name`  | `Invoice/SellerDtls/TrdNm`                        | Seller trade name                               |
| `supplier_address`     | `Invoice/SellerDtls/Addr1`                        | Seller address line 1                           |
| `supplier_city`        | `Invoice/SellerDtls/Loc`                          | Seller city / location                          |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin`                          | Seller PIN code                                 |
| `supplier_state_code`  | `Invoice/SellerDtls/Stcd`                         | Seller state code (2 digits)                    |
| `buyer_name`           | `Invoice/BuyerDtls/LglNm`                         | Buyer legal name                                |
| `buyer_id`             | `Invoice/BuyerDtls/Gstin`                         | Buyer GSTIN                                     |
| `buyer_trade_name`     | `Invoice/BuyerDtls/TrdNm`                         | Buyer trade name                                |
| `buyer_address`        | `Invoice/BuyerDtls/Addr1`                         | Buyer address line 1                            |
| `buyer_city`           | `Invoice/BuyerDtls/Loc`                           | Buyer city / location                           |
| `buyer_postal_code`    | `Invoice/BuyerDtls/Pin`                           | Buyer PIN code                                  |
| `buyer_state_code`     | `Invoice/BuyerDtls/Stcd`                          | Buyer state code                                |
| `irn`                  | `Irn`                                             | Invoice Reference Number (64-char SHA-256 hash) |
| `ack_number`           | `AckNo`                                           | IRP acknowledgement number                      |
| `ack_date`             | `AckDt`                                           | IRP acknowledgement date                        |

### Line Item Table (`INVOICE_TABLE`)

Row path: `Invoice/ItemList/Item`

| Column        | Source XML Element                   | Notes                                      |
| ------------- | ------------------------------------ | ------------------------------------------ |
| `POSITION`    | `SlNo`                               | Line sequence number                       |
| `DESCRIPTION` | `PrdDesc`                            | Product / service description              |
| `QUANTITY`    | `Qty`                                | Invoiced quantity                          |
| `UNIT`        | `Unit`                               | Unit of measure (e.g. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE`  | `UnitPrice`                          | Unit price                                 |
| `VAT_RATE`    | `GstRt`                              | GST rate in % (e.g. 18%)                   |
| `VAT`         | `IgstAmt` (or `CgstAmt` + `SgstAmt`) | GST amount per line                        |
| `NET_AMOUNT`  | `AssAmt`                             | Assessable amount per line                 |

## Classification Rule

DocBits detects India GST E-Invoice documents by matching the root element:

| Electronic Document Type | Pattern                                |
| ------------------------ | -------------------------------------- |
| INDIA GST E-INVOICE      | Root element contains `<SignedInvoice` |

## Related

* [Currently Supported E-Invoice Standards](../../currently-supported-e-invoice-standards/)
* [Supported Electronic Documents](./)
