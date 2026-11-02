# Fournisseurs et commandes fournisseur

## **Point de connexion**

Vous devrez créer le point de connexion DocBits API afin de créer le flux de données ultérieurement.

Dans InforOS, accédez à ION Desk → Connect → Points de connexion

![Navigation d'ION Desk avec le groupe Connect déployé et les entrées Data Flows, API Flows, Mappings, Connection Points et File Templates](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Une fois ici, vous devrez créer un nouveau point de connexion.

![Page Connection Points d'ION Desk avec le groupe Connect ouvert dans la navigation et le fil d'Ariane Home et Connection Points](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Select API**

Donnez au point de connexion un nom et une description décrivant sa nature et son environnement. Sous l'onglet Connexion, importez le compte de service que vous avez créé pour l'environnement avec lequel vous travaillez.

![Boîte de dialogue API Connection Point DocBits-DEV-Demo-Import avec les onglets Usage, Connection et Documents, le nom DocBits-DEV-Demo-Import, l'entrée d'authentification DocBits-DEV-Demo-Import Service Account et le Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Ensuite, passez à l'onglet Documents. Vous devrez ajouter les BOD suivants au point de connexion. Tous ne sont pas nécessaires pour les données de base des fournisseurs et des bons de commande, mais seront utiles lorsque d'autres fonctionnalités telles que la comptabilité automatique doivent être implémentées.

![Onglet Documents du point de connexion avec les BOD Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster et Sync.SupplierPartyMaster et une case à cocher sur chaque ligne](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Pour l'instant, nous nous concentrerons uniquement sur les BOD nécessaires, à savoir : Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster et Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData et Sync.SupplierPartyMaster

La configuration de ces deux BOD devrait ressembler à ce qui suit (le nom de l’appel API change pour chacun)

![Configuration du BOD avec les onglets Input Document, ION API, Request Parameters, Request Body et Settings et les champs API Call Name Sync.SupplierPartyMaster, Product DocBits-DEV et l'opération POST CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

La configuration de ce BOD devrait ressembler à ce qui suit

![Configuration du BOD avec les onglets Input Document, ION API, Request Parameters, Request Body et Settings et les champs API Call Name Sync.PurchaseOrder, Product DocBits-DEV et l'opération POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Une fois ces BOD configurés, vous pouvez enregistrer le point de connexion en appuyant sur l'icône située à droite du bouton retour.

## **Flux de données**

Le flux de données ressemblera à ce qui suit

![Flux de données dans ION Desk avec un nœud M3 à gauche, plusieurs nœuds DocBits nommés DocBits-DEV-P, DocBits-DEV-S et DocBits-DEV-D au centre, un nœud End et une condition avec les branches Yes et No](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(La raison pour laquelle il existe plusieurs API DocBits est due au fait que chaque connexion représente un environnement différent, ce qui signifie qu'en fonction du nombre d'environnements dont vous disposez, votre flux de données peut différer légèrement)

Pour les besoins de cette explication, nous utiliserons l’exemple de quatre environnements distincts.

### **M3**

Le début du flux de données est constitué de votre application M3

### **Filtre**

La configuration du filtre ressemble à ceci

![Panneau Filter Properties avec les onglets Properties, Attributes et Conditions et les champs Name et Description vides](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Panneau Filter Properties avec l'onglet Attributes ouvert et les lignes AccountingEntityID_3 pour ChartOfAccounts, AccountingEntityID pour PurchaseOrder, AccountingEntityID_1 pour RemitToPartyMaster et AccountingEntityID_2 pour SupplierPartyMaster, toutes de type STRING avec le chemin DataArea/*/AccountingEntityID](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Panneau Filter Properties avec l'onglet Conditions ouvert, le document ChartOfAccounts, la condition Not Filtered et la ligne DIV780AAA avec l'expression AccountingEntityID_3 égale à 780_AAA](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(L'entité comptabl’ID étant bien entendu unique à votre organisation)

### **API DocBits**

Ici, vous ajouterez une application et sélectionnerez le(s) DocBits API(s) que vous avez créé précédemment.

### **Fichiers**

La configuration devrait ressembler à ceci

![Détail du flux de données avec le nœud M3 à gauche, le nœud de condition et les nœuds DocBits, les marqueurs Start et End et le panneau Documents avec Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster et Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Déclenchement des BOD M3**

Navigate to the Infor M3 application

Une fois dans le menu principal, tapez Commande + R pour ouvrir la zone de recherche d'invite de commande. Tapez ensuite evs006 et recherchez.

![Boîte de dialogue Search and Start dans Infor M3 avec le champ de recherche d'une commande](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Une fois sur cette page, vous devrez ajouter les SupplierPartyMaster, RemitToPartyMaster et PurchaseOrder à la liste.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Pour chaque cas, vous devrez appuyer sur l'icône plus pour les ajouter à la liste.

![En-tête du panneau EVS006 avec les menus ACTIONS, OPTIONS, RELATED et TOOLS et les colonnes BOD noun, BOD variant et BOD description](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Après avoir ajouté chacun des BOD, faites un clic droit sur le nom BOD du BOD et sélectionnez Associé → Exécuter

![Menu Related dans Infor M3 avec les entrées Drill down, Select, Run, Change, History, Copy, Delete, Display et leurs raccourcis clavier](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Vous serez redirigé vers le menu suivant, où vous devrez changer le verbe BOD en Sync, puis appuyer sur NEXT pour déclencher les BOD.

![Panneau EVS007 Initial Load Job Open avec la table CIDMAS, le BOD noun SupplierPartyMaster, le numéro de tâche 243249962976569068, le statut 1-Pending et le BOD verb défini sur Sync](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Une fois que vous aurez déclenché les BOD, vous recevrez une notification le confirmant.

Si cela est fait avec succès, les tableaux Fournisseur et Bon de commande devraient maintenant être disponibles sous Paramètres → Recherche de données de base.
