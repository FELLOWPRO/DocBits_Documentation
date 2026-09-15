---
description: How to import a Supplier BOD into DocBits manually using the API
hidden: true
noIndex: true
---

# Import Suppliers (Supplier BOD)

Supplier master data normally reaches DocBits automatically through your ION data flow. This page describes how to send a **Supplier BOD** in by hand — useful when you want to re-import a supplier, load a batch that never arrived, or test a field mapping before switching the automatic flow on.

## Two ways to send the same BOD

There are two endpoints, and they do the same thing. The only difference is how you hand over the BOD:

| Endpoint | Use it when |
| --- | --- |
| `/import/supplier_bod` | You have the BOD as an **XML file** and want to upload it. |
| `/import/supplier_bod_xml` | You want to send the **XML content** in the request instead of a file. The BOD has to be wrapped in JSON, so this suits short XML or another system calling the API — for a full BOD by hand, upload the file. |

Both are described below. Steps 1 and 2 are the same either way.

## Before you start

You will need:

* **An API key.** See [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) if you do not have one yet.
* **The BOD** — a `SyncSupplierPartyMaster` or `SyncRemitToPartyMaster` XML file, or its content.
* **Your Org ID**, from **Settings → Integration & SSO** in the **ID** section.

<figure><img src="../../../.gitbook/assets/import-org-id.png" alt="The ID section showing Org ID and Sub Org ID with their copy buttons"><figcaption><p>Settings → Integration &#x26; SSO → ID</p></figcaption></figure>

{% hint style="info" %}
**Sub Org ID** shows whichever sub-organization is selected in the header. With **CROSS** selected — the view across all sub-organizations — it shows the same value as **Org ID**. Switch to a specific sub-organization first if you need its ID.

If you are not importing into a particular sub-organization, leave the `sub_org_id` field empty.
{% endhint %}

## Step-by-Step Instructions

### 1. Open the API link

Open the API test interface for the environment and region you are working with:

* [Sandbox API (Europe)](https://eu.sandbox.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Sandbox API (United States)](https://us.sandbox.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Production API (Europe)](https://eu.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Production API (United States)](https://us.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)

Expand the endpoint you want by clicking on it.

{% hint style="info" %}
Use the region your organization is hosted in — the same region you use to log in to DocBits. The European and American environments are separate, so an import sent to the wrong region will not show up in your organization.

The addresses without a region prefix — `api.docbits.com` and `sandbox.api.docbits.com` — point to Europe. You will see those in older documentation and in existing configurations; they are the same environment as the `eu.` addresses above.
{% endhint %}

### 2. Authorize

Everything under **import** is locked until you authorize. There are two things to fill in: your organization and your API key.

* Click the **lock icon** on the right of the endpoint.

<figure><img src="../../../.gitbook/assets/import-swagger-lock.png" alt="The import endpoints with the lock icon highlighted"><figcaption><p>Click the lock to open the authorization dialog</p></figcaption></figure>

* The **Available authorizations** dialog opens with two entries.
* Paste your **Org ID** into **X-ORG-ID** and click **Authorize**.

<figure><img src="../../../.gitbook/assets/import-authorize-orgid.png" alt="The X-ORG-ID authorization with an empty value field"><figcaption><p>X-ORG-ID — paste the Org ID, then Authorize</p></figcaption></figure>

* Scroll down to **X-API-KEY**, paste your API key and click **Authorize**. In DocBits you find it under **Settings → Integration & SSO** in the **API Key** section, or you can [create a new key](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#creating-an-api-key).

<figure><img src="../../../.gitbook/assets/import-authorize-apikey.png" alt="The X-API-KEY authorization with an empty value field"><figcaption><p>X-API-KEY — paste the key, then Authorize</p></figcaption></figure>

* Click **Close**.

{% hint style="info" %}
Paste the key on its own — do not type `Bearer` in front of it. Both authorizations stay set until you reload the page or click **Logout**.
{% endhint %}

### 3. Fill in the fields

Click **Try it out**, then fill in the form for the endpoint you chose.

#### Uploading a file — `/import/supplier_bod`

<!-- SCREENSHOT: the Try it out form of /import/supplier_bod -->

| Field | |
| --- | --- |
| **file** | Required. Click **Choose file** and select your supplier BOD XML file. |
| **org\_id** | Your Org ID — the same value you put into **X-ORG-ID** in step 2. Setting it here as well makes the request explicit about which organization it is writing to. It must be an organization your API key has access to; anything else is refused. |
| **sub\_org\_id** | Only needed if you are importing into a particular sub-organization. |
| **custom\_fields\_mapping** | Optional. Reads extra fields out of the BOD into the supplier's custom fields. See [Custom field mappings](#custom-field-mappings) below. |

There is no line-mapping field here — supplier master data has no lines.

{% hint style="warning" %}
**`string` is a value, not a placeholder.** Swagger fills the optional fields with the word `string`, and it is sent as-is if you leave it there — an import with `org_id` set to `string` will fail.

For every optional field you do not want to use, clear the field. Clearing it enables the **Send empty value** checkbox underneath, which you can then tick.
{% endhint %}

#### Custom field mappings

The mapping field takes a JSON object. The **name on the left must be one of DocBits' own custom fields** — `custom_field_1` through `custom_field_5` for suppliers. Any other name is ignored without warning, so a typo here looks exactly like a mapping that did not work.

The value on the right is the XPath to read from. Write it without namespace prefixes — DocBits adds those itself:

```json
{"custom_field_2": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

#### Pasting the XML — `/import/supplier_bod_xml`

This endpoint does not take the BOD as a plain paste. The **xml** field is an object, pre-filled with `{"xml": "string"}`. Replace `string` with the content of your BOD, keeping the surrounding quotes and braces:

```json
{
  "xml": "<SyncSupplierPartyMaster ...>...</SyncSupplierPartyMaster>"
}
```

{% hint style="warning" %}
The BOD sits inside a JSON string, so every double quote in the XML has to be escaped as `\"` — and a BOD is full of them. If the result is not valid JSON the request fails with a **422** and nothing is imported.

For a real BOD that is fiddly to do by hand, so prefer **uploading the file**.
{% endhint %}

The `org_id`, `sub_org_id` and `custom_fields_mapping` fields work exactly as above.

{% hint style="warning" %}
Check which environment and which organization you are pointing at before you execute. An import writes straight into that organization's master data.
{% endhint %}

### 4. Execute

Before you execute, check the **Servers** dropdown at the bottom of the form. It decides which environment the request is actually sent to, and it can differ from the page you opened.

Click **Execute**. A successful import returns:

```json
{
  "success": true,
  "message": "BOD processed successfully."
}
```

Supplier BODs are processed while you wait, so by the time you see this message the data is in.

If something was wrong with the request, you get `"success": false` together with a message describing the problem. The most common causes are content that is not a supplier BOD, and an Org ID that your API key has no access to.

### 5. Check that the data arrived

* In DocBits, go to **Settings → Document Processing → Lookup Master Data**.
* Select **BOD Input Data** on the left, then open the **Supplier** tab.
* Search for the supplier from your BOD.

<!-- SCREENSHOT: Lookup Master Data with BOD Input Data selected and the Supplier tab open -->

{% hint style="info" %}
DocBits decides what to do with the BOD by reading the type inside it, not by which import endpoint you used. If you send a purchase order BOD here by mistake, it is imported as a purchase order rather than rejected — so check that the tab you find the data in is the one you expected.
{% endhint %}
