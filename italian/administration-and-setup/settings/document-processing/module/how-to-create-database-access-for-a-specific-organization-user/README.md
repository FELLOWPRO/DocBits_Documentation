# Come creare l'accesso al database per un utente specifico dell'organizzazione

### **1. Accedi a DocBits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Vai alla pagina di accesso della tua applicazione.
2. Inserisci le tue credenziali (nome utente e password) per accedere.

### **2. Apri le impostazioni** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Dopo l'accesso, individua l'icona **Settings** (ingranaggio ⚙️) nella barra laterale sinistra.
2. Fai clic su **Settings** per aprire il pannello di configurazione del sistema.

### **3. Apri il modulo Document Processing** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. In **Settings**, individua la sezione **Document Processing**.
2. In **Document Processing**, trova e fai clic sull'opzione **Module**.
   * Si aprirà la pagina di configurazione del modulo, dove puoi procedere con la creazione dell'utente per il database.

### 4. Passaggi per attivare e accedere all'utente AI Document e database: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Attiva le funzionalità**:
   * Usa gli interruttori sulla destra per attivare o disattivare funzionalità specifiche:
     * **AI Document Warehouse**: attivalo per abilitare l'accesso alle funzionalità legate all'IA.
     * **DB Access**: attivalo per concedere all'utente l'accesso al database.
2. **Credenziali del database**:
   * Il dashboard mostra i seguenti dettagli di connessione al database:
     * **Username**: viene mostrato un nome utente univoco
     * **Password**: assicurati di conservare o copiare la password in modo sicuro.
     * **Database**: è il nome del database
     * **Host**: nome dell'host
     * **Port**: è la porta
     * **SSL Mode:** la connessione richiede `sslmode=require` per una comunicazione sicura.
3. **Copia delle credenziali**:
   * Usa le icone di copia accanto a ciascun campo per copiare rapidamente le credenziali da usare nel tuo client di database o nella tua applicazione.
4. **Connessione tramite DBeaver**:
   * Connessione tramite Host
     * scegli PostgreSQL
     * compila le informazioni richieste
     * passa alla scheda SSL e seleziona Use SSL. Scorri fino a SSL mode e seleziona require
   * Connessione tramite URL
     * Compila le informazioni richieste:\n - sostituisci Host con le informazioni sull'host fornite\n - sostituisci Port con le informazioni sulla porta fornite\n - sostituisci Database con le informazioni sul database fornite\n - per Username seleziona le informazioni sul nome utente fornite\n - per Password seleziona le informazioni sulla password fornite
5. **Verifica la connessione**:
   * Fai clic sul pulsante **"Test Connection"** per assicurarti che le credenziali e i dettagli di connessione siano corretti.
   * Se il test ha esito positivo, procedi con la connessione.
6. **Esplora il database**:
   * Una volta connesso, vai alla sezione **schema** o **tables** nel tuo client di database.
   * Controlla le tabelle disponibili.
