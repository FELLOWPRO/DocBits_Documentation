# AI Workforce

<figure><img src="../../.gitbook/assets/docnet-agents-infographic-en.png" alt="AI Workforce Agents Infographic"><figcaption><p>Le système multi-agents de DocBits pour le traitement autonome des documents</p></figcaption></figure>

## Vue d'ensemble

**AI Workforce** est la couche d'orchestration au sein de DocBits qui transforme le travail entrant en agents IA coordonnés. Au lieu qu'une personne exécute manuellement chaque étape, elle prend une unité de travail entrant — un e-mail, un message de chat dans Microsoft Teams ou Discord, une action manuelle dans l'interface ou un appel API — et la mène à son terme : classer le document, extraire et valider les champs, effectuer le rapprochement avec les commandes d'achat et les données de référence, puis exporter vers l'ERP, avec des humains impliqués là où cela compte.

Voyez-la comme une équipe que vous gérez plutôt qu'un outil que vous manipulez. Chaque élément de travail suit la même structure fixe :

* Un **Orchestrateur** reçoit une **Mission** (une unité de travail), la planifie et la délègue.
* Le plan est décomposé en **Problèmes** (tâches individuelles), chacun traité par un **agent Spécialiste** ou par un **humain**.
* Les Spécialistes rendent compte de leurs résultats, et l'Orchestrateur synthétise le résultat final.

Les _agents_ qui remplissent ces rôles ne sont pas figés : DocBits fournit un **DocBits Orchestrator** prêt à l'emploi ainsi que deux spécialistes par défaut, et vous pouvez créer les vôtres (voir [Agents](./#agents)).

Un déroulement type, de bout en bout : une facture arrive par e-mail → une Mission est créée → l'Orchestrateur la planifie et distribue des Problèmes aux spécialistes (classer, extraire, valider, rapprocher la commande) → une étape sensible s'arrête dans la **Boîte de réception** pour qu'un humain l'approuve → une fois approuvée, le document est exporté et la Mission se termine. Vous suivez l'ensemble depuis le **Tableau de bord**, regroupez les exécutions connexes dans des **Projets**, et intervenez via la **Boîte de réception** et les **Problèmes** dès qu'une décision humaine est requise.

## Comment l'activer

AI Workforce s'active par organisation depuis les paramètres principaux.

1. Allez dans **Paramètres → Modules**.
2. Activez le module **AI Workforce**.
3. Confirmez l'abonnement dans la boîte de dialogue qui apparaît.

Une fois activé, **AI Workforce** apparaît dans la barre de navigation principale et l'espace de travail devient disponible pour votre organisation.

## Tableau de bord

Le **Tableau de bord** est votre vue d'ensemble d'AI Workforce — KPI, graphiques et listes d'activité en un coup d'œil. Vous choisissez les indicateurs affichés.

