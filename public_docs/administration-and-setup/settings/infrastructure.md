# Infrastructure

La page **Infrastructure** donne aux administrateurs une vue en temps réel de l'endroit où s'exécute chaque partie de la plateforme (EU ou US) et de la bonne santé du traitement. Elle est en lecture seule : rien ne s'y configure.

> **Access:** Infrastructure est une page réservée aux administrateurs. Ouvrez **Settings → Organization & Access → Infrastructure**.

La page comporte trois onglets. Chacun charge ses données lors de la première ouverture, si bien qu'un aller-retour ne récupère pas tout à nouveau.

| Tab | Answers |
|-----|---------|
| **Topology** | Où s'exécute chaque composant, et comment un document traverse-t-il DocBits ? |
| **Processing** | Les étapes du traitement des documents s'exécutent-elles, et le travail s'accumule-t-il ? |
| **Scheduled Tasks** | Les tâches de fond récurrentes se déclenchent-elles comme prévu ? |

## Topology

**Topology** s'ouvre par défaut. La vue présente la plateforme sous deux formes : **Architecture** et **Process**. Le commutateur situé au-dessus du schéma permet de passer de l'une à l'autre ; l'indicateur à côté affiche **live** tant que la vue diffuse son état.

Une bannière au-dessus du schéma résume le contrôle des régions :

* **Green** : tous les composants s'exécutent dans la région de votre organisation, et la bannière nomme cette région (par exemple **EU**).
* **Red** : un composant marqué comme critique s'exécute hors de la région de votre organisation.
* **Amber** : l'avis nomme des composants situés dans une autre région alors que le contrôle global est satisfait. Il s'agit d'un écart de région, pas d'une panne.

### Vue de l'architecture

La vue de l'architecture représente la plateforme sous forme de voies de cartes de composants, par exemple Edge / Web, Core API, Import, Background Services et Modules. Des flèches montrent les connexions entre les cartes.

Chaque carte affiche le nom du composant, un badge de région et, pour les composants critiques, un point d'état qui passe au vert lorsque le composant répond et affiche sa latence en millisecondes lorsqu'une valeur est remontée.

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | Le composant s'exécute dans la région de votre organisation. |
| **SHARED** | Un composant global tel que le CDN, sans région propre. C'est normal. |
| **EU ⓘ** / **US ⓘ** | Le composant s'exécute dans une autre région et est signalé comme avis. |
| **EU ⚠** / **US ⚠** | Le composant s'exécute dans une autre région et est signalé comme erreur. Signalez-le au support. |
| Badge gris, sans marque | La région de ce composant n'est pas connue. |

### Vue du processus

La vue du processus anime un document unique dans le pipeline : les sources d'entrée **Email**, **FTP** et **Web** convergent vers **API**, puis passent par **OCR**, **Extraction**, **PO matching**, **Auto Accounting** et **Export**. Chaque étape est reliée à une barre de stockage de données avec **Postgres** et le stockage de fichiers. Une légende nomme l'étape en cours d'animation, et le bouton de lecture met l'animation en pause ou la reprend.

PO matching et Auto Accounting sont facultatifs. Lorsque l'un d'eux est désactivé pour votre organisation, son étape apparaît en gris et l'animation l'ignore.

### Modules facultatifs

Les modules facultatifs (Full-Text Search, DocFlow, Auto-Accounting, DocNet et PO Matching) portent un badge **active** ou **inactive** sur leur carte. Un module désactivé propose un bouton **Activate** qui vous mène à la page où l'activer : les réglages Modules pour la plupart des modules, ou **Document Types** pour PO Matching, qui s'active par type de document.

## Processing

L'onglet **Processing** liste les étapes du traitement des documents de votre organisation et indique si le travail circule ou s'accumule.

| Column | Description |
|--------|-------------|
| **Process** | L'étape de traitement : Document Processing, OCR, TR-OCR, Barcode Split, Barcode Extraction, Extraction et PO Match. |
| **Last run** | Depuis combien de temps l'étape s'est exécutée pour la dernière fois. Survolez la cellule pour obtenir l'horodatage exact. **Never run** signifie qu'aucun document n'a encore atteint cette étape. |
| **Status** | Un ou plusieurs badges (voir ci-dessous). |

Les badges d'état sont des signaux indépendants :

* Badge rouge **Errors (N)** : `N` documents ont récemment échoué à cette étape.
* Badge ambre avec un compteur : `N` documents sont en cours de traitement par cette étape en ce moment.
* Badge vert **OK** : aucune erreur récente et rien en attente.

Comme les erreurs et le travail en cours sont comptés séparément, une étape peut afficher les deux à la fois : une panne reste donc visible pendant que d'autres documents s'exécutent encore.

## Scheduled Tasks

L'onglet **Scheduled Tasks** liste les tâches de fond récurrentes qui maintiennent DocBits en fonctionnement, par exemple les rafraîchissements de cache, les alertes d'état, les délais d'expiration des documents et les synchronisations sortantes. Chaque ligne indique si la tâche se déclenche à l'heure.

| Column | Description |
|--------|-------------|
| **Task** | Le nom de la tâche planifiée, les séparateurs étant remplacés par des espaces. |
| **Last run** | Depuis combien de temps elle s'est exécutée pour la dernière fois. Survolez la cellule pour obtenir l'horodatage exact. **Never run** signifie qu'elle ne s'est pas encore déclenchée. |
| **Status** | Santé de la planification (voir ci-dessous). |

| Status | Meaning |
|--------|---------|
| **On schedule** (vert) | La tâche s'exécute à l'intervalle prévu. |
| **Delayed** (rouge) | La tâche ne s'est pas exécutée au moment prévu. Analysez-la ou signalez-la au support. |
| **Unknown** (gris) | L'état de la planification n'a pas pu être déterminé. |

Les deux tableaux disposent d'un bouton **Refresh** qui recharge les chiffres actuels à la demande.
