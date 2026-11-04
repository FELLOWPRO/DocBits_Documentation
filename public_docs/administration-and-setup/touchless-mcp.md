# Spiegare e migliorare Touchless con MCP

<!-- touchless-admin-video-v2-20261104:start -->
**Capitolo video (versione di verifica):** [Consultare indicatori con MCP](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/it.html#chapter=12).
<!-- touchless-admin-video-v2-20261104:end -->

Questi percorsi usano strumenti realmente offerti da DocBits MCP. Distinguete lettura e spiegazione dalle scritture. Controllate organizzazione, ruolo, tipo, periodo e data; non inventate prove mancanti.

<figure><img src="../.gitbook/assets/touchless-owned-po-price-it.png" alt="Vera vista italiana di un ordine fittizio creato su Dev: 10 × 9 = 90. È un confronto della fonte per la diagnosi MCP, non una schermata di un client MCP né prova di estrazione o elaborazione riuscita."><figcaption><p>Vera vista italiana di un ordine fittizio creato su Dev: 10 × 9 = 90. È un confronto della fonte per la diagnosi MCP, non una schermata di un client MCP né prova di estrazione o elaborazione riuscita.</p></figcaption></figure>

## Spiegare Touchless tramite MCP

> Spiega Pure Touchless, sola approvazione e tasso AP combinato per le fatture degli ultimi 30 giorni. Indica numeratore, denominatore, documenti in corso, esclusioni, filtri e data dei dati. Separa precisione di estrazione e automazione.

Usate `touchless_get_summary` con `period: "30d"` e `doc_type: "INVOICE"`. Per un sottoprocesso usate soltanto dimensioni e valori realmente restituiti da `touchless_list_segments`. Confrontate stessa organizzazione, tipo, periodo e segmento; leggete `data_as_of`.

**Controesempio verificato su Dev:** tre nuove fatture erano ancora `IN_PROGRESS`: `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0`, `official_touchless_rate.ap_pct: null`. Nessun tasso era ancora calcolabile. Non significa precisione 0 % o Touchless 100 %. Qui `eligible` nel riepilogo indica la popolazione KPI conclusa; una singola traccia può avere `eligible: true` e `bucket_final: false`.

Gli esempi usano strumenti MCP realmente disponibili e verificati su Dev. Valgono organizzazione e permessi dell’account collegato; non provano la disponibilità in altre interfacce o elenchi di strumenti consentiti. Gli identificatori tecnici restano invariati.

## Esaminare le discrepanze tramite MCP

> Verifica ordine, import e regole attive. Separa estrazione, copia vecchia, fonte errata e configurazione mancante. Non modificare ancora nulla.

1. Confrontate originale, `get_extracted_fields` e `get_extracted_tables` prima di dichiarare corretta l’estrazione.
2. Usate `get_po_sync_status`, ad esempio `po_number: "TL20261104X1-PO02"`, `language: "en"`. Il riepilogo accetta `de` o `en`; spiegate la risposta in italiano. Il test conferma import elaborato e ordine presente, non correttezza aziendale né stato attuale di Infor.
3. Usate `touchless_get_document_trace` e `touchless_explain_po_match` con lo stesso `doc_id`. Leggete motore reale, versione attiva, colonne e tolleranze effettive. Per un cluster realmente restituito, passate il suo `issue_signature` a `touchless_get_po_match_evidence`.
4. Mantenete i limiti: il tipo di test restituiva `state: "none_published"`, `parse_error: "no published rule set"` e campi vuoti. Non erano provati blocchi di prezzo/quantità né abbinamenti riusciti. Un flusso generale non sostituisce tali controlli.
5. Correggete la causa confermata e verificate nuove fatture. Correzione o riavvio umano persistono dopo il successo; un errore ERP definitivo prevale come eccezione. I documenti in corso sono fuori dal denominatore.

Per il caso completo servono originale, estrazione precedente alle correzioni, valori importati/attuali e data, regole realmente applicate, azione AP ed esito finale. Le prove mancanti restano aperte.

## Leggere le prove con MCP

> Esamina questa fattura senza modificarla. Confronta originale, campi e tabelle attuali. Spiega le esecuzioni registrate e segnala le prove storiche mancanti.

| Strumento con lo stesso `doc_id` | Evidenza e limite |
| --- | --- |
| `get_extracted_fields` | Valori attuali e confidenza; non un’istantanea storica |
| `get_extracted_tables` | Tabelle e righe presenti; non la loro corrispondenza all’originale |
| `touchless_get_document_trace` | Esiti, interventi, fasi ed esecuzioni registrati |
| `touchless_explain_pipeline` | Spiegazione del percorso provato; non colma prove assenti |

**Controllo negativo reale:** fattura di test con `header_extraction: passed`, ma `extracted_field_count: 0`, otto campi obbligatori vuoti e nessuna tabella. La validazione bloccava con `REQUIRED_FIELD_MISSING`. Va verificata l’estrazione/configurazione: una fase verde non prova né estrazione corretta né blocco dovuto al prezzo dell’ordine.

### Un’azione MCP è un intervento umano?

Leggere non modifica la fattura. Altri strumenti possono scrivere, validare o riavviare. La classificazione dipende da evento e autore registrati: una chiave API può rappresentare un account di sistema. «Eseguito tramite MCP» non prova né intervento umano né Pure Touchless. Non usate un account di sistema per nascondere lavoro umano.

Controllate `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, stato finale ed esecuzioni. La sola approvazione è distinta da correzione salvata, validazione manuale o riavvio umano.

## Dare priorità ai fornitori e verificare i miglioramenti con MCP

> Ordina i fornitori che perdono più documenti Touchless. Separa errori di estrazione, discrepanze dei dati importati e impostazioni del processo. Proponi un’azione e una verifica per ogni causa confermata; non cambiare ancora nulla.

1. Usate `touchless_rank_supplier_opportunities` con `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. `search` cerca nome o numero; `limit` e `offset` paginano.
2. Passate il `supplier_key` restituito a `touchless_diagnose_supplier`. Usate `window: 30` per la situazione attuale o 90 per esaminare ricorrenze.
3. Passate un vero `issue_signature` a `touchless_get_issue_cluster`. Esaminate documenti e prove mancanti prima di confermare la causa. Non inventate identificatori.
4. `touchless_get_recommendations` spiega rimedi supportati. Il guadagno previsto è una stima; non sommate cluster sovrapposti.
5. Verificate nuove fatture comparabili e la misurazione successiva. Le fatture già trattate manualmente non diventano Pure retroattivamente.

Con estrazione corretta e ordini obsoleti correggete fonte/import. Se originale ed estrazione differiscono, verificate la configurazione di estrazione. La sola approvazione aziendale rimane AP Touchless dopo il successo. Una classifica vuota non prova assenza di problemi: le tre fatture di test in corso non producevano ancora esiti fornitore conclusi. Controllate filtri, data, identificazione del fornitore e volume concluso.

## Anteprima, applicazione e misurazione con MCP

> Spiega la causa confermata ed elenca proposte supportate. Mostra l’anteprima della modifica scelta e dei rischi. Applica soltanto quella modifica, quindi verifica valore salvato, storico ed effetto misurabile.

| Passo | Strumento e identificatori realmente restituiti | Risultato |
| --- | --- | --- |
| Elencare | `touchless_list_change_proposals`, opzionalmente `issue_signature`, `window: "30d"`, `lang: "it"` | Proposte presenti; nessuna impostazione salvata |
| Anteprima | `touchless_preview_change` con `proposal_id` e `issue_signature` restituiti | Ambito concreto e, se consentito, `preview_token` vincolato |
| Applicare la modifica scelta | `touchless_apply_change` con stessi ID, token, `overrides` e `window` | **Scrive** l’impostazione supportata; dopo successo restituisce `change_id` |
| Leggere l’effetto | `touchless_verify_change` con quel `change_id` e lo stesso `window` | Prima/dopo; servono ancora almeno 20 documenti conclusi idonei per periodo |

Copiate ID e token da risposte reali. L’anteprima di un valore non permette di applicarne un altro. Un’anteprima scaduta, vietata o incompleta non prova l’applicazione. La tabella spiega il percorso; non afferma che il caso dimostrativo abbia applicato una proposta o misurato un guadagno.

Dopo una correzione di configurazione confermata, verificate impostazione e nuove fatture. Passare dal 52 al 61 % sono 9 punti osservati, non prova di una causa unica. Un ordine Infor errato richiede correzione aziendale e import verificato: `touchless_apply_change` non è uno strumento generico di scrittura Infor. Non allargate le tolleranze per occultare dati errati.

Il report mostra stime, non applicazione o annullamento. L’applicazione richiede risposta di successo e voce nello storico. L’annullamento dipende dalla proposta: verificate il valore ripristinato. Ricaricare lo storico non applica modifiche; annullare non cancella gli interventi passati.

## Pagine correlate

* [Touchless Intelligence](touchless-intelligence.md)
* [Metriche e calcolo](touchless-metrics.md)
* [Usare il pannello](touchless-dashboard.md)
* [Esempi: prezzo e quantità](touchless-examples.md)
* [Touchless Intelligence: Diagnosi del fornitore e cluster di problemi](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Diagnosi dell'abbinamento ordini](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Tracciamento del documento](touchless-document-trace.md)
* [Touchless Intelligence: Proposte di modifica e report](touchless-change-proposals.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described. -->
<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
