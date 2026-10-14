# Se connecter via ClickHouse

Ce guide vous explique comment connecter **ClickHouse** à **Power BI Desktop** en utilisant le **pilote ODBC**. Il couvre l'installation du pilote, la configuration ODBC, l'intégration de Power BI et la configuration de l'actualisation des données.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Installer le pilote ODBC ClickHouse

* Téléchargez le dernier **pilote ODBC ClickHouse** depuis :
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Exécutez l'installateur et suivez l'assistant de configuration.

### 2. Configurer la source de données ODBC

* Ouvrez **Administrateur de source de données ODBC (64 bits)** via le Panneau de configuration ou la recherche Windows.
* Allez à l'onglet **DSN système** et cliquez sur **Ajouter**.
* Sélectionnez **Pilote ODBC ClickHouse** dans la liste et cliquez sur **Terminer**.
*   Remplissez les champs requis. Vous pouvez trouver les informations nécessaires dans :

    **DocBits** → **Paramètres** → **Traitement de document** → **Module** → **Tableau de bord IA** → **Accès direct à ClickHouse**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNkgb8IJ4dQVRnJ4gpqH0%252Fimage.png%3Falt%3Dmedia%26token%3D27d97e71-dd81-488a-851f-e7d659ad4992\&width=768\&dpr=4\&quality=100\&sign=88a4a589\&sv=2)

    **Champs requis :**

    * **Nom** : Un nom pour la connexion (par exemple, `ClickHouse_Prod`)
    * **Description** : Une brève description pour votre référence (facultatif)
    * **Hôte** : Copiez la valeur de l'hôte depuis DocBits
    * **Port** : Copiez la valeur du port depuis DocBits
    * **Base de données** : Copiez le nom de la base de données depuis DocBits
    * **Nom d'utilisateur** : Copiez le nom d'utilisateur depuis DocBits
    * **Mot de passe** : Copiez le mot de passe depuis DocBits

### 3. Connecter ClickHouse à Power BI

* Ouvrez **Power BI Desktop**.
*   Sélectionnez **Obtenir des données** → **ODBC** → **Connexion**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
*   Dans la liste DSN, sélectionnez votre source configurée (par exemple, `ClickHouse_Prod`).

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgDWq5vmtqfAGAQEY0SAX%252FScreenshot%25202025-05-19%2520163823.png%3Falt%3Dmedia%26token%3D443435ac-82ba-40de-a4d1-17611afebb6a\&width=768\&dpr=4\&quality=100\&sign=c0c7d7ae\&sv=2)
* Cliquez sur **OK**. Entrez à nouveau vos informations d'identification si demandé.

### 4. Charger et transformer les données

* Dans le volet **Navigateur**, parcourez et sélectionnez les tables ou vues à importer.
* Choisissez :
  * **Charger** : pour importer directement
  *   **Transformer les données** : pour ouvrir Power Query pour le façonnage des données

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2lrWi9PduJgVQGHQMmhX%252FScreenshot%25202025-05-19%2520164134.png%3Falt%3Dmedia%26token%3D135c45ad-a7ca-4f01-a2f0-07998397f4d9\&width=768\&dpr=4\&quality=100\&sign=e27f4d93\&sv=2)

### 5. Visualiser vos données

* Utilisez le canevas du rapport pour créer des visualisations.
* Faites glisser des champs, ajoutez des filtres, choisissez des types de graphiques et utilisez des expressions **DAX** si nécessaire.
* Exploitez l'**Éditeur Power Query** pour nettoyer ou pivoter vos données ClickHouse avant de créer des visuels.
* Documentation PowerBI : [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

### 6. Activer l'actualisation planifiée (Optionnel)

**Remarque :** **Nécessite Power BI Pro ou Premium + Gateway**

* Pour maintenir vos rapports synchronisés avec ClickHouse :
* Publiez votre fichier `.pbix` sur **Power BI Service**.
* Installez la **Passerelle Power BI** (mode standard) sur une machine avec accès réseau à ClickHouse.
* Dans Power BI Service :
  * Accédez à votre jeu de données → **Paramètres** → **Actualisation planifiée**
  * Associez votre DSN et fournissez les informations d'identification
* Plus d'informations [ici](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Exemples de tableaux de bord et de vues de données

![](../../.gitbook/assets/example_4.avif)![](../../.gitbook/assets/example_3.avif)![](../../.gitbook/assets/example_2.avif)![](../../.gitbook/assets/example_1.avif)
