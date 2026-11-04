# Utiliser le tableau de bord

<!-- touchless-admin-video-v2-20261104:start -->
**Chapitre vidéo (version de contrôle):** [Sélection et date des données](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/fr.html#chapter=01).
<!-- touchless-admin-video-v2-20261104:end -->

### Filtres

| Filtre | Ce qu'il fait |
| --- | --- |
| **7J / 30J / 90J** (7D / 30D / 90D) | La période pour les chiffres clés et la file d'attente. La valeur par défaut est de 30 jours |
| **Type de document** (Document Type) | Filtre les métriques Touchless et leur analyse par type. Les propositions de règles apprises ont actuellement leur propre sélection ; voir ci-dessous. |
| **Champ de segment / Valeur de segment** (Segment field / Segment value) | Uniquement si votre organisation fait passer plusieurs processus par un même type de document (par exemple des commandes directes, indirectes et EAM dans le champ `order_type`). Choisissez un champ pour voir la répartition, choisissez une valeur pour y limiter tous les chiffres |
| **ID du document** (Document ID) | Ouvre la **Trace du document** pour un document |

La **sous-organisation** que vous avez sélectionnée en haut de DocBits limite les chiffres clés et la file d'attente des fournisseurs. Les clusters de problèmes et l'analyse par IA couvrent toujours toute l'organisation.

### Type de document et propositions de règles apprises

Le sélecteur supérieur et celui des règles apprises sont indépendants dans l’implémentation vérifiée. Cette section charge ses types et choisit initialement le premier. **ORDER_CONFIRMATION** en haut peut donc coexister avec **INVOICE** en bas : ces règles concernent les factures, pas les confirmations de commande. Vérifiez le type local avant d’appliquer une règle. S’il manque, aucune proposition n’est établie pour ce type. L’échantillon de corrections, par exemple sur 60 jours, ne reprend pas automatiquement la période du taux supérieur. Cette description ne signifie pas qu’une synchronisation ait été mise en œuvre.

### Les cinq chiffres clés

<figure><img src="../.gitbook/assets/touchless-report-kpi-fr-20261104.png" alt="Rapport actuel sur 30 jours pour les factures : 107 entièrement automatiques et 11 avec approbation seule donnent 118 sur 201, soit 58,7 % AP Touchless. Pure seul représente 53,2 %. La carte AP affiche déjà le total combiné de 118. Historique fictif de formation ; aucun export ERP exécuté n’est établi."><figcaption><p>Rapport actuel sur 30 jours pour les factures : 107 entièrement automatiques et 11 avec approbation seule donnent 118 sur 201, soit 58,7 % AP Touchless. Pure seul représente 53,2 %. La carte AP affiche déjà le total combiné de 118. Historique fictif de formation ; aucun export ERP exécuté n’est établi.</p></figcaption></figure>

| Carte | Ce qui est compté | Capture actuelle |
| --- | --- | --- |
| Pure Touchless | Traitement réussi sans intervention ni approbation | 107 · 53,2 % |
| AP Touchless | Pure et approbation seule ; pourcentage et nombre combinés | 118 · 58,7 % |
| AP Assisted | Traitement réussi avec intervention manuelle | 37 · 18,4 % |
| Exceptions de processus | Résultat classé comme exception | 46 · 22,9 % |
| Couverture du diagnostic | Cas bloqués avec une cause connue | 100 % · 0 sans cause connue |

* Une carte affiche un tiret (—) au lieu de **0 %** lorsqu'il n'y a rien à mesurer. Un tiret signifie « pas de données », pas « zéro ».
* **Couverture du diagnostic** = documents avec un motif de blocage connu ÷ tous les documents bloqués. Exemple : 50 documents bloqués, dont 10 avec une cause inconnue → 40 ÷ 50 = **80 %**. Une valeur faible signifie « nous ne comprenons pas encore pourquoi les documents s'arrêtent ». Améliorez-la avant d'essayer de corriger des causes individuelles.
* **Cliquez sur une carte** pour ouvrir dans un nouvel onglet la liste des documents derrière le chiffre (« Voir les documents derrière ce chiffre »). Les cartes avec 0 document ne sont pas cliquables.

### Taux touchless dans le temps

<figure><img src="../.gitbook/assets/touchless-report-trend-fr-20261104.png" alt="Tendance actuelle : rose représente Pure Touchless et bleu le taux combiné, approbation seule incluse. La ligne pointillée marque l’objectif de 70 %. Ces cas fictifs de formation ne démontrent pas une amélioration réelle du processus."><figcaption><p>Tendance actuelle : rose représente Pure Touchless et bleu le taux combiné, approbation seule incluse. La ligne pointillée marque l’objectif de 70 %. Ces cas fictifs de formation ne démontrent pas une amélioration réelle du processus.</p></figcaption></figure>

Le graphique actuel montre Pure, le taux AP combiné et l’objectif. Bleu inclut Pure et approbation seule : il est au même niveau ou au-dessus de rose ; n’additionnez pas les deux taux. Chaque point utilise sa propre population de documents terminés et éligibles : un taux quotidien n’est pas automatiquement celui de toute la période. Les périodes courtes affichent des points quotidiens, les longues des points hebdomadaires. La catégorie distincte approbation seule diffère de cette courbe combinée.

**Exemple.** Un taux Pure passant de 55 à 68 % après un changement montre une association temporelle. Comparez type, fournisseurs et autres changements : l’avant/après ne prouve pas à lui seul une cause unique.

### Où le touchless est perdu en premier

<figure><img src="../.gitbook/assets/touchless-blocking-stages-fr.png" alt="Graphique en barres des documents bloqués par première étape de blocage et par motif"><figcaption><p>Documents bloqués par étape et par motif où ils se sont arrêtés en premier. Ici, <strong>Validation des champs : champ obligatoire manquant</strong> coûte le plus de documents (58), suivi de <strong>Échec du mappage d'exportation</strong> (46) et de <strong>Écart d'article du BC</strong> (27). Organisation d'exemple avec des données de démonstration ; les noms de fournisseurs sont fictifs.</p></figcaption></figure>

Un graphique en barres des **Documents bloqués** (Blocked documents) par étape du pipeline : la **première** étape qui a arrêté un document.

**Exemple.** Si les barres indiquent identification fournisseur 12, validation des champs 41 et rapprochement des lignes 7, examinez d’abord la validation. Une valeur non extraite est une cause possible ; comparez original, règles et données source avant de la confirmer.

### Opportunités fournisseurs


Chaque document terminé et éligible appartient à une seule catégorie :

| Catégorie | Signification | Compte comme touchless ? |
| --- | --- | --- |
| **Pure Touchless** | Traitement réussi, sans intervention humaine ni approbation | Oui |
| **AP Touchless** | Traitement réussi ; seule une approbation métier était nécessaire | Oui |
| **AP Assisted**, avec intervention AP | Traitement réussi, mais une personne a corrigé, validé manuellement ou relancé le document | Non |
| **Exception de processus** | Par exemple rejet, erreur définitive, refus de l’ERP ou blocage classé comme exception | Non |

La validation manuelle désigne ici une intervention enregistrée ; une simple approbation reste AP Touchless. **AP Assisted décrit l’intervention, pas sa cause** : une extraction correcte peut être suivie d’un écart avec Infor. Les documents en cours ou non éligibles sont exclus du dénominateur.

**Exemple.** Votre organisation a 1 000 documents éligibles sur la période. Le fournisseur A a 40 documents récupérables, le fournisseur B a 90 documents perdus mais seulement 10 récupérables (son problème est de son côté).

* Fournisseur A : 40 ÷ 1 000 = **+4,0 pp de gain attendu**
* Fournisseur B : 10 ÷ 1 000 = **+1,0 pp**, bien que B ait plus de documents perdus

La file d'attente classe A avant B parce que le **gain attendu** est mesuré par rapport à toute votre organisation, pas par rapport au fournisseur. Un fournisseur avec quatre mauvais documents ne peut pas passer devant un fournisseur avec quatre cents.

Utilisez le champ de recherche (« Rechercher un numéro ou un nom de fournisseur ») pour trouver un fournisseur. Cliquez sur une ligne pour ouvrir le **Diagnostic fournisseur**.

### Comparer les fournisseurs


Cliquez sur **Comparer les fournisseurs**, cochez **deux à cinq** fournisseurs (chacun est listé avec son nombre de documents bloqués) et cliquez sur **Comparer**.

La comparaison affiche les fournisseurs côte à côte : **Taux pur**, **Documents perdus**, **Récupérables**, **Cause racine**, **Gain attendu**, un graphique en barres des résultats et un lien vers chaque **Diagnostic fournisseur**.

**Exemple.** A et B utilisent la même mise en page ; B atteint 80 % Pure et A 35 %. Si le diagnostic suggère les données de référence, comparez originaux, extraction et enregistrements importés. Cet écart de taux ne prouve à lui seul ni une mise en page correcte ni des données incomplètes chez A.

### Analyser avec l'IA

Le bouton **Analyser n clusters avec l'IA** (Analyse n clusters with AI) analyse les clusters de problèmes ayant le plus fort potentiel touchless (au moins un nombre minimal de documents chacun). Cela prend environ 13 secondes par cluster et couvre **toute l'organisation**. Seuls les administrateurs peuvent le lancer.

Pendant l'exécution, vous voyez **En file d'attente**, **En cours**, **Terminé**, **Déjà analysé** ou **Erreur** pour chaque cluster, avec un lien **Ouvrir le cluster**. Si l'IA est désactivée ou n'est pas configurée dans l'environnement, le bouton est désactivé avec la raison, et **tout le reste de la page continue de fonctionner**.

## Travailler avec Touchless Intelligence : une routine

1. **Chaque semaine** : ouvrez l'onglet et comparez le **taux** et la **tendance** à l'objectif.
2. Regardez la **Couverture du diagnostic**. En dessous d'environ 80 %, cherchez d'abord pourquoi les documents s'arrêtent.
3. Lisez **Où le touchless est perdu en premier** et choisissez l'étape la plus importante.
4. Ouvrez **Opportunités fournisseurs**. Triez par **Gain attendu** et prenez le premier fournisseur avec le statut **RECOVERABLE**.
5. Lisez les **clusters de problèmes**, vérifiez **Preuves manquantes**, puis suivez **Que modifier**.
6. Corrigez une cause confirmée. Pour une proposition DocBits compatible, utilisez prévisualisation et historique. Pour Infor, consignez source et import séparément : cela ne crée pas automatiquement une modification de paramètre dans cet historique.
7. Après deux semaines, vérifiez le résultat **avant/après**.

## Qui peut le voir

* L'onglet fait partie du Tableau de bord analytique. Votre administrateur l'active pour l'organisation. Si l'onglet est absent, demandez à votre administrateur.
* Les **administrateurs de l'organisation** le voient toujours.
* Les autres utilisateurs le voient lorsqu'un administrateur a accordé à leur rôle l'onglet **Tableau de bord analytique** (**Paramètres → Rôles**). Sans cette autorisation, seuls les administrateurs y ont accès.
* Certaines actions sont réservées aux administrateurs : l'**analyse par IA**, l'**application et l'annulation d'une modification**, les **propositions de règles apprises** et le **rapport de conseil** (Consulting report).

Si vous n'y êtes pas autorisé, la page affiche *Action non autorisée, veuillez contacter l'administrateur* (Action not allowed, please contact the administrator).

## Pages associées

* [Touchless Intelligence](touchless-intelligence.md)
* [Indicateurs et calcul](touchless-metrics.md)
* [Exemples : prix et quantité](touchless-examples.md)
* [Touchless Intelligence : Diagnostic fournisseur et clusters de problèmes](touchless-supplier-diagnosis.md)
* [Touchless Intelligence : Diagnostic du rapprochement avec le BC](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence : Trace du document](touchless-document-trace.md)
* [Touchless Intelligence : Propositions de modification et rapports](touchless-change-proposals.md)
* [Expliquer et améliorer Touchless avec MCP](touchless-mcp.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Touchless documentation alignment 2026-11-04: extraction quality is distinct from process automation. KPI definition checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4; existing native screenshots and video sources preserved except unsafe historical list images. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
