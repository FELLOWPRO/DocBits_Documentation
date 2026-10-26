---
hidden: true
noIndex: true
---

# Legacy M3 setup (archived)

This page used to offer a connection-point XML template tied to a DocBits development logical ID. It is not a reusable template for a customer or production environment. Do not import it into Infor ION: an incorrect logical ID or service account can route data to the wrong destination.

Use the current, tenant-specific guides instead:

* [M3 integration overview](m3/README.md) — choose the integration path for your environment.
* [Suppliers and Purchase Orders](m3/suppliers-and-purchase-orders.md) — review the ION route and verify delivered records.
* [Start a supplier initial load](m3/how-to-import-all-suppliers.md) — check EVS006/EVS007 selection, history and ION delivery.
* [Auto Accounting](m3/auto-accounting.md) and [Table Extraction](m3/table-extraction-for-costing-element.md) — feature-specific setup.

Your Infor administrator must create or import a connection point with the correct tenant credentials, logical ID, company and division. Confirm the resulting BOD in ION, then look for an expected supplier in **Settings → Lookup Master Data → Supplier** in the intended DocBits organisation.

![Current English DocBits Sandbox Lookup Master Data Supplier tab with search controls and synthetic demo rows.](../../.gitbook/assets/dbdc-149-supplier-verification-en.png)

The screenshot shows existing synthetic Sandbox Test A data. No M3 connection or supplier import was tested for this page update.
