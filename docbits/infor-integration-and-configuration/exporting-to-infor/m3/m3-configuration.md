# M3 Configuration

This page explains the checks that connect a DocBits export configuration to an Infor ION document flow for M3. The previous page contained 38 screenshots from an older Infor tenant, including environment-specific API and mapping settings. They cannot establish the configuration in your tenant, so the current guide links to Infor's instructions and shows the verified English DocBits form. No Infor connection or invoice export was tested for this update.

## Prepare the Infor tenant

Ask the Infor administrator for the approved **ION API endpoint**, a tenant-specific `.ionapi` file, the **IDM mapping** and **M3 mapping** `.properties` files, and the names of the BOD mappings used by this company's invoice flow. The `.ionapi` file contains credentials; keep it out of screenshots, Jira attachments and Git. Its `ci` value is the client ID, as described in [Infor's credential-field reference](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

In ION Desk, the administrator should:

1. Import and approve the mapping versions required by the current tenant. Verify the mapping input and output BOD names instead of reusing names from an old screenshot.
2. Check the DocBits and M3 connection points, their environment-specific logical IDs, document subscriptions and permissions.
3. Build the document flow with the approved mappings and any required filters. Infor explains [connection points, mappings and document flows](https://docs.infor.com/inforos/2024.x/en-us/useradminlib_cloud/iondeskceug_cloud_osm/lnj1556623308383.html).
4. Save, review and [activate the document flow](https://docs.infor.com/inforos/2026.10/en-us/useradminlib_cloud/iondeskceug/lsm1436532178869.html) only after the routes have been checked. Activation is distinct from a successful document export.

For a worked historical ION example, see [Export to Infor M3](./). Compare every Infor screen there with your tenant before following it.

## Configure export in DocBits

In the intended DocBits organisation, open **Settings → Export** and select **New**. The first image shows the New action; organisation-specific configuration values are hidden.

<figure><img src="../../../.gitbook/assets/dbdc-33-export-new-en-20261103.png" alt="English Export view with the New button at the upper right; configuration values in the existing rows are redacted."><figcaption><p>In Settings → Export, select New at the upper right to open an unsaved configuration. Organisation-specific configuration values are hidden in this English Dev view.</p></figcaption></figure>

Enter a **Configuration Title**, choose the **Document Type** (Invoice for this flow), and select a **Sub-Organization** only if required. Choose **Infor** for **Export** and **Infor IDM + M3** for **Infor Type**. The current form asks for an **ION API File** (`.ionapi`, required), **IDM Mapping File** (`.properties`) and **M3 Mapping File** (`.properties`). Obtain only files for this tenant and review them before saving. The screenshot deliberately leaves all uploads empty.

<figure><img src="../../../.gitbook/assets/dbdc-33-export-m3-unsaved-en-20261103.png" alt="Unsaved English Infor IDM + M3 form with blank Configuration Title and Document Type, empty ION API, IDM and M3 file areas, and visible Cancel and disabled Save buttons."><figcaption><p>The unsaved Infor IDM + M3 form shows where to enter the configuration details and choose the three tenant files. All upload fields are empty, and Save is disabled in this incomplete example. Cancel closes the draft without saving.</p></figcaption></figure>

After the Infor flow is active, test with one non-production invoice. Check its result in DocBits, ION and M3. A saved configuration or activated flow alone does not show that the invoice arrived.

**Image verification scope:** These English Dev images show the New action and an unsaved form. No configuration was saved, no tenant files were uploaded, and no connection test or invoice export was run.
