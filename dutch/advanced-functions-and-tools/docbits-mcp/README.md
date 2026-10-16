# DocBits MCP

DocBits biedt een **Model Context Protocol (MCP)**-server waarmee AI-assistenten met uw documenten, extractie, zoekopdrachten, analyses en configuratie kunnen werken — rechtstreeks vanuit een chat- of codeersessie. Elke MCP-compatibele client kan verbinding maken: **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex** of een eigen integratie.

De server is gekoppeld aan de DocBits API op `/v3/mcp` en is afgebakend tot uw organisatie — elke aanroep wordt uitgevoerd met de rechten van de gebruiker (of API-sleutel) die de verbinding heeft gemaakt.

{% hint style="info" %}
**Endpoint — gebruik uw regio (EU of US):**

* Productie (EU) — `https://eu.api.docbits.com/v3/mcp`
* Productie (US) — `https://us.api.docbits.com/v3/mcp`

Zie [Installatie en configuratie](setup-and-configuration.md) voor de volledige hostmatrix en hoe u zich met OAuth aanmeldt.
{% endhint %}

## Wat kunt u doen?

Met DocBits MCP kan een assistent namens u:

* **Documenten zoeken en lezen** — weergeven, zoeken (full-text en per veld), een document openen, de status, logs, paginabeelden en exportvoorvertoning lezen
* **Met geëxtraheerde gegevens werken** — geëxtraheerde velden en tabellen lezen, veldwaarden corrigeren, tabellen met AI extraheren, valideren, goedkeuren en exporteren naar uw ERP
* **Het dashboard bevragen** — dashboardquery's in natuurlijke taal uitvoeren, zoekmodi vergelijken en zoekmogelijkheden inspecteren
* **Analyses ophalen** — managementsamenvattingen, succespercentages, volumetrends, belangrijkste documenttypen en details over openstaande taken
* **E-facturen (eDocs) verwerken** — typen elektronische documenten weergeven, e-documenten testen en verifiëren, aangepaste extractieattributen beheren
* **Stamgegevens beheren** — leveranciersstamgegevens upserten, leveranciersopzoekingen starten, BOD's van leveranciersfacturen importeren, toewijzingen voor betalingsvoorwaarden en kortingen onderhouden
* **Configuratie lezen en wijzigen** — organisatievoorkeuren, documenttypen, veldinstellingen, gebruikers en cache
* **Status controleren** — API- en Celery-status, huidige gebruiker en API-informatie

## Overzicht van tools

DocBits MCP groepeert ruim honderd tools in de onderstaande categorieën (het exacte aantal groeit met elke release; uw assistent toont de actuele set). De meeste komen overeen met bestaande DocBits REST-endpoints; zie de [API-referentie](../../) voor details over verzoek en antwoord. Een assistent kiest op basis van uw verzoek automatisch de juiste tool; de tabellen zijn een overzicht van wat beschikbaar is.

### Documenten en verwerking

| Tool                                    | Beschrijving                                         |
| --------------------------------------- | ---------------------------------------------------- |
| `list_documents`                        | Documenten van de organisatie weergeven (filterbaar) |
| `get_document` / `get_document_by_name` | Een document openen via ID of bestandsnaam           |
| `upload_document`                       | Een nieuw document uploaden voor verwerking          |
| `get_document_status`                   | Huidige pipelinestatus van een document              |
| `get_document_logs`                     | Verwerkingslogregels van een document                |
| `query_org_logs`                        | Door de servicelogs van de organisatie bladeren      |
| `restart_document`                      | De verwerkingspipeline opnieuw uitvoeren             |
| `delete_document`                       | Een document verwijderen                             |
| `get_pending_documents_count`           | Hoeveel documenten op validatie wachten              |

### Extractie en validatie

| Tool                                                | Beschrijving                                                                                 |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `get_extracted_fields` / `get_document_fields`      | Geëxtraheerde headervelden lezen                                                             |
| `get_extracted_tables`                              | Geëxtraheerde tabellen met factuurregels lezen                                               |
| `get_document_for_validation` / `get_next_document` | Een document openen zoals het validatiescherm dat doet; het volgende uit de wachtrij ophalen |
| `get_page_image`                                    | Paginabeeld voor visuele controles                                                           |
| `update_document_fields`                            | Veldwaarden corrigeren of instellen                                                          |
| `validate_document`                                 | Veldvalidatieregels uitvoeren                                                                |
| `approve_document`                                  | Een gevalideerd document goedkeuren                                                          |
| `validate_and_export`                               | Valideren en daarna exporteren naar het ERP                                                  |
| `get_export_preview`                                | De exportpayload bekijken voordat deze wordt verzonden                                       |

