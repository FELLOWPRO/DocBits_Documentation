# Risoluzione dei problemi

## La nuova colonna non compare nella schermata di validazione

* Il documento è stato elaborato prima che la colonna fosse aggiunta. Le modifiche valgono per i documenti caricati o riavviati in seguito: **riavvia il documento** (Dashboard → menu del documento → Riavvia).
* La colonna è **Nascosta**. Controlla il flag nell'elenco Colonne della Tabella.
* La colonna è stata aggiunta a una **tabella diversa** da quella mostrata. La schermata di validazione mostra le tabelle del tipo di documento; confronta la colonna *Nome tabella*.
* Il documento non è del tipo di documento che hai configurato.

## La colonna c'è ma è sempre vuota

* Il fornitore ha **regole addestrate** e la nuova colonna non è mappata al loro interno. Apri uno dei documenti del fornitore nell'addestramento della tabella e mappa la colonna, oppure imposta *Usa AI* sulla colonna.
* Con l'estrazione AI il valore non è riconoscibile sul documento (nessuna intestazione, abbreviato, in un'altra lingua). Aggiungi un [tag della tabella AI](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) che indichi la colonna, oppure mappala nell'addestramento.

## "Column name already exists"

Nella tabella esiste già una colonna con lo stesso nome tecnico. Se non compare nell'elenco, si tratta di una colonna predefinita nascosta: il messaggio dice *Please activate it in Table Column settings*. Disattiva *Nascosta* su quella colonna invece di crearne una nuova.

## L'approvazione è bloccata da una colonna obbligatoria

Il messaggio sulla tabella indica il nome della colonna. Compila la cella in ogni riga oppure (se il valore non esiste su questo documento) togli la spunta a *Obbligatoria* per la colonna, riavvia il documento e riprova. Valuta se la colonna debba davvero essere obbligatoria (vedi [Buone pratiche](best-practices-2.md)).

## L'AI compila una colonna con il valore sbagliato

Caso tipico: `CHARGES` riceve il totale della riga, e ogni riga fallisce quindi il controllo del totale riga con *Line total does not match quantity x unit price (expected …, got …)*, perché gli oneri fanno parte della formula `quantità × prezzo unitario + oneri`.

* Togli la spunta a *Usa AI* sulla colonna se le regole addestrate la acquisiscono correttamente.
* Se il fornitore non ha regole, addestra la tabella una volta (addestramento della tabella) in modo che la colonna sia legata alla posizione corretta, oppure nascondi la colonna se il fornitore non stampa mai quel valore.
* Come ultima risorsa, *Salta la validazione della tabella* nelle Altre impostazioni del tipo di documento disattiva tutti i controlli sulla tabella per l'intero tipo di documento; la discrepanza non viene più rilevata, e nemmeno le colonne obbligatorie vuote.

## PO matching: "Line Item Table is missing Mandatory column"

Il PO matching richiede le colonne predefinite numero articolo, prezzo unitario, quantità e importo totale. Una di esse è nascosta o è stata sostituita da una colonna personalizzata. Rendi di nuovo visibile la colonna predefinita, oppure mappa il valore su di essa nell'addestramento della tabella.

## Uno script o un'esportazione fallisce dopo l'eliminazione di una colonna

Lo script o la mappatura di esportazione fa ancora riferimento al *Nome colonna* eliminato. Rimuovi il riferimento oppure aggiungi di nuovo la colonna con lo stesso titolo; il nome tecnico deriva dal titolo e torna a corrispondere.

## Dove cercare ancora

* [Risoluzione dei Problemi di Estrazione delle Tabelle](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): qualità dell'estrazione, OCR, E-Text
* [Campi di addestramento Linee/Tabella di addestramento](../../../../setup/document-training/training-line-fields-table-training/README.md)
