# Fournisseurs et commandes fournisseur depuis Infor M3

Cet exemple relie les BOD fournisseur et commande fournisseur de M3 à DocBits via Infor ION. Les quinze images Infor ci-dessous sont des exemples historiques d'un tenant ; elles ne valident pas votre configuration M3 actuelle. Demandez à l'administrateur Infor de confirmer les noms de BOD, les tables source, la société, la division, les noms d'appel API et l'environnement cible avant de lancer un job. Aucun chargement initial M3 ni import DocBits n'a été exécuté pour cette mise à jour.

Le [guide de chargement initial](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html) d'Infor décrit les définitions dans EVS006, le verbe et la sélection dans EVS007, la soumission et l'historique. Commencez par une sélection limitée ; une exécution sans restriction peut générer beaucoup d'événements.

## **Point de connexion**

Vous devez créer le point de connexion de l'API DocBits pour pouvoir construire ensuite le flux de données.

Dans InforOS, ouvrez ION Desk → Connect → Connection Points.

<figure><img src="https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o" alt="Navigation historique d'ION Desk avec le groupe Connect déployé et l'entrée Connection Points mise en évidence."><figcaption><p>Navigation historique : ION Desk → Connect → Connection Points.</p></figcaption></figure>

Une fois sur cette page, vous devez créer un nouveau point de connexion.

<figure><img src="https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI" alt="Page historique Connection Points avec une flèche verte qui pointe vers Add."><figcaption><p>Action historique Add pour créer un point de connexion.</p></figcaption></figure>

**Sélectionnez API**

Donnez au point de connexion un nom et une description qui décrivent sa nature et son environnement. Sous l'onglet Connection, importez le compte de service que vous avez créé pour l'environnement utilisé.

<figure><img src="https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0" alt="Point de connexion historique DocBits-DEV-Demo-Import avec l'onglet Connection sélectionné et un contrôle Import de compte de service."><figcaption><p>Onglet historique Connection. Les noms affichés renvoient à l'environnement d'exemple ; utilisez votre propre compte de service.</p></figcaption></figure>

Passez ensuite à l'onglet Documents. Vous devez ajouter les BOD suivants au point de connexion. Tous ne sont pas nécessaires aux données de base des fournisseurs et des commandes fournisseur, mais ils seront utiles lorsque d'autres fonctions, comme la comptabilisation automatique, devront être mises en place.

<figure><img src="https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8" alt="Onglet historique Documents listant Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster et Sync.SupplierPartyMaster."><figcaption><p>Liste historique des documents reçus. Le BOD fournisseur affiché est Sync.RemitToPartyMaster, sans suffixe Data.</p></figcaption></figure>

Cette configuration historique utilise Sync.RemitToPartyMaster, Sync.SupplierPartyMaster et Sync.PurchaseOrder. Confirmez les BOD nécessaires à votre mapping DocBits ; la configuration peut varier selon le tenant et la fonction.

* Sync.RemitToPartyMaster et Sync.SupplierPartyMaster

L'image historique suivante montre Sync.SupplierPartyMaster. Configurez chaque BOD fournisseur requis avec le nom d'appel API et l'opération de réception confirmés pour votre environnement ; la seconde route fournisseur n'est pas représentée.

<figure><img src="https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk" alt="Onglet historique ION API avec Send to API sélectionné, le nom d'appel API Sync.SupplierPartyMaster et une opération POST."><figcaption><p>Route historique SupplierPartyMaster. L'image ne montre qu'une route fournisseur ; confirmez séparément l'opération de réception de chaque BOD requis.</p></figcaption></figure>

* Sync.PurchaseOrder

L'image historique suivante montre une opération de réception de commande fournisseur. Confirmez son point de terminaison actuel et le format de requête pour votre environnement.

