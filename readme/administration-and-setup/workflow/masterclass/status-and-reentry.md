---
description: "P0 : changer le statut et maîtriser les réexécutions"
---

# P0 : changer le statut et maîtriser les réexécutions

**Change Status to** actualise le statut documentaire. En version 3, `trigger_docflow` détermine si un nouveau traitement des workflows est demandé. Définissez-le explicitement. S’il manque, le code utilise `true` ; les versions 1/2 ne lisent pas ce commutateur dans le même chemin d’exécution. Vérifiez la version enregistrée.

Commencez avec `validated_pending_approval` et `trigger_docflow=false`. Le statut est une option technique : un `pending_approval` inventé ne convient pas. Advanced Test simule la modification. Il ne prouve ni sa persistance ni le traitement d’une nouvelle exécution demandée.

Un processus borné contrôle le statut initial et un marqueur de traitement, effectue l’action puis passe à l’état suivant. Un événement répété ne doit plus satisfaire la condition initiale. Deux exécutions concurrentes peuvent toutefois lire l’ancien marqueur : les tâches et destinations d’export nécessitent une gestion supplémentaire des doublons.

Pour la recette, comparez première et seconde exécutions réelles : statut, traitement ultérieur demandé et nombre de tâches ou d’enregistrements destinataires. N’alternez pas deux statuts pour expérimenter. Modifier le statut ne donne pas une approbation dont la condition métier reste insatisfaite.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `staus_change` · v3

Identité: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | exécution suivante demandée ≠ terminée |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## Preuves et limites

Des résultats sélectionnés de cartes et de nœuds ont été vérifiés avec des données synthétiques dans Advanced Test. Les réponses sont dans le kit. Les actions documentaires sont simulées ; elles ne prouvent ni exécution persistante ni livraison externe.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
