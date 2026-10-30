# Suppliers and Purchase Orders from Infor LN

This example covers the Infor ION route for supplier and purchase-order BODs and where to verify them in DocBits. The fourteen Infor screenshots below are historical tenant examples. Confirm connection points, API call names and LN publishing options with your integration administrator; they were not verified in an Infor tenant for this update. No BOD was published or imported during this update.

Infor explains the [LN logistic master-data publisher](https://docs.infor.com/ln/latest/en-us/lnolh/tcolh/help/tc/bod/tcbod0200m000.html) and [order-management transactional publisher](https://docs.infor.com/ln/2025.x/en-us/lnolh/tdolh/help/td/bod/tdbod0200m000.html). Their modes have different effects: **Count** reports record totals without publishing; **Simulate** builds a trial result without committing the publication; **Publish** sends the selected data. Publication can reach all subscribers, so check the company range and subscribers before running it.

## **Connection Point**

You will need to create the DocBits API connection point in order to create the data flow later.

First, in InforOS, navigate to ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE" alt="Historical Infor ION Desk navigation with Connect expanded and Connection Points highlighted."><figcaption><p>Historical navigation example: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Once here, you will need to create a new connection point.

<figure><img src="https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU" alt="Historical Connection Points screen with a green arrow pointing to Add."><figcaption><p>Choose Add to create a connection point; the green annotation marks the action in this historical UI.</p></figcaption></figure>

**Select API**

Give the connection point a name and description that describes its nature and its environment. Under the Connection tab, import the service account you created for the environment you are working with.

<figure><img src="https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0" alt="Historical DocBits-DEV-Demo-Import API connection point with Connection selected and a service-account Import control."><figcaption><p>Historical Connection tab. The displayed service-account and connection names belong to the example environment.</p></figcaption></figure>

Next, switch to the Documents tab. You will need to add the following BODs to the connection point.

<figure><img src="https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg" alt="Historical German Documents tab listing Ack-SupplierInvoice, Sync.PurchaseOrder and Sync.ReceiveDelivery API calls and received BODs."><figcaption><p>Historical Dokumente (Documents) tab. This crop shows three routes; it does not show the complete supplier configuration.</p></figcaption></figure>

* Ack-SupplierInvoice

This BOD is used to signal on DocBits that an error has occurred within Infor. The Acknowledge.SupplierInvoice route shown below is an example for invoice acknowledgements. Confirm its API call name and whether this route is needed for your supplier/purchase-order flow.

<figure><img src="https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y" alt="Historical German ION API tab for Ack-SupplierInvoice with a POST operation selected."><figcaption><p>Historical acknowledgement route. Ack-SupplierInvoice is an example API call name; Acknowledge.SupplierInvoice is the received BOD.</p></figcaption></figure>

* Sync.PurchaseOrder

The historical example below shows one receiving operation; confirm the current operation and request format for your environment.

<figure><img src="https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0" alt="Historical ION API tab with Send to API selected for Sync.PurchaseOrder and a POST operation configured."><figcaption><p>Historical purchase-order route. Review the receiving operation for your DocBits environment instead of copying the old proxy path.</p></figcaption></figure>

* Sync.ReceiveDelivery

The historical example below shows one receiving operation; confirm the current operation and request format for your environment.

<figure><img src="https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc" alt="Historical German ION API tab for Sync.ReceiveDelivery with a POST operation configured."><figcaption><p>Historical receiving-data route. Confirm whether ReceiveDelivery is required for your integration and which operation receives it.</p></figcaption></figure>

Once these BODs are configured, you can save the connection point by pressing the icon located right to the back button.

## **Data Flow**

The data flow will look similar to the following

<figure><img src="https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU" alt="Historical document flow from an LN node through a parallel split to four DocBits API nodes, followed by a join and end."><figcaption><p>Historical four-environment flow. The split and join are visible; the number and destinations of nodes depend on your integration design.</p></figcaption></figure>

The multiple DocBits API nodes in this historical example represent separate environments. Your production design may use a different number of nodes; never route test data into a production organisation.

The following illustration uses four environments only as an example.

### **LN**

The start of the data flow consists of your LN application

### **DocBits API**

Here you will add an application and select the DocBits API(s) you created earlier

### **Documents**

Review the document list assigned to the flow. The supplier messages shown here also need corresponding receiving routes in the API connection point. Their API call configuration is not shown in the earlier three-route crop; confirm the required operations with your integration administrator.

<figure><img src="https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU" alt="Historical flow canvas with the German Dokumente panel below listing Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster and Sync.SupplierPartyMaster."><figcaption><p>Historical document list for the flow. Supplier messages appear here as well as purchase-order and receipt messages.</p></figcaption></figure>

## **LN BOD Triggering**

After the integration administrator has checked the connection point, document routes and active data flow, use the appropriate LN publishing session. Follow each test identifier through LN, ION and DocBits; triggering a BOD alone does not prove that a record arrived.

<figure><img src="https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y" alt="Historical German Infor LN home page with a favorites list; the Publish BODs menu is not open."><figcaption><p>Historical LN starting page. Use the navigation described below to find the appropriate publication session.</p></figcaption></figure>

### **PurchaseOrder**

From the above menu, in the left menu tab, select Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Select the PurchaseOrder tab and check the box.

<figure><img src="https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco" alt="Historical Publish Order Management Transactional Data session with the PurchaseOrder tab and checkbox selected and order-range fields visible."><figcaption><p>Historical PurchaseOrder selection. Review the order range and statuses before publishing.</p></figcaption></figure>

### **Suppliers**

From the LN homepage, in the left menu tab, navigate to Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Select the PartyMaster tab and check the Supplier → Buy-from or SupplierPartyMaster box.

<figure><img src="https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0" alt="Historical Publish Logistic Master Data session with PartyMaster selected and the Supplier Buy-from checkbox checked."><figcaption><p>Historical supplier selection on PartyMaster. Choose the partner roles needed by your integration and check the selection range.</p></figcaption></figure>

### **BOD Triggering**

Once all the correct BODs have been checked for publication, select the Options tab.

Review the options for your tenant. The historical example highlights Publish and Use Process/Sync Verb; these are not universal settings for every integration.

<figure><img src="https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U" alt="Historical LN Options tab with Publish and Use Process/Sync Verb highlighted and a company range visible."><figcaption><p>Historical Options example. Publish and Use Process/Sync Verb are selected here; verify mode, company range and subscribers for your own run.</p></figcaption></figure>

Before **Process**, use **Count** or **Simulate** and inspect the record count and company range where your LN version offers those modes. Publish only with the integration administrator’s approval. A confirmation that BODs were triggered does not prove delivery to DocBits.

<figure><img src="https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM" alt="Historical LN Options tab with the Process button highlighted before execution."><figcaption><p>Historical Process action before execution. This screenshot contains no publication result or confirmation that DocBits received data.</p></figcaption></figure>

## Verify in DocBits

Check Infor ION for successful delivery to the intended DocBits organisation. Then open **Settings → Document Processing → Lookup Master Data**. Under **BOD Input data**, open **Supplier**. Choose the identifier field in **Search by column**, enter a known supplier number or name in **Search String**, and use the magnifier to search. Open **Purchase Order** and search for one known order number. Also check **Purchase Order Header** if your mapping separates header and lines. Compare the identifiers and company with LN; do not infer that all records arrived from a successful publish message alone.

<figure><img src="../../../../.gitbook/assets/dbdc-185187-supplier-en-20261029.png" alt="English DocBits Lookup Master Data Supplier view with search controls; record rows are outside the captured area."><figcaption><p>Supplier verification view in Dev. Use a known test identifier; the record rows are outside this image and do not prove an LN import.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-185187-purchase-order-en-20261029.png" alt="English DocBits Lookup Master Data Purchase Order view with search controls; record rows are outside the captured area."><figcaption><p>Purchase Order verification view in Dev. Compare the test order and company with LN and ION.</p></figcaption></figure>

The English Dev views were inspected on 29 October 2026 without publishing a BOD, importing a file or changing master data. Record rows are excluded from the images; these images demonstrate where to check, not a completed LN transfer. If the expected record is missing, check LN publishing logs, ION routing, organisation and BOD mapping before rerunning.
