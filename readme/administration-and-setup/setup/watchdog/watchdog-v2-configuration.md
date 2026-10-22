# Configuration de WatchDog

Ce guide explique comment configurer le service WatchDog dans l'application DocBits. Toutes les configurations sont gérées directement dans **Settings → Document Processing → WatchDog**.

<figure><img src="../../../.gitbook/assets/watchdog-v2-config-infographic.svg" alt="Aperçu de la configuration de WatchDog"><figcaption></figcaption></figure>

---

## 1. Onglet General

L'onglet General fournit les instructions d'installation, les liens de téléchargement et les paramètres de mise à jour.

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Onglet General de WatchDog"><figcaption></figcaption></figure>

### 1.1 Téléchargement et configuration

* Téléchargez la dernière version de `WatchDog.exe` directement depuis l'onglet General
* Copiez l'API Key affichée
* Exécutez la commande de configuration dans une invite de commandes administrateur :

```powershell
WatchDog.exe -api YOUR_API_KEY
```

### 1.2 Calendrier de mise à jour automatique

| Option | Intervalle |
| :--- | :--- |
| On Startup Only | Vérification unique au démarrage |
| Hourly | Toutes les 3600 secondes |
| Daily | Toutes les 86400 secondes |
| Weekly | Toutes les 604800 secondes |

---

## 2. Onglet Configurations

Créez et gérez les configurations d'importation et d'exportation. Toutes les configurations sont créées directement dans DocBits — aucun fichier de configuration local n'est nécessaire.

<figure><img src="../../../.gitbook/assets/watchdog_v2_03.png" alt="Aperçu des configurations WatchDog"><figcaption></figcaption></figure>

### 2.1 Importer les configurations

Définissez les emplacements que WatchDog surveille pour détecter de nouveaux documents.

<figure><img src="../../../.gitbook/assets/watchdog_v2_02.png" alt="Configuration d'importation WatchDog"><figcaption></figcaption></figure>

| Champ | Description |
| :--- | :--- |
| **Name** | Nom d'affichage de cette configuration |
| **Watch Folder** | Répertoire à surveiller pour détecter de nouveaux documents (obligatoire) |
| **Success Folder** | Emplacement où les fichiers sont déplacés après une importation réussie |
| **Document Type** | INVOICE, CREDIT\_NOTE, PURCHASE\_ORDER, etc. |
| **Sub-Organisation** | Facultatif — achemine les documents vers une sous-organisation spécifique |

### 2.2 Configuration d’exportations

Définissez comment et où les documents traités sont exportés.

> **Important :** les configurations d'exportation **exigent désormais un type de document** (`doc_type`). Les configurations sans type de document seront rejetées par le système.

| Champ | Description |
| :--- | :--- |
| **Name** | Nom d'affichage de cette configuration |
| **Document Type** | Obligatoire — INVOICE, CREDIT\_NOTE, etc. |
| **Export Method** | Mode d'exportation des documents (voir ci-dessous) |
| **Export Folder** | Répertoire cible pour les exportations vers un dossier |
| **Execution Order** | Priorité lorsque plusieurs configurations correspondent (par défaut : 1) |
| **XSLT Template** | Facultatif — modèle de transformation XML |

### 2.3 Méthodes d'exportation

| Méthode | Description |
| :--- | :--- |
| **Folder (watcher)** | Exporte le PDF et le XML vers un dossier local |
| **Infor IDM** | Téléverse vers Infor Document Management |
| **Infor BOD** | Envoie un BOD XML vers Infor ERP / M3 |
| **ION API** | Appelle les points de terminaison de l'API Infor ION |
| **GLS840MI** | Traitement par lots M3 (via REST API) |
| **REST API** | Envoie vers une API externe avec authentification ION OAuth |

<figure><img src="../../../.gitbook/assets/watchdog_v2_04.png" alt="Configuration d'exportation WatchDog"><figcaption></figcaption></figure>

### 2.4 Options de traitement

* **Barcode Divider :** divise automatiquement les documents de plusieurs pages à partir des codes-barres
* **DocBits Operator :** active les tâches d'automatisation du navigateur

---

## 3. Onglet Status

Surveillez l'état de santé et l'activité du service WatchDog.

<figure><img src="../../../.gitbook/assets/watchdog_v2_status.png" alt="État du service WatchDog"><figcaption></figcaption></figure>

### Informations d'état

| Champ | Description |
| :--- | :--- |
| **Online/Offline** | État de connexion actuel (seuil de heartbeat de 30 s) |
| **Version** | Version de WatchDog installée |
| **Version First Seen** | Date à laquelle cette version a été signalée pour la première fois |
| **Last Restart** | Horodatage du dernier redémarrage du service |
| **Auto-Update Enabled** | Indique si les mises à jour automatiques sont actives |
| **Latest Version** | Version disponible la plus récente |
| **Latest Version Checked At** | Date de la dernière vérification de la version la plus récente |
| **System Info** | Chemin d'installation, mémoire RAM disponible, espace disque disponible |

### Indicateur d'état

| État | Signification |
| :--- | :--- |
| ✅ **Online** | WatchDog est connecté et actif |
| ⚠️ **Offline** | Aucun heartbeat reçu depuis plus de 30 secondes |
| ❌ **Not Installed** | WatchDog ne s'est jamais connecté à cette organisation |

---

## 4. Onglet Logs

Consultez tous les événements WatchDog stockés dans OpenSearch.

<figure><img src="../../../.gitbook/assets/watchdog_v2_05.png" alt="Journaux de WatchDog"><figcaption></figcaption></figure>

* Filtrez par date, type d'événement ou mots-clés
* Types d'événements : `FILE_IMPORT_STARTED`, `FILE_IMPORT_COMPLETED`, `FILE_IMPORT_FAILED`, `EXPORT_STARTED`, `EXPORT_COMPLETED`, `EXPORT_FAILED`, `FOLDER_VALIDATION_FAILED`, `CONFIG_LOADED`, `SERVICE_RESTART_INITIATED`, `SERVICE_RESTART_COMPLETED`

---

## 5. Onglet XSLT Templates

Gérez les modèles de transformation XSLT utilisés pour les exportations XML.

<figure><img src="../../../.gitbook/assets/watchdog_v2_06.png" alt="Liste des modèles XSLT"><figcaption></figcaption></figure>

* Téléversez et modifiez les modèles XSLT
* **Validation en direct** — testez les modèles sur un XML d'exemple avec analyse des champs
* Associez les modèles aux configurations d'exportation
* Consultez le nombre d'utilisations (quelles configurations utilisent chaque modèle)

<figure><img src="../../../.gitbook/assets/watchdog_v2_07.png" alt="Éditeur de modèles XSLT"><figcaption></figcaption></figure>

---

## 6. Onglet Configuration d’exportations

Vue d'ensemble de toutes les configurations d'exportation actives avec leur état de connexion.

* Surveillez l'horodatage de la dernière connexion réussie
* Gérez les configurations directement dans la liste (modifier, copier, supprimer)
* Copiez en masse des configurations entre sous-organisations