Pour configurer les indicateurs actifs, ouvrez les **Paramètres** (icône d'engrenage) et utilisez le panneau **Widgets du tableau de bord**. Activez ou désactivez chaque widget puis **Enregistrez** ; votre sélection est stockée comme préférence personnelle, de sorte que chaque utilisateur peut personnaliser sa propre vue.

Les widgets disponibles comprennent :

* **Surveillance de la flotte** — l'état en temps réel de tous vos agents.
* **Cartes KPI** — Problèmes ouverts, Missions actives, Agents activés, Exécutions du jour, Utilisation des jetons et Approbations en attente.
* **Graphiques** — tendance des problèmes au fil du temps, missions par statut, réception des e-mails, problèmes par priorité, exécutions par jour et utilisation des jetons par agent.
* **Listes** — missions actives, activité récente, approbations en attente, vos problèmes ouverts, agents au travail et éléments bloqués.

## Boîte de réception

La **Boîte de réception** est l'endroit où le travail attend une **intervention humaine**. Lorsqu'un agent est sur le point d'exécuter un outil nécessitant une validation, il met la tâche en pause et émet ici une **demande d'approbation**. C'est le principe Human-in-the-Loop (HITL) : l'action ne s'exécute pas tant qu'une personne n'a pas tranché. Le fait qu'un outil donné nécessite une validation dépend du **mode d'approbation** de l'agent et des marqueurs **critique** de ses outils (voir [Paramètres de l'agent](./#agent-settings)).

Chaque élément de la Boîte de réception affiche le titre de la demande, l'agent qui l'a émise et une courte description de ce qui nécessite une décision. Depuis l'élément, vous pouvez :

* **Approuver** — laisser l'agent poursuivre l'action.
* **Rejeter** — arrêter l'action.
* **Commenter / envoyer un message** — donner à l'agent des instructions alternatives avant qu'il ne continue.
* **Ouvrir la mission** — accéder à la mission à laquelle cet élément appartient pour disposer de tout le contexte.

Les éléments restent **En attente** jusqu'à ce que quelqu'un agisse, puis passent à **Résolu** (ou **Ignoré** si l'élément est écarté sans décision — par exemple lorsque sa mission est annulée). L'élément de navigation Boîte de réception affiche un badge indiquant le nombre d'approbations en attente, afin que rien de critique ne soit manqué.

## Missions

Une **Mission** est l'unité de travail de plus haut niveau et l'exécution d'agent qui poursuit un objectif unique. Chaque mission peut impliquer plusieurs tâches et est coordonnée par un **agent Orchestrateur**, qui planifie le travail, le délègue sous forme de Problèmes aux spécialistes, surveille les résultats et synthétise le résultat.

Une mission est créée à partir de sa **source** — E-mail, Chat (Microsoft Teams ou Discord), Mission Control (manuel) ou l'API — et conserve ce contexte tout au long de sa vie. Vous pouvez en démarrer une vous-même depuis **Mission Control** en décrivant en langage naturel ce que vous souhaitez faire ; l'Orchestrateur prend le relais à partir de là.

Les missions passent par les statuts suivants :

| Statut                    | Signification                                                              |
| ------------------------- | ------------------------------------------------------------------------- |
| **Planification**         | L'Orchestrateur analyse la demande et élabore un plan.                     |
| **En cours** _(Active)_   | Les agents spécialistes exécutent les problèmes planifiés.                 |
| **En attente d'approbation** | La mission est en pause, en attente d'une décision humaine dans la Boîte de réception. |
| **Complété**              | Tous les problèmes sont réglés et l'objectif de la mission est atteint.    |

Les missions peuvent également être **En pause** ou **Annulées**. Depuis la vue détaillée d'une mission, vous pouvez suivre sa **progression**, examiner les **problèmes** associés, voir le temps et les jetons consommés, ouvrir la **chronologie** des événements, et **relancer**, **modifier** ou **supprimer** la mission.

## Problèmes

Un **Problème** est une tâche individuelle créée pour atteindre une partie de l'objectif d'une mission — par exemple _importer un document_, _envoyer une réponse à l'expéditeur_ ou _approuver manuellement une étape_. Les problèmes sont traités par des **agents spécialistes** et des **humains**, travaillant ensemble sur la même tâche.

Chaque problème porte le contexte dont son responsable a besoin et suit son propre cycle de vie (À faire / En cours → En révision → Terminé, ou Erreur / Annulé). Les problèmes peuvent être assignés à un agent ou à une personne, se voir attribuer une priorité (Critique, Élevée, Moyenne, Faible), être liés à une mission et faire l'objet de discussions via des commentaires.

Vous pouvez consulter tous les problèmes, les filtrer par statut, priorité, responsable ou mission, les regrouper par statut, priorité ou responsable, et voir **Mes problèmes** — les tâches qui vous sont assignées. Créer un problème manuellement vous permet d'ajouter directement du travail pour un agent ou un collègue au sein d'une mission.

## Projets

Les **Projets** sont des dossiers qui regroupent des **Missions** connexes — par exemple _toutes les factures d'un fournisseur donné au T1_, puis un autre projet pour le _T2_, et ainsi de suite. Ils permettent de garder un grand volume d'exécutions d'agents organisé et facile à retrouver.

Lorsque vous créez un projet, vous lui attribuez :

* un **Nom** — par exemple _« Factures Acme T1 »_ ;
* une **Description** facultative — de quoi traite le projet et le résultat attendu ;
* une **Date d'échéance** facultative — la date jusqu'à laquelle le projet doit rester actif.

Un projet est **Actif** ou **Complété**. Un projet doté d'une date d'échéance **reste actif jusqu'à ce que cette date soit atteinte**, puis se termine automatiquement — ainsi une collection trimestrielle se clôture d'elle-même à la fin du trimestre (la vérification s'exécute une fois par jour). Un projet sans date d'échéance reste actif jusqu'à ce que vous le terminiez vous-même. Vous pouvez également terminer ou rouvrir un projet manuellement à tout moment. Depuis un projet, vous pouvez voir combien de missions il contient et y lier d'autres missions.

## Agents

Les agents sont les travailleurs. Chaque agent possède un **rôle** qui détermine ce qu'il fait dans le flux Orchestrateur → Missions → Problèmes :

* **Orchestrateur** — coordonne le travail entre plusieurs agents. Il reçoit une mission, la planifie, délègue les étapes sous forme de problèmes et synthétise les résultats. Un orchestrateur est requis pour que les missions puissent s'exécuter.
* **Spécialiste** — exécute une tâche précise, comme importer un document ou envoyer une réponse par e-mail, et en rend compte à son orchestrateur.

DocBits fournit AI Workforce prêt à l'emploi, avec ces agents par défaut :

* **DocBits Orchestrator** — l'orchestrateur par défaut.
* **Document Processor** — importe et traite les documents téléversés.
* **Email Reply** — rédige et envoie les réponses à l'expéditeur.

Ce sont des **agents système** : vous pouvez en configurer certaines parties, mais vous ne pouvez pas les supprimer. Vous pouvez aussi créer vos propres orchestrateurs et spécialistes à leurs côtés.

### Règles de hiérarchie et d'activation

Comme un orchestrateur est requis pour exécuter toute mission, l'activation obéit à quelques règles :

* Les **Orchestrateurs** disposent d'un interrupteur **activer/désactiver**, mais un orchestrateur ne peut être **désactivé que s'il existe au moins deux orchestrateurs** — le système ne vous laisse jamais désactiver le dernier, car il ne resterait plus rien pour coordonner les missions.
* Lorsque **plusieurs orchestrateurs sont actifs**, le **System Router** s'active automatiquement. Son rôle est d'examiner chaque mission entrante et de la déléguer au bon orchestrateur. Avec un seul orchestrateur, le routeur est inutile et reste en retrait.
* Les **Spécialistes ne disposent pas d'un interrupteur activer/désactiver.** À la place, vous contrôlez où ils peuvent travailler en les **assignant à des orchestrateurs** (voir _Agent Pool_ ci-dessous). Un spécialiste qui n'est assigné à aucun orchestrateur n'est pas disponible du tout — il reste dans l'annuaire, mais aucun orchestrateur ne peut lui déléguer de travail ; chaque spécialiste doit donc être assigné à au moins un orchestrateur pour être utilisé.

Vous pouvez visualiser et réorganiser ces relations dans l'**Org Chart**, qui présente Router → Orchestrateurs → Spécialistes.

### Paramètres de l'agent

Chaque agent — système ou personnalisé — dispose d'un menu de paramètres comportant les sections suivantes :

* **Prompt** — le prompt système de base de l'agent. _En lecture seule sur les agents système._
* **Paramètres** — le **modèle** de l'agent et son **effort de raisonnement**. AI Workforce fonctionne sur un seul modèle capable de raisonnement (**DocBits Pro**), donc au lieu de réglages de bas niveau, il existe un unique curseur — **Effort de raisonnement** — qui contrôle l'intensité de la réflexion de l'agent (et donc son coût) :
  * **None** — le plus rapide et le moins cher ; aucun raisonnement.
  * **Low** — tâches rapides, raisonnement léger.
  * **Medium** _(par défaut)_ — qualité et coût équilibrés.
  * **High** — raisonnement approfondi pour les tâches plus difficiles ; coût plus élevé.
  * **X-High** — raisonnement maximal ; coût le plus élevé.
* **Mode d'approbation** — la part du travail de l'agent qui nécessite une validation humaine dans la [Boîte de réception](./#inbox) :
  * **None** — l'agent exécute chaque outil automatiquement ; rien n'est envoyé pour approbation.
  * **Critical** _(par défaut)_ — seuls les outils marqués **critique** nécessitent une approbation ; tout le reste s'exécute automatiquement. Les outils critiques sont les actions sensibles, d'écriture ou externes (par exemple _téléverser/importer un document_, _mettre à jour les champs d'un document_, _répondre à un e-mail_, _envoyer une notification_). Dans ce mode, un outil critique émet **toujours** une demande d'approbation dans la Boîte de réception. Vous pouvez affiner des outils individuels (marquer comme nécessitant une approbation un outil normalement sûr, ou retirer ce marquage d'un outil critique) — ces surcharges par outil ne s'appliquent qu'en mode Critical.
  * **All** — chaque outil exécuté par l'agent nécessite une approbation.
*   **Instructions personnalisées** — champ de texte libre où vous décrivez les habitudes de travail de l'agent (modifiable même sur les agents système). Le modèle par défaut ressemble à ceci :

    > **Classification :** utilisez le classificateur de DocBits sur le document téléversé. Ne vous fiez à l'objet/au corps de l'e-mail que lorsqu'aucun document n'est joint.
    >
    > **Surcharges de champs :** aucune — acceptez les valeurs extraites telles quelles.
    >
    > **Approbation :** non configurée. (Pour exiger une approbation humaine pour des actions précises, nommez l'action et le seuil.)
    >
    > **Affectation de projet :** effectuez le rapprochement avec les descriptions de projets ; préférez laisser la mission non assignée plutôt que de forcer une correspondance médiocre. (Pour surcharger, indiquez des mots-clés ou des motifs d'expéditeur : par exemple `supplier@acme.com → Acme Onboarding`.)
* **Compétences** — les outils que l'agent est autorisé à utiliser (par exemple _téléverser des documents_ ou _lister les utilisateurs_). Chaque outil est soit **critique** (actions sensibles d'écriture ou externes), soit non critique, ce qui détermine le comportement d'approbation décrit ci-dessus. _Non modifiable sur les agents système._
* **Agent Pool** — _orchestrateurs uniquement._ Une liste des agents disponibles, où vous sélectionnez les spécialistes auxquels cet orchestrateur peut déléguer du travail. Un spécialiste doit être assigné ici à un orchestrateur (ou à un autre orchestrateur) pour effectuer un travail ; un spécialiste laissé sans affectation partout n'est pas disponible du tout.

### Créer des agents personnalisés

Au-delà des agents par défaut, vous pouvez créer vos propres **orchestrateurs** et **spécialistes** adaptés à vos processus. Ouvrez **Agents → Créer un agent** pour lancer l'assistant, qui vous guide à travers la même configuration décrite ci-dessus : choisissez le **rôle** (Orchestrateur ou Spécialiste), donnez à l'agent un **nom** et une **description** claire (un orchestrateur est choisi à partir de ce texte, et un orchestrateur sélectionne ses spécialistes à partir des leurs), rédigez son prompt, choisissez ses compétences, définissez son effort de raisonnement et — pour les orchestrateurs — sélectionnez les spécialistes de son agent pool. Les agents personnalisés peuvent être entièrement modifiés ou supprimés à tout moment.
