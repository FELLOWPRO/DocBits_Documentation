# How to import all suppliers

The Infor M3 screenshots below are retained as historical examples. Screens, permissions and menu labels can differ in your environment. Before creating or running an initial-load job, confirm the company, division and supplier selection for the intended transfer.

* [ ] Log yourself into the Infor OS environment and go to the M3 application. Recommendation: Make sure you have admin rights in order to be able to run all the programs.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Infor M3 start screen with module menu on the left and Recent list showing EVS006 Initial Load, BOD Processor Administration"><figcaption><p>Historical Infor M3 start screen with EVS006 Initial Load, BOD Processor Administration in the Recent list.</p></figcaption></figure>

* [ ] Run the program _**evs006**_. Press command + R and you will see the open tab to search and start.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Infor M3 Search and Start dialog with an empty input field and OK button"><figcaption><p>Historical Infor M3 Search and Start dialog with its input field and OK button.</p></figcaption></figure>

* [ ] When _**evs006**_ is open you will see an empty table. Please fill the columns of “BOD noun” and “Table”. For “BOD noun” introduce “SupplierPartyMaster” and for “Table” we are going to use the M3 supplier table called “CIDMAS”.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Search and Start dialog with evs006 typed into the input field"><figcaption><p>Historical Search and Start example with EVS006 entered in the input field.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="EVS006 Initial Load list with BOD noun SupplierPartyMaster and Table CIDMAS filled in"><figcaption><p>Historical EVS006 Initial Load list with SupplierPartyMaster as the BOD noun and CIDMAS as the table.</p></figcaption></figure>

* [ ] When you have filled these columns, just click on CREATE button (on the upper bar side of the screen). You will come to following screen.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="EVS006 list with the Create (plus) toolbar button highlighted in red"><figcaption><p>Historical EVS006 list with the Create toolbar button highlighted.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="EVS006 create panel for table CIDMAS with an empty BOD description field"><figcaption><p>Historical EVS006 create panel for CIDMAS with the BOD description field still empty.</p></figcaption></figure>

* [ ] Fill the “BOD Description” with SupplierPartyMaster.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="EVS006 create panel with BOD description set to SupplierPartyMaster"><figcaption><p>Historical EVS006 create panel with SupplierPartyMaster entered as the BOD description.</p></figcaption></figure>

* [ ] Click on Next at the bottom right of the panel shown below.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="EVS006 create panel with the Next button highlighted at the bottom right"><figcaption><p>Historical EVS006 create panel with the Next button highlighted.</p></figcaption></figure>

* [ ] Click Next in this window.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Text dialog in EVS006 with empty text block fields and Next button"><figcaption><p>Historical EVS006 Text dialog with text-block fields and a Next button.</p></figcaption></figure>

* [ ] Now when you see this screen with the filled table with the BOD SupplierPartyMaster make right click on the BOD and choose Related > Run.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="EVS006 list with the right-click menu open on the SupplierPartyMaster row showing Related > Run"><figcaption><p>Historical EVS006 list with the Related → Run menu open on the SupplierPartyMaster row.</p></figcaption></figure>

* [ ] In this next window select “Sync” and next.

<figure><img src="../../../.gitbook/assets/m3-supplier-initial-load-job-historical-id-masked-20261102.png" alt="EVS007 Initial Load Job for CIDMAS and SupplierPartyMaster with BOD verb Sync and status 1-Pending"><figcaption><p>Historical EVS007 Initial Load Job showing CIDMAS, SupplierPartyMaster, Sync and status 1-Pending. The job identifier is masked; the pending status does not prove a completed import.</p></figcaption></figure>

The historical screens illustrate an initial-load setup; they do not prove that a transfer into DocBits has completed. Check the EVS006 run history and the ION routing for the intended company, division and supplier scope, then search for representative suppliers in DocBits. A supplier shown in an existing screenshot is not evidence that this M3 import ran successfully.

### Check the DocBits search view

In Supplier Management, the English search control is labelled “Search by Name, Number”. This current view shows the available search control only. It does not establish that M3 supplier master data has arrived or that a transfer completed; verify the intended records in the appropriate destination for your configured integration.

<figure><img src="../../../.gitbook/assets/supplier-search-native-en-20261102.png" alt="Current English empty Supplier Management search control showing Search by Name, Number and the unopened filter icon"><figcaption><p>Current English Supplier Management search control. Existing supplier rows, names, totals and account details are outside the crop. No search or M3 import was performed for this image.</p></figcaption></figure>
