# Buone pratiche

## Mantieni le colonne predefinite per importi e quantità

I controlli sulle voci di riga (*quantità × prezzo unitario = totale riga*) e il PO matching cercano le colonne predefinite `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Se invece crei colonne personalizzate per questi valori, i controlli non vengono eseguiti e il PO matching segnala colonne obbligatorie mancanti. Rinomina il *titolo* se la dicitura non ti convince; mantieni la colonna.

## Nascondi, non eliminare

Le colonne predefinite che non ti servono vanno nascoste, non eliminate; in ogni caso non possono essere eliminate. Anche per le colonne personalizzate, nascondere è la scelta più sicura finché non sei certo che nessuno script o mappatura di esportazione faccia ancora riferimento alla colonna.

## Contrassegna come obbligatorio solo ciò che blocca l'esportazione

Ogni colonna obbligatoria deve essere compilata in ogni riga prima che un utente possa approvare il documento. Usa il flag per i valori che l'ERP rifiuta se mancano (ad esempio il centro di costo in un'esportazione contabile), non per valori semplicemente utili.

## Usa *Sola lettura* per i valori provenienti da una ricerca

I valori che uno script o una ricerca nei dati master scrive nella tabella (descrizione articolo dall'anagrafica articoli, codice imposta dal fornitore) dovrebbero essere in sola lettura, così gli utenti correggono l'origine invece della copia.

## Usa l'AI per colonna, non per fornitore

Per un fornitore con regole addestrate, la maggior parte delle colonne viene estratta correttamente dalle regole. Se una colonna è inaffidabile (descrizioni lunghe che vanno a capo, uno sconto che a volte si trova in una posizione diversa), imposta *Usa AI* solo su quella colonna. Le regole continuano a gestire il resto.

## Dai alle colonne nomi pensati per l'ERP, non per il documento

Il *Nome colonna* finisce nelle mappature di esportazione e negli script. `COST_CENTRE` è più facile da mappare di `KST` e non cambia quando un fornitore lo stampa in modo diverso.

## Fai una prova su un documento riavviato

Dopo una modifica, riavvia un documento esistente del tipo di documento e aprilo: la nuova colonna compare, quella nascosta è sparita, le celle obbligatorie sono evidenziate. Solo a quel punto rendi la modifica disponibile agli utenti.

## Una tabella per ogni struttura di voci di riga

Crea una seconda tabella solo quando un tipo di documento ha davvero due tabelle indipendenti (ad esempio le righe articolo e una tabella separata degli oneri). Le tabelle vuote in più compaiono su ogni documento di quel tipo.
