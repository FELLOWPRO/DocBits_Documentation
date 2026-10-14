# Quale percorso di estrazione è stato usato?

Alla domanda "Perché questa tabella appare così?" si risponde scoprendo _cosa_ ha fatto DocBits per questo documento: regole salvate, tabella AI, quale livello AI e dove qualcosa è andato storto. Questa pagina è la checklist che supporto e partner usano prima di modificare qualsiasi configurazione.

## 1. Guarda le schede nella schermata di validazione

Apri il documento e osserva le schede sopra la tabella delle voci di riga:

| Cosa vedi                                                          | Percorso                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Righe nella scheda **Tabella estratta**                            | Percorso basato su regole. Il fornitore ha una tabella addestrata; le righe provengono dalle regole di coordinate salvate e l'AI non è intervenuta (tranne che per le colonne contrassegnate _Usa AI_).                                                                   |
| Righe nella scheda **Tabella estratta dall'AI**, campo _Tag_ sotto | Percorso AI. Nessuna regola salvata ha trovato corrispondenza; l'estrazione AI della tabella ha prodotto le righe, usando il livello AI dell'organizzazione oppure il livello impostato per questo fornitore in _Altre impostazioni_ → _Modello AI basato sul fornitore_. |
| Tooltip _AI table not found_ sulla scheda AI                       | Il percorso AI è stato eseguito e non ha restituito nulla per questo documento.                                                                                                                                                                                           |
| Nessuna scheda della tabella                                       | Entrambe le impostazioni delle tabelle sono disattivate per l'organizzazione: nulla ha estratto la tabella.                                                                                                                                                               |
| _No line items yet_                                                | Il percorso è stato eseguito ma non ha trovato righe (nessun testo leggibile, nessuna tabella sulla pagina, oppure le regole non corrispondono a questo layout).                                                                                                          |

I campi di intestazione hanno un proprio indicatore di origine accanto al valore: _Extracted using AI_, _Learned from validated AI extraction_, _Extracted using saved rules (FELLOW\_KV2)_, _Extracted from electronic document_, _Calculated from vendor master data_. Questi indicatori descrivono il campo di intestazione, non la tabella.

## 2. Controlla la configurazione del fornitore

* **Impostazioni → Elaborazione del documento → Classificazione ed estrazione → Modello AI**: la tabella sotto il selettore elenca ogni fornitore con un modello memorizzato o un addestramento. Un fornitore in questo elenco con _dati di addestramento_ ha regole salvate; _reimposta i dati di addestramento_ le rimuove.
* **Impostazioni → Elaborazione del documento → Impostazioni OCR**: _Usa E-Text se disponibile_ e _Usa i dati AI per le tabelle_ cambiano il testo che l'estrazione vede. Un fornitore può sovrascrivere l'E-Text in _Altre impostazioni_ nella schermata di validazione.
* **Impostazioni → Impostazioni Globali → Tipi di Documento → Colonne della Tabella**: flag nascosta, obbligatoria e _Usa AI_. Una colonna nascosta non viene mai compilata; una colonna _Usa AI_ viene compilata dall'AI anche per i fornitori con regole.

## 3. Riproduci senza l'interfaccia (API / MCP)

Con accesso all'API o all'MCP puoi porre le stesse domande in modo programmatico:

| Domanda                                              | Strumento                                                                                                                                                                                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Questa tabella è stata prodotta dall'AI?             | `get_extracted_tables(doc_id)`: ogni tabella riporta `is_ai_table: true/false`.                                                                                                                                |
| Cosa danno le regole, cosa dà l'AI?                  | `get_table_extraction_report(doc_id, mode="nonai")` e di nuovo con `mode="ai"`: il report mostra la struttura configurata, le righe estratte e l'anteprima della pagina per ciascun percorso. Confronta i due. |
| Quali colonne sono configurate, con quali flag?      | `get_table_config(doc_type)`                                                                                                                                                                                   |
| Il livello AI fa differenza?                         | `compare_table_extraction_models(doc_id)`: esegue due livelli sullo stesso documento (richiede un documento con un numero fornitore).                                                                          |
| Ripetere l'estrazione su questo documento            | `extract_table_ai(doc_id)` (AI) oppure `restart_document(doc_id)` (intera pipeline).                                                                                                                           |
| Cosa ha registrato la pipeline per questo documento? | `get_document_logs(doc_id)`                                                                                                                                                                                    |

