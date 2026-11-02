# Suppliers and Purchase Orders from Infor M3

This example connects M3 supplier and purchase-order BODs to DocBits through Infor ION. The fifteen Infor images below are historical tenant examples, not current validation of your M3 setup. Ask the Infor administrator to confirm the BOD names, source tables, company, division, API call names and target environment before running a job. No M3 initial load or DocBits import was executed for this update.

Infor's [initial-load guide](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html) explains EVS006 definitions, the EVS007 verb and selection, submission, and history. Use a limited selection first; an unrestricted run can generate many events.

## **Connection Point**

You will need to create the DocBits API connection point in order to create the data flow later.

In InforOS, navigate to ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o" alt="Historical ION Desk navigation with Connect expanded and Connection Points highlighted."><figcaption><p>Historical navigation: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Once here, you will need to create a new connection point.

<figure><img src="https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI" alt="Historical Connection Points page with a green arrow pointing to Add."><figcaption><p>Historical Add action for creating a connection point.</p></figcaption></figure>

**Select API**

Give the connection point a name and description that describes its nature and its environment. Under the Connection tab, import the service account you created for the environment you are working with.

<figure><img src="https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0" alt="Historical DocBits-DEV-Demo-Import API connection point with Connection selected and a service-account Import control."><figcaption><p>Historical Connection tab. The displayed names refer to the example environment; use your own service account.</p></figcaption></figure>

Next, switch to the Documents tab. You will need to add the following BODs to the connection point, not all are necessary for the supplier and purchase order master data but will be useful when other features such as Auto Accounting need to be implemented.

<figure><img src="https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8" alt="Historical Documents tab listing Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster and Sync.SupplierPartyMaster."><figcaption><p>Historical received-document list. The supplier BOD shown is Sync.RemitToPartyMaster, without a Data suffix.</p></figcaption></figure>

This historical setup uses Sync.RemitToPartyMaster, Sync.SupplierPartyMaster and Sync.PurchaseOrder. Confirm the required BODs for your DocBits mapping; the setup can vary by tenant and feature.

* Sync.RemitToPartyMaster and Sync.SupplierPartyMaster

The following historical image shows Sync.SupplierPartyMaster. Configure each required supplier BOD with the API call name and receiving operation confirmed for your environment; the second supplier route is not pictured.

<figure><img src="https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk" alt="Historical ION API tab with Send to API selected, API Call Name Sync.SupplierPartyMaster and a POST operation."><figcaption><p>Historical SupplierPartyMaster route. The image shows one supplier route; confirm the receiving operation separately for each required BOD.</p></figcaption></figure>

* Sync.PurchaseOrder

The following historical image shows one purchase-order receiving operation. Confirm its current endpoint and request format for your environment.

<figure><img src="https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4" alt="Historical ION API tab with Send to API selected for Sync.PurchaseOrder and a POST operation."><figcaption><p>Historical PurchaseOrder route. The old API Gateway proxy path is an example, not a universal DocBits address.</p></figcaption></figure>

Once these BODs are configured, you can save the connection point by pressing the icon located right to the back button.

## **Data Flow**

This historical data flow is one possible design; check its routes and receiving organisation in your own tenant.

<figure><img src="https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8" alt="Historical flow from M3 through a Yes or No filter, then a parallel split to four DocBits API nodes, with join and end nodes."><figcaption><p>Historical flow. The No branch ends before the API nodes; the Yes branch reaches the four example environments.</p></figcaption></figure>

The multiple DocBits API nodes represent separate environments in this example. Your design may differ; check that test messages cannot reach production.

Four environments are shown only as an example.

### **M3**

The start of the data flow consists of your M3 application

### **Filter**

Configuration of the filter looks as follows

<figure><img src="https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY" alt="Historical Filter Properties panel with Properties selected and Name and Description both set to Division."><figcaption><p>Historical filter name and description. The name Division alone does not establish which records are filtered.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA" alt="Historical Filter Properties Attributes tab listing AccountingEntityID attributes for ChartOfAccounts, PurchaseOrder, RemitToPartyMaster and SupplierPartyMaster."><figcaption><p>Historical attributes: each BOD has an AccountingEntityID path. Review the path for each document in your tenant.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw" alt="Historical Filter Properties Conditions tab showing ChartOfAccounts, Used Condition set to Not Filtered and an example expression for AccountingEntityID_3."><figcaption><p>Historical Conditions example. Used Condition reads Not Filtered even though an expression is listed; check the selected condition and its effect instead of assuming that the expression is active.</p></figcaption></figure>