### Tabelextractie

Alles wat het validatiescherm en de instellingen voor tabelkolommen met tabellen met factuurregels kunnen doen. Configuratietools wijzigen de documenttypen van de organisatie; extractie- en correctietools werken op één document; regeltools slaan op wat DocBits voor een leverancier heeft geleerd.

| Tool                                                          | Beschrijving                                                                                                                              |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `list_tables` / `get_table_config`                            | Tabellen en kolommen van een documenttype, met de vlaggen Required / Read Only / Hidden / Use AI                                          |
| `create_table`                                                | Een tweede tabel met factuurregels aan een documenttype toevoegen                                                                         |
| `add_table_column` / `delete_table_column`                    | Een tabelkolom toevoegen of soft-delete verwijderen                                                                                       |
| `set_ai_table_config`                                         | AI-tabelextractie, vision en gestructureerde modus voor de organisatie in- of uitschakelen                                                |
| `extract_table_ai`                                            | De AI-tabelextractie op een document uitvoeren (tekst of vision)                                                                          |
| `extract_table_only`                                          | De tabel extraheren zonder de headervelden aan te raken (regels of AI)                                                                    |
| `extract_table_nonai`                                         | Regelgebaseerde extractie op basis van coördinaten die u opgeeft, de eerste stap van een tabeltraining via de API                         |
| `apply_ai_table_formatting` / `apply_table_feedback`          | Een AI-tabel opnieuw opmaken: kolommen verbergen, hertoewijzen, gebruikersfeedback toepassen                                              |
| `remap_table_columns`                                         | Wijzigen welke geëxtraheerde kolom welke geconfigureerde kolom vult                                                                       |
| `save_table_rules` / `save_table_training_rules`              | De coördinatenregels of de AI-opmaakregels voor de leverancier opslaan, zodat het volgende document op dezelfde manier wordt geëxtraheerd |
| `delete_table_training_rules`                                 | De opgeslagen regels van een leverancier verwijderen; het volgende document valt terug op de AI                                           |
| `get_table_extraction_report` / `list_table_report_suppliers` | Rapport per leverancier over hoe tabellen worden geëxtraheerd (regels, AI, model), met een voorvertoning                                  |
| `compare_table_extraction_models`                             | Hetzelfde document met twee AI-niveaus extraheren en de tabellen vergelijken                                                              |

### Zoeken en dashboard

| Tool                                              | Beschrijving                                                                                                 |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `search_documents` / `search_documents_by_name`   | Full-text zoeken en zoeken op bestandsnaam                                                                   |
| `query_document_dashboard`                        | Dashboardquery in natuurlijke taal                                                                           |
| `explain_document_dashboard_query`                | Tonen hoe een query is geïnterpreteerd                                                                       |
| `get_search_capabilities`                         | Welke zoekfuncties de organisatie heeft ingeschakeld                                                         |
| `compare_search_modes`                            | Trefwoord- en vectorresultaten vergelijken                                                                   |
| `diagnose_document_search`                        | Waarom een document wel of niet verschijnt bij een bepaalde zoekopdracht, klassiek en full-text naast elkaar |
| `inspect_document_search_index`                   | Of een document aanwezig is in de document-, tekst- en vectorindexen, en wanneer elk is geschreven           |
| `get_dashboard_columns` / `set_dashboard_columns` | De kolommen op het documentdashboard lezen of wijzigen                                                       |

### Touchless Intelligence

Waarom documenten menselijke tussenkomst nodig hebben en wat u kunt wijzigen zodat dit minder vaak nodig is. Elke tool hier is alleen-lezen, behalve `touchless_apply_change`, die precies één vooraf bekeken instellingswijziging doorvoert.

