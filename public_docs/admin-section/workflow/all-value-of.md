# Tutti i valori di

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa carta DocBits viene utilizzata per convalidare se **tutti i valori** in una colonna specifica di una tabella corrispondono a un pattern regex fornito. Affinché il flusso di lavoro continui, ogni voce nella colonna deve soddisfare la condizione, rendendo questa carta ideale per garantire la coerenza e l'integrità dei dati tra tutte le voci.

## **Funzionalità:**

* **Convalida del pattern regex:** Questa carta controlla che **tutti i valori** in una colonna specificata di una tabella corrispondano al pattern di espressione regolare fornito. Il flusso di lavoro procederà solo se ogni voce nella colonna soddisfa la condizione.
* **Operatore:** Gli utenti definiscono la colonna e specificano il pattern regex. La condizione disponibile include:
  * **Corrisponde al pattern regex:** Verifica che ogni valore nella colonna specificata corrisponda al pattern regex.
* **Selezione di tabella e colonna:** Gli utenti specificano la tabella e la colonna che desiderano controllare per le corrispondenze complete del pattern regex.

## **Utilizzo:**

Questa carta è ideale per i casi in cui è richiesta l'uniformità dei dati, come garantire che tutti i numeri di telefono, gli ID prodotto o altre voci di campo aderiscano a un formato specifico. Garantisce che i flussi di lavoro procedano solo quando ogni voce pertinente è coerente con il pattern.

## **Esempio di scenario:**

* Un utente imposta la carta per controllare la colonna "Numero di telefono" nella tabella "Contatti", utilizzando un pattern regex per convalidare i formati dei numeri di telefono. Se ogni voce del numero di telefono nella colonna corrisponde al pattern, la carta attiverà il passaggio successivo nel flusso di lavoro, confermando la formattazione uniforme dei dati.

Utilizzando la carta "Corrispondenza pattern regex di tutti i valori", le organizzazioni possono applicare rigorosi standard di dati e migliorare l'accuratezza del flusso di lavoro, garantendo che ogni voce in una colonna specificata soddisfi il formato richiesto prima di procedere.
