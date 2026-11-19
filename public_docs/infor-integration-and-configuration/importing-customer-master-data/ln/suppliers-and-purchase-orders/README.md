# Fournisseurs et bons de commande depuis Infor LN

Cet exemple décrit la route Infor ION pour les BOD de fournisseurs et de bons de commande, ainsi que l'endroit où les vérifier dans DocBits. Les quatorze captures Infor ci-dessous sont des exemples historiques provenant d'un locataire. Confirmez les points de connexion, les noms d'appels API et les options de publication LN avec votre administrateur d'intégration ; ils n'ont pas été vérifiés dans un locataire Infor pour cette mise à jour. Aucun BOD n'a été publié ni importé pendant cette mise à jour.

Infor documente le [publicateur de données de base logistiques LN](https://docs.infor.com/ln/latest/en-us/lnolh/tcolh/help/tc/bod/tcbod0200m000.html) et le [publicateur transactionnel de gestion des commandes](https://docs.infor.com/ln/2025.x/en-us/lnolh/tdolh/help/td/bod/tdbod0200m000.html). Leurs modes ont des effets différents : **Count** indique le total des enregistrements sans publier ; **Simulate** produit un résultat d'essai sans valider la publication ; **Publish** envoie les données sélectionnées. La publication peut atteindre tous les abonnés : vérifiez la plage de sociétés et les abonnés avant de l'exécuter.

## **Point de connexion**

Vous devrez créer le point de connexion API DocBits afin de pouvoir créer le flux de données par la suite.

Tout d'abord, dans InforOS, accédez à ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE" alt="Navigation historique dans Infor ION Desk avec le groupe Connect déployé et l'entrée Connection Points mise en évidence."><figcaption><p>Exemple de navigation historique : ION Desk → Connect → Connection Points.</p></figcaption></figure>

Une fois sur cet écran, vous devrez créer un nouveau point de connexion.

<figure><img src="https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU" alt="Écran historique Connection Points avec une flèche verte qui pointe vers Add."><figcaption><p>Choisissez Add pour créer un point de connexion ; l'annotation verte marque l'action dans cette interface historique.</p></figcaption></figure>

**Sélectionnez API**

Donnez au point de connexion un nom et une description qui en décrivent la nature et l'environnement. Dans l'onglet Connection, importez le compte de service que vous avez créé pour l'environnement avec lequel vous travaillez.

<figure><img src="https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0" alt="Point de connexion API historique DocBits-DEV-Demo-Import avec Connection sélectionné et un contrôle Import pour le compte de service."><figcaption><p>Onglet Connection historique. Les noms de compte de service et de connexion affichés appartiennent à l'environnement d'exemple.</p></figcaption></figure>

Passez ensuite à l'onglet Documents. Vous devrez ajouter les BOD suivants au point de connexion.

<figure><img src="https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg" alt="Onglet Documents historique en allemand avec les appels API Ack-SupplierInvoice, Sync.PurchaseOrder et Sync.ReceiveDelivery et les BOD reçus."><figcaption><p>Onglet Dokumente (Documents) historique. Ce recadrage montre trois routes ; il ne montre pas la configuration complète des fournisseurs.</p></figcaption></figure>

* Ack-SupplierInvoice

Ce BOD sert à signaler à DocBits qu'une erreur s'est produite dans Infor. La route Acknowledge.SupplierInvoice présentée ci-dessous est un exemple pour les accusés de réception de factures. Confirmez le nom de votre appel API et si cette route est nécessaire pour votre flux de fournisseurs et de bons de commande.

<figure><img src="https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y" alt="Onglet ION API historique en allemand pour Ack-SupplierInvoice avec une opération POST sélectionnée."><figcaption><p>Route d'accusé de réception historique. Ack-SupplierInvoice est un nom d'appel API d'exemple ; Acknowledge.SupplierInvoice est le BOD reçu.</p></figcaption></figure>

* Sync.PurchaseOrder

L'exemple historique ci-dessous montre une opération de réception ; confirmez l'opération actuelle et le format de la requête pour votre environnement.

<figure><img src="https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0" alt="Onglet ION API historique avec Send to API sélectionné pour Sync.PurchaseOrder et une opération POST configurée."><figcaption><p>Route de bons de commande historique. Vérifiez l'opération de réception de votre environnement DocBits au lieu de copier l'ancien chemin de proxy.</p></figcaption></figure>

* Sync.ReceiveDelivery

L'exemple historique ci-dessous montre une opération de réception ; confirmez l'opération actuelle et le format de la requête pour votre environnement.

<figure><img src="https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc" alt="Onglet ION API historique en allemand pour Sync.ReceiveDelivery avec une opération POST configurée."><figcaption><p>Route historique des données de réception. Confirmez si ReceiveDelivery est nécessaire pour votre intégration et quelle opération le reçoit.</p></figcaption></figure>

Une fois ces BOD configurés, vous pouvez enregistrer le point de connexion en cliquant sur l'icône située à droite du bouton Retour.

## **Flux de données**

Le flux de données doit ressembler à ce qui suit

<figure><img src="https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU" alt="Flux de documents historique allant d'un nœud LN vers une répartition parallèle vers quatre nœuds API DocBits, suivie d'une jonction et d'une fin."><figcaption><p>Flux historique avec quatre environnements. La répartition et la jonction sont visibles ; le nombre et les destinations des nœuds dépendent de la conception de votre intégration.</p></figcaption></figure>

Les multiples nœuds API DocBits de cet exemple historique représentent des environnements distincts. Votre conception de production peut utiliser un nombre différent de nœuds ; n'acheminez jamais de données de test vers une organisation de production.

L'illustration suivante utilise quatre environnements uniquement à titre d'exemple.

### **LN**

Le début du flux de données est constitué de votre application LN

### **API DocBits**

Ajoutez ici une application et sélectionnez la ou les API DocBits que vous avez créées précédemment

### **Documents**

Vérifiez la liste des documents affectés au flux. Les messages de fournisseurs présentés ici nécessitent également des routes de réception correspondantes dans le point de connexion API. Leur configuration d'appel API n'apparaît pas dans le recadrage des trois routes précédent ; confirmez les opérations requises avec votre administrateur d'intégration.

<figure><img src="https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU" alt="Canevas de flux historique avec le panneau allemand Dokumente en dessous, listant Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster et Sync.SupplierPartyMaster."><figcaption><p>Liste de documents historique du flux. Les messages de fournisseurs y apparaissent, comme les messages de bons de commande et de réception.</p></figcaption></figure>

## **Déclenchement des BOD LN**

Une fois que l'administrateur d'intégration a vérifié le point de connexion, les routes de documents et le flux de données actif, utilisez la session de publication LN appropriée. Suivez chaque identifiant de test à travers LN, ION et DocBits ; le déclenchement d'un BOD ne prouve pas à lui seul qu'un enregistrement est arrivé.

<figure><img src="https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y" alt="Page d'accueil historique en allemand d'Infor LN avec une liste de favoris ; le menu Publish BODs n'est pas ouvert."><figcaption><p>Page de démarrage historique de LN. Utilisez la navigation décrite ci-dessous pour trouver la session de publication appropriée.</p></figcaption></figure>

### **PurchaseOrder**

Dans le menu ci-dessus, onglet de gauche, sélectionnez Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Sélectionnez l'onglet PurchaseOrder et cochez la case.

<figure><img src="https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco" alt="Session historique Publish Order Management Transactional Data avec l'onglet PurchaseOrder et la case cochée et les champs de plage de commandes visibles."><figcaption><p>Sélection historique de PurchaseOrder. Vérifiez la plage de commandes et les statuts avant de publier.</p></figcaption></figure>

### **Fournisseurs**

Depuis la page d'accueil de LN, dans l'onglet de menu de gauche, accédez à Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Sélectionnez l'onglet PartyMaster et cochez la case Supplier → Buy-from ou SupplierPartyMaster.

<figure><img src="https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0" alt="Session historique Publish Logistic Master Data avec PartyMaster sélectionné et la case Supplier Buy-from cochée."><figcaption><p>Sélection historique de fournisseurs dans PartyMaster. Choisissez les rôles de partenaire nécessaires à votre intégration et vérifiez la plage de la sélection.</p></figcaption></figure>

### **Déclenchement des BOD**

Une fois tous les BOD à publier correctement cochés, sélectionnez l'onglet Options.

Vérifiez les options de votre locataire. L'exemple historique met en évidence Publish et Use Process/Sync Verb ; ce ne sont pas des réglages universels pour toutes les intégrations.

<figure><img src="https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U" alt="Onglet Options historique de LN avec Publish et Use Process/Sync Verb mis en évidence et une plage de sociétés visible."><figcaption><p>Exemple historique d'Options. Ici, Publish et Use Process/Sync Verb sont sélectionnés ; vérifiez le mode, la plage de sociétés et les abonnés pour votre propre exécution.</p></figcaption></figure>

Avant **Process**, utilisez **Count** ou **Simulate** et consultez le nombre d'enregistrements et la plage de sociétés lorsque votre version de LN propose ces modes. Ne publiez qu'avec l'accord de l'administrateur d'intégration. Une confirmation que les BOD ont été déclenchés ne prouve pas la livraison à DocBits.

<figure><img src="https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM" alt="Onglet Options historique de LN avec le bouton Process mis en évidence avant l'exécution."><figcaption><p>Action Process historique avant l'exécution. Cette capture ne contient aucun résultat de publication ni confirmation que DocBits a reçu des données.</p></figcaption></figure>

## Vérifier dans DocBits

Vérifiez dans Infor ION que la livraison à l'organisation DocBits prévue a réussi. Ouvrez ensuite **Paramètres → Traitement des documents → Consultation des données de base**. Sous **BOD Données d'entrée**, ouvrez **Fournisseur**. Choisissez le champ identifiant dans **Rechercher par colonne**, saisissez un numéro ou un nom de fournisseur connu dans **Recherche Chaîne**, puis utilisez la loupe pour lancer la recherche. Ouvrez **Bon De Commande** et recherchez un numéro de commande connu. Vérifiez également **En-Tête De Commande** si votre mappage sépare l'en-tête et les lignes. Comparez les identifiants et la société avec LN ; ne concluez pas que tous les enregistrements sont arrivés sur la seule base d'un message de publication réussi.

<figure><img src="../../../../.gitbook/assets/dbdc-1145-supplier-fr-20261112.png" alt="Vue Fournisseur de la Consultation des données de base dans DocBits en français, avec les champs Rechercher par colonne et Recherche Chaîne et dix lignes de fournisseurs d'exemple inventées, de SUP-1001 à SUP-1010."><figcaption><p>Vue de vérification des fournisseurs, sandbox en version 11.27.7, avec des lignes d'exemple inventées. Dans cette version, les en-têtes de colonnes du tableau s'affichent encore en anglais.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1145-purchase-order-fr-20261112.png" alt="Vue Bon de commande de la Consultation des données de base dans DocBits en français, avec les onglets Fournisseur et Bon de commande, les mêmes champs de recherche et dix lignes de bons de commande d'exemple inventées, de PO-4500 à PO-4509."><figcaption><p>Vue de vérification des bons de commande, sandbox en version 11.27.7, avec des lignes d'exemple inventées. Les lignes ne prouvent aucune importation depuis LN.</p></figcaption></figure>

Les vues anglaises de Dev ont été contrôlées le 29 octobre 2026 sans publier de BOD, importer de fichier ni modifier de données de base ; les lignes d'enregistrements étaient exclues de ces images. Les deux captures en français proviennent du sandbox en version 11.27.7 et affichent des lignes d'exemple inventées au lieu de données de base réelles ; elles montrent où vérifier, et non un transfert LN terminé. Si l'enregistrement attendu manque, vérifiez les journaux de publication LN, le routage ION, l'organisation et le mappage BOD avant de relancer.
