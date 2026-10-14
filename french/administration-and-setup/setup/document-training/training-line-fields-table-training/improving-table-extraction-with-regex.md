# Structuration et amélioration de l'extraction de table dans DocBits

Une fois qu'une table est extraite et que le mappage initial des colonnes est complet, vous pouvez améliorer la qualité et la structure des données en utilisant plusieurs outils intégrés. Ce guide vous accompagne à travers :

* Regroupement des lignes
* Sélection manuelle de lignes
* Mappage des colonnes
* Affinage de l'en-tête en utilisant des regex

Ces outils sont particulièrement utiles lorsqu'il s'agit de mises en page de documents complexes ou incohérentes.

## 1. Regroupement des lignes

Des documents tels que des factures ou des confirmations de commande contiennent souvent des entrées de table où une colonne (par exemple, une description) s'étend sur plusieurs lignes, tandis que d'autres colonnes (par exemple, quantité ou prix) n'utilisent qu'une seule ligne.

Prenons cet exemple de facture allemande - la colonne "Bezeichnung" (description) s'étend sur plusieurs lignes :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FVino2M4Esor3IRHGqBd5Brx7_lKPIwEOlRYBHzMXw4WoacFNW39hbWuwoUNGocubx4Bh9_BvUBqZSWA4U_NmU8FBw4Q1_AiTASgMx-2MLKvsHLJY057oqyks0fQ5b7mI577JTX5rBKdEG90O9F5TcoU\&width=768\&dpr=4\&quality=100\&sign=ae0bd75a\&sv=2)

Initialement, DocBits extrait chaque ligne séparément :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FUX5OdkW59HPVROnNzSeZbDw4NYTPbfayDLIXBQi0pwHzUEJ1B5t7I9uKBNc0dmOB3Cile8Xv6AdgVXuUd0aMbQFGWagBCEetw8P-N4zgG_cGTjWHhpDtGQZg27UZKdCDJ5FeEDJgFAYtTB8kZrMSdho\&width=768\&dpr=4\&quality=100\&sign=b6990876\&sv=2)

Vous pouvez ensuite **regrouper les lignes en fonction d'une colonne**, telle que "Position". Cela fusionne les lignes liées en une seule entrée structurée :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FPxA6h2udUuYd1YmHV97t-bzfZzipFpdA5t8gjpGXWx9sA-I4tW3tYwD28icv88UEmitz0EAaWuGkU5ZwqAjcQnoOkmg9u1AcBJW3nITU6eFa0foHB-AQPb0qv0AWaaEwM6WvwaEcAODEUzKtvRZOMN0\&width=768\&dpr=4\&quality=100\&sign=36b99bc7\&sv=2)

## 2. Sélection manuelle de lignes

Dans certains cas, le texte sur un document est réparti sur plusieurs colonnes dans une seule ligne, ce qui rend difficile l'attribution automatique.

Voici un exemple où la ligne "PRAEF" chevauche **Bezeichnung**, **Menge**, **ME**, et **Preis in EUR** :

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FLbVbmfdOBpeCWDftPvW0qjEHjbLmWYRrAGTZHVW8VEHQTEvl5GoqH2wkFE5iUOySmF50b1V8CDAZhfMzPTeMQscmc61SDKaqSCW-y0Z7fjlwOjhtjxWD44oCsgHmwrgrBD4cuEGgn9JY_UX3t9jRlPs\&width=768\&dpr=4\&quality=100\&sign=5ff4a2e1\&sv=2)

### Comment attribuer manuellement des valeurs :

1.  **Activer le mode d'entraînement**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4D8iCXk0p_Mur8bX_11ne_2iA-GOxoFi2OQWlSEvrH1auoE0ksnYXpZx3Pw3PUJJRZJN85dnQlSSBB369FfafXAy8adjFZcnepQnODSaaIj69cxtUKFAXPgn5eyPE6jbJuzStJALMgumlt49Z1Pv3FY\&width=768\&dpr=4\&quality=100\&sign=232c58a9\&sv=2)
2.  **Activer le mode d'édition de ligne**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8YQmo_WRuKKVjk1a_eoxSBiQr0GncuS4BmCA0aI9aOlrbsIvdj8dZlurxxBHp2lH4ozT4HPWw9qYDW7xLQ7u2DSyU8DrNzSBC7LjzKLTDJ2tudY9a_DENDoK5Aya6L1hcf1WF1RD92S_DzhGVV4Gh6Q\&width=768\&dpr=4\&quality=100\&sign=8fc5c089\&sv=2)
3.  **Sélectionner et mapper le texte** Cliquez sur la partie de texte correcte et attribuez-la à un en-tête de colonne **bleu**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fi2tlbwl9qFE0clthaoRPe7kcPRiURCvemuLEjBK4uAnfsR4auXbftMfEY1ZW5WXwezTBVSG5hbNRkddwIeLtrgJUvZoeKGdPKN8f75O_dPdIWkm4EFALfAj-evDUI3UKrgNOTNjF37C1bBLtE95OA1w\&width=768\&dpr=4\&quality=100\&sign=842a42\&sv=2)

