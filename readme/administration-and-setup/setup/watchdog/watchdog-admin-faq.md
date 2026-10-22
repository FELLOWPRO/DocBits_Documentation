# FAQ administrateur et dépannage de WatchDog

<figure><img src="../../../.gitbook/assets/watchdog-troubleshooting-infographic.svg" alt="Aide-mémoire de dépannage de WatchDog"><figcaption></figcaption></figure>

Cette documentation aide les administrateurs à comprendre les messages d'erreur de WatchDog et à résoudre les problèmes.

**Emplacement dans l'interface :** Paramètres → Traitement des documents → WatchDog

---

## 1. Pages de paramètres de WatchDog (interface)

### 1.1 Onglet General

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Onglet General de WatchDog"><figcaption></figcaption></figure>

* **Download :** télécharger la dernière version de WatchDog.exe
* **API Key :** copier la commande de configuration
* **Auto-Update Schedule :** configurer la fréquence des mises à jour
* **Installation Guide :** instructions d'installation pas à pas

### 1.2 Onglet Configurations

* **Import Configurations :** définir les dossiers surveillés et les types de documents
* **Export Configurations :** définir les destinations et les méthodes d'exportation
* **Bulk Copy :** copier les configurations entre sous-organisations
* **Import/Export :** importer/exporter les configurations au format JSON

> **Important :** les configurations d'exportation **exigent désormais un type de document** (`doc_type`). Les configurations sans type de document valide seront rejetées.

### 1.3 Onglet Status

<figure><img src="../../../.gitbook/assets/watchdog_v2_status.png" alt="État du service WatchDog"><figcaption></figcaption></figure>

* Affiche l'état de connexion de WatchDog en temps réel
* **Nouveaux champs :** `last_restart`, `version_first_seen`, `latest_version_checked_at`
* **Informations système :** chemin d'installation, mémoire RAM disponible, espace disque disponible

### 1.4 Onglet Logs

<figure><img src="../../../.gitbook/assets/watchdog_v2_05.png" alt="Journaux de WatchDog"><figcaption></figcaption></figure>

* Affiche tous les événements WatchDog provenant d'OpenSearch
* Filtrable par type d'événement, période, etc.
* **Types d'événements :**
  * `FILE_IMPORT_STARTED` : l'importation du fichier a démarré
  * `FILE_IMPORT_COMPLETED` : importation réussie
  * `FILE_IMPORT_FAILED` : échec de l'importation
  * `EXPORT_STARTED` : l'exportation a démarré
  * `EXPORT_COMPLETED` : exportation réussie
  * `EXPORT_FAILED` : échec de l'exportation
  * `FOLDER_VALIDATION_FAILED` : dossier inaccessible
  * `CONFIG_LOADED` : configuration chargée
  * `SERVICE_RESTART_INITIATED` : redémarrage du service demandé
  * `SERVICE_RESTART_COMPLETED` : service redémarré

### 1.5 Onglet XSLT Templates

<figure><img src="../../../.gitbook/assets/watchdog_v2_06.png" alt="Liste des modèles XSLT"><figcaption></figcaption></figure>

* Téléverser et gérer les modèles de transformation XSLT
* Validation en direct avec analyse des champs
* Associer les modèles aux configurations d'exportation

---

## 2. Messages d'erreur de validation des dossiers

| Erreur | Signification | Solution |
| :--- | :--- | :--- |
| `not_found` | Le dossier n'existe pas | Créer le dossier ou corriger le chemin |
| `no_read_access` | Aucune autorisation de lecture | Définir les autorisations pour le compte de service WatchDog |
| `no_write_access` | Aucune autorisation d'écriture | Accorder les droits d'écriture au compte de service |
| `not_configured` | Chemin du dossier non configuré | Saisir le chemin dans la configuration |

**Dossiers concernés :**

* **Watch Folder (Import) :** où WatchDog recherche les nouveaux fichiers
* **Success Folder :** où les fichiers importés avec succès sont déplacés
* **Export Folder :** où les fichiers XML/PDF exportés sont écrits

---

## 3. Messages d'erreur d'importation

| Erreur | Signification | Solution |
| :--- | :--- | :--- |
| `file_not_found` | Le fichier a été supprimé avant l'importation | Fournir de nouveau le fichier |
| `invalid_file_type` | Seuls les fichiers PDF sont pris en charge | Retirer les autres types de fichiers |
| `api_not_accessible` | L'API DocBits est inaccessible | Vérifier le réseau/pare-feu, contrôler l'URL de l'API |
| `api_check_failed` | Échec du contrôle d'état de l'API | Vérifier l'API Key et la connexion |
| `upload_failed` | Échec du téléversement vers l'API | Vérifier l'API Key, le réseau et l'état du serveur |

---

## 4. Messages d'erreur d'exportation

| Erreur | Signification | Solution |
| :--- | :--- | :--- |
| `transformation_error` | Échec de la transformation XSLT | Vérifier le modèle XSLT, valider la structure XML |
| `folder_error` | Dossier d'exportation inaccessible | Créer le dossier, vérifier les autorisations |
| `file_write_error` | Le fichier n'a pas pu être écrit | Vérifier l'espace disque, les autorisations et les verrous de fichiers |
| `permission_denied` | Aucune autorisation d'écriture | Définir les autorisations du compte de service |
| `creation_failed` | Le dossier n'a pas pu être créé | Vérifier les autorisations du dossier parent |
| `no_config_match` | Aucune configuration d'exportation correspondante | Créer une configuration d'exportation avec le bon type de document |

> **Remarque :** les configurations d'exportation exigent un `doc_type`. Si vous voyez `no_config_match`, vérifiez qu'une configuration d'exportation active existe pour le type du document.

---

## 5. Configuration désactivée — motifs

