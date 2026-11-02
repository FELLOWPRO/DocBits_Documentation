# Scopo e utilizzo

Una colonna della tabella è un campo della tabella delle voci di riga. Tutto ciò che DocBits fa con una tabella (estrazione, validazione, PO matching, esportazione) lavora sulle colonne configurate qui.

## Dove compare una colonna

| Dove | Cosa fa la colonna in quel punto |
|---|---|
| **Schermata di validazione** | Una colonna nella tabella delle voci di riga. Il *Titolo* è l'intestazione, il *Tipo di colonna* decide l'editor (importo, data, testo, sì/no). Le colonne nascoste non vengono mostrate. |
| **Addestramento della tabella** | Quando addestri la tabella di un fornitore, mappi ogni colonna rilevata su una delle colonne configurate qui. Solo le colonne configurate possono essere mappate. |
| **Estrazione AI della tabella** | L'AI compila le colonne configurate. Una colonna contrassegnata *Usa AI* viene compilata dall'AI anche per i fornitori con regole addestrate. |
| **Regole di validazione** | I controlli sulle voci di riga, come *quantità × prezzo unitario = totale riga*, vengono eseguiti sulle colonne predefinite `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO matching** | Richiede le colonne predefinite numero articolo, prezzo unitario, quantità e importo totale. Senza di esse il documento mostra *Line Item Table is missing Mandatory column for PO*. |
| **Esportazione** | Ogni colonna non nascosta fa parte dei dati delle voci di riga inviati all'ERP. La mappatura di esportazione fa riferimento al *Nome colonna*. |
| **Script** | Gli script leggono e scrivono le colonne tramite il *Nome colonna*, ad esempio `row["TOTAL_AMOUNT"]`. |

## Ambito

* Le colonne della tabella sono configurate **per tabella**, e una tabella appartiene a un **tipo di documento**. Le colonne delle fatture non influiscono sulle bolle di consegna.
* La configurazione è **per organizzazione**. Le sotto-organizzazioni la ereditano.
* Quali colonne vengono *compilate* per un determinato fornitore lo decide l'addestramento di quel fornitore o l'AI; la configurazione delle colonne stabilisce solo quali colonne esistono.

## Motivi tipici per modificare la configurazione

* Un valore specifico del cliente deve essere acquisito per ogni riga (centro di costo, numero di progetto, codice articolo interno) → aggiungi una colonna.
* Una colonna predefinita non viene mai usata e ingombra la schermata di validazione → nascondila.
* Una colonna deve essere sempre compilata prima dell'esportazione → contrassegnala come *Obbligatoria*.
* Un valore proviene dalla ricerca nell'ERP e non deve essere modificato dagli utenti → contrassegnala come *Sola lettura*.
* L'AI acquisisce una colonna meglio delle regole addestrate (ad esempio descrizioni a testo libero) → contrassegnala come *Usa AI*.

## Pagine correlate

* [Aggiungere una nuova colonna](adding-a-new-column.md)
* [Modifica ed eliminazione delle colonne](editing-and-deleting-columns.md)
* [Risoluzione dei Problemi di Estrazione delle Tabelle](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
