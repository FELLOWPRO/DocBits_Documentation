# Installazione di WatchDog

### Configurazione di WatchDog in DocBits

1. **Accedi alle Impostazioni di WatchDog**
   * Naviga su **Impostazioni → Elaborazione Documenti → WatchDog**.
2. **Impostazioni della Cartella**
   * Definisci i percorsi in cui WatchDog trova ed elabora i documenti.
   *   I percorsi delle cartelle devono corrispondere a quelli creati durante l'installazione:

       * `C:/WatchDog/Read`
       * `C:/WatchDog/Processed`

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG1EFmtSO4AxZjWir401%252Fimage.png%3Falt%3Dmedia%26token%3Dc356e023-8cfb-4f45-b863-b27c5af1d9df\&width=768\&dpr=4\&quality=100\&sign=1b1ae0c4\&sv=2)
   * <mark style="color:red;">**Nota:**</mark>**&#x20;Si consiglia di utilizzare percorsi locali. Questi dovrebbero corrispondere alle cartelle nell'Installazione di DocBits**
3. **Impostazioni Generali**
   *   Seleziona i tipi di documento da elaborare selezionando le relative caselle di controllo\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZbCt5UHd37PdNZsVItdt%252Fimage.png%3Falt%3Dmedia%26token%3Db3c3f203-0f60-42a0-bd56-ee70c204f5e8\&width=768\&dpr=4\&quality=100\&sign=becd5e31\&sv=2)
   * **Barcode Divider:** Quando attivato, abilita la divisione del codice a barre.
   * **DocBits Operator:** Quando abilitato, apre un browser Chrome in background per il DocBits Operator.
   * **Destinazione di esportazione:** Imposta la destinazione di esportazione.
     * **Infor:** I documenti vengono esportati in Infor.
     * **Cartella di Esportazione:** I documenti vengono esportati in una cartella definita che può essere configurata di seguito.
4. **Configurazioni di Esportazione**
   * Mostra tutte le esportazioni configurate per **elaborazione on-premise**.
   *   Mostra il timestamp della **ultima connessione riuscita** per ciascuna configurazione.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FRvK5qn6EggWJxcSYNP5J%252Fimage.png%3Falt%3Dmedia%26token%3D195b9cc6-c5ac-4ee6-90da-b3ee9696ee30\&width=768\&dpr=4\&quality=100\&sign=3bc11ec5\&sv=2)
5. **Configurazione bod\_mapping (Opzionale)**
   * <mark style="color:red;">**Campi obbligatori:**</mark> Prima di aggiungere mappature di metadati personalizzati, è necessario definire i seguenti due valori
     * **`file_name`**
     * **`pdf_path`**
   *   Clicca su **Aggiungi Riga** per definire le mappature dei metadati.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlzUqcr51kq18OrmYAR8X%252Fimage.png%3Falt%3Dmedia%26token%3D3035122b-f1d3-44cc-bfe6-5230943bd77d\&width=768\&dpr=4\&quality=100\&sign=e98d5a1b\&sv=2)
   * **Valore:** Specifica il nome del campo per i metadati.
   * **Percorso:** L'espressione XPath che punta ai dati XML che devono essere assegnati al campo.
   * **Icona del Cestino:** Usata per eliminare una riga specifica.
6. **Scarica la Configurazione**
   * Salva la configurazione
   *   Scarica la configurazione\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZXiz4KB7QpnaqD9XwX3o%252Fimage.png%3Falt%3Dmedia%26token%3D04c9f8dc-7d79-443f-9ce4-6d4214edc98b\&width=768\&dpr=4\&quality=100\&sign=574a4218\&sv=2)

### Guida all'Installazione di WatchDog

1. **Crea le Cartelle Richieste**
   * Crea una directory principale: `C:/WatchDog`
   * All'interno di `C:/WatchDog`, crea le seguenti sottocartelle: **Nota**: queste devono corrispondere alle cartelle in DocBits
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Nota:**</mark>**&#x20;Si consiglia di utilizzare percorsi locali. Questi dovrebbero corrispondere alle cartelle nella Configurazione di DocBits**
2. **Scarica WatchDog**
   * Scarica l'ultima versione di `WatchDog.exe` da: [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Posiziona il file `WatchDog.exe` scaricato in `C:/WatchDog`.
   * Posiziona il file `watchdog-config.json` scaricato in `C:/WatchDog`.
   * Apri il `watchdog-config.json` e modifica il **config\_path.**
   * In questo esempio:
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **Installa WatchDog**
   * Apri **Prompt dei Comandi (CMD)** con **diritti di Amministratore**.
   * Naviga nella cartella di WatchDog
   *   Esegui il seguente comando per installare WatchDog:

       `WatchDog.exe install`
4. **Avvia il Servizio WatchDog**
   *   Esegui il seguente comando in CMD:

       `WatchDog.exe start`
5. **Imposta il Tipo di Avvio**
   * Apri **Servizi** (Premi `Win + R`, digita `services.msc` e premi **Invio**).
   * Trova **WatchDog** nell'elenco dei servizi.
   * Fai doppio clic per aprire le sue proprietà.
   * Imposta il **Tipo di Avvio** su **Automatico (Avvio Ritardato)**.
   * Clicca su **OK**.
