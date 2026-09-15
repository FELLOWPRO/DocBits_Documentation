# Colonne della Tabella

Le colonne della tabella definiscono quali colonne ha la tabella delle voci di riga di un tipo di documento: cosa DocBits estrae in ogni colonna, cosa vede l'utente nella schermata di validazione e cosa viene inviato all'ERP in fase di esportazione.

**Dove:** Impostazioni → Impostazioni Globali → Tipi di Documento → Colonne della Tabella

<figure><img src="../../../../.gitbook/assets/table-columns_list.png" alt="Elenco Colonne della Tabella con i flag Obbligatoria, Sola lettura, Nascosta e Usa AI per ogni colonna"><figcaption><p>Colonne della Tabella: una riga per colonna, i flag si attivano direttamente nell'elenco</p></figcaption></figure>

## Cosa vedi

Ogni riga è una colonna di una tabella. L'elenco mostra:

| Colonna | Significato |
|---|---|
| **Nome colonna** | Nome tecnico, generato dal titolo (maiuscole, trattini bassi). Viene usato negli script, nelle mappature di esportazione e nell'API. Non può essere modificato in seguito. |
| **Titolo** | Etichetta mostrata nella schermata di validazione. Si modifica con l'icona di traduzione nella colonna *Azioni* (*Aggiorna chiave di traduzione*). |
| **Tipo di colonna** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` o `CURRENCY`. Determina la validazione e la formattazione. |
| **Nome tabella** | La tabella a cui appartiene la colonna, ad esempio `INVOICE_TABLE`. |
| **Obbligatoria** | Il documento non può essere approvato finché questa colonna è vuota in una qualsiasi riga. |
| **Sola lettura** | Gli utenti vedono il valore ma non possono modificarlo. |
| **Nascosta** | La colonna non viene né mostrata né esportata. Serve per disattivare le colonne predefinite che non ti servono. |
| **Usa AI** | L'estrazione AI della tabella compila questa colonna, anche quando il fornitore ha regole addestrate. |
| **Azioni** | Icona di traduzione: rinomina il titolo. Icona info: da dove proviene l'etichetta mostrata (la tua traduzione, il valore predefinito, la chiave). Menu a tre punti: *Elimina*, solo per le colonne create dalla tua organizzazione; le colonne predefinite possono solo essere nascoste. |

Sopra l'elenco ci sono due pulsanti:

* **Crea nuova tabella**: una seconda tabella di voci di riga per il tipo di documento (ad esempio una tabella degli oneri accanto alla tabella degli articoli).
* **Aggiungi nuova colonna della tabella**: apre la finestra di dialogo descritta in [Aggiungere una nuova colonna](#aggiungere-una-nuova-colonna).

## Colonne predefinite e colonne personalizzate

Ogni tipo di documento viene fornito con un set di colonne predefinite (per le fatture: numero articolo, descrizione, quantità, prezzo unitario, importo totale, imposta, …). Appartengono a DocBits, non alla tua organizzazione, quindi non possono essere eliminate: nascondile invece. Le colonne che aggiungi tu appartengono alla tua organizzazione e possono essere eliminate.

{% hint style="info" %}
**Le modifiche valgono solo per i nuovi documenti.** Una colonna che aggiungi, nascondi o elimini compare sui documenti caricati o riavviati dopo la modifica. I documenti già presenti nella dashboard mantengono la tabella così come è stata estratta. Riavvia un documento per applicare la nuova configurazione.
{% endhint %}

## Scopo e utilizzo

Una colonna della tabella è un campo della tabella delle voci di riga. Tutto ciò che DocBits fa con una tabella (estrazione, validazione, PO matching, esportazione) lavora sulle colonne configurate qui.

### Dove compare una colonna

| Dove | Cosa fa la colonna in quel punto |
|---|---|
| **Schermata di validazione** | Una colonna nella tabella delle voci di riga. Il *Titolo* è l'intestazione, il *Tipo di colonna* decide l'editor (importo, data, testo, sì/no). Le colonne nascoste non vengono mostrate. |
| **Addestramento della tabella** | Quando addestri la tabella di un fornitore, mappi ogni colonna rilevata su una delle colonne configurate qui. Solo le colonne configurate possono essere mappate. |
| **Estrazione AI della tabella** | L'AI compila le colonne configurate. Una colonna contrassegnata *Usa AI* viene compilata dall'AI anche per i fornitori con regole addestrate. |
| **Regole di validazione** | I controlli sulle voci di riga, come *quantità × prezzo unitario = totale riga*, vengono eseguiti sulle colonne predefinite `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO matching** | Richiede le colonne predefinite numero articolo, prezzo unitario, quantità e importo totale. Senza di esse il documento mostra *Line Item Table is missing Mandatory column for PO*. |
| **Esportazione** | Ogni colonna non nascosta fa parte dei dati delle voci di riga inviati all'ERP. La mappatura di esportazione fa riferimento al *Nome colonna*. |
| **Script** | Gli script leggono e scrivono le colonne tramite il *Nome colonna*, ad esempio `row["TOTAL_AMOUNT"]`. |

