# All Value of

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda DocBits viene utilizzata per validare se **tutti i valori** in una colonna specifica di una tabella corrispondono a un pattern regex fornito. Affinché il workflow prosegua, ogni voce nella colonna deve soddisfare la condizione, rendendo questa scheda ideale per garantire coerenza e integrità dei dati in tutte le voci.

## **Funzionalità:**

* **Validazione del pattern regex:** Questa scheda verifica che **tutti i valori** in una colonna specificata di una tabella corrispondano al pattern di espressione regolare fornito. Il workflow procederà solo se ogni voce nella colonna soddisfa la condizione.
* **Operatore:** Gli utenti definiscono la colonna e specificano il pattern regex. La condizione disponibile include:
  * **Matches Regex Pattern:** Verifica che ogni valore nella colonna specificata corrisponda al pattern regex.
* **Selezione di tabella e colonna:** Gli utenti specificano la tabella e la colonna che desiderano verificare per la corrispondenza completa con il pattern regex.

## **Utilizzo:**

Questa scheda è ideale nei casi in cui è richiesta uniformità dei dati, come garantire che tutti i numeri di telefono, gli ID prodotto o altre voci di campo rispettino un formato specifico. Garantisce che i workflow procedano solo quando ogni voce pertinente è coerente con il pattern.

## **Scenario di esempio:**

* Un utente imposta la scheda per verificare la colonna "Phone Number" nella tabella "Contacts", utilizzando un pattern regex per validare i formati dei numeri di telefono. Se ogni voce di numero di telefono nella colonna corrisponde al pattern, la scheda attiverà il passaggio successivo del workflow, confermando la formattazione uniforme dei dati.

Utilizzando la scheda "All Values Regex Pattern Matching", le organizzazioni possono applicare standard rigorosi sui dati e migliorare l'accuratezza del workflow, garantendo che ogni voce in una colonna specificata soddisfi il formato richiesto prima di proseguire.
