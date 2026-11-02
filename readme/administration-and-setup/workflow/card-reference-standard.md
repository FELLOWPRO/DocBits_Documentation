---
description: "Configurer les cartes selon leur nom, version, entrées, portée, résultats et effets."
---

# Comprendre et configurer les cartes de workflow

Choisissez une carte selon son opération et sa portée. **Field is** vérifie présence ou état vide ; **Docfield is** compare une valeur. Affectation documentaire, tâche et notification ont des effets distincts. Une catégorie ne remplace pas la référence d’une version précise.

## Contenu d’une référence complète

| Élément | Question à traiter |
| --- | --- |
| Identité | Nom visible, type technique, version et rôle When/And/Then ? |
| Prérequis | Licence, autorisations et données nécessaires ? |
| Entrées | Type, valeur, défaut et choix permis pour chaque paramètre ? |
| Portée | Champ, ligne, toutes les positions ou variable d’organisation ? |
| Résultats | Succès, faux ou erreur ? Qu’utilise la carte suivante ? |
| Effets | Documents, tâches ou systèmes externes modifiés ? Que simule le test ? |
| Exemples | Quelle configuration et entrée complètes produisent quel résultat ? |
| Limites et versions | Données absentes, limites exactes et anciennes versions ? |

## Exemple rempli : Docfield is

**Type technique :** `condition_docfield_operator_value` · **Version :** 2 · **Rôle :** And. Un document avec layout défini et le champ à contrôler est nécessaire.

| Entrée | Configuration |
| --- | --- |
| Field Name | `total_amount`, clé technique et non libellé traduit |
| Operator | `gt` / Supérieur à |
| Field Value | `1000`, sans symbole monétaire |

La carte compare le champ du document actuel à la valeur configurée. Elle ne change pas le statut, ne crée pas de tâche et n’exporte pas. Dans Advanced, vrai suit Success, faux suit Failed Condition et une erreur d’évaluation suit Error. Dans Standard, une condition non satisfaite arrête la séquence linéaire.

Cas effectivement vérifiés : **1785** → Success ; **999** et **1000** → Failed Condition ; **1000,01** → Success ; montant absent ou invalide → Error. JSON utilise un point décimal. Ces résultats décrivent cette configuration numérique, pas tous les types et opérateurs.

Distinguez cette carte des cartes de tolérance explicites. Ne déduisez pas l’égalité ou les opérateurs inclusifs du seul `gt` ; testez la combinaison voulue avec ses propres limites.

## Étapes suivantes

Reliez succès à vérification, faux au traitement standard et erreur à correction des données. Le [cas complet](advanced-workflow-case-study.md) présente configuration, cartes suivantes et résultats réels. Le [modèle d’exécution](workflow-execution-model.md) explique enregistrement et activation ; le [diagnostic](workflow-troubleshooting.md) aide à analyser les écarts.

## WF-05: Exercice et recette

Décrivez Run Workflow et une carte PO selon le même plan : paramètres, valeurs par défaut examinées, chemins, effets et versions. Vérifiez cible inactive, données absentes et base du pourcentage.

[Parcours](workflow-learning-path.md)
