---
description: Set up a custom master data template or API endpoint in DocBits.
---

# Custom Master Data

Custom Master Data lets an administrator define a source of reference data for lookups. You can create a reusable template or connect an endpoint. Prepare the API URL, authentication details and a sample response with your integration administrator before you start.

## Enable the module

1. Open **Settings → Module → Document Integration**.
2. Turn on **Custom Master Data**. The blue switch indicates that it is enabled for the current organization.

<figure><img src="../../.gitbook/assets/custom-master-data-module-en-20260928.png" alt="Document Integration module settings with the Custom Master Data switch enabled"><figcaption><p>Enable Custom Master Data in Document Integration.</p></figcaption></figure>

## Open Custom Master Data

1. Open **Settings → Lookup Master Data**.
2. Select the **settings gear next to ERP API Data**. This gear is shown when Custom Master Data is enabled. The plus icon next to **Imported** is for CSV uploads, not for API endpoints.

<figure><img src="../../.gitbook/assets/custom-master-data-lookup-en-20260928.png" alt="Lookup Master Data page with a settings gear next to ERP API Data and a separate plus icon next to Imported"><figcaption><p>Use the ERP API Data gear to open Custom Master Data.</p></figcaption></figure>

The dialog lists existing custom data connections. **Create Template** starts a reusable API configuration; **Create Endpoint** starts a connection that can populate a master data table. An existing row offers **Edit**, **Trigger Endpoint** and **Delete**. Use Delete only when the connection is no longer needed.

<figure><img src="../../.gitbook/assets/custom-master-data-actions-en-20260928.png" alt="Custom Master Data dialog with Create Template and Create Endpoint buttons above an empty list"><figcaption><p>Choose a template or endpoint; this test organization has no existing custom connections.</p></figcaption></figure>

## Create a template

Select **Create Template**, then choose **ION API** or **OAuth2**. The ION API path asks for an ION authentication JSON file; keep that file private. The next steps configure the preset, identify the path to table data in a sample response, and map response values to columns. Use **Continue** to move through the steps and review the mappings before finishing.

<figure><img src="../../.gitbook/assets/custom-master-data-template-en-20260928.png" alt="Create Preset wizard at Select Preset with ION API and OAUTH2 choices"><figcaption><p>Choose the API authentication method for a reusable template.</p></figcaption></figure>

## Create an endpoint

Select **Create Endpoint**. The first step offers **Blank**, **ION API**, **OAuth2**, and any templates already saved in your organization. Choose the option that matches your integration; **Blank** starts without saved authentication settings.

<figure><img src="../../.gitbook/assets/custom-master-data-create-en-20260928.png" alt="Create Endpoint wizard at Select Preset with Blank, ION API and OAuth2 choices"><figcaption><p>Choose how the new endpoint should be configured.</p></figcaption></figure>

In **Configure API Endpoint**, enter an endpoint name without spaces, choose the body type and request method, and enter the API URL. **Params**, **Headers**, **Authorization** and **Body** configure the request. The **Dynamic Lookup Population Based on Document Fields** checkbox is for values that depend on the current document. Continue only when the request works: DocBits checks the endpoint response before it moves to the table data path. Then select the response path, map columns in **Create Table with Response**, and finish.

<figure><img src="../../.gitbook/assets/custom-master-data-endpoint-en-20260928.png" alt="Configure API Endpoint step with endpoint name, method, base URL, Params, Headers, Authorization and Body tabs"><figcaption><p>The endpoint configuration step. This example has no API address or credentials entered.</p></figcaption></figure>

The screenshots show the setup screens only. No endpoint was saved or triggered in the test organization because it has no connected example API. For help finding and using master data after setup, see [Master Data Lookup](../../administration-and-setup/settings/document-processing/master-data-lookup.md).
