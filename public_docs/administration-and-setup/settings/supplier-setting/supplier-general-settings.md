# Impostazioni Generali del Fornitore

<figure><img src="../../../.gitbook/assets/supplier-general-settings-overview-it-20261111.png" alt="Pagina Impostazioni Generali Del Fornitore con le sezioni Generale, Stato e Raggruppamento ID fornitore"><figcaption><p>Pagina <strong>Impostazioni Generali Del Fornitore</strong>. Dall'alto verso il basso: <strong>Generale</strong> (campi di invito aggiuntivi, stato e raggruppamento ID fornitore), <strong>Carica il logo</strong>, <strong>Politica e dichiarazione sulla privacy</strong> e <strong>Documenti di riferimento per la registrazione dei fornitori</strong>.</p></figcaption></figure>

### Panoramica

La pagina **Impostazioni Generali Del Fornitore** (Impostazioni → Impostazioni Generali Del Fornitore) definisce l'aspetto e il comportamento del portale fornitori. Contiene sei sezioni:

* **Generale** — tre moduli che determinano il flusso di registrazione dei fornitori:
  * **Portale fornitori Campi di invito aggiuntivi**: aggiunge campi supplementari al modulo di registrazione dei fornitori.
  * **Stato**: definisce gli stati del flusso di lavoro che un fornitore può attraversare e chi può approvare ciascuno di essi.
  * **Raggruppamento ID fornitore**: raggruppa più ID fornitore in modo che vengano trattati come un unico fornitore.
* **Carica il logo** — il logo aziendale mostrato nel portale fornitori e nelle e-mail di invito.
* **Politica e dichiarazione sulla privacy** — i documenti legali che i fornitori devono accettare.
* **Documenti di riferimento per la registrazione dei fornitori** — documenti di riferimento che i fornitori possono consultare durante la registrazione.

Queste sezioni hanno effetto solo quando il modulo **Portale fornitori** è attivo; vedere [Portale fornitori](../../setup/supplier-portal/README.md) per l'attivazione.

### Portale fornitori: campi di invito aggiuntivi

Per impostazione predefinita i fornitori si registrano con i campi standard del layout fornitore. Questa sezione consente di richiedere inoltre campi dei dati anagrafici del fornitore (per esempio **VAT ID**, **Website**, **IBAN** o **Contact Person**) durante la registrazione.

1. Attivare l'interruttore **Portale fornitori Campi di invito aggiuntivi**.
2. Nel menu a discesa **Campi** che compare, selezionare uno o più campi. L'elenco contiene i campi definiti per il tipo di dati anagrafici del fornitore; se è vuoto, i campi anagrafici del fornitore non sono ancora stati configurati nell'organizzazione.
3. La selezione viene salvata automaticamente. I fornitori invitati vedono ora i campi selezionati nel modulo di registrazione.

### Stato

