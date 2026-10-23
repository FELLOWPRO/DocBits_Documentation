# Export

<figure><img src="../../../../.gitbook/assets/prior-t006-en.png" alt="Unsaved Webhook export configuration."><figcaption><p>Unsaved Webhook export configuration.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/prior-u019-en.png" alt="Unsaved Infor IDM export configuration."><figcaption><p>Unsaved Infor IDM export configuration.</p></figcaption></figure>

## Overview

The Export page displays all configured export setups, including whether they are active or inactive. From here, users can:

* View and manage existing export configurations
* Create new export connections (e.g., to **Infor**, **Infor & IDM**, **Webhook**, or **SFTP**)
* Edit or delete existing export configurations

## Where to Find It

You can find it under: **Settings** → **Document Processing** → **Export**

<figure><img src="../../../../.gitbook/assets/s150-export_settings_menu_access.png" alt="Open export configuration from the English settings."><figcaption><p>Open export configuration from the English settings.</p></figcaption></figure>

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


#### **Important Rules for Export Configuration**

For each **document type** **within a given organization or sub-organization**, the following rules apply:

* You can have **only one active Infor export**
* You can have **only one active non-Infor export** (e.g., Webhook, SFTP)

However, it is possible to have:

* **One active Infor export** _and_ **one active non-Infor export** at the same time for the same document type
* **Different export configurations for different sub-organizations** — for example, one Infor export for Sub-Org A and another Infor export for Sub-Org B

## **Creating a New Export**

To create a new export:

1. Click on the **“New”** button.

<figure><img src="../../../../.gitbook/assets/s150-export_create_new_button.png" alt="Unsaved new export configuration showing its basic information."><figcaption><p>Unsaved new export configuration showing its basic information.</p></figcaption></figure>
2. Select the **Export Type** you want to configure (e.g., Infor, IDM, SFTP).
3. Fill in the required fields based on the export type.
4. Save the configuration.

## Export Options

#### Webhook

<details>

<summary>Webhook</summary>

<figure><img src="../../../../.gitbook/assets/image (11).png" alt="Export Webhook Configuration"><figcaption></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/prior-t007-en.png" alt="Unsaved SFTP export configuration."><figcaption><p>Unsaved SFTP export configuration.</p></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/export_sftp_2.png" alt="Actions menu of the export list open on a document row with entries Validate, Assign to, Document-flow, Download, Restart, Document Logs and Workflow Logs" width="316"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/prior-u016-en.png" alt="Unsaved advanced SFTP export options."><figcaption><p>Unsaved advanced SFTP export options.</p></figcaption></figure>

</details>

#### Infor Export to SFTP

<details>

<summary>Infor Export to SFTP</summary>

<figure><img src="../../../../.gitbook/assets/prior-u017-en.png" alt="Unsaved Infor SFTP export configuration."><figcaption><p>Unsaved Infor SFTP export configuration.</p></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Select a mapping file from the file manager. [Need help creating one? View the BOD Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** The path on the SFTP server where documents should be uploaded (e.g., `/incoming/invoices/`). Must exist and be writable.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

<figure><img src="../../../../.gitbook/assets/prior-u018-en.png" alt="Unsaved SMB export configuration."><figcaption><p>Unsaved SMB export configuration.</p></figcaption></figure>

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

<figure><img src="../../../../.gitbook/assets/image (10).png" alt="Export Infor IDM Configuration"><figcaption></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** A switch to indicate the Infor deployment type:
  * **Cloud**: Select this if Infor CloudSuite customer.
  * **On-Prem**: Select this if Infor is self-hosted.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

<figure><img src="../../../../.gitbook/assets/prior-u020-en.png" alt="Unsaved Infor ION export configuration."><figcaption><p>Unsaved Infor ION export configuration.</p></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **BOD Mapping File** Select a mapping file from the file manager. [Need help creating one? View the BOD Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** A switch to indicate the Infor deployment type:
  * **Cloud**: Select this if Infor CloudSuite customer.
  * **On-Prem**: Select this if Infor is self-hosted.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

<figure><img src="../../../../.gitbook/assets/prior-u021-en.png" alt="Unsaved Infor IDM ION BOD export configuration."><figcaption><p>Unsaved Infor IDM ION BOD export configuration.</p></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Select a mapping file from the file manager. [Need help creating one? View the BOD Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** A switch to indicate the Infor deployment type:
  * **Cloud**: Select this if Infor CloudSuite customer.
  * **On-Prem**: Select this if Infor is self-hosted.

</details>

### For Infor CloudSuite customers

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

<figure><img src="../../../../.gitbook/assets/prior-u022-en.png" alt="Unsaved Infor IDM LN export configuration."><figcaption><p>Unsaved Infor IDM LN export configuration.</p></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** Select a mapping file from the file manager. [Need help creating one? View the LN Mapping Example](../../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

<figure><img src="../../../../.gitbook/assets/prior-u023-en.png" alt="Unsaved Infor IDM M3 export configuration."><figcaption><p>Unsaved Infor IDM M3 export configuration.</p></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** Select a mapping file from the file manager. [Need help creating one? View the M3 Mapping Example](../../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

<figure><img src="../../../../.gitbook/assets/prior-u024-en.png" alt="Unsaved Infor IDM M3 export configuration with TOML."><figcaption><p>Unsaved Infor IDM M3 export configuration with TOML.</p></figcaption></figure>

**Field Descriptions**

* **Title** The name of the export configuration. This will appear in the export list.
* **Sub-Organization** _(optional)_ A dropdown with all available sub-organizations.
  * If left empty: applies to the main organization.
  * If selected: the export will only apply to the chosen sub-organization.
* **Document Type** Dropdown listing all available document types. This determines which type of document this export configuration applies to.
* **ION Mapping File** Select a mapping file from the file manager.
* **IDM Mapping File** Select a mapping file from the file manager. [Need help creating one? View the IDM Mapping Guide](../../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** Select a mapping file from the file manager or use the select Toml option to use a toml created with the rule manager. [Need help creating one? View the Rule Manager Guide](../rule-manager/)

</details>
