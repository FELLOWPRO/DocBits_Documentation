# WatchDog

WatchDog est un service Windows qui surveille des dossiers, transmet les documents à DocBits et prend en charge les destinations d’exportation configurées. Les connexions, autorisations et méthodes doivent correspondre à votre environnement.

<figure><img src="../../../.gitbook/assets/watchdog-overview-fr.svg" alt="WatchDog : surveillance des dossiers, traitement dans DocBits et destinations d’export."><figcaption><p>WatchDog : surveillance des dossiers, traitement dans DocBits et destinations d’export.</p></figcaption></figure>

## Démarrage rapide

### 1. Télécharger et préparer

Ouvrez **Paramètres → WatchDog → Général**. Utilisez le téléchargement et les instructions adaptés à votre environnement. Une version Dev illustrée n’est pas une recommandation de déploiement pour tous les environnements.

<figure><img src="../../../.gitbook/assets/site-complete-watchdog-general-safe-fr.png" alt="Vue Général avec les quatre onglets actuels et l’état Hors ligne de l’environnement de test. La clé API, les commandes sensibles et le chemin d’installation sont masqués. Cette image ne prouve pas une installation ou une connexion réussie."><figcaption><p>Vue Général avec les quatre onglets actuels et l’état Hors ligne de l’environnement de test. La clé API, les commandes sensibles et le chemin d’installation sont masqués. Cette image ne prouve pas une installation ou une connexion réussie.</p></figcaption></figure>

### 2. Configurer la clé API

Dans un terminal administrateur, utilisez la clé autorisée de votre organisation et de votre environnement. Remplacez le marqueur d’exemple ; ne publiez pas une commande contenant une véritable clé.

```powershell
WatchDog.exe -api YOUR_API_KEY
```

### 3. Installer et démarrer le service Windows

```powershell
WatchDog.exe install
WatchDog.exe start
```

### 4. Créer les configurations

Dans **Configurations**, préparez les importations et les exportations. Les importations définissent les dossiers et le périmètre des documents ; les exportations définissent leur méthode et leur destination. Le type de document (`doc_type`) est obligatoire pour une configuration d’exportation.

La vue actuelle comprend **Général**, **Configurations**, **Journaux** et **Modèles XSLT**. Le statut du service figure dans Général ; les exportations ne constituent pas un onglet supplémentaire.

### 5. Définir le démarrage automatique

Si votre installation doit démarrer avec Windows, ouvrez `services.msc`, sélectionnez le service WatchDog et configurez le type de démarrage adapté. Vérifiez ensuite l’état, la communication récente et les journaux. La capture Hors ligne ne prouve pas une installation réussie.

## Référence des commandes

| Commande | Description |
| :--- | :--- |
| `WatchDog.exe -api KEY` | Configure la clé d'API et se connecte à DocBits |
| `WatchDog.exe install` | Installe en tant que service Windows |
| `WatchDog.exe start` | Démarre le service |
| `WatchDog.exe stop` | Arrête le service |
| `WatchDog.exe debug` | Exécute en mode console pour le dépannage |
| `WatchDog.exe --version` | Affiche la version actuelle |
| `WatchDog.exe --list-folders` | Liste les dossiers surveillés configurés |
| `WatchDog.exe remove` | Désinstalle le service |



## Ressources complémentaires

* [Installation de WatchDog](watchdog-installation.md)
* [Configuration de WatchDog](watchdog-v2-configuration.md)
* [FAQ administrateur et dépannage](watchdog-admin-faq.md)