Gli strumenti del DocBits MCP sono descritti nella pagina DocBits MCP della documentazione (attualmente disponibile in inglese).

## 4. Leggi i log

**Impostazioni → Impostazioni Log** (registrazione delle attività) mostra gli eventi di tutti i servizi. Per una domanda sulla tabella:

* Filtra per nome file o ID del documento in _Cerca nei log_.
* Usa il filtro _Servizio_: l'estrazione vera e propria viene eseguita nel servizio di estrazione e nei worker Celery, non nel servizio `api`. Se vedi solo righe `api`, allarga il filtro.
* Un'esecuzione normale registra, nell'ordine: documento ricevuto → OCR / E-Text → classificazione → estrazione dei campi → estrazione della tabella (ricerca delle regole, poi AI quando nessuna regola corrisponde) → validazione → cambio di stato. Il passaggio mancante o che segnala un errore è quello da esaminare.

## 5. Decidi: configurazione, dati o bug

| Sintomo                                                                                     | Causa più probabile                                                                                             | Passo successivo                                                                                                          |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Tabella corretta per il fornitore A, sbagliata per il fornitore B, stesso tipo di documento | Per fornitore: B non ha regole, oppure ha regole vecchie che non corrispondono più al layout di B               | Addestra una volta la tabella di B (oppure elimina le regole di B in modo che subentri l'AI).                             |
| Tabella sbagliata per tutti i fornitori a partire da una certa data                         | Impostazione dell'organizzazione modificata (livello AI, estrazione strutturata, vision, colonne della tabella) | Confronta le impostazioni con la data della modifica; riavvia un documento per conferma.                                  |
| Stesso documento: percorso regole vuoto, percorso AI corretto                               | Le regole non corrispondono a questa variante di layout                                                         | Addestra di nuovo con questo documento, oppure elimina le regole.                                                         |
| Stesso documento: entrambi i percorsi vuoti                                                 | Nessun testo leggibile (scansione senza testo OCR, PDF solo immagine)                                           | Vista OCR nella schermata di validazione; abilita l'E-Text se il PDF ha un livello di testo; prova un'altra versione OCR. |
| Una colonna sbagliata su ogni riga, il resto corretto                                       | Mappatura delle colonne o flag _Usa AI_                                                                         | Impostazioni Colonne della Tabella; rimappa nell'addestramento della tabella.                                             |
| Righe mancanti alle interruzioni di pagina o dopo un subtotale                              | Layout che l'AI o le regole non hanno seguito                                                                   | Addestra la tabella con un documento di più pagine; aggiungi un tag come _"la tabella continua a pagina 2"_.              |
| Passaggio di estrazione assente nei log, documento bloccato in _running_                    | Infrastruttura (coda dei worker), non configurazione                                                            | Controlla le attività in sospeso (`get_pending_tasks_detail` tramite MCP) e contatta il supporto con l'ID del documento.  |

## Cosa inviare al supporto

* ID del documento e organizzazione
* Quale scheda contiene le righe (Tabella estratta / Tabella estratta dall'AI / nessuna) e il livello AI in uso
* Se il fornitore ha regole salvate e quando sono state salvate l'ultima volta
* Un documento di esempio in cui funziona e uno in cui non funziona, se li hai entrambi

## Pagine correlate

* [Risoluzione dei Problemi di Estrazione delle Tabelle](table-extraction-troubleshoot.md): qualità dell'estrazione, OCR, E-Text, messaggi sulla tabella
* [Campi di addestramento Linee/Tabella di addestramento](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/)
* [Tabella AI](../../../end-user-and-partner-section/end-user-section/ai-table/)
* [Impostazioni Log](../../../administration-and-setup/settings/log-settings/)
