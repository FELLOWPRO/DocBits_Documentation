---
description: "Diagnostiquer les workflows à partir des événements, données, chemins choisis et résultats réels."
---

# Diagnostiquer les problèmes de workflow

Commencez par une exécution affectée. Notez organisation et environnement, nom et révision enregistrée du workflow, référence documentaire, horodatage et fuseau ainsi que le message exact du nœud. Dans les réponses de test, utilisez aussi `execution_id`. Excluez clés d’accès et données client non protégées des preuves partagées.

## Du symptôme à la vérification

| Symptôme | Preuves à chercher | Correction et nouveau test |
| --- | --- | --- |
| Aucune exécution | Licence, module, activation, filtres temporels et événement | Corriger entrée et filtres ; reproduire l’événement réel. Start manuel ne le prouve pas. |
| Action grise | Résultat du prédécesseur et sortie connectée | Suivre le chemin pris. Un nœud ignoré n’a pas lui-même échoué. |
| Condition orange | Clé, type, valeur et opérateur lus | Distinguer résultat négatif et erreur. Tester sous, sur et au-dessus de la limite. |
| Nœud rouge | Premier message d’erreur et données requises | Corriger données ou configuration ; répéter échec et succès. |
| Wait ALL ne continue pas | Chaque source et sa sortie connectée | Ne pas exiger ensemble des chemins exclusifs. Démontrer un chemin possible pour chaque source nécessaire. |
| Tâches ou exports en double | Répétitions, événements, statuts et appels Run Workflow | Limiter conditions et transitions ; tester deux passages. Examiner une protection adaptée contre les traitements concurrents chez le destinataire. |
| Variable affectant d’autres workflows | Variable d’organisation partagée | Examiner les dépendances. La persistance est indépendante du canevas ; retester les workflows concernés. |
| Test réussi sans effet | Ce qui a été comparé ou simulé | Vérifier affectation sur le document, tâche dans son espace et réception à destination. Le statut seul ne suffit pas. |
| Export lancé sans réception | Historique, réponse et données du destinataire | Diagnostiquer avant de répéter ; vérifier si la première requête a déjà été traitée. |

## Interpréter les messages

Dans l’[exemple Advanced](advanced-workflow-case-study.md), un montant absent suit rouge vers la correction. Le traitement et OR peuvent réussir tandis que l’ensemble conserve l’erreur initiale. Une condition normalement fausse suit orange et peut terminer avec succès sur le chemin standard.

Deux connexions issues de la même source ne sont pas deux approbations indépendantes. Les jonctions évaluent les résultats connectés des sources. Examinez le flux complet : un test partiel depuis un nœud intermédiaire peut omettre des prédécesseurs requis.

## Démontrer la correction

1. Conserver le constat original et l’attente métier.
2. Modifier précisément données ou configuration. Changer l’attente uniquement si l’exigence change.
3. Répéter échec, cas positif et limites concernées avec le [kit](workflow-training-kit.md).
4. Enregistrer la règle et vérifier son activation séparément.
5. Comparer une nouvelle exécution réelle à l’ancienne. Les anciens journaux décrivent toujours leur révision d’origine.

Consignez cause, correction, résultat démontré et limites restantes. Séparez attente et exécution : une longue durée totale ne désigne pas à elle seule un nœud lent.

## WF-04: Exercice et recette

Commencez par invalid-number. Conservez la première erreur amount et le résultat error. Répétez avec above et comparez les nouvelles preuves. Gardez l’ancien constat ; traiter l’erreur avec succès ne suffit pas.

[Parcours](workflow-learning-path.md)

## Répéter les tests de carte avec un périmètre explicite

Dans le concepteur Dev examiné, répéter un test lancé depuis un nœud sélectionné a basculé vers le graphe complet. Relancez le test du menu contextuel de la carte voulue et vérifiez les nœuds effectivement visités. Un résultat à six nœuds ne prouve pas un test isolé de valeur vide. Le compteur d’actions échouées peut inclure une condition non satisfaite : lisez aussi la sortie choisie, le journal et le résultat global.
