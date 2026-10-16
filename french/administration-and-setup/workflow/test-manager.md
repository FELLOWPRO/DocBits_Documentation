# Test Manager

Le **Test Manager** vous permet d'enregistrer des **scénarios de test** réutilisables pour vos workflows et de les exécuter ensemble — afin de confirmer qu'un workflow se comporte toujours correctement après une modification. Il fonctionne aussi bien pour les workflows Standard que Avancés.

Ouvrez-le depuis **Workflow Dashboard → Test Manager List**.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Test Manager List avec les scénarios de test, leur statut et Run All Tests"><figcaption><p>La Test Manager List — chaque scénario enregistré affiche un résultat réussite/échec.</p></figcaption></figure>

## Ce qu'est un scénario de test

Un scénario de test capture un workflow, une entrée d'exemple et le **résultat attendu**. Lorsque vous l'exécutez, le Test Manager rejoue le workflow avec cette entrée et compare le résultat à celui que vous attendiez — la ligne devient alors **verte** (réussite) ou **rouge** (échec).

## Travailler avec les scénarios

- **Add Test Scenario** — créez un nouveau scénario à partir d'un workflow et d'un document d'exemple.
- **Run All Tests** — exécutez tous les scénarios d'un seul coup et voyez, en un coup d'œil, quels workflows réussissent toujours.
- **View Details** — ouvrez un scénario pour en inspecter le résultat.

<figure><img src="../../.gitbook/assets/workflow_test_manager_detail.png" alt="Détails d'un scénario de test de workflow avec le statut, la durée d'exécution et les données"><figcaption><p>Détails du scénario — nom, statut, durée d'exécution, ainsi que les données réelles et extraites produites par l'exécution.</p></figcaption></figure>

La vue des détails affiche le nom du scénario et son **statut**, le **nom du workflow**, la **durée d'exécution**, ainsi que les **données réelles** et **données extraites** produites par l'exécution — pour que vous puissiez voir précisément pourquoi un scénario a réussi ou échoué.

## Test Manager comparé aux tests dans le générateur

Ce sont deux choses différentes :

- **Test Manager** (cette page) — des scénarios *enregistrés et reproductibles* avec des résultats attendus, exécutés ensemble grâce à **Run All Tests**. Utilisez-le pour les tests de régression après des modifications.
- **Les tests dans le générateur** — les contrôles intégrés **Validate** et **Test** à l'intérieur du générateur Advanced Workflow, pour des vérifications rapides pendant que vous construisez. Voir [Validation et tests](advanced-workflow/validation-and-testing.md).
