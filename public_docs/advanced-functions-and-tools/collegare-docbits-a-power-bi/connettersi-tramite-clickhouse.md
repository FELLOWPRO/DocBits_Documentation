# Connettersi tramite ClickHouse

Questa guida ti guida nel collegamento di **ClickHouse** a **Power BI Desktop** utilizzando il **driver ODBC**. Copre l'installazione del driver, la configurazione ODBC, l'integrazione di Power BI e l'impostazione dell'aggiornamento dei dati.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Installare il driver ODBC di ClickHouse

* Scarica l'ultimo **driver ODBC di ClickHouse** da:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Esegui l'installazione e segui la procedura guidata.

### 2. Configurare l'origine dati ODBC

* Apri **Amministratore origine dati ODBC (a 64 bit)** tramite Pannello di controllo o Ricerca di Windows.
* Vai alla scheda **DSN di sistema** e clicca su **Aggiungi**.
* Seleziona **ClickHouse ODBC Driver** dalla lista e clicca su **Fine**.
*   Compila i campi obbligatori. Puoi trovare le informazioni necessarie in:

    **DocBits** → **Impostazioni** → **Elaborazione documenti** → **Modulo** → **Dashboard AI** → **Accesso diretto a ClickHouse**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNkgb8IJ4dQVRnJ4gpqH0%252Fimage.png%3Falt%3Dmedia%26token%3D27d97e71-dd81-488a-851f-e7d659ad4992\&width=768\&dpr=4\&quality=100\&sign=88a4a589\&sv=2)

    **Campi obbligatori:**

    * **Nome**: Un nome per la connessione (ad es., `ClickHouse_Prod`)
    * **Descrizione**: Una breve descrizione per il tuo riferimento (opzionale)
    * **Host**: Copia il valore host da DocBits
    * **Porta**: Copia il valore della porta da DocBits
    * **Database**: Copia il nome del database da DocBits
    * **Nome utente**: Copia il nome utente da DocBits
    * **Password**: Copia la password da DocBits

### 3. Collegare ClickHouse a Power BI

* Apri **Power BI Desktop**.
*   Seleziona **Ottieni dati** → **ODBC** → **Connetti**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
*   Dalla lista DSN, seleziona la tua origine configurata (ad es., `ClickHouse_Prod`).

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgDWq5vmtqfAGAQEY0SAX%252FScreenshot%25202025-05-19%2520163823.png%3Falt%3Dmedia%26token%3D443435ac-82ba-40de-a4d1-17611afebb6a\&width=768\&dpr=4\&quality=100\&sign=c0c7d7ae\&sv=2)
* Clicca su **OK**. Inserisci nuovamente le credenziali se richiesto.

### 4. Caricare e Trasformare i Dati

* Nel riquadro **Navigatore**, sfoglia e seleziona le tabelle o le viste da importare.
* Scegli:
  * **Carica**: per importare direttamente
  *   **Trasforma dati**: per aprire Power Query per la modellazione dei dati

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2lrWi9PduJgVQGHQMmhX%252FScreenshot%25202025-05-19%2520164134.png%3Falt%3Dmedia%26token%3D135c45ad-a7ca-4f01-a2f0-07998397f4d9\&width=768\&dpr=4\&quality=100\&sign=e27f4d93\&sv=2)

### 5. Visualizza i Tuoi Dati

* Utilizza il canvas del report per creare visualizzazioni.
* Trascina campi, aggiungi slicers, scegli tipi di grafico e utilizza espressioni **DAX** come necessario.
* Sfrutta **Power Query Editor** per pulire o pivotare i tuoi dati ClickHouse prima di creare le visualizzazioni.
* Documentazione di PowerBI: [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

### 6. Abilita l'Aggiornamento Pianificato (Opzionale)

**Nota:** **Richiede Power BI Pro o Premium + Gateway**

* Per mantenere i tuoi report sincronizzati con ClickHouse:
* Pubblica il tuo file `.pbix` su **Power BI Service**.
* Installa il **Power BI Gateway** (modalità Standard) su una macchina con accesso di rete a ClickHouse.
* In Power BI Service:
  * Vai al tuo dataset → **Impostazioni** → **Aggiornamento pianificato**
  * Mappa il tuo DSN e fornisci le credenziali
* Ulteriori informazioni [qui](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Esempi Dashboard e Visualizzazioni dei Dat

![](../../.gitbook/assets/example_4.avif)![](../../.gitbook/assets/example_3.avif)![](../../.gitbook/assets/example_2.avif)![](../../.gitbook/assets/example_1.avif)
