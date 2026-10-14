# Paramètres avancés

Dans certains documents, les structures de table peuvent être complexes, s'étendant sur plusieurs lignes, contenant des informations regroupées ou incluant des lignes supplémentaires inutiles. Les _Paramètres avancés_ en mode d'entraînement vous permettent d'affiner l'extraction de table pour de tels cas, améliorant ainsi la précision et la cohérence.

Pour accéder à ces paramètres, activez le **Mode d'entraînement** et cliquez sur l'icône d'engrenage **Paramètres** dans la barre d'actions supérieure :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FW1cBx4IOjycKv6IZM9AX8Wggj1eEBgzBVJWgsyWkutX9dRRJuEjQtSCsPaNZuRndd9ewMVvfqSXr45C-2cO-pxXkYFdl_9eEGVW6-UBqqZCsuhia6alJjD1ZuZawwSbjS9Yeywe1wDK5yAcIOUH5QAw\&width=768\&dpr=4\&quality=100\&sign=4bf6ac31\&sv=2)

## Nombre de lignes d'en-tête

**Utilisez ce paramètre pour définir le nombre de lignes constituant l'en-tête de la table.**

Certaines tables ont des en-têtes sur plusieurs lignes. Par exemple, l'en-tête de cette table s'étend sur deux lignes :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FJ_nYZKzUSJHcpJuNp1ykf6shnfetOuiIPhyhyTfSqh_cTsDT5obwOSIc21OsLkjF9tMBP7Q1GQ1ZQfBsEmQIrJpfX3QpdjHnLkzInsjpngeg2L7i_TAyl9MdVmgHsDpUvoURdxfqp8FOdJxuRAMCwhk\&width=768\&dpr=4\&quality=100\&sign=554fa70\&sv=2)

Définissez le **Nombre de lignes d'en-tête** pour correspondre :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FG8-QpKxnRin9PGPmkbtJ35r1EugXsD4_Yd5QvTkdbb7sXqRVC3a9t0cIlNILJHLr--GsykgAlMJmMYbJaUoMqHEPvAT3PlPNf-syCmPz_GVMFEMsbhcHI2DQBbT4MJXjS2Sx7M3xl4zAzcw3aa-XNms\&width=768\&dpr=4\&quality=100\&sign=a487f5a9\&sv=2)

### Pourquoi est-ce important ?

Si vous ne définissez pas cela, DocBits peut traiter la deuxième ligne comme des données au lieu de faire partie de l'en-tête, ce qui entraîne des erreurs d'extraction :

**Avant :**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F35BElgcq-zbs8wcGcguVSKHRpwQXqQG9dQmBaYa8BT4RNwJxd6g-jL5wlQgrnVLrMxtpncr8ayaasWVV3snGpBiDUWs4Zx7Tn2Dck-YFBpanlcN500yIWkVz9RJXQhoq6op0WbYcgklp_LsmE9LXt9k\&width=768\&dpr=4\&quality=100\&sign=7c68faf7\&sv=2)

Après :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FbPGn9eWPK3Mmbu_ab2N3tVVP8ODho4MW6r6ynSKJWiPxq-IPlP_0Q1ghfcwjN56Sp_HA0nV-fedAfzkZoAXsj5O5ata32PCXPHJQ-dizWZ1OdpdEPS5wSPNW9jjc7TSPKQiNnCGPjLtnXQDLCbwEj3U\&width=768\&dpr=4\&quality=100\&sign=b032f2da\&sv=2)

## Déplacer les lignes supplémentaires vers la corbeille

**Utilisez ceci pour supprimer les entrées sur plusieurs lignes non désirées, telles que les descriptions débordantes.**

Dans cet exemple, la description déborde sur plusieurs lignes, mais seule la première ligne est pertinente :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FAEFanKF7uUtS_78nxi5zESPW8WOESa0Do_sCQCsttC21KoFK-sB9TQgFHboJB7CMEpc_auEbeXINU4BpEh8XuNMBHDYhuwjVX40cRyygxECs3XogrurWKNdw4s4F1kxWXLGrrF4jSqd1bba0dKPVO2E\&width=768\&dpr=4\&quality=100\&sign=926d60ed\&sv=2)

Activez **Déplacer les lignes supplémentaires vers la corbeille** pour supprimer le débordement :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FQdYUZ0ANpuFRkvNxVZzYfEhTRVf2fk1jPmoNUZcNotdkgL6VDHV1BgBXU2xqFfjBJ7W6uvB8TRZcpKEk7Qk_c0mIohiS4Jl9ZPRpG7HdS_EktuCcAtJ4KjJ_vYvYok7lv0nz2MfVMG08oDFqRSyFHy4\&width=768\&dpr=4\&quality=100\&sign=135061e3\&sv=2)

