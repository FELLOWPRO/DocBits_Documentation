# Installation de WatchDog

<figure><img src="../../../.gitbook/assets/watchdog-installation-infographic.svg" alt="Étapes d'installation de WatchDog"><figcaption></figcaption></figure>

> **Recommandé :** utilisez la configuration moderne décrite ci-dessous. Les configurations de WatchDog sont désormais créées directement dans l'application DocBits — aucun fichier de configuration local n'est nécessaire.

## Prérequis

* Windows Server ou Windows 10/11
* Accès administrateur
* Connectivité réseau vers l'API DocBits
* API Touche DocBits (disponible dans Paramètres → WatchDog → onglet Général)

## Étapes d'installation

### 1. Créer les dossiers requis

Créez un répertoire principal et des sous-dossiers pour WatchDog :

```
C:\WatchDog\              ← WatchDog executable
C:\WatchDog\Import\       ← Watch folder for incoming documents
C:\WatchDog\Processed\    ← Success folder for processed documents
C:\WatchDog\Export\        ← Export folder for exported files
```

> **Remarque :** il est recommandé d'utiliser des chemins locaux. Les chemins réseau UNC (par exemple `\\server\share`) sont pris en charge, mais peuvent nécessiter un Polling Observer pour une détection fiable des fichiers.

### 2. Télécharger WatchDog

Téléchargez `WatchDog.exe` depuis l'application DocBits :

**Paramètres → Traitement des documents → WatchDog → onglet Général → Télécharger**

Placez le fichier `WatchDog.exe` téléchargé dans `C:\WatchDog\`.

### 3. Configurer la connexion à l'API

Ouvrez l'**invite de commandes (CMD)** en tant qu'**administrateur** et exécutez :

```powershell
cd C:\WatchDog
WatchDog.exe -api YOUR_API_KEY
```

Cela connecte WatchDog à votre organisation DocBits et récupère automatiquement les configurations.

### 4. Installer en tant que service Windows

```powershell
WatchDog.exe install
```

### 5. Démarrer le service

```powershell
WatchDog.exe start
```

### 6. Créer les configurations dans DocBits

Dans DocBits, accédez à **Settings → Document Processing → WatchDog → onglet Configurations** :

* Cliquez sur **New Import Configuration** pour configurer les dossiers surveillés
* Cliquez sur **New Export Configuration** pour configurer les destinations d'exportation

> **Important :** les configurations d'exportation exigent un **type de document**. Toutes les configurations sont gérées de manière centralisée dans DocBits, et non dans des fichiers de configuration locaux.

### 7. Définir le démarrage automatique

1. Ouvrez **Services** (`Win + R` → `services.msc`)
2. Recherchez **WatchDog** dans la liste des services
3. Double-cliquez pour ouvrir les propriétés
4. Définissez le **Type de démarrage** sur **Automatique (démarrage différé)**
5. Cliquez sur **OK**

## Vérifier l'installation

Après l'installation, vérifiez l'état de WatchDog dans DocBits :

**Settings → WatchDog → onglet General**

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Onglet General de WatchDog — état du service"><figcaption></figcaption></figure>

* ✅ **Online** — WatchDog est connecté et envoie des heartbeats
* La version, le dernier redémarrage et les informations système doivent être visibles

## Référence des commandes

| Commande | Description |
| :--- | :--- |
| `WatchDog.exe -api KEY` | Configurer l'API Key |
| `WatchDog.exe install` | Installer en tant que service Windows |
| `WatchDog.exe start` | Démarrer le service |
| `WatchDog.exe stop` | Arrêter le service |
| `WatchDog.exe debug` | Exécuter en mode console (pour le dépannage) |
| `WatchDog.exe remove` | Désinstaller le service |
| `WatchDog.exe --version` | Afficher la version actuelle |
| `WatchDog.exe --list-folders` | Lister les dossiers surveillés configurés |
| `WatchDog.exe --add-folder PATH` | Ajouter un dossier surveillé |
| `WatchDog.exe --remove-folder PATH` | Supprimer un dossier surveillé |

---

## Ancienne méthode : configuration V1 (obsolète)

La méthode de configuration V1 ci-dessous, qui repose sur des fichiers de configuration locaux, est **obsolète**. Utilisez plutôt la configuration moderne basée sur l'API décrite ci-dessus.

<details>
<summary>Configuration V1 (cliquez pour développer)</summary>

### Configurer WatchDog dans DocBits (V1)

1. **Accéder aux paramètres de WatchDog**
   * Accédez à **Settings → Document Processing → WatchDog**
2. **Paramètres des dossiers**
   * Définissez les chemins : `C:/WatchDog/Read` et `C:/WatchDog/Processed`

   <figure><img src="../../../.gitbook/assets/watchdog_folder_settings.png" alt="Paramètres des dossiers WatchDog"><figcaption></figcaption></figure>

3. **Paramètres généraux**
   * Sélectionnez les types de documents, configurez la destination d'exportation

   <figure><img src="../../../.gitbook/assets/watchdog_general_settings_doctypes.png" alt="Paramètres généraux de WatchDog"><figcaption></figcaption></figure>

4. **Configurations d'exportation**
   * Affiche les exportations configurées pour le traitement sur site (on-premise)

   <figure><img src="../../../.gitbook/assets/watchdog_export_configurations_list.png" alt="Configurations d'exportation de WatchDog"><figcaption></figcaption></figure>

5. **Télécharger la configuration**
   * Téléchargez `watchdog-config.json` et placez-le dans `C:\WatchDog\`

   <figure><img src="../../../.gitbook/assets/watchdog_download_configuration.png" alt="Télécharger la configuration"><figcaption></figcaption></figure>

</details>
