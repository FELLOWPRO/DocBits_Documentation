# DocBits MCP

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/docbits-mcp-admin/v1/it.mp4" %}

DocBits espone un server **Model Context Protocol (MCP)** che consente agli assistenti AI di lavorare con i tuoi documenti, l'estrazione, la ricerca, le analisi e la configurazione, direttamente da una chat o da una sessione di programmazione. Qualsiasi client compatibile con MCP può collegarsi: **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex** o qualsiasi integrazione personalizzata.

Il server è montato sull'API DocBits all'indirizzo `/v3/mcp` ed è limitato alla tua organizzazione: ogni chiamata viene eseguita con le autorizzazioni dell'utente (o della chiave API) che ha effettuato la connessione.

{% hint style="info" %}
**Endpoint: utilizza la tua regione (UE o USA):**

- Produzione (UE): `https://eu.api.docbits.com/v3/mcp`
- Produzione (USA): `https://us.api.docbits.com/v3/mcp`

Consulta [Configurazione e setup](setup-and-configuration.md) per la matrice completa degli host e per scoprire come accedere con OAuth.
{% endhint %}

## Cosa puoi fare?

Con DocBits MCP un assistente può, per tuo conto:

- **Trovare e leggere documenti**: elencare, cercare (full-text e per campo), aprire un documento, leggerne lo stato, i log, le immagini delle pagine e l'anteprima di esportazione
- **Lavorare sui dati estratti**: leggere campi e tabelle estratti, correggere i valori dei campi, estrarre tabelle con l'AI, validare, approvare ed esportare nel tuo ERP
- **Interrogare la dashboard**: eseguire query sulla dashboard in linguaggio naturale, confrontare le modalità di ricerca e ispezionare le funzionalità di ricerca
- **Ottenere analisi**: riepiloghi per la direzione, tassi di successo, andamento dei volumi, tipi di documento principali e dettaglio delle attività in sospeso
- **Gestire le e-fatture (eDocs)**: elencare i tipi di documento elettronico, testare e verificare gli e-document, gestire gli attributi di estrazione personalizzati
- **Gestire i dati anagrafici**: eseguire l'upsert dei dati anagrafici dei fornitori, avviare le ricerche fornitore, importare BOD di fatture fornitore, mantenere le mappature di condizioni di pagamento e sconti
- **Leggere e modificare la configurazione**: preferenze dell'organizzazione, tipi di documento, impostazioni dei campi, utenti e cache
- **Controllare lo stato di salute**: stato di API e Celery, utente corrente e informazioni sull'API

## Panoramica degli strumenti

