# Privilegi di amministratore

Il ruolo di un amministratore è fondamentale per la gestione dei sistemi IT, delle reti e delle piattaforme digitali in un'organizzazione. Un amministratore dispone di permessi e responsabilità avanzati che gli consentono di controllare vari aspetti dell'infrastruttura tecnica e di garantire che venga gestita in modo efficiente e sicuro. Ecco alcune delle principali responsabilità di un amministratore:

* **Gestione degli utenti:** gli amministratori gestiscono gli account utente, i diritti di accesso e i permessi. Creano nuovi account utente, assegnano loro i permessi necessari e gestiscono il controllo degli accessi per garantire che solo gli utenti autorizzati possano accedere a determinate risorse.
* **Sicurezza:** gli amministratori sono responsabili della sicurezza dei sistemi IT, per proteggerli dalla perdita di dati e dagli accessi non autorizzati.
* **Risoluzione dei problemi e supporto:** l'amministratore è spesso il primo punto di contatto per le questioni tecniche. Aiuta gli utenti a individuare e risolvere i problemi e garantisce che il sistema funzioni senza intoppi.

Oltre a queste responsabilità, gli amministratori hanno anche il compito di gestire le impostazioni sensibili e di garantire che i sistemi soddisfino i requisiti di conformità e le migliori pratiche di sicurezza delle informazioni. Ciò include la gestione dei dati sensibili, la configurazione dei controlli di accesso e dei permessi, e il monitoraggio e l'analisi dei registri di sistema per identificare e affrontare potenziali rischi per la sicurezza.

## Admin vs System Admin

DocBits dispone di due ruoli di amministratore: **Admin** e **System Admin**. Sembrano simili, ma svolgono compiti diversi. Ecco la versione semplice.

### Admin — una persona che gestisce la tua organizzazione

Un **Admin** è una persona reale del tuo team a cui è consentito gestire DocBits. Gli Admin possono:

* Aprire tutte le aree delle **Impostazioni** e modificare il funzionamento della tua organizzazione.
* Aggiungere nuovi utenti, modificarli, attivarli o disattivarli e decidere chi altro diventa Admin.
* Configurare gruppi, permessi, integrazioni e flussi di lavoro.

Puoi avere **tutti gli Admin di cui hai bisogno** e puoi assegnare o revocare il ruolo di Admin a qualsiasi utente in qualsiasi momento. La maggior parte degli amministratori del tuo team è di questo tipo.

### System Admin — l'account che DocBits utilizza per operare in autonomia

Un **System Admin** è **un unico account speciale per ogni organizzazione** che DocBits utilizza per le azioni che avvengono **automaticamente, senza che nessuno faccia clic su un pulsante** — ad esempio quando i documenti vengono importati dall'email, esportati verso un altro sistema o trasferiti in background da un servizio collegato.

Pensalo come l'account "robot" dell'organizzazione. Quando il sistema esegue qualcosa per conto proprio, lo fa **in qualità di System Admin**, in modo che l'attività automatica sia facile da riconoscere e non venga confusa con il lavoro dei membri reali del tuo team.

Un System Admin è speciale per tre motivi:

* **È sempre anche un Admin.** Scegliere System Admin conferisce automaticamente a quell'account anche i diritti completi di Admin.
* **Ne esiste uno solo per organizzazione.** Una volta che esiste un System Admin, non puoi designare un altro utente come System Admin.
* **Viene impostato solo al momento della creazione dell'utente.** Lo decidi nel momento in cui aggiungi l'utente. **Non può essere attivato o disattivato in seguito.**

> **Consiglio:** crea un account dedicato a questo scopo — ad esempio `system@your-company.com` — e contrassegnalo come System Admin. In questo modo, tutto ciò che DocBits fa automaticamente appare chiaramente come **System Admin** nei tuoi registri e nella cronologia dei documenti, separato dai tuoi utenti reali.

### In sintesi

| | Admin | System Admin |
|---|---|---|
| Accesso completo per gestire l'organizzazione | Sì | Sì |
| Quanti puoi averne | Tutti quelli necessari | Solo uno |
| Modificabile dopo la creazione dell'utente | Sì, in qualsiasi momento | No, impostabile solo alla creazione |
| Usato per azioni automatiche dietro le quinte | No | Sì |
| Dispone sempre dei diritti di Admin | — | Sì |

## Migliori pratiche di sicurezza

La sicurezza è un aspetto essenziale di qualsiasi organizzazione, specialmente quando si tratta di gestire account utente e diritti di accesso. Ecco alcune migliori pratiche per mantenere un protocollo di gestione degli utenti sicuro:

* **Aggiornamenti regolari delle password:** incoraggia gli utenti ad aggiornare regolarmente le proprie password per mantenere sicuri i propri account. Stabilisci politiche di complessità delle password e richiedi l'uso di password forti che includano una combinazione di lettere, numeri e caratteri speciali.
* **Monitorare le azioni degli amministratori:** implementa meccanismi per monitorare le attività degli amministratori al fine di rilevare attività sospette o insolite. Registra tutte le azioni degli amministratori, inclusi gli accessi a dati o impostazioni sensibili, per garantire la responsabilità e individuare potenziali violazioni della sicurezza.
* **Limitare il numero di amministratori:** riduci al minimo il numero di amministratori e concedi i privilegi amministrativi solo a chi ne ha davvero bisogno. Limitando il numero di amministratori, riduci il rischio di violazioni della sicurezza e rendi più semplice la gestione e il monitoraggio degli account utente.
* **Autenticazione a due fattori (2FA):** implementa un'autenticazione a due fattori per gli account amministratore per aumentare ulteriormente la sicurezza. Questo introduce un ulteriore passaggio di sicurezza che garantisce che, anche in caso di compromissione di una password, un malintenzionato non possa accedere in modo non autorizzato all'account.
* **Controlli di sicurezza regolari:** esegui controlli di sicurezza e audit regolari per identificare e risolvere potenziali falle o punti deboli. Verifica i diritti di accesso e i permessi degli account utente per assicurarti che siano conformi ai requisiti e alle migliori pratiche attuali.
* **Formazione e consapevolezza:** forma regolarmente i dipendenti e gli amministratori sulle migliori pratiche di sicurezza e sulla consapevolezza degli attacchi di phishing e di altre minacce informatiche. Rendili consapevoli dell'importanza della sicurezza e incoraggiali a segnalare le attività sospette.

Implementando queste migliori pratiche, le organizzazioni possono migliorare la sicurezza del proprio protocollo di gestione degli utenti e ridurre al minimo il rischio di violazioni della sicurezza e di perdita di dati. È importante considerare la sicurezza come un processo continuo e apportare aggiornamenti e adeguamenti regolari per tenere il passo con le minacce e i requisiti di sicurezza in continua evoluzione.
