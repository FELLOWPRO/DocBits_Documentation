# LN Configuration

This guide combines historical Infor ION examples with the current DocBits LN export form. The Infor images illustrate the individual steps; their tenant names, mapping names and layout are examples. Check the connection points, mapping package and BOD permissions with your Infor administrator for your LN company before activating a flow. No Infor tenant connection or invoice export was tested for this documentation update.

## Prerequisites

You have created:

* An ION API Endpoint
* An ION API File
* A BOD Mapping File
* An IDM Mapping File

## Import Mapping Files

Before you set up the data flow, you need to import the mapping files into InforOS

In ION Desk → Connect and open Mappings

<figure><img src="https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k" alt="Historical example: iON Desk navigation with the Connect group expanded and the entries Data Flows, API Flows, Connection Points, File Templates and Enterprise Locations."><figcaption><p>Historical example: iON Desk navigation with the Connect group expanded and the entries Data Flows, API Flows, Connection Points, File Templates and Enterprise Locations. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

Click on the Import icon

<figure><img src="https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0" alt="Historical example: mappings toolbar in historical ION Desk with the import control circled."><figcaption><p>Historical example: mappings toolbar in historical ION Desk with the import control circled. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

* From here you need to select the various mapping files you will need which include: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.
* Once you have imported all the mappings files, make sure to approve each of them by clicking the tick icon within each of their squares on the Mapping dashboard.

## DocBits to LN

The next step is to setup the Data Flow in ION Desk, navigate to the ION Desk application and select Data Flow → + ADD → Document Flow like below

<figure><img src="https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I" alt="Historical example: data Flows page in ION Desk with the navigation on the left, the flow DF_SLTStAPI in the list and the menu entries Document Flow and Data Lake Flow."><figcaption><p>Historical example: data Flows page in ION Desk with the navigation on the left, the flow DF_SLTStAPI in the list and the menu entries Document Flow and Data Lake Flow. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

Use this canvas to build the flow of information from DocBits to LN.

<figure><img src="https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8" alt="Historical example: new Document Flow with the empty properties panel and the messages Document flow name must be specified and The document flow has no activities."><figcaption><p>Historical example: new Document Flow with the empty properties panel and the messages Document flow name must be specified and The document flow has no activities. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

An LN data flow will look similar to what is shown below (there are multiple paths due to each individual path being meant for a specific document type, for this explanation we will focus on the invoice data flow).

<figure><img src="https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U" alt="Historical example: data Flow canvas with several paths for different document types, each path built from a DocBits connection point, a mapping and an LN connection point."><figcaption><p>Historical example: data Flow canvas with several paths for different document types, each path built from a DocBits connection point, a mapping and an LN connection point. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

All parts of the chain are dragged and dropped from the top section

In the chain, DocBits and LN are both Applications whereas in between them there are mappings that convert the data into a form that can be understood by the next section of the dataflow and “map” the information so that it goes to where it is needed or meant too.

<figure><img src="https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM" alt="Historical ION activity palette and flow: Application activities represent DocBits and LN, with Mapping activities between them."><figcaption><p>Historical ION activity palette and flow: Application activities represent DocBits and LN, with Mapping activities between them. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

### DocBits Application

Give it the appropriate name such as “DocBits” then select the plus sign and search for the connection point you created earlier such as DocBits\_Export or similar and click on it.

To create this connection point, go to ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530" alt="Historical example: iON Desk navigation with the Connect group expanded and the entries Data Flows, API Flows, Mappings and Connection Points."><figcaption><p>Historical example: iON Desk navigation with the Connect group expanded and the entries Data Flows, API Flows, Mappings and Connection Points. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

Click “+ Add”

<figure><img src="https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos" alt="Historical example: connection Points page in ION Desk with the Connect group open in the navigation."><figcaption><p>Historical example: connection Points page in ION Desk with the Connect group open in the navigation. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

Select “IMS via API Gateway” and fill in the following information

<figure><img src="https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I" alt="Historical IMS via API Gateway connection point with an example logical ID and a redacted ION API Client Id field."><figcaption><p>Historical IMS via API Gateway connection point with an example logical ID and a redacted ION API Client Id field. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