La sezione **Stato** definisce il flusso di lavoro attraversato dalla registrazione di un fornitore. Il pannello sinistro (**STATI DEL FLUSSO DI LAVORO**) elenca tutti gli stati in ordine; il pannello destro (**CONFIGURA STATO**) configura lo stato selezionato. Per la differenza tra stati di attivazione, invito, registrazione e approvazione, vedere [Portale fornitori — Comprendere accesso e stati](../../setup/supplier-portal/README.md#comprendere-accesso-e-stati).

<figure><img src="../../../.gitbook/assets/supplier-general-settings-status-approval-it-20261111.png" alt="Sezione Stato con lo stato di approvazione selezionato e il pannello Configura stato"><figcaption><p>Sezione <strong>Stato</strong>: a sinistra l'elenco <strong>STATI DEL FLUSSO DI LAVORO</strong> con il distintivo <em>Approval</em>, a destra il pannello <strong>CONFIGURA STATO</strong> dello stato selezionato con colore del distintivo, stato di approvazione, esportazione M3 e ruoli che possono approvare.</p></figcaption></figure>

* **Riordinare gli stati**: trascinare uno stato dalla maniglia alla sua sinistra. Il nuovo ordine viene salvato automaticamente.
* **Selezionare uno stato**: fare clic su uno stato dell'elenco per caricarlo nel pannello **CONFIGURA STATO**. Gli stati predefiniti sono bloccati: il nome e le impostazioni di approvazione non sono modificabili e non possono essere eliminati.
* **Nome dello stato**: digitare un nome per creare uno stato personalizzato (quando non è selezionato alcuno stato) oppure per rinominare lo stato personalizzato selezionato.
* **Colore del distintivo**: colore del punto che precede lo stato nell'elenco. Digitare un valore di colore nel campo (il valore predefinito è mostrato come **Colore predefinito**), sceglierlo con il contagocce oppure rimuoverlo con la × per tornare al colore standard.
* **Stato di approvazione**: attivare **Contrassegna questo come uno stato che richiede approvazione** se un fornitore può lasciare questo stato solo dopo un'approvazione esplicita. Lo stato mostra quindi il distintivo *Approval* nell'elenco.
* **Stato di esportazione M3**: questo interruttore compare per gli stati che richiedono approvazione e indica che l'approvazione di un fornitore in questo stato lo esporta in M3. È possibile selezionare un solo stato.
* **Chi può approvare?**: non appena uno stato richiede approvazione, scegliere quali ruoli possono approvarlo — **Admin** (la persona con accesso amministrativo), il **Referente** (la persona che ha segnalato il fornitore), l'**Assegnatario** (la persona a cui è assegnato il fornitore) e un numero qualsiasi di **Gruppi di utenti**. Negli stati predefiniti questa selezione non è modificabile.
* **Salva modifiche** salva lo stato selezionato; **Reimposta** svuota il modulo.
* **Eliminare uno stato personalizzato**: fare clic sull'icona del cestino accanto allo stato e confermare. Gli stati predefiniti non possono essere eliminati.

### Raggruppamento ID fornitore

Usare **Raggruppamento ID fornitore** quando lo stesso fornitore compare nel sistema con più ID fornitore (per esempio dopo una fusione o in stabilimenti diversi). Tutti gli ID di un gruppo vengono trattati come un unico fornitore nel portale fornitori.

1. Nel campo di testo inserire gli ID fornitore separati da virgole (per esempio `1001, 1002`).
2. Fare clic su **Creare un nuovo gruppo**. Ogni gruppo richiede almeno due ID; altrimenti viene mostrato un avviso e non viene creato alcun gruppo.
3. Ogni gruppo appare come riga di etichette ID, preceduta dall'etichetta del gruppo (**GROUP 1**, **GROUP 2** e così via). Le modifiche vengono salvate automaticamente.
4. **Modificare un gruppo**: fare clic sulla riga del gruppo, correggere l'elenco separato da virgole e poi fare clic su **Salva** (oppure su **Annulla** per scartare la modifica).
5. **Eliminare un gruppo**: fare clic sull'icona del cestino alla fine della riga.

### Carica il logo

#### Scopo

La funzione **Carica il logo** consente agli amministratori di personalizzare il portale fornitori caricando il logo della propria azienda. Questo migliora il riconoscimento del marchio e fornisce un'esperienza visiva coerente per gli utenti che accedono al portale.

#### Passaggi per caricare un logo

1. **Accedi alle Impostazioni Generali del Fornitore**:
   * Naviga alla sezione **Impostazioni Generali Del Fornitore** dal menu principale.
2. **Trova la sezione Carica il logo**:
   * Scorri verso il basso fino alla sezione **Carica il logo** all'interno della pagina delle impostazioni.
3. **Carica un nuovo logo**:
   * Clicca sull'area **Carica il logo** per aprire la finestra di selezione file.
   * Seleziona il file immagine che desideri caricare. I formati supportati includono tipicamente `.png`, `.jpg` o `.jpeg`.
   * Il logo caricato verrà visualizzato nell'area di anteprima.
4. **Salva il logo caricato**:
   * Una volta caricato il logo, clicca sul pulsante **Salva** per applicare le modifiche.
   * Il nuovo logo verrà ora visualizzato in tutto il portale fornitori.

#### Migliori pratiche

* **Dimensioni del logo**: assicurati che le dimensioni del logo siano ottimizzate per le visualizzazioni desktop e mobili. Il sistema potrebbe offrire linee guida o ridimensionamento automatico.
* **Dimensione del file**: utilizza un file immagine compresso per ridurre i tempi di caricamento e migliorare l'esperienza dell'utente.
* **Coerenza del marchio**: utilizza lo stesso logo su tutte le piattaforme per mantenere un'identità di marchio coerente.

### Politica e dichiarazione sulla privacy

#### Scopo

La sezione **Politica e dichiarazione sulla privacy** consente agli amministratori di caricare o definire i documenti legali che regolano l'uso del portale fornitori. Questi documenti sono critici per la conformità ai requisiti legali e normativi, delineando i termini di utilizzo, le politiche di protezione dei dati e altre informazioni essenziali per gli utenti.

#### Passaggi per caricare la politica e la dichiarazione sulla privacy

1. **Accedi alle Impostazioni Generali del Fornitore**:
   * Naviga alla sezione **Impostazioni Generali Del Fornitore** dal menu principale.
2. **Trova la sezione Politica e dichiarazione sulla privacy**:
   * Scorri verso il basso fino alla sezione **Politica e dichiarazione sulla privacy**.
3. **Carica o aggiorna i documenti**:
   * Clicca sul pulsante **Carica documento** per selezionare il file o i file rilevanti. Finché non è presente alcun documento, la sezione mostra l'avviso **È necessario caricare il documento di dichiarazione della politica.**
   * Scegli il file del documento dal tuo spazio di archiviazione locale. I formati supportati includono tipicamente `.pdf`, `.docx` o `.txt`.
   * I documenti caricati verranno elencati in questa sezione per la revisione.
4. **Salva le modifiche**:
   * Dopo aver caricato o aggiornato i documenti, clicca sul pulsante **Salva** per garantire che le nuove politiche siano applicate.

#### Migliori pratiche

* **Aggiornamenti regolari**: rivedi e aggiorna regolarmente la Politica e la dichiarazione sulla privacy per garantire che siano conformi ai più recenti requisiti legali e alle politiche aziendali.
* **Chiarezza e accessibilità**: assicurati che i documenti caricati siano chiari, concisi e accessibili a tutti gli utenti. Considera di fornire traduzioni se la tua base di fornitori è internazionale.
* **Revisione legale**: fai rivedere tutti i documenti da un legale prima di caricarli per garantire la conformità alle leggi e ai regolamenti pertinenti.

### Documenti di riferimento per la registrazione dei fornitori

Questa sezione contiene i documenti che assistono i fornitori durante la registrazione, per esempio un modulo di registrazione IVA o un modello di licenza di attività. I documenti caricati sono elencati in una tabella con le colonne **Nome**, **Tipo Di File** e **Azioni**.

<figure><img src="../../../.gitbook/assets/supplier-general-settings-reference-documents-it-20261111.png" alt="Sezione Documenti di riferimento con la tabella Nome, Tipo Di File e Azioni"><figcaption><p>Sezione <strong>Documenti di riferimento per la registrazione dei fornitori</strong> con il pulsante <strong>Caricare</strong> e la tabella dei documenti caricati.</p></figcaption></figure>

* **Caricare**: fare clic su **Caricare** e scegliere il file. Il documento compare nella tabella al termine del caricamento.
* **Aprire un documento**: fare clic sull'icona dell'occhio accanto al nome del documento (suggerimento **File di anteprima**); il documento si apre in una finestra di anteprima.
* **Copia**: aprire il menu con i tre punti nella colonna **Azioni** e scegliere **Copia**. Viene copiato negli appunti un link al documento, che si può incollare nelle proprie istruzioni.
* **Cancellare**: aprire lo stesso menu e scegliere **Cancellare**; il documento viene eliminato dopo la conferma dell'avviso.