<figure><img src="https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4" alt="Onglet historique ION API avec Send to API sélectionné pour Sync.PurchaseOrder et une opération POST."><figcaption><p>Route historique PurchaseOrder. L'ancien chemin du proxy API Gateway est un exemple, pas une adresse DocBits universelle.</p></figcaption></figure>

Une fois ces BOD configurés, vous pouvez enregistrer le point de connexion en actionnant l'icône située à droite du bouton de retour.

## **Flux de données**

Ce flux de données historique est une conception possible ; vérifiez ses routes et son organisation de réception dans votre propre tenant.

<figure><img src="https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8" alt="Flux historique partant de M3, passant par un filtre Yes ou No puis une répartition parallèle vers quatre nœuds d'API DocBits, avec des nœuds de jonction et de fin."><figcaption><p>Flux historique. La branche No se termine avant les nœuds d'API ; la branche Yes atteint les quatre environnements d'exemple.</p></figcaption></figure>

Les multiples nœuds d'API DocBits représentent des environnements distincts dans cet exemple. Votre conception peut différer ; vérifiez que des messages de test ne peuvent pas atteindre la production.

Quatre environnements ne sont affichés qu'à titre d'exemple.

### **M3**

Le début du flux de données est constitué par votre application M3.

### **Filtre**

La configuration du filtre se présente comme suit.

<figure><img src="https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY" alt="Panneau historique Filter Properties avec l'onglet Properties sélectionné et les champs Name et Description tous deux réglés sur Division."><figcaption><p>Nom et description historiques du filtre. Le seul nom Division n'établit pas quels enregistrements sont filtrés.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA" alt="Onglet historique Filter Properties Attributes listant les attributs AccountingEntityID pour ChartOfAccounts, PurchaseOrder, RemitToPartyMaster et SupplierPartyMaster."><figcaption><p>Attributs historiques : chaque BOD possède un chemin AccountingEntityID. Vérifiez le chemin de chaque document dans votre tenant.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw" alt="Onglet historique Filter Properties Conditions affichant ChartOfAccounts, Used Condition réglé sur Not Filtered et une expression d'exemple pour AccountingEntityID_3."><figcaption><p>Exemple historique de conditions. Used Condition affiche Not Filtered alors qu'une expression est listée ; vérifiez la condition sélectionnée et son effet au lieu de supposer que l'expression est active.</p></figcaption></figure>

(L'identifiant d'entité comptable est bien entendu propre à votre organisation.)

### **API DocBits**

Ici, vous ajoutez une application et sélectionnez la ou les API DocBits créées précédemment.

### **Documents**

Sélectionnez les documents affectés au nœud source M3 et aux nœuds de réception. Vérifiez que les attributs du filtre et les routes de réception couvrent chaque document requis.

<figure><img src="https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY" alt="Flux M3 historique avec l'icône de document mise en évidence et un panneau Documents listant Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster et Sync.SupplierPartyMaster."><figcaption><p>Sélection historique des documents du flux M3. Il s'agit d'une liste de documents BOD, pas d'une configuration de nœud de fichier.</p></figcaption></figure>

## **Déclenchement des BOD M3**

Accédez à l'application Infor M3.

Ouvrez le contrôle **Search and Start** de M3, saisissez **EVS006** et confirmez le programme. Utilisez la navigation prise en charge par votre client M3.

<figure><img src="https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o" alt="Boîte de dialogue historique M3 Search and Start contenant evs006 et un bouton OK."><figcaption><p>Recherche historique de programme : saisissez EVS006 dans Search and Start.</p></figcaption></figure>

Dans EVS006, définissez les noms de BOD requis pour votre mapping validé. L'exemple historique utilise SupplierPartyMaster, RemitToPartyMaster et PurchaseOrder. Confirmez leurs noms de table M3 dans votre version avant de créer une définition de chargement initial.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Utilisez l'action d'ajout pour chaque définition validée. Vérifiez la société et la division avant de continuer.

