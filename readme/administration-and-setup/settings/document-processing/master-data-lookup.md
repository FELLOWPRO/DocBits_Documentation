# Master Data Lookup

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}

**Master Data Lookup** (sidebar: **Lookup Master Data**) lets you view and manage the master data that DocBits uses to validate extracted document data against your ERP system. It is essential for accurate PO matching, supplier validation and field auto-completion. Open it from **Settings → Document Processing → Lookup Master Data**.

<figure><img src="../../../.gitbook/assets/master_data_lookup_overview.png" alt="Master Data Lookup"><figcaption><p>Master Data Lookup page — data sources and the data table</p></figcaption></figure>

## Data Sources

The left panel lists four data-source categories:

| Source | Description |
|--------|-------------|
| **BOD Input Data** | Data received via Infor BOD (Business Object Document) messages. |
| **ERP API Data** | Data fetched directly from your ERP system via API. Click the gear icon to configure the API connection. |
| **Imported** | Manually imported data (for example via CSV upload). Click the **+** icon to add new data. |
| **DocBits Master Data** | Internal master data managed within DocBits. |

## Data Table

Selecting a data source opens its data in a searchable, sortable table on the right:

* **Tabs** — each tab is a master-data type (for example Supplier, Purchase Order, Item).
* **Search** — filter by column (**Search by column**) or search by text (**Search String**).
* **Actions** — update column labels, hide empty columns, update aliases, or download the data as CSV.
* **Pagination** — navigate large datasets with the page controls.

The Supplier and Purchase Order tables include columns such as Supplier ID, Supplier Name, Address, Bank Id, PO Number, Item ID, Description, Quantity, Unit Price, Total Amount, Currency and Status, plus any custom fields.

## Settings

Click **Settings** (gear icon) at the bottom-left of the data-sources panel to open the master-data settings.

<figure><img src="../../../.gitbook/assets/master_data_lookup_settings.png" alt="Master Data Lookup settings"><figcaption><p>Supplier BOD and Purchase Order Deletion settings</p></figcaption></figure>

### Supplier BOD

**Allow Multiple Supplier Accounts Sync**

* **Enabled**: a single supplier may have multiple `<FinancialParty>` elements in the BOD (often due to multiple IBANs or financial accounts). All `<FinancialParty>` entries are extracted and saved to the supplier table, so multiple financial attributes can be stored.
* **Disabled**: only the last `<FinancialParty>` element found for the supplier is extracted. Earlier financial attributes (for example additional IBANs) are ignored, and only the data from the last occurrence is saved.

### Purchase Order Deletion Assistant

**Delete Purchase Order After** — choose when closed purchase orders should be removed. After the selected time span, the records are deleted automatically.

{% hint style="info" %}
To learn how to load master data into DocBits, see [Import Master Data](../../../infor-integration-and-configuration/importing-customer-master-data/).
{% endhint %}
