# Suppliers and Purchase Orders from Infor M3

This example connects M3 supplier and purchase-order BODs to DocBits through Infor ION. The fifteen Infor images below are historical tenant examples, not current validation of your M3 setup. Ask the Infor administrator to confirm the BOD names, source tables, company, division, API call names and target environment before running a job. No M3 initial load or DocBits import was executed for this update.

Infor documents how to [start an initial load in EVS006](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) and [review the EVS007 selection, verb and history](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Use a limited selection first; an unrestricted run can generate many events.

## **Connection Point**

You will need to create the DocBits API connection point in order to create the data flow later.

In InforOS, navigate to ION Desk → Connect → Connection Points

![Historical Infor ION Desk connection points list for M3 to DocBits.](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Once here, you will need to create a new connection point.

![Historical Infor ION action for creating an API connection point.](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Select API**

Give the connection point a name and description that describes its nature and its environment. Under the Connection tab, import the service account you created for the environment you are working with.

![Historical environment-specific API connection point form.](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Next, switch to the Documents tab. You will need to add the following BODs to the connection point, not all are necessary for the supplier and purchase order master data but will be useful when other features such as Auto Accounting need to be implemented.

![Historical Documents tab for the DocBits API connection point.](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

This historical setup uses Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster and Sync.PurchaseOrder. Confirm the required BODs for your DocBits mapping; the setup can vary by tenant and feature.

* Sync.RemitToPartyMasterData and Sync.SupplierPartyMaster

The configuration for these two BODs should look similar to the following (API Call Name changing for each)

![Historical Sync.RemitToPartyMasterData and Sync.SupplierPartyMaster route example.](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

The configuration for this BOD should look similar to the following

![Historical Sync.PurchaseOrder route example.](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Once these BODs are configured, you can save the connection point by pressing the icon located right to the back button.

## **Data Flow**

This historical data flow is one possible design; check its routes and receiving organisation in your own tenant.

![Historical M3 to DocBits ION document flow with several environment nodes.](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

The multiple DocBits API nodes represent separate environments in this example. Your design may differ; check that test messages cannot reach production.

Four environments are shown only as an example.

### **M3**

The start of the data flow consists of your M3 application

### **Filter**

Configuration of the filter looks as follows

![Historical ION filter node configuration, first view.](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Historical ION filter node configuration, second view.](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Historical ION filter node configuration, third view.](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(The accounting entity ID of course being unique to your organization)

### **DocBits API**

Here you will add an application and select the DocBits API(s) you created earlier

### **Files**

The configuration should look as follows

![Historical file node in the M3 document flow.](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **M3 BOD Triggering**

Navigate to the Infor M3 application

Once at the main menu, type Command + R to open the command prompt search box. Then type evs006 and search.

![Historical M3 program search for EVS006.](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

In EVS006, define the BOD nouns required for your approved mapping. The historical example uses SupplierPartyMaster, RemitToPartyMaster and PurchaseOrder. Confirm their M3 table names in your version before creating an initial-load definition.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Use the add action for each approved definition. Check company and division before continuing.

![Historical EVS006 initial-load definitions for supplier and order BODs.](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

After you have added each of the BODs, right click on the BOD noun of the BOD and select Related → Run

![Historical EVS006 Related Run action.](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

The related **Run** action opens EVS007. Choose **Sync** only when the receiving ION flow expects it. Inspect the selection and filters before the final submission; moving to the next screen is not proof of delivery.

![Historical EVS007 Sync verb and run settings.](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

A submission notification confirms that the job was requested. In EVS006 **History**, inspect the processed count and errors. Then check the message and target in Infor ION.

## Verify in DocBits

Open **Settings → Lookup Master Data → BOD Input data → Supplier** in the intended DocBits organisation. Search for one expected supplier number or name. Then open **Purchase Order** and search for a known purchase-order number; check **Purchase Order Header** if your mapping separates header and line data. Compare identifiers and company with the M3 source. A successful EVS007 request alone does not establish that all records arrived.

![Current English DocBits Sandbox Lookup Master Data Supplier tab with search controls and synthetic supplier rows.](../../../.gitbook/assets/dbdc-187-supplier-en.png)

![Current English DocBits Sandbox BOD Input data Purchase Order tab with search controls and synthetic order rows.](../../../.gitbook/assets/dbdc-187-purchase-order-en.png)

The Sandbox Test A rows were already present; they are examples of where to inspect data, not evidence of an M3 import. If an expected record is missing, check EVS006 history, ION routing, the BOD mapping and the DocBits organisation before rerunning.
