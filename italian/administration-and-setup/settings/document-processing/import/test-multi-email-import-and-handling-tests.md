# Test: importazione e gestione delle e-mail

## Che cosa viene testato?

Questi test garantiscono che il nostro sistema di importazione della posta elettronica funzioni correttamente. Gli obiettivi principali sono:

1. **Invia email** con allegati.
2. **Ricevi e sposta email** in cartelle specifiche.
3. **Controlla se le email sono lette o non lette.**
4. **Importa email nel nostro sistema.**
5. **Pulisci** eliminando successivamente le email e i documenti importati.

## Passaggi necessari

1. **Setup:**
   * **Ottieni impostazioni ambiente:** Carica i dettagli e le credenziali del server di posta elettronica dalle variabili di ambiente.
   * **Crittografa password e-mail:** Crittografa in modo sicuro la password e-mail.
2. **Invia e gestisci email:**
   * **Invia email:** Utilizza una funzione SMTP per inviare email con oggetti e allegati specifici.
   * **Sposta email:** Utilizza le funzioni IMAP per spostare le email nella cartella di destinazione.
   * **Elenca cartelle:** Controlla se la cartella di destinazione esiste.
   * **Elimina email:** Pulisci le email eliminandole dalle cartelle.
   * **Verifica stato e-mail:** Verifica se le e-mail sono contrassegnate come non lette o lette.
3.  **Test Sequence**

    **Initial Setup:**

    * **Verifica connessione:** Verifica la connessione al server di posta elettronica e ottieni la connessione ID.
    * **Test di accesso:** Conferma che l'accesso con le credenziali memorizzate funziona.
    * **Controllo cartella:** Assicurarsi che la cartella di destinazione esista sul server di posta elettronica.

    **Email Operations:**

    * **Invia email di prova:** Invia tre email con oggetti univoci.
    * **Recupera ID e-mail:** Ottieni gli ID delle e-mail inviate dalla casella di posta.
    * **Sposta email:** Sposta queste email dalla posta in arrivo alla cartella di destinazione.
    * **Verifica stato e-mail:** Assicurati che le e-mail nella cartella di destinazione siano contrassegnate come non lette.

    **Email Importing:**

    * **Recupera email:** Importa le email dalla cartella di destinazione nel nostro sistema.
    * **Controlla le email importate:** Assicurati che le email importate siano recuperate e registrate correttamente.

    **Log Verification:**

    * **Controlla i log di importazione:** Verifica che gli oggetti delle email inviate siano registrati nei log di importazione.

    **Cleanup:**

    * **Elimina documenti importati:** Rimuovi i documenti importati dalle e-mail.
    * **Elimina email:** Pulisci eliminando le email inviate e spostate dalle cartelle.

### Spiegazione dettagliata di ogni test

* **Configurazione e inizializzazione:**
  * **Inizializza dati condivisi:** Prepara i dati condivisi per i test.
* **Test di connessione e-mail:**
  * **Ottieni connessione ID:** Controlla se possiamo connetterci al server di posta elettronica e ottieni un ID per la connessione.
  * **Verifica dell'accesso:** Assicurarsi che l'accesso al server di posta elettronica funzioni correttamente.
* **Test di verifica delle cartelle:**
  * **Controlla cartella di destinazione:** Assicurati che la cartella di destinazione esista sul server di posta elettronica.
  * **Verifica elenco cartelle:** Assicurati che l'elenco delle cartelle dal server corrisponda alle nostre aspettative.
* **Invio e ID Recupero e-mail:**
  * **Invia email:** Invia tre email di prova con oggetti e allegati specifici.
  * **Ottieni ID e-mail:** Recupera gli ID univoci di queste e-mail inviate dalla casella di posta.
* **Spostamento e-mail e controllo dello stato:**
  * **Sposta le email nella cartella:** Sposta le email di prova dalla posta in arrivo alla cartella di destinazione.
  * **Controlla lo stato non letto:** Assicurati che le e-mail siano contrassegnate come non lette dopo lo spostamento.
* **Recupero e-mail e convalida della risposta:**
  * **Recupera email dalla cartella:** Importa le email dalla cartella di destinazione nel nostro sistema.
  * **Convalida e-mail recuperate:** Conferma che le e-mail recuperate corrispondono alle e-mail inviate.
* **Verifica registro importazione:**
  * **Recupera registro di importazione:** Recupera il registro delle email importate.
  * **Controlla gli oggetti delle email nel registro:** Assicurati che gli oggetti delle email di prova siano presenti nel registro di importazione.
* **Cleanup:**
  * **Elimina documenti importati:** Rimuovi i documenti importati dalle e-mail.
  * **Elimina email:** Elimina le email di prova dalla posta in arrivo e dalla cartella di destinazione per mantenere tutto pulito.

\


