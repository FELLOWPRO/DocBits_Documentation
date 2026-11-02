---
description: "P1 : choisir l’export, les tâches ouvertes et le statut final"
---

# P1 : choisir l’export, les tâches ouvertes et le statut final

**Start Export** utilise la voie d’export configurée. **Export with Export Configuration** exécute une configuration choisie. Sa variante différée la met en attente pour l’export final à la fin de l’exécution courante. Cela ne signifie pas une livraison automatique après de futures approbations humaines.

Les nouvelles versions examinées proposent `status=finished` ou `status=exported` : finished ferme le document ; exported permet de continuer à le modifier. Le choix existe dès v4 pour Start Export et v3 pour les exports configuré et différé. Les versions antérieures utilisent finished. Une option absente utilise aussi finished dans les nouvelles versions ; une valeur invalide est une erreur de configuration.

Avec `ignore_pending_tasks=false`, les tâches ouvertes sont contrôlées. Le service peut donc refuser l’export configuré immédiat. Cette carte ne prouve aucune reprise automatique après clôture ultérieure des tâches. Définissez un nouvel événement et vérifiez un éventuel enregistrement cible avant de renvoyer. Ignorer les tâches ne remplace pas l’approbation.

Reliez l’export à une condition d’approbation explicitement vérifiée. La recette couvre tâche ouverte, terminée, approbation absente, réception par la cible de test et réexécution. Distinguez demande d’export, réception et traitement ERP. Le kit ne contient aucune destination réelle ; ses tests ne prouvent pas de livraison.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `export` · v4

Identité: `757f30ca-ed60-4e04-8131-2779df17f019`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

Identité: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

Identité: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| EXPORT-01 | status=finished | fermé |
| EXPORT-02 | status=exported | modifiable |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | refus possible ; reprise automatique non démontrée |
| EXPORT-04 | action_export_with_config_deferred | mis en attente ≠ reçu |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## Preuves et limites

Paramètres et comportement ont été confrontés au catalogue Dev et au code examiné. Les cas métier constituent une procédure de recette. Aucune approbation personnelle, modification réelle ou livraison n’a été réalisée pour ce chapitre.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