DocBits MCP raggruppa ben oltre cento strumenti nelle categorie riportate di seguito (il numero esatto cresce a ogni rilascio; il tuo assistente elenca l'insieme attuale). La maggior parte rispecchia gli endpoint REST esistenti di DocBits; per i dettagli di richiesta/risposta consulta il [Riferimento API](../../README.md). Un assistente sceglie automaticamente lo strumento giusto in base alla tua richiesta; le tabelle sono una mappa di ciò che è disponibile.

### Documenti ed elaborazione

| Strumento | Descrizione |
|------|-------------|
| `list_documents` | Elenca i documenti dell'organizzazione (filtrabili) |
| `get_document` / `get_document_by_name` | Apre un documento tramite ID o nome file |
| `upload_document` | Carica un nuovo documento per l'elaborazione |
| `get_document_status` | Stato attuale della pipeline di un documento |
| `get_document_logs` | Voci del log di elaborazione di un documento |
| `query_org_logs` | Scorre per pagine i log dei servizi dell'organizzazione |
| `restart_document` | Riesegue la pipeline di elaborazione |
| `delete_document` | Elimina un documento |
| `get_pending_documents_count` | Quanti documenti sono in attesa di validazione |

### Estrazione e validazione

| Strumento | Descrizione |
|------|-------------|
| `get_extracted_fields` / `get_document_fields` | Legge i campi di intestazione estratti |
| `get_extracted_tables` | Legge le tabelle delle righe estratte |
| `get_document_for_validation` / `get_next_document` | Apre un documento come fa la schermata di validazione; recupera il successivo in coda |
| `get_page_image` | Immagine della pagina per i controlli visivi |
| `update_document_fields` | Corregge o imposta i valori dei campi |
| `validate_document` | Esegue le regole di validazione dei campi |
| `approve_document` | Approva un documento validato |
| `validate_and_export` | Valida e poi esporta nell'ERP |
| `get_export_preview` | Anteprima del payload di esportazione prima dell'invio |

### Estrazione delle tabelle

Tutto ciò che la schermata di validazione e le impostazioni delle colonne di tabella possono fare con le tabelle delle righe. Gli strumenti di configurazione modificano i tipi di documento dell'organizzazione; gli strumenti di estrazione e correzione lavorano su un singolo documento; gli strumenti per le regole memorizzano ciò che DocBits ha appreso per un fornitore.

| Strumento | Descrizione |
|------|-------------|
| `list_tables` / `get_table_config` | Tabelle e colonne di un tipo di documento, con i flag Required / Read Only / Hidden / Use AI |
| `create_table` | Aggiunge una seconda tabella di righe a un tipo di documento |
| `add_table_column` / `delete_table_column` | Aggiunge o elimina (soft delete) una colonna di tabella |
| `set_ai_table_config` | Attiva l'estrazione AI delle tabelle, la visione e la modalità strutturata per l'organizzazione |
| `extract_table_ai` | Esegue l'estrazione AI della tabella su un documento (testo o visione) |
| `extract_table_only` | Estrae la tabella senza toccare i campi di intestazione (regole o AI) |
| `extract_table_nonai` | Estrazione basata su regole a partire dalle coordinate che fornisci, il primo passo di un addestramento delle tabelle tramite API |
| `apply_ai_table_formatting` / `apply_table_feedback` | Riformatta una tabella AI: nasconde colonne, rimappa, applica il feedback dell'utente |
| `remap_table_columns` | Cambia quale colonna estratta alimenta quale colonna configurata |
| `save_table_rules` / `save_table_training_rules` | Memorizza le regole di coordinate o le regole di formattazione AI per il fornitore, così il documento successivo viene estratto allo stesso modo |
| `delete_table_training_rules` | Rimuove le regole salvate di un fornitore; il documento successivo ricade sull'AI |
| `get_table_extraction_report` / `list_table_report_suppliers` | Report per fornitore su come vengono estratte le tabelle (regole, AI, modello), con anteprima |
| `compare_table_extraction_models` | Estrae lo stesso documento con due livelli AI e confronta le tabelle |

### Ricerca e dashboard

| Strumento | Descrizione |
|------|-------------|
| `search_documents` / `search_documents_by_name` | Ricerca full-text e per nome file |
| `query_document_dashboard` | Query della dashboard in linguaggio naturale |
| `explain_document_dashboard_query` | Mostra come è stata interpretata una query |
| `get_search_capabilities` | Quali funzionalità di ricerca sono abilitate per l'organizzazione |
| `compare_search_modes` | Confronta i risultati per parola chiave e vettoriali |
| `diagnose_document_search` | Perché un documento compare o non compare per una data ricerca, classica e full-text a confronto |
| `inspect_document_search_index` | Se un documento è presente negli indici di documento, testo e vettoriale, e quando ciascuno è stato scritto |
| `get_dashboard_columns` / `set_dashboard_columns` | Legge o modifica le colonne mostrate nella dashboard dei documenti |

### Touchless Intelligence

Perché i documenti richiedono l'intervento umano e cosa modificare perché ne servano meno. Tutti gli strumenti di questa sezione sono di sola lettura, tranne `touchless_apply_change`, che scrive esattamente una modifica di impostazione di cui è stata vista l'anteprima.

| Strumento | Descrizione |
|------|-------------|
| `touchless_get_summary` | Scorecard touchless dell'organizzazione: quanti documenti sono passati senza interventi, per periodo e segmento |
| `touchless_list_segments` | Valori per cui puoi segmentare i numeri (fornitore, tipo di documento, …) |
| `touchless_rank_supplier_opportunities` | Fornitori classificati in base a quanto lavoro manuale generano |
| `touchless_diagnose_supplier` | Perché i documenti di un fornitore si fermano in attesa di una persona |
| `touchless_get_issue_cluster` | Un problema ricorrente e i documenti che ha interessato |
| `touchless_get_document_trace` | Cronologia touchless completa di un documento |
| `touchless_explain_pipeline` | In quale punto della pipeline si è fermato un documento o un cluster |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | Perché il PO matching è riuscito o fallito, con il set di regole e il calcolo delle tolleranze |
| `touchless_get_recommendations` | Cosa modificare, non solo cosa è andato storto |
| `touchless_list_change_proposals` | Modifiche alle impostazioni che aumenterebbero il tasso touchless, con il miglioramento atteso |
| `touchless_preview_change` | Prova a vuoto di una proposta: non viene scritto nulla |
| `touchless_apply_change` | Applica all'organizzazione una proposta di cui è stata vista l'anteprima |
| `touchless_verify_change` | Quanto è valsa, alla fine, una modifica applicata |

### Analisi e BI

| Strumento | Descrizione |
|------|-------------|
| `get_executive_summary` | KPI di alto livello dell'organizzazione |
| `get_success_rates` | Tassi touchless / straight-through |
| `get_volume_trends` | Volume dei documenti nel tempo |
| `get_top_document_types` | Tipi di documento più frequenti |
| `get_pending_tasks_detail` | Dettaglio del lavoro in sospeso |

### Documenti elettronici (e-fatture)

| Strumento | Descrizione |
|------|-------------|
| `list_electronic_document_types` | Formati di e-fattura supportati (ZUGFeRD, XRechnung, Factur-X, UBL, …) |
| `test_electronic_document` | Classifica ed estrae un e-document di esempio |
| `verify_electronic_documents` / `validate_all_edocs` | Verifica l'estrazione degli e-document |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | Gestisce gli attributi di estrazione personalizzati |

### Dati anagrafici

| Strumento | Descrizione |
|------|-------------|
| `upsert_vendor_master_data` | Crea o aggiorna i dati anagrafici dei fornitori |
| `trigger_supplier_lookup` | Arricchisce un documento con i dati anagrafici del fornitore |
| `import_supplier_invoice_bod` | Importa un BOD di fattura fornitore |
| `get_supplier_invoice` | Legge i dati persistiti della fattura fornitore (BOD) per fattura, fornitore o documento |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | Mantiene le mappature di calcolo |

### Configurazione, amministrazione e stato di salute

| Strumento | Descrizione |
|------|-------------|
| `get_preferences` / `get_preference` / `set_preference` | Legge e modifica le preferenze dell'organizzazione |
| `list_document_types` / `get_field_settings` | Ispeziona la configurazione di tipi di documento e campi |
| `list_users` | Elenca gli utenti dell'organizzazione |
| `clear_org_cache` | Svuota la configurazione in cache |
| `check_api_health` / `check_celery_health` | Stato di salute dei servizi |
| `get_current_user` / `get_api_info` | Identità e metadati dell'API |

## Prossimi passi

- [**Configurazione e setup**](setup-and-configuration.md): collega Claude Code, Gemini CLI o Codex (con login o chiave API)
- [**Esempi**](examples.md): cose reali che i clienti chiedono all'assistente di fare
- [**Documenti elettronici (eDocs)**](../edocs-mcp/README.md): approfondimento sugli strumenti eDoc: ispezionare/testare l'elaborazione delle e-fatture e gestire le regole personalizzate di estrazione/anteprima (stesso endpoint, stesso login)
- [**Workflow e Card (DocFlow)**](../docflow-mcp/README.md): gestisci workflow avanzati e card partner

{% hint style="info" %}
**Un unico MCP per tutto.** Gli strumenti eDoc e quelli **Workflow e Card (DocFlow)** vengono eseguiti sullo **stesso** endpoint `api.docbits.com/v3/mcp` con lo stesso login DocBits. Gli strumenti DocFlow vi compaiono con il prefisso `docflow_` (ad esempio `docflow_list_workflows`); la pagina DocFlow li documenta con il loro nome senza prefisso. Collegarsi direttamente all'host DocFlow è ancora possibile, ma non è più necessario.
{% endhint %}

[Configurare DocBits con Claude o Codex](configuration-with-claude-or-codex.md): connessione, prompt, anteprime, modifiche con versioni, verifiche e ripristino.
