# How to import all suppliers

* [ ] Log yourself into the Infor OS environment and go to the M3 application. Recommendation: Make sure you have admin rights in order to be able to run all the programs.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Infor M3 start menu in Infor OS with the program list, Favorites and Recent panels and the evs006 search field open"><figcaption></figcaption></figure>

* [ ] Run the program _**evs006**_. Press command + R and you will see the open tab to search and start.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Infor M3 start menu with the search field showing evs006 Initial Load ready to open under Recent"><figcaption><p><em><strong>evs006</strong></em></p></figcaption></figure>

* [ ] When _**evs006**_ is open you will see an empty table. Please fill the columns of “BOD noun” and “Table”. For “BOD noun” introduce “SupplierPartyMaster” and for “Table” we are going to use the M3 supplier table called “CIDMAS”.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Infor M3 menu screen with the search field opened for starting a program"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="EVS006 Initial Load table with the columns BOD noun, BOD variant, Table and BOD description"><figcaption></figcaption></figure>

* [ ] When you have filled these columns, just click on CREATE button (on the upper bar side of the screen). You will come to following screen.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="Empty EVS006 Initial Load table with the column headers BOD noun, BOD variant, Table and BOD description"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="EVS006 Initial Load panel with Table CIDMAS Supplier, BOD noun SupplierPartyMaster and the Details and Table keys sections"><figcaption></figcaption></figure>

* [ ] Fill the “BOD Description” with SupplierPartyMaster.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="EVS006 Initial Load panel with BOD description SupplierPartyMaster filled in under Details"><figcaption></figcaption></figure>

* [ ] Click on Next. (On the down left side of the screen).

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="EVS006 Initial Load panel for table CIDMAS with BOD noun SupplierPartyMaster and the Next button at the bottom left"><figcaption></figcaption></figure>

* [ ] Click Next in this window.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Text dialog in M3 with the columns Text block and Language and the name InvExt"><figcaption></figcaption></figure>

* [ ] Now when you see this screen with the filled table with the BOD SupplierPartyMaster make right click on the BOD and choose Related > Run.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="EVS006 Initial Load table with the SupplierPartyMaster row and its right-click context menu including Related, Run and Change"><figcaption></figcaption></figure>

* [ ] In this next window select “Sync” and next.

<figure><img src="../../../.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png" alt="BOD Processor Administration panel in Infor M3 with the SupplierPartyMaster job, verb Sync and status Pending"><figcaption></figcaption></figure>

After finishing all these steps you have activated the BOD to import all suppliers from table CIDMAS. After some minutes you should see the supplier in DocBits.
