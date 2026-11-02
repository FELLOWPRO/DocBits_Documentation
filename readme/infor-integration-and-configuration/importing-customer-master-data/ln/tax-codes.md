# Codes fiscaux

## **Créer des points de connexion DocBits**

Ouvrez ION Desk → Connecter → Points de connexion

![Page d'accueil d'ION Desk avec le menu Connect ouvert et les entrées Connection Points, Data Flows, API Flows, Mappings et File Templates](https://lh7-us.googleusercontent.com/QLQB17W\_hywZWBqme8Wio-orbdOdFHXLv5zTd89B3EkeS0WCuuo5Pv1CndLRQ2rFUefvQYM95U2Unhrl3YU3WAR23Ij\_tDw\_TOEVenWjyCh-9H8CPFSezF2gmED7u5QTR7q9WV4CSXRvDqkmKJYPqAI)

Vous aurez besoin de 4 points de connexion pour ce flux de données, de 3 points de connexion API pour les différentes catégories de codes fiscaux (taux normal, taux réduit et exonéré) et d'un point de connexion Application représentant votre entreprise LN.

Afin de créer de nouveaux points de connexion, sélectionnez le bouton “+ADD””

![Page Connection Points d'ION Desk avec la liste des points de connexion existants et le bouton +ADD](https://lh7-us.googleusercontent.com/cECLuIswRSK3WWhUMi1n3tm2AIcrksZdpz7ZCO6-H\_MzaKe9CDT0w1b7GKJ8GtT\_d6nvvDe4ukLJfWcMocbHZ5dSSCw25Ky7-JUdrYb893GYYyaHL9tTjG1ZniORJPLSu1zJxL3c-1VQRw4IC0LpYuA)

Sélectionnez “API” en bas de la liste des options

![Liste des types de points de connexion avec Infor LN et IMS via API Gateway sous Infor Technology et API en bas de la liste](https://lh7-us.googleusercontent.com/bpeLxdmi8b10LLMGy02vMRXuLoic9kFLywnpd6SSYV0fNv82dQahyvaA85mC1PEVScNW4m63fOw89vkhQr0-ou8VWOSjkwGWG5GnP7GQl77THtjXWP3YNo8LUzAstpCs0Q5fOjxaoT\_\_ZKM4jciHA5I)

Vous serez redirigé vers la page suivante

![Formulaire vide d'un point de connexion API dans ION Desk avec la date de dernière modification et la section Connection Documents](https://lh7-us.googleusercontent.com/4pcN0B7aibjn\_Qn8nMgkzRc\_NiXev-c1wJudDKo2V5r0ORuajVzfzAWnWu0Wt68hKMKSLYkieUhOYChkcZuCZDWkg-F22Rq2WvVqgPweSg3by2TGrrJHweKWTlf\_DK1X2pCkoNU4yoGo3DyHsoqcGjg)

C'est ici que vous saisirez tous les détails du point de connexion TaxCode. Pour chacun des trois points de connexion que vous allez créer, procédez comme suit

* Entrez un nom : TaxCodeFull, TaxCodeReduced, TaxCodeFree
* Description : cela peut être le même que le nom ou similaire
* Importez un compte de service que vous avez créé.

Basculez vers l'onglet “Documents” et sélectionnez l'icône PLUS pour ajouter le BOD dont nous avons besoin, comme ci-dessous

![Barre de scénario du point de connexion API avec les icônes Get from API, Send to API et Trigger](https://lh7-us.googleusercontent.com/byhA18LzkcY9ZyfnzyDlru5qBx88E8U1yggMNNkoHGsYVCbNkflNFXGVvJwMvE\_104VCjoYOM0SQIJVniyBBdn5UKasVR0uat6UvmCmpzz9ZYsY2Wv14B4ElOwqcg2qklxYAQVU84UOG70l3fMLRrwo)

Recherchez le BOD

![Onglet Document du point de connexion avec les sous-onglets Input Document, ION API Request Parameters, Request Body et Settings](https://lh7-us.googleusercontent.com/DAKzvEsjCmk1jy7L6GwrVY2DWg3\_InluNftWnR7hGlnyeBxSDW6XTDPBMLqtJuUc9Lq3Nga6-EKS4tZpOjE09h5FUJaTm\_E70UdA4l17jWGQ6BSr121lC3LzhffUXi6Bsk5EZEz4XHyjekk1Njb3H4I)

Recherchez le BOD appelé “Sync.LnTaxCode”, cliquez dessus et appuyez sur “OK” pour ajouter le BOD.

![Boîte de dialogue Select Document Type avec le filtre sync.lntax et l'entrée Sync.LnTaxCode dans la liste des résultats](https://lh7-us.googleusercontent.com/7BLwrq8kr9OTHleI2anmAr2-4ChksQ0pptddwm1quFHquGfnMBEW32RFx31ETGbrxf0KGVr-VzlZC9h9heD3ymTq9L5NZEV1b9E67IIR0is18UGBCoJ5j7KIMmF533EDMvZzgi4LXqAkV9zgCyl0\_Lk)

Passez à la section ION API. Sous API Call Name, vous pouvez utiliser le nom du BOD, Sync.LnTaxCode

Appuyez sur le bouton “SELECT”

![Onglet ION API Request Parameters avec API Call Name Sync.LnTaxCode et Product LN](https://lh7-us.googleusercontent.com/7MukO6oUAzVBFMPhFepwMvugqnhDDMhX9j7wZRU7BU0OusW3CKpMgqQNC7uNlehPp6eFniVxrX3DxjgsGZ\_Tmt\_cQOWGGiBfXAQfCC85amOGp1VY8RGo3nPABCiwzaIkYmnQF6t3FPVZ1fPV6fLazNc)

Sélectionnez l’API que vous avez configuré pour l'environnement avec lequel vous travaillez et recherchez l’API suivant. Une fois que vous l'avez sélectionné, appuyez sur “OK”.

![Boîte de dialogue Search ION API Operation avec Product DocBits-Demo, le filtre import_xml et les opérations import_xml correspondantes](https://lh7-us.googleusercontent.com/IpUUqJaXF0MmIeR6gtE9GDCccLfNsQLZ-RSHhQGVwJEj8WJwI-twgiHpFomBKhbnTUUKrhxJ0EUZ7F\_21MCSBjNS2VQq3azprekoxctRJZ-NJUHhb4J9rHUSRDoR\_OCzDHTG5q5KTwWMHOR5qNoNd38)

Ensuite, passez à l’onglet Corps de la demande.

C'est ici qu'il y aura un léger changement pour chaque point de connexion, cela se voit dans les mappages de champs que vous attribuerez à chaque code fiscal car ils diffèrent légèrement.

![Onglet Request Body avec le format multipart/form-data et les lignes de type de données pour data_type, field_mappings et file](https://lh7-us.googleusercontent.com/f4c-1M9mgCci2jjxkhaCDFX9bRWzMDaRwVv4XiaUH7BpHchPklvMnWoP\_ILSm6VB7GoFJNJzHsEPzk3eCFyLm1Kc3QI8OufjQ1mr7PqowjzViFDWc2opiNE1ODICtI9yEyUOi\_d\_hzN8CGo8gu6Ec84)

Dans la ligne field\_mappings, sous valeur, vous placerez les mappages de champs spécifiques pour le point de connexion du code fiscal spécifique que vous créez (taux normal, taux réduit ou exonéré). Ces mappages sont disponibles sur https://docbits.com/doc/field-mappings/.

Le résultat final devrait être identique ou similaire à l’image ci-dessus. Une fois cela fait, cliquez sur l'option SAVE située ici.

![Point de connexion API DocBits-Stage-Import-LnTaxCodeFull avec le scénario Send to API, API Call Name Sync.LnTaxCode et le document à envoyer Sync.LnTaxCode](https://lh7-us.googleusercontent.com/LSYrbElw6BgQbbIdSstbakfwLENZ\_09WQcQhjO7kbb2U3jSK\_\_wFnr43tIj2hTHYegQ9lrSZBuJ9N7MNewr2W3yjPCrrVLeP9UAZjvrKKBzeY9h-q6FrVd5gPtlH0iP0GpMcvhGxjAnHN7BlY8CmT3c)

## **Configuration du flux de données**

Accédez à ION Desk → Connect → Flux de données

![Menu d'ION Desk avec le groupe API Flows déployé et l'entrée Connection Points sélectionnée](https://lh7-us.googleusercontent.com/cpWAepQyLP8V0b-Oj7djzl21eZLU2JdnJPEMPs53Uq-adZbaCegl35RjguLx8rsP2E87ZmwbNgISFIpAy6kOeahaBCSygDVSJzmv1GQGn1w1MgR8N08mnnfhb02XjsLnt\_rVJKr4Y0UtiTf14NqTHLQ)

Cliquez sur “+ADD” et sélectionnez le flux de documents

![Page Data Flows d'ION Desk avec le flux de documents Ln-Docbits et l'entrée Data Lake Flow ainsi que l'utilisateur de la dernière modification](https://lh7-us.googleusercontent.com/HYqc\_P2DQjBoc-mpsyZ\_nlPFNiU17ZCLHfiOa282-Sa5JSA3Hv1XlwFjmlPhVGnAaEAqqalJ5ka43AJOzEO3uljwVAogAHkTVer7Q9JgI0WaOVX2Uo5Z8KGEqoa3BH\_zZwup7Bh4lKe4O5kr6hmAZm4)

Créez le flux de données suivant en faisant glisser et en déposant les composants depuis le menu vers

![Canevas vide d'un flux de données dans ION Desk avec la palette de composants Application, Database, Network et Message Queue](https://lh7-us.googleusercontent.com/V\_aJHPhFJssPUQ4mAHU20SVPSfhqhjU8BOQ2Ws1MtaauKp6OVAENLXod2uQe6Zbuc5JKZx6Bp3WyJtkQtkbnDluZZS5GLMGcaC9EuCrV8cn2aJk2y-Cih3PP2dg-umW0iDhak5UXNUuPxwkgqVg-mvk)

### **Application (LN)**

![Nœud Application du flux de données avec ses branches Get from et Send to menant à End](https://lh7-us.googleusercontent.com/2CCNlz0S-Z8p\_l9kPPUMqPkreoO3aLy8MkqY6UFMIABJRNFXGTFMXbaw78E42g8fEO4ZxFL\_oJMf2QnWn2xZLtS4zjN8AzCS\_B2i2x-tjWmmjyVLa1jSLQAnSB8-EhNfNISzf2uuX9kcqN-QixUUXvw)

C'est ici que vous sélectionnerez votre entreprise LN, le résultat final devrait ressembler à ce qui suit

![Boîte de dialogue Application Activity Properties avec Name LN_companyno et Application in01_1100](https://lh7-us.googleusercontent.com/b5pb4YfbZMCSi2X-xT4mj-Yw\_Uu77zNyJGl3rntVdqf907PwgX6Z9uQJIoHA2FS5M\_mVbdQgkh0HWgsOgtkoySmtrT7W8CrqsqlCnPEt6hv\_yODGulfp1qdxXvrB1HL-en3W9bY285fC3kARLZfSfck)

### **Document**

![Flux de données avec le nœud d'application LN_companyno relié aux nœuds API par les branches Yes et No jusqu'à End](https://lh7-us.googleusercontent.com/U8cqu3jABU3RQLGEGsS5qCnDkc-boTpAdZEVIUA9AlmD9Oz33JvnzD43SBTmLY55i8Bsr4lbi6udeIimCcRG1NgWbynv6OllCLaJPC50kJ0gPq7rsR5Rvj50yKngMiNvnYoLLT\_Hzn5cyhp18jq\_IyI)

C'est ici que vous ajouterez le Sync.LnTaxCode BOD de plus tôt, le résultat ressemble à ceci

![Onglet Documents du nœud d'application avec le document Sync.LnTaxCode dans la liste](https://lh7-us.googleusercontent.com/bgC1y3NtmX09XBjng\_pKmP5VQ5w0E\_VuFOfMF1rYs3iGGL5OaMHkKoyQJNtcVtbS6bEvF4KdtFNaX0VxT9MF0P-zTDnOnt5mhA0Gxcs4eMcRLtbXl5a\_8y84XyLyvh61-LdoQ7f15j-wE1nl\_TSYSDg)

### **Filtres**

![Flux de données avec le nœud de décision LN_companyno qui se ramifie vers les nœuds de filtre et API et trois nœuds End](https://lh7-us.googleusercontent.com/1Cv1XxqdpiNfonz6jdFgz9zGibQTRLd\_0ONFHf3FvzPB9-sQuX4lTUyuDWzm-RffuPf5jDmZAZwUqbXX-1kers1sEb9ykRMHeYYP6zGgF8yZ247Dx0nG04kSYUTTKSwt3NLS-3TwXA5tbvy5z8HA2bw)

#### **Filtre 1 (haut) : taux normal**

Le nom et la description dépendront de l'environnement que vous utilisez et de vos préférences.

![Boîte de dialogue Filter Properties avec Name TaxRateFull et Description TaxRateFull](https://lh7-us.googleusercontent.com/WVKWUme9uUjRRn7dZ5c\_RyPk\_GCTFEfiNxU\_H5aA979k5hOv2coDYEJHu4K1EaTLUf8\_Pd9ffOk757DaflF0Se0gZ1ZYvRk4QHlpKP0IeirfNr-L6JU3Z\_xFZJ2eeFI-Rhcctwk9QOHRORGNt1oIEpE)

![Onglet Attributes de la boîte de dialogue Filter Properties avec l'attribut RateNumeric et le chemin de document LnTaxCode/SingularRatesGroup/SingularRate/RateNumeric](https://lh7-us.googleusercontent.com/1gCPbUtC7KknzEHVZqIMKyjQGmNyNnR4c1mJ5x0LCJnAjd8D3SdW3W6nPMTsLokL-W2-XjoSM9MU1mJ77K12g887r\_jHoHBwquN1Ore2AmyjCaf\_YVT78KiKtY\_itlr-vyMvJrU7YV6ErgVSYbw5SEU)

![Onglet Conditions de la boîte de dialogue Filter Properties avec la condition TaxFull OR Tax16 OR Tax20 sur le chemin RateNumeric](https://lh7-us.googleusercontent.com/ijzGaLt9Uhzw6Wf66ah3auWo5TbkCnM-xGDYezsXXjPEkdCe5RO1wWfhhhG0qRuKbojijLKUm-WUV21eRdq36moWu9Ft0ujexe\_1lTUUEQbfXPvtrzP7iudkSaG\_oiX\_LV7AqZRGlNAp0OXnN8BXRIM)

#### **Filtre 2 (milieu) : taux réduit**

Le nom et la description dépendront de l'environnement que vous utilisez et de vos préférences.

![Boîte de dialogue Filter Properties avec Name TaxRateReduced et Description TaxRateReduced](https://lh7-us.googleusercontent.com/pKLo6q5zCQOZQhiRppyd8M-nlIrX5leGUiCct4Xn-4teIZTip5GAJVP0EFc2PrJ6EeDmU2KVOHRKVCaaML4sK8jCnsgTmxbTYjc-9CNd6bOfU-WD9tySeKL7gSRltjzoTEI5Ozrd\_s-7qj2KVNOWN7s)

![Onglet Attributes de la boîte de dialogue Filter Properties avec l'attribut RateNumeric du filtre à taux réduit](https://lh7-us.googleusercontent.com/87PoQQ5q\_35buL\_VNcvz3v-um1upk1U579LDASCJptnnC8ip5mwXxz89d1YmtIK59dOUhl9dfz6BrXBLSNUy6EnWU5uPmUEzbLQv-MwzR0dDkuM1BJ477yre-X4QeJzkkzprF9y5wCWY4zvaooMwIZ0)

![Onglet Conditions de la boîte de dialogue Filter Properties avec la condition TaxReduced AND TaxReduced2 sur le chemin RateNumeric](https://lh7-us.googleusercontent.com/Pa19AN6Mhxbn6bHSc5qKEGM0xRsEV6v77ooyeg5-91i8qGhaThb4328nr\_g6a\_z-7BOCJmWpo8Gbd2twl9FQkOf1Q8QZqOkJmxsIxaTP0R6dASgZdIV6z7p8PFYPYUJ1eKp8btYOBapliANstQSUgAQ)

#### **Filtre 3 (bas) : exonéré**

Le nom et la description dépendront de l'environnement que vous utilisez et de vos préférences.

![Boîte de dialogue Filter Properties avec les champs Name et Description vides pour le filtre à taux exonéré](https://lh7-us.googleusercontent.com/c\_SuWaZ3gF-FbOPWkxB\_eFgkT-TGJEYwV\_fQT05wGWHFNzI9SDZRQfauVMeBl0rn79QdU-W3kRgN-hWsYkfdMSevlYyiNPxxT\_3RxXcETo-lkjvI5TCygUag91PFJycrRdMA5hSQJCuzt8FekMwpu98)

![Onglet Attributes de la boîte de dialogue Filter Properties avec l'attribut RateNumeric du filtre à taux exonéré](https://lh7-us.googleusercontent.com/HGZ8fR6XgYtZ46i8Rov8xIr5J4z8DmGFfJkeovDGzT7S68VYI-OdG5jpMdoOiROIZckYMbVIlPQmS\_kWQazJVbco1t4ZH5Sr73b4xePlisnbm9ZLJrOPwtXn7-90F1FcFH99P6ZKI0hCWdI6z4d7qNA)

![Onglet Conditions de la boîte de dialogue Filter Properties avec la condition TaxFree sur le chemin RateNumeric](https://lh7-us.googleusercontent.com/\_APmMO6A2AG2km4H4em-ZMrn6\_XRpO3zxRhZwftiaKi5uoDhv3TTzCBfi8WVDCf6mOQNgtcEJ-z-BmP28J86noGJ5dgqVni2QIxePaO5-LU8fdwRqySUQt\_6wmFWiOFzTMmItcClQPRaSKUaosgWwNk)

### **APIs**

![Flux de données avec les nœuds API et le nœud de décision LN_companyno reliés à leurs nœuds End](https://lh7-us.googleusercontent.com/XDhVCKHYaxrRIFyYfq0guXwnZH6jK-WZIFj2i0Wkr4kxyNcdCH1TzKd0Pb3-H6qs-b7JZ3UUIGm0BVHiUL7Aya-D7YOSV8p8tnwQeAfBN30T4fW5-ANePN1TcvUr1gzLJPwj7rRO4Hw4ziuyYrqZBX8)

C'est ici que vous sélectionnez les points de connexion API que vous avez créés précédemment, cela se fait en sélectionnant l’API dans le menu déroulant “Select ION API Connector”.

#### **API 1 (haut) : taux normal**

Le nom et la description dépendront de l'environnement que vous utilisez et de vos préférences.

![Boîte de dialogue ION API Activity Properties avec Name et Description DocBits-PRO-Full et ION API Connector DocBits-PRO-Import-LnTaxCodeFull](https://lh7-us.googleusercontent.com/90c2E47fMC9CKNVY8DtgyaNUAqAnQmfErZm\_R-njUlEdIX6mafMUOk3GcAooaWfCzD4-OmdPUq5VSuMXmTSNjVEc924ASIPqmTxAQXqsq6eKs5y82rvwHxqnsT4S-sEm2mQRNwleiubkwIO\_kS9Vwzg)

#### **API 2 (milieu) : taux réduit**

Le nom et la description dépendront de l'environnement que vous utilisez et de vos préférences.

![Boîte de dialogue ION API Activity Properties de l'appel API à taux réduit avec les champs ION API Connector et ION API Call Name](https://lh7-us.googleusercontent.com/vw1hM3W4eCt\_8OG7Ht203tckaWarPOLi463WvQzGgixTMnfk7iC27JzL3iNgd5LmvBzWTFnYa3QNy5y\_oNSHJ9R-Ck5CAgLoBmGurbCn1RZ32jiSJr-LUnL3b0nhHctBqcCx\_25L1Ce-\_va3ZgfKXY8)

#### **API 3 (bas) : exonéré**

Le nom et la description dépendront de l'environnement que vous utilisez et de vos préférences.

![Boîte de dialogue ION API Activity Properties avec Name et Description DocBits-PRO-Free](https://lh7-us.googleusercontent.com/C0wmqAkrlgyXlMjKsGMOqre4MPLuHawrZB1oYDzkGFocperUB5dKea7kx44hrA\_Kz6Ptx495cQbwq\_EHfEGNvvpr\_0dvCuUS2zz0-SARyuNbf2gKsK3vTdd4Sfg3jWtE1YAN3o0VpoK\_HRn7T-fFOR8)

Une fois tout ce qui précède est fait, SAVE et ACTIVATE le flux de données en appuyant sur les boutons suivants

![Boutons d'enregistrement et d'activation sous le canevas du flux de données](https://lh7-us.googleusercontent.com/f8gkYY1Z\_W1if2h1es9vbjebtDX0zGiqY4p9OD68gKSAcNU6si-guvyIg8hzdjP7TulZ6Yq8NcbT2EyuHleVeNxpY\_6TDlbgIUaxDJ72ILcy8kVvFuSja7FT6gpYhMLFGw7wv-r0XyFN8xIrQ3OuUGI)

## **Déclenchement des BOD (LN)**

Open LN in Infor

![Page d'accueil d'Infor LN avec le menu des applications et la sélection de la société](https://lh7-us.googleusercontent.com/aAKRLInqsogQLv9nye2rHLtVFlW4yaCpnQ8A4cKG5A2145Tl6poOxthfo2InYimNk5dd8RabYrX9xP7sPO0aJ5ThF07ZVfKvUXBqVoxRJg53IhpeOeiA4B\_CGOpeLKWlPbCf4EaFXjgzmBOcezocF9k)

Accédez à Common → BOD Messagerie → Publier les BOD → Publier les données financières de base

![Session Publish Financial Master Data dans Infor LN avec l'onglet Options, le mode Insertion et la sélection de la société](https://lh7-us.googleusercontent.com/pMAgPzyhBNrEsFkTm8-iniHBhEXIPswoJ8URt\_v0fv\_7dSayrS8UkN7F9WMAOZQB9Q6sCe9faRl4rRDDft3VdrzfNUT-IbWxE6GyWPPKZh4R67JRmXmJ2NsTVPdjLo6uJdCpki7QDpgiY\_azWtqaqKA)

Sélectionnez MORE et cliquez sur LnTaxCode

![Menu MORE de la session Publish Financial Master Data avec les BOD tels que AccountingBookDefinition, AccountingEntity et LnTaxCode](https://lh7-us.googleusercontent.com/MtjE7Glgv7e\_F\_CJ4LXMuWk6SaInmNFlKzhGJu71iGgxRWtjI96lX5J0gqxRcj3y1u4E6Aq-xNEpuf83dsjHh6op0qeH89oBMvlVTTD\_VhGs10-gjuIb0eyc9b3dcCk75Wa5sASreXKW6SbQPYrs8sM)

Cochez la case pour sélectionner les BOD LnTaxCode

![Liste des BOD avec la ligne LnTaxCode sélectionnée par sa case à cocher et les boutons PROCESS, CLOSE, SELECT ALL et CLEAR ALL](https://lh7-us.googleusercontent.com/VTFntcBK0GVsUdr\_fZBUaN8rXYdufObLE7PnwwNg9QU69zYwKHvwFZ7En9WZ6p\_WGIkVdqEjBBYeIYSuHHJWBWYonwd6Edtr0ZZuGsX3qhNMDWQWefOaGfrYxrq\_yLm6\_gEw967PGp3HK0hzO-G2XiQ)

Revenez à l'onglet OPTIONS, votre configuration devrait ressembler à ceci

![Onglet OPTIONS de la session Publish Financial Master Data avec le mode, la plage de sélection société 005108 et les options Settings](https://lh7-us.googleusercontent.com/2tr7VHNOLActJCiLGC6jyWsdyqwZV7Je6UsekeoBo57qNpOBDYtOQuoelKOdvLMRo6uQJWn1S4ir\_zRZHAx2C96NyKp4ZjIUyFCYt58T59TqO3ml0ZfiEtSLwdRPp9g8pkMemN0xDS5ao8DL5xgosWE)

Lorsque vous souhaitez publier les BOD, sélectionnez PROCESS.

Le résultat final devrait vous donner une table similaire dans votre environnement DocBits.

![Liste des documents dans DocBits avec les documents de codes de taxe importés et leur statut de traitement](https://lh7-us.googleusercontent.com/4wK-mfKl0UNqvp5ngolE54miiwAKxAcOERO2mSDWzZ5t838VhFZrZGzCMeIyg7WDPpHvNzkeWRJV7ZZdsaxwXiFS9uxm29QZUYHhs9gU2v6QgSz07vfjpHXW3oTb5ZiiiTjI93gmV9MDTHbNWJmrvHY)
