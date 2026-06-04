# Validation & Test

Avant de vous fier à un Workflow Avancé, utilisez les commandes de la barre d'outils pour confirmer qu'il est correct et se comporte comme prévu.

## Validate

Cliquez sur la commande **Validate** (l'icône cercle avec coche, ou appuyez sur <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validation vérifie le graphe à la recherche de problèmes — nœuds non connectés, configuration manquante et connexions invalides — afin que vous puissiez les corriger avant que le workflow ne s'exécute sur des documents réels.

## Test

Cliquez sur la commande **Test** (l'icône lecture, ou appuyez sur <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) pour exécuter le workflow sur un échantillon et voir son comportement, sans affecter les documents en production.

## Scénarios de test

Pour des vérifications répétables, enregistrez des **scénarios de test** dans le **Test Manager** (voir le [Tableau de bord](../workflow-dashboard.md)). Chaque scénario enregistre un résultat attendu et affiche un résultat réussi/échoué, et **Run All Tests** les ré-exécute ensemble — vous pouvez ainsi confirmer que vos workflows se comportent toujours correctement après une modification.

<figure><img src="../../../.gitbook/assets/workflow_test_manager.png" alt="Liste du Test Manager des workflows avec des scénarios de test et Run All Tests"><figcaption><p>Le Test Manager — scénarios enregistrés avec résultats réussi/échoué et <strong>Run All Tests</strong>.</p></figcaption></figure>

## Étapes suivantes

- Passez en revue les types de nœuds et les connexions dans [Nœuds](nodes.md).
- Découvrez toutes les commandes de la barre d'outils et du canevas dans [Barre d'outils & Canevas](toolbar-and-canvas.md).
