# Classificazione ed estrazione

[AI Table](../../../../end-user-and-partner-section/end-user-section/ai-table/README.md) · [Structured Output per le tabelle](../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md)

## Quale impostazione funziona in quale fase del processo?

<figure><img src="../../../../.gitbook/assets/process-extraction-it-20261028.png" alt="Dal file ai dati riconosciuti: visualizza separatamente il tipo di documento, l'origine dei dati e il percorso di estrazione."><figcaption><p>Visualizza separatamente il tipo di documento, l'origine dei dati e il percorso di estrazione. Il diagramma è schematico; le impostazioni attive della tua organizzazione determinano il comportamento effettivo.</p></figcaption></figure>

La classificazione risponde alla domanda **"Che tipo di documento è questo?"**. L'estrazione risponde **"Che valori contiene?"**. Le impostazioni di questa pagina influiscono su punti diversi dell'elaborazione e non vanno intese come un unico interruttore AI.

1. **Preparare l'input:** per i PDF si può usare il testo esistente o l'OCR; i documenti elettronici supportati possono fornire valori strutturati. Una suddivisione attivata può separare un documento in arrivo in base ai criteri configurati di codice a barre o codice QR.
2. **Determinare il tipo di documento:** regole di classificazione e modelli assegnano i documenti a un tipo e, se necessario, a un sottotipo. Questa assegnazione va distinta dalla successiva estrazione di campi e tabelle.
3. **Estrarre i valori:** le tabelle possono seguire percorsi diversi a seconda della configurazione e delle regole salvate applicabili. I campi di intestazione hanno propri indicatori di origine. Il solo modello AI selezionato quindi non spiega ogni valore di riga o di campo.
4. **Tracciare il risultato:** nella schermata di convalida controlla quale scheda della tabella contiene le righe e quale indicatore di origine ha un campo di intestazione. Se manca una fase di elaborazione, leggi i log del documento prima di modificare le impostazioni.

### Distinguere tra percorso delle regole e percorso AI

Regole di tabella salvate e adeguate possono determinare l'estrazione della tabella per il template o il fornitore pertinente. Senza regole adatte si può usare il percorso AI, quando l'estrazione delle tabelle con AI è attivata. Singole colonne possono avere proprie opzioni AI. Un'origine AI per un campo di intestazione non significa che l'intera tabella provenga dall'AI.

La guida diagnostica [Quale percorso di estrazione è stato usato?](../../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md) spiega schede, identificatori di origine e protocolli. La pagina [Modello AI](ai-model.md) spiega lo standard dell'organizzazione e le sostituzioni legate al template.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-general-overview-en-20261030.png" alt="Classificazione ed estrazione con General, Classification Rules e AI Models, più Document Splitting e Document Processing"><figcaption><p>General contiene le impostazioni di elaborazione. AI Models è visibile qui perché il modulo è abilitato; i suoi modelli di classificazione personalizzati sono separati dal selettore del livello di estrazione. Il pattern del codice a barre memorizzato è oscurato.</p></figcaption></figure>
<!-- English source image: dbdc-193-general-overview-en-20261030.png -->

## Panoramica

Nelle impostazioni **Classification and Extraction** puoi:

* Controllare come vengono **suddivisi** i documenti caricati e quante pagine vengono elaborate
* Configurare la **formattazione degli importi** per il confronto degli importi
* Impostare l'**estrazione delle tabelle**, compreso il modello AI usato per ogni fornitore
* Attivare o disattivare l'elaborazione dei file **ZUGFeRD** non supportati
* Definire **regole di classificazione** che assegnano automaticamente un tipo di documento
* Esaminare i **AI Models** e le loro etichette addestrate

La pagina ha **General** e **Classification Rules**, più **AI Models** quando il modulo per modelli ed etichette è abilitato per la tua organizzazione. I modelli di classificazione personalizzati e le etichette in **AI Models** sono separati dal selettore del livello di estrazione sotto **General → Extraction**.

