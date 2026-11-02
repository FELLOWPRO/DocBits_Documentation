# Start a supplier initial load from Infor M3

Use this procedure only after your Infor administrator has confirmed the company, division, `SupplierPartyMaster` BOD and DocBits ION route. An unrestricted initial load may send every eligible supplier, so agree on a small selection first. The eleven Infor M3 screenshots below are historical examples; compare them with your tenant before running a job. This page update did not run an M3 job or import suppliers into DocBits.

Infor documents the [EVS006 initial-load procedure](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) and [EVS007 selection and run options](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Follow your tenant's approved procedure if labels differ.

* [ ] Open Infor OS and the M3 application with an account authorised for initial loads. Confirm the intended company and division before continuing.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Historical Infor OS application launcher with M3 available."><figcaption></figcaption></figure>

* [ ] Open **Initial Load. Open (EVS006)** using your tenant's program search.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Historical Infor M3 program search for EVS006."><figcaption><p><em><strong>evs006</strong></em></p></figcaption></figure>

* [ ] In EVS006, create an initial-load definition for **SupplierPartyMaster**. The historical example uses **CIDMAS** as the table. Ask the M3 administrator to confirm that this BOD/table combination is valid in your version and integration.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Historical empty Initial Load Open EVS006 table."><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="Historical EVS006 entry with SupplierPartyMaster BOD noun and CIDMAS table."><figcaption></figcaption></figure>

* [ ] Select **Create** and review the definition before proceeding.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="Historical EVS006 Create action for a supplier initial load."><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="Historical EVS006 detail form after Create."><figcaption></figcaption></figure>

* [ ] Enter a clear **BOD Description**, for example **SupplierPartyMaster initial load for DocBits**.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="Historical BOD description field set to SupplierPartyMaster."><figcaption></figcaption></figure>

* [ ] Select **Next** and define an agreed selection where available. Infor recommends selection criteria to avoid triggering too many events.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="Historical Next action on the initial load form."><figcaption></figcaption></figure>

* [ ] Continue to the run settings. Review the company, division and selection again.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Historical EVS006 selection screen before the final run settings."><figcaption></figcaption></figure>

* [ ] On the SupplierPartyMaster definition, choose **Related → Run**. This opens **Initial Load Job. Open (EVS007)**; it is not yet proof that DocBits received the data.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="Historical Related Run action for SupplierPartyMaster."><figcaption></figcaption></figure>

* [ ] Choose **Sync** only if the receiving ION flow expects Sync.SupplierPartyMaster. Confirm filters and target before submitting EVS007. A full initial load can generate many events.

<figure><img src="../../../.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png" alt="Historical EVS007 run form with Sync BOD verb."><figcaption></figcaption></figure>

## Verify the result

After an authorised run, check **Related → History** in EVS006 for the processed count and any errors. Then verify the SupplierPartyMaster message in Infor ION and confirm that it reached the configured DocBits organisation. Only then look for one expected supplier in DocBits under **Settings → Lookup Master Data → Supplier**. Use the search control and supplier number or name; do not assume every M3 supplier arrived merely because the job was submitted.

![Current English DocBits Sandbox Settings Lookup Master Data Supplier tab with search controls and synthetic supplier rows. These demo rows do not prove an M3 import.](../../../.gitbook/assets/dbdc-176-supplier-master-data-en.png)

The screenshot shows synthetic Sandbox data already present in Test A. No M3 tenant was connected during this documentation update. If the expected supplier is missing, compare the EVS006 history, ION routing and DocBits organisation before rerunning the load.
