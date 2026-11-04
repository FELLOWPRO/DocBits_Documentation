# La tabella decisionale ha ritorni

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa carta DocBits controlla se una specifica tabella decisionale ha valori di ritorno per un determinato documento e determina se i dati restituiti devono essere utilizzati nei successivi passaggi del flusso di lavoro. Garantisce che i flussi di lavoro possano adattarsi dinamicamente in base ai risultati della tabella decisionale.

## **Funzionalità:**

* **Convalida della tabella decisionale:** Questa carta verifica se la tabella decisionale selezionata fornisce valori di ritorno per il documento in fase di elaborazione.
* **Selezione della tabella decisionale:** Gli utenti specificano il nome della tabella decisionale da controllare.
* **Usa dati di ritorno:** Gli utenti possono specificare se utilizzare i dati di ritorno nelle carte successive con un'impostazione **Booleana**:
  * **Vero (True):** I dati di ritorno sono disponibili e verranno utilizzati nei successivi passaggi del flusso di lavoro.
  * **Falso (False):** I dati di ritorno non verranno utilizzati e il flusso di lavoro procede senza di essi.

## **Utilizzo:**

Questa carta è ideale per i flussi di lavoro che coinvolgono logica condizionale o processi decisionali basati su regole predefinite in una tabella decisionale. Garantisce una perfetta integrazione dei risultati della tabella decisionale nei processi del flusso di lavoro.

## **Esempio di scenario:**

* Un utente configura la carta per controllare la tabella decisionale **"Regole di elaborazione fatture"** per i valori di ritorno. Il valore **Booleano** è impostato su **Vero**, a indicare che i dati di ritorno (ad esempio i requisiti di approvazione) verranno utilizzati nelle carte successive per guidare le decisioni del flusso di lavoro.

Utilizzando la carta "Controllo tabella decisionale", le organizzazioni possono migliorare la flessibilità del flusso di lavoro, semplificare l'elaborazione basata su regole e garantire la coerenza nel processo decisionale tra i flussi di lavoro automatizzati.
