---
description: "Télécharger facture synthétique, workflow JSON, entrées, attentes et réponses réelles de test."
---

# Kit de formation aux workflows

Utilisez ce kit avec le [cas Advanced](advanced-workflow-case-study.md). Il comprend une facture synthétique, un workflow importable, sept entrées documentaires complètes, des attentes indépendantes et les réponses réelles enregistrées. Les clés techniques et noms des chemins restent identiques dans toutes les langues.

{% file src="../../.gitbook/assets/workflow-training-kit-v2.zip" %}
Kit de formation avec exemples et résultats
{% endfile %}

## Contenu et formats

| Fichier | Utilisation |
| --- | --- |
| `training-invoice.pdf` | Facture synthétique : 1500 EUR nets, 285 EUR de taxe, total 1785 EUR. Aucun paiement à effectuer. |
| `advanced-workflow.json` | Importer désactivé via **Import Workflow** ; aucune variable globale, limité à Facture et au numéro exact de formation. |
| `*-input.json` | Données documentaires complètes pour **Advanced Test → Custom Data**. |
| `expectations.json` | Chemins, messages de statut et résultats attendus ; spécification métier, pas un fichier d’import Test Manager. |
| `*-result.json` | Vraies réponses Dev avec résultats et messages ; références privées d’organisation remplacées. |
| `prepare_inputs.py` | Remplace l’organisation synthétique aux deux endroits nécessaires. |
| `verify_results.py` | Vérifie les réponses selon les attentes indépendantes. Python 3 suffit, aucune clé d’accès requise. |

## Utilisation

1. Décompressez le ZIP et lisez les instructions jointes.
2. Importez le workflow dans votre organisation de test et confirmez sa désactivation.
3. Relevez l’identifiant de votre organisation de test et exécutez localement :

```bash
python3 prepare_inputs.py --org-id YOUR_TEST_ORGANIZATION_UUID --out prepared
python3 verify_results.py
```

4. Utilisez les fichiers de `prepared/` dans le dialogue Advanced. Ne remplacez pas un identifiant synthétique par celui d’une facture client en cours.
5. Vérifiez les sept cas avec le [tableau des résultats](advanced-workflow-case-study.md). Les variations de montant sont intentionnelles ; elles ne modifient pas la facture jointe.

Les données contiennent `id`, `org_id`, `doc_type`, `status` et `extracted_data` avec `layout.groups`, `fields` et `tables`. Les références d’organisation au premier niveau et dans `extracted_data` doivent correspondre au compte connecté. Une valeur dépourvue de définition dans le layout peut ne pas être reconnue comme champ documentaire existant.

## Portée de l’exercice

Les attentes vérifient chemins choisis, texte de routage, messages de statut et nœuds finaux, au-delà du seul statut documentaire. Elles ne correspondent pas à la comparaison de statut d’un scénario Test Manager enregistré.

Un test Advanced réussi confirme le traitement des données fournies. Les actions simulées ne sont pas des affectations, courriels ou livraisons réels. L’activation nécessite une entrée d’événement adaptée et une exécution réelle vérifiée séparément. Voir [Quand mon workflow s’exécute-t-il ?](workflow-execution-model.md).

## WF-03: Exercice et recette

Extrayez v2, adaptez l’organisation avec prepare_inputs.py puis lancez verify_results.py. decision-table-setup.json est une aide de configuration et acceptance-record-template.json un modèle de compte rendu ; aucun n’importe des workflows. Confirmez l’état inactif avant import.

[Parcours](workflow-learning-path.md)
