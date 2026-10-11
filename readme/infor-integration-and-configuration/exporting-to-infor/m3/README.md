# Export to Infor M3

This page covers the Infor ION flow and the DocBits export configuration. The Infor screenshots below are historical examples; their menus and data-flow settings must be checked in your own tenant before activation. The DocBits section uses current English Sandbox screenshots. No Infor connection or invoice export was tested for this update.


## Step 1: Create a connection point in Infor ION

1. Navigate to **OS > ION > Connect > Connection Points**
2. Click **Add** and select **IMS via API Gateway** as the connection type.
3. Configure the following settings:
   * **Name**: Set to `DocBits_Export`.
   * **Description**: Set to `DocBits_Export`.
   * **Uncheck**: _Application has IMS End Point_.
   * **ION API Client ID**:
     * Open the ION API file.
     * Search for `"ci"` within the file.
     * Copy the `ci` client ID value. Keep the full `.ionapi` file private because it also contains credentials. Infor explains the [file fields](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_1.png" alt="Example Infor ION connection point with IMS via API Gateway settings."><figcaption></figcaption></figure>

4. Under **Documents**, add `Sync.CaptureDocument`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_2.png" alt="Example documents tab adding Sync.CaptureDocument to the connection point."><figcaption></figcaption></figure>

5. Click **Save** to finalize the configuration.

## Step 2: Upload Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Download the M3 Mapping File
2. Navigate to **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Click **Import** and select the appropriate mapping file for **M3**.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_3.png" alt="Example Infor ION mapping import screen for the M3 mapping file."><figcaption></figcaption></figure>

4. Once the files are imported, approve the mappings to activate them.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_4.png" alt="Example imported mapping awaiting approval in Infor ION."><figcaption></figcaption></figure>

## Step 3: Create the Data Flow

1. Navigate to **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Click **Add** and select **Document Flow**.
3. Fill in the details:
   * **Name**: `DocBits_Export_to_M3`
4. Add nodes to the flow:

#### Application Node

1. Add an **Application Node** to the flow.
   * **Name**: `DocBits` or `DocBits-Export`.
2. Click **Add** and select the **Connection Point** created in Step 1.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_5.png" alt="Example DocBits application node linked to the connection point."><figcaption></figcaption></figure>

3. Click on the **Document Icon** next to the application node.
   * Click **Add** and select `Sync.CaptureDocument`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_6.png" alt="Example Sync.CaptureDocument document selected for the DocBits node."><figcaption></figcaption></figure>

#### Mapping Node

1. Add a **Mapping Node** to the right of the application node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_7.png" alt="Example mapping node using CaptureDocument_to_ProcessSupplierInvoice."><figcaption></figcaption></figure>

#### Application Node

1. Add an **Application Node** to the right of the previous mapping node.
   * **Name**: `M3`.
2. Click **Add** and select the **M3 Application** from the customer.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_8.png" alt="Example M3 application node linked to a customer M3 connection point."><figcaption></figcaption></figure>

3. Click on the **Document Icon** next to the application node.
   * Click **Add** and select `Acknowledge.SupplierInvoice`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_9.png" alt="Example Acknowledge.SupplierInvoice document selected for the M3 node."><figcaption></figcaption></figure>

#### API Node

1. Add an **API Node** to the right of the application node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * If `DocBits_Import` does not exist, refer to **Step 1** and **Step 2** of the Import from M3 documentation to create the connection point.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_10.png" alt="Example DocBits-Error API node in the Infor ION flow."><figcaption></figcaption></figure>

#### Save and Activate the Flow

* Once all nodes are added and configured, click **Save**.
* Activate the flow to complete the setup.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_11.png" alt="Example complete Infor ION flow before activation."><figcaption></figcaption></figure>

## Step 4: Configure export in DocBits

In the correct DocBits organisation, open **Settings → Export** and choose **New**. The current Sandbox test organisation has no saved export configuration; creating one is a separate, administrator-controlled step.

![Current English DocBits Sandbox Export list with New action and no saved configuration.](../../../.gitbook/assets/dbdc-184-export-list-en.png)

In **Basic Information**, enter a meaningful **Configuration Title**, choose the **Document Type** (for this invoice flow, Invoice), and select a **Sub-Organization** only if needed. Set **Export** to **Infor**. The **Infor Type** field then appears. The current choices include **Infor IDM + ION BOD**, **Infor IDM + M3**, and **Infor IDM + M3 (TOML)**. Choose the type that matches the connection and mapping files supplied by your integration administrator; the older label “Infor IDM + M3 (API)” is no longer shown in this screen.

For **Infor IDM + M3**, the form asks for an **ION API File** (`.ionapi`, required), **IDM Mapping File** (`.properties`) and **M3 Mapping File** (`.properties`). The TOML and ION BOD variants have different fields; do not substitute one file for another. Obtain tenant-specific files from the authorised Infor administrator. The `.ionapi` file contains credentials and must not appear in screenshots, tickets or the Git repository.

![Current English DocBits Sandbox configuration form with Infor IDM + M3 selected and the three file upload areas, all blank.](../../../.gitbook/assets/dbdc-184-export-m3-en.png)

Review the document type, organisation and file names before **Save**. After the Infor flow is active, test with a single non-production invoice and confirm its status in DocBits, Infor ION and M3. Do not consider a saved configuration proof that an invoice reached M3.

### Infor review required

The eleven Infor screenshots in steps 1–3 are retained as annotated examples. They were not refreshed because no authorised Infor tenant was available. Ask the Infor administrator to compare connection points, document flow, mapping names and permissions against the tenant's current UI. Infor's [connection point and document-flow explanation](https://docs.infor.com/ln/10.8/en-us/lnesolh/lnoshybridng/wxa1699288671147.html) describes how these pieces relate.
