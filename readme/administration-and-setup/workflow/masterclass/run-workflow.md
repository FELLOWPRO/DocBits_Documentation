---
description: "P0 : comprendre Run Workflow, conditions cibles et erreurs"
---

# P0 : comprendre Run Workflow, conditions cibles et erreurs

**Run Workflow** appelle un workflow par son ID et attend son exécution. Le nom ne suffit pas. Le concepteur gère l’ID caché du workflow appelant ; ne le modifiez pas comme paramètre métier. Le document courant est transmis à la cible, dont l’entrée et les conditions sont réévaluées.

L’appel explicite examiné atteint aussi une cible **inactive**. Inactive ne signifie donc pas inaccessible par Run Workflow. Les tests Dev couvrent une cible de formation inactive, un auto-appel et un ID inconnu. Les deux derniers prennent Error. Les limites de récursion et de chaîne intégrées ne remplacent pas les règles bornant les appels répétés.

Distinguez variables d’organisation et champs documentaires des retours propres à une exécution. L’appel ne transmet pas automatiquement tous les retours de table de décision ou HTTP du parent. Convenez des champs nécessaires et vérifiez leurs valeurs réelles dans la carte suivante.

Un appel vert ne confirme pas toutes les conditions métier de la cible : un résultat Advanced sans erreur technique compte comme un appel réussi, y compris éventuellement `failed_condition`. Examinez le chemin choisi et son effet. Traitez explicitement l’erreur dans l’appelant ; évitez A→B→A et les appels répétés à la même cible.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `run_workflow` · v2

Identité: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | appel éventuellement réussi ; vérifier la cible |

## Preuves et limites

Des résultats sélectionnés de cartes et de nœuds ont été vérifiés avec des données synthétiques dans Advanced Test. Les réponses sont dans le kit. Les actions documentaires sont simulées ; elles ne prouvent ni exécution persistante ni livraison externe.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
