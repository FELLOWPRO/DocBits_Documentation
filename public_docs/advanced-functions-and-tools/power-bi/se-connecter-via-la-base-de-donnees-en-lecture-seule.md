# Se connecter via la base de données en lecture seule

Ce guide vous explique comment connecter la **base de données en lecture seule de DocBits à Power BI Desktop** en utilisant le **pilote ODBC PostgreSQL**. Il couvre l'installation du pilote, la configuration ODBC, l'intégration de Power BI et l'actualisation planifiée.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Installer le pilote ODBC PostgreSQL

* Téléchargez le dernier pilote ODBC PostgreSQL (**psqlODBC**) depuis le site officiel :
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Exécutez l'installateur et suivez l'assistant de configuration.

### 2. Configurer la source de données ODBC

* Ouvrez **Administrateur de source de données ODBC (64 bits)** via le Panneau de configuration ou la recherche Windows.
* Allez dans l'onglet **DSN système** et cliquez sur **Ajouter**.
* Sélectionnez le pilote **PostgreSQL Unicode(x64)** dans la liste et cliquez sur **Terminer**.
* Remplissez les champs requis avec les informations d'identification de : **DocBits → Paramètres → Traitement de document → Module → Tableau de bord IA → Accès à la base de données en lecture seule**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FupCHowPUuMJ8hO9Y36EY%252Fconnect_read_only_4.png%3Falt%3Dmedia%26token%3D3eb69744-6696-41e2-90be-63295b9b6f6d\&width=768\&dpr=4\&quality=100\&sign=647db68c\&sv=2)

**Champs requis :**

* **Nom :** Un nom pour la connexion (par exemple, `Sandbox-Read_Only`)
* **Serveur :** Copiez la valeur de l'hôte depuis DocBits
* **Port :** Copiez la valeur du port depuis DocBits
* **Base de données :** Copiez le nom de la base de données depuis DocBits
* **Nom d'utilisateur :** Copiez le nom d'utilisateur depuis DocBits
* **Mot de passe :** Copiez le mot de passe depuis DocBits
* **Mode SSL :** Défini sur **Requis** (assure une communication chiffrée)

### 3. Connecter la base de données en lecture seule à Power BI

* Ouvrez **Power BI Desktop**.
*   Sélectionnez **Obtenir des données** → **ODBC** → **Connecter**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
* Dans la liste DSN, sélectionnez votre source configurée (par exemple, `Sandbox-Read_Only`).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKPDLjfDw2SRYvzvFKWXq%252Fconnect_read_only_3.png%3Falt%3Dmedia%26token%3Dc67c1362-7f63-479e-a373-974d198f5eb7\&width=768\&dpr=4\&quality=100\&sign=f001e759\&sv=2)

* Cliquez sur **OK**. Renseignez à nouveau les informations d'identification si demandé.
  * **Remarque :** Si vous voyez l'erreur **“l'authentification par mot de passe a échoué pour l'utilisateur”**, essayez d'entrer votre mot de passe entre **accolades** `**{}**`.

### 4. Charger et transformer les données

* Dans le volet **Navigateur**, développez la liste des schémas.
* Ouvrez le schéma `**public**`.
* Sélectionnez les tables que vous souhaitez importer.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSmtEspL1H6ieOJhtDwYb%252Fconnect_read_only_1.png%3Falt%3Dmedia%26token%3Dd402a928-175e-4904-bd21-592ff114fad7\&width=300\&dpr=4\&quality=100\&sign=464e3a3d\&sv=2) ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3Phea1Pf3ZBJtMzw3rxi%252Fconnect_read_only_2.png%3Falt%3Dmedia%26token%3D94037886-57e3-440d-bf08-61cd37c65b98\&width=300\&dpr=4\&quality=100\&sign=5ead9fe9\&sv=2)

* Choisissez :
  * **Charger** → Importez directement dans Power BI
  * **Transformer les données** → Ouvrez Power Query pour le façonnage et le filtrage avant le chargement

### 5. Visualiser vos données

* Utilisez le canevas de rapport Power BI pour construire des tableaux de bord.
* Faites glisser des champs, ajoutez des filtres, choisissez des types de graphiques et appliquez des calculs DAX.
* Utilisez l'**Éditeur Power Query** pour nettoyer ou joindre les données avant de créer des visuels.
* Référence : [Documentation Power BI](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

### 6. Activer l'actualisation planifiée (Optionnel)

**Remarque :** **Nécessite Power BI Pro ou Premium + Gateway**

* Pour maintenir vos rapports synchronisés avec ClickHouse :
* Publiez votre fichier `.pbix` sur **Power BI Service**.
* Installez la **Passerelle Power BI** (mode Standard) sur une machine avec accès réseau à ClickHouse.
* Dans Power BI Service :
  * Accédez à votre jeu de données → **Paramètres** → **Actualisation planifiée**
  * Associez votre DSN et fournissez les informations d'identification
* Plus d'informations [ici](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Exemples de tableaux de bord et de vues de données

![](<../../.gitbook/assets/example_4 (1).avif>)![](<../../.gitbook/assets/example_3 (1).avif>)![](<../../.gitbook/assets/example_2 (1).avif>)![](<../../.gitbook/assets/example_1 (1).avif>)
