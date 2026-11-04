# Comptabilité automatique

## **Prérequis**

* Flux de données M3 vers DocBits fonctionnel
* Environnement DocBits correctement configuré

## **Configuration Infor**

Dans Infor, ouvrez l'application ION Desk. Dans l'onglet de gauche, allez à Connecter → Points de connexion

&#x20;

![](https://lh7-us.googleusercontent.com/Gl49rTfnpYQjXjpUNF3SEouZiJ4pPeHVk60d7dyHizfPLT6sn4AoKVQPPvpgg2cD4ts40hDeWQRs3BqmKW-CAco7Dt0oWKF7ukQJUVDBgSUoMNHt\_gRkqLxkF5CC\_CNGpVRzrNs7rfF1msK320\_J02g)

C'est ici que vous allez créer le point de connexion nécessaire pour importer vos données de M3 requises pour la comptabilité automatique.

Cliquez sur "+AJOUTER" pour créer un nouveau point de connexion, sélectionnez l'option API comme ci-dessous

![](https://lh7-us.googleusercontent.com/ctE76pck6mGmBVxRIMhHyn0TbSKKsiGjO7rO185fjndTIo7qYyvSZS3neUdV2CWPqBSangpJ4oG\_g946\_KyOwWyJvacZe5htWiQLTZQLzfNHvsHDhmMQmjh7MrGsqKp6sm-XPcGmEwrH2ZMYCd0bUl8)

Vous devrez configurer le point de connexion API appelé :

* PlanComptable

### **PlanComptable**

L'onglet de connexion pour votre point de connexion PlanComptable devrait ressembler à ce qui est illustré ci-dessous. Donnez un nom et une description appropriés au point de connexion, ainsi qu'importez le Compte de Service que vous avez créé.

![](https://lh7-us.googleusercontent.com/p-jly6\_S96TsCmpFg9oOob0h7Q7NBlTxRKgNCphiy5QfbK\_lrLMAR2miVUQh-fXrCfGdZr17ongp5c9bnK6HuHCVuDArHhYcmKDlAyO52tGcxg-VXBLXZ1ka8yqZ4DWnxFFMxUKkE7jgvCgr7P-nzdU)

![](https://lh7-us.googleusercontent.com/GkX20Q23htKae7OOcGnJ5J6f0L4I69vOU9jYBpY1m9bpDPdtsD584mh\_9IaZF37Ne1OY2uOPgFxYYjwTrBOoZqahpJLlY3n3qmBn0sgzC0eVu91wE0NWBvESBFJmeVTITQoqUTEU56tHEj47-LQmI6E)

Vous devrez ajouter deux BODs dans cette section pour ce point de connexion. Il s'agit de Sync.PlanComptable et Sync.DéfinitionCode, pour ajouter ces BODs, faites ce qui suit :

#### **Sync.PlanComptable**

* Cliquez sur l'icône PLUS (+)

![](https://lh7-us.googleusercontent.com/hFWg7-4Osuy9Q0uZYqT9yfAPFYsBi7yitHj7BBxQ94vbsDVg-GuCeTBakvV2eQNjqMGwDAF90nO5h-OxFR8HtYEiYcALdBq5Fdj\_Gl-wU8QePGV4Wr3\_78OK22nUY35dfCQhUPQIp\_qkdHN0wr7V-VY)

* Sélectionnez "Envoyer à l'API"

![](https://lh7-us.googleusercontent.com/jA97YupOjXJlRFRxduo\_tYO4YYDZoT0mHxWaPWfJGyU4RTNSVNRAIAsR5mzRyLh1iusHl0cBKUxhYj3hQMzacGdN2QGsvPGy1vHeq\_JNhDqxc-SI5HtZh\_Z\_zmaSjyJwmr2337tzYSWfqDl3JGkjBqY)

* Recherchez le BOD Sync.PlanComptable

![](https://lh7-us.googleusercontent.com/hzuwy-VU8xpgQ85NGHAk9u-m-\_Sw4iffT0SNtWTJw9iWHRIsIvGTEYQgJYi7CUoYC7\_Yp2KDtsohRQkNtIgr1VutFbR8mTkT\_5HmJ7ecgW8pcGuZTuwxtPDOlJpWuONq3WPIupRRBxBJPlsYQ9w-bxo)

![](https://lh7-us.googleusercontent.com/6p8nXaRAI0ucRzmyKfYYg3J8MmHXVgHs-KxcItxeZ6wbefK1YdMrYSblHwnXkSiajApB5ds\_EgpJJWYjfbKOjHdsh-H49jG45weOX9v0YBSAqdXmKgoaBcP7A4zDyINMNVt7RWgbQ51WxNTsfBllvQ4)

* Basculez vers l'onglet API ION, copiez le nom de l'API et recherchez l'Appel API en appuyant sur le bouton SÉLECTIONNER

![](https://lh7-us.googleusercontent.com/aRXjuD3nkYsFNM2eYkfmHrshU3ycmN5G4OGSFFadbSToy3pHKYWMw6apbyMhJ9o-5xB6UDA4rbdPjZWAdP-OCH8gQFWV5vWXp0rqLxP9DozP4yMS074\_nsHzirJUgBfkBkQ8Ydp\_WjImf2bx3pDnLPE)

* Au produit, sélectionnez le Point de Terminaison API que vous avez créé pour l'environnement avec lequel vous travaillez, que vous avez créé dans l'API ION. Recherchez l'Appel API suivant, sélectionnez l'Appel API et appuyez sur OK.

![](https://lh7-us.googleusercontent.com/LQWk7uiEPCxJcohMmIuRrg2p\_wwE\_h5GoEEP3Y2IdpKARppHoGB4Rt1KRM\_2AiXyG0-ieIV7BM51IRN5exKkhG8eLTkKCftm88j2NLc15X50VLu9t1sZZnQ7DsIIvgUsxz7oryzVIkfmifw-m3qkLDY)

* Ensuite, basculez vers l'onglet Corps de la Requête

![](https://lh7-us.googleusercontent.com/0tnYxKvtW5Fw7yJfW0QBMclidw5kKJB4oi6M932hGO8ROokbMXbyFcjPQq\_LSVe8hv3ZyVVWqjDO4vMMRgPm1L2iXV3pSoiyzrxGLvBTx4kwt5uo6XtHEt25PRVdM6aIddhHDrT7HGzx3JaZ1F02-YI)

* C'est ici que vous configurerez la correspondance des champs pour ce BOD, votre configuration devrait ressembler à ce qui suit. Les correspondances de champs sont disponibles ici.

![](https://lh7-us.googleusercontent.com/3giuZYeQjdZZHAg7W-pcAHB\_69KP8Ukh\_0NhATYBxvrS\_Qy3yH58fQyrp6GKfOzi1xJms5KV-XVNnAWtX6VmIBwdxSVum9JA6-H9W3XIUYKiTEK3IWoKA560a5I2lwmYd0kitdfC4pRkQVULyWp9PpA)

Une fois que vous avez terminé les étapes ci-dessus, vous aurez configuré avec succès le BOD Sync.PlanComptable. Cliquez sur l'icône PLUS pour ajouter le prochain et dernier BOD.
#### **Sync.CodeDefinition**

L'onglet de connexion pour votre point de connexion CodeDefinition devrait ressembler à ce qui est illustré ci-dessous. Donnez un nom et une description appropriés au point de connexion, ainsi qu'importez le Compte de Service que vous avez créé.

* Sélectionnez "Envoyer à l'API"

![](https://lh7-us.googleusercontent.com/YLaFsc0K1Lzruo84Np3EdCTF1xsaQOLRypNpgZB7L9keTh1TwPOMnjBxJYnBOj8GrNSG\_URcRGgv\_p70-pjhBed-wvURRW08YtEWjmACMc3CleRPrHia6nihWQwVOUaZ3qHD\_zLy2W\_iMQ0I77cY\_Bs)

* Recherchez le BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/f3ikl4jh0PBhYmP3r80BrHuGGu9w9MHe-E0VmyXOCmFEkkK92cxgVimwyP8RF0kF2GruVaeDjiYRKuONX5bQ2ZBRmdKFx8Bf9cHvX5q-xYnXNH0a2xnR4eg1ynyWbRRRoY5xn28HJ\_ziRiKcTN43aHQ)

![](https://lh7-us.googleusercontent.com/nXQZ1LLZsrndggHkAmRtMlV7YzFemnjC9CnS4AdUVDits4zNfzlaqKdHnNcLyTtDkQSX3SB8R3fnZhGBPd-By8C364IIYc4vE2VXNXzoa4LfHP6irTiAg\_N\_2BHSYBLzaQyMCN1w5LdFiiqeiiwAXuk)

* Passez à l'onglet ION API, copiez le nom de l'API et recherchez l'Appel API en appuyant sur le bouton SÉLECTIONNER

![](https://lh7-us.googleusercontent.com/LbHmVr1PimQkPu-t6VMvNVk9wVXeQBHOu-X4pW-9vGm-dON2buizVGbKekGL7tY1t4OkwQtzhl7uDhq908UxCfDCJaRDEukpk-07pJjLO-ezRUHgblp3REm0qrKF9wOtMkNWJlVVNVhmfzZ0TtUsqQQ)

![](https://lh7-us.googleusercontent.com/K-kDDTSaZiothC4o3JDihhVJFNt0PiBnLK7kF6RcBOX9EpzutfLHGstzvywBBqaEqm4WqOSQSxtvxRPtbVafPlhtf\_YMVkXjhTkvnGwLzwH\_p-YgRCGAu-DzA94MHjqQoAYTSBPgojcGlJs7tBRcpME)

* Ensuite, passez à l'onglet Corps de la Requête

![](https://lh7-us.googleusercontent.com/DfT6FtrbW7LbK4b4I6ssYDWOaPgUxkWsuTDpvQGw549tPFxgEU\_gmh3UwXTbyKHZR8SOHXPHDdobEhA91RIMB57ZAVatrZEsad2QW6QHiUkdZoyW\_yE\_iIGDgs2IrY0I6qL1JTZxksYoaLKu0Il8smU)

* C'est ici que vous configurerez la correspondance des champs pour ce BOD, votre configuration devrait ressembler à ce qui suit. Les correspondances de champs sont disponibles ici.

![](https://lh7-us.googleusercontent.com/nqK7x1Km4wIP9aWnvMlSHl1\_omw22GRKONfB-zc8ikn\_rSsl60Ksml0oQacs8UNmPSLFSKPD7Eo9FsH42RjDo4oragvHZJHFW\_yv62KXDrF3SKnDN2-X6vqYJ5a-3bYkkvPDlNJSxFylvtAFr-2Kt8Y)

Une fois que vous avez terminé les étapes ci-dessus, vous aurez configuré avec succès le BOD Sync.CodeDefinition pour la table de données maîtresses M3FlexDimensions.

## **Flux de Données**

Vous devrez configurer le flux de données suivant pour la Comptabilité Automatique :

* PlanComptable

### **PlanComptable**

Un aperçu de ce flux de données ressemble à ce qui est montré ci-dessous (le nombre de points de connexion API DocBits à la fin dépend du nombre d'environnements différents que vous configurez).

![](https://lh7-us.googleusercontent.com/RfkP8xiF2vDzQhBNa66L0NQHk7TGjj52aK3hWoisEnWbdG3l-SZKKw8mYJ3b28ShXZ9omPS6WdNiXaCpYRQzwfges0SKznwQal7K2ElILbGBJNYu3VFm6gDQJMHYRItAFX0cdRZjXgCk2FQqHJ4iSjY)

### **Société M3**

![](https://lh7-us.googleusercontent.com/tqYoI-gLUpe0c0x1T-WhP0\_FolVzPGHhFY8m52Fw38mJNzsDvjb7stRrBfWVjXLnFrJTTy2lyd9Dmva3\_EPG5eRWyf5ATA2cTWvCj3Ksa4Fu4pHF6rNFjfd3Cjei0UlibT0HAQYE0V22bdTStjY61zk)

La configuration de ce point de connexion dépend de la société M3 qui contient les données maîtresses que vous souhaitez importer dans DocBits, la vôtre devrait ressembler à ce qui est montré ci-dessous.

![](https://lh7-us.googleusercontent.com/wpSluEs21T5wXG0egZPfUCYBP6X\_uUm6XAh-PyD8RrojTuIztzRJzhVYdzcNI5dQGGDsrhSKx\_K2-y0JDmK9w41fVUXWcW1N2lz5rizXcMnn5BuiaGRy-TEOBryGxvP9mBGJTZ16lMisoC\_YumwpS9Q)

### **Documents**

![](https://lh7-us.googleusercontent.com/uR6XaFI7TPQ4L8Suom25PBdtXdL4i100Juz7kRBxT5rdxhejZW7nPtVIlEGjWWnZLbo9ipx7G95NBFV8dd-g4vw\_vM-uPApJ02QdxvCmX27bwAW\_qUWUXajV6BFVmIfzTQ46Zj4DybsYKKblXjuWc6w)

Les documents suivants doivent être ajoutés au flux de données :

* Sync.PlanComptable
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/6Bq-yQ9Yaf2OJwjBxyFvqAMUitcovquo\_iU4hc-pgag1iDwLcstggVjLsdY3bRl9XWNc3mKOwZrY1FSlu47IzxxUQHFkjIAl1r08Iw9UbKaaMh4WiWrqFuSObdTjEvCEI5IDvD\_Pys8jAydydJgbsK8)
### **Filtre**

![](https://lh7-us.googleusercontent.com/LyKGzQUEswTD1XfpNDPSHjChgqNFfs4guXfM0KNuW2fPoiaeUo4uPrlGgwt3RepWUGQmu\_trUMiWb68cUjUAwXU9IRoWOsv9M2l5v4zFfBkEcioz5ok7Eoss7I-tBKtpD7wVUkGWi3U3ySrIQ\_fDPiY)

Pour la deuxième route du flux de données (selon le routage dans le flux de données), nous appliquons un filtre avec la configuration suivante.

![](https://lh7-us.googleusercontent.com/7xdqGdo9bS6\_IIzTVYF\_08woBXvhIVkA-c6-ZrDpDEzmEDFzDZSuxZ5LYHKVUhJqYq4Wlq1FXPfr5myjKFUsMbnJrefc\_L7URD7AbEq\_D90jEw7o8Yrhg5XZwLdU83OwlZVXqlYla61b0LyISXeBLWk)

![](https://lh7-us.googleusercontent.com/OdI-0FaqDaPKy2g9Mr8HUx\_oGRZkDrkeI6P1rWqOounpDauMThaqzs2wOawmw3RwcMlQHgI6wj16RXQDAP\_JNMGkxvmiEnPJ\_bvse2CvMegPwinSIJRLmXaCzfjxtB1FDqnqPOMwrMYNKJyiC2sGUe8)

![](https://lh7-us.googleusercontent.com/RMPIV6ZWsUcBA6klny6Ln-\_nhMGl1zdEHfUKK56owelabcG-6gM1S\_eqWAVLTeOHdec3D5D6xVJeC5evnJC61L8daV6IbJbCmMashkWXSK4Tv4RdE\_erjR-Mk2RihPodIG4HrqSOQ8hi7SG3xctXd-E)

### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/Npm92rS\_EO5roSy3tldC88hFIyiDnZjHnnVSkkKyfmNrOcbuVj4LPNrcsWvOT8IHNQKGMqIZymG9q3VMGG6RwvuRBqZgmhHxqXn1oieajDmz8giQxSr8wOFzb8TQTJJWwj912-sDRtkrDAXCr7ne-pk)

C'est ici que vous ajoutez le point de connexion API ChartOfAccounts que vous avez créé précédemment, la configuration pour cela devrait ressembler à ceci

![](https://lh7-us.googleusercontent.com/Dw4y6OMuMAYHZjH1etj\_FqdsaFxaRhQyk6\_PaxXrWLhrNirEn7xQc5uIpbDT6Wz85XvZgY02aNuWfbYKBzo6W9aavN\_Asu5ENfr2dszWYQqs9sy6zl4o0NxRe3IPXodLIGf9JkbK2\_UtYe4dVii0JbM)

## **Déclenchement de BOD**

Une fois tout ce qui précède est terminé, vous devrez naviguer vers Infor M3 et déclencher les BOD afin que les diverses données maîtresses dont vous avez besoin pour la comptabilité automatique arrivent dans DocBits.

Commencez par appuyer sur Commande + r, pour ouvrir le menu d'invite, tapez "evs006" et appuyez sur Entrée.

![](https://lh7-us.googleusercontent.com/pzAL0cnM94AUE4KmTyBV8OPU9ft\_g9o0-KB9Ib0AjrvG7Q59GHT-2biP4n7yFyXRxQ0gjy85G6MWMWUeMIWJcTQ9TKwzCEywd7I\_6\_vV-muepobkW0O-4-CZxsmjOEQ7uM1frZpTLqlLS3aSYkEuwAw)

Le menu suivant vous sera affiché

![](https://lh7-us.googleusercontent.com/Wx41TNpg1zuaf1rXIBvSCVzSRf6q74rdLs91el21iErqQnDiF4cv7X0nyDaS2Gjimj7xbfAK-7mo6sXN6fkK934mHnCnivFTz9NqHi6dBoMYiRT\_vLrkVUlFd\_T4Oan3Zkq3WKLoI-kmsElHSKO7zY0)

Pour ajouter les différents BOD, vous devrez entrer les noms de BOD et les noms de table pour chaque BOD individuellement.

![](https://lh7-us.googleusercontent.com/5gVWRDm\_8CSyoQRkq-7LuI8MLU1BjRN6Z6YCcVZp7G3Be62nQBht-eUNZreTzV2rFWYK\_RcKiyzwTTlT5y5X8eGf-Z7qDavDyHML0zv6Yt6jGu2z9d-nL0K-m446nDZa2-aiFLnnzjAwk8pTT4RQK6Q)

Les BOD que vous devez ajouter incluent :

* ChartOfAccounts
* CodeDefinition
* CodeDefinitionAccountingDimension

Pour ajouter le nouveau BOD après, après avoir saisi le nom de BOD et le nom de la table, appuyez sur l'icône pLUS indiquée ci-dessous

![](https://lh7-us.googleusercontent.com/66wclj8g8RAYT9-UIgRMs0qnuA9srmWv21PdqdNm\_q5icGmabL17-DpLOSs4pm6Nj3xJN-9xt7io\_5GZGfzSQ2qt\_8Y--CJFou6FaOdufiuxOdKHrUUYELNdGy9e-gnWg\_hAMSfs\_NJa6zYBMpoyTVs)

Les noms de BOD et les noms de table sont les suivants.

**ChartOfAccounts**

* Nom de BOD : ChartOfAccounts
* Nom de la table : FCHACC

**CodeDefinition**

* Nom de BOD : CodeDefinitionAccountingDimension
* Nom de la table : FCHACC

### **Publier les BODs**

Après avoir ajouté chaque BOD, faites un clic droit sur le BOD que vous avez ajouté, sélectionnez Relatif, puis Exécuter.

![](https://lh7-us.googleusercontent.com/225-ujyGzG\_RJOXgbx8NOh\_4s-Sn\_o80b\_h0DTsJqfr6OcyPUwkWLF2lfEyzFFFKddKmlWd32bb94qeYlOdVBTI8RL0r6ZfZKloVTrAYLNp-U5gL3aJhW4d72ExkkyM4AydLczsPvdE1cRDfGNKupdA)

Vous serez redirigé vers cet écran.

Changez le verbe BOD en "sync" et appuyez sur SUIVANT.

![](https://lh7-us.googleusercontent.com/3DyjXUSlAF7msQT1OAO3aCr1U9R68XZj0oE\_yJwsBrBj-FkiZR-oRYQYSClHG0iN0FXFdDdKQA1hOBlw3jc-lXQCWkiDFa0IweuQnoR8k-Mgyp1HeI5ImJqNogz-Q3b3P33ywb0B2o1pZ-TkZ7mAwZA)

Une fois que vous appuyez sur SUIVANT, vous recevrez une notification indiquant que le processus de publication des BOD a commencé.
### **Élément de coût**

Pour importer la table m3costingelement dans DocBits, vous devez suivre les étapes suivantes.

Depuis la page d'accueil de M3, tapez Command + r et recherchez l'invite "PPS280".

Sélectionnez l'une des lignes affichées. Dans le menu suivant, sélectionnez OUTILS et "Exporter vers Excel".

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m\_blJ\_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI\_anUNvmACFyx\_ssgxaqWq25vLt\_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Sélectionnez "Exporter toutes les lignes" puis appuyez sur EXPORTER.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis\_zELtCIfpmkIUKgasfrdfNW-dr\_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP\_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6FcdpeClZ9L4)

Une fois téléchargé, vous devrez modifier le fichier Excel avant de le convertir en fichier CSV.

Vous devrez ouvrir le fichier Excel, qui ressemblera à ce qui est montré ci-dessous.

![](https://lh7-us.googleusercontent.com/l4WbidK-5zSEQ6rwqhknudPBmmDji0f1WwTh-kHomSkgEOA7s4m72cLw8z-4nflqBvPp\_2AajIEZDZz4dRLs8jlAeYHp4ee2tDysxYy8YBjj4ktHxdUXpxO\_Z34c8\_f0cNMX-9lp0lT5wOZoH1QUCgE)

À partir de cette feuille Excel, vous avez seulement besoin des 2 premières colonnes. Modifiez la feuille Excel pour que le résultat final ressemble à ce qui suit.

![](https://lh7-us.googleusercontent.com/QaNRlKHrU6kZWFqmwYR8C\_\_nLVOeqowAxJlvooSVBIAF5ayx2xZtUppsn0jzBcJVi90vemM3tZMZOjn549N3RzMuWuE3w911WLVS5NMuiUmnfXM\_xUXbqmzBtiQZstnpEYj1dUSbs\_IkAydlhBfdmcc)

Une fois cela fait, enregistrez le fichier au format CSV.

Une fois que vous avez votre fichier CSV, accédez à la page Web suivante. Cela dépend de l'environnement que vous utilisez :

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Ici, vous téléchargerez manuellement la table CostingElement via une API. Cliquez sur le bouton Autoriser.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O\_mxN5bSVp40jYfgsVJcE\_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Vous devrez insérer la clé API de votre environnement DocBits. Cela se trouve dans Paramètres sous Intégration.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq\_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf\_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i\_gvBPuE8CvfwRpX-ZIlb\_g)

Une fois terminé, recherchez l'API appelée master\_data\_lookup/import\_data et remplissez les informations requises. Une fois terminé, cliquez sur EXECUTER pour déclencher l'API.

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

Si tout est fait correctement, la table M3CostingElement devrait maintenant être dans votre environnement DocBits. La comptabilité automatique pour M3 a maintenant été configurée pour votre environnement.
