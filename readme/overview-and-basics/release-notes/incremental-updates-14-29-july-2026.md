# Note della versione DocBits — 14–29 luglio 2026

_Cosa cambia con l'aggiornamento di produzione di DocBits del 29 luglio 2026
(l'aggiornamento del canale Nova), che copre tutto quanto rilasciato dopo la
release del 14 luglio. Per ogni servizio è indicata la versione ora in
produzione, seguita dalle novità e correzioni spiegate in linguaggio semplice.
I servizi non elencati non hanno avuto modifiche visibili ai clienti._

---

## Highlights

- **Autenticazione a due fattori.** Gli account DocBits possono ora essere
  protetti con un secondo fattore: un'app di autenticazione (TOTP), un codice
  monouso via e-mail oppure una passkey tramite Touch ID, Windows Hello,
  YubiKey e simili. I codici di backup coprono il caso di un dispositivo
  smarrito, e un dispositivo attendibile può saltare il secondo fattore per un
  certo periodo. Ogni utente può attivarla per sé; gli amministratori possono
  renderla obbligatoria per l'intera organizzazione. Consultate la
  [guida all'autenticazione a due fattori](../two-factor-authentication.md).
- **Ticket di supporto dalla schermata di errore.** Quando qualcosa va storto,
  potete ora aprire un ticket di supporto direttamente dal record di errore.
  Il ticket contiene già il contesto tecnico, quindi non dovete descriverlo
  voi.
- **E-mail in ingresso nella regione corretta.** Le organizzazioni USA
  ricevono indirizzi di importazione nella propria regione, e le caselle
  Microsoft 365 su tenant di cloud nazionali (GCC, 21Vianet e simili) possono
  ora essere configurate tramite una selezione Cloud Instance.
- **Stato del PO matching più chiaro.** Le fatture la cui tabella delle righe
  non poteva essere mappata venivano etichettate come "ordine d'acquisto non
  trovato", spingendo a cercare il problema sbagliato. Ora hanno un proprio
  stato "tabella incompleta", con il dettaglio a livello di colonna di cosa
  non è stato mappato.
- **Mappatura dei codici imposta per gli e-document.** Una nuova pagina di
  impostazioni mappa i vostri codici imposta ERP per i documenti elettronici,
  e le esportazioni verificano la mappatura in anticipo invece di fallire
  nell'ERP.
- **Ritirato il livello AI Turbo.** Il modello Turbo ha raggiunto il fine
  vita. Chi lo aveva selezionato è stato spostato automaticamente su Fast;
  non è richiesta alcuna azione.

---

## Web App — live: `10.46.2`

### Accesso

- **Autenticazione a due fattori:** configurate un'app di autenticazione, i
  codici via e-mail o una passkey dal vostro profilo, stampate i codici di
  backup e contrassegnate un dispositivo come attendibile, così da non dover
  ripetere la verifica ogni volta. Chi usa una passkey può accedere anche del
  tutto senza password. Gli amministratori dell'organizzazione dispongono di
  un interruttore per renderla obbligatoria e di una panoramica di adozione
  che mostra chi si è già registrato.
- **Account eliminati:** l'accesso con un account eliminato lo segnala
  esplicitamente, invece di fallire con un errore generico.
- **SSO:** corretto un errore all'accesso quando era selezionata una regione
  diversa. Le sessioni SSO scadono ora quando lo indica l'identity provider,
  e non secondo un timer locale fisso.

### Lavorare con i documenti

- **Documenti eliminati:** aprire un documento eliminato nel frattempo mostra
  un messaggio chiaro invece di errori di script.
- **Validazione dei campi:** il campo del numero di pagina è più largo e salta
  alla pagina premendo Invio. Un campo reso di sola lettura da uno script
  continua a mostrare la sua connessione campo. Un popup di avviso che
  stampava JavaScript grezzo mostra ora il messaggio effettivo, e la
  schermata non si blocca più sui documenti con lunghe tabelle di righe
  e-document.
- **Estrazione tabelle:** eliminare una colonna libera il suo nome per il
  riutilizzo, e le intestazioni eliminate non ricompaiono più nella tabella
  salvata.
- **Approvazioni:** aprire un documento appena passato in attesa porta alla
  schermata di approvazione corretta. Gli utenti non possono più approvare un
  passaggio Sales Tax per cui il loro gruppo non ha i permessi, e la
  cronologia delle approvazioni mostra di nuovo tutte le voci. La cronologia
  indica inoltre la persona che ha effettivamente approvato, incluse le
  approvazioni effettuate da un amministratore per conto dell'assegnatario.
- **Fornitori:** la pagina Accounting non mostra più un falso avviso
  "Supplier is missing", e l'eliminazione di un fornitore che esiste solo
  dall'estrazione non lascia più la finestra di dialogo bloccata.
- **Dati anagrafici:** le tabelle nella pagina dei dati anagrafici tornano a
  scorrere.
- **Attività e notifiche:** l'eliminazione di un'attività non è più riservata
  agli amministratori. Se gli utenti senza diritti di amministratore possano
  eliminare le proprie attività è ora un'impostazione dell'organizzazione, e
  gli utenti che hanno un'attività su un documento che non possono aprire
  ricevono una vista limitata all'attività invece di un errore.

### Dashboard e ricerca

- **Esportazione:** le esportazioni usano la dashboard che avete selezionato,
  e l'app vi avvisa prima di esportare una dashboard con modifiche non
  salvate.
- **Ricerca:** Invoice Type è disponibile come campo di ricerca con il suo
  elenco di valori. Quando un insieme di risultati supera quanto la Dashboard
  riesce a mostrare nella finestra, il badge del conteggio lo segnala invece
  di troncare l'elenco in silenzio.
- **Log di importazione:** i documenti suddivisi si trovano tramite il loro
  documento padre, e la colonna Failed Filenames elenca solo i file
  effettivamente falliti o saltati.

### Impostazioni e amministrazione

- **Ticket di supporto:** create un ticket direttamente da un record di
  errore. I ticket includono ambiente e canale di rilascio, e la cattura
  dello screenshot non si blocca più.
- **Gruppi e permessi:** i documenti non classificati possono essere concessi
  come permesso al pari di qualsiasi altro tipo di documento.
- **Workflow Builder:** le card appena create o rinominate, i modelli e-mail
  e le altre voci dei menu a tendina compaiono subito, senza ricaricare la
  pagina.
- **Alberi decisionali:** le etichette dei campi documento nel designer
  seguono la lingua dell'interfaccia, invece di mostrare sempre il nome
  inglese.
- **Tipi di documento:** nuova impostazione Structured Extraction nella
  sezione di estrazione.
- **Codici imposta E-Doc:** nuova pagina di impostazioni per mappare i vostri
  codici imposta ERP per i documenti elettronici (vedi Highlights).
- **Auto Accounting:** le dimensioni vengono mostrate in modo affidabile e
  non più a intermittenza.
- **Selezione del modello AI:** il livello Turbo ritirato è sparito dal menu
  a tendina; le selezioni esistenti mostrano Fast.
- **Finestra Versioni dei servizi:** ora è scorrevole, include il servizio
  Auth Bridge e mostra i nomi dei canali di rilascio Vesta e Nova.
- **Pagina di importazione:** non va più in errore per le organizzazioni con
  una voce di abbonamento vuota.

### Correzioni minori

Le notifiche toast vuote vengono soppresse, la finestra di creazione/modifica
delle idee è scorrevole, le caselle disallineate nelle impostazioni dei campi
sono di nuovo allineate, le eliminazioni di documenti bloccate spiegano il
motivo, e le impostazioni E-Document gestiscono correttamente il passaggio da
Default a Custom.

## API Service — live: `12.68.1`

- **Autenticazione a due fattori:** tutti i percorsi di login basati su
  password passano attraverso il controllo del secondo fattore, quindi
  nessuna rotta di integrazione riesce ad aggirarlo.
- **Codici imposta E-Doc:** mappatura dei codici imposta ERP per i documenti
  elettronici, con un controllo centrale prima dell'esportazione, così che i
  codici mancanti emergano subito.
- **Controllo degli accessi:** gli amministratori possono concedere agli
  utenti non amministratori la visibilità dei documenti non classificati.
- **Traccia di audit delle eliminazioni:** i documenti registrano chi li ha
  eliminati e quando.
- **Dashboard personali:** corrette le impostazioni di condivisione che non
  si salvavano.
- **Ricerca nella dashboard:** Invoice Type si aggiunge ai campi di ricerca
  estesi, e i documenti creati da una suddivisione per codice a barre o QR
  si trovano tramite il loro documento padre.
- **Dati sempre aggiornati nella Dashboard:** l'aggiornamento di una tabella
  o la rielaborazione di un documento svuota la cache della Dashboard, così
  l'elenco non mostra più i valori precedenti alla modifica.
- **Caricamenti:** caricamenti ripetuti dello stesso file durante un nuovo
  tentativo di rete non creano più documenti duplicati.
- **Ricerca fornitori:** i risultati arrivano appena i dati sono pronti,
  invece che dopo un'attesa fissa.
- **Esportazione Infor:** i prezzi unitari mantengono quattro decimali. Le
  esportazioni M3 possono includere addebiti di riga a importo zero, e le
  righe di costo LN negative vengono inviate come accrediti positivi.
  L'esportazione attende inoltre il completamento di un workflow in corso,
  invece di partire a metà workflow.
- **Approvazioni:** un'approvazione viene collegata a una richiesta di
  approvazione solo quando l'approvatore ne è l'assegnatario. Le modifiche
  che un workflow ha effettuato di propria iniziativa vengono attribuite
  all'utente System e non all'ultima persona che ha toccato il documento.
- **Stabilità del login:** un errore temporaneo nella validazione del token
  non disconnette più gli utenti; l'app riprova. Lo stesso vale per i
  documenti, che non falliscono più del tutto per un breve intoppo
  dell'autenticazione.
- **Classificazione:** le regole sulla provenienza confrontano ora tutti i
  campi di origine del documento, non posizioni fisse.
- **Stabilità della validazione:** un campo senza nome non manda più in
  errore la validazione del documento.
- **Modelli AI:** il livello Turbo (ritirato) viene rimappato ovunque su
  Fast, incluse le varianti fine-tuned, con una protezione che impedisce a
  un modello ritirato di essere eseguito.
- **Job in background:** uno scheduler bloccato viene rilevato e riavviato,
  così i job ricorrenti non possono fermarsi in silenzio.

## Auth Service — live: `1.75.3`

- **Autenticazione a due fattori:** il backend dietro la voce negli
  Highlights. App di autenticazione, codici monouso via e-mail, passkey e
  dispositivi attendibili, oltre a codici di backup, obbligo per
  organizzazione e login con passkey senza password. La registrazione
  disconnette le vostre altre sessioni, il cambio della password revoca i
  dispositivi attendibili, e gli endpoint di verifica sono soggetti a un
  limite di frequenza con blocco e a una protezione contro il riutilizzo dei
  codici.
- **Cronologia dei login:** gli accessi via SSO/SAML compaiono ora nella
  cronologia dei login, e il timestamp dell'ultimo accesso viene registrato
  in modo affidabile per ogni tipo di login. La visualizzazione della
  cronologia dei login di un altro utente richiede il livello di
  amministratore appropriato.
- **Account legacy:** l'eliminazione di un account utente legacy funziona di
  nuovo, invece di non fare nulla in silenzio.
- **Amministrazione utenti in blocco:** aggiungete in blocco utenti esistenti
  a sotto-organizzazioni e gruppi via CSV, con corrispondenza per indirizzo
  e-mail. Corretti anche un crash su righe CSV riempite in modo disomogeneo
  e un errore del server nell'aggiunta di due o più nuovi utenti insieme.
- **Elenchi membri:** gli utenti eliminati non compaiono più negli elenchi
  membri delle sotto-organizzazioni.
- **Single sign-on:** una serie di interventi di irrobustimento. I token
  scaduti restituiscono ora una risposta pulita di "scaduto", le
  organizzazioni senza configurazione SAML ricevono una corretta risposta
  not-found invece di un flusso di login sbagliato, il logout si completa
  sempre anche quando la richiesta di disconnessione non può essere
  verificata, e sono spariti diversi crash legati a configurazioni mancanti
  dell'identity provider. La durata del token restituita dal provider viene
  inoltre trasmessa all'app.
- **Token di sessione:** corretto il caso di token di sessione a breve durata
  rifiutati come non validi anche se non erano scaduti.
- **Strumenti di gestione:** la regione dell'organizzazione è visibile
  nell'API di gestione, l'utente di sistema di un'organizzazione può essere
  riassegnato, e l'amministrazione di piani e consumi ha ottenuto endpoint
  dedicati. Queste modifiche riguardano gli strumenti interni di DocBits,
  non l'app dei clienti.

## Email Service — live: `1.40.2`

- **Importazione nella regione corretta:** i domini e-mail in ingresso
  esistono per regione, e le mail arrivate nella regione sbagliata vengono
  inoltrate a quella giusta. Le organizzazioni USA non dipendono più dal
  percorso in ingresso UE.
- **Microsoft 365:** i tenant di cloud nazionali si configurano tramite una
  selezione Cloud Instance, correggendo le importazioni O365 per i clienti
  USA. Un tenant non valido produce ora un chiaro errore di login invece di
  un errore del server, e credenziali tenant incomplete falliscono subito
  con un messaggio invece che in silenzio.
- **Test di connessione:** il test di una casella IMAP che non risponde
  fallisce con un messaggio di timeout dopo pochi secondi, invece di
  incappare in un timeout del gateway.
- **Ordine nella casella:** le e-mail senza allegati vengono spostate fuori
  dalla casella invece di accumularsi.
- **Nessun duplicato sui nuovi tentativi:** i caricamenti verso l'API
  documenti portano una chiave di idempotenza, quindi una consegna ritentata
  non può creare due volte lo stesso documento.
- **Nomi delle sorgenti:** le sorgenti O365 con una cartella configurata
  includono l'e-mail dell'account nel proprio nome, così sorgenti simili
  restano distinguibili. L'indirizzo della casella viene letto dall'account
  autenticato e non più da un campo digitato a mano.
- **Pulizia del log di importazione:** le voci del log di importazione
  vengono conservate per 90 giorni e poi eliminate automaticamente.

## PO Match Service — live: `1.59.3`

- **Stato "tabella incompleta":** le fatture la cui tabella delle righe non
  poteva essere mappata ricevono un proprio stato invece del fuorviante
  "ordine d'acquisto non trovato" (vedi Highlights). La dashboard lo mostra
  con l'icona di mancata corrispondenza.
- **Dettaglio errori migliore:** gli errori di mappatura della tabella
  indicano la colonna specifica che non è stata mappata.
- **Più rapido sulle fatture di grandi dimensioni:** la corrispondenza basata
  su regole raggruppa i candidati per numero di articolo e legge le
  impostazioni di tolleranza una volta per organizzazione, invece che una
  volta per riga.
- **Comportamento API più pulito:** le richieste di regole PO inesistenti
  restituiscono una corretta risposta not-found, e le voci di cache corrotte
  vengono scartate invece di causare errori ripetuti.
- **Corrispondenza sul totale:** corretto un bug nella corrispondenza
  rispetto al totale dell'ordine d'acquisto.

## Fulltext Service — live: `1.39.1`

- **Formati numerici europei:** gli importi scritti con la virgola decimale
  (`1.234,56`) vengono normalizzati prima dell'indicizzazione, quindi le
  ricerche e i filtri sugli importi funzionano a prescindere dal formato
  numerico.
- **Conteggi dei risultati veritieri:** quando una ricerca trova più documenti
  di quanti la finestra della dashboard ne restituisca, la risposta lo
  segnala invece di presentare come completo un elenco troncato.
- **Conteggi ERP:** corretto un errore di token che poteva interrompere il
  flusso dei conteggi in tempo reale sulla dashboard.
- **Resilienza dell'indicizzazione:** l'indicizzazione supera ora i
  disservizi temporanei del database e del servizio di autenticazione (nuovo
  tentativo automatico, fallback sul database primario) e scarta i messaggi
  di coda malformati invece di ritentarli all'infinito.

## OCR Service — live: `1.10.3`

- **Ordine di lettura stabile:** il testo viene letto in un ordine
  deterministico, quindi lo stesso documento viene estratto sempre allo
  stesso modo.
- **Documenti di grandi dimensioni:** il budget di tempo OCR cresce con la
  dimensione del documento, quindi i file molto grandi non falliscono più
  per timeout.
- **Caratteri inusuali:** un sanitizzatore ripulisce i caratteri che il
  motore OCR non può rappresentare, correggendo gli errori su documenti con
  simboli esotici.
- **Meno errori transitori:** gli errori temporanei di connessione allo
  storage vengono ritentati automaticamente, e un worker in stallo viene
  riconosciuto in base al fatto che stia effettivamente consumando lavoro.

## Extraction Service — live: `1.53.3`

- **Fatture USA a imposta zero:** corretto un caso in cui la coppia corretta
  netto/imposta veniva scartata quando l'importo dell'imposta è zero.
- **Estrazione tabelle:** le tabelle restano modificabili quando la mappatura
  configurata prevede più colonne di quante il documento ne fornisca, ed è
  stato corretto un crash su dati di riga inusuali.
- **Ordine di lettura stabile:** rispecchia la modifica dell'OCR qui sopra,
  così l'estrazione vede lo stesso ordine dei token prodotto dall'OCR.
- **Modelli AI:** ritiro del livello Turbo, in linea con l'API Service.

## Docflow Service — live: `2.7.3`

- **PO matching nei workflow:** i valori di confronto mancanti vengono
  trattati come dati mancanti, non come una mancata corrispondenza.
- **Card di conferma d'ordine:** acquirente e responsabile vengono risolti
  in modo affidabile.
- **Card di offerta:** il log registra ora i casi in cui un prezzo di offerta
  esiste ma cade fuori dall'intervallo di date consentito, che in precedenza
  sembravano dati mancanti.
- **Spese di trasporto:** quando nessuna delle due parti ha spese, il caso
  viene risolto dalla card dell'operatore invece di rimanere in stallo.
- **Sicurezza:** i token API dei workflow vengono validati rispetto
  all'organizzazione a cui appartengono.
- **Attivazione più rapida:** il controllo dei workflow attivi viene messo in
  cache, e i worker in background si riavviano in modo pulito invece di
  lasciare processi in stallo.

## Barcode Service — live: `1.18.1`

- **Suddivisioni di lunga durata:** la connessione alla coda dei task resta
  attiva durante i job barcode prolungati, quindi la suddivisione di batch
  di grandi dimensioni non si blocca più verso la fine.

## FTP Service — live: `1.31.2`

- **Pulizia del log di importazione:** stessa conservazione di 90 giorni e
  stessa pulizia automatica dell'Email Service.

## Auth Bridge Service — live: `0.4.1`

- **Avvisi di replica accurati:** il bridge di replica degli account UE/USA
  misura uno stallo a partire dall'ultimo progresso reale invece che dal
  primo errore, e conta come progresso solo un movimento di replica
  effettivo. Gli avvisi notturni fasulli di "bridge in stallo" sono spariti.
  Nell'app non cambia nulla.

## Operator Service — live: `1.42.1`

- **Stabilità dei worker:** un worker in stallo viene riconosciuto in base al
  fatto che stia consumando lavoro, e le comunicazioni superflue tra worker
  sono state disattivate.

---

## Invariati in questa release

**Auto Accounting** (`1.21.1`) è stato ricompilato senza modifiche visibili ai
clienti. **Docnet** (`1.55.1`) e **Ideas** (`0.3.1`) non presentano modifiche
in questa finestra.

<!-- Generated by the docbits-changelog skill. Boundary: versions live in the
     prod namespace on 28 Jul 2026 (Web App 10.41.8, API 12.57.8, Auth 1.71.1)
     up to the versions live in the sandbox namespace the same day, which is
     what the 29 July upgrade promotes. Re-check the version headers on the
     morning of the upgrade in case anything else lands on sandbox first.
     Manage Layouts and Custom Validation Rules stay excluded: DOCB-13719 gates
     both behind a beta query parameter, so they are not generally available in
     10.46.2. The hourly password for script changes (DOCB-13673) was added and
     then reverted inside this window, so it must not be announced. -->
