# Test: importazione e gestione delle e-mail

## Scopo

Questi test garantiscono che il nostro sistema possa gestire correttamente l'importazione delle email. Ciò include l'invio di e-mail, la ricezione e lo spostamento in cartelle specifiche, il controllo se sono letti o non letti, l'importazione nel sistema e l'esecuzione successiva della pulizia.

## Passaggi di test

1. **Setup:**
   * **Ottieni impostazioni ambiente:** Carica i dettagli necessari come le informazioni sul server di posta elettronica e le credenziali dalle variabili di ambiente.
   * **Crittografa password e-mail:** Crittografa in modo sicuro la password e-mail per un utilizzo sicuro.
2. **Invio e gestione email:**
   * **Invia un'e-mail:** Utilizza una funzione SMTP per inviare un'e-mail con un oggetto e un allegato specifici.
   * **Sposta l'e-mail:** Utilizza le funzioni IMAP per spostare l'e-mail in una cartella di destinazione.
   * **Elenca cartelle:** Assicurarsi che la cartella di destinazione esista.
   * **Elimina l'e-mail:** Pulisci eliminando l'e-mail dalla cartella.
   * **Verifica stato e-mail:** Verifica se l'e-mail è contrassegnata come letta o non letta.
3.  **Test Sequence**

    **Initial Setup:**

    * **Verifica connessione:** Verifica la connessione al server di posta elettronica e ottieni la connessione ID.
    * **Test di accesso:** Conferma che l'accesso con le credenziali memorizzate funziona.
    * **Controllo cartella:** Assicurarsi che la cartella di destinazione esista sul server di posta elettronica.

    **Email Operations:**

    * **Invia un'e-mail di prova:** Invia un'e-mail con un oggetto specifico.
    * **Recupera emal’ID:** Ottieni l’ID dell'email inviata dalla casella di posta.
    * **Sposta l'e-mail:** Sposta l'e-mail dalla posta in arrivo alla cartella di destinazione.
    * **Controlla stato e-mail:** Assicurati che l'e-mail nella cartella di destinazione sia contrassegnata come non letta.

    **Email Importing:**

    * **Recupera l'e-mail:** Importa l'e-mail dalla cartella di destinazione nel nostro sistema.
    * **Controlla l'e-mail importata:** Assicurati che l'e-mail importata sia stata recuperata e registrata correttamente.

    **Log Verification:**

    * **Controlla registro di importazione:** Verifica che l'oggetto dell'e-mail inviata sia registrato nel registro di importazione.

    **Cleanup:**

    * **Elimina documento importato:** Rimuove il documento importato dall'e-mail.
    * **Elimina l'e-mail:** Elimina le e-mail inviate e spostate dalle cartelle per mantenere tutto pulito.

## Spiegazione dettagliata di ogni test

* **Configurazione e inizializzazione:**
  * **Inizializza dati condivisi:** Prepara i dati condivisi per i test.
* **Test di connessione e-mail:**
  * **Ottieni connessione ID:** Controlla se possiamo connetterci al server di posta elettronica e ottieni un ID per la connessione.
  * **Verifica dell'accesso:** Assicurarsi che l'accesso al server di posta elettronica funzioni correttamente.
* **Test di verifica delle cartelle:**
  * **Controlla cartella di destinazione:** Assicurati che la cartella di destinazione esista sul server di posta elettronica.
  * **Verifica elenco cartelle:** Assicurati che l'elenco delle cartelle dal server corrisponda alle nostre aspettative.
* **Invio e ID Recupero e-mail:**
  * **Invia un'e-mail:** Invia un'e-mail di prova con un oggetto e un allegato specifici.
  * **Ricevi emal’ID:** Recupera l'unico ID di questa email inviata dalla casella di posta.
* **Spostamento e-mail e controllo dello stato:**
  * **Sposta e-mail nella cartella:** Sposta l'e-mail di prova dalla posta in arrivo alla cartella di destinazione.
  * **Controlla lo stato non letto:** Assicurati che l'e-mail sia contrassegnata come non letta dopo lo spostamento.
* **Recupero e-mail e convalida della risposta:**
  * **Recupera email dalla cartella:** Importa l'email dalla cartella di destinazione nel nostro sistema.
  * **Convalida e-mail recuperata:** Conferma che l'e-mail recuperata è presente nella risposta.
* **Verifica registro importazione:**
  * **Recupera registro di importazione:** Recupera il registro delle email importate.
  * **Controlla l'oggetto dell'e-mail nel registro:** Assicurati che l'oggetto dell'e-mail di prova sia presente nel registro di importazione.
* **Cleanup:**
  * **Elimina documento importato:** Rimuove il documento importato dall'e-mail.
  * **Elimina l'e-mail:** Elimina l'e-mail di prova dalla posta in arrivo e dalla cartella di destinazione per mantenere tutto pulito.

\


