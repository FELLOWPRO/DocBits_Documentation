---
description: Sending master data into DocBits by hand using the API
hidden: true
noIndex: true
---

# Importing via the API

Master data normally reaches DocBits automatically through your ION data flow. The pages in this section describe how to send the same data in by hand using the API test interface — useful when you want to re-import a record, load something that never arrived, or try a new field mapping before switching the automatic flow on.

Each page follows the same five steps: open the API link for your environment, authorize with your Org ID and API key, fill in the form, execute, and check that the data arrived.

* [Import Purchase Orders (Purchase Order BOD)](purchase-order-bod.md)

## What you need

* **An API key** — see [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).
* **Your Org ID** — under **Settings → Integration & SSO** in the **ID** section.
* **The data itself**, as an XML file or as XML content you can paste.

{% hint style="warning" %}
An import writes straight into your organization's master data. Check which environment, which region and which organization you are pointing at before you execute.
{% endhint %}