| Scheda | Contenuto |
|---|---|
| General | Document Splitting, Document Processing, Amount Formatting, Table Extraction, Electronic Document |
| Classification Rules | Regole regex che classificano i documenti in base al nome dell'origine |
| AI Models | Modelli addestrati su misura con le loro etichette, i tipi di documento e la priorità |

## Accedere alle impostazioni di Classification and Extraction

Vai su **Settings → Document Types → Classification and Extraction**.

## General

La scheda **General** raggruppa le impostazioni in sezioni comprimibili. La maggior parte dei controlli salva quando il valore cambia. Un **Barcode Pattern** non vuoto e modificato usa la sua azione di validazione/**Save**, e una modifica della versione di estrazione delle tabelle richiede conferma. Verifica l'organizzazione e il comportamento previsto prima di modificare un controllo.

### Document Splitting

**Split** decide se un documento caricato viene suddiviso in più documenti quando su una delle sue pagine compare un codice a barre. Il menu a discesa offre:

* **Do not split uploaded documents** – l'impostazione predefinita; il documento viene elaborato come un unico file.
* **Split by Barcode/QR-Code** – il documento viene suddiviso a ogni codice a barre rilevato.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-document-splitting-en-20261030.png" alt="Document Splitting con la suddivisione per codice a barre e codice QR, i tipi di codice a barre selezionati e il campo Barcode Pattern oscurato"><figcaption><p>Controlla il metodo di suddivisione e i tipi di codice a barre prima di modificarli. Il pattern specifico dell'organizzazione è oscurato; nessun valore è stato modificato.</p></figcaption></figure>
<!-- English source image: dbdc-193-document-splitting-en-20261030.png -->

Quando è selezionato **Split by Barcode/QR-Code**, compaiono altri due campi:

* **Barcode Type** – uno o più tipi di codice a barre da rilevare, per esempio *CODE-128* o *QR-CODE*.
* **Barcode Pattern** – una regex a cui il valore del codice a barre deve corrispondere perché la suddivisione venga attivata. Lascialo vuoto per suddividere su qualsiasi codice a barre dei tipi selezionati. Il pattern viene validato prima di essere memorizzato; un'espressione non valida viene segnalata subito.

Dopo una suddivisione riuscita il documento padre viene eliminato e le pagine proseguono come documenti separati che condividono lo stesso batch.

<figure><img src="../../../../.gitbook/assets/anatomy-barcode-split.svg" alt="Illustrazione isometrica di otto fogli in un vassoio con uno scanner che legge un codice a barre sul foglio 6. Dei separatori stanno davanti ai fogli 3 e 6 e dividono i fogli in tre documenti, e un elastico circonda l'intero vassoio."><figcaption><p>Esempio con il pattern <code>^INV\d{6}$</code>: i codici sui fogli 3 e 6 corrispondono e ciascuno avvia un nuovo documento, il codice sul foglio 4 non corrisponde e non suddivide nulla, e l'elastico rappresenta il batch che i documenti risultanti condividono.</p></figcaption></figure>

### Document Processing

**Pages to process** limita quante pagine vengono sottoposte a OCR, classificate ed estratte per documento.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-document-processing-en-20261030.png" alt="Document Processing con Pages to process impostato a 10 e la spiegazione che le pagine successive restano memorizzate e in sola lettura"><figcaption><p>Questo esempio ha un limite di 10 pagine elaborate. Il campo spiega che un valore vuoto o 0 significa tutte le pagine; il valore mostrato non è stato modificato.</p></figcaption></figure>
<!-- English source image: dbdc-193-document-processing-en-20261030.png -->

* Un valore vuoto o **0** significa che tutte le pagine vengono elaborate.
* Un numero *N* limita OCR, classificazione ed estrazione alle prime *N* pagine. Il documento completo viene comunque memorizzato, mostrato ed esportato; le pagine oltre il limite sono mostrate in sola lettura.

### Amount Formatting

Due interruttori controllano come gli importi vengono confrontati con i dati anagrafici e con gli ordini di acquisto.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-amount-formatting-en-20261030.png" alt="Amount Formatting con Allow Rounding During Amount Comparison e Require Exact Match for Amount Comparison"><figcaption><p>I due interruttori del confronto importi sono mostrati disattivati in questo esempio. Verifica la politica prevista prima di modificare uno dei due interruttori.</p></figcaption></figure>
<!-- English source image: dbdc-193-amount-formatting-en-20261030.png -->

* **Allow Rounding During Amount Comparison** – se abilitato, è ammessa una tolleranza di ±0.5. Se disabilitato, si applica ±0.05.
* **Require Exact Match for Amount Comparison** – se abilitato, gli importi devono corrispondere esattamente, senza tolleranza. Se disabilitato, si applica ±0.05.

Solo uno dei due interruttori può essere attivo alla volta; abilitarne uno disabilita l'altro.

### Table Extraction

{% hint style="info" %}
**Prerequisiti per un'estrazione delle tabelle funzionante**

* Il tipo di documento ha delle **colonne di tabella** (Settings → Document Processing → Document Types → [Table Columns](../../global-settings/document-types/table-columns/README.md)). Senza colonne non c'è nulla in cui estrarre.
* **Table Extraction** o **AI Table Extraction** è attivata qui sotto, per l'intera organizzazione.
* Il documento ha testo leggibile: l'OCR è stato eseguito oppure si usa l'E-Text per i PDF nativi digitali ([OCR Settings](../ocr-settings.md)).
* Addestramento e modelli AI sono **per fornitore**. Una tabella addestrata vale solo per i documenti del fornitore su cui è stata addestrata.
{% endhint %}

Puoi estrarre tabelle dai documenti abilitando **Table Extraction** oppure **AI Table Extraction**. Una tabella addestrata (basata sull'AI o manuale) è sempre collegata a un fornitore specifico.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-table-extraction-en-20261030.png" alt="Controlli di estrazione per l'estrazione delle tabelle con regole e con AI, vision mode, estrazione strutturata, campi nascosti e selettore del modello AI"><figcaption><p>Il selettore del livello di estrazione si trova in General → Extraction. Sotto è mostrata l'intestazione della tabella delle sostituzioni per fornitore; i dati delle righe esistenti sono oscurati e nessuna impostazione è stata modificata.</p></figcaption></figure>
<!-- English source image: dbdc-193-table-extraction-en-20261030.png -->

**Table Extraction:** attiva l'estrazione delle tabelle basata su regole. Le tabelle vengono addestrate per fornitore nella schermata di convalida (*Go to table extraction view*).\
Maggiori informazioni sull'addestramento [qui](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**AI Table Extraction:** usa l'AI per estrarre la tabella di qualsiasi fornitore senza addestramento. Se i risultati per un fornitore non sono abbastanza accurati, addestra la tabella di quel fornitore; le regole salvate hanno quindi la precedenza sull'AI per quel fornitore.

**Use Table Extraction Vision (AI):** scegli l'input per l'estrazione delle tabelle con AI da un menu a discesa a quattro modalità. È una selezione di modalità, non un interruttore separato acceso/spento. La modifica della modalità selezionata salva subito l'impostazione:

* **Off (text only)** – viene usato solo il testo OCR.
* **Images only** – viene letta solo l'immagine della pagina.
* **Hybrid (text and images)** – livello di testo e immagine della pagina vengono combinati nella stessa richiesta.
* **Auto (decided per document)** – DocBits sceglie per ogni documento l'input solo testo oppure ibrido.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-3-four-vision-options-en-20261031.png" alt="Menu Vision inglese attuale con Off (text only), Images only, Hybrid (text and images) e Auto (decided per document)"><figcaption><p>Le quattro modalità di input nel menu Dev inglese attuale. Il menu è stato aperto e chiuso senza selezionare un'altra modalità; nessuna estrazione è stata eseguita.</p></figcaption></figure>
<!-- English source image: dbdc-3-four-vision-options-en-20261031.png -->

**Use Structured Extraction (AI):** l'interruttore imposta il valore predefinito dell'output strutturato per l'organizzazione. Le colonne richieste dipendono dalla selezione Use AI a tre stati; contano anche le sostituzioni del template e l'addestramento del fornitore. Leggi la guida completa su [configurazione, anteprima ed esempio](../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md) per Structured Output per le tabelle.

**Table Extraction for Costing Element:** se abilitata, DocBits può estrarre gli elementi di costo dalle tabelle a livello di riga e classificarli di conseguenza.\
Spiegazione dettagliata disponibile [qui](table-extraction-for-costing-element.md).

**Auto Extract Tax Code:** se abilitata, il sistema compila automaticamente il campo **Tax Code** nella schermata di convalida, a condizione che sia configurato un campo per il codice fiscale.\
Maggiori informazioni su questa impostazione [qui](auto-extract-tax-code.md).

**Save extraction rules (Admin only):** solo gli amministratori possono fare clic su *Save Rules* nell'addestramento della tabella. Attivala quando gli utenti continuano a salvare regole che compromettono l'estrazione di un fornitore.

**Extract hidden fields:** vengono estratti anche i campi contrassegnati come nascosti nelle impostazioni dei campi. Usala quando un valore serve per una regola o per un export ma non deve essere mostrato nella schermata di convalida.

**AI Model:** imposta il modello dell'organizzazione per l'estrazione di campi e tabelle. Il menu offre Full, Fast, Nexus, Nexus Flash, Auto e Auto Nexus. Verifica disponibilità, qualità, durata e costi con documenti rappresentativi. Un livello non è sempre il più accurato o il più veloce per ogni documento. Le sostituzioni del template possono sostituire l'impostazione dell'organizzazione. La tabella sotto il selettore mostra:

* quali **fornitori** usano quale modello AI
* se usano l'estrazione strutturata (AI) e l'E-Text
* le opzioni per eliminare una voce e reimpostare così il fornitore al valore predefinito

Questa impostazione è spiegata in dettaglio [qui](ai-model.md).

#### Perché la tabella appare diversa da fornitore a fornitore?

L'elaborazione della tabella dipende dalle regole e dalle impostazioni salvate nel contesto del fornitore o del template pertinente:

* **Regole salvate** (addestramento della tabella): posizione della tabella e mappatura delle sue colonne sul layout di quel fornitore.
* **Tag della tabella AI e regole di formattazione**: i suggerimenti che l'utente ha salvato per la tabella AI di quel fornitore.
* **Modello AI specifico del template:** la selezione effettuata nella schermata di convalida viene salvata per organizzazione e template di estrazione corrente. Non cambia automaticamente ogni template dello stesso fornitore. Senza una sostituzione si usa l'impostazione dell'organizzazione applicabile.

Quindi il fornitore A con regole salvate mostra una tabella deterministica nella scheda *Extracted table* della schermata di convalida, mentre il fornitore B senza regole riceve la *AI Extracted table*. Per far comportare il fornitore B come A, addestra una volta la tabella di B. Per reimpostare un fornitore, elimina le sue regole nella schermata di convalida oppure reimposta i suoi dati di addestramento nella tabella di AI Model.

#### Chiavi delle preferenze

Ogni interruttore di questa sezione viene memorizzato come preferenza dell'organizzazione. Usa la chiave quando imposti il valore tramite l'API (`/preferences/set_preference`), uno script o il DocBits MCP (`get_preference` / `set_preference`).

| Impostazione (etichetta UI) | Chiave della preferenza | Valori |
|---|---|---|
| Split | `SPLIT_DOCUMENT_ON_BARCODE` | `true` / `false` |
| Barcode Type | `SPLIT_DOCUMENT_BARCODE_TYPE` | elenco dei nomi dei tipi di codice a barre |
| Barcode Pattern | `SPLIT_DOCUMENT_BARCODE_PATTERN` | stringa regex |
| Pages to process | `RESTRICT_TO_PAGES` | numero; vuoto o `0` = tutte le pagine |
| Allow Rounding During Amount Comparison | `AMOUNTS_ROUNDING` | `true` / `false` |
| Require Exact Match for Amount Comparison | `AMOUNTS_NO_ROUNDING` | `true` / `false` |
| Table Extraction | `TABLE_EXTRACTION_SETTING` | `true` / `false` |
| AI Table extraction | `USE_AI_TABLE_EXTRACTION` | `true` / `false` |
| Use Table Extraction Vision (AI) | `TABLE_EXTRACTION_VISION_MODE` | `off`, `vision`, `hybrid`, `auto`; se non impostata, la modalità è determinata dalla preferenza legacy |
| Use Table Extraction Vision (AI) – legacy switch | `TABLE_EXTRACTION_USE_VISION` | `true` / `false`; significa di fatto `vision` |
| Use Structured Extraction (AI) | `USE_STRUCTURED_EXTRACTION` | `true` / `false` |
| Table extraction for costing element | `CHARGES_TABLE_EXTRACTION` | `true` / `false` |
| Auto extract tax code | `AUTO_EXTRACT_TAX_CODE` | `true` / `false` |
| Save extraction rules (Admin only) | `ONLY_ADMIN_CAN_SAVE_RULES` | `true` / `false` |
| Extract hidden fields | `EXTRACT_HIDDEN_FIELDS` | `true` / `false` |
| AI Model | `AI_MODEL` | `gpt-6-sol` (Full), `gpt-6-luna` (Fast), `qwen3.8-max` (Nexus), `glm-5.3-flash` (Nexus Flash), `auto` (Auto), `auto-nexus` (Auto Nexus) |
| Table extraction version (confirmation dialog) | `TBL_EXT_VERSION` | stringa di versione |
| OCR Settings → Use AI data for tables if available | `USE_AI_DATA_FOR_TABLE` | `true` / `false` |
| OCR Settings → Use E-Text if available | `USE_ETEXT_IF_AVAILABLE` | `true` / `false` |

Note:

* Le preferenze booleane vengono memorizzate come stringhe `true` / `false`. Una chiave non impostata usa il valore predefinito di quell'impostazione; l'interfaccia mostra **Extract hidden fields** come attivo quando non è impostato. Non dare per scontato che ogni chiave assente significhi false. Se invii `1` o `0`, DocBits memorizza `true` / `false`.
* `AI_MODEL` non impostato significa **Fast**.
* Un `TABLE_EXTRACTION_VISION_MODE` non impostato viene risolto dal vecchio interruttore `TABLE_EXTRACTION_USE_VISION`: `true` dà `vision`, qualunque altro valore dà `off`.
* La modifica di una chiave ha effetto sui documenti elaborati in seguito. Riavvia un documento per estrarlo di nuovo con la nuova impostazione.
* Le sostituzioni del template differiscono dalle preferenze dell'organizzazione. La guida su AI Model spiega l'ambito esatto.

### Electronic Document

**Process Unsupported ZUGFeRD PDF:** se abilitata, le versioni **ZUGFeRD** non supportate vengono elaborate come PDF standard e l'XML incorporato viene ignorato.

L'elenco delle versioni **ZUGFeRD** supportate è disponibile [qui](../../global-settings/document-types/edi/zugferd/README.md).

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-electronic-document-en-20261030.png" alt="Electronic Document con l'interruttore Process Unsupported ZUGFeRD PDF"><figcaption><p>Electronic Document contiene l'opzione per i PDF ZUGFeRD non supportati. Lo stato mostrato è un'impostazione esistente; per questa cattura non è stata eseguita alcuna elaborazione di documenti.</p></figcaption></figure>
<!-- English source image: dbdc-193-electronic-document-en-20261030.png -->

## Classification Rules

La scheda **Classification Rules** elenca le regole che assegnano automaticamente un tipo di documento durante l'elaborazione. Ogni regola confronta un **pattern regex** con il nome dell'origine del documento e, in caso di corrispondenza, imposta il tipo di documento e facoltativamente un sottotipo di documento.

Passa alla scheda facendo clic su **Classification Rules** in cima alla pagina.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-rules-list-en-20261030.png" alt="Classification Rules con Search by column, Add e le intestazioni della tabella delle regole"><figcaption><p>Cerca regole esistenti oppure scegli Add per preparare una regola. Le righe delle regole esistenti sono oscurate; non è un esempio di elenco vuoto.</p></figcaption></figure>
<!-- English source image: dbdc-193-rules-list-en-20261030.png -->

La tabella ha una riga per regola con queste colonne:

* **Type** – dove viene applicato il pattern. Esistono due tipi: **Barcode** e **E-Mail**.
* **Pattern** – la regex memorizzata per la regola.
* **Document Type** – il tipo di documento assegnato quando il pattern corrisponde.
* **Sub Document Type** – il sottotipo di documento assegnato quando il pattern corrisponde.
* **Sub Organization** – la sotto-organizzazione a cui la regola è limitata. Vuoto significa che la regola vale per tutte le sotto-organizzazioni.
* **Actions** – il menu della riga con *Edit* e *Delete*.

Il campo di ricerca sopra la tabella filtra tutte le colonne, comprese le etichette mostrate delle colonne a discesa.

### Aggiungere una nuova regola di classificazione

1.  Fai clic su **Add** sopra la tabella.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-rule-add-en-20261030.png" alt="Finestra Configure classification Rule vuota con Pattern, Show help, Type, organizzazione, tipo di documento, Cancel e Save"><figcaption><p>Add apre questo modulo di regola vuoto. Controlla pattern e tipo di destinazione prima di Save; Cancel lo chiude senza creare una regola.</p></figcaption></figure>
    <!-- English source image: dbdc-193-rule-add-en-20261030.png -->
2. Compila i campi:
   * **Pattern** (obbligatorio) – la regex che la regola cerca.
   * **Type** (obbligatorio) – **Barcode** oppure **E-Mail**. Questo decide su quale nome di origine viene confrontato il pattern.
   * **Sub Organization** *(facoltativo)* – limita la regola a una sotto-organizzazione.
   * **Document Type** – il tipo di documento assegnato quando il pattern corrisponde.
   * **Sub Document Type** *(facoltativo)* – un tipo più specifico; l'elenco dipende dal tipo di documento selezionato. Cambiando il tipo di documento si azzera il sottotipo di documento.
3.  Fai clic su **Save**.

La finestra valida il pattern prima di salvare. Un pattern già usato da un'altra regola viene rifiutato con *Pattern already exists*; un pattern vuoto viene rifiutato con il messaggio di campo obbligatorio.

#### Guida per il pattern

L'interruttore **Show help** sotto il campo del pattern apre un riferimento in linea con i formati del nome di origine su cui viene confrontato il pattern:

* **O365** – `Shared Email + Folder › Shared Email › Folder › Email › Id`
* **Gmail** – `Email + Folder › Folder › Email › Id`

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-rule-pattern-help-en-20261030.png" alt="Guida per il pattern con i formati del nome di origine O365 e Gmail, esempi di espressioni regolari e suggerimenti di corrispondenza"><figcaption><p>Show help spiega quale nome di origine viene confrontato con la regex. Il riferimento e gli esempi sono mostrati senza inserire o salvare una regola.</p></figcaption></figure>
<!-- English source image: dbdc-193-rule-pattern-help-en-20261030.png -->

Esempi riportati nel pannello:

* `.*@acme\.de.*` – qualsiasi origine da quella casella
* `^ap@acme\.de:.*` – una casella specifica, qualsiasi cartella

Suggerimento: usa `^` / `$` come àncore per corrispondenze esatte, esegui l'escape dei punti come `\.` e usa `:` come separatore dei campi. Vince il primo insieme di campi presente nel nome di origine.

Se usi il tipo **E-Mail**, il pattern viene confrontato con i nomi della casella e delle cartelle della posta importata, non con il contenuto del documento.

### Modificare una regola di classificazione

1.  Fai clic sui tre punti nella colonna **Actions** della regola che vuoi modificare.
2.  Seleziona **Edit**. La finestra si apre con i valori attuali della regola.
3. Apporta le modifiche al pattern, al tipo, alla sotto-organizzazione, al tipo di documento o al sottotipo di documento.
4.  Fai clic su **Save**.

Vale la stessa validazione dell'aggiunta: il pattern non deve essere vuoto e non deve duplicare il pattern di un'altra regola.

### Eliminare una regola di classificazione

1. Fai clic sui tre punti nella colonna **Actions**.
2. Seleziona **Delete**.

La regola viene rimossa subito dall'elenco. Eliminare una regola non modifica i documenti già classificati con essa.

## AI Models

La scheda **AI Models** mostra i modelli addestrati su misura disponibili per la classificazione dei documenti e le loro etichette. Compare solo quando il modulo per modelli ed etichette è abilitato per la tua organizzazione.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-193-ai-models-empty-en-20261030.png" alt="Scheda AI Models selezionata con No Record Found nell'organizzazione corrente"><figcaption><p>AI Models è una scheda facoltativa per modelli di classificazione ed etichette personalizzati. In questa organizzazione la lettura riuscita dell'elenco non ha restituito modelli; questo non descrive l'impostazione del livello di estrazione.</p></figcaption></figure>
<!-- English source image: dbdc-193-ai-models-empty-en-20261030.png -->

Se per l'organizzazione non è disponibile alcun modello personalizzato, la scheda mostra *No Record Found!*.

### Modelli

Ogni modello è una voce espandibile con:

* il **nome del modello** e un badge **Default** sul modello usato quando non se ne applica nessun altro;
* il numero di **etichette** addestrate per quel modello;
* per ogni modello, una volta espanso: **Type**, **First page only** e **Version**.

Sotto queste informazioni sono elencate le etichette del modello.

### Etichette

Le etichette sono ciò che il modello apprende. Ogni etichetta mappa un pattern riconosciuto dal modello su un tipo di documento.

* **Name** – il nome dell'etichetta.
* **Next model** – un modello che continua l'elaborazione dell'output di questa etichetta.
* **DOC TYPE** – il tipo di documento assegnato dall'etichetta.
* **Sub Document Type** – un tipo più specifico per l'etichetta.
* **Priority** – l'ordine in cui le etichette vengono valutate; prima i numeri più bassi.

Il campo di ricerca sopra la tabella delle etichette filtra le etichette del modello selezionato.

### Modificare un'etichetta

Fai clic sull'icona a forma di penna su una riga di etichetta per aprire la finestra di modifica. Offre **Next model** e **Document Type**; impostane uno, perché la finestra richiede un modello successivo oppure un tipo di documento. Fai clic su **Save** per applicare la modifica.

## Pagine correlate

* [AI Model](ai-model.md) – i sei livelli di estrazione e come un fornitore ottiene un proprio modello
* [Auto Extract Tax Code](auto-extract-tax-code.md)
* [Table Extraction for Costing Element](table-extraction-for-costing-element.md)
* [OCR Settings](../ocr-settings.md)

<figure><img src="../../../../.gitbook/assets/structured-output-settings-it-20261104.png" alt="Controlli di estrazione attuali. Structured Output è disattivato in questa configurazione esistente, quindi non viene mostrata alcuna anteprima dello schema. Nessuna impostazione di estrazione è stata modificata."><figcaption><p>Controlli di estrazione attuali. Structured Output è disattivato in questa configurazione esistente, quindi non viene mostrata alcuna anteprima dello schema. Nessuna impostazione di estrazione è stata modificata.</p></figcaption></figure>