Lorsqu'une configuration est désactivée, l'un de ces motifs apparaît :

| Motif de désactivation | Signification |
| :--- | :--- |
| `Watch folder: not_found` | Le dossier d'importation n'existe pas |
| `Watch folder: no_read_access` | Le dossier d'importation n'est pas lisible |
| `Export folder: not_found` | Le dossier d'exportation n'existe pas |
| `Export folder: no_write_access` | Le dossier d'exportation n'est pas accessible en écriture |
| `Success folder: not_found` | Le dossier de succès n'existe pas |
| `Success folder: no_write_access` | Le dossier de succès n'est pas accessible en écriture |

**Réactivation automatique :** WatchDog vérifie régulièrement les dossiers (toutes les 60 secondes). Dès que le dossier est de nouveau accessible, la configuration est réactivée automatiquement.

---

## 6. Dossier d'erreurs (`_error`)

Les fichiers en échec sont déplacés dans le dossier `_error` :

**Emplacement :** `{import_folder}/_error/{error_type}/`

**Format de fichier :** `{original_name}_{YYYYMMDD_HHMMSS}.pdf`

**Fichier annexe :** chaque fichier en échec s'accompagne d'un fichier `.error` contenant :

```
Error Type: transformation_error
Error Message: XSLT template not found
Timestamp: 2026-03-26 08:30:15
Original File: invoice_001.pdf
Original Path: C:\WatchDog\Import\invoice_001.pdf
```

---

## 7. Heartbeat et état de la connexion

WatchDog envoie à DocBits un heartbeat toutes les ~10 secondes avec des informations système :

| Données envoyées | Description |
| :--- | :--- |
| Timestamp | Heure actuelle |
| Version | Version de WatchDog installée |
| Last Restart | Heure du dernier redémarrage du service |
| Auto-Update Enabled | Indique si la mise à jour automatique est active |
| Latest Version | Version disponible la plus récente |
| Installation Path | Emplacement d'installation de WatchDog |
| Free RAM / Disk | Ressources système disponibles |

### État de la connexion

| État | Signification |
| :--- | :--- |
| ✅ **Online** | WatchDog est connecté et actif |
| ⚠️ **Offline** | Aucun heartbeat depuis plus de 30 secondes |
| ❌ **Not Installed** | WatchDog ne s'est jamais connecté |

**Erreurs de heartbeat :**

* `Heartbeat failed - invalid API key` → l'API Key n'est pas valide
* `Heartbeat failed: 401` → échec de l'authentification
* `Heartbeat failed: 5xx` → problème côté serveur

---

## 8. Problèmes courants et solutions

### Problème : WatchDog n'importe pas les fichiers

1. Vérifiez que le service est en cours d'exécution : `services.msc` → WatchDog
2. Consultez les journaux : Settings → WatchDog → onglet Logs
3. Vérifiez les autorisations des dossiers pour le compte de service WatchDog
4. Testez la connexion à l'API : `WatchDog.exe debug` dans CMD
5. Vérifiez que le type de fichier est PDF

### Problème : l'exportation ne fonctionne pas

1. Une configuration d'exportation avec le bon type de document existe-t-elle ?
2. Le type de document correspond-il entre le document et la configuration ?
3. Un modèle XSLT est-il associé (pour l'exportation vers un dossier) ?
4. Le dossier d'exportation est-il accessible en écriture pour le compte de service ?
5. Pour les exportations Infor : les identifiants ION sont-ils correctement configurés ?

### Problème : la configuration est désactivée

1. Le chemin du dossier existe-t-il ?
2. Les autorisations sont-elles définies pour `NT AUTHORITY\LOCAL SERVICE` ou le compte de service ?
3. Le lecteur réseau est-il accessible ? (vérifiez les chemins UNC)
4. WatchDog se réactive automatiquement dès que les dossiers sont de nouveau disponibles

### Problème : la transformation XSLT échoue

1. Le modèle XSLT est-il valide ? (utilisez l'onglet XSLT Templates → Validate)
2. Le modèle correspond-il au type de document ?
3. Vérifiez la structure XML du document
4. L'exportation vers un dossier V3 utilise une transformation côté serveur — vérifiez la connectivité à l'API

### Problème : l'exportation via REST API échoue

1. Les identifiants ION OAuth sont-ils configurés dans la configuration d'exportation ?
2. Le point de terminaison de l'API cible est-il accessible depuis le serveur WatchDog ?
3. Vérifiez que le format de la charge utile correspond aux attentes de l'API cible
4. Examinez la configuration de la chaîne de requêtes pour détecter d'éventuelles erreurs JSONPath

---

## 9. Commandes en ligne de commande

```bash
# Configure API connection
WatchDog.exe -api YOUR_API_KEY

# Install Service
WatchDog.exe install

# Start Service
WatchDog.exe start

# Stop Service
WatchDog.exe stop

# Run in debug mode (console output)
WatchDog.exe debug

# Uninstall Service
WatchDog.exe remove

# Show version
WatchDog.exe --version

# List watch folders
WatchDog.exe --list-folders

# Add/remove watch folder
WatchDog.exe --add-folder "C:\Import\Invoices"
WatchDog.exe --remove-folder "C:\Import\Invoices"

# Check Windows service status
sc query WatchDog
```

---

## 10. Fichiers journaux

**Emplacement :** `C:\WatchDog\logs\{module}\`

**Format des journaux :**
```
INFO  - 2026-03-26 10:00:00 - module_name - Message - function=func_name - line=42
```

**Niveau de journalisation :** DEBUG, INFO, WARNING, ERROR

**Journaux distants :** WatchDog envoie également ses journaux à DocBits (consultables dans l'onglet Logs) et, en option, au service de journalisation cloud Logtail.
