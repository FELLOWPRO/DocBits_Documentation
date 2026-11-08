# Diagnostic fournisseur et clusters de problèmes

<!-- touchless-admin-video-v2-20261104:start -->
**Chapitre vidéo (version de contrôle):** [Analyser des problèmes récurrents](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/fr.html#chapter=06).
<!-- touchless-admin-video-v2-20261104:end -->

Cliquez sur un fournisseur dans la file d'attente pour ouvrir sa page de diagnostic.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-supplier-detail.png" alt="La page Supplier Diagnosis avec les tuiles de résultat, la tendance et deux clusters de problèmes"><figcaption><p>La page Supplier Diagnosis : tuiles de résultat, tendance avec sélecteur de période et deux clusters de problèmes classés par gain attendu. Organisation d'exemple avec des données de démonstration ; les noms de fournisseurs sont fictifs.</p></figcaption></figure>

La page affiche :

Les tuiles de résultat et les segments du graphique comptent des résultats de document distincts. Ici, AP touchless désigne les documents avec approbation seule ; le taux global combiné AP de la vue d'ensemble inclut aussi les documents purement automatiques.

* **Quatre tuiles de résultat final** (Pure touchless, AP touchless, AP assisted, Process exception), chacune reliée aux documents correspondants.
* **La tendance**, avec son propre sélecteur de période : 30 jours, 90 jours, 6 mois, 1 an ou une plage personnalisée (jusqu'à deux ans). Cela ne modifie que le graphique.
* **Les clusters de problèmes** (voir ci-dessous).
* **Change history** : les modifications que vous avez appliquées pour ce fournisseur et leur effet.
* **Recent examples** : des documents d'exemple, dans deux onglets : **Needed attention** et **Went touchless**.
* **Diagnose supplier with AI** : analyse tous les clusters du fournisseur (administrateurs).

Une courte note explique une page vide, par exemple : _5 documents de ce fournisseur sont encore en cours de traitement et n'ont pas encore de résultat d'analyse._ ou _Les 40 documents terminés de ce fournisseur ont tous été traités en touchless : il n'y a rien à diagnostiquer._

### Clusters de problèmes

Un **cluster** regroupe les documents d'un fournisseur qui se sont arrêtés pour la **même première raison**. Au lieu de 40 problèmes isolés, vous voyez « 3 problèmes ».

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-issue-cluster.png" alt="Une carte de cluster de problèmes ouverte avec le premier blocage, ce qu'il faut modifier et la proposition de modification"><figcaption><p>Une carte de cluster ouverte : le premier blocage, <strong>What to change</strong> et une <strong>Change proposal</strong> avec le risque, la portée et les questions ouvertes. Ici, le cluster couvre 58 documents et vaut +18,7 pp. Organisation d'exemple avec des données de démonstration ; les noms de fournisseurs sont fictifs.</p></figcaption></figure>

**Exemple de cluster (illustratif).**

* **Headline** : _Required field missing_ à l'étape _Field Validation_
* **Affected** : 28 documents. **Recoverable** : 28 documents. **Expected lift** : +2,8 pp
* **Suspected cause** : le fournisseur imprime le numéro de BC sous le tableau, là où l'extraction ne regarde pas
* **What to check next** : comparez le numéro de BC imprimé avec la valeur extraite et vérifiez la configuration d'extraction de ce fournisseur avant de proposer une modification
* **Owner** : Consultant. **Confidence** : Medium. **Source** : Hypothesis

Ce qu'affiche une carte de cluster :

| Partie                                     | Signification                                                                                                                                                                                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **First blocker** et **stage**             | La raison et l'étape du pipeline où les documents s'arrêtent. Il existe plus de 30 raisons, par exemple _Supplier not identified_, _Purchase order not found_, _Unit price outside PO tolerance_, _Rejected by the ERP_, _E-invoice validation failed_   |
| **Affected / Recoverable / Expected lift** | Combien de documents, combien peuvent être récupérés, combien de points de pourcentage cela apporterait                                                                                                                                                 |
| **Suspected cause / Confirmed cause**      | Ce que DocBits pense être la raison (ou ce qu'une personne a confirmé)                                                                                                                                                                                  |
| **Evidence** et **Missing evidence**       | Sur quoi repose le constat, et ce que DocBits n'a **pas** pu établir. Lisez **Missing evidence** avant de vous fier au reste                                                                                                                            |
| **What to change**                         | Des étapes concrètes avec des liens **Open** vers les paramètres. Un chip indique le type : _Configuration change_, _Master data change_, _Supplier template change_, _Process change_, _Supplier action needed_, _Not fixable_                          |
| **Owner**                                  | DocBits, Customer, Consultant, Supplier ou Unassigned. Le chip nomme le propriétaire de la proposition de modification ; ce n'est que lorsque les propositions de la carte divergent qu'il retombe sur le propriétaire de l'ensemble du cluster          |
| **Sample documents**                       | Des documents réels du cluster à consulter                                                                                                                                                                                                              |

**Fixable in DocBits** et **Supplier action only** apparaissent dans deux groupes. Pour _Supplier action only_, rien dans DocBits ne change le résultat : le fournisseur doit corriger le document et le renvoyer.

### D'où vient une recommandation

Chaque cause affiche sa **source**, ce qui permet de distinguer une conclusion dérivée d'une supposition :

| Source                             | Signification                                                                                              |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Deterministic** / **Rule-based** | Une règle l'a déduite des preuves enregistrées du pipeline. Aucun modèle de langage n'est intervenu         |
| **Hypothesis**                     | Un modèle de langage l'a proposée à partir des preuves du cluster. Traitez-la comme une piste et vérifiez-la avant d'agir |
| **Confirmed**                      | Une personne a examiné les preuves et confirmé la cause                                                    |

Les textes d'IA sont rédigés dans la langue de votre organisation. Si un cluster a été analysé dans une autre langue, utilisez **Analyse in this language**.

## Qui doit corriger un écart de données source ?

N'assimilez pas **AP assisted** à un échec d'extraction. Pour chaque document d'exemple, distinguez le résultat de traitement de la cause confirmée :

| Preuve | À examiner ou à corriger |
| --- | --- |
| La facture contient une valeur que DocBits a extraite différemment | Configuration de l'extraction ou modèle fournisseur |
| L'extraction correspond à la facture, mais la commande Infor présente un prix, une quantité ou une unité confirmés comme incorrects | Données du système source ; AP se coordonne avec les achats ou le responsable des données de base |
| Infor est correct, mais DocBits en a une copie ancienne ou incomplète | Import ou intégration ERP |
| La facture et les valeurs source diffèrent, mais la valeur convenue n'est pas établie | Clarification métier ; gardez la cause racine non confirmée |

Une petite intervention AP peut terminer la facture tout en laissant un problème récurrent de données source non résolu. Consignez à la fois l'action immédiate et la correction durable. Le cluster seul ne prouve pas le contenu historique d'Infor. Voir l'[exemple Infor détaillé](touchless-po-matching-diagnosis.md#worked-example-correct-extraction-different-infor-data).

## Clusters de rapprochement avec le BC

Si le premier blocage d'un cluster est un motif de rapprochement avec le BC (par exemple _PO item mismatch_ ou _Purchase order not found_), la carte du cluster montre comment DocBits tente de rapprocher la facture du bon de commande. Voir [Diagnostic du rapprochement avec le BC](touchless-po-matching-diagnosis.md).

Voir [Touchless avec MCP](touchless-mcp.md) pour les appels d'outils du rapprochement et la classification des actions humaines.

## Pages connexes

* [Touchless Intelligence](./)
* [Diagnostic du rapprochement avec le BC](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals et rapports](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
