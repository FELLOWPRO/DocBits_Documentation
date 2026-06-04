# Then

## Panoramica delle schede di azione "Then..."

### **1. Azioni Document Field:**

* **Invert Checkbox:** Questa azione inverte lo stato di un campo casella di controllo in un documento.
* **Set Checkbox:** Imposta lo stato di un campo casella di controllo su vero (selezionato) o falso (deselezionato).
* **Set Field to Text:** Questa azione imposta un campo specificato del documento su un determinato valore testuale.

<figure><img src="../../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

### **2. Azioni Document:**

* **Approve the Document:** Contrassegna un documento come approvato all'interno del sistema.
* **Reject the Document:** Contrassegna un documento come rifiutato.

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### **3. Azioni Export:**

* **Export document with export configuration:** Avvia il processo di esportazione con una specifica configurazione di esportazione.
* **Start Export:** Avvia il processo di esportazione.



<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

### **4. Azioni Status:**



* **Change Status:** Cambia lo stato di un documento o di un'attività in un nuovo stato specificato.

<figure><img src="../../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

### **5. Azioni Task:**

* Assegnazioni e notifiche:
  * **Assign Task:** Crea e assegna un'attività con dettagli specifici a un individuo o a un gruppo, con la possibilità di notificarli via email.
  * **Create a New Task:** Simile all'assegnazione ma focalizzata sulla creazione di un'attività completamente nuova all'interno del sistema.

<figure><img src="../../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

### **6. Azioni Table:**

* **Calculate in Table:** Esegue calcoli sui dati di tabella in base a condizioni specificate e memorizza i risultati in una colonna designata.
* **Change Entries:** Aggiorna le voci in una tabella in base a condizioni specificate.

<figure><img src="../../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

### **7. Azioni Assignee:**

* **Assign User from Field:** Assegna un utente a un'attività o documento in base ai dati utente memorizzati in un campo specifico, con un'opzione per un utente di riserva se il principale non è disponibile.
* **Assign Document to User or Group:** Assegna direttamente un documento a un utente o gruppo, garantendo che la responsabilità sia attribuita in modo appropriato.

<figure><img src="../../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

### **8. Azioni di interazione esterna:**

* **Call API:** Invia una richiesta a un'API esterna, personalizzabile con metodi, parametri e dati specifici.
* **Send HTTPS Request:** Simile alle chiamate API ma formattata specificamente per i protocolli HTTPS.

<figure><img src="../../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

### **9. Elaborazione avanzata:**

* **Run Workflow:** Attiva un altro workflow all'interno del sistema, consentendo concatenazioni di processi complesse.

#### Applicazione pratica

Queste schede di azione vengono utilizzate per automatizzare le risposte in base a trigger specifici identificati nelle parti precedenti della configurazione del workflow. Ad esempio:

* Se un documento viene identificato come bisognoso di revisione, l'azione "Approve the Document" può essere attivata automaticamente una volta che supera tutte le condizioni specificate.
* Per le attività di gestione dati, le azioni "Set Checkbox" o "Set Field to Text" garantiscono che i campi del documento vengano aggiornati automaticamente, riducendo l'inserimento manuale dei dati e il potenziale di errori.
* Attività complesse come le interazioni con le API o i cambiamenti di stato semplificano le interazioni non solo all'interno del sistema ERP ma anche con servizi e strumenti esterni, migliorando l'integrazione e la funzionalità.

### Conclusione

La sezione "Then..." del tuo sistema di workflow fornisce strumenti robusti per definire azioni precise che dovrebbero verificarsi come risultato del soddisfacimento delle condizioni nel workflow. Utilizzando efficacemente queste azioni, le aziende possono automatizzare i processi di routine, garantire l'accuratezza dei dati e rispondere dinamicamente alle informazioni e agli stati del sistema che cambiano. Comprendere come configurare e utilizzare queste azioni è fondamentale per massimizzare l'efficienza e l'efficacia delle capacità di workflow del tuo sistema ERP.
