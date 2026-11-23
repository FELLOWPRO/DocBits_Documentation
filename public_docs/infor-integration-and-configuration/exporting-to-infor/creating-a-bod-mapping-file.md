# Creating a BOD Mapping File

Download a BOD Mapping File and open it in your applicable file editor of choice to edit it. For this walkthrough, VSCode is used.

## Editing Mapping File

Change the company to the correct one (SFV\_AccountingEntityID) and edit location ID if needed.

![BOD mapping file text with SFV_AlternateDocLocation, SFV_LogicalID, SFV_AccountingEntityID and Document_Types lines highlighted](https://lh7-us.googleusercontent.com/eJQI1CKlxEkS\_Pwp0VH2hgS220b-q8NSFG5iJKpLOL457qTN3CbUB8IHTw1lRinbB\_kP00UUNgepWNsbh3\_Ko-SExObePjqmxP7ee\_lQnADTtDmxEtRM\_S7AONMbcpjwtnHTakYd1Q06GVm2G0o-UDA)

Check the document code by going to the field settings of the document type you are trying to export (found in URL of field settings of document type in DocBits like below

![Browser address bar on sandbox.docbits.com settings/fields/INVOICE with the INVOICE part highlighted above the Document Types header](https://lh7-us.googleusercontent.com/AhU3i27qFS7BMCgpNQnmLWAjcIWHXHOlxMKqd2Yob5RQKa8qysQQsSsacr6zao4cnAh3DISPgYu1GnjubIJpgtAdiBR\_0vy3WJZXPY-HeEfVQkWnlRI9UEJWMPQ7DbWYLQhz339BOlbd4KgxU9B\_CPE)

Lastly, edit the SFV\_LogicalID which can be found in INFOR ION DESK → Connect → Connection points and select the DocBits\_Export or similar connection point and within that page you will find the Logical ID you need.

![ION Desk Connection Points page with the DocBits-Prod-Export connection point card (Active) highlighted](https://lh7-us.googleusercontent.com/f50i7pzRuZULJ6shehba0lWIWFBTsPZyip-LQxAYJpYDXK66SlzdGOpdEG-wqLQfqXMgMMhm5SAvj57UOCvF6xf2OMCXtFiEEKr9yiQr4xtv8vbV-NGcLuJwuQ9zHMBBKfTktAp1nSfBJhdPeAu3RWc)

![ION connection point DocBits-Prod-Export details with the Logical ID infor.ims.docbits-prod-export highlighted](https://lh7-us.googleusercontent.com/qyEt4iYRIjOZCCrVbImeK6EdZGun2YrAy8li8u3tulcD8bwzl\_sl1TiEXKqbik-4MxnbV\_MCwltvuA2WAgzzvDpTVd7W52he9QD9IK0qijoz3ZihUYcWJlqlD5kbcsRTj3SfP1CDqcyhoFfBeiE1Xfo)

## Create Logical ID (Connection Point)

If this Connection Point does not yet exist, you need to create one.

First, go to ION Desk → Connect → Connection Points and click on the “+ Add” button”

![ION Desk Connection Points page with the Add tile highlighted](https://lh7-us.googleusercontent.com/fQPmV8KgffyWhM0i0cQlyh7fyQe37p8uR6C\_pVD5SboEx2emIJX2212GXqk\_KT71DfYMKSjkfYFFTARqgLLxoOPNQFXHxUOo9vMXH2pmDN469VgbQkV-JjRtCevZJsbvS8vbfUtasN83xN25tX6\_S5U)

Then select the “IMS via API Gateway” option

![ION Desk Connection Points page with the Add menu open and IMS via API Gateway highlighted under Infor](https://lh7-us.googleusercontent.com/uPLiiLHp6Z3jPCzYBOzHVuI8sGY5XQuUfv66fZYH0HndSBL7yvzFHh3lJjEMxteJfXsVMhUe3U\_38xZHDRFSn0jeiMZUQBJJLzZ2oaIQAixY7wUPd6D0PJwg7wvC8XBeZxPmjNoiUvP3ImoG\_aOhFmY)

![Empty Infor Application Connection Point (IMS via API Gateway) form with Name, Description, Logical ID and IMS Endpoint fields](https://lh7-us.googleusercontent.com/VhyMDEuglPfxeX-3cATu6ZFB\_Mz2Y7C-yJ99EvBvrhD8IoVzGd4ksjrWAE0mIPub2PX5\_Zua10ZHQeWI82QbJ8ZgJKN-tVpVrYGvMdfQOj3Uco5efsPT6JYkDyPu\_lkeR9aTGhh5-q2bzZztXuTUixM)

You will be taken to the above screen where you must now fill in the necessary information, the name should be something like “DocBits\_export” or similar.

For “ION API Client ID” you enter the same Client ID you obtained earlier for the ION Mapping File.

Then select the Document tab of the Connection Point creation menu and add the following documents by pressing the “+” sign, this will only become useful later.

![Connection point DocBits-Sandbox-Export on the Documents tab listing Sync.CaptureDocument as sent from application](https://lh7-us.googleusercontent.com/GtHlTliePV-JIDLP9YNGlXELKuWIU2VSlUt4mvWO4q\_XM54MSL9zTmtxPMdeOl24VFtNC0pQ-nbXyHb9PaeMkKvgzpCOo5kLdL3A8Bw54ILniwIdTyfxFhPuzRUGKs2hRi5ioKvfkdsPMgq4x6EHOtM)

Once you save this Connection Point you will obtain the Logical ID as shown below

![Connection point DocBits-Sandbox form with the Logical ID infor.ims.docbits-sandbox highlighted](https://lh7-us.googleusercontent.com/P7cihsQT2Qcq\_XGL08dTV2jHMUK7YCMQyXsJudkVDXDh73GZ-hS61IoAKSHptPyX4C5e\_xPKP0yZGzpQOwCFw6BppPlzZuFWZ\_VGIrOUmJH2egxaCEXMoVBHBM6lkZeb3gPYWYdMYpuNqFFPC-4Qol0)

Then insert this Logical ID into the appropriate section of the BOD Mapping File and save the file.

## Tables in the BOD

The BOD can carry tables in `CaptureDocument/DocumentTable`. Each table row is a `Row`, and each value in it is a `Column` with a `Name` and a `Value`. The column names are free text, so use the names the system that reads the BOD expects.

`Table_COMMON_PATH` sets where tables are written, `TableColumn_MappedFields` and the `TCP_` keys set how a column is built, and `Tables` lists the tables to export. Each table then maps its columns with `TN_<table>_TC_<DOCBITS_COLUMN>=<BOD column name>`. Only mapped columns are exported, and an empty value is left out.

### Export the auto-accounting lines

By default a table exports the document's line items. To export the auto-accounting lines (GL account, dimensions, voucher text, amount) instead, add a table whose source is `accounting`:

```properties
Tables=InvoiceTable,AccountingTable
TN_AccountingTable_Source=accounting
TN_AccountingTable_TC_POSITION=Position
TN_AccountingTable_TC_LEDGER_ACCOUNT=AccountingLine_Dim1
TN_AccountingTable_TC_DIMENSION_2=AccountingLine_Dim2
TN_AccountingTable_TC_DIMENSION_3=AccountingLine_Dim3
TN_AccountingTable_TC_VOUCHER_TEXT=AccountingLine_VoucherText
TN_AccountingTable_TC_AMOUNT=ExtendedAmount
TN_AccountingTable_TC_TAX_CODE=TaxCode
TN_AccountingTable_Static_Fields=nameLanguageID,name
TNP_AccountingTable_nameLanguageID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable\\Name\\languageID
TNV_AccountingTable_nameLanguageID=en-us
TNP_AccountingTable_name=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable\\Name
TNV_AccountingTable_name=AccountingRows
```

The accounting table is written as its own `DocumentTable`, after the invoice table:

```xml
<DocumentTable>
  <Name languageID="en-us">AccountingRows</Name>
  <Row>
    <ID>1</ID>
    <Column><Name languageID="en-us">AccountingLine_Dim1</Name><Value>6300</Value></Column>
    <Column><Name languageID="en-us">ExtendedAmount</Name><Value>59.40</Value></Column>
  </Row>
</DocumentTable>
```

The rows are the same accounting lines the Infor M3 and LN API exports send: one row per accounting line, and one row per split of a split line. Each row can use these values:

| DocBits value | Content |
| --- | --- |
| `LEDGER_ACCOUNT` | GL account |
| `DIMENSION_<id>` | Accounting dimension, for example `DIMENSION_2` |
| `AMOUNT` | Line amount |
| `VOUCHER_TEXT` | Voucher text |
| `TAX_CODE`, `TAX_COUNTRY` | Tax code and tax country |
| `QUANTITY`, `QUANTITY2` | Quantities |
| `POSITION` | Position of the accounting line |
| `BOOKING_REFERENCE` | Booking reference |

Fields added through the `AUTO_ACCOUNTING_FIELDS` preference can be mapped the same way, by their field name.

* A document gets the accounting table only when its auto accounting has lines.
* `TN_<table>_PATH` places a table somewhere other than `Table_COMMON_PATH`.
* Table values longer than 30 characters are cut. Set `TableColumn_MaxLength` to a larger width, or to `0` for no limit. The setting applies to every table in the mapping.
* The column names in the example follow the Infor M3 accounting line (line type 8): `AccountingLine_Dim1` to `AccountingLine_Dim7`, with dimension 1 as the GL account. Use the names the receiving system expects.

## Upload File to DocBits

Drag and drop the file into your export configuration in DocBits. This is available at Settings → Export.

![DocBits Export Settings with the Infor ION dialog open and the BOD Mapping File field highlighted](https://lh7-us.googleusercontent.com/AqCo7QgC-kaAxbaIJD8MYeKGLBXbwGVJPGx9\_2yfUp3R2MYxJPowVAjnO80uxQ9qMDxNoXy1eY3WH-mEpaeWwatwi91edm\_0lS9Hg93FSAjQGtDAR5y7Ptce-ARfetSiXIBJKiGwujSggVXXHUhG77U)


