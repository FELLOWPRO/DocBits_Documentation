# WatchDog Installation

<figure><img src="../../.gitbook/assets/watchdog-infographic-fr.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

### Configuration de WatchDog dans DocBits

1. **Accéder aux paramètres de WatchDog**
   * Naviguez vers **Paramètres → Traitement des documents → WatchDog**.
2. **Paramètres du dossier**
   * Définissez les chemins où WatchDog trouve et traite les documents.
   *   Les chemins des dossiers doivent correspondre à ceux créés lors de l'installation :

       * `C:/WatchDog/Read`
       * `C:/WatchDog/Processed`

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG1EFmtSO4AxZjWir401%252Fimage.png%3Falt%3Dmedia%26token%3Dc356e023-8cfb-4f45-b863-b27c5af1d9df\&width=768\&dpr=4\&quality=100\&sign=1b1ae0c4\&sv=2)
   * <mark style="color:red;">**Remarque:**</mark>**&#x20;Il est recommandé d'utiliser des chemins locaux. Ceux-ci doivent correspondre aux dossiers dans l'installation de DocBits**
3. **Paramètres généraux**
   *   Sélectionnez les types de documents à traiter en cochant les cases correspondantes\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZbCt5UHd37PdNZsVItdt%252Fimage.png%3Falt%3Dmedia%26token%3Db3c3f203-0f60-42a0-bd56-ee70c204f5e8\&width=768\&dpr=4\&quality=100\&sign=becd5e31\&sv=2)
   * **Diviseur de code-barres :** Lorsqu'il est activé, permet la division des codes-barres.
   * **Opérateur DocBits :** Lorsqu'il est activé, ouvre un navigateur Chrome en arrière-plan pour l'opérateur DocBits.
   * **Destination d'exportation :** Définit la destination d'exportation.
     * **Infor :** Les documents sont exportés vers Infor.
     * **Dossier d'exportation :** Les documents sont exportés vers un dossier défini qui peut être configuré ci-dessous.
4. **Configurations d'exportation**
   * Affiche toutes les exportations configurées pour **le traitement sur site**.
   *   Montre l'horodatage de la **dernière connexion réussie** pour chaque configuration.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FRvK5qn6EggWJxcSYNP5J%252Fimage.png%3Falt%3Dmedia%26token%3D195b9cc6-c5ac-4ee6-90da-b3ee9696ee30\&width=768\&dpr=4\&quality=100\&sign=3bc11ec5\&sv=2)
5. **Configuration bod\_mapping (Optionnel)**
   * <mark style="color:red;">**Champs requis:**</mark> Avant d'ajouter des mappages de métadonnées personnalisés, vous devez définir les deux valeurs suivantes
     * **`file_name`**
     * **`pdf_path`**
   *   Cliquez sur **Ajouter une ligne** pour définir les mappages de métadonnées.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlzUqcr51kq18OrmYAR8X%252Fimage.png%3Falt%3Dmedia%26token%3D3035122b-f1d3-44cc-bfe6-5230943bd77d\&width=768\&dpr=4\&quality=100\&sign=e98d5a1b\&sv=2)
   * **Valeur :** Spécifie le nom du champ pour les métadonnées.
   * **Chemin :** L'expression XPath pointant vers les données XML qui doivent être assignées au champ.
   * **Icône de corbeille :** Utilisée pour supprimer une ligne spécifique.
6. **Télécharger la configuration**
   * Enregistrez la configuration
   *   Téléchargez la configuration\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZXiz4KB7QpnaqD9XwX3o%252Fimage.png%3Falt%3Dmedia%26token%3D04c9f8dc-7d79-443f-9ce4-6d4214edc98b\&width=768\&dpr=4\&quality=100\&sign=574a4218\&sv=2)

### Guide d'installation de WatchDog

1. **Créer les dossiers requis**
   * Créez un répertoire principal : `C:/WatchDog`
   * À l'intérieur de `C:/WatchDog`, créez les sous-dossiers suivants : **Remarque :** ceux-ci doivent correspondre aux dossiers dans DocBits
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Remarque:**</mark>**&#x20;Il est recommandé d'utiliser des chemins locaux. Ceux-ci doivent correspondre aux dossiers dans la configuration de DocBits**
2. **Télécharger WatchDog**
   * Téléchargez la dernière version de `WatchDog.exe` depuis : [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Placez le fichier `WatchDog.exe` téléchargé dans `C:/WatchDog`.
   * Placez le fichier `watchdog-config.json` téléchargé dans `C:/WatchDog`.
   * Ouvrez le `watchdog-config.json` et changez le **config\_path.**
   * Dans cet exemple :
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **Installer WatchDog**
   * Ouvrez **Invite de commandes (CMD)** avec **droits d'administrateur**.
   * Naviguez vers le dossier WatchDog
   *   Exécutez la commande suivante pour installer WatchDog :

       `WatchDog.exe install`
4. **Démarrer le service WatchDog**
   *   Exécutez la commande suivante dans CMD :

       `WatchDog.exe start`
5. **Définir le type de démarrage**
   * Ouvrez **Services** (Appuyez sur `Win + R`, tapez `services.msc`, et appuyez sur **Entrée**).
   * Localisez **WatchDog** dans la liste des services.
   * Double-cliquez pour ouvrir ses propriétés.
   * Définissez le **Type de démarrage** sur **Automatique (Démarrage différé)**.
   * Cliquez sur **OK**.
