# Export

## Overview

The Export page displays all configured export setups, including whether they are active or inactive. From here, users can:

* View and manage existing export configurations
* Create new export connections (e.g., to **Infor**, **Infor & IDM**, **Webhook**, or **SFTP**)
* Edit or delete existing export configurations

## Where to Find It

You can find it under: **Settings** → **Document Processing** → **Export**

<figure><img src="../../../.gitbook/assets/export_list_view.png" alt="Export Settings Menu Access"><figcaption></figcaption></figure>

## **Using the Export Page**

When you open the Export page, you’ll see a list of all existing export configurations.

Each row in the list shows:

* **Status Indicator**
  * **Green** means the export is active
  * **Red** means the export is deactivated
* **Name** – the name of the export configuration
* **Document Type** – the type of document the export is configured for
* **Sub-Organization** – if the export is limited to a specific sub-organization
* **Export Method** – where the document will be sent (e.g., Infor, IDM, SFTP)
* **Actions** – buttons to **edit, delete** or **activate/deactivate** the configuration

<figure><img src="../../../.gitbook/assets/export_list_view.png" alt="Export List View"><figcaption></figcaption></figure>

#### **Important Rules for Export Configuration**

For each **document type** **within a given organization or sub-organization**, the following rules apply:

* You can have **only one active Infor export**
* You can have **only one active non-Infor export** (e.g., Webhook, SFTP)

However, it is possible to have:

* **One active Infor export** _and_ **one active non-Infor export** at the same time for the same document type
* **Different export configurations for different sub-organizations** — for example, one Infor export for Sub-Org A and another Infor export for Sub-Org B

## **Creating a New Export**

To create a new export:

1. Click on the **“New”** button. ![](../../../.gitbook/assets/export_create_new_button.png)
2. Select the **Export Type** you want to configure (e.g., Infor, IDM, SFTP).
3. Fill in the required fields based on the export type.
4. Save the configuration.

## Export Options

#### Webhook

<details>

<summary>Webhook</summary>

<figure><img src="../../../.gitbook/assets/image (14) (1).png" alt="Export Webhook Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **Export URL** The destination URL where the document should be exported.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

<figure><img src="../../../.gitbook/assets/export_sftp_configuration.png" alt="Export SFTP Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **Username** The username used to authenticate against the SFTP server.
* **Password** The corresponding password for the SFTP account. Ensure the account has write access to the specified folder.
* **Server URL** The hostname or IP address of the target SFTP server.
* **Port** The port used to connect to the SFTP server.
* **Folder** The path on the SFTP server where documents should be uploaded (e.g., `/incoming/invoices/`). Must exist and be writable.
*   **XSLT File (Optional)**

    The **XSLT file** allows for transformation of the default DocBits export format.

    * **When to use:** Only if the receiving system requires a different structure or specific formatting that differs from the DocBits default.
    * **Leave it empty** if the default export format meets the requirements.

**Advanced Settings:**

* **Filename Export Mode** Specifies whether the exported file retains its original filename or is renamed using the DocBits document ID.
* **Include Document History** When enabled, the exported file will include the document history based on the logs available on the dashboard.

<figure><img src="../../../.gitbook/assets/export_sftp_2.png" alt="" width="316"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/export_sftp_3.png" alt=""><figcaption></figcaption></figure>

</details>

#### Infor Export to SFTP

<details>

<summary>Infor Export to SFTP</summary>

<figure><img src="../../../.gitbook/assets/export_infor_sftp_configuration.png" alt="Export Infor SFTP Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Select a mapping file from the file manager. [Need help creating one? View the BOD Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** The path on the SFTP server where documents should be uploaded (e.g., `/incoming/invoices/`). Must exist and be writable.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

<figure><img src="../../../.gitbook/assets/export_smb_configuration.png" alt="Export SMB Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **Username** The username used to connect to the SMB share.
* **Password** The corresponding password for SMB authentication.
* **Server URL** The address of the SMB server.
* **Port** Port number used to access the SMB share.
* **Folder** The folder path within the SMB share where documents should be saved(e.g., `/incoming/invoices/`). Must exist and be writable.
*   **JPL Mapping File (Optional)**

    The **JPL file** is used to define a transformation of the exported data before it is written to the SMB share.

    * **When to use:** Only when the exported document data needs to be adjusted to match external formatting or system expectations.
    * **Leave it empty** if no transformation is necessary.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

<figure><img src="../../../.gitbook/assets/image (12) (1).png" alt="Export Infor IDM Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** A switch to indicate the Infor deployment type:
  * **Cloud**: Select this if Infor CloudSuite customer.
  * **On-Prem**: Select this if Infor is self-hosted.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

<figure><img src="../../../.gitbook/assets/export_infor_ion_configuration.png" alt="Export Infor ION Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **BOD Mapping File** Select a mapping file from the file manager. [Need help creating one? View the BOD Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** A switch to indicate the Infor deployment type:
  * **Cloud**: Select this if Infor CloudSuite customer.
  * **On-Prem**: Select this if Infor is self-hosted.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

<figure><img src="../../../.gitbook/assets/export_infor_idm_ion_bod_configuration.png" alt="Export Infor IDM + ION BOD Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Select a mapping file from the file manager. [Need help creating one? View the BOD Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** A switch to indicate the Infor deployment type:
  * **Cloud**: Select this if Infor CloudSuite customer.
  * **On-Prem**: Select this if Infor is self-hosted.

</details>

### For Infor CloudSuite customers

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

<figure><img src="../../../.gitbook/assets/export_infor_idm_ln_configuration.png" alt="Export Infor IDM + LN Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** Select a mapping file from the file manager. [Need help creating one? View the LN Mapping Example](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

<figure><img src="../../../.gitbook/assets/export_infor_idm_m3_configuration.png" alt="Export Infor IDM + M3 Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** Select a mapping file from the file manager. [Need help creating one? View the M3 Mapping Example](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

<figure><img src="../../../.gitbook/assets/export_infor_idm_m3_toml_configuration.png" alt="Export Infor IDM + M3 (toml) Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** Select a mapping file from the file manager or use the select Toml option to use a toml created with the rule manager. [Need help creating one? View the Rule Manager Guide](rule-manager/)

</details>
