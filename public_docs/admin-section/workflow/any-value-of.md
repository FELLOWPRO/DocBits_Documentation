# Qualsiasi valore di

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa carta DocBits viene utilizzata per convalidare se un qualsiasi valore in una colonna specifica di una tabella corrisponde a un pattern regex fornito. Se una singola voce nella colonna corrisponde al pattern, il flusso di lavoro continuerà, rendendo questa carta ideale per i casi d'uso in cui l'identificazione anche di una singola corrispondenza attiva i passaggi successivi del processo.

## **Funzionalità:**

* **Convalida del pattern regex:** Questa carta controlla se un qualsiasi valore in una data colonna di una tabella corrisponde al pattern di espressione regolare fornito. La carta si attiverà e consentirà al flusso di lavoro di continuare se almeno una voce nella colonna soddisfa la condizione.
* **Operatore:** Gli utenti definiscono la colonna e specificano il pattern regex. La condizione disponibile include:
  * **Corrisponde al pattern regex:** Verifica che almeno un valore nella colonna specificata corrisponda al pattern regex.
* **Selezione di tabella e colonna:** Gli utenti specificano la tabella e la colonna che desiderano controllare per le corrispondenze del pattern regex.

## **Utilizzo:**

Questa carta è particolarmente utile per scenari in cui una tabella contiene dati che potrebbero richiedere corrispondenze specifiche, come la convalida di indirizzi e-mail, numeri di fattura o ID prodotto. Garantisce che i flussi di lavoro procedano quando una voce pertinente corrisponde al pattern definito, senza dover controllare ogni voce.

## **Esempio di scenario:**

* Un utente imposta la carta per controllare le voci nella colonna "Indirizzo e-mail" della tabella "Clienti", utilizzando un pattern regex per i formati e-mail validi. Se almeno un indirizzo e-mail nella colonna corrisponde al pattern, la carta attiverà il passaggio successivo del flusso di lavoro, assicurando che il sistema elabori la voce valida.

Utilizzando la carta "Corrispondenza pattern regex", le organizzazioni possono automatizzare i flussi di lavoro basati su convalide dinamiche basate su pattern, semplificando i processi e garantendo che solo le voci pertinenti attivino ulteriori azioni.
