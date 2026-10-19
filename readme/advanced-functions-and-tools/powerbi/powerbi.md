---
description: Come configurare PowerBI
---

# Collegamento tramite ClickHouse

Questa guida ti accompagna nel collegamento di **ClickHouse** a **Power BI Desktop** tramite il **driver ODBC**. Copre l'installazione del driver, la configurazione ODBC, l'integrazione con Power BI e l'impostazione dell'aggiornamento dei dati.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

#### 1. Installa il driver ODBC di ClickHouse

* Scarica il **driver ODBC di ClickHouse** più recente da:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Esegui il programma di installazione e segui la procedura guidata.

#### 2. Configura l'origine dati ODBC

* Apri **ODBC Data Source Administrator (64-bit)** dal Pannello di controllo o dalla ricerca di Windows.
* Vai alla scheda **System DSN** e fai clic su **Add**.
* Seleziona **ClickHouse ODBC Driver** dall'elenco e fai clic su **Finish**.
*   Compila i campi richiesti. Le informazioni necessarie si trovano in:

    **DocBits** → **Settings** → **Document Processing** → **Module** → **AI Dashboard** → **ClickHouse Direct Access**

    <figure><img src="../../.gitbook/assets/clickhouse_direct_access_settings.png" alt="Impostazioni ClickHouse Direct Access in DocBits"><figcaption></figcaption></figure>

    **Campi obbligatori:**

    * **Name**: un nome per la connessione (ad es. `ClickHouse_Prod`)
    * **Description**: una breve descrizione per tua comodità (facoltativa)
    * **Host**: copia il valore host da DocBits
    * **Port**: copia il valore della porta da DocBits
    * **Database**: copia il nome del database da DocBits
    * **Username**: copia il nome utente da DocBits
    * **Password**: copia la password da DocBits

#### 3. Collega ClickHouse a Power BI

* Apri **Power BI Desktop**.
* Seleziona **Get Data** → **ODBC** → **Connect**.\


  <figure><img src="../../.gitbook/assets/powerbi_get_data_odbc.png" alt="Power BI Get Data ODBC"><figcaption></figcaption></figure>
* Dall'elenco DSN seleziona l'origine che hai configurato (ad es. `ClickHouse_Prod`).\


  <figure><img src="../../.gitbook/assets/powerbi_select_dsn.png" alt="Selezione del DSN in Power BI"><figcaption></figcaption></figure>
* Fai clic su **OK**. Se richiesto, inserisci di nuovo le credenziali.

#### 4. Carica e trasforma i dati

* Nel pannello **Navigator** sfoglia e seleziona le tabelle o le viste da importare.
* Scegli:
  * **Load**: per importare direttamente
  * **Transform Data**: per aprire Power Query e modellare i dati\


  <figure><img src="../../.gitbook/assets/powerbi_navigator_load_transform.png" alt="Navigator di Power BI con Load e Transform Data"><figcaption></figcaption></figure>

#### 5. Visualizza i tuoi dati

* Utilizza l'area di lavoro dei report per creare le visualizzazioni.
* Trascina i campi, aggiungi filtri dinamici (slicer), scegli i tipi di grafico e usa espressioni **DAX** secondo necessità.
* &#x20;Sfrutta **Power Query Editor** per pulire o ruotare (pivot) i dati ClickHouse prima di creare le visualizzazioni.
* Documentazione di PowerBI: [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

#### 6. Abilita l'aggiornamento pianificato (facoltativo)

<mark style="color:red;">**Nota:**</mark> **Richiede Power BI Pro o Premium + Gateway**

* Per mantenere i tuoi report sincronizzati con ClickHouse:
* Pubblica il tuo file `.pbix` su **Power BI Service**.
* Installa il **Power BI Gateway** (modalità Standard) su una macchina con accesso di rete a ClickHouse.
* In Power BI Service:
  * Vai al tuo dataset → **Settings** → **Scheduled Refresh**
  * Associa il tuo DSN e fornisci le credenziali
* Ulteriori informazioni [qui](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).&#x20;

#### 7. Esempi di dashboard e viste dati&#x20;

<div><figure><img src="../../.gitbook/assets/powerbi_dashboard_example_1.png" alt="Esempio di dashboard Power BI 1"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_2.png" alt="Esempio di dashboard Power BI 2"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_3.png" alt="Esempio di dashboard Power BI 3"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_4.png" alt="Esempio di dashboard Power BI 4"><figcaption></figcaption></figure></div>
