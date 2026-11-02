# Export to Infor LN

This guide combines an example Infor ION document flow with the current DocBits export form. The Infor images are historical examples and were not checked in an Infor tenant. Check the connection points, mapping names and BOD permissions with your Infor administrator before activating the flow. No LN export was run for this update.

## Prerequisites

You have created:

* An ION API Endpoint
* An ION API File
* A BOD Mapping File
* An IDM Mapping File

## Import Mapping Files

Before setting up the document flow, ask your Infor administrator to import and approve the mapping files in your Infor OS tenant. The names below are examples; confirm which mapping package applies to your LN company.

In ION Desk → Connect and open Mappings

![Historical Infor ION Desk Connect Mappings screen before importing mapping files.](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu\_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ\_aAIxcJil5LNiep4U6KZr3\_tBfs1RRwXoW749q3FUxurXy\_pT\_k)

Click on the Import icon

![Historical Infor ION mapping import action.](https://lh7-us.googleusercontent.com/d\_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn\_Vd\_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* From here you need to select the various mapping files you will need which include: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.
* Once you have imported all the mappings files, make sure to approve each of them by clicking the tick icon within each of their squares on the Mapping dashboard.

## DocBits to LN

The next step is to setup the Data Flow in ION Desk, navigate to the ION Desk application and select Data Flow → + ADD → Document Flow like below

![Historical Infor ION new document flow action.](https://lh7-us.googleusercontent.com/rjPVR1EFKw\_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a\_Fn3s1HSYDRmQVvgZtX\_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Use this canvas to build the document flow from DocBits to LN.

![Historical empty ION document flow canvas for DocBits to LN.](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x\_-lVRbK6tpTxvbRYKvwyWO\_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

An LN data flow will look similar to what is shown below (there are multiple paths due to each individual path being meant for a specific document type, for this explanation we will focus on the invoice data flow).

![Historical example of a DocBits to LN invoice document flow with several mappings.](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn\_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD\_3myQY4Qcd9motySYh9U)

All parts of the chain are dragged and dropped from the top section

In the chain, DocBits and LN are both Applications whereas in between them there are mappings that convert the data into a form that can be understood by the next section of the dataflow and “map” the information so that it goes to where it is needed or meant too.

![Historical ION flow node palette and connected applications.](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0\_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC\_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### DocBits Application

Give it the appropriate name such as “DocBits” then select the plus sign and search for the connection point you created earlier such as DocBits\_Export or similar and click on it.

To create this connection point, go to ION Desk → Connect → Connection Points

![Historical Infor ION connection points list for the DocBits application.](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l\_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Click “+ Add”

![Historical Infor ION Add connection point action.](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc\_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ\_vj\_-XPdegP1P0ySdos)

Select “IMS via API Gateway” and fill in the following information

![Historical IMS via API Gateway connection point form.](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

The ION API client ID is the `ci` value in your `.ionapi` file. Ask your Infor administrator for the tenant-specific file. It contains credentials, so keep it out of screenshots and Git. See the [Infor explanation of ION API credential fields](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

Switch to the document tab, and add the Sync.CaptureDocument BOD to the DocBits connection point like below.

![Historical document tab with Sync.CaptureDocument for the DocBits connection point.](https://lh7-us.googleusercontent.com/Wy2BIr1z\_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE\_333uCWuKvKiVoo99FrXVg)

Then save the connection point by pressing the disk icon in the upper-left corner.

Navigate back to the Dataflow section of ION Desk to access your dataflow. Your DocBits application should look similar to what is shown below.

![Historical DocBits application node linked to its connection point.](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa\_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)

### Mapping 1

The first mapping node should look as follows

![Historical first mapping node in the LN invoice flow.](https://lh7-us.googleusercontent.com/9tlIun\_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw\_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Mapping 2

The second mapping node should look as follows

![Historical second mapping node in the LN invoice flow.](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### LN Application

Your Infor administrator should provide an LN connection point for the appropriate company. Select it using the “+” action on the LN application node, then verify its document subscriptions.

![Historical LN application node linked to an LN connection point.](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O\_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![Historical BOD flow configuration in ION Desk.](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

The following configurations should look as follows:

#### First

![Historical first BOD configuration in the LN document flow.](https://lh7-us.googleusercontent.com/rj\_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn\_lmxtqUDVTm\_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Second

![Historical second BOD configuration in the LN document flow.](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y\_MF\_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc\_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Third

![Historical third BOD configuration in the LN document flow.](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q\_epAj9\_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ\_rbCCixhWcaJg2kHyyYw)

The last icon should be empty as it is not carrying any document or information.

Once you have added all necessary nodes to the data flow, press this button to activate the data flow

![Historical action used to activate an Infor ION document flow.](https://lh7-us.googleusercontent.com/WjQeGz\_effl\_RlkWC4CdJS9Dg\_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)



## Configure export in DocBits

Open **Settings → Export** in the correct DocBits organisation, then select **New**. The English Sandbox test organisation shown below has no saved export configuration.

![Current English DocBits Sandbox Export list with the New action and no saved configuration.](../../../.gitbook/assets/dbdc-196-export-list-en.png)

Under **Basic Information**, enter a **Configuration Title**, select the **Document Type** (for this example, Invoice), and select a **Sub-Organization** only if your setup requires one. Choose **Infor** for **Export**, then choose **Infor IDM + LN** for **Infor Type**. Confirm these values before adding credentials.

The current form asks for an **ION API File** (`.ionapi`, required), **IDM Mapping File** (`.properties`), and **LN Mapping File** (`.properties`). The form in this screenshot is deliberately blank. Use only files supplied by the authorised Infor administrator for this tenant. Do not attach the `.ionapi` file to tickets or include it in the repository.

![Current English DocBits Sandbox Export configuration with Infor IDM + LN selected and the three empty file upload fields.](../../../.gitbook/assets/dbdc-196-export-ln-en.png)

After the Infor administrator confirms the ION flow and files, save the configuration and test a single non-production invoice. Check the result in DocBits, Infor ION and LN. A saved configuration alone does not show that LN received the invoice.

For the roles of connection points and document flows, see the [Infor ION explanation](https://docs.infor.com/ln/10.8/en-us/lnesolh/lnoshybridng/wxa1699288671147.html). The historical Infor screens above still need comparison with your own tenant.
