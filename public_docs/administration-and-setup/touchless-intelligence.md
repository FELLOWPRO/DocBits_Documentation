# Touchless Intelligence

Touchless Intelligence répond à deux questions distinctes : **DocBits a-t-il correctement extrait la facture ?** et **Le processus entier a-t-il abouti sans intervention de traitement ?** Une extraction correcte peut encore nécessiter du travail si les données Infor diffèrent. AP désigne l’équipe humaine de comptabilité fournisseurs.

## Vidéo : fonctions du rapport Touchless

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/fr.mp4" %}

Cette version de contrôle de 5:45 montre un rapport alimenté : filtres, indicateurs et calcul, évolution, premiers blocages, preuves enregistrées, historique du document, exécutions, règles apprises, améliorations et historique, conseil et résultats MCP réels.

[Ouvrir la vidéo avec sous-titres français et 16 chapitres](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/fr.html). L'évaluation auditive de cette nouvelle version reste à réaliser.

Ces cas pédagogiques expliquent les fonctions du rapport. Une recommandation ou un aperçu ne prouve ni une modification appliquée ni une amélioration mesurée. La proposition MCP affichée nécessite encore une configuration cible précise ; aperçu et application sont indisponibles. Certains textes natifs du produit peuvent conserver leur langue d'origine. Dans les règles apprises, «20 sur 21» indique les cas auxquels la règle s’applique. Le contre-exemple montre une valeur déjà acceptée que la règle remplacerait ; certains libellés natifs traduisent ce sens de façon imprécise.

<figure><img src="../.gitbook/assets/anatomy-touchless-fr.svg" alt="Chaîne de tri isométrique : un convoyeur avec 14 portes, un poussoir qui dévie un document vers un bac de contrôle, un bac d'export avec une pile de documents et un cadran indiquant 78,9 pour cent"><figcaption><p>Touchless comme chaîne de tri, avec les chiffres illustratifs de l'exemple de calcul : les 14 portes sont les étapes du Chemin du pipeline, les feuilles encore sur le tapis sont en cours et ne sont pas comptées, un document qui s'arrête à une porte est poussé dans le bac de contrôle avec les documents AP assisté (30) et Exception de processus (10), et les documents Pure (120) et avec approbation seule (30) dans le bac d'export donnent les 150 sur 190 du cadran, soit 78,9 %, au-dessus de la marque cible de 70 %.</p></figcaption></figure>

## Trouver le bon guide

| Guide | Contenu |
| --- | --- |
| [Indicateurs et calcul](touchless-metrics.md) | Catégories, numérateur/dénominateur, interventions et calculs |
| [Utiliser le tableau de bord](touchless-dashboard.md) | Filtres, indicateurs, tendances et premiers blocages |
| [Exemples : prix et quantité](touchless-examples.md) | Factures fictives et vues Dev réelles avec écarts de prix et quantité |
| [Touchless Intelligence : Diagnostic fournisseur et clusters de problèmes](touchless-supplier-diagnosis.md) | Prioriser les fournisseurs et les causes récurrentes |
| [Touchless Intelligence : Diagnostic du rapprochement avec le BC](touchless-po-matching-diagnosis.md) | Comprendre règles actives, tolérances et décisions |
| [Touchless Intelligence : Trace du document](touchless-document-trace.md) | Contrôler originaux, exécutions, blocages et interventions |
| [Touchless Intelligence : Propositions de modification et rapports](touchless-change-proposals.md) | Distinguer prévisualisation, application, mesure et annulation |
| [Expliquer et améliorer Touchless avec MCP](touchless-mcp.md) | Expliquer, diagnostiquer et améliorer avec MCP de manière contrôlée |

<figure><img src="../.gitbook/assets/touchless-overview-fr.png" alt="L'onglet Touchless Intelligence avec cinq chiffres clés, des suggestions d'amélioration et le graphique du taux touchless"><figcaption><p>L'onglet Touchless Intelligence : chiffres clés, améliorations, le taux dans le temps et le graphique de la première perte. Organisation d'exemple avec des données de démonstration ; les noms de fournisseurs sont fictifs.</p></figcaption></figure>

## Accès

Cette section appartient au [tableau de bord analytique](analytics-dashboard.md). Les administrateurs y accèdent ; les autres utilisateurs doivent avoir le droit de rôle correspondant. Analyse IA, modifications compatibles et rapports peuvent exiger des droits administrateur.

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Touchless documentation alignment 2026-11-04: extraction quality is distinct from process automation. KPI definition checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4; existing native screenshots and video sources preserved except unsafe historical list images. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
