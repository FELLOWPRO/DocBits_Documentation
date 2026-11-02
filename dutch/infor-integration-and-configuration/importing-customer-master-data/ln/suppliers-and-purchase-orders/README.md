# Leveranciers en inkooporders

## **Verbindingspunt**

Maak eerst het DocBits-API-verbindingspunt aan om later de gegevensstroom te kunnen inrichten.

Ga in InforOS naar ION Desk → Connect → Connection Points.

![Navigatie van ION Desk met de groep Connect uitgeklapt en de items Data Flows, API Flows, Mappings, Connection Points en File Templates](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Maak hier een nieuw verbindingspunt aan.

![Pagina Connection Points van ION Desk met de groep Connect open in de navigatie en het pad Home en Connection Points](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**API selecteren**

Geef het verbindingspunt een naam en beschrijving die de functie en omgeving duidelijk maken. Importeer op het tabblad Connection het serviceaccount voor de betreffende omgeving.

![Venster API Connection Point DocBits-DEV-Demo-Import met de tabbladen Usage, Connection en Documents, de naam DocBits-DEV-Demo-Import, de verificatievermelding DocBits-DEV-Demo-Import Service Account en de Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Open vervolgens het tabblad Documents. Voeg de volgende BOD's toe aan het verbindingspunt.

![Tabblad Documents van het verbindingspunt met de rijen Ack-SupplierInvoice, Sync.PurchaseOrder en Sync.ReceiveDelivery, elk met de richting In en het gelijknamige BOD](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Dit BOD meldt in DocBits dat er een fout is opgetreden in Infor. De configuratie voor deze twee BOD's ziet er ongeveer als volgt uit; API Call Name verschilt per BOD.

![BOD-configuratie met de tabbladen Input Document, ION API, Request Parameters, Request Body en Settings en de API Call Name Ack-SupplierInvoice](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

De configuratie voor dit BOD ziet er ongeveer als volgt uit.

![BOD-configuratie met de tabbladen Input Document, ION API, Request Parameters, Request Body en Settings en de velden API Call Name Sync.PurchaseOrder, Product DocBits-DEV en de bewerking POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

De configuratie voor dit BOD ziet er ongeveer als volgt uit.

![BOD-configuratie met de tabbladen Input Document, ION API, Request Parameters, Request Body en Settings en de API Call Name Sync.ReceiveDelivery](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Sla het verbindingspunt na het instellen van de BOD's op met het pictogram rechts naast de knop Terug.

## **Gegevensstroom**

De gegevensstroom ziet er ongeveer als volgt uit.

![Gegevensstroom in ION Desk met een DocBits-verbindingspunt links en het End-knooppunt rechts](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

Elke DocBits-API-verbinding vertegenwoordigt een andere omgeving. Afhankelijk van het aantal omgevingen kan uw gegevensstroom daarom afwijken van dit voorbeeld.

Voor deze uitleg gebruiken we een voorbeeld met vier afzonderlijke omgevingen.

### **LN**

De gegevensstroom begint bij uw LN-toepassing.

### **DocBits-API**

Voeg hier een toepassing toe en selecteer de eerder aangemaakte DocBits-API's.

### **Bestanden**

De configuratie ziet er als volgt uit.

![Detail van de gegevensstroom met het DocBits-knooppunt DocBits-DEV-P, de markeringen Start en Ende en een tweede DocBits-knooppunt in het midden, en het paneel Dokumente met Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster en Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **LN-BOD's activeren**

Ga na het voltooien van deze stappen naar Infor LN en activeer de BOD's, zodat de benodigde stamgegevens voor leveranciers en inkooporders in DocBits aankomen.

![Startpagina van Infor LN met het favorietenpaneel links en de tegels voor bestellingen, facturen en magazijnorders](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

Selecteer in het linkermenu Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data.

Open het tabblad PurchaseOrder en schakel het selectievakje in.

![Venster Publish Order Management Transactional Data met de knoppen PROCESS, CLOSE, SELECT ALL en CLEAR ALL, het gekozen tabblad PurchaseOrder en de boom links met BOD Messaging en Publish BODs uitgeklapt](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Leveranciers**

Ga vanaf de LN-startpagina via het linkermenu naar Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data.

Open het tabblad PartyMaster en schakel Supplier → Buy-from of SupplierPartyMaster in.

![Venster Publish Logistic Master Data met de knoppen PROCESS, CLOSE, SELECT ALL en CLEAR ALL, het gekozen tabblad PartyMaster en het raster met de kolommen Supplier, Buy-from PartyMaster, Pay-to PartyMaster, Pay-from PartyMaster en Remit-to PartyMaster](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **BOD's activeren**

Open het tabblad Options nadat u alle juiste BOD's voor publicatie hebt geselecteerd.

Selecteer de volgende opties.

![Venster Publish Logistic Master Data met de kiezer Mode, de sectie Selection Range met het bedrijf 0051 en de sectie BOD Messaging Settings](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Klik daarna op PROCESS om de BOD's te activeren. Een melding op het scherm bevestigt dit.

![Venster Publish Logistic Master Data met de selectievakjes Show Verb, Logical IDxs, Use ProcessSync Verb en Logging in de sectie BOD Messaging Settings en de knoppen PROCESS, CLOSE, SELECT ALL en CLEAR ALL](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Als de publicatie is geslaagd, zijn de tabellen voor leveranciers en inkooporders beschikbaar onder Settings → Master Data Lookup.

\\
