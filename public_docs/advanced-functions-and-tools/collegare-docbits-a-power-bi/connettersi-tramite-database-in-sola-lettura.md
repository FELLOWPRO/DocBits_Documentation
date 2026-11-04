# Connettersi tramite Database in sola lettura

Questa guida ti guida nel collegamento del **Database in sola lettura di DocBits a Power BI Desktop** utilizzando il **driver ODBC PostgreSQL**. Copre l'installazione del driver, la configurazione ODBC, l'integrazione di Power BI e l'aggiornamento programmato.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Installare il driver ODBC PostgreSQL

* Scarica l'ultimo driver ODBC PostgreSQL (**psqlODBC**) dal sito ufficiale:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Esegui l'installatore e segui la procedura guidata.

### 2. Configurare la fonte dati ODBC

* Apri **Amministratore origine dati ODBC (a 64 bit)** tramite Pannello di controllo o Ricerca di Windows.
* Vai alla scheda **DSN di sistema** e clicca su **Aggiungi**.
* Seleziona il driver **PostgreSQL Unicode(x64)** dalla lista e clicca su **Fine**.
* Compila i campi richiesti con le credenziali da: **DocBits → Impostazioni → Elaborazione documenti → Modulo → Dashboard AI → Accesso al DB in sola lettura**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FupCHowPUuMJ8hO9Y36EY%252Fconnect_read_only_4.png%3Falt%3Dmedia%26token%3D3eb69744-6696-41e2-90be-63295b9b6f6d\&width=768\&dpr=4\&quality=100\&sign=647db68c\&sv=2)

**Campi obbligatori:**

* **Nome:** Un nome per la connessione (es. `Sandbox-Read_Only`)
* **Server:** Copia il valore host da DocBits
* **Porta:** Copia il valore della porta da DocBits
* **Database:** Copia il nome del database da DocBits
* **Nome utente:** Copia il nome utente da DocBits
* **Password:** Copia la password da DocBits
* **Modalità SSL:** Imposta su **Richiesta** (garantisce comunicazioni criptate)

### 3. Collegare il DB in sola lettura a Power BI

* Apri **Power BI Desktop**.
*   Seleziona **Ottieni dati** → **ODBC** → **Connetti**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
* Dalla lista DSN, seleziona la tua origine configurata (es. `Sandbox-Read_Only`).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKPDLjfDw2SRYvzvFKWXq%252Fconnect_read_only_3.png%3Falt%3Dmedia%26token%3Dc67c1362-7f63-479e-a373-974d198f5eb7\&width=768\&dpr=4\&quality=100\&sign=f001e759\&sv=2)

* Clicca su **OK**. Inserisci nuovamente le credenziali se richiesto.
  * **Nota:** Se visualizzi l'errore **“autenticazione password fallita per l'utente”**, prova a inserire la password racchiusa tra **parentesi graffe** `**{}**`.

### 4. Caricare e trasformare i dati

* Nel riquadro **Navigatore**, espandi l'elenco dello schema.
* Apri lo schema `**public**`.
* Seleziona le tabelle che desideri importare.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSmtEspL1H6ieOJhtDwYb%252Fconnect_read_only_1.png%3Falt%3Dmedia%26token%3Dd402a928-175e-4904-bd21-592ff114fad7\&width=300\&dpr=4\&quality=100\&sign=464e3a3d\&sv=2) ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3Phea1Pf3ZBJtMzw3rxi%252Fconnect_read_only_2.png%3Falt%3Dmedia%26token%3D94037886-57e3-440d-bf08-61cd37c65b98\&width=300\&dpr=4\&quality=100\&sign=5ead9fe9\&sv=2)

* Scegli:
  * **Carica** → Importa direttamente in Power BI
  * **Trasforma dati** → Apri Power Query per la modellazione e il filtraggio prima del caricamento

### 5. Visualizza i tuoi dati

* Utilizza il canvas del report di Power BI per creare dashboard.
* Trascina campi, aggiungi slicers, scegli tipi di grafico e applica calcoli DAX.
* Utilizza **Editor Power Query** per pulire o unire dati prima di creare visualizzazioni.
* Riferimento: [Documentazione Power BI](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

### 6. Abilita l'aggiornamento programmato (Opzionale)

**Nota:** **Richiede Power BI Pro o Premium + Gateway**

* Per mantenere i tuoi report sincronizzati con ClickHouse:
* Pubblica il tuo file `.pbix` su **Power BI Service**.
* Installa il **Power BI Gateway** (Modalità Standard) su una macchina con accesso di rete a ClickHouse.
* In Power BI Service:
  * Vai al tuo dataset → **Impostazioni** → **Aggiornamento programmato**
  * Mappa il tuo DSN e fornisci le credenziali
* Ulteriori informazioni [qui](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Esempi di Dashboard e Visualizzazioni dei dati

![](<../../.gitbook/assets/example_4 (1).avif>)![](<../../.gitbook/assets/example_3 (1).avif>)![](<../../.gitbook/assets/example_2 (1).avif>)![](<../../.gitbook/assets/example_1 (1).avif>)
