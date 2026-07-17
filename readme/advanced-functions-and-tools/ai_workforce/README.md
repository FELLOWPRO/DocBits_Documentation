# AI Workforce

<figure><img src="../../.gitbook/assets/docnet-agents-infographic-en.png" alt="AI Workforce Agents Infographic"><figcaption><p>Il sistema multi-agente di DocBits per l'elaborazione autonoma dei documenti</p></figcaption></figure>

## Panoramica

**AI Workforce** è il livello di orchestrazione all'interno di DocBits che trasforma il lavoro in arrivo in agenti IA coordinati. Invece di far seguire ogni passaggio a una persona, prende un'unità di lavoro in arrivo — un'e-mail, un messaggio di chat in Microsoft Teams o Discord, un'azione manuale nell'interfaccia o una chiamata API — e la porta a termine: classifica il documento, estrae e convalida i campi, esegue l'abbinamento con gli ordini di acquisto e i dati anagrafici ed esporta verso l'ERP, mantenendo le persone coinvolte dove è importante.

Consideralo come un team che gestisci piuttosto che uno strumento che utilizzi. Ogni attività segue la stessa struttura fissa:

* Un **Orchestratore** riceve una **Missione** (un'unità di lavoro), la pianifica e la delega.
* Il piano viene suddiviso in **Problemi** (attività singole), ciascuno gestito da un **agente Specialista** o da una **persona**.
* Gli Specialisti riferiscono i risultati e l'Orchestratore sintetizza l'esito.

Gli _agenti_ che ricoprono questi ruoli non sono fissi: DocBits include un **DocBits Orchestrator** pronto all'uso e due Specialisti predefiniti, e puoi crearne di tuoi (vedi [Agenti](./#agents)).

Un'esecuzione tipica, dall'inizio alla fine: una fattura arriva via e-mail → viene creata una Missione → l'Orchestratore la pianifica e assegna i Problemi agli Specialisti (classificazione, estrazione, convalida, abbinamento OdA) → un passaggio sensibile si mette in pausa nella **Posta in arrivo** in attesa dell'approvazione di una persona → dopo l'approvazione il documento viene esportato e la Missione si completa. Puoi monitorare l'intero processo dalla **Dashboard**, tenere insieme le esecuzioni correlate nei **Progetti** e intervenire tramite la **Posta in arrivo** e i **Problemi** ogni volta che è necessaria una decisione umana.

## Come attivarla

AI Workforce si abilita per ogni organizzazione dalle impostazioni principali.

1. Vai su **Impostazioni → Moduli**.
2. Attiva il modulo **AI Workforce**.
3. Conferma l'abbonamento nella finestra di dialogo che appare.

Una volta abilitata, **AI Workforce** appare nella barra di navigazione principale e lo spazio di lavoro diventa disponibile per la tua organizzazione.

## Dashboard

La **Dashboard** è la tua panoramica dell'AI Workforce — KPI, grafici ed elenchi di attività a colpo d'occhio. Sei tu a scegliere quali metriche visualizzare.

Per configurare le metriche attive, apri le **Impostazioni** (icona a forma di ingranaggio) e usa il pannello **Widget della dashboard**. Attiva o disattiva ogni widget e premi **Salva**; la tua selezione viene memorizzata come preferenza personale, così ogni utente può personalizzare la propria vista.

I widget disponibili includono:

* **Monitoraggio della flotta** — stato in tempo reale di tutti i tuoi agenti.
* **Schede KPI** — Problemi aperti, Missioni attive, Agenti abilitati, Esecuzioni di oggi, Utilizzo dei token e Approvazioni in sospeso.
* **Grafici** — andamento dei problemi nel tempo, missioni per stato, ricezione di e-mail, problemi per priorità, esecuzioni al giorno e utilizzo dei token per agente.
* **Elenchi** — missioni attive, attività recenti, approvazioni in sospeso, i tuoi problemi aperti, agenti al lavoro ed elementi bloccati.

## Posta in arrivo

La **Posta in arrivo** è il luogo in cui il lavoro attende l'**attenzione umana**. Quando un agente sta per eseguire uno strumento che richiede un'approvazione, mette in pausa l'attività e genera qui una **richiesta di approvazione**. Questo è l'Human-in-the-Loop (HITL): l'azione non viene eseguita finché una persona non decide. Se un determinato strumento richieda o meno un'approvazione dipende dalla **modalità di approvazione** dell'agente e dai contrassegni **critico** dei suoi strumenti (vedi [Impostazioni dell'agente](./#agent-settings)).

Ogni elemento della Posta in arrivo mostra il titolo della richiesta, l'agente che l'ha generata e una breve descrizione di ciò che richiede una decisione. Dall'elemento puoi:

* **Approva** — consenti all'agente di procedere con l'azione.
* **Rifiuta** — interrompi l'azione.
* **Commenta / invia un messaggio** — fornisci all'agente istruzioni alternative prima che continui.
* **Apri missione** — passa alla missione a cui appartiene questo elemento per avere il contesto completo.

Gli elementi restano **In attesa** finché qualcuno non interviene, poi diventano **Risolti** (oppure **Ignorati** se l'elemento viene messo da parte senza una decisione — ad esempio quando la relativa missione viene annullata). La voce di navigazione Posta in arrivo mostra un badge con il numero di approvazioni in sospeso, così nulla di critico viene perso.

## Missioni

Una **Missione** è l'unità di lavoro di livello superiore e l'esecuzione dell'agente che persegue un singolo obiettivo. Ogni missione può coinvolgere più attività ed è coordinata da un **agente Orchestratore**, che pianifica il lavoro, lo delega come Problemi agli Specialisti, ne osserva i risultati e sintetizza l'esito.

Una missione viene creata a partire dalla sua **origine** — E-mail, Chat (Microsoft Teams o Discord), Mission Control (manuale) o l'API — e mantiene quel contesto per tutta la sua durata. Puoi avviarne una tu stesso da **Mission Control** descrivendo in linguaggio naturale ciò che vuoi ottenere; da lì se ne occupa l'Orchestratore.

Le missioni attraversano i seguenti stati:

| Stato                          | Significato                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------- |
| **Pianificazione**             | L'Orchestratore sta analizzando la richiesta e costruendo un piano.             |
| **In elaborazione** _(Attiva)_ | Gli agenti Specialisti stanno eseguendo i problemi pianificati.                  |
| **In attesa di approvazione**  | La missione è in pausa, in attesa di una decisione umana nella Posta in arrivo. |
| **Completata**                 | Tutti i problemi sono stati risolti e l'obiettivo della missione è raggiunto.   |

Le missioni possono anche essere **In pausa** o **Annullate**. Dalla vista di dettaglio di una missione puoi seguirne l'**avanzamento**, esaminare i **problemi** collegati, vedere il tempo e l'utilizzo dei token, aprire la **linea temporale** degli eventi e **riavviare**, **modificare** o **eliminare** la missione.

## Problemi

Un **Problema** è una singola attività creata per raggiungere una parte dell'obiettivo di una missione — ad esempio _importa un documento_, _invia una risposta al mittente_ o _approva manualmente un passaggio_. I problemi sono gestiti dagli **agenti Specialisti** e dalle **persone**, che lavorano insieme sulla stessa attività.

Ogni problema porta con sé il contesto di cui il suo assegnatario ha bisogno e attraversa il proprio ciclo di vita (Da fare / In corso → In revisione → Fatto, oppure Errore / Annullato). I problemi possono essere assegnati a un agente o a una persona, possono avere una priorità (Critica, Alta, Media, Bassa), essere collegati a una missione e discussi tramite commenti.

Puoi visualizzare tutti i problemi, filtrarli per stato, priorità, assegnatario o missione, raggrupparli per stato, priorità o assegnatario e vedere **I miei problemi** — le attività assegnate a te. Creare un problema manualmente ti permette di aggiungere lavoro per un agente o un collega direttamente in una missione.

## Progetti

I **Progetti** sono cartelle che raggruppano **Missioni** correlate — ad esempio _tutte le fatture di un determinato fornitore nel Q1_, poi un altro progetto per il _Q2_ e così via. Mantengono organizzato e facilmente reperibile un grande volume di esecuzioni degli agenti.

Quando crei un progetto gli assegni:

* un **Nome** — ad es. _"Fatture Acme Q1"_;
* una **Descrizione** facoltativa — di cosa tratta il progetto e quale risultato ti aspetti;
* una **Data di scadenza** facoltativa — la data fino alla quale il progetto deve rimanere attivo.

Un progetto è **Attivo** o **Completato**. Un progetto con una data di scadenza **resta attivo finché non viene raggiunta quella data**, poi si completa automaticamente — così una raccolta trimestrale si chiude da sola alla fine del trimestre (il controllo viene eseguito una volta al giorno). Un progetto senza data di scadenza rimane attivo finché non lo completi tu stesso. Puoi anche completare o riaprire un progetto manualmente in qualsiasi momento. Da un progetto puoi vedere quante missioni contiene e collegarvi ulteriori missioni.

## Agenti

Gli agenti sono i lavoratori. Ogni agente ha un **ruolo** che determina cosa fa nel flusso Orchestratore → Missioni → Problemi:

* **Orchestratore** — coordina il lavoro tra più agenti. Riceve una missione, la pianifica, ne delega i passaggi come problemi e sintetizza i risultati. Un Orchestratore è indispensabile perché le missioni possano essere eseguite.
* **Specialista** — esegue un'attività specifica come importare un documento o inviare una risposta e-mail, e riferisce al proprio Orchestratore.

DocBits fornisce l'AI Workforce pronta all'uso, con questi agenti predefiniti:

* **DocBits Orchestrator** — l'Orchestratore predefinito.
* **Document Processor** — importa ed elabora i documenti caricati.
* **Email Reply** — compone e invia le risposte al mittente.

Questi sono **agenti di sistema**: puoi configurarne alcune parti, ma non puoi eliminarli. Puoi anche creare i tuoi Orchestratori e Specialisti insieme ad essi.

### Regole di gerarchia e attivazione

Poiché un Orchestratore è indispensabile per eseguire qualsiasi missione, l'attivazione segue alcune regole:

* Gli **Orchestratori** hanno un interruttore di **abilitazione/disabilitazione**, ma un Orchestratore può essere **disattivato solo se esistono almeno due Orchestratori** — il sistema non ti consente mai di spegnere l'ultimo, poiché non resterebbe nulla a coordinare le missioni.
* Quando è attivo **più di un Orchestratore**, il **System Router** diventa automaticamente attivo. Il suo compito è esaminare ogni missione in arrivo e delegarla all'Orchestratore giusto. Con un solo Orchestratore, il router non è necessario e resta in disparte.
* **Gli Specialisti non hanno un interruttore di abilitazione/disabilitazione.** Controlli invece dove possono operare **assegnandoli agli Orchestratori** (vedi _Agent Pool_ più avanti). Uno Specialista non assegnato ad alcun Orchestratore non è affatto disponibile — rimane nell'elenco ma nessun Orchestratore può delegargli lavoro, quindi ogni Specialista deve essere assegnato ad almeno un Orchestratore per poter essere utilizzato.

Puoi visualizzare e riorganizzare queste relazioni nell'**Org Chart**, che mostra Router → Orchestratori → Specialisti.

### Impostazioni dell'agente

Ogni agente — di sistema o personalizzato — dispone di un menu di impostazioni con le seguenti sezioni:

* **Prompt** — il prompt di sistema di base dell'agente. _Di sola lettura sugli agenti di sistema._
* **Impostazioni** — il **modello** dell'agente e il suo **sforzo di ragionamento**. L'AI Workforce funziona su un unico modello capace di ragionamento (**DocBits Pro**), quindi invece di manopole di basso livello c'è un solo comando — lo **Sforzo di ragionamento** (Reasoning Effort) — che controlla quanto intensamente pensa l'agente (e quindi quanto costa):
  * **None** — il più veloce ed economico; nessun ragionamento.
  * **Low** — attività rapide, ragionamento leggero.
  * **Medium** _(predefinito)_ — qualità e costo in equilibrio.
  * **High** — ragionamento approfondito per attività più difficili; costo più elevato.
  * **X-High** — ragionamento massimo; costo più elevato.
* **Modalità di approvazione** — quanta parte del lavoro dell'agente necessita di approvazione umana nella [Posta in arrivo](./#inbox):
  * **None** — l'agente esegue automaticamente ogni strumento; nulla viene inviato per l'approvazione.
  * **Critical** _(predefinito)_ — solo gli strumenti contrassegnati come **critici** richiedono l'approvazione; tutto il resto viene eseguito automaticamente. Gli strumenti critici sono le azioni sensibili di scrittura/esterne (ad esempio _carica/importa documento_, _aggiorna i campi del documento_, _rispondi all'e-mail_, _invia notifica_). In questa modalità uno strumento critico genera **sempre** una richiesta di approvazione nella Posta in arrivo. Puoi regolare finemente i singoli strumenti (contrassegnare come bisognoso di approvazione uno strumento normalmente sicuro, oppure rimuoverla da uno critico) — queste sostituzioni per singolo strumento si applicano solo in modalità Critical.
  * **All** — ogni strumento eseguito dall'agente richiede l'approvazione.
*   **Istruzioni personalizzate** — testo libero in cui descrivi le abitudini di lavoro dell'agente (questo è modificabile anche sugli agenti di sistema). Il modello predefinito appare così:

    > **Classificazione:** usa il classificatore di DocBits sul documento caricato. Affidati all'oggetto/corpo dell'e-mail solo quando non è stato allegato alcun documento.
    >
    > **Sostituzioni dei campi:** nessuna — accetta i valori dell'estrazione così come sono.
    >
    > **Approvazione:** non configurata. (Per richiedere l'approvazione umana per azioni specifiche, indica l'azione e la soglia.)
    >
    > **Assegnazione ai progetti:** confronta con le descrizioni dei progetti; preferisci lasciare la missione non assegnata piuttosto che forzare un abbinamento inadeguato. (Per sovrascrivere, elenca parole chiave o schemi del mittente: ad es. `supplier@acme.com → Acme Onboarding`.)
* **Competenze** — gli strumenti che l'agente è autorizzato a usare (ad esempio _carica documenti_ o _elenca utenti_). Ogni strumento è **critico** (azioni sensibili di scrittura/esterne) o non critico, il che determina il comportamento di approvazione descritto sopra. _Non modificabile sugli agenti di sistema._
* **Agent Pool** — _solo per gli Orchestratori._ Un elenco degli agenti disponibili, in cui selezioni a quali Specialisti questo Orchestratore può delegare il lavoro. Uno Specialista deve essere assegnato qui a un Orchestratore (o a un altro Orchestratore) per svolgere qualsiasi lavoro; uno lasciato ovunque non assegnato non è affatto disponibile.

### Creazione di agenti personalizzati

Oltre a quelli predefiniti, puoi creare i tuoi **Orchestratori** e **Specialisti** per adattarli ai tuoi processi. Apri **Agenti → Crea agente** per avviare la procedura guidata, che ripercorre la stessa configurazione descritta sopra: scegli il **ruolo** (Orchestratore o Specialista), assegna all'agente un **nome** e una chiara **descrizione** (un Orchestratore viene scelto in base a questo testo, e un Orchestratore seleziona i propri Specialisti in base al loro), scrivi il suo prompt, scegli le sue competenze, imposta il suo sforzo di ragionamento e — per gli Orchestratori — scegli gli Specialisti nel suo Agent Pool. Gli agenti personalizzati possono essere modificati o eliminati completamente in qualsiasi momento.
