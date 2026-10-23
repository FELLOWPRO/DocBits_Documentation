# Architecture

## **DocBits Cloud customer**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="DocBits Cloud Customer Architecture"><figcaption></figcaption></figure>

## DocBits On premise

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="DocBits On Premise Architecture"><figcaption></figcaption></figure>

Doc**Bits** seamlessly integrates with Infor LN/M3 through ION API, ION Desk, and Infor Standard BODs. Our API integration allows us to export data to Infor and perform master data validation in Doc**Bits**.

## **DocBits Operator Architecture**

All connections between components are secured using industry-standard encryption protocols. SSH, HTTPS, and other secure channels ensure data integrity and confidentiality throughout the system.

**On Premise:**&#x20;

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt="Operator On-Prem architecture diagram with DocAgent on a client machine connecting to the Prefect API and the DocBits cloud"><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[prefect-local-setup-requirements.md](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud**:

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt="Operator Cloud architecture diagram with the Chrome extension, DocBits Operator Cloud, DocFlow and DocBits AI exchanging task and response messages"><figcaption></figcaption></figure>

## Exporting Data to Infor

We use the ION API to send the PDF with attributes to IDM and the BOD Sync.CaptureDocument to ION Desk. In ION Desk, we transform the [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) to the desired target BODs based on the document type being processed. These transformed Infor BODs are then automatically imported to LN or M3.

{% hint style="info" %}
Export to [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Master Data Validation in DocBits

To identify the supplier or compare/match purchase order lines, we activate a trigger in LN/M3 that sends the Sync.RemitToPartyMaster, Sync.SupplierPartyMaster, and Sync.PurchaseOrder BODs to Doc**Bits**. We configure this process in ION Desk by defining the dataflow to a specific connection point to Doc**Bits**.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt="DocBits architecture diagram of the Kubernetes cluster with load balancer, Redis, PostgreSQL, worker pods and Spaces data storage"><figcaption></figcaption></figure>

{% hint style="info" %}
[Master Data Validation](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Email Import OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt="Office 365 email import diagram showing Microsoft Graph API issuing an access token to the DocBits mail service and main system"><figcaption></figcaption></figure>