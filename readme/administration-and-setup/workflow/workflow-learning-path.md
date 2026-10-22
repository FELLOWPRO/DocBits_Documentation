---
description: "Parcours du débutant à l’expert"
---

# Parcours du débutant à l’expert

Suivez les niveaux dans l’ordre. Lire ne suffit pas : chaque niveau se termine par votre configuration, une attente vérifiable et des preuves. P0 prévient les erreurs fondamentales d’exécution ; P1 approfondit données, décisions métier et intégrations.

1. [Orientation et modèle d’exécution](#level-1)
2. [Votre première règle](#level-2)
3. [Champs, types et limites](#level-3)
4. [Règles métier et approbations](#level-4)
5. [Contrôle Advanced et sous-workflows](#level-5)
6. [Calcul, intégration et export](#level-6)
7. [Gestion des changements et exploitation experte](#level-7)

## Prérequis

Utilisez votre organisation de test et un document synthétique. Contrôlez organisation, rôle, licence workflow et droit Advanced. Gardez les exercices importés inactifs. Les JSON complets servent à Advanced Test → Custom Data. La recette réelle des approbations et intégrations nécessite utilisateurs et destinations de test dédiés.

## 1. Orientation et modèle d’exécution <a id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec les sous-titres français et la transcription](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/fr.html).

**Exercice:** Expliquez organisation, accès, When–And–Then et différence entre règle linéaire et graphe Advanced. Distinguez filtre documentaire, événement, enregistrement et activation.

**Critère de fin:** Vous expliquez quand la règle est prise en compte et quelle preuve distingue simulation et exécution documentaire.

Lire et construire: [Quand mon workflow s’exécute-t-il ?](workflow-execution-model.md) · [P0 : changer le statut et maîtriser les réexécutions](masterclass/status-and-reentry.md).

## 2. Votre première règle <a id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/fr.mp4" %}

[Ouvrir la vidéo avec les sous-titres français et la transcription](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/fr.html).

**Exercice:** Construisez When Invoice → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW. Gardez-la inactive. Testez les données complètes pour 999, 1000 et 1000.01. Aucun nœud de contrôle n’est encore nécessaire.

**Critère de fin:** REVIEW n’est atteint qu’au-dessus de 1000. Notez type, opérateur et sortie choisie. Traitez séparément l’entrée absente.

Lire et construire: [Cas Advanced : acheminement des factures](advanced-workflow-case-study.md) · [Kit de formation aux workflows](workflow-training-kit.md).

## 3. Champs, types et limites <a id="level-3"></a>

**Exercice:** Contrôlez absent, null, texte vide, espaces, false, 0 et nombres textuels. Calculez la tolérance avec référence commande puis document. Comparez une puis toutes les lignes réellement rapprochées.

**Critère de fin:** Expliquez vrai, faux et erreur selon valeur, type, référence et données. Aucune ligne comparable ne vaut pas approbation réussie.

Lire et construire: [P1 : choisir Field is, Docfield is ou Compare two Fields](masterclass/field-conditions.md) · [P1 : préciser la référence des tolérances et comparaisons PO](masterclass/tolerances-and-po.md).

## 4. Règles métier et approbations <a id="level-4"></a>

**Exercice:** Configurez deux règles de montant sans chevauchement. Suivez le retour utilisateur stocké jusqu’à l’affectation. Prévoyez A à l’ordre 10, B à 20, refus et repli.

**Critère de fin:** Distinguez responsabilité, tâche, notification et approbation réelle. Le transfert à B exige une décision de A effectivement traitée.

Lire et construire: [P1 : suivre la table de décision jusqu’à l’affectation](masterclass/decision-table-routing.md) · [P1 : distinguer affectation, tâche et approbation séquentielle](masterclass/assignment-task-sequential.md).

## 5. Contrôle Advanced et sous-workflows <a id="level-5"></a>

**Exercice:** Comparez ALL, ANY et OR avec deux contrôles atteints. Examinez une branche non choisie. Exécutez les sept cas v2 et testez Run Workflow avec votre cible inactive.

**Critère de fin:** Expliquez différence test/ordonnanceur, comptage des sources et erreurs. V2 termine sans OR bloqué ; vérifiez un appel vert sur sa cible.

Lire et construire: [P0 : connecter correctement Wait ALL, Wait ANY et OR](masterclass/control-nodes.md) · [P0 : comprendre Run Workflow, conditions cibles et erreurs](masterclass/run-workflow.md) · [Cas Advanced : acheminement des factures](advanced-workflow-case-study.md).

## 6. Calcul, intégration et export <a id="level-6"></a>

**Exercice:** Comparez tout le tableau avant/après, avec regex sans correspondance et division par zéro. Définissez l’écriture réelle des retours d’intégration. Prévoyez l’export après approbation avec votre configuration de test.

**Critère de fin:** Prouvez séparément valeurs suivantes, réception et traitement ERP. Ne présentez ni simulation ni demande d’export comme livraison.

Lire et construire: [P1 : calculer les colonnes et contrôler les dépendances regex](masterclass/table-calculations.md) · [P1 : vérifier les appels API et l’utilisation des réponses](masterclass/api-response-contract.md) · [P1 : choisir l’export, les tâches ouvertes et le statut final](masterclass/export-lifecycle.md).

## 7. Gestion des changements et exploitation experte <a id="level-7"></a>

**Exercice:** Sauvegardez l’export du workflow et les versions avant modification. Répétez positifs, négatifs, erreurs, limites et seconde exécution. Reliez la première erreur à une entrée et une configuration précises.

**Critère de fin:** Vous validez un changement, restaurez la configuration et comparez une nouvelle exécution et ses effets. Notez cause, correction et limites.

Lire et construire: [Diagnostiquer les problèmes de workflow](workflow-troubleshooting.md) · [Comprendre et configurer les cartes de workflow](card-reference-standard.md).

## Vérifier ses connaissances

| Question | Réponse |
| --- | --- |
| false est-il vide pour Field is v2 ? | Oui ; le nombre 0 et le texte "false" ne le sont pas. |
| Un test OR vert garantit-il l’exécution documentaire ? | Non. Les prédécesseurs non atteints diffèrent entre test et ordonnanceur examiné. |
| Run Workflow peut-il appeler une cible inactive ? | Oui pour l’appel explicite examiné. Contrôlez toujours conditions et résultat de la cible. |
| HTTP 200 expose-t-il automatiquement api.response.cost_center ? | Non. Les actions examinées ne fournissent pas ce contrat automatique de sortie JSON. |
| Un test vert prouve-t-il la réception de l’export ? | Non. Exécution documentaire, réception et traitement ERP exigent des preuves distinctes. |

## Les cinq guides associés

Utilisez tout au long des exercices : modèle d’exécution → cas reproductible → kit → diagnostic → référence des cartes. Ce sont les supports des niveaux, pas cinq tâches supplémentaires non vérifiées.

1. [Quand mon workflow s’exécute-t-il ?](workflow-execution-model.md)
2. [Cas Advanced : acheminement des factures](advanced-workflow-case-study.md)
3. [Kit de formation aux workflows](workflow-training-kit.md)
4. [Diagnostiquer les problèmes de workflow](workflow-troubleshooting.md)
5. [Comprendre et configurer les cartes de workflow](card-reference-standard.md)

## Compte rendu de fin

Utilisez acceptance-record-template.json du kit. Notez scénario, révision, attente, observation et type de preuve. Distinguez test Dev, contrôle isolé du code, exécution documentaire réelle, réception et traitement ERP. Laissez explicitement ouverts les points non vérifiés.
