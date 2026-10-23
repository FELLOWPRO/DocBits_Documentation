# Collegamento tramite database in sola lettura

Questa guida ti accompagna nel collegamento del **database in sola lettura di DocBits a Power BI Desktop** tramite il **driver ODBC di PostgreSQL**. Copre l'installazione del driver, la configurazione ODBC, l'integrazione con Power BI e l'aggiornamento pianificato.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

#### 1. Installa il driver ODBC di PostgreSQL

* Scarica il driver ODBC di PostgreSQL più recente (**psqlODBC**) dal sito ufficiale:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Esegui il programma di installazione e segui la procedura guidata.

#### 2. Configura l'origine dati ODBC

* Apri **ODBC Data Source Administrator (64-bit)** dal Pannello di controllo o dalla ricerca di Windows.
* Vai alla scheda **System DSN** e fai clic su **Add**.
* Seleziona dall'elenco il driver **PostgreSQL Unicode(x64)** e fai clic su **Finish**.
* Compila i campi richiesti con le credenziali che trovi in:\n  **DocBits → Settings → Document Processing → Module → AI Dashboard → Read-Only DB Access**

<figure><img src="../../.gitbook/assets/connect_read_only_4.png" alt="Riquadro Navigator di Power BI che mostra l'origine dati ODBC dsn-Sandbox-Read_Only con lo schema public e le relative tabelle elencate"><figcaption></figcaption></figure>

**Campi obbligatori:**

* **Name:** un nome per la connessione (ad es. `Sandbox-Read_Only`)
* **Server:** copia il valore host da DocBits
* **Port:** copia il valore della porta da DocBits
* **Database:** copia il nome del database da DocBits
* **Username:** copia il nome utente da DocBits
* **Password:** copia la password da DocBits
* **SSL Mode:** imposta su **Require** (garantisce la comunicazione cifrata)

#### 3. Collega il database in sola lettura a Power BI

* Apri **Power BI Desktop**.
*   Seleziona **Get Data** → **ODBC** → **Connect**.

    <figure><img src="../../.gitbook/assets/powerbi_get_data_odbc.png" alt="Power BI Get Data ODBC"><figcaption></figcaption></figure>
* Dall'elenco DSN seleziona l'origine che hai configurato (ad es. `Sandbox-Read_Only`).

<figure><img src="../../.gitbook/assets/connect_read_only_3.png" alt="Power BI Navigator con tabelle di sandbox-doc2api come supplier group, supplier header e task assignment, con i pulsanti Select Related Tables, Load e Transform Data"><figcaption></figcaption></figure>

* Fai clic su **OK**. Se richiesto, inserisci di nuovo le credenziali.
  * Se compare `password authentication failed for user`, verificare host, database, nome utente e password. Nella finestra delle credenziali inserire la password effettiva. Le parentesi graffe per l’escape in una stringa di connessione ODBC fanno parte della sintassi del driver e non risolvono in generale gli errori di autenticazione.

#### 4. Carica e trasforma i dati

* Nel pannello **Navigator** espandi l'elenco degli schemi.
* Apri lo schema **`public`**.
* Seleziona le tabelle che desideri importare.

![Pannello Read-Only DB Access di DocBits che mostra i campi nome utente, password, database, host e porta e l'elenco delle tabelle disponibili](../../.gitbook/assets/connect_read_only_1.png)        ![Finestra di dialogo From ODBC di Power BI con l'elenco a discesa Data source name (DSN) e le opzioni avanzate](../../.gitbook/assets/connect_read_only_2.png)

* Scegli:
  * **Load** → importa direttamente in Power BI
  * **Transform Data** → apre Power Query per modellare e filtrare i dati prima del caricamento

#### 5. Visualizza i tuoi dati

* Utilizza l'area di lavoro dei report di Power BI per creare dashboard.
* Trascina i campi, aggiungi filtri dinamici (slicer), scegli i tipi di grafico e applica calcoli DAX.
* Utilizza **Power Query Editor** per pulire o unire i dati prima di creare le visualizzazioni.
* Riferimento: [Documentazione di Power BI](https://learn.microsoft.com/en-us/power-bi/)

#### 6. Abilita l'aggiornamento pianificato (facoltativo)

L’aggiornamento pianificato dipende dalla licenza o capacità dell’area di lavoro, dal connettore e dalla modalità di connessione. Per questa connessione ODBC, configurare un gateway raggiungibile con driver, DSN e credenziali appropriati. Verificare i requisiti attuali nella documentazione ufficiale.

* Per mantenere i tuoi report sincronizzati con PostgreSQL:
* Pubblica il tuo file `.pbix` su **Power BI Service**.
* Installa il **Power BI Gateway** (modalità Standard) su una macchina con accesso di rete a PostgreSQL.
* In servizio Power BI:
  * Vai al tuo dataset → **Impostazioni** → **Aggiornamento pianificato**
  * Associa il tuo DSN e fornisci le credenziali
* Ulteriori informazioni [qui](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).&#x20;

#### 7. Esempi di dashboard e viste dati&#x20;

<div><figure><img src="../../.gitbook/assets/powerbi_dashboard_example_1.png" alt="Esempio di dashboard Power BI 1"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_2.png" alt="Esempio di dashboard Power BI 2"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_3.png" alt="Esempio di dashboard Power BI 3"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_4.png" alt="Esempio di dashboard Power BI 4"><figcaption></figcaption></figure></div>

[Documentazione ufficiale — ODBC](https://learn.microsoft.com/en-us/power-query/connectors/odbc)

[Documentazione ufficiale — psqlODBC](https://odbc.postgresql.org/docs/config-opt.html)

[Documentazione ufficiale — Power BI](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh)
