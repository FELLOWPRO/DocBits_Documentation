# Fournisseurs et Commandes d'Achat

## **Point de Connexion**

Vous devrez créer le point de connexion de l'API DocBits afin de créer ultérieurement le flux de données.

Tout d'abord, dans InforOS, accédez à ION Desk → Connect → Points de Connexion

![](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Une fois ici, vous devrez créer un nouveau point de connexion.

![](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Sélectionnez l'API**

Donnez au point de connexion un nom et une description décrivant sa nature et son environnement. Sous l'onglet Connexion, importez le compte de service que vous avez créé pour l'environnement avec lequel vous travaillez.

![](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Ensuite, passez à l'onglet Documents. Vous devrez ajouter les BOD suivants au point de connexion.

![](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Ce BOD est utilisé pour signaler sur DocBits qu'une erreur s'est produite dans Infor. La configuration pour ces deux BOD devrait ressembler à ce qui suit (Nom de l'Appel API changeant pour chacun)

![](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

La configuration pour ce BOD devrait ressembler à ce qui suit

![](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

La configuration pour ce BOD devrait ressembler à ce qui suit

![](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Une fois ces BOD configurés, vous pouvez enregistrer le point de connexion en appuyant sur l'icône située à droite du bouton de retour.

## **Flux de Données**

Le flux de données ressemblera à ce qui suit

![](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(La raison pour laquelle il y a plusieurs API DocBits est due à chaque connexion représentant un environnement différent, ce qui signifie qu'en fonction du nombre d'environnements que vous avez, votre flux de données pourrait légèrement différer)

Pour les besoins de cette explication, nous utiliserons l'exemple de quatre environnements distincts.

### **LN**

Le début du flux de données consiste en votre application LN

### **API DocBits**

Ici, vous ajouterez une application et sélectionnerez le(s) API DocBits que vous avez créé(s) précédemment

### **Fichiers**

La configuration devrait ressembler à ce qui suit

![](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **Déclenchement des BOD LN**

Une fois tout ce qui précède est terminé, vous devrez naviguer vers Infor LN et déclencher les BOD afin que les diverses données principales dont vous avez besoin pour les Fournisseurs et les Commandes d'Achat arrivent dans DocBits.

![](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **Commande d'Achat**

Dans le menu ci-dessus, dans l'onglet du menu de gauche, sélectionnez Commun → Messagerie BOD → Publier les BOD → Publier les Données Transactionnelles de Gestion des Commandes

Sélectionnez l'onglet Commande d'Achat et cochez la case.

![](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)
### **Fournisseurs**

À partir de la page d'accueil LN, dans l'onglet du menu de gauche, accédez à Commun → BOD-Messaging → Publier BODs → Publier les données maîtresses de la logistique

Sélectionnez l'onglet PartyMaster et cochez la case Fournisseur → Acheter à ou SupplierPartyMaster.

![](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Déclenchement de BOD**

Une fois que tous les BOD corrects ont été vérifiés pour la publication, sélectionnez l'onglet Options.

Les options suivantes doivent être sélectionnées.

![](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Une fois cela fait, appuyez sur le bouton PROCESS et les BOD seront déclenchés. Un message apparaîtra à l'écran pour vous informer que les BOD ont été déclenchés.

![](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Si tout se passe bien, les tables Fournisseur et Commande d'achat devraient maintenant être disponibles sous Paramètres → Recherche de données maîtresses.
