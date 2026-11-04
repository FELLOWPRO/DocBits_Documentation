---
description: "P1 : suivre la table de décision jusqu’à l’affectation"
---

# P1 : suivre la table de décision jusqu’à l’affectation

Une table de décision relie des champs d’entrée à des retours typés. L’exemple utilise `cost_center=4711` et `total_amount` : contrôleur A jusqu’à 1000, B au-delà. Créez deux règles sans chevauchement avec des utilisateurs valides de votre organisation de test. Le fichier du kit décrit la configuration ; il ne garantit pas un import dans l’éditeur.

Pour **Decision Table has Returns** v3, activez `store_data=wf_store_data`. La v2 lit plutôt l’option booléenne de stockage. La carte d’affectation nécessite les retours stockés dans la même exécution. Une table exécutée avec succès ne confirme pas encore un utilisateur valide.

Un retour utilisateur peut contenir `output_type=user` et `value=101` ; 101 est synthétique et doit être remplacé par un utilisateur de test existant. Choisissez ensuite **Assign document based on decision table** avec `assignee_type=user`. La v2 examinée de cette action sélectionne le dernier retour correspondant. Plusieurs correspondances n’imposent pas automatiquement l’approbation de tous les utilisateurs.

Testez un, aucun et plusieurs résultats, un mauvais type, un utilisateur invalide et le stockage désactivé. Reliez absence de résultat et erreur d’affectation à un repli explicite. Définissez ordre et politique de correspondance au lieu de transformer un ordre accidentel en règle métier. Vérifiez l’affectation réelle sur le document.

La condition de table de décision appelle réellement le service pour évaluer la table. Le mode test ne garantit pas l’absence de tout effet ; utilisez uniquement vos données de test et examinez les actions concernées.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `condition_decision_tree_data` · v3

Identité: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

Identité: `699912a7-2369-47e0-9092-8d027e13752a`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | aucun résultat / utilisateur invalide / type incorrect | Chemin de repli |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | aucun retour stocké pour affectation |

## Preuves et limites

Paramètres et comportement ont été confrontés au catalogue Dev et au code examiné. Les cas métier constituent une procédure de recette. Aucune approbation personnelle, modification réelle ou livraison n’a été réalisée pour ce chapitre.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
