# Exemples

Une fois DocBits MCP connecté (voir [Installation et configuration](setup-and-configuration.md)), vous parlez à votre assistant en langage courant — il choisit pour vous les bons outils DocBits. Voici des cas réalistes menés par des clients, avec le type de demande que vous saisiriez et les outils que l'assistant utilise en coulisses.

{% hint style="info" %}
Cela fonctionne de la même manière dans Claude Code, Gemini CLI et Codex — les demandes sont en langage naturel, pas des commandes.
{% endhint %}

## Trier la file de travail

> *« Combien de documents attendent une validation, et de quels types sont-ils ? »*

Utilise `get_pending_documents_count`, `get_pending_tasks_detail`, `get_top_document_types`. L'assistant résume le retard et peut détailler n'importe quel document.

> *« Montre-moi les factures qui ont échoué aujourd'hui et dis-moi pourquoi. »*

Utilise `search_documents` / `query_document_dashboard` + `get_document_logs` pour trouver les documents en erreur et expliquer l'échec à partir des journaux.

## Trouver et inspecter un document

> *« Ouvre la facture INV-2026-00231 et montre les champs extraits et les lignes. »*

Utilise `get_document_by_name`, `get_extracted_fields`, `get_extracted_tables`. L'assistant renvoie les données d'en-tête et le tableau, et peut récupérer l'image de la page avec `get_page_image` si vous voulez voir la source.

> *« Cherche tous les documents du fournisseur "ACME GmbH" du mois dernier de plus de 10 000 €. »*

Utilise `search_documents` / `query_document_dashboard` avec des filtres par champs.

## Corriger et approuver

> *« Sur le document 84213, mets le numéro de bon de commande à 4500098123 et la date d'échéance au 2026-07-15, puis valide-le. »*

Utilise `update_document_fields` puis `validate_document`. L'assistant signale les éventuelles erreurs de validation afin que vous puissiez les corriger.

> *« Valide et exporte le document 84213 vers l'ERP, mais montre-moi d'abord l'aperçu de l'export. »*

Utilise `get_export_preview`, puis `validate_and_export` une fois que vous avez confirmé.

## Corriger une extraction de tableau

> *« Le tableau de lignes de ce bon de livraison est incomplet, il manque deux lignes : réextrais-le avec l'IA, masque la colonne *Charges* et conserve cela pour ce fournisseur. »*

Utilise `extract_table_ai` pour relancer le tableau IA sur le document, `apply_ai_table_formatting` pour masquer la colonne, et `save_table_training_rules` pour enregistrer le résultat pour le fournisseur ; le prochain bon de livraison de ce fournisseur sera extrait de la même manière. `get_extracted_tables` affiche le tableau final. Utile pour les documents où l'extraction par règles a manqué des lignes.

## Analyses et rapports

> *« Donne-moi une synthèse de direction pour ce mois : tendance du volume, taux touchless et les 5 principaux types de documents. »*

Utilise `get_executive_summary`, `get_volume_trends`, `get_success_rates`, `get_top_document_types`. Idéal pour un point rapide à la direction sans ouvrir le tableau de bord.

## Facturation électronique (eDocs)

> *« Quels formats de factures électroniques sont activés chez nous, et ce fichier ZUGFeRD s'extrait-il correctement ? »*

Utilise `list_electronic_document_types` + `test_electronic_document`, puis `verify_electronic_documents` pour confirmer les champs extraits.

## Données de référence et enrichissement des fournisseurs

> *« Ajoute un nouveau fournisseur (nom, TVA, IBAN) aux données de référence, puis relance la recherche de fournisseur sur le document 84500. »*

Utilise `upsert_vendor_master_data` + `trigger_supplier_lookup`.

## Modifications de la configuration

> *« Active l'extraction des QR codes pour notre organisation et confirme que la préférence est bien définie. »*

Utilise `set_preference` (qui vide automatiquement le cache) + `get_preference` pour confirmer.

> *« Liste nos types de documents et montre les paramètres de champs de "Invoice". »*

Utilise `list_document_types` + `get_field_settings`.

## Santé et diagnostics

> *« L'API DocBits et le worker de traitement fonctionnent-ils correctement en ce moment ? Avec quel compte suis-je connecté ? »*

Utilise `check_api_health`, `check_celery_health`, `get_current_user`.

---

## Conseils

- **Soyez précis sur le document** — un ID ou un nom de fichier exact est le plus rapide ; sinon, l'assistant commencera par rechercher.
- **Demandez un aperçu avant d'exporter** — `get_export_preview` vous permet de confirmer la charge utile destinée à l'ERP avant que `validate_and_export` ne l'envoie.
- **Les autorisations s'appliquent** — l'assistant ne peut faire que ce que votre utilisateur DocBits ou votre clé d'API est autorisé à faire. Les approbations et les exports respectent votre rôle et vos ACL.
- **Prudence en production** — le MCP agit sur des données réelles. Sur les environnements clients/de production, privilégiez les actions de lecture et d'aperçu, et confirmez avant d'approuver, d'exporter ou de supprimer.
