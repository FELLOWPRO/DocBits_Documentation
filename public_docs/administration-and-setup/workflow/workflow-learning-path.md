---
description: "Parcours du débutant à l’expert"
---

# Parcours du débutant à l’expert

Sept niveaux vous mènent du premier regard sur le concepteur de workflows jusqu’à la responsabilité d’une modification sur un workflow en production. Chaque niveau indique un objectif, les étapes à réaliser dans votre propre organisation de test et un résultat que vous pouvez vérifier. Parcourez-les dans l’ordre et construisez chaque exercice vous-même : chaque niveau s’appuie sur la configuration du précédent.

1. [Orientation et modèle d’exécution](#level-1)
2. [Votre première règle](#level-2)
3. [Champs, types et limites](#level-3)
4. [Règles métier et approbations](#level-4)
5. [Contrôle Advanced et sous-workflows](#level-5)
6. [Calcul, intégration et export](#level-6)
7. [Gestion des changements et exploitation experte](#level-7)

## Avant de commencer

* Une organisation de test qui vous appartient, avec une facture synthétique à l’intérieur. Ne vous entraînez jamais sur des documents clients.
* Votre rôle, la licence de workflow et l’habilitation Advanced, vérifiés avant le niveau 1.
* Les exercices importés restent inactifs tant que vous ne les avez pas testés.
* Les jeux de données JSON complets vont dans **Advanced Test → Custom Data**.
* Les approbations et intégrations réelles ont besoin de leurs propres utilisateurs et destinations de test ; un test dans le concepteur ne les remplace pas.

## 1. Orientation et modèle d’exécution <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec sous-titres et transcription en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/fr.html).

**Objectif:** Savoir ce qui déclenche un workflow et ce qu’un résultat de test peut affirmer, ou non, sur une exécution réelle.

1. Vérifiez l’organisation, votre accès, le module workflow et l’habilitation Advanced.
2. Dites When–And–Then avec vos propres mots, puis expliquez où s’arrête une règle linéaire et comment un graphe Advanced suit à la place ses sorties connectées.
3. Distinguez quatre choses qui se ressemblent dans le concepteur : le filtre de type de document, l’événement d’exécution, l’enregistrement et l’activation.

**Critère de fin:** Vous savez dire quand une règle est seulement prise en compte et quelle preuve sépare une simulation d’une exécution sur un document réel.

**Pour aller plus loin:** [Quand mon workflow s’exécute-t-il ?](workflow-execution-model.md) · [Changer le statut sans relancer le workflow](masterclass/status-and-reentry.md)

## 2. Votre première règle <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec sous-titres et transcription en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/fr.html).

**Objectif:** Mener une règle du concepteur jusqu’à un résultat vérifié, sans toucher à un document.

1. Construisez-la dans l’Advanced Builder : When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. Une règle linéaire de cette taille n’a pas besoin de nœud de contrôle.
2. Enregistrez-la, puis vérifiez dans la liste des règles qu’elle est encore inactive, car enregistrer une nouvelle règle peut déjà l’activer. Advanced Test est une surface d’exécution distincte : il évalue le graphe du constructeur, pas la règle activée.
3. Lancez Advanced Test avec des données complètes pour 999, 1000 et 1000.01. Notez pour chaque cas le type de champ, l’opérateur et la sortie retenue, puis ajoutez un cas où le montant manque complètement.

**Critère de fin:** REVIEW n’est atteint qu’avec 1000.01, un montant absent apparaît comme une erreur et non comme un résultat ordinaire sous le seuil, et la règle est de nouveau désactivée à la fin.

**Pour aller plus loin:** [Cas métier Advanced : routage des factures](advanced-workflow-case-study.md) · [Kit d’exercices workflow](workflow-training-kit.md)

## 3. Champs, types et limites <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec sous-titres et transcription en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/fr.html).

**Objectif:** Savoir ce qu’une condition compare réellement avant de faire confiance à son résultat.

1. Testez le contrôle de vacuité sur un champ absent, `null`, un texte vide, des espaces, `false`, `0`, `"0"` et `"false"`, et notez lesquels comptent comme vides.
2. Calculez deux fois la même tolérance de 2 pour cent : une fois avec la commande comme référence (commande 100, document 102.02) et une fois avec le document comme référence.
3. Basculez entre Any et All sur la carte de commande et comptez combien de lignes ont réellement été comparées.

**Critère de fin:** Vous expliquez vrai, faux et erreur à partir de la valeur, du type, de la référence et des données présentes. Dans la version 5 de la carte de commande, un document sans ligne comparable est une erreur de données et non une approbation réussie.

**Pour aller plus loin:** [Field is, Docfield is et comparer deux champs](masterclass/field-conditions.md) · [Rendre les tolérances et la référence de commande non ambiguës](masterclass/tolerances-and-po.md)

## 4. Règles métier et approbations <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec sous-titres et transcription en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/fr.html).

**Objectif:** Envoyer une facture à la bonne personne via une table de décision, puis dérouler une chaîne d’approbation qui attend la première personne qui contrôle.

**Exercice 1 : table de décision avec affectation directe**

1. Créez une table de décision avec deux règles qui ne peuvent pas se déclencher ensemble : contrôleuse A jusqu’à 1000, contrôleur B au-dessus de 1000, avec `cost_center=4711` et `total_amount`.
2. Dans **Decision Table has Returns** version 3, définissez `store_data=wf_store_data`. Affectez le document avec **Assign document based on decision table** et `assignee_type=user`, en utilisant de vrais utilisateurs de votre organisation de test.
3. Testez une correspondance, aucune, plusieurs et un identifiant d’utilisateur invalide, puis envoyez les absences de correspondance et les erreurs d’affectation vers un repli explicite. Acceptez l’affectation sur le document lui-même.

**Exercice 2 : approbation séquentielle sans affectation directe**

1. Créez une deuxième règle distincte avec les cartes séquentielles : la carte d’affectation séquentielle en position 10 pour la contrôleuse A, puis la carte de tâche séquentielle en position 20 pour le contrôleur B. Laissez l’affectation directe hors de cette exécution, car la finalisation vérifiée peut sauter le premier destinataire séquentiel lorsque le document a déjà été affecté directement dans la même exécution.
2. Approuvez en tant que A, puis vérifiez que B ne reçoit le document qu’après la décision de A traitée ; approuvez ensuite en tant que B.
3. Refusez en tant que A dans une nouvelle exécution et confirmez que l’export n’a pas lieu. Testez ensuite ce qui se passe lorsque aucun destinataire ne peut être déterminé.

**Critère de fin:** Vous distinguez responsabilité, tâche, notification et approbation réelle ; A → approbation → B → approbation s’est produit dans cet ordre ; un refus de A a empêché l’export ; et un destinataire manquant n’a pas été compté comme une approbation terminée.

**Pour aller plus loin:** [Suivre la table de décision jusqu’à l’affectation](masterclass/decision-table-routing.md) · [Distinguer affectation, tâche et approbation séquentielle](masterclass/assignment-task-sequential.md)

## 5. Contrôle Advanced et sous-workflows <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec sous-titres et transcription en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/fr.html).

**Objectif:** Réunir correctement des chemins parallèles et transmettre du travail à un autre workflow.

1. Comparez ALL, ANY et OR avec deux contrôles réellement atteints : ALL exige une sortie correspondante de chaque source, ANY et OR en exigent une, et vert plus orange provenant d’une même source comptent toujours pour une seule source.
2. Regardez une branche que l’exécution n’a pas prise, comme dans le cas MERGE-04 : Advanced Test évalue encore la jonction en attente, alors que l’exécution normale la saute dès qu’un prédécesseur n’arrive jamais.
3. Déroulez les sept cas de l’étude de cas v2 (au-dessus, en dessous, limite, juste au-dessus, absent, nombre invalide, autre facture). Appelez ensuite avec Run Workflow l’un de vos propres workflows inactifs et ouvrez le chemin dans la cible elle-même.

**Critère de fin:** Vous expliquez la différence du cas MERGE-04 entre test et exécution de l’étape 2, la façon dont les sources sont comptées et où va une erreur. Un appel Run Workflow au vert exige tout de même une vérification dans la cible. V2 désigne ici la deuxième version du graphe de l’étude de cas : la carte de statut de chaque chemin mène directement à la carte de clôture commune, sans nœud OR en attente.

**Pour aller plus loin:** [Bien connecter Wait ALL, Wait ANY et OR](masterclass/control-nodes.md) · [Comprendre Run Workflow, les conditions de cible et les erreurs](masterclass/run-workflow.md) · [Cas métier Advanced : routage des factures](advanced-workflow-case-study.md)

## 6. Calcul, intégration et export <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec sous-titres et transcription en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/fr.html).

**Objectif:** Calculer des valeurs, récupérer un résultat depuis un système externe et exporter seulement après une approbation réelle.

1. Calculez une colonne et comparez tout le tableau avant et après, y compris une ligne où l’expression régulière ne correspond pas et une division par zéro.
2. Écrivez le contrat de réécriture avec le système externe : quel champ du document reprend le résultat, quelle carte ou extension l’y écrit, et comment vous vérifiez ensuite la valeur enregistrée. Un HTTP 200 seul n’est pas un résultat.
3. Prévoyez l’export après approbation avec votre propre configuration et notez ce que vous allez vérifier chez le destinataire.

**Critère de fin:** Les valeurs suivantes dans le champ, la réception chez le destinataire et le traitement dans l’ERP ont chacun leur propre preuve. Une simulation ou un export mis en file n’est pas une livraison.

**Pour aller plus loin:** [Calculer des tableaux et vérifier la dépendance à la regex](masterclass/table-calculations.md) · [Vérifier l’appel API et la réutilisation de la réponse](masterclass/api-response-contract.md) · [Variantes d’export, tâches ouvertes et statut de clôture](masterclass/export-lifecycle.md)

## 7. Gestion des changements et exploitation experte <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec sous-titres et transcription en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/fr.html).

**Objectif:** Modifier un workflow que vous n’avez pas construit et pouvoir revenir en arrière.

1. Exportez le workflow et notez les versions des cartes avant de toucher à quoi que ce soit.
2. Après la modification, reprenez les cas positifs, négatifs, d’erreur et de limite, plus une deuxième exécution du même cas.
3. Ramenez la première défaillance à une entrée et une configuration précises, et gardez l’export enregistré comme chemin de retour.

**Critère de fin:** Vous savez accepter la modification, restaurer la configuration enregistrée et comparer une nouvelle exécution documentaire avec ses preuves. Notez la cause, la correction et les limites qui subsistent.

**Pour aller plus loin:** [Diagnostiquer méthodiquement les erreurs de workflow](workflow-troubleshooting.md) · [Comprendre les cartes et les configurer de façon fiable](card-reference-standard.md)

## Vérifier ses connaissances

| Question | Réponse |
| --- | --- |
| `false` compte-t-il comme vide dans Field is v2 ? | Oui. Le nombre 0 et le texte "false" ne sont pas vides. |
| Un test OR au vert garantit-il l’exécution documentaire ? | Non. Dans le cas vérifié MERGE-04, un test évalue la jonction qu’une exécution documentaire saute lorsqu’un prédécesseur n’arrive jamais. |
| Run Workflow peut-il appeler une cible inactive ? | Oui, dans l’appel explicite vérifié. Vérifiez tout de même les conditions de la cible et le résultat. |
| Un HTTP 200 expose-t-il automatiquement api.response.cost\_center ? | Non. Les actions vérifiées n’offrent pas ce contrat de sortie JSON automatique. |
| Un test au vert prouve-t-il la réception de l’export ? | Non. L’exécution documentaire, la réception chez le destinataire et le traitement ERP demandent des preuves séparées. |

## Consigner ce que vous avez accepté

Téléchargez `workflow-training-kit-v2.zip` depuis le [kit d’exercices workflow](workflow-training-kit.md), décompressez-le et ouvrez `acceptance-record-template.json`. C’est un registre vierge et non quelque chose à importer ; la même archive contient aussi les données, les attentes et les réponses de test enregistrées auxquelles les niveaux se réfèrent.

Notez ce que vous avez testé et comment vous le savez : le scénario, la configuration (empreinte de l’export du workflow, versions des cartes), ce que vous attendiez, ce que vous avez observé et le type de preuve dont vous disposez. Gardez séparés un test dans Advanced Test, une vérification isolée de la source, une exécution sur document réel, la réception chez le destinataire et le traitement dans l’ERP, et laissez ouverts les étapes que vous n’avez pas testées.
