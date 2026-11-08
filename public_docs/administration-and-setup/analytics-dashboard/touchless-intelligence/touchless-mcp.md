# Expliquer et améliorer Touchless avec MCP

<!-- touchless-admin-video-v2-20261104:start -->
**Chapitre vidéo (version de contrôle):** [Interroger les indicateurs avec MCP](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/fr.html#chapter=12).
<!-- touchless-admin-video-v2-20261104:end -->

Les parcours suivants utilisent des outils réellement proposés par DocBits MCP. Distinguez la lecture et l'explication de l'écriture. Vérifiez l'organisation, le rôle, le type de document, la période et l'horodatage des données ; n'inventez pas de preuves manquantes.

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-fr.png" alt="Véritable vue Dev anglaise d'un PO fictif créé pour nous : 10 × 9 = 90. C'est une comparaison de source pour le diagnostic MCP, pas une capture d'un client MCP ni une preuve d'extraction ou de traitement réussi."><figcaption><p>Véritable vue Dev anglaise d'un PO fictif créé pour nous : 10 × 9 = 90. C'est une comparaison de source pour le diagnostic MCP, pas une capture d'un client MCP ni une preuve d'extraction ou de traitement réussi.</p></figcaption></figure>

## Expliquer Touchless avec MCP

> Explique Pure Touchless, les résultats avec approbation seule et le taux AP combiné pour les factures des 30 derniers jours. Indique le numérateur, le dénominateur, les documents en cours et exclus, le périmètre et l'horodatage des données. Garde l'exactitude de l'extraction à part.

Utilisez `touchless_get_summary` avec `period: "30d"` et `doc_type: "INVOICE"`. Pour un sous-processus, utilisez uniquement les champs de segment et les valeurs réellement renvoyés par `touchless_list_segments`. Comparez le tableau de bord et MCP avec la même organisation, le même type de document, le même segment et la même période ; lisez `data_as_of`.

**Contre-exemple Dev vérifié :** trois factures de test nouvellement importées étaient encore `IN_PROGRESS`. Le résumé renvoyait `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0` et `official_touchless_rate.ap_pct: null`. Aucun taux n'était encore mesurable. Ce n'est ni une précision d'extraction de 0 % ni 100 % de Touchless. L'éligibilité du résumé désigne ici la population terminée des indicateurs ; une trace individuelle peut simultanément afficher `eligible: true` et `bucket_final: false`.

Les exemples MCP de ces cinq pages utilisent les outils DocBits MCP directs vérifiés en Dev. L'organisation et le rôle de votre compte connecté s'appliquent ; la disponibilité dans une autre interface ou dans une liste d'autorisation d'outils supplémentaire n'est pas établie par ce test.

## FAQ

**DocBits a tout extrait correctement. Pourquoi la facture est-elle AP assisted ?**
Touchless mesure l'ensemble du processus. Des données Infor incorrectes ou obsolètes peuvent nécessiter une correction enregistrée ou une relance manuelle même avec une extraction correcte. Vérifiez séparément la facture d'origine, les valeurs extraites par DocBits et les données source importées.

**AP assisted indique-t-il si DocBits ou Infor est à l'origine du travail ?**
Non. Il enregistre l'intervention, pas la responsabilité. Utilisez la trace du document et les données du document et de la source sous-jacents pour confirmer la cause.

**Les taux affichent un tiret (—).** Aucun document n'a atteint de résultat final sur la période, ou moins de documents que le minimum ont été mesurés. Les documents encore en cours ne sont pas comptés.

**L'onglet est absent.** Demandez à votre administrateur d'activer le module et d'accorder l'onglet **Analytics dashboard** à votre rôle.

**Un document est compté comme touché, alors qu'il a cette fois été traité sans personne.** Il a été touché lors d'une exécution antérieure (une correction ou une relance). Le taux compte le travail qui a eu lieu.

**Pourquoi le nombre change-t-il après quelques heures ?** L'ERP peut confirmer un export plusieurs heures après son envoi. Le résultat est recalculé toutes les 15 minutes.

**L'IA modifie-t-elle quelque chose de sa propre initiative ?** Non. L'IA n'écrit que des explications. Un paramètre ne change qu'après l'aperçu et l'application par un administrateur.

## Analyser les écarts avec MCP

> Vérifie le numéro de PO de cette facture, l'état de l'import et les règles de correspondance réellement actives. Sépare l'extraction, l'import obsolète, des données source erronées et une configuration manquante. Ne modifie rien pour l'instant.

1. Comparez l'original, `get_extracted_fields` et `get_extracted_tables` avant d'affirmer que l'extraction est correcte.
2. Utilisez `get_po_sync_status` avec `po_number: "TL20261104X1-PO02"` et `language: "en"`. Le test Dev a confirmé un import traité et un PO existant. Cela prouve l'arrivée, pas l'exactitude métier ni l'enregistrement Infor actuel.
3. Utilisez `touchless_get_document_trace` et `touchless_explain_po_match` avec le même `doc_id`. Lisez le moteur réel, la version de règle active, les colonnes et les tolérances effectives. Pour un cluster réellement renvoyé, utilisez son `issue_signature` dans `touchless_get_po_match_evidence`.
4. Conservez les preuves manquantes : notre nouveau type de test a renvoyé `state: "none_published"` et `parse_error: "no published rule set"`, ainsi que des champs d'extraction vides. Aucun blocage de prix ou de quantité ni aucune correspondance réussie n'a été prouvé. Un déroulement de décision générique ne remplace pas ces contrôles manquants.
5. Corrigez la cause confirmée et vérifiez les nouvelles factures. Une correction humaine ou une relance reste pertinente après la réussite ; une défaillance ERP finale prime comme exception, et un document inachevé est hors du dénominateur du taux.

Pour un cas complet, conservez l'original, l'extraction d'avant correction, les valeurs source importées et actuelles avec l'heure d'import, les règles réelles, l'action AP et le résultat final. Une preuve manquante reste ouverte.

## Lire les preuves avec MCP

> Inspecte cette facture sans la modifier. Compare l'original, les champs et les tableaux actuels. Explique les étapes et exécutions enregistrées et identifie les preuves d'extraction historiques manquantes.

| Outil, avec le même `doc_id` | Preuve et limite |
| --- | --- |
| `get_extracted_fields` | Valeurs d'en-tête et confiance actuelles ; pas un instantané historique |
| `get_extracted_tables` | Tableaux et lignes réels ; pas la preuve qu'ils concordent avec l'original |
| `touchless_get_document_trace` | Résultats, interventions, étapes et exécutions enregistrés |
| `touchless_explain_pipeline` | Explication du chemin de traitement attesté ; ne comble pas les preuves manquantes |

**Contrôle négatif observé :** notre facture de test récente avait une étape d'extraction d'en-tête `passed` mais `extracted_field_count: 0`, huit champs obligatoires vides et aucun tableau. La validation des champs a bloqué avec `REQUIRED_FIELD_MISSING`. L'assistant doit rechercher une extraction ou une configuration manquante, au lieu d'affirmer une extraction correcte à partir d'une étape verte ou un blocage de prix de PO prouvé à partir de valeurs source différentes.

### Une action MCP compte-t-elle comme une intervention humaine ?

Une inspection en lecture seule ne modifie pas une facture. D'autres outils MCP peuvent écrire des champs, valider ou relancer. La classification dépend de l'événement enregistré et de la nature humaine ou système de son acteur. Une clé d'API peut agir comme un compte système ; « effectué via MCP » seul ne prouve ni une intervention humaine ni Pure Touchless. N'utilisez jamais d'identifiants système pour masquer une reprise humaine.

Après une action sur un document, inspectez `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, le statut final et les exécutions. Une simple approbation métier diffère d'une correction enregistrée, d'une validation manuelle ou d'une relance humaine.

## Prioriser les fournisseurs et vérifier une amélioration durable avec MCP

> Classe les fournisseurs qui perdent le plus de factures Touchless. Sépare les erreurs d'extraction, les écarts de source importée et les paramètres de processus. Propose une action et un contrôle de réussite vérifiable pour chaque cause confirmée ; ne modifie rien pour l'instant.

1. Utilisez `touchless_rank_supplier_opportunities` avec `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. Utilisez `search` pour un numéro ou un nom de fournisseur ; `limit` et `offset` paginent les résultats.
2. Transmettez le `supplier_key` renvoyé tel quel à `touchless_diagnose_supplier`. Utilisez `window: 30` pour les problèmes actuels ou 90 pour analyser des problèmes récurrents.
3. Transmettez un `issue_signature` réellement renvoyé à `touchless_get_issue_cluster`. Examinez les documents d'exemple et les preuves manquantes avant de confirmer la cause. N'inventez pas d'identifiants.
4. Utilisez `touchless_get_recommendations` pour expliquer une action prise en charge. Le gain attendu est une estimation ; des clusters qui se recouvrent ne doivent pas être simplement additionnés.
5. Vérifiez les nouvelles factures comparables après la correction et la [mesure de la modification](touchless-change-proposals.md). Les factures déjà touchées ne deviennent pas Pure Touchless rétroactivement.

Pour une extraction correcte et des PO obsolètes, corrigez les données source et d'import. Pour un écart entre l'original et l'extraction, examinez la configuration de l'extraction. Une approbation exigée par la politique est un résultat AP Touchless réussi distinct. Un classement vide ne prouve pas l'absence de problèmes : nos trois factures de test en cours n'ont produit aucun résultat fournisseur classé. Vérifiez le périmètre, l'horodatage des données, l'identification du fournisseur et le volume terminé.

## Prévisualiser, appliquer et mesurer avec MCP

> Explique la cause confirmée et liste les propositions prises en charge. Prévisualise la modification choisie, son périmètre et ses risques. Applique uniquement cette modification choisie, puis vérifie le paramètre enregistré, l'historique des modifications et l'effet mesurable.

| Étape | Outil et identifiants réellement renvoyés | Ce que cela prouve |
| --- | --- | --- |
| Lister | `touchless_list_change_proposals`, `issue_signature` facultatif, `window: "30d"`, `lang: "en"` | Propositions disponibles ; aucun paramètre enregistré |
| Prévisualiser | `touchless_preview_change` avec le `proposal_id` renvoyé et l'identifiant `issue_signature` correspondant | Périmètre concret et `preview_token` lié, lorsque c'est permis |
| Appliquer la modification choisie | `touchless_apply_change` avec les mêmes identifiants, `preview_token`, `overrides` et `window` | **Écrit** le paramètre pris en charge ; une réponse réussie renvoie un `change_id` |
| Lire l'effet | `touchless_verify_change` avec ce `change_id` et le même `window` | Mesure avant/après ; au moins 20 documents terminés éligibles par période restent nécessaires |

Copiez les identifiants et jetons depuis de véritables réponses. Un jeton qui prévisualise une valeur ne peut pas en appliquer une autre. Un aperçu expiré, interdit ou incomplet ne prouve pas une modification appliquée. Les outils en lecture seule et l'application ne doivent pas être décrits comme équivalents. Ce tableau explique la séquence d'outils ; il n'affirme pas que la démo a exécuté une proposition ni mesuré un gain.

**Exemple de configuration :** après une correction de configuration confirmée, inspectez la valeur réellement enregistrée et les nouvelles factures. 52 % avant et 61 % après correspondent à un écart observé de 9 points de pourcentage, pas à la preuve que cette seule modification l'a causé. **Exemple de données source :** un PO Infor erroné nécessite une correction métier et un import vérifié. `touchless_apply_change` n'est pas un outil général d'écriture Infor. N'élargissez pas les tolérances pour masquer des données source erronées.

La capture du rapport montre des recommandations et un impact estimé, pas une application ni une annulation. Une application réussie nécessite une réponse de succès et une entrée d'historique. Undo n'est disponible que lorsque la proposition sélectionnée le permet ; vérifiez le paramètre réellement restauré. Recharger l'historique n'applique pas de paramètre, et une annulation ne supprime pas les interventions passées sur les documents.

## Pages associées

* [Touchless Intelligence](./)
* [Indicateurs et calcul](touchless-metrics.md)
* [Utiliser le tableau de bord](touchless-dashboard.md)
* [Exemples pratiques : prix et quantité](touchless-examples.md)
* [Diagnostic fournisseur et clusters de problèmes](touchless-supplier-diagnosis.md)
* [Diagnostic du rapprochement avec le BC](touchless-po-matching-diagnosis.md)
* [Trace du document](touchless-document-trace.md)
* [Propositions de modification et rapports](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
