# Test: importazione file 1

## Scopo

Questi test sono progettati per garantire che il nostro sistema di importazione dei file funzioni correttamente. Testiamo specificamente l'importazione dei file PDF e TIFF nel sistema, assicurandoci che vengano elaborati e archiviati con successo.

#### Preparazione e pulizia dei test

* **Setup:**
  * Prima di ogni test, registriamo un messaggio di configurazione.
  * **Pulizia:** Dopo ogni test, puliamo eliminando tutti i documenti creati dall'utente del test dal database per garantire che nessun dato residuo influenzi i test successivi.

#### Scenari di test

1. **Import PDF File:**
   * **Test di importazione PDF (`test_import_pdf`):**
     * Importa un file PDF (`FellowBananaInvoice.pdf`) nel sistema.
     * **Risultato previsto:** Il file dovrebbe essere importato con successo, restituendo un documento ID.
2. **Import TIFF File:**
   * **Test di importazione TIFF (`test_import_tiff`):**
     * Importa un file TIFF (`TIFF_FILE.TIF`) nel sistema.
     * **Risultato previsto:** Il file dovrebbe essere importato con successo, restituendo un documento ID.

## Spiegazione dettagliata di ogni test

* **Configurazione e pulizia:**
  * **Logging:** Per ogni test viene registrato un messaggio di configurazione e pulizia.
  * **Pulizia database (`clean_documents`):** Elimina tutti i documenti creati dall'utente test dal database per mantenere uno stato pulito.
*   **Test di importazione file:**

    **Import PDF File:**

    * **Carica Utente:** Carica l'utente di prova.
    * **Percorso file:** Specificare il percorso del file PDF (`tests/files/pdfs/FellowBananaInvoice.pdf`).
    * **Importa file:** Usa la classe `FileImporter` per importare il file PDF.
    * **Risposta di controllo:** Assicurati che la risposta sia un elenco contenente un messaggio di successo e un documento ID.

    **Import TIFF File:**

    * **Carica Utente:** Carica l'utente di prova.
    * **Percorso file:** Specificare il percorso del file TIFF (`tests/files/pdfs/TIFF_FILE.TIF`).
    * **Importa file:** Usa la classe `FileImporter` per importare il file TIFF.
    * **Risposta di controllo:** Assicurati che la risposta sia un elenco contenente un messaggio di successo e un documento ID.

## Struttura del codice

* **Logger:** Utilizzato per registrare i messaggi di debug durante l'installazione, la pulizia e l'esecuzione del test.
* **Assistente database:** Esegue query senza restituire risultati per la pulizia.
* **Importatore file:** Gestisce l'importazione di file nel sistema.
* **Fixtures:** `set_up` fixture per gestire la configurazione e la pulizia per i test.
* **Tests:**
  * `test_import_pdf`: verifica l'importazione di un file PDF.
  * `test_import_tiff`: verifica l'importazione di un file TIFF.

#### Riepilogo

Questi test garantiscono che la nostra funzionalità di importazione dei file funzioni come previsto sia per i file PDF che per quelli TIFF. Seguendo questo approccio, verifichiamo che i file vengano importati correttamente e che il sistema possa gestire diversi tipi di file senza problemi.


