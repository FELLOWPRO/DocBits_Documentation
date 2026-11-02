# Test: connessione di importazione FTP

#### Scopo

Questi test garantiscono che il nostro sistema di importazione FTP funzioni correttamente. Verifichiamo che sia possibile aggiungere una nuova connessione di importazione FTP, testare la connessione, attivarla/disattivarla e ripulirla successivamente.



{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Scenari di test

1. **Setup:**
   * **Variabili d'ambiente:** Carica i dettagli necessari come informazioni sul server FTP e credenziali dalle variabili di ambiente.
2.  **FTP Connection Tests:**

    **Aggiungi nuova connessione:**

    * **Test Aggiungi nuovo FTP Importa connessione (`test_add_new_ftp_import_connection`):**
      * Aggiungi una nuova connessione di importazione FTP con le credenziali e i dettagli del server specificati.
      * **Risultato previsto:** La connessione dovrebbe essere aggiunta correttamente.

    **Deactivate Connection:**

    * **Test Disattiva FTP Importa connessione (`test_deactivate_ftp_import_connection`):**
      * Disattiva la connessione di importazione FTP appena aggiunta.
      * **Risultato previsto:** La connessione dovrebbe essere disattivata con successo.

    **Test Connection:**

    * **Test della connessione FTP (`test_test_ftp_connection`):**
      * Verifica se la connessione di importazione FTP può connettersi correttamente al server FTP.
      * **Risultato previsto:** La connessione dovrebbe essere testata con successo.

    **Controlla connessione nell'elenco:**

    * **Test Verifica FTP Connessione in Lista (`test_check_ftp_connection_in_list`):**
      * Controlla se la connessione di importazione FTP appena aggiunta è presente nell'elenco delle connessioni.
      * **Risultato previsto:** La connessione dovrebbe essere trovata nell'elenco.

    **Verifica connessione disattivata:**

    * **Test Verifica FTP Connessione Disattivata (`test_check_ftp_connection_deactivated`):**
      * Verificare che la connessione di importazione FTP sia contrassegnata come inattiva nell'elenco.
      * **Risultato previsto:** La connessione dovrebbe essere inattiva.

    **Aggiungi cartella di prova:**

    * **Test Aggiungi cartella di prova alla connessione (`test_add_test_folder_to_connection`):**
      * Aggiungi una directory predefinita (cartella di prova) alla connessione di importazione FTP.
      * **Risultato previsto:** La directory predefinita dovrebbe essere aggiunta correttamente.

    **Reactivate Connection:**

    * **Test Riattivazione FTP Importa connessione (`test_reactivate_ftp_import_connection`):**
      * Riattivare la connessione di importazione FTP precedentemente disattivata.
      * **Risultato previsto:** La connessione dovrebbe essere riattivata con successo.

    **Verifica connessione riattivata:**

    * **Test Verifica FTP Connessione Riattivata (`test_check_ftp_connection_reactivated`):**
      * Verificare che la connessione di importazione FTP sia contrassegnata come attiva nell'elenco.
      * **Risultato previsto:** La connessione dovrebbe essere attiva.

    **Cleanup:**

    * **Test pulizia FTP Importa (`test_cleanup_ftp_import`):**
      * Elimina la connessione di importazione FTP per ripulirla dopo i test.
      * **Risultato previsto:** La connessione dovrebbe essere eliminata correttamente.

## Spiegazione dettagliata di ogni test

* **Configurazione e inizializzazione:**
  * **Inizializza dati condivisi:** Prepara i dati condivisi per i test.
* **FTP Connection Tests:**
  * **Aggiungi nuova connessione:** Aggiungi una nuova connessione di importazione FTP con le credenziali e i dettagli del server forniti.
  * **Disattiva connessione:** Disattiva la connessione di importazione FTP appena aggiunta.
  * **Test connessione:** Verifica se la connessione di importazione FTP può connettersi correttamente al server FTP.
  * **Verifica connessione nell'elenco:** Verificare che la nuova connessione di importazione FTP sia presente nell'elenco delle connessioni.
  * **Verifica connessione disattivata:** Confermare che la connessione di importazione FTP sia contrassegnata come inattiva nell'elenco.
  * **Aggiungi cartella di test:** Aggiungi una directory predefinita (cartella di test) alla connessione di importazione FTP.
  * **Riattiva connessione:** Riattiva la connessione di importazione FTP precedentemente disattivata.
  * **Verifica connessione riattivata:** Assicurarsi che la connessione di importazione FTP sia contrassegnata come attiva nell'elenco.
  * **Cleanup:** Elimina la connessione di importazione FTP per ripulire dopo i test.

\


