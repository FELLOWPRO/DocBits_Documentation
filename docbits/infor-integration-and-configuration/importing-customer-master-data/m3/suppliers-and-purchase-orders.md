# Suppliers and Purchase Orders

## **Connection Point**

You will need to create the DocBits API connection point in order to create the data flow later.

In InforOS, navigate to ION Desk → Connect → Connection Points

![ION Desk navigation with the Connect group expanded and the entries Data Flows, API Flows, Mappings, Connection Points and File Templates](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Once here, you will need to create a new connection point.

![Connection Points page in ION Desk with the Connect group open in the navigation and the breadcrumb Home and Connection Points](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Select API**

Give the connection point a name and description that describes its nature and its environment. Under the Connection tab, import the service account you created for the environment you are working with.

![API Connection Point dialog DocBits-DEV-Demo-Import with the tabs Usage, Connection and Documents, the name DocBits-DEV-Demo-Import, the authentication entry DocBits-DEV-Demo-Import Service Account and the Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Next, switch to the Documents tab. You will need to add the following BODs to the connection point, not all are necessary for the supplier and purchase order master data but will be useful when other features such as Auto Accounting need to be implemented.

![Documents tab of the connection point with the BODs Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster and Sync.SupplierPartyMaster and a checkbox in each row](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

For now we will only focus on the necessary BODs, these being: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster and Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData and Sync.SupplierPartyMaster

The configuration for these two BODs should look similar to the following (API Call Name changing for each)

![BOD configuration with the tabs Input Document, ION API, Request Parameters, Request Body and Settings and the fields API Call Name Sync.SupplierPartyMaster, Product DocBits-DEV and the Operation POST CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

The configuration for this BOD should look similar to the following

![BOD configuration with the tabs Input Document, ION API, Request Parameters, Request Body and Settings and the fields API Call Name Sync.PurchaseOrder, Product DocBits-DEV and the Operation POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Once these BODs are configured, you can save the connection point by pressing the icon located right to the back button.

## **Data Flow**

The data flow will look similar to the following

![Data flow canvas in ION Desk with one M3 node on the left, several DocBits nodes labelled DocBits-DEV-P, DocBits-DEV-S and DocBits-DEV-D in the middle, an End node and a condition with Yes and No branches](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(The reason for multiple DocBits APIs is due to each connection representing a different environment meaning, depending on the amount of environments you have, your data flow could differ slightly)

For the purpose of this explanation we will use the example of having four separate environments.

### **M3**

The start of the data flow consists of your M3 application

### **Filter**

Configuration of the filter looks as follows

![Filter Properties panel with the tabs Properties, Attributes and Conditions and the fields Name and Description without entries](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Filter Properties panel with the Attributes tab open and the rows AccountingEntityID_3 for ChartOfAccounts, AccountingEntityID for PurchaseOrder, AccountingEntityID_1 for RemitToPartyMaster and AccountingEntityID_2 for SupplierPartyMaster, all of type STRING with the path DataArea/*/AccountingEntityID](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Filter Properties panel with the Conditions tab open, the Document ChartOfAccounts, the condition Not Filtered and the row DIV780AAA with the expression AccountingEntityID_3 equals 780_AAA](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(The accounting entity ID of course being unique to your organization)

### **DocBits API**

Here you will add an application and select the DocBits API(s) you created earlier

### **Files**

The configuration should look as follows

![Data flow detail with the M3 node on the left, the condition node and the DocBits nodes, the Start and End markers and the Documents panel listing Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster and Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **M3 BOD Triggering**

Navigate to the Infor M3 application

Once at the main menu, type Command + R to open the command prompt search box. Then type evs006 and search.

![Search and Start dialog in Infor M3 with the search field for a command](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Once on this page, you will need to add the SupplierPartyMaster, RemitToPartyMaster and PurchaseOrder to the list.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

For each case you will need to press the plus icon to add them to list.

![EVS006 panel header with the menus ACTIONS, OPTIONS, RELATED and TOOLS and the columns BOD noun, BOD variant and BOD description](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

After you have added each of the BODs, right click on the BOD noun of the BOD and select Related → Run

![Related menu in Infor M3 with the entries Drill down, Select, Run, Change, History, Copy, Delete, Display and the shortcut keys next to them](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

You will be taken to the following menu, where you will need to change BOD verb to Sync and then press NEXT to trigger the BODs.

![EVS007 Initial Load Job Open panel with the table CIDMAS, the BOD noun SupplierPartyMaster, the job number 243249962976569068, the status 1-Pending and the BOD verb set to Sync](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Once you trigger the BODs, you will get a notification confirming this.

If done successfully, the Supplier and Purchase Order tables should now be available under Settings → Master Data Lookup.