### Ambito

* Le colonne della tabella sono configurate **per tabella**, e una tabella appartiene a un **tipo di documento**. Le colonne delle fatture non influiscono sulle bolle di consegna.
* La configurazione è **per organizzazione**. Le sotto-organizzazioni la ereditano.
* Quali colonne vengono *compilate* per un determinato fornitore lo decide l'addestramento di quel fornitore o l'AI; la configurazione delle colonne stabilisce solo quali colonne esistono.

### Motivi tipici per modificare la configurazione

* Un valore specifico del cliente deve essere acquisito per ogni riga (centro di costo, numero di progetto, codice articolo interno) → aggiungi una colonna.
* Una colonna predefinita non viene mai usata e ingombra la schermata di validazione → nascondila.
* Una colonna deve essere sempre compilata prima dell'esportazione → contrassegnala come *Obbligatoria*.
* Un valore proviene dalla ricerca nell'ERP e non deve essere modificato dagli utenti → contrassegnala come *Sola lettura*.
* L'AI acquisisce una colonna meglio delle regole addestrate (ad esempio descrizioni a testo libero) → contrassegnala come *Usa AI*.

## Aggiungere una nuova colonna

Aggiungi una colonna quando per ogni voce di riga deve essere acquisito un valore che le colonne predefinite non coprono: un centro di costo, un numero di progetto, un codice articolo interno.

### Prima di iniziare

* Decidi a quale **tabella** appartiene la colonna. La maggior parte dei tipi di documento ha una sola tabella (ad esempio `INVOICE_TABLE`). Se l'elenco è vuoto, fai prima clic su **Crea nuova tabella**; la finestra di dialogo chiede solo il nome della tabella.
* Decidi il **tipo**: `AMOUNT` per gli importi, `NUMBER` per le quantità, `DATE`, `BOOLEAN` per sì/no, `CURRENCY` per un codice valuta ISO, `STRING` per tutto il resto. Il tipo non può essere modificato dopo il salvataggio.
* Verifica se esiste già una **colonna predefinita** con lo stesso significato ma nascosta. Le colonne nascoste compaiono nell'elenco con il flag *Nascosta* attivo: rendila di nuovo visibile invece di creare un duplicato.

### Passaggi

1. Apri **Impostazioni → Impostazioni Globali → Tipi di Documento → Colonne della Tabella**.
2. Fai clic su **Aggiungi nuova colonna della tabella**.

<figure><img src="../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Finestra di dialogo Aggiungi nuova colonna della tabella con Titolo, La colonna è obbligatoria, Seleziona tipo di colonna e Seleziona tabella"><figcaption><p>Aggiungi nuova colonna della tabella</p></figcaption></figure>

3. Compila la finestra di dialogo:

| Campo | Cosa inserire |
|---|---|
| **Titolo** | L'etichetta che l'utente vede nella schermata di validazione, ad esempio `Cost Centre`. Solo lettere e numeri. DocBits ne ricava il *Nome colonna* tecnico (`COST_CENTRE`). |
| **La colonna è obbligatoria?** | Spunta la casella quando il documento non deve essere approvato finché la colonna è vuota in una qualsiasi riga. |
| **Seleziona tipo di colonna** | Vedi l'elenco dei tipi qui sopra. |
| **Seleziona tabella** | La tabella che riceve la colonna. |

4. Fai clic su **Procedi**. La colonna compare nell'elenco con *Sola lettura*, *Nascosta* e *Usa AI* disattivati. Se necessario, attiva questi flag nell'elenco, vedi [Modifica ed eliminazione delle colonne](#modifica-ed-eliminazione-delle-colonne).

### Dopo l'aggiunta

* La colonna è **vuota sui documenti esistenti**. Viene compilata sui documenti caricati o riavviati dopo la modifica.
* Per i fornitori con **regole addestrate**, apri uno dei loro documenti nell'addestramento della tabella e mappa la nuova colonna, altrimenti la colonna resta vuota per quel fornitore. Vedi [Definizione Tabelle e Colonne](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Con l'**estrazione AI della tabella**, l'AI compila la colonna se il valore è riconoscibile sul documento. Contrassegna la colonna come *Usa AI* se il fornitore ha regole addestrate ma questa colonna deve comunque provenire dall'AI.
* Aggiungi la colonna alla **mappatura di esportazione** se l'ERP deve riceverla, vedi [Esportazione](../../document-processing/export.md).

### Messaggi

| Messaggio | Significato |
|---|---|
| *Column name already exists* | Nella tabella esiste già una colonna con questo nome tecnico. Scegli un titolo diverso. |
| *Column name already exists – Please activate it in Table Column settings* | Una colonna predefinita nascosta ha questo nome. Disattiva il suo flag *Nascosta* invece di crearne una nuova. |
| *No table exists. Please create table before creating columns.* | Il tipo di documento non ha ancora una tabella: fai prima clic su **Crea nuova tabella**. |

## Modifica ed eliminazione delle colonne

Tutto, tranne il titolo, si modifica direttamente nell'elenco; non esiste una finestra di modifica.

### Attivare o disattivare un flag

Spunta o togli la spunta alla casella nella riga. La modifica viene salvata immediatamente (*Successfully saved*).

| Flag | Attivo | Disattivo |
|---|---|---|
| **Obbligatoria** | L'approvazione è bloccata finché la colonna è vuota in una qualsiasi riga; la schermata di validazione evidenzia la cella. | Le celle vuote sono ammesse. |
| **Sola lettura** | Il valore viene mostrato ma non può essere sovrascritto. Usalo per i valori che provengono da una ricerca o da uno script. | Gli utenti possono modificare la cella. |
| **Nascosta** | La colonna scompare dalla schermata di validazione e dall'esportazione. I suoi dati vengono conservati. | La colonna viene mostrata ed esportata. |
| **Usa AI** | L'estrazione AI della tabella compila questa colonna, anche per i fornitori che hanno regole addestrate. | La colonna viene compilata dalle regole addestrate, oppure dall'AI quando non esistono regole. |

{% hint style="info" %}
I flag hanno effetto sui documenti caricati o riavviati **dopo** la modifica. I documenti aperti mantengono la tabella attuale finché non vengono riavviati.
{% endhint %}

### Rinominare il titolo

Fai clic sull'icona di traduzione nella colonna *Azioni* (*Aggiorna chiave di traduzione*), inserisci la nuova etichetta e conferma. L'icona info accanto mostra quale etichetta è attualmente in uso e da dove proviene. Cambia solo l'etichetta; il *Nome colonna* tecnico resta lo stesso, quindi script, mappature di esportazione e regole addestrate continuano a funzionare.

### Modificare il tipo o la tabella

Non è possibile. Nascondi la colonna (o eliminala se è una colonna personalizzata) e aggiungine una nuova con il tipo corretto.

### Eliminare una colonna

L'azione di eliminazione è disponibile solo per le colonne create dalla tua organizzazione. Le colonne predefinite non possono essere eliminate: nascondile.

1. Apri il menu a tre punti nella colonna *Azioni* e scegli **Elimina**. La voce non compare per le colonne predefinite.
2. Conferma.

Cosa succede:

* La colonna viene rimossa dalla configurazione. I documenti elaborati **da questo momento in poi** non la hanno più.
* I documenti già estratti mantengono la colonna e i suoi valori finché non vengono riavviati.
* Le regole addestrate che mappavano questa colonna continuano a funzionare per le altre colonne; la mappatura della colonna eliminata viene ignorata.
* Se la colonna è referenziata in una mappatura di esportazione o in uno script, rimuovi il riferimento; altrimenti l'esportazione o lo script fallisce con un errore di colonna mancante.

### Annullare un'eliminazione

Una colonna eliminata non può essere ripristinata dall'elenco. Aggiungila di nuovo con lo stesso titolo: il nome tecnico deriva dal titolo, quindi una colonna creata con lo stesso titolo riceve lo stesso *Nome colonna* e le mappature esistenti tornano a corrispondere.

## Buone pratiche

### Mantieni le colonne predefinite per importi e quantità

I controlli sulle voci di riga (*quantità × prezzo unitario = totale riga*) e il PO matching cercano le colonne predefinite `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Se invece crei colonne personalizzate per questi valori, i controlli non vengono eseguiti e il PO matching segnala colonne obbligatorie mancanti. Rinomina il *titolo* se la dicitura non ti convince; mantieni la colonna.

### Nascondi, non eliminare

Le colonne predefinite che non ti servono vanno nascoste, non eliminate; in ogni caso non possono essere eliminate. Anche per le colonne personalizzate, nascondere è la scelta più sicura finché non sei certo che nessuno script o mappatura di esportazione faccia ancora riferimento alla colonna.

### Contrassegna come obbligatorio solo ciò che blocca l'esportazione

Ogni colonna obbligatoria deve essere compilata in ogni riga prima che un utente possa approvare il documento. Usa il flag per i valori che l'ERP rifiuta se mancano (ad esempio il centro di costo in un'esportazione contabile), non per valori semplicemente utili.

### Usa *Sola lettura* per i valori provenienti da una ricerca

I valori che uno script o una ricerca nei dati master scrive nella tabella (descrizione articolo dall'anagrafica articoli, codice imposta dal fornitore) dovrebbero essere in sola lettura, così gli utenti correggono l'origine invece della copia.

### Usa l'AI per colonna, non per fornitore

Per un fornitore con regole addestrate, la maggior parte delle colonne viene estratta correttamente dalle regole. Se una colonna è inaffidabile (descrizioni lunghe che vanno a capo, uno sconto che a volte si trova in una posizione diversa), imposta *Usa AI* solo su quella colonna. Le regole continuano a gestire il resto.

### Dai alle colonne nomi pensati per l'ERP, non per il documento

Il *Nome colonna* finisce nelle mappature di esportazione e negli script. `COST_CENTRE` è più facile da mappare di `KST` e non cambia quando un fornitore lo stampa in modo diverso.

### Fai una prova su un documento riavviato

Dopo una modifica, riavvia un documento esistente del tipo di documento e aprilo: la nuova colonna compare, quella nascosta è sparita, le celle obbligatorie sono evidenziate. Solo a quel punto rendi la modifica disponibile agli utenti.

### Una tabella per ogni struttura di voci di riga

Crea una seconda tabella solo quando un tipo di documento ha davvero due tabelle indipendenti (ad esempio le righe articolo e una tabella separata degli oneri). Le tabelle vuote in più compaiono su ogni documento di quel tipo.

## Risoluzione dei problemi

### La nuova colonna non compare nella schermata di validazione

* Il documento è stato elaborato prima che la colonna fosse aggiunta. Le modifiche valgono per i documenti caricati o riavviati in seguito: **riavvia il documento** (Dashboard → menu del documento → Riavvia).
* La colonna è **Nascosta**. Controlla il flag nell'elenco Colonne della Tabella.
* La colonna è stata aggiunta a una **tabella diversa** da quella mostrata. La schermata di validazione mostra le tabelle del tipo di documento; confronta la colonna *Nome tabella*.
* Il documento non è del tipo di documento che hai configurato.

### La colonna c'è ma è sempre vuota

* Il fornitore ha **regole addestrate** e la nuova colonna non è mappata al loro interno. Apri uno dei documenti del fornitore nell'addestramento della tabella e mappa la colonna, oppure imposta *Usa AI* sulla colonna.
* Con l'estrazione AI il valore non è riconoscibile sul documento (nessuna intestazione, abbreviato, in un'altra lingua). Aggiungi un [tag della tabella AI](../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) che indichi la colonna, oppure mappala nell'addestramento.

### "Column name already exists"

Nella tabella esiste già una colonna con lo stesso nome tecnico. Se non compare nell'elenco, si tratta di una colonna predefinita nascosta: il messaggio dice *Please activate it in Table Column settings*. Disattiva *Nascosta* su quella colonna invece di crearne una nuova.

### L'approvazione è bloccata da una colonna obbligatoria

Il messaggio sulla tabella indica il nome della colonna. Compila la cella in ogni riga oppure (se il valore non esiste su questo documento) togli la spunta a *Obbligatoria* per la colonna, riavvia il documento e riprova. Valuta se la colonna debba davvero essere obbligatoria (vedi [Buone pratiche](#buone-pratiche)).

### L'AI compila una colonna con il valore sbagliato

Caso tipico: `CHARGES` riceve il totale della riga, e ogni riga fallisce quindi il controllo del totale riga con *Line total does not match quantity x unit price (expected …, got …)*, perché gli oneri fanno parte della formula `quantità × prezzo unitario + oneri`.

* Togli la spunta a *Usa AI* sulla colonna se le regole addestrate la acquisiscono correttamente.
* Se il fornitore non ha regole, addestra la tabella una volta (addestramento della tabella) in modo che la colonna sia legata alla posizione corretta, oppure nascondi la colonna se il fornitore non stampa mai quel valore.
* Come ultima risorsa, *Salta la validazione della tabella* nelle Altre impostazioni del tipo di documento disattiva tutti i controlli sulla tabella per l'intero tipo di documento; la discrepanza non viene più rilevata, e nemmeno le colonne obbligatorie vuote.

### PO matching: "Line Item Table is missing Mandatory column"

Il PO matching richiede le colonne predefinite numero articolo, prezzo unitario, quantità e importo totale. Una di esse è nascosta o è stata sostituita da una colonna personalizzata. Rendi di nuovo visibile la colonna predefinita, oppure mappa il valore su di essa nell'addestramento della tabella.

### Uno script o un'esportazione fallisce dopo l'eliminazione di una colonna

Lo script o la mappatura di esportazione fa ancora riferimento al *Nome colonna* eliminato. Rimuovi il riferimento oppure aggiungi di nuovo la colonna con lo stesso titolo; il nome tecnico deriva dal titolo e torna a corrispondere.

## Pagine correlate

* [Risoluzione dei Problemi di Estrazione delle Tabelle](../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): qualità dell'estrazione, OCR, E-Text
* [Campi di addestramento Linee/Tabella di addestramento](../../../setup/document-training/training-line-fields-table-training/README.md): insegna a DocBits dove si trova la tabella di un fornitore
* [Tabella AI](../../../../end-user-and-partner-section/end-user-section/ai-table/README.md): cosa vede l'utente nella schermata di validazione
