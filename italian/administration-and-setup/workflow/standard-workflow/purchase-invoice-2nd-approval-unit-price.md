# Fattura di acquisto: seconda approvazione del prezzo unitario

Questa pagina descrive una **regola di esempio configurata**, non un comportamento attivo per tutte le fatture. Le seguenti stringhe tecniche identificano le condizioni e l’azione dell’esempio e restano in inglese.

## Condizioni dell’esempio

* **Document Type is Invoice**: limita il caso al tipo di documento fattura.
* **Document Status is Pending Second Approval**: richiede lo stato di seconda approvazione in attesa.
* **Document Field Invoice Sub Type is Equals Purchase Invoice**: verifica il sottotipo configurato.
* **Logic Unit Price in order confirmation Not Equals purchase order**: verifica la condizione di differenza del prezzo unitario tra conferma e ordine prevista dalla regola.

Controlla identificatori, campi e versione delle condizioni realmente presenti nel workflow. Il nome di una regola non dimostra che il confronto sia stato eseguito né che i valori estratti siano corretti.

## Azione dell’esempio

**Assign user from field Buyer Name, use user User as fallback** usa il campo `Buyer Name` per risolvere l’utente e l’utente `User` configurato come ripiego quando necessario. `User` è il valore dell’esempio, non la promessa di un amministratore predefinito. Verifica validità dell’utente, stato del documento e log dell’azione.

L’assegnazione del documento non crea da sola un’attività e non esegue la seconda approvazione. I passaggi successivi dipendono dal workflow configurato.

## Prova consigliata

In un ambiente autorizzato verifica un caso con differenza di prezzo, uno senza differenza e uno con destinatario non risolvibile. Controlla condizioni, assegnazione e percorso di ripiego separatamente. La regola può supportare la revisione, ma non garantisce precisione dei dati, assenza di frodi o conformità del processo. Questa revisione documentale non ha eseguito la regola.
