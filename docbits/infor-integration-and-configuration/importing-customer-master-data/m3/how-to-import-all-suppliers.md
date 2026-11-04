# Start a supplier initial load from Infor M3

Use this procedure only after your Infor administrator has confirmed the company, division, `SupplierPartyMaster` BOD and DocBits ION route. An unrestricted initial load may send every eligible supplier, so agree on a small selection first. The eleven Infor M3 screenshots below are historical examples; compare them with your tenant before running a job. This page update did not run an M3 job or import suppliers into DocBits.

Infor documents the [EVS006 initial-load procedure](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) and [EVS007 selection and run options](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Follow your tenant's approved procedure if labels differ.

* [ ] Open Infor OS and the M3 application with an account authorised for initial loads. Confirm the intended company and division before continuing.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Infor M3 start screen with module menu on the left and Recent list showing EVS006 Initial Load, BOD Processor Administration"><figcaption><p>Historical Infor M3 start screen with EVS006 Initial Load, BOD Processor Administration in the Recent list.</p></figcaption></figure>

* [ ] Open **Initial Load. Open (EVS006)** using your tenant's program search.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Infor M3 Search and Start dialog with an empty input field and OK button"><figcaption><p>Historical Infor M3 Search and Start dialog with its input field and OK button.</p></figcaption></figure>

* [ ] In EVS006, create an initial-load definition for **SupplierPartyMaster**. The historical example uses **CIDMAS** as the table. Ask the M3 administrator to confirm that this BOD/table combination is valid in your version and integration.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Search and Start dialog with evs006 typed into the input field"><figcaption><p>Historical Search and Start example with EVS006 entered in the input field.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="EVS006 Initial Load list with BOD noun SupplierPartyMaster and Table CIDMAS filled in"><figcaption><p>Historical EVS006 Initial Load list with SupplierPartyMaster as the BOD noun and CIDMAS as the table.</p></figcaption></figure>

* [ ] Select **Create** and review the definition before proceeding.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="EVS006 list with the Create (plus) toolbar button highlighted in red"><figcaption><p>Historical EVS006 list with the Create toolbar button highlighted.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="EVS006 create panel for table CIDMAS with an empty BOD description field"><figcaption><p>Historical EVS006 create panel for CIDMAS with the BOD description field still empty.</p></figcaption></figure>

* [ ] Enter a clear **BOD Description**, for example **SupplierPartyMaster initial load for DocBits**.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="EVS006 create panel with BOD description set to SupplierPartyMaster"><figcaption><p>Historical EVS006 create panel with SupplierPartyMaster entered as the BOD description.</p></figcaption></figure>

* [ ] Select **Next** and define an agreed selection where available. Infor recommends selection criteria to avoid triggering too many events.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="EVS006 create panel with the Next button highlighted at the bottom right"><figcaption><p>Historical EVS006 create panel with the Next button highlighted.</p></figcaption></figure>

* [ ] Continue to the run settings. Review the company, division and selection again.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Text dialog in EVS006 with empty text block fields and Next button"><figcaption><p>Historical EVS006 Text dialog with text-block fields and a Next button.</p></figcaption></figure>

* [ ] On the SupplierPartyMaster definition, choose **Related → Run**. This opens **Initial Load Job. Open (EVS007)**; it is not yet proof that DocBits received the data.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="EVS006 list with the right-click menu open on the SupplierPartyMaster row showing Related > Run"><figcaption><p>Historical EVS006 list with the Related → Run menu open on the SupplierPartyMaster row.</p></figcaption></figure>

* [ ] Choose **Sync** only if the receiving ION flow expects Sync.SupplierPartyMaster. Confirm filters and target before submitting EVS007. A full initial load can generate many events.

<figure><img src="../../../.gitbook/assets/m3-supplier-initial-load-job-historical-id-masked-20261102.png" alt="EVS007 Initial Load Job for CIDMAS and SupplierPartyMaster with BOD verb Sync and status 1-Pending"><figcaption><p>Historical EVS007 Initial Load Job showing CIDMAS, SupplierPartyMaster, Sync and status 1-Pending. The job identifier is masked; the pending status does not prove a completed import.</p></figcaption></figure>

## Verify the result

After an authorised run, check **Related → History** in EVS006 for the processed count and any errors. Then verify the SupplierPartyMaster message in Infor ION and confirm that it reached the configured DocBits organisation. Only then look for one expected supplier in DocBits under **Settings → Lookup Master Data → Supplier**. Use the search control and supplier number or name; do not assume every M3 supplier arrived merely because the job was submitted.

![Current English DocBits Sandbox Settings Lookup Master Data Supplier tab with search controls and synthetic supplier rows. These demo rows do not prove an M3 import.](../../../.gitbook/assets/dbdc-176-supplier-master-data-en.png)

The screenshot shows synthetic Sandbox data already present in Test A. No M3 tenant was connected during this documentation update. If the expected supplier is missing, compare the EVS006 history, ION routing and DocBits organisation before rerunning the load.

### Alternative: Supplier Management

If the Supplier Portal is in use (the **Supplier Management** entry appears in the main menu), the imported suppliers appear there as well, because both views read the same supplier master data. Search by supplier name or number with **Search by Name, Number**.

<figure><img src="../../../.gitbook/assets/supplier-search-native-en-20261102.png" alt="Supplier Management search control labelled Search by Name, Number, with the filter icon"><figcaption><p>Supplier Management search control.</p></figcaption></figure>