> Remarque : Les colonnes de couleur violette sont déjà mappées par le système et ne peuvent pas être modifiées manuellement.

## 3. Mappage des colonnes

Le mappage des colonnes relie vos données extraites aux en-têtes de colonnes attendus, garantissant ainsi la cohérence et l'exportabilité.

Pour mapper ou remapper une colonne :

1. Cliquez sur l'en-tête de colonne dans la vue d'extraction.
2. Choisissez la colonne cible correcte dans la liste déroulante.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FX_65pCWrI4HMFr_aiA0eoSDp-yIYy49lULzAZaiIgnr0aIowlLSed21MuehkGLs4UIdQousdfhiZi5pnQtpZ0uUn6dxlzii7WPQvov-kN1_Jimsi6U6zowOLxjBzZzZ47kaRhduAVBd_Ya9QQtXTpJ4\&width=768\&dpr=4\&quality=100\&sign=4e2a3bdc\&sv=2)

Vous pouvez ajuster le mappage autant de fois que nécessaire.

## 4. Extraire d'au-dessus / d'en-dessous

Certains documents sont structurés de telle manière que les valeurs de table pertinentes n'apparaissent pas sur la même ligne que les autres données. Dans ces cas, DocBits vous permet de contrôler **d'où les données doivent être extraites** :

* **Extraire d'au-dessus** : Utilisez ceci lorsque la valeur pour la ligne actuelle apparaît **dans la ligne au-dessus**.
* **Extraire d'en-dessous** : Utilisez ceci lorsque la valeur apparaît **dans la ligne en dessous** de la ligne actuelle.

**Où le trouver**

1. Entrez en **Mode d'entraînement**.
2. Cliquez sur les trois points (⋯) sur un en-tête de colonne.
3. Sous l'option **"Extraire de"**, choisissez `Au-dessus` ou `En-dessous` en fonction de la mise en page du document.

## 5. Format de montant

Certaines colonnes, telles que **Quantité** ou **Prix unitaire**, contiennent des valeurs numériques ou de date qui peuvent suivre différentes conventions de formatage en fonction de l'origine ou de la localisation du document. DocBits vous permet de spécifier le format que ces valeurs doivent suivre pour garantir une extraction et une interprétation précises.

**Options de format de montant :**

* Définissez le format de nombre ou de date attendu pour la colonne, tel que US (MM/JJ/AAAA, décimal avec point), Pologne (JJ.MM.AAAA, décimal avec virgule), Allemagne, et autres.
* Cela aide DocBits à analyser et standardiser correctement les valeurs même si le document utilise un format régional différent.

**Où le trouver**

1. Entrez en **Mode d'entraînement**.
2. Cliquez sur les trois points (⋯) sur l'en-tête d'une colonne prise en charge (par exemple, Quantité, Prix unitaire).
3. Sous l'option **Format de montant**, sélectionnez le format souhaité correspondant à la localisation de votre document.

## 6. Amélioration de l'extraction de table avec Regex

## **Ce que cela fait**

Cette fonctionnalité vous permet de définir une regex pour chaque en-tête de table, améliorant la précision de l'extraction et garantissant des résultats corrects.

## **Comment l'utiliser**

1. Ouvrez un document du fournisseur pour lequel vous souhaitez définir une regex.
2.  Accédez à la vue **Extraction de table**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Activez le **Mode d'entraînement**.
4.  Sélectionnez l'en-tête de table que vous souhaitez affiner, puis choisissez **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Une fenêtre contextuelle apparaîtra où vous pouvez entrer et définir votre regex.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Cliquez sur **Valider** pour vérifier la regex, puis sur **Enregistrer les modifications** pour l'appliquer.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Enregistrez la règle et confirmez** pour appliquer les modifications.

## Quand utiliser chaque fonctionnalité

Utilisez ces outils pour augmenter la précision de l'extraction et réduire le travail manuel :

* **Regroupement** : Lorsqu'une description ou toute colonne s'étend sur plusieurs lignes et doit être combinée pour plus de clarté.
* **Sélection manuelle de lignes** : Lorsque les lignes ne sont pas structurées proprement et que des parties du contenu tombent dans les mauvaises colonnes.
* **Mappage des colonnes** : Lorsque les noms de colonnes détectés automatiquement ne correspondent pas à votre structure ou nécessitent un affinement.
* **Règles Regex** : Lorsque les en-têtes de table varient légèrement d'un document à l'autre du même fournisseur ou que l'OCR introduit des incohérences.
