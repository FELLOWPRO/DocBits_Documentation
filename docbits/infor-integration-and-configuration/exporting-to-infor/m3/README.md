# M3

## Step 1: Create an Connection Point

1. Navigate to **OS > ION > Connect > Connection Points**
2. Click **Add** and select **IMS via API Gateway** as the connection type.
3. Configure the following settings:
   * **Name**: Set to `DocBits_Export`.
   * **Description**: Set to `DocBits_Export`.
   * **Uncheck**: _Application has IMS End Point_.
   * **ION API Client ID**:
     * Open the ION API file.
     * Search for `"ci"` within the file.
     * Copy the value inside the quotation marks (without the quotation marks).

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_1.png" alt="Infor Application Connection Point dialog IMS via API Gateway with the tabs Usage, Connection and Documents, the name DocBits_Export, the unchecked option Application has IMS End Point, the ION API Client ID field and the Logical ID inforims.docbits_export"><figcaption></figcaption></figure>

4. Under **Documents**, add `Sync.CaptureDocument`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_2.png" alt="Connection tab of the application connection point with the name DocBits_Export, the document sync.captureDocument shown as Send from Application and the Logical ID inforims.docbits_export"><figcaption></figcaption></figure>

5. Click **Save** to finalize the configuration.

## Step 2: Upload Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Download the M3 Mapping File
2. Navigate to **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Click **Import** and select the appropriate mapping file for **M3**.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_3.png" alt="Mappings page in ION Desk with the search field, the filter controls and the button Add"><figcaption></figcaption></figure>

4. Once the files are imported, approve the mappings to activate them.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_4.png" alt="Imported mapping with the source Sync.CaptureDocument and the target Process.SupplierInvoice"><figcaption></figcaption></figure>

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

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_5.png" alt="Data flow canvas in ION Desk with the node palette at the top and the panel Application Activity Properties on the right with the name DocBits-Dev-Demo-Export"><figcaption></figcaption></figure>

3. Click on the **Document Icon** next to the application node.
   * Click **Add** and select `Sync.CaptureDocument`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_6.png" alt="Data flow canvas in ION Desk with the application node selected and the Documents panel open showing the entry Sync.CaptureDocument"><figcaption></figcaption></figure>

#### Mapping Node

1. Add a **Mapping Node** to the right of the application node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_7.png" alt="Data flow canvas in ION Desk with the mapping node selected and the panel Mapping Properties on the right with the name and the mapping SyncCaptDoc_SyncSuppInv"><figcaption></figcaption></figure>

#### Application Node

1. Add an **Application Node** to the right of the previous mapping node.
   * **Name**: `M3`.
2. Click **Add** and select the **M3 Application** from the customer.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_8.png" alt="Data flow canvas in ION Desk with the M3 application node selected and the panel Application Activity Properties on the right with the entry M3 BODs"><figcaption></figcaption></figure>

3. Click on the **Document Icon** next to the application node.
   * Click **Add** and select `Acknowledge.SupplierInvoice`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_9.png" alt="Data flow canvas in ION Desk with the M3 application node selected and the Documents panel open showing the entry Acknowledge.SupplierInvoice"><figcaption></figcaption></figure>

#### API Node

1. Add an **API Node** to the right of the application node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * If `DocBits_Import` does not exist, refer to **Step 1** and **Step 2** of the Import from M3 documentation to create the connection point.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_10.png" alt="Data flow canvas in ION Desk with the API node selected and the panel ION API Activity Properties on the right with the ION API Connector DocBits Dev Demo-Import"><figcaption></figcaption></figure>

#### Save and Activate the Flow

* Once all nodes are added and configured, click **Save**.
* Activate the flow to complete the setup.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_11.png" alt="Data flow canvas in ION Desk with the nodes DocBits_Demo_to_M3, the mapping node, the M3 node and the error node connected in a row and the button REMOVE CONNECTION POINTS above the canvas"><figcaption></figcaption></figure>

## Step 4: Configure Export in DocBits

### On-Premise:

1. Open **DocBits**.
2.  Navigate to **Settings > Document Processing > Export**.

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="Settings page in DocBits with the navigation group Document Processing expanded and the entries Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values and Module"><figcaption></figcaption></figure>
3. Create a new export:
   * **Select**: **Infor IDM + ION BOD**.
   * **Title**: Choose a meaningful title.
   * **Document Type**: Set to **Invoice**.
   * **Sub-Organization**: Can be left empty, or set to a specific sub-organization if needed.
4. Upload the required files:
   * **ION Mapping File**: This can be found in **Infor OS → API Gateway → Authorized Apps**. Look for the **DocBits** app, open it, and download the credentials.
   * **IDM Mapping File**: (Provide the relevant file path or location).
   * **BOD Mapping File**: (Provide the relevant file path or location).

### Cloud:

1. Open **DocBits**.
2.  Navigate to **Settings > Document Processing > Export**.

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="Settings page in DocBits with the navigation group Document Processing expanded and the entries Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values and Module"><figcaption></figcaption></figure>
3. Create a new export:
   * **Select**: **Infor IDM + M3 (API)**.
   * **Title**: Choose a meaningful title.
   * **Document Type**: Set to **Invoice**.
   * **Sub-Organization**: Can be left empty, or set to a specific sub-organization if needed.
4. Upload the required files:
   * **ION Mapping File**: This can be found in **Infor OS → API Gateway → Authorized Apps**. Look for the **DocBits** app, open it, and download the credentials.
   * **IDM Mapping File**: (Provide the relevant file path or location).
   * **M3 Mapping File**: (Provide the relevant file path or location).

### Cloud with toml:

1. Open **DocBits**.
2.  Navigate to **Settings > Document Processing > Export**.

    <figure><img src="../../../.gitbook/assets/settings_export.png" alt="Settings page in DocBits with the navigation group Document Processing expanded and the entries Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values and Module"><figcaption></figcaption></figure>
3. Create a new export:
   * **Select**: **Infor IDM + M3 (API)**.
   * **Title**: Choose a meaningful title.
   * **Document Type**: Set to **Invoice**.
   * **Sub-Organization**: Can be left empty, or set to a specific sub-organization if needed.
4. Upload the required files:
   * **ION Mapping File**: This can be found in **Infor OS → API Gateway → Authorized Apps**. Look for the **DocBits** app, open it, and download the credentials.
   * **IDM Mapping File**: (Provide the relevant file path or location).
   * **M3 toml Mapping File**: (Provide the relevant file path or location).
