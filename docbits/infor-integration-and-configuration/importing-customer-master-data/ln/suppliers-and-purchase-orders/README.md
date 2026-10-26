# Suppliers and Purchase Orders

## **Connection Point**

You will need to create the DocBits API connection point in order to create the data flow later.

First, in InforOS, navigate to ION Desk → Connect → Connection Points

![ION Desk navigation with the group Connect expanded and the entries Data Flows, API Flows, Mappings, Connection Points and File Templates](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Once here, you will need to create a new connection point.

![Connection Points page in ION Desk with the Connect group open in the navigation and the breadcrumb Home and Connection Points](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Select API**

Give the connection point a name and description that describes its nature and its environment. Under the Connection tab, import the service account you created for the environment you are working with.

![API Connection Point dialog DocBits-DEV-Demo-Import with the tabs Usage, Connection and Documents, the name DocBits-DEV-Demo-Import, the authentication entry DocBits-DEV-Demo-Import Service Account and the Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Next, switch to the Documents tab. You will need to add the following BODs to the connection point.

![Documents tab of the connection point with the rows Ack-SupplierInvoice, Sync.PurchaseOrder and Sync.ReceiveDelivery, each with the direction In and the BOD name of the same name](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

This BOD is used to signal on DocBits that an error has occurred within Infor. The configuration for these two BODs should look similar to the following (API Call Name changing for each)

![BOD configuration with the tabs Input Document, ION API, Request Parameters, Request Body and Settings and the API Call Name Ack-SupplierInvoice](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

The configuration for this BOD should look similar to the following

![BOD configuration with the tabs Input Document, ION API, Request Parameters, Request Body and Settings and the fields API Call Name Sync.PurchaseOrder, Product DocBits-DEV and the Operation POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

The configuration for this BOD should look similar to the following

![BOD configuration with the tabs Input Document, ION API, Request Parameters, Request Body and Settings and the API Call Name Sync.ReceiveDelivery](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Once these BODs are configured, you can save the connection point by pressing the icon located right to the back button.

## **Data Flow**

The data flow will look similar to the following

![Data flow in ION Desk with one DocBits connection point node on the left and the End node on the right](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(The reason for multiple DocBits APIs is due to each connection representing a different environment meaning, depending on the amount of environments you have, your data flow could differ slightly)

For the purpose of this explanation we will use the example of having four separate environments.

### **LN**

The start of the data flow consists of your LN application

### **DocBits API**

Here you will add an application and select the DocBits API(s) you created earlier

### **Files**

The configuration should look as follows

![Data flow detail with the DocBits node DocBits-DEV-P, the markers Start and End and a second DocBits node in the middle, and the Documents panel listing Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster and Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **LN BOD Triggering**

Once all the above is completed, you will need to navigate to Infor LN and trigger the BODs in order for the various master data you need for Suppliers and Purchase Orders to arrive in DocBits.

![Infor LN start page with the favourites panel on the left and the tiles for purchase orders, invoices and warehouse orders](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

From the above menu, in the left menu tab, select Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Select the PurchaseOrder tab and check the box.

![Publish Order Management Transactional Data dialog with the buttons PROCESS, CLOSE, SELECT ALL and CLEAR ALL, the selected tab PurchaseOrder and the tree on the left with BOD Messaging and Publish BODs expanded](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Suppliers**

From the LN homepage, in the left menu tab, navigate to Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Select the PartyMaster tab and check the Supplier → Buy-from or SupplierPartyMaster box.

![Publish Logistic Master Data dialog with the buttons PROCESS, CLOSE, SELECT ALL and CLEAR ALL, the selected tab PartyMaster and the grid with the columns Supplier, Buy-from PartyMaster, Pay-to PartyMaster, Pay-from PartyMaster and Remit-to PartyMaster](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **BOD Triggering**

Once all the correct BODs have been checked for publication, select the Options tab.

The following options should be selected.

![Publish Logistic Master Data dialog with the Mode picker, the section Selection Range with the company 0051 and the section BOD Messaging Settings](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Once this is complete, press the PROCESS button and the BODs will be triggered. A message will appear on screen to notify you that the BODs have been triggered.

![Publish Logistic Master Data dialog with the checkboxes Show Verb, Logical IDxs, Use ProcessSync Verb and Logging in the section BOD Messaging Settings and the buttons PROCESS, CLOSE, SELECT ALL and CLEAR ALL](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

If done successfully, the Supplier and Purchase Order tables should now be available under Settings → Master Data Lookup.

\\
