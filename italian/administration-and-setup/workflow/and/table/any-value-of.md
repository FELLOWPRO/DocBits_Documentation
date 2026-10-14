# Any Value of

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda DocBits viene utilizzata per validare se un valore qualsiasi in una colonna specifica di una tabella corrisponde a un pattern regex fornito. Se anche una sola voce nella colonna corrisponde al pattern, il workflow proseguirà, rendendola ideale per i casi d'uso in cui l'individuazione anche di una sola corrispondenza attiva i passaggi successivi del processo.

## **Funzionalità:**

* **Validazione del pattern regex:** Questa scheda verifica se un valore qualsiasi in una determinata colonna di una tabella corrisponde al pattern di espressione regolare fornito. La scheda si attiva e consente al workflow di proseguire se almeno una voce nella colonna soddisfa la condizione.
* **Operatore:** Gli utenti definiscono la colonna e specificano il pattern regex. La condizione disponibile include:
  * **Matches Regex Pattern:** Verifica che almeno un valore nella colonna specificata corrisponda al pattern regex.
* **Selezione di tabella e colonna:** Gli utenti specificano la tabella e la colonna che desiderano verificare per la corrispondenza con il pattern regex.

## **Utilizzo:**

Questa scheda è particolarmente utile negli scenari in cui una tabella contiene dati che potrebbero richiedere corrispondenze specifiche, come la validazione di indirizzi email, numeri di fattura o ID prodotto. Garantisce che i workflow procedano quando una voce pertinente corrisponde al pattern definito, senza la necessità di verificare ogni voce.

## **Scenario di esempio:**

* Un utente imposta la scheda per verificare le voci nella colonna "Email Address" della tabella "Customers", utilizzando un pattern regex per i formati email validi. Se almeno un indirizzo email nella colonna corrisponde al pattern, la scheda attiverà il passaggio successivo del workflow, garantendo che il sistema elabori la voce valida.

Utilizzando la scheda "Regex Pattern Matching", le organizzazioni possono automatizzare i workflow in base a validazioni dinamiche basate su pattern, semplificando i processi e garantendo che solo le voci pertinenti attivino ulteriori azioni.
