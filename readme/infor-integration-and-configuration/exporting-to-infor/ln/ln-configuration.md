# Configuration LN

## Prérequis

Vous avez créé :

* An ION API Endpoint
* An ION API File
* Un fichier de mappage BOD
* Un fichier de mappage IDM

## Importer les fichiers de mappage

Avant de configurer le flux de données, vous devez importer les fichiers de mappage dans InforOS

Dans ION Desk → Connectez-vous et ouvrez Mappings

![](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu\_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ\_aAIxcJil5LNiep4U6KZr3\_tBfs1RRwXoW749q3FUxurXy\_pT\_k)

Cliquez sur l'icône Importer

![](https://lh7-us.googleusercontent.com/d\_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn\_Vd\_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* À partir de là, vous devez sélectionner les différents fichiers de mappage dont vous aurez besoin, notamment : SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.
* Une fois que vous avez importé tous les fichiers de mappage, assurez-vous d'approuver chacun d'eux en cliquant sur l'icône de coche dans chacun de leurs carrés sur le tableau de bord Mappage.

## De DocBits vers LN

L'étape suivante consiste à configurer le flux de données dans ION Desk, à accéder à l'application ION Desk et à sélectionner Data Flow → + ADD → Document Flow comme ci-dessous.

![](https://lh7-us.googleusercontent.com/rjPVR1EFKw\_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a\_Fn3s1HSYDRmQVvgZtX\_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Vous verrez alors cette page, c'est ici que vous construirez le flux d'informations de DocBits à M3

![](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x\_-lVRbK6tpTxvbRYKvwyWO\_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

Un flux de données LN ressemblera à ce qui est présenté ci-dessous (il existe plusieurs chemins car chaque chemin individuel est destiné à un type de document spécifique, pour cette explication, nous nous concentrerons sur le flux de données de facture).

![](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn\_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD\_3myQY4Qcd9motySYh9U)

Toutes les parties de la chaîne sont glissées et déposées depuis la section supérieure

Dans la chaîne, DocBits et LN sont tous deux des applications tandis qu'entre eux se trouvent des mappages qui convertissent les données en une forme qui peut être comprise par la section suivante du flux de données et “map” les informations afin qu'elles aillent là où elles sont nécessaires ou destinées également.

![](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0\_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC\_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### Application DocBits

Donnez-lui le nom approprié tel que “DocBits” puis sélectionnez le signe plus et recherchez le point de connexion que vous avez créé précédemment tel que DocBits\_Export ou similaire et cliquez dessus.

Pour créer ce point de connexion, allez dans ION Desk → Connect → Points de connexion

![](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l\_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Click “+ Add”

![](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc\_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ\_vj\_-XPdegP1P0ySdos)

Sélectionnez “IMS via API Gateway” et remplissez les informations suivantes

![](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

Le ION API Client ID se trouve dans le fichier ION API que vous avez créé dans Comment créer un fichier ION API sous la valeur “ci”.

Basculez vers l'onglet Document et ajoutez le Sync.CaptureDocument BOD au point de connexion DocBits comme ci-dessous.

![](https://lh7-us.googleusercontent.com/Wy2BIr1z\_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE\_333uCWuKvKiVoo99FrXVg)

Enregistrez ensuite le point de connexion en appuyant sur l'icône de disque dans le coin supérieur gauche.

Revenez à la section Dataflow de ION Desk pour accéder à votre flux de données. Votre candidature DocBits devrait ressembler à ce qui est présenté ci-dessous.

![](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa\_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)

### Mappage 1

Le premier nœud de mappage devrait ressembler à ceci

![](https://lh7-us.googleusercontent.com/9tlIun\_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw\_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Mappage 2

Le deuxième nœud de mappage devrait ressembler à ceci

![](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### Application LN

Il devrait déjà y avoir un point de connexion LN ou un nom similaire (pour l'entreprise LN appropriée) créé dans INFOR donc, tout comme l'application DocBits, vous le sélectionnez en cliquant sur le signe “+” et il devrait ressembler à ceci

![](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O\_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

Les configurations suivantes devraient ressembler à ceci :

#### Premier

![](https://lh7-us.googleusercontent.com/rj\_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn\_lmxtqUDVTm\_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Deuxième

![](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y\_MF\_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc\_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Troisième

![](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q\_epAj9\_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ\_rbCCixhWcaJg2kHyyYw)

La dernière icône doit être vide car elle ne contient aucun document ni information.

Une fois que vous avez ajouté tous les nœuds nécessaires au flux de données, appuyez sur ce bouton pour activer le flux de données

![](https://lh7-us.googleusercontent.com/WjQeGz\_effl\_RlkWC4CdJS9Dg\_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
