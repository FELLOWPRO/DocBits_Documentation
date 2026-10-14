# Esempi

Una volta collegato DocBits MCP (vedi [Configurazione e setup](setup-and-configuration.md)), parli con il tuo assistente in linguaggio naturale: sceglie lui gli strumenti DocBits giusti per te. Di seguito trovi cose realistiche che fanno i clienti, con il tipo di prompt che digiteresti e gli strumenti che l'assistente usa dietro le quinte.

{% hint style="info" %}
Funzionano allo stesso modo in Claude Code, Gemini CLI e Codex: i prompt sono in linguaggio naturale, non comandi.
{% endhint %}

## Gestire la coda di lavoro

> *"Quanti documenti sono in attesa di validazione e di che tipo sono?"*

Utilizza `get_pending_documents_count`, `get_pending_tasks_detail`, `get_top_document_types`. L'assistente riepiloga gli arretrati e può approfondire qualsiasi documento.

> *"Mostrami le fatture andate in errore oggi e spiegami perché."*

Utilizza `search_documents` / `query_document_dashboard` + `get_document_logs` per trovare i documenti in errore e spiegare il problema a partire dai log.

## Trovare e ispezionare un documento

> *"Apri la fattura INV-2026-00231 e mostrami i campi estratti e le righe."*

Utilizza `get_document_by_name`, `get_extracted_fields`, `get_extracted_tables`. L'assistente restituisce i dati di intestazione e la tabella e, se vuoi vedere l'originale, può recuperare l'immagine della pagina con `get_page_image`.

> *"Cerca tutti i documenti del fornitore 'ACME GmbH' del mese scorso con importo superiore a 10.000 €."*

Utilizza `search_documents` / `query_document_dashboard` con filtri per campo.

## Correggere e approvare

> *"Sul documento 84213 imposta il numero d'ordine su 4500098123 e la data di scadenza su 2026-07-15, poi validalo."*

Utilizza `update_document_fields` e poi `validate_document`. L'assistente segnala eventuali errori di validazione, così puoi correggerli.

> *"Valida ed esporta il documento 84213 nell'ERP, ma mostrami prima l'anteprima di esportazione."*

Utilizza `get_export_preview` e poi `validate_and_export` una volta che hai confermato.

## Correggere l'estrazione di una tabella

> *"Nella tabella delle righe di questa bolla di consegna mancano due righe: riestraila con l'AI, nascondi la colonna *Charges* e conserva questa impostazione per questo fornitore."*

Utilizza `extract_table_ai` per rieseguire la tabella AI sul documento, `apply_ai_table_formatting` per nascondere la colonna e `save_table_training_rules` per memorizzare il risultato per il fornitore; la bolla di consegna successiva dello stesso fornitore viene estratta allo stesso modo. `get_extracted_tables` mostra la tabella finale. Utile per i documenti in cui l'estrazione basata su regole ha perso delle righe.

## Analisi e reportistica

> *"Dammi un riepilogo per la direzione di questo mese: andamento dei volumi, tasso touchless e i 5 tipi di documento principali."*

Utilizza `get_executive_summary`, `get_volume_trends`, `get_success_rates`, `get_top_document_types`. Ideale per un rapido aggiornamento alla direzione senza aprire la dashboard.

## Fatturazione elettronica (eDocs)

> *"Quali formati di fattura elettronica sono abilitati per noi e questo file ZUGFeRD viene estratto correttamente?"*

Utilizza `list_electronic_document_types` + `test_electronic_document`, poi `verify_electronic_documents` per confermare i campi estratti.

## Dati anagrafici e arricchimento dei fornitori

> *"Aggiungi un nuovo fornitore (nome, partita IVA, IBAN) ai dati anagrafici, poi riesegui la ricerca fornitore sul documento 84500."*

Utilizza `upsert_vendor_master_data` + `trigger_supplier_lookup`.

## Modifiche alla configurazione

> *"Abilita l'estrazione dei codici QR per la nostra organizzazione e conferma che la preferenza sia impostata."*

Utilizza `set_preference` (che svuota automaticamente la cache) + `get_preference` per confermare.

> *"Elenca i nostri tipi di documento e mostra le impostazioni dei campi di 'Invoice'."*

Utilizza `list_document_types` + `get_field_settings`.

## Stato di salute e diagnostica

> *"L'API DocBits e il worker di elaborazione funzionano correttamente in questo momento? Con quale utente sono collegato?"*

Utilizza `check_api_health`, `check_celery_health`, `get_current_user`.

---

## Suggerimenti

- **Sii preciso sul documento**: un ID o un nome file esatto è il modo più rapido; altrimenti l'assistente cercherà prima.
- **Chiedi un'anteprima prima di esportare**: `get_export_preview` ti consente di confermare il payload ERP prima che `validate_and_export` lo invii.
- **Si applicano le autorizzazioni**: l'assistente può fare solo ciò che il tuo utente DocBits o la tua chiave API è autorizzato a fare. Approvazioni ed esportazioni rispettano il tuo ruolo e le tue ACL.
- **Attenzione alla produzione**: l'MCP agisce su dati reali. Negli ambienti cliente/produzione preferisci azioni di lettura/anteprima e chiedi conferma prima di approvare, esportare o eliminare.
