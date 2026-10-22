---
description: "P1 : distinguer affectation, tâche et approbation séquentielle"
---

# P1 : distinguer affectation, tâche et approbation séquentielle

Une **affectation documentaire** définit la responsabilité actuelle. Une **tâche** est un travail distinct. Une **notification** informe. Aucune ne constitue déjà une approbation personnelle. Affecter un groupe ne prouve pas non plus l’accord de chacun de ses membres.

Les cartes séquentielles collectent destinataires et ordre d’approbation. L’exemple utilise A à l’ordre 10 et B à 20. La finalisation examinée commence par la plus petite valeur. Le passage à B suit la décision utilisateur traitée par le circuit d’approbation ; un nœud Wait ne réalise pas ce transfert à lui seul.

Évitez une affectation directe dans la même exécution si vous attendez le premier destinataire séquentiel : la finalisation peut ignorer cette première affectation après une affectation directe du document. Pour les tâches, configurez séparément `task_type`, priorité, destinataire et `send_email`. Désactivez les e-mails pour les exercices.

La recette métier nécessite A→approuver→B→approuver, refus de A, destinataire absent et nouveau déclenchement. Le refus doit empêcher l’export final ; un destinataire non résolu ne doit pas apparaître comme une approbation terminée. Vérifiez séparément responsabilité et tâches. La simulation ne prouve pas un transfert réel entre utilisateurs.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `action_assign_doc_to_user_sequential` · v2

Identité: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identité: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → Approuver → B → Approuver |
| ASSIGN-02 | A → Refuser | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | Chemin de repli |
| ASSIGN-04 | RUN-1 → RUN-2 | vérifier les doublons |
| ASSIGN-05 | direct + sequential | vérifier le premier destinataire |

## Preuves et limites

Paramètres et comportement ont été confrontés au catalogue Dev et au code examiné. Les cas métier constituent une procédure de recette. Aucune approbation personnelle, modification réelle ou livraison n’a été réalisée pour ce chapitre.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
