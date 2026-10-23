# Fournisseurs et bons de commande

## **Point de connexion**

Vous devrez créer le point de connexion API DocBits afin de pouvoir créer le flux de données par la suite.

Tout d'abord, dans InforOS, accédez à ION Desk → Connect → Connection Points

![Navigation de ION Desk dans InforOS avec les entrées de menu Home, Data Flows, API Flows et Mappings](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Une fois sur cet écran, vous devrez créer un nouveau point de connexion.

![Page Connection Points dans ION Desk avec les icônes de la barre d'outils et une liste vide de points de connexion](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Sélectionnez API**

Donnez au point de connexion un nom et une description qui en décrivent la nature et l'environnement. Dans l'onglet Connection, importez le compte de service que vous avez créé pour l'environnement avec lequel vous travaillez.

![Paramètres du point de connexion de DocBits-DEV-Demo-Import dans ION Desk affichant Name, Description et compte de service sous l'onglet Connection](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Passez ensuite à l'onglet Documents. Vous devrez ajouter les BOD suivants au point de connexion.

![Onglet Documents du point de connexion ION Desk listant les documents de connexion Ack SupplierInvoice, Sync.PurchaseOrder et Sync.ReceiveDelivery](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Ce BOD sert à signaler à DocBits qu'une erreur s'est produite dans Infor. La configuration de ces deux BOD doit ressembler à ce qui suit (le nom de l'appel d'API change pour chacun)

![Configuration Send to API pour Ack-SupplierInvoice avec les onglets allemands Eingabedokument, Anforderungsparameter, Anforderungstext et Einstellungen](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

La configuration de ce BOD doit ressembler à ce qui suit

![Configuration Send to API pour Sync.PurchaseOrder avec Product DocBits-DEV et l'opération post CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

La configuration de ce BOD doit ressembler à ce qui suit

![Configuration Send to API pour Sync.ReceiveDelivery dans ION Desk avec les champs API call name, Product et Operation](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Une fois ces BOD configurés, vous pouvez enregistrer le point de connexion en cliquant sur l'icône située à droite du bouton Retour.

## **Flux de données**

Le flux de données doit ressembler à ce qui suit

![Diagramme de flux de données ION reliant l'application LN via un filtre à une application DocBits API et à un élément End](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(La présence de plusieurs API DocBits s'explique par le fait que chaque connexion représente un environnement différent ; selon le nombre d'environnements dont vous disposez, votre flux de données peut donc différer légèrement.)

Pour les besoins de cette explication, nous prendrons l'exemple de quatre environnements distincts.

### **LN**

Le début du flux de données est constitué de votre application LN.

### **API DocBits**

Ajoutez ici une application et sélectionnez la ou les API DocBits que vous avez créées précédemment.

### **Fichiers**

La configuration doit ressembler à ce qui suit

![Configuration Files dans ION Desk affichant une liste de documents comprenant Sync.PurchaseOrder et Sync.ReceiveDelivery pour l'application DocBits API](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **Déclenchement des BOD LN**

Une fois toutes les étapes ci-dessus terminées, vous devrez accéder à Infor LN et déclencher les BOD afin que les différentes données de base nécessaires pour les fournisseurs et les bons de commande arrivent dans DocBits.

![Menu Publish BODs dans Infor LN avec le chemin de navigation Common, BOD-Messaging, Publish BODs, Publish Order Management Transactional Data](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

Dans le menu ci-dessus, onglet de gauche, sélectionnez Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Sélectionnez l'onglet PurchaseOrder et cochez la case.

![Page Publish Order Management Transactional Data dans Infor LN avec l'onglet PurchaseOrder coché et les boutons PROCESS, CLONE, SELECT ALL et CLEAR ALL](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Fournisseurs**

Depuis la page d'accueil de LN, dans l'onglet de menu de gauche, accédez à Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Sélectionnez l'onglet PartyMaster et cochez la case Supplier → Buy-from ou SupplierPartyMaster.

![Page Publish Logistics Master Data dans Infor LN avec l'onglet PartyMaster et l'option Supplier Buy-from SupplierPartyMaster cochée](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Déclenchement des BOD**

Une fois tous les BOD à publier correctement cochés, sélectionnez l'onglet Options.

Les options suivantes doivent être sélectionnées.

![Onglet Options de la page Publish Logistics Master Data dans Infor LN affichant la sélection et les paramètres de document avec les boutons PROCESS et CLEAR ALL](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Cela fait, cliquez sur le bouton PROCESS et les BOD seront déclenchés. Un message s'affiche à l'écran pour vous informer que les BOD ont été déclenchés.

![Page Publish Logistics Master Data dans Infor LN après traitement, montrant l'onglet Factory Track, le panneau Selection et les options Settings](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Si l'opération a réussi, les tables Supplier et Purchase Order doivent maintenant être disponibles sous Settings → Master Data Lookup.

\\