| Tool                                                             | Beschrijving                                                                                                   |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `touchless_get_summary`                                          | Touchless-scorekaart van de organisatie: hoeveel documenten ongemoeid zijn doorgelopen, per periode en segment |
| `touchless_list_segments`                                        | Waarden waarop u de cijfers kunt segmenteren (leverancier, documenttype, …)                                    |
| `touchless_rank_supplier_opportunities`                          | Leveranciers gerangschikt naar hoeveel handwerk ze veroorzaken                                                 |
| `touchless_diagnose_supplier`                                    | Waarom de documenten van één leverancier bij een mens stoppen                                                  |
| `touchless_get_issue_cluster`                                    | Eén terugkerend probleem en de documenten die het trof                                                         |
| `touchless_get_document_trace`                                   | Volledige touchless-historie van één document                                                                  |
| `touchless_explain_pipeline`                                     | Waar in de pipeline een document of cluster is gestopt                                                         |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | Waarom PO-matching slaagde of mislukte, met de regelset en de tolerantieberekening                             |
| `touchless_get_recommendations`                                  | Wat u moet wijzigen, niet alleen wat er misging                                                                |
| `touchless_list_change_proposals`                                | Instellingswijzigingen die het touchless-percentage zouden verhogen, met de verwachte winst                    |
| `touchless_preview_change`                                       | Eén voorstel als proefrun uitvoeren: er wordt niets geschreven                                                 |
| `touchless_apply_change`                                         | Eén vooraf bekeken voorstel op de organisatie toepassen                                                        |
| `touchless_verify_change`                                        | Wat een doorgevoerde wijziging uiteindelijk waard bleek                                                        |

### Analyses en BI

| Tool                       | Beschrijving                              |
| -------------------------- | ----------------------------------------- |
| `get_executive_summary`    | KPI's op hoog niveau voor de organisatie  |
| `get_success_rates`        | Touchless- / straight-through-percentages |
| `get_volume_trends`        | Documentvolume in de tijd                 |
| `get_top_document_types`   | Meest voorkomende documenttypen           |
| `get_pending_tasks_detail` | Details van openstaand werk               |

### Elektronische documenten (e-facturen)

| Tool                                                           | Beschrijving                                                          |
| -------------------------------------------------------------- | --------------------------------------------------------------------- |
| `list_electronic_document_types`                               | Ondersteunde e-factuurformaten (ZUGFeRD, XRechnung, Factur-X, UBL, …) |
| `test_electronic_document`                                     | Een voorbeeld-e-document classificeren en extraheren                  |
| `verify_electronic_documents` / `validate_all_edocs`           | E-documentextractie verifiëren                                        |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | Aangepaste extractieattributen beheren                                |

### Stamgegevens

| Tool                                                      | Beschrijving                                                                                       |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `upsert_vendor_master_data`                               | Leveranciersstamgegevens aanmaken of bijwerken                                                     |
| `trigger_supplier_lookup`                                 | Een document verrijken met leveranciersstamgegevens                                                |
| `import_supplier_invoice_bod`                             | Een BOD van een leveranciersfactuur importeren                                                     |
| `get_supplier_invoice`                                    | De opgeslagen gegevens van een leveranciersfactuur (BOD) lezen op factuur, leverancier of document |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | Berekeningstoewijzingen onderhouden                                                                |

### Configuratie, beheer en status

| Tool                                                    | Beschrijving                                          |
| ------------------------------------------------------- | ----------------------------------------------------- |
| `get_preferences` / `get_preference` / `set_preference` | Organisatievoorkeuren lezen en wijzigen               |
| `list_document_types` / `get_field_settings`            | De inrichting van documenttypen en velden inspecteren |
| `list_users`                                            | Gebruikers van de organisatie weergeven               |
| `clear_org_cache`                                       | Gecachte configuratie wissen                          |
| `check_api_health` / `check_celery_health`              | Servicestatus                                         |
| `get_current_user` / `get_api_info`                     | Identiteit en API-metagegevens                        |

## Volgende stappen

* [**Installatie en configuratie**](setup-and-configuration.md) — verbind Claude Code, Gemini CLI of Codex (met aanmelding of API-sleutel)
* [**Voorbeelden**](examples.md) — echte dingen die klanten de assistent laten doen
* [**Elektronische documenten (eDocs)**](edocs-mcp/) — verdieping in de eDoc-tools: verwerking van e-facturen inspecteren/testen en aangepaste extractie-/voorvertoningsregels beheren (zelfde endpoint, zelfde aanmelding)
* [**Workflows en kaarten (DocFlow)**](docflow-mcp/) — geavanceerde workflows en partnerkaarten beheren

{% hint style="info" %}
**Eén MCP voor alles.** De eDoc-tools en de tools voor **Workflows en kaarten (DocFlow)** draaien op **hetzelfde** endpoint `api.docbits.com/v3/mcp` met dezelfde DocBits-aanmelding. DocFlow-tools verschijnen daar met het voorvoegsel `docflow_` (bijvoorbeeld `docflow_list_workflows`); de DocFlow-pagina documenteert ze onder hun kale namen. Rechtstreeks verbinden met de DocFlow-host is nog steeds mogelijk, maar niet langer nodig.
{% endhint %}
