# DocBits MCP

DocBits expose un serveur **Model Context Protocol (MCP)** qui permet aux assistants IA de travailler avec vos documents, l'extraction, la recherche, les analyses et la configuration — directement depuis un chat ou une session de code. Tout client compatible MCP peut s'y connecter : **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex** ou toute intégration personnalisée.

Le serveur est monté sur l'API DocBits à l'adresse `/v3/mcp` et est limité à votre organisation — chaque appel s'exécute avec les autorisations de l'utilisateur (ou de la clé d'API) qui s'est connecté.

{% hint style="info" %}
**Point de terminaison — utilisez votre région (UE ou États-Unis) :**

* Production (UE) — `https://eu.api.docbits.com/v3/mcp`
* Production (États-Unis) — `https://us.api.docbits.com/v3/mcp`

Consultez [Installation et configuration](setup-and-configuration.md) pour la matrice complète des hôtes et la connexion avec OAuth.
{% endhint %}

## Que pouvez-vous faire ?

Avec DocBits MCP, un assistant peut, en votre nom :

* **Trouver et lire des documents** — lister, rechercher (texte intégral et par champs), ouvrir un document, lire son statut, ses journaux, ses images de page et son aperçu d'export
* **Travailler sur les données extraites** — lire les champs et tableaux extraits, corriger des valeurs de champs, extraire des tableaux avec l'IA, valider, approuver et exporter vers votre ERP
* **Interroger le tableau de bord** — exécuter des requêtes de tableau de bord en langage naturel, comparer les modes de recherche et inspecter les capacités de recherche
* **Obtenir des analyses** — synthèses de direction, taux de réussite, tendances de volume, types de documents les plus fréquents et détail des tâches en attente
* **Gérer les factures électroniques (eDocs)** — lister les types de documents électroniques, tester et vérifier les e-documents, gérer les attributs d'extraction personnalisés
* **Gérer les données de référence** — créer ou mettre à jour les données de référence fournisseurs, déclencher des recherches de fournisseurs, importer des BOD de factures fournisseurs, maintenir les mappages des conditions de paiement et des remises
* **Lire et modifier la configuration** — préférences de l'organisation, types de documents, paramètres de champs, utilisateurs et cache
* **Vérifier l'état de santé** — santé de l'API et de Celery, utilisateur courant et informations sur l'API

## Aperçu des outils

DocBits MCP regroupe bien plus d'une centaine d'outils dans les catégories ci-dessous (le nombre exact augmente à chaque version ; votre assistant liste l'ensemble actuel). La plupart reflètent des points de terminaison REST DocBits existants ; consultez la [Référence de l'API](../../) pour le détail des requêtes et des réponses. Un assistant choisit automatiquement l'outil adapté à partir de votre demande ; les tableaux constituent une carte de ce qui est disponible.

### Documents et traitement

| Outil                                   | Description                                                       |
| --------------------------------------- | ----------------------------------------------------------------- |
| `list_documents`                        | Lister les documents de l'organisation (filtrable)                |
| `get_document` / `get_document_by_name` | Ouvrir un document par ID ou par nom de fichier                   |
| `upload_document`                       | Charger un nouveau document à traiter                             |
| `get_document_status`                   | Statut actuel d'un document dans le pipeline                      |
| `get_document_logs`                     | Entrées du journal de traitement d'un document                    |
| `query_org_logs`                        | Parcourir page par page les journaux de service de l'organisation |
| `restart_document`                      | Relancer le pipeline de traitement                                |
| `delete_document`                       | Supprimer un document                                             |
| `get_pending_documents_count`           | Nombre de documents en attente de validation                      |

### Extraction et validation

| Outil                                               | Description                                                                                |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `get_extracted_fields` / `get_document_fields`      | Lire les champs d'en-tête extraits                                                         |
| `get_extracted_tables`                              | Lire les tableaux de lignes extraits                                                       |
| `get_document_for_validation` / `get_next_document` | Ouvrir un document comme le fait l'écran de validation ; récupérer le suivant dans la file |
| `get_page_image`                                    | Image de page pour les contrôles visuels                                                   |
| `update_document_fields`                            | Corriger ou définir des valeurs de champs                                                  |
| `validate_document`                                 | Exécuter les règles de validation des champs                                               |
| `approve_document`                                  | Approuver un document validé                                                               |
| `validate_and_export`                               | Valider puis exporter vers l'ERP                                                           |
| `get_export_preview`                                | Prévisualiser la charge utile de l'export avant l'envoi                                    |

### Extraction de tableaux

Tout ce que l'écran de validation et les paramètres des colonnes de tableau permettent de faire avec les tableaux de lignes. Les outils de configuration modifient les types de documents de l'organisation ; les outils d'extraction et de correction travaillent sur un seul document ; les outils de règles enregistrent ce que DocBits a appris pour un fournisseur.

| Outil                                                         | Description                                                                                                                                               |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_tables` / `get_table_config`                            | Tableaux et colonnes d'un type de document, avec les indicateurs Required / Read Only / Hidden / Use AI                                                   |
| `create_table`                                                | Ajouter un second tableau de lignes à un type de document                                                                                                 |
| `add_table_column` / `delete_table_column`                    | Ajouter une colonne de tableau ou la supprimer (suppression logique)                                                                                      |
| `set_ai_table_config`                                         | Activer l'extraction de tableaux par IA, la vision et le mode structuré pour l'organisation                                                               |
| `extract_table_ai`                                            | Exécuter l'extraction de tableau par IA sur un document (texte ou vision)                                                                                 |
| `extract_table_only`                                          | Extraire le tableau sans toucher aux champs d'en-tête (règles ou IA)                                                                                      |
| `extract_table_nonai`                                         | Extraction par règles à partir de coordonnées que vous transmettez, première étape d'un entraînement de tableau via l'API                                 |
| `apply_ai_table_formatting` / `apply_table_feedback`          | Remettre en forme un tableau IA : masquer des colonnes, remapper, appliquer le retour d'un utilisateur                                                    |
| `remap_table_columns`                                         | Changer quelle colonne extraite alimente quelle colonne configurée                                                                                        |
| `save_table_rules` / `save_table_training_rules`              | Enregistrer les règles de coordonnées ou les règles de mise en forme IA pour le fournisseur, afin que le document suivant soit extrait de la même manière |
| `delete_table_training_rules`                                 | Supprimer les règles enregistrées d'un fournisseur ; le document suivant revient à l'IA                                                                   |
| `get_table_extraction_report` / `list_table_report_suppliers` | Rapport par fournisseur sur la manière dont les tableaux sont extraits (règles, IA, modèle), avec un aperçu                                               |
| `compare_table_extraction_models`                             | Extraire le même document avec deux niveaux d'IA et comparer les tableaux                                                                                 |

### Recherche et tableau de bord

| Outil                                             | Description                                                                                                       |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `search_documents` / `search_documents_by_name`   | Recherche en texte intégral et par nom de fichier                                                                 |
| `query_document_dashboard`                        | Requête de tableau de bord en langage naturel                                                                     |
| `explain_document_dashboard_query`                | Montrer comment une requête a été interprétée                                                                     |
| `get_search_capabilities`                         | Quelles fonctions de recherche l'organisation a activées                                                          |
| `compare_search_modes`                            | Comparer les résultats par mots-clés et vectoriels                                                                |
| `diagnose_document_search`                        | Pourquoi un document apparaît ou non pour une recherche donnée, recherche classique et texte intégral côte à côte |
| `inspect_document_search_index`                   | Si un document est présent dans les index de documents, de texte et vectoriel, et quand chacun a été écrit        |
| `get_dashboard_columns` / `set_dashboard_columns` | Lire ou modifier les colonnes affichées sur le tableau de bord des documents                                      |

### Touchless Intelligence

Pourquoi des documents nécessitent une intervention humaine et que modifier pour qu'il y en ait moins. Tous les outils ci-dessous sont en lecture seule, sauf `touchless_apply_change`, qui écrit exactement une modification de paramètre prévisualisée.

| Outil                                                            | Description                                                                                                                      |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `touchless_get_summary`                                          | Tableau de bord touchless de l'organisation : combien de documents ont été traités sans intervention, par période et par segment |
| `touchless_list_segments`                                        | Valeurs selon lesquelles vous pouvez segmenter les chiffres (fournisseur, type de document, …)                                   |
| `touchless_rank_supplier_opportunities`                          | Fournisseurs classés selon le volume de travail manuel qu'ils génèrent                                                           |
| `touchless_diagnose_supplier`                                    | Pourquoi les documents d'un fournisseur s'arrêtent en attente d'une personne                                                     |
| `touchless_get_issue_cluster`                                    | Un problème récurrent et les documents qu'il a touchés                                                                           |
| `touchless_get_document_trace`                                   | Historique touchless complet d'un document                                                                                       |
| `touchless_explain_pipeline`                                     | À quel endroit du pipeline un document ou un cluster s'est arrêté                                                                |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | Pourquoi le rapprochement des bons de commande a réussi ou échoué, avec le jeu de règles et le calcul des tolérances             |
| `touchless_get_recommendations`                                  | Que modifier, et pas seulement ce qui a mal tourné                                                                               |
| `touchless_list_change_proposals`                                | Modifications de paramètres qui augmenteraient le taux touchless, avec le gain attendu                                           |
| `touchless_preview_change`                                       | Simuler une proposition : rien n'est écrit                                                                                       |
| `touchless_apply_change`                                         | Appliquer une proposition prévisualisée à l'organisation                                                                         |
| `touchless_verify_change`                                        | Ce que valait finalement une modification appliquée                                                                              |

### Analyses et BI

| Outil                      | Description                           |
| -------------------------- | ------------------------------------- |
| `get_executive_summary`    | KPI de haut niveau de l'organisation  |
| `get_success_rates`        | Taux touchless / de traitement direct |
| `get_volume_trends`        | Volume de documents dans le temps     |
| `get_top_document_types`   | Types de documents les plus fréquents |
| `get_pending_tasks_detail` | Détail du travail en attente          |

### Documents électroniques (factures électroniques)

| Outil                                                          | Description                                                                             |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `list_electronic_document_types`                               | Formats de factures électroniques pris en charge (ZUGFeRD, XRechnung, Factur-X, UBL, …) |
| `test_electronic_document`                                     | Classer et extraire un exemple d'e-document                                             |
| `verify_electronic_documents` / `validate_all_edocs`           | Vérifier l'extraction des e-documents                                                   |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | Gérer les attributs d'extraction personnalisés                                          |

### Données de référence

| Outil                                                     | Description                                                                                      |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `upsert_vendor_master_data`                               | Créer ou mettre à jour les données de référence d'un fournisseur                                 |
| `trigger_supplier_lookup`                                 | Enrichir un document à partir des données de référence fournisseurs                              |
| `import_supplier_invoice_bod`                             | Importer un BOD de facture fournisseur                                                           |
| `get_supplier_invoice`                                    | Lire les données de facture fournisseur (BOD) enregistrées, par facture, fournisseur ou document |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | Maintenir les mappages de calcul                                                                 |

### Configuration, administration et santé

| Outil                                                   | Description                                                     |
| ------------------------------------------------------- | --------------------------------------------------------------- |
| `get_preferences` / `get_preference` / `set_preference` | Lire et modifier les préférences de l'organisation              |
| `list_document_types` / `get_field_settings`            | Inspecter la configuration des types de documents et des champs |
| `list_users`                                            | Lister les utilisateurs de l'organisation                       |
| `clear_org_cache`                                       | Vider la configuration en cache                                 |
| `check_api_health` / `check_celery_health`              | Santé des services                                              |
| `get_current_user` / `get_api_info`                     | Identité et métadonnées de l'API                                |

## Étapes suivantes

* [**Installation et configuration**](setup-and-configuration.md) — connecter Claude Code, Gemini CLI ou Codex (avec connexion ou clé d'API)
* [**Exemples**](examples.md) — ce que les clients demandent réellement à l'assistant
* [**Documents électroniques (eDocs)**](edocs-mcp/) — approfondissement sur les outils eDoc : inspecter/tester le traitement des factures électroniques et gérer les règles d'extraction/d'aperçu personnalisées (même point de terminaison, même connexion)
* [**Workflows et cartes (DocFlow)**](docflow-mcp/) — gérer les workflows avancés et les cartes partenaires

{% hint style="info" %}
**Un seul MCP pour tout.** Les outils eDoc et les outils **Workflows et cartes (DocFlow)** s'exécutent sur le **même** point de terminaison `api.docbits.com/v3/mcp` avec la même connexion DocBits. Les outils DocFlow y apparaissent avec le préfixe `docflow_` (par exemple `docflow_list_workflows`) ; la page DocFlow les documente sous leur nom simple. Il reste possible de se connecter directement à l'hôte DocFlow, mais ce n'est plus nécessaire.
{% endhint %}
