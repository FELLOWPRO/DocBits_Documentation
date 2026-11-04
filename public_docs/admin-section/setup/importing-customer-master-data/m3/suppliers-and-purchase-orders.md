# Fournisseurs et Commandes d'Achat

## **Point de Connexion**

Vous devrez créer le point de connexion API de DocBits afin de créer ultérieurement le flux de données.

Dans InforOS, accédez à ION Desk → Connect → Points de Connexion

![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Une fois ici, vous devrez créer un nouveau point de connexion.

![](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Sélectionnez l'API**

Donnez au point de connexion un nom et une description décrivant sa nature et son environnement. Sous l'onglet Connexion, importez le compte de service que vous avez créé pour l'environnement avec lequel vous travaillez.

![](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Ensuite, passez à l'onglet Documents. Vous devrez ajouter les BOD suivants au point de connexion, tous ne sont pas nécessaires pour les données maîtres des fournisseurs et des commandes d'achat mais seront utiles lorsque d'autres fonctionnalités telles que la comptabilité automatique devront être implémentées.

![](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Pour l'instant, nous nous concentrerons uniquement sur les BOD nécessaires, à savoir : Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster et Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData et Sync.SupplierPartyMaster

La configuration de ces deux BOD devrait ressembler à ce qui suit (le nom de l'appel API change pour chacun)

![](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

La configuration de ce BOD devrait ressembler à ce qui suit

![](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Une fois ces BOD configurés, vous pouvez enregistrer le point de connexion en appuyant sur l'icône située à droite du bouton de retour.

## **Flux de Données**

Le flux de données ressemblera à ce qui suit

![](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(La raison pour laquelle plusieurs APIs de DocBits sont nécessaires est que chaque connexion représente un environnement différent, ce qui signifie que, en fonction du nombre d'environnements que vous avez, votre flux de données pourrait légèrement différer)

Dans le cadre de cette explication, nous utiliserons l'exemple de quatre environnements distincts.

### **M3**

Le début du flux de données consiste en votre application M3

### **Filtre**

La configuration du filtre ressemble à ce qui suit

![](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(L'ID de l'entité comptable étant bien sûr unique à votre organisation)

### **API DocBits**

Ici, vous ajouterez une application et sélectionnerez le(s) API DocBits que vous avez créé précédemment
### **Fichiers**

La configuration devrait ressembler à ce qui suit

![](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Déclenchement M3 BOD**

Accédez à l'application Infor M3

Une fois sur le menu principal, tapez Command + R pour ouvrir la boîte de recherche de l'invite de commande. Ensuite, tapez evs006 et recherchez.

![](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Une fois sur cette page, vous devrez ajouter SupplierPartyMaster, RemitToPartyMaster et PurchaseOrder à la liste.

Nom BOD : SupplierPartyMaster

Table : CIDMAS

Nom BOD : RemitToPartyMaster

Table : CIDMAS

Nom BOD : PurchaseOrder

Table : MPHEAD

Pour chaque cas, vous devrez appuyer sur l'icône plus pour les ajouter à la liste.

![](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Après avoir ajouté chacun des BOD, cliquez avec le bouton droit sur le nom du BOD du BOD et sélectionnez Relatif → Exécuter

![](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Vous serez redirigé vers le menu suivant, où vous devrez changer le verbe BOD en Sync puis appuyer sur SUIVANT pour déclencher les BOD.

![](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Une fois les BOD déclenchés, vous recevrez une notification confirmant cela.

Si cela est fait avec succès, les tables Fournisseur et Bon de commande devraient maintenant être disponibles sous Paramètres → Recherche de données maîtresses.