**Résultat après le mapping :**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fzto-P_Knp1YQmCUBU6_vCg2IEwaBiBeAao8Jvu30-89x_Sj2BLDSTQu31vUNBlaQp73DPVy2F-UZawn8j4hxycD6bpfCf_KXZYvrqH5w0cwGwsjatBelIh6gdenY-NpzmQ372jtthucHpMrsXNz3DcA\&width=768\&dpr=4\&quality=100\&sign=741cbfd1\&sv=2)

## Nombre minimum de lignes regroupées

**Utilisez ceci lorsque des lignes doivent être regroupées sous une ligne principale (par exemple, des éléments de ligne avec plusieurs sous-lignes).**

Ici, seules trois lignes sur six sont pertinentes. Deux colonnes clés sont associées (par exemple, Position, Description), tandis que d'autres sont traitées comme des champs personnalisés.

Commencez par définir le **Nombre de lignes d'en-tête** et le **Nombre minimum de lignes regroupées** :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fp0k-n1IG3_FHexG4iAlISSmN4Yaq9xUjRO2cLpV3w6a67DpULRnxj4x291DOXBVx2SHqKp6Zs-ZXxr8KHKzT9O6oCwgEOkvfMqwpDGZUrfFpozdR16sbaybtrMEqDOXO1TsNmuPFz6mOKX0pR8I5RO8\&width=768\&dpr=4\&quality=100\&sign=e19a8ef6\&sv=2)

Activez également **Déplacer les lignes supplémentaires vers la corbeille** pour nettoyer les données non pertinentes :

<figure><img src="../../../../.gitbook/assets/docbits_approval_2.png" alt="DocBits Approbation 2" width="522"><figcaption></figcaption></figure>

Ensuite, définissez la colonne clé de regroupement, par exemple _Position_ :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F5hy2YTNQRZ6plQZnc1HwAbAUXU7LKfNpLdlfr8sPnDXMryv0KoAGgkcqAWqjvznvBa1YwW0ecTrpStpm5AIc0qiFX1zB-I_y_crIx0jKS2t6QVKdAz66Wb3XMt9sRsEUHKIuk51_AatHNCRZjOghn4A\&width=768\&dpr=4\&quality=100\&sign=6ca2a12e\&sv=2)

**Résultat :**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FxaorEjiOEeypLMAAOXvm3VAc5BVzhIujUeLdSt0SPwrEz5x_hd8sb3Hhc7OpnUpzj6qvjWWptOsefhxjF5pIzf12RVXah1wPhlMoa3Wwx7T3s_D7Pzw8cryaAzgh8SpN-uTxpl1FWke8v33dh2VNgJ0\&width=768\&dpr=4\&quality=100\&sign=e955b28f\&sv=2)

## Regroupement inversé

**Utilisez ceci lorsque la ligne de regroupement apparaît** _**après**_ **les lignes qu'elle devrait regrouper.**

Si la ligne qui devrait être regroupée avec d'autres données apparaît _au-dessus_ de la clé de regroupement, activez cette option :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FiH7rDa637FWtr8wWtXpdqSh68xsaOFrb_vIWf-ZOpAjExmFPHVRaDGGipdwNy30gpLmEWT0UujjqlbcSlHU7ldQ5zhAy15pMxuqbDpS2xFSuL35EjbaXfFQTOSSO3QE_I37kvdL3i5k-N7F_9tedMss\&width=768\&dpr=4\&quality=100\&sign=95d583b1\&sv=2)

Activez le **Regroupement inversé**, regroupez par une colonne principale (par exemple, Montant net), et utilisez **Déplacer les lignes supplémentaires vers la corbeille** si nécessaire :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FFJNKYXmELlMFi-Zh_0Pjgc0pcKI2-_UbDhF7b4D5p7GA4f9r-FqjruzkJw3nfJH4NA0G_BC2xQpJEzl26GbOlPt9fPyOkGowtGWgRWt5GJ62Vj-Qd04rDP0kzDFiJnRlpWF13d9YQ1e-FurQI-gHJx4\&width=768\&dpr=4\&quality=100\&sign=4b2677ae\&sv=2)

**Résultat final :**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fe8x8gIUV10Y_FmPeW_X-UZw6uJ8P7alQTDy_m5OGGLZ8Ev7Ip-C-6fqtTixiSU0ZnLMIc4VR_f0xJV6beDnl7bFBIh4U2dME8KHB3qokj__SrQGp-3BXeOsN63SabFNd5miRCtK-jlf49nzcbbe8UJw\&width=768\&dpr=4\&quality=100\&sign=f7571dde\&sv=2)

## Résumé

Utilisez les _Paramètres avancés_ pour apprendre à DocBits comment gérer avec précision des structures de table plus complexes ou incohérentes. Ces paramètres améliorent la précision de l'extraction en tenant compte de :

* En-têtes sur plusieurs lignes
* Descriptions sur plusieurs lignes
* Éléments de ligne regroupés
* Ordre inverse des données regroupées

Activer ces options pendant l'entraînement garantit que DocBits se souvienne de la mise en page correcte pour les futurs documents du même fournisseur.
