# Infrastructure

La page **Infrastructure** offre aux administrateurs une vue en temps réel de l'endroit où s'exécute chaque partie de DocBits (UE ou États-Unis), de la manière dont un document circule dans le système et de la bonne santé du traitement en arrière-plan. Elle est en lecture seule — rien ne s'y configure ; elle répond à la question : *« est-ce que tout fonctionne, et mes données restent-elles dans ma région ? »*

> **Accès :** Infrastructure est une page réservée aux administrateurs. Ouvrez **Paramètres → Organisation et Accès → Infrastructure**.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Page Infrastructure avec l'onglet Topologie ouvert"><figcaption><p>La page Infrastructure, onglet Topologie</p></figcaption></figure>

La page est divisée en trois onglets :

| Onglet | Répond à |
|--------|----------|
| **Topologie** | Où s'exécute chaque composant, et tout est-il dans ma région ? |
| **Traitement** | Les étapes de traitement (OCR, extraction, rapprochement de PO …) s'exécutent-elles et sont-elles à jour ? |
| **Tâches planifiées** | Les tâches récurrentes en arrière-plan s'exécutent-elles comme prévu ? |

## Topologie

L'onglet Topologie représente l'ensemble de la plateforme DocBits sous forme de diagramme, organisé en couches — **Edge / Web**, **Core API**, **Import**, **Services en arrière-plan**, **Magasins de données** et **Authentification**. Chaque case est un composant (l'application Web/CDN, la passerelle d'API, le worker OCR, la base de données, etc.).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Diagramme de topologie avec badges de région"><figcaption><p>Chaque composant est étiqueté avec la région dans laquelle il s'exécute</p></figcaption></figure>

### Transparence de la région

Chaque composant porte un badge de région afin que vous puissiez confirmer la résidence de vos données d'un coup d'œil :

| Badge | Signification |
|-------|---------------|
| **UE ✓** / **US ✓** | Le composant s'exécute dans la région de votre organisation. |
| **SHARED** | Un composant global (par ex. le CDN) sans région unique — c'est attendu et ne pose pas de problème. |
| **Région divergente** | Le composant s'exécute dans une région *différente* de celle de votre organisation. Il est mis en évidence afin que vous puissiez le signaler au support. |

La bannière en haut résume le résultat : **« Tous les composants s'exécutent dans votre région (UE) »** lorsque tout correspond, ou un avertissement si un composant critique se trouve dans une autre région.

### Architecture vs. Lire le processus

Utilisez le commutateur au-dessus du diagramme pour changer de vue :

- **Architecture** — la carte statique de tous les composants et de leurs connexions.
- **Lire le processus** — anime le parcours d'un document dans le système, étape par étape, afin que vous voyiez l'ordre dans lequel les composants interviennent.

L'indicateur **● live** montre que les informations d'état du diagramme reflètent l'état actuel du système.

### Modules optionnels

Les composants appartenant à un module optionnel (Recherche plein texte, DocFlow, Auto-Accounting, DocNet, Rapprochement de PO) affichent un badge **activé** ou **désactivé**. Cliquer sur un module désactivé vous amène directement à la page où l'activer — **Paramètres → Module** pour la plupart des modules, ou **Types de document** pour le Rapprochement de PO (qui s'active par type de document).

## Traitement

L'onglet Traitement affiche le pipeline de traitement des documents de **votre organisation** — quand chaque étape s'est exécutée pour la dernière fois et si le travail circule ou s'accumule.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Tableau de traitement avec badges d'état"><figcaption><p>État de traitement par étape pour votre organisation</p></figcaption></figure>

| Colonne | Description |
|---------|-------------|
| **Processus** | L'étape de traitement — Traitement des documents, OCR, TR-OCR, Découpage par code-barres, Extraction de code-barres, Extraction, Rapprochement de PO. |
| **Dernière exécution** | Depuis combien de temps l'étape s'est exécutée. Survolez pour l'horodatage exact. *« Jamais exécuté »* signifie qu'aucun document n'a encore atteint cette étape. |
| **État** | Un badge de type feu tricolore (voir ci-dessous). |

Badges d'état :

| Badge | Signification |
|-------|---------------|
| **OK** (vert) | Aucune erreur récente et rien en attente — l'étape est saine. |
| **En cours (N)** (orange) | `N` documents sont actuellement traités par cette étape. |
| **Erreur (N)** (rouge) | `N` documents ont récemment échoué à cette étape. |

Les erreurs et *en cours* sont des signaux indépendants ; une étape peut donc afficher les deux badges à la fois — vous voyez ainsi un échec même pendant que d'autres traitements se poursuivent. Utilisez **Actualiser** (en haut à droite) pour récupérer les derniers chiffres.

## Tâches planifiées

L'onglet Tâches planifiées répertorie les tâches récurrentes en arrière-plan qui font tourner DocBits (rafraîchissements de cache, alertes d'état, expirations de documents, synchronisations sortantes, etc.) et confirme que chacune se déclenche à l'heure.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Tableau des tâches planifiées"><figcaption><p>Tâches récurrentes en arrière-plan et leur état de planification</p></figcaption></figure>

| Colonne | Description |
|---------|-------------|
| **Tâche** | Le nom de la tâche planifiée. |
| **Dernière exécution** | Depuis combien de temps elle s'est exécutée. Survolez pour l'horodatage exact ; *« Jamais exécuté »* signifie qu'elle ne s'est pas encore déclenchée. |
| **État** | État de planification (voir ci-dessous). |

Valeurs d'état :

| Badge | Signification |
|-------|---------------|
| **À l'heure** (vert) | La tâche s'exécute à l'intervalle prévu. |
| **En retard** (rouge) | La tâche ne s'est pas exécutée comme prévu — à examiner ou à signaler au support. |
| **Inconnu** (gris) | L'état de planification n'a pas pu être déterminé. |

Utilisez **Actualiser** pour revérifier l'état de planification à la demande.