<figure><img src="https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw" alt="Capture partielle historique de la barre d'outils EVS006 avec Add mis en évidence au-dessus des champs BOD noun, BOD variant, BOD et Table vides."><figcaption><p>Action historique Add dans EVS006. Cette capture ne montre pas de définitions de chargement initial renseignées.</p></figcaption></figure>

Après avoir ajouté chacun des BOD, faites un clic droit sur le nom de BOD et sélectionnez Related → Run.

<figure><img src="https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo" alt="Menu contextuel historique avec Related déployé et Run mis en évidence ; History est listé en dessous."><figcaption><p>Action historique Related → Run. Utilisez ensuite History pour examiner le résultat du chargement initial.</p></figcaption></figure>

L'action associée **Run** ouvre EVS007. Ne choisissez **Sync** que si le flux ION de réception l'attend. Vérifiez la sélection et les filtres avant la soumission finale ; le passage à l'écran suivant ne prouve pas la livraison.

<figure><img src="https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA" alt="Écran historique EVS007 Initial Load Job pour CIDMAS et SupplierPartyMaster, statut Pending, avec le menu du verbe BOD ouvert et l'option Sync annotée alors que Show est encore affiché."><figcaption><p>Sélection historique du verbe dans EVS007 avant l'exécution. L'image montre un job en attente et une option Sync annotée ; elle ne prouve pas que Sync a été sélectionné ni que des données ont été importées.</p></figcaption></figure>

Une notification de soumission confirme que le job a été demandé. Dans **History** d'EVS006, vérifiez le nombre d'éléments traités et les erreurs. Contrôlez ensuite le message et la cible dans Infor ION.

## Vérification dans DocBits

Ouvrez **Paramètres → Traitement des documents → Consultation des données de base → BOD Données d'entrée → Fournisseur** dans l'organisation DocBits visée. Choisissez le champ identifiant dans **Rechercher par colonne**, saisissez un numéro ou un nom de fournisseur connu dans **Recherche Chaîne** et lancez la recherche avec la loupe. Le bouton **Actions** propose **Télécharger en CSV**, **Mettre à jour l'alias** et **Masquer les colonnes vides**. Ouvrez ensuite **Bon de commande** et recherchez un numéro de commande connu ; vérifiez **En-Tête De Commande** si votre mapping sépare les données d'en-tête et de ligne. Comparez les identifiants et la société avec la source M3. Une requête EVS007 réussie ne prouve pas à elle seule que tous les enregistrements sont arrivés.

<figure><img src="../../../.gitbook/assets/dbdc-1138-supplier-fr-20261112.png" alt="Vue française Consultation des données de base de DocBits avec l'onglet Fournisseur, les champs Rechercher par colonne et Recherche Chaîne et dix lignes fournisseur inventées de SUP-1001 à SUP-1010 (version 11.27.7)."><figcaption><p>Vue Fournisseur de DocBits en français (version Sandbox 11.27.7). Les lignes affichées sont des données d'exemple inventées : recherchez un identifiant de test connu et comparez-le avec M3 et ION.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc-1138-purchase-order-fr-20261112.png" alt="Vue française Consultation des données de base de DocBits avec les onglets Fournisseur et Bon de commande ouverts et dix lignes de commande inventées de PO-4500 à PO-4509 (version 11.27.7)."><figcaption><p>Vue Bon de commande de DocBits en français (version Sandbox 11.27.7). Les lignes sont des données d'exemple inventées et ne prouvent pas un import M3.</p></figcaption></figure>

Les deux vues françaises ont été capturées le 12 novembre 2026 sur la version Sandbox 11.27.7, sans lancer de job M3, importer de fichier ni modifier de données de base. Les lignes visibles sont des données d'exemple inventées : ces images indiquent où vérifier, pas un transfert abouti. Si un enregistrement attendu manque, vérifiez l'historique EVS006, le routage ION, le mapping des BOD et l'organisation DocBits avant de relancer.
