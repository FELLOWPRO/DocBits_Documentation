---
description: Monitor workflow performance, manage workflows, and access the Card SDK
---

# Tableau de Bord des Workflows

Le Tableau de Bord des Workflows est votre centre de controle pour la gestion et la surveillance de tous les workflows dans DocBits. Accedez-y en cliquant sur l'icone **Workflows** dans la barre laterale gauche.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Tableau de Bord des Workflows avec les totaux d'exécutions, les taux de réussite et d'échec, le graphique des exécutions et l'activité récente"><figcaption><p>Le Tableau de Bord des Workflows — totaux d'exécutions, taux de réussite/échec et activité récente pour chaque workflow.</p></figcaption></figure>

## Onglet Tableau de Bord

L'onglet Tableau de Bord offre un apercu rapide des performances des workflows pour une periode selectionnee.

### Filtres

- **Date de debut / Date de fin** — Selectionnez la plage de temps pour les statistiques
- **Nom du Workflow** — Filtrez par un workflow specifique ou affichez tous les workflows
- **Comparer** — Comparez deux periodes cote a cote
- **Effacer** — Reinitialiser tous les filtres

### Cartes de Statistiques

| Metrique | Description |
|---|---|
| **Workflows executes aujourd'hui** | Nombre total d'executions de workflows aujourd'hui |
| **Workflows crees (periode)** | Nouveaux workflows crees dans la plage de dates selectionnee |
| **Total des executions** | Executions cumulees de workflows sur la periode |
| **Executions reussies** | Nombre d'executions terminees sans erreurs |
| **Taux de reussite** | Pourcentage d'executions reussies par rapport au total |
| **Taux d'echec** | Pourcentage d'executions echouees par rapport au total |

{% hint style="warning" %}
Un taux d'echec eleve (affiche comme **CRITIQUE** en rouge) indique que les workflows rencontrent des erreurs. Examinez les workflows defaillants en utilisant les journaux d'execution dans le [Constructeur Avance de Workflows](advanced-workflow-builder/).
{% endhint %}

### Graphique des Executions de Workflows

Le graphique affiche une repartition mensuelle des executions de workflows **reussies** (vert) et **echouees** (rouge/rose), vous aidant a identifier les tendances et les pics d'erreurs.

### Activite Recente

- **Derniers Tests de Workflows** — Affiche les executions de tests recentes avec le statut reussite/echec
- **Derniers Workflows** — Affiche les workflows recemment crees ou modifies

## Onglet Liste des Workflows

L'onglet Liste des Workflows affiche tous les workflows avec des fonctionnalites de recherche, de tri et de gestion.

<!-- screenshot: Workflow List showing Advanced workflows with columns -->

### Colonnes

| Colonne | Description |
|---|---|
| **Statut** | Icone a bascule — cliquez pour activer/desactiver un workflow |
| **Nom** | Nom du workflow (cliquez pour ouvrir dans le Constructeur de Workflows) |
| **Type** | Badge affichant `Advanced` pour les workflows visuels |
| **Quand...** | Resume de la condition de declenchement |
| **Mis a jour par** | Utilisateur ayant modifie le workflow en dernier |
| **Cree le** | Date et heure de creation |
| **Mis a jour** | Date et heure de la derniere modification |
| **Actions** | Menu contextuel (supprimer, dupliquer, exporter) |

### Actions

- **Rechercher** — Filtrez les workflows par nom a l'aide de la barre de recherche
- **+ AJOUTER UN WORKFLOW** — Creez un nouveau workflow (ouvre le [Constructeur Avance de Workflows](advanced-workflow-builder/))
- **MODELES** — Parcourez et chargez des modeles de workflows enregistres
- **IMPORTER UN WORKFLOW** — Importez un workflow a partir d'un fichier JSON

## Onglet Liste du Gestionnaire de Tests

La Liste du Gestionnaire de Tests affiche toutes les configurations et resultats de tests de workflows. Utilisez-la pour configurer des scenarios de tests automatises pour vos workflows.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Liste du Gestionnaire de Tests des workflows avec les scénarios de test et Run All Tests"><figcaption><p>La Liste du Gestionnaire de Tests — chaque scénario affiche un résultat réussite/échec ; utilisez <strong>Run All Tests</strong> pour les réexécuter tous.</p></figcaption></figure>

## Onglet Licence

L'onglet Licence affiche le statut actuel de votre licence DocFlow et les fonctionnalites disponibles.

## Onglet SDK de Cartes

L'onglet SDK de Cartes vous permet de creer et de gerer des cartes de workflow personnalisees (cartes partenaires) qui etendent les fonctionnalites integrees de DocFlow.

<!-- screenshot: Card SDK page with Upload ZIP and Submissions tabs -->

### Telecharger un ZIP

Telechargez une application partenaire sous forme de fichier ZIP contenant :
- `app.json` — Metadonnees et configuration de la carte
- `.docflowcompose/flow/` — Fichiers de definition de la carte

Taille maximale du fichier : **10 Mo**. Cliquez sur **Telecharger et Valider** pour soumettre la carte a l'examen.

### Importation GitHub

Importez des cartes partenaires directement depuis un depot GitHub au lieu de telecharger un fichier ZIP.

### Soumissions

Consultez et gerez toutes les cartes partenaires soumises :

<!-- screenshot: Card SDK Submissions list with status badges -->

| Colonne | Description |
|---|---|
| **Nom de la Carte** | Nom de l'application partenaire et de la carte |
| **card_type_label** | Type de carte (`Action_card` ou `Condition_card`) |
| **Version** | Numero de version de la carte |
| **Soumis** | Date de soumission |
| **Statut** | Statut actuel de l'examen |
| **Actions** | Actions disponibles selon le statut |

#### Statuts des Cartes

| Statut | Signification | Actions disponibles |
|---|---|---|
| **Valide** | La carte a passe la validation | Telecharger, Approuver, Rejeter |
| **Approuve** | La carte est active et disponible dans les workflows | Telecharger, Desactiver, Revoquer |
| **Rejete** | La carte a echoue a l'examen | Supprimer |
| **Desactive** | La carte a ete desactivee | Supprimer |

### Telecharger le Modele SDK

Cliquez sur **Telecharger le Modele SDK** pour obtenir un modele de demarrage pour la creation de vos propres cartes personnalisees. Le modele comprend la structure de fichiers requise et des exemples de configurations.

{% hint style="info" %}
Les cartes partenaires peuvent egalement etre gerees de maniere programmatique via les [outils DocFlow MCP](../../../advanced-functions-and-tools/docflow-mcp/). Utilisez les outils MCP du SDK de Cartes pour creer, valider, approuver et tester des cartes depuis votre IDE ou vos scripts d'automatisation.
{% endhint %}
