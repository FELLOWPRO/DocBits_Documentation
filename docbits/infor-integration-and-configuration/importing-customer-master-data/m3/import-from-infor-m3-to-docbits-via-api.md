# Import master data from Infor M3 through ION API

Use this guide when an Infor M3 administrator needs to deliver selected BODs to DocBits through Infor ION and API Gateway. The previous version of this page contained 42 screenshots from one older Infor tenant and fixed Sandbox API addresses. Those screens and addresses are not a safe configuration template for another tenant.

The path to check is **M3 publishes a BOD → ION routes it → API Gateway calls the DocBits API → DocBits shows the imported record**. Each stage has its own status. Seeing a record in DocBits is the final check; an active ION data flow alone does not prove an import.

## Before you configure the flow

1. Confirm the M3 company, ION tenant, DocBits organisation and environment you intend to connect. Ask a DocBits administrator for the current API base URL and the required API operation from that environment's OpenAPI description. Regional hosts may differ; do not copy a host or API Gateway proxy path from an old screenshot.
2. Agree which document types the organisation needs. Supplier and purchase order master data can be checked in DocBits. Add delivery and accounting documents only when their use case and receiving operation are confirmed.
3. Prepare an Infor service account with permission for the selected API operation and a DocBits API credential with the minimum required access. Enter credentials only in the authorised configuration screen. Do not paste a complete `.ionapi` file or an API key into a documentation page, Jira issue or screenshot.
4. Keep one non-sensitive test identifier for each chosen BOD so you can trace the same record in M3, ION OneView and DocBits.

## Choose the document and receiving operation

The old tenant example used these BODs. Use the current API metadata and your integration design to confirm each mapping before creating a connection point:

| BOD in the old example | Intended DocBits data | Where to check the receiving format |
| --- | --- | --- |
| `Sync.SupplierPartyMaster`, `Sync.RemitToPartyMaster` | Supplier master data | [Supplier BOD import](../importing-via-the-api/supplier-bod.md) |
| `Sync.PurchaseOrder` | Purchase orders | [Purchase Order BOD import](../importing-via-the-api/purchase-order-bod.md) |
| `Sync.ReceiveDelivery` | Delivery data | [Receive Delivery BOD import](../importing-via-the-api/receive-delivery-bod.md) |
| `Sync.AdvanceShipNotice`, `Sync.ChartOfAccounts`, `Sync.CodeDefinition-AccountingDimension` | Additional master data for configured features | [Master data XML import](../importing-via-the-api/master-data-xml.md) and your tenant's API metadata |

`Acknowledge.SupplierInvoice` belongs to an invoice acknowledgement flow and should be configured separately from an M3-to-DocBits master-data import. The old page mixed these directions and included a tenant-specific request body; do not copy that body into a new flow without reviewing the endpoint contract and access controls.

## Configure Infor OS and ION

1. In Infor OS, prepare the API Gateway target for the **confirmed** DocBits API operation. Check the target URL, request method, request format and authentication with the DocBits administrator. Use the current [Infor API Gateway guide](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/ionapi_2025.x_apigatewayag_cloud_en-us.pdf) for the Gateway controls.
2. In **ION → Connect → Connection Points**, create or select the connection point for the DocBits API. Add only the chosen BODs in **Documents**, select the matching Gateway operation and configure the request payload the operation expects. Infor's [API element instructions](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/hqg1491985489422.html) explain the service account and request settings.
3. In **ION → Connect → Data Flows**, connect the M3 source and the API destination. Check the document list, filters and mappings; then save and activate the flow. Infor distinguishes [saving from activating a data flow](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/lsm1436532178755.html).
4. Publish one approved test BOD from M3. In **ION OneView**, find that identifier and confirm which connection point, mapping and API call handled it. See [Infor OneView](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/lsm1436532196155.html). If no route or an error is shown, fix the ION flow before checking DocBits.

## Verify the result in DocBits

Open **Settings → Document Processing → Lookup Master Data**. Expand **BOD Input data**, choose the relevant type, and search for the test identifier. The **Supplier** and **Purchase Order** tabs shown below are current English views in the synthetic **DocBits Documentation Test A** organisation. Their existing demo rows are **not evidence of an M3 import**.

<figure><img src="../../../.gitbook/assets/dbdc206-supplier-bod-input-en.png" alt="English DocBits Lookup Master Data screen with the Supplier tab and search controls for checking an imported supplier"><figcaption><p>Choose Supplier, select a search column and enter the test supplier identifier.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc206-purchase-order-bod-input-en.png" alt="English DocBits BOD Input data menu with Purchase Order selected and a searchable purchase order table"><figcaption><p>Choose Purchase Order and search for the test order; the rows pictured are synthetic demo data.</p></figcaption></figure>

In either tab, **Search by column** chooses the field, **Search String** accepts the identifier and the magnifier runs the search. The table headers sort the visible rows; the arrows at the bottom move between pages. **Actions** opens table operations and is not needed for this read-only check. The **×** on a tab closes it. The **Imported** plus button is for CSV uploads, not for receiving an ION BOD.

If the BOD appears in OneView but the record is absent in DocBits, check the API operation and response, organisation/environment, document type, payload format and identifier used in the search. Ask the DocBits administrator for the corresponding import log. Do not infer success from an HTTP call or screenshot of an unrelated demo row.

This page was updated using current DocBits Sandbox controls and Infor documentation. No Infor tenant or live M3-to-DocBits BOD transfer was available for an end-to-end test; a tenant administrator must validate the final mapping and result.