The ION API client ID is the `ci` value in your `.ionapi` file. Obtain the tenant-specific file from your authorised Infor administrator. It contains credentials; keep it out of screenshots, tickets and Git. See the [Infor explanation of ION API credential fields](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

Switch to the document tab, and add the Sync.CaptureDocument BOD to the DocBits connection point like below.

<figure><img src="https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg" alt="Historical example: connection point DocBits-Sandbox-Export with the Documents tab open and the document Sync.CaptureDocument assigned."><figcaption><p>Historical example: connection point DocBits-Sandbox-Export with the Documents tab open and the document Sync.CaptureDocument assigned. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

Then save the connection point by pressing the disk icon in the upper-left corner.

Navigate back to the Dataflow section of ION Desk to access your dataflow. Your DocBits application should look similar to what is shown below.

<figure><img src="https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw" alt="Historical Application Activity Properties with the application name DocBits-Sandbox and its selected connection point DocBits-Sandbox-Export."><figcaption><p>Historical Application Activity Properties with the application name DocBits-Sandbox and its selected connection point DocBits-Sandbox-Export. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

### Mapping 1

The first mapping node should look as follows

<figure><img src="https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY" alt="Historical first mapping properties: Capture2sync with the example mapping LN_CaptureDocumentToSupplierInvoice_1."><figcaption><p>Historical first mapping properties: Capture2sync with the example mapping LN_CaptureDocumentToSupplierInvoice_1. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

### Mapping 2

The second mapping node should look as follows

<figure><img src="https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao" alt="Historical second mapping properties: Load2Process with the example mapping LoadSupplierToProcessSupplierInvoice."><figcaption><p>Historical second mapping properties: Load2Process with the example mapping LoadSupplierToProcessSupplierInvoice. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

### LN Application

There should already be an LN or similarly named connection point (for the appropriate LN company) created in INFOR so, just like the DocBits Application you select it by clicking the “+” sign and it should look as follows

<figure><img src="https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE" alt="Historical LN Application Activity Properties with the example name LN-200 and the selected application connection In01_0200."><figcaption><p>Historical LN Application Activity Properties with the example name LN-200 and the selected application connection In01_0200. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

### BODs

<figure><img src="https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk" alt="Historical example: data Flow canvas with the nodes DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder and AdvancedShip above the entry End."><figcaption><p>Historical example: data Flow canvas with the nodes DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder and AdvancedShip above the entry End. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

The following configurations should look as follows:

#### First

<figure><img src="https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY" alt="Historical Documents list for the first step showing Sync.CaptureDocument."><figcaption><p>Historical Documents list for the first step showing Sync.CaptureDocument. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

#### Second

<figure><img src="https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8" alt="Historical Documents list for the second step showing Load.SupplierInvoice."><figcaption><p>Historical Documents list for the second step showing Load.SupplierInvoice. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

#### Third

<figure><img src="https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw" alt="Historical Documents list for the third step showing Process.SupplierInvoice."><figcaption><p>Historical Documents list for the third step showing Process.SupplierInvoice. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>

The last icon should be empty as it is not carrying any document or information.

After your Infor administrator has verified all nodes, mappings and document subscriptions, use the activation control for the intended flow. The historical screenshot below marks that control; its old flow name contains M3 and must not be used as the name or destination for your LN setup.

<figure><img src="https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o" alt="Historical Document Flow toolbar with the activation control circled. The legacy example is named DocBits-Export-M3; choose the correct LN flow in your tenant."><figcaption><p>Historical Document Flow toolbar with the activation control circled. The legacy example is named DocBits-Export-M3; choose the correct LN flow in your tenant. Confirm the corresponding settings in your Infor tenant.</p></figcaption></figure>



## Configure export in DocBits

Open **Settings → Export** in the intended DocBits organisation. The list shows existing export configurations; select **New** to prepare a new configuration.

<figure><img src="../../../.gitbook/assets/dbdc-196-export-list-en-20261030.png" alt="Current English DocBits Export list with New and the table headers; existing configuration rows are covered."><figcaption><p>New opens a configuration form. Existing rows are covered in this documentation image; no saved configuration was opened or changed.</p></figcaption></figure>

Under **Basic Information**, enter a **Configuration Title**, select the **Document Type** (Invoice for the example), and select a **Sub-Organization** only if your setup requires one. Choose **Infor** for **Export**, then **Infor IDM + LN** for **Infor Type**.

Provide all three files required for a new LN configuration: the **ION API File** (`.ionapi`), **IDM Mapping File** (`.properties`) and **LN Mapping File** (`.properties`). Obtain the files for this tenant and LN company from the authorised Infor administrator. The screenshot deliberately leaves every upload empty and contains no credentials.

<figure><img src="../../../.gitbook/assets/dbdc-196-export-ln-en-20261030.png" alt="Current blank English DocBits form with Infor IDM + LN and Invoice selected and empty ION API, IDM Mapping and LN Mapping file fields."><figcaption><p>The current LN form separates the three upload fields. Basic Information identifies the destination type and document type; this example was canceled without files or a saved configuration. The existing execution-order panel is outside this detail view.</p></figcaption></figure>

After your administrator has confirmed the ION flow and files, save the configuration and test one authorised non-production invoice. Check the result in DocBits, Infor ION and LN. A saved configuration alone does not prove that LN received an invoice. Cancel the form if you are only inspecting the available fields.

For the roles of connection points and document flows, see the [Infor ION explanation](https://docs.infor.com/ln/10.8/en-us/lnesolh/lnoshybridng/wxa1699288671147.html).