(The accounting entity ID of course being unique to your organization)

### **DocBits API**

Here you will add an application and select the DocBits API(s) you created earlier

### **Documents**

Select the documents assigned to the M3 source and receiving nodes. Confirm that the filter attributes and receiving routes cover every required document.

<figure><img src="https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY" alt="Historical M3 flow with its document icon highlighted and a Documents panel listing Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster and Sync.SupplierPartyMaster."><figcaption><p>Historical document selection for the M3 flow. This is a BOD document list, not a file-node configuration.</p></figcaption></figure>

## **M3 BOD Triggering**

Navigate to the Infor M3 application

Open the M3 **Search and Start** control, enter **EVS006**, and confirm the program. Use the navigation supported by your M3 client.

<figure><img src="https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o" alt="Historical M3 Search and Start dialog containing evs006 and an OK button."><figcaption><p>Historical program search: enter EVS006 in Search and Start.</p></figcaption></figure>

In EVS006, define the BOD nouns required for your approved mapping. The historical example uses SupplierPartyMaster, RemitToPartyMaster and PurchaseOrder. Confirm their M3 table names in your version before creating an initial-load definition.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Use the add action for each approved definition. Check company and division before continuing.

<figure><img src="https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw" alt="Cropped historical EVS006 toolbar with Add highlighted above empty BOD noun, BOD variant, BOD and Table fields."><figcaption><p>Historical Add action in EVS006. This crop does not show completed initial-load definitions.</p></figcaption></figure>

After you have added each of the BODs, right click on the BOD noun of the BOD and select Related → Run

<figure><img src="https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo" alt="Historical context menu with Related expanded and Run highlighted; History is listed below it."><figcaption><p>Historical Related → Run action. Use History later to inspect the initial-load result.</p></figcaption></figure>

The related **Run** action opens EVS007. Choose **Sync** only when the receiving ION flow expects it. Inspect the selection and filters before the final submission; moving to the next screen is not proof of delivery.

<figure><img src="https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA" alt="Historical EVS007 Initial Load Job screen for CIDMAS and SupplierPartyMaster, status Pending, with the BOD verb menu open and Sync annotated while Show is still displayed."><figcaption><p>Historical EVS007 verb selection before execution. The image shows a pending job and an annotated Sync option; it does not prove that Sync was selected or that data was imported.</p></figcaption></figure>

A submission notification confirms that the job was requested. In EVS006 **History**, inspect the processed count and errors. Then check the message and target in Infor ION.

## Verify in DocBits

Open **Settings → Document Processing → Lookup Master Data → BOD Input data → Supplier** in the intended DocBits organisation. Choose the identifier field in **Search by column**, enter a known supplier number or name in **Search String**, and use the magnifier to search. Then open **Purchase Order** and search for a known purchase-order number; check **Purchase Order Header** if your mapping separates header and line data. Compare identifiers and company with the M3 source. A successful EVS007 request alone does not establish that all records arrived.

<figure><img src="../../../.gitbook/assets/dbdc-185187-supplier-en-20261029.png" alt="English DocBits Lookup Master Data Supplier view with search controls; record rows are outside the captured area."><figcaption><p>Supplier verification view in Dev. Search for a known test identifier and compare it with M3 and ION.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc-185187-purchase-order-en-20261029.png" alt="English DocBits Lookup Master Data Purchase Order view with search controls; record rows are outside the captured area."><figcaption><p>Purchase Order verification view in Dev. The record rows are outside this image; this is not evidence of an M3 import.</p></figcaption></figure>

The English Dev views were inspected on 29 October 2026 without running an M3 job, importing a file or changing master data. Record rows are excluded from the images; the images demonstrate where to check, not a completed transfer. If an expected record is missing, check EVS006 history, ION routing, the BOD mapping and the DocBits organisation before rerunning.
