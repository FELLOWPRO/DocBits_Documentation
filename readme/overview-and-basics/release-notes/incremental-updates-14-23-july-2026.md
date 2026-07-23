# Note della versione DocBits — 14–23 luglio 2026

_Cosa cambia con l'aggiornamento di produzione di DocBits del 23 luglio 2026
(l'aggiornamento del canale Nova), che copre tutto quanto rilasciato dopo la
release del 14 luglio. Per ogni servizio è indicata la versione ora in
produzione, seguita dalle novità e correzioni spiegate in linguaggio semplice.
I servizi non elencati non hanno avuto modifiche visibili ai clienti._

---

## Highlights

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
- **Le modifiche agli script sono protette da password.** Gli script
  personalizzati possono cambiare il modo in cui i documenti vengono
  elaborati, quindi ogni modifica a uno script richiede ora una password che
  ruota ogni ora. Chiedete quella corrente al vostro amministratore.
- **Ritirato il livello AI Turbo.** Il modello Turbo ha raggiunto il fine
  vita. Chi lo aveva selezionato è stato spostato automaticamente su Fast;
  non è richiesta alcuna azione.

---

## Web App — live: `10.45.1`

### Lavorare con i documenti

- **Documenti eliminati:** aprire un documento eliminato nel frattempo mostra
  un messaggio chiaro invece di errori di script.
- **Validazione dei campi:** il campo del numero di pagina è più largo e
  salta alla pagina premendo Invio. Un campo reso di sola lettura da uno
  script continua a mostrare la sua connessione campo.
- **Estrazione tabelle:** eliminare una colonna libera il suo nome per il
  riutilizzo, e le intestazioni eliminate non ricompaiono più nella tabella
  salvata.
- **Approvazioni:** gli utenti non possono più approvare un passaggio Sales
  Tax per cui il loro gruppo non ha i permessi, e la cronologia delle
  approvazioni mostra di nuovo tutte le voci. La cronologia indica inoltre la
  persona che ha effettivamente approvato, incluse le approvazioni effettuate
  da un amministratore per conto dell'assegnatario.
- **Fornitori:** la pagina Accounting non mostra più un falso avviso
  "Supplier is missing", e l'eliminazione di un fornitore che esiste solo
  dall'estrazione non lascia più la finestra di dialogo bloccata.
- **Attività e notifiche:** l'opzione di eliminazione è nascosta agli utenti
  senza diritti di amministratore.

### Dashboard e ricerca

- **Esportazione:** le esportazioni usano la dashboard che avete selezionato,
  e l'app vi avvisa prima di esportare una dashboard con modifiche non
  salvate.
- **Ricerca:** Invoice Type è disponibile come campo di ricerca con il suo
  elenco di valori.
- **Log di importazione:** i documenti suddivisi si trovano tramite il loro
  documento padre, e la colonna Failed Filenames elenca solo i file
  effettivamente falliti o saltati.

### Accesso

- **Account eliminati:** l'accesso con un account eliminato lo segnala
  esplicitamente, invece di fallire con un errore generico.
- **SSO:** corretto un errore all'accesso quando era selezionata una regione
  diversa.

### Impostazioni e amministrazione

- **Ticket di supporto:** create un ticket direttamente da un record di
  errore. I ticket includono ambiente e canale di rilascio, e la cattura
  dello screenshot non si blocca più.
- **Workflow Builder:** le card appena create o rinominate, i modelli e-mail
  e le altre voci dei menu a tendina compaiono subito, senza ricaricare la
  pagina.
- **Tipi di documento:** nuova impostazione Structured Extraction nella
  sezione di estrazione.
- **Codici imposta E-Doc:** nuova pagina di impostazioni per mappare i vostri
  codici imposta ERP per i documenti elettronici (vedi Highlights).
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

## API Service — live: `12.64.3`

- **Sicurezza degli script:** le modifiche agli script richiedono una
  password a tempo (vedi Highlights).
- **Codici imposta E-Doc:** mappatura dei codici imposta ERP per i documenti
  elettronici, con un controllo centrale prima dell'esportazione, così che i
  codici mancanti emergano subito.
- **Controllo degli accessi:** gli amministratori possono concedere agli
  utenti non amministratori la visibilità dei documenti non classificati.
- **Dashboard personali:** corrette le impostazioni di condivisione che non
  si salvavano.
- **Ricerca nella dashboard:** Invoice Type si aggiunge ai campi di ricerca
  estesi, e i documenti creati da una suddivisione per codice a barre o QR
  si trovano tramite il loro documento padre.
- **Caricamenti:** caricamenti ripetuti dello stesso file durante un nuovo
  tentativo di rete non creano più documenti duplicati.
- **Ricerca fornitori:** i risultati arrivano appena i dati sono pronti,
  invece che dopo un'attesa fissa.
- **Esportazione Infor:** i prezzi unitari mantengono quattro decimali. Le
  esportazioni M3 possono includere addebiti di riga a importo zero, e le
  righe di costo LN negative vengono inviate come accrediti positivi.
- **Approvazioni:** un'approvazione viene collegata a una richiesta di
  approvazione solo quando l'approvatore ne è l'assegnatario.
- **Stabilità del login:** un errore temporaneo nella validazione del token
  non disconnette più gli utenti; l'app riprova.
- **Classificazione:** le regole sulla provenienza confrontano ora tutti i
  campi di origine del documento, non posizioni fisse.
- **Stabilità della validazione:** un campo senza nome non manda più in
  errore la validazione del documento.
- **Modelli AI:** il livello Turbo (ritirato) viene rimappato ovunque su
  Fast, incluse le varianti fine-tuned, con una protezione che impedisce a
  un modello ritirato di essere eseguito.

## Auth Service — live: `1.72.8`

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
  dell'identity provider.
- **Token di sessione:** corretto il caso di token di sessione a breve durata
  rifiutati come non validi anche se non erano scaduti.
- **Strumenti di gestione:** la regione dell'organizzazione è visibile
  nell'API di gestione, l'utente di sistema di un'organizzazione può essere
  riassegnato, e l'amministrazione di piani e consumi ha ottenuto endpoint
  dedicati. Queste modifiche riguardano gli strumenti interni di DocBits,
  non l'app dei clienti.

## Email Service — live: `1.39.9`

- **Importazione nella regione corretta:** i domini e-mail in ingresso
  esistono per regione, e le mail arrivate nella regione sbagliata vengono
  inoltrate a quella giusta. Le organizzazioni USA non dipendono più dal
  percorso in ingresso UE.
- **Microsoft 365:** i tenant di cloud nazionali si configurano tramite una
  selezione Cloud Instance, correggendo le importazioni O365 per i clienti
  USA. Un tenant non valido produce ora un chiaro errore di login invece di
  un errore del server, e credenziali tenant incomplete falliscono subito
  con un messaggio invece che in silenzio.
- **Ordine nella casella:** le e-mail senza allegati vengono spostate fuori
  dalla casella invece di accumularsi.
- **Nessun duplicato sui nuovi tentativi:** i caricamenti verso l'API
  documenti portano una chiave di idempotenza, quindi una consegna ritentata
  non può creare due volte lo stesso documento.
- **Nomi delle sorgenti:** le sorgenti O365 con una cartella configurata
  includono l'e-mail dell'account nel proprio nome, così sorgenti simili
  restano distinguibili.
- **Pulizia del log di importazione:** le voci del log di importazione
  vengono conservate per 90 giorni e poi eliminate automaticamente.

## PO Match Service — live: `1.59.1`

- **Stato "tabella incompleta":** le fatture la cui tabella delle righe non
  poteva essere mappata ricevono un proprio stato invece del fuorviante
  "ordine d'acquisto non trovato" (vedi Highlights). La dashboard lo mostra
  con l'icona di mancata corrispondenza.
- **Dettaglio errori migliore:** gli errori di mappatura della tabella
  indicano la colonna specifica che non è stata mappata.
- **Comportamento API più pulito:** le richieste di regole PO inesistenti
  restituiscono una corretta risposta not-found, e le voci di cache corrotte
  vengono scartate invece di causare errori ripetuti.
- **Corrispondenza sul totale:** corretto un bug nella corrispondenza
  rispetto al totale dell'ordine d'acquisto.

## Fulltext Service — live: `1.38.3`

- **Formati numerici europei:** gli importi scritti con la virgola decimale
  (`1.234,56`) vengono normalizzati prima dell'indicizzazione, quindi le
  ricerche e i filtri sugli importi funzionano a prescindere dal formato
  numerico.
- **Conteggi ERP:** corretto un errore di token che poteva interrompere il
  flusso dei conteggi in tempo reale sulla dashboard.
- **Resilienza dell'indicizzazione:** l'indicizzazione supera ora i
  disservizi temporanei del database e del servizio di autenticazione (nuovo
  tentativo automatico, fallback sul database primario) e scarta i messaggi
  di coda malformati invece di ritentarli all'infinito.

## OCR Service — live: `1.9.9`

- **Documenti di grandi dimensioni:** il budget di tempo OCR cresce con la
  dimensione del documento, quindi i file molto grandi non falliscono più
  per timeout.
- **Caratteri inusuali:** un sanitizzatore ripulisce i caratteri che il
  motore OCR non può rappresentare, correggendo gli errori su documenti con
  simboli esotici.
- **Meno errori transitori:** gli errori temporanei di connessione allo
  storage vengono ritentati automaticamente.

## Extraction Service — live: `1.52.0`

- **Fatture USA a imposta zero:** corretto un caso in cui la coppia corretta
  netto/imposta veniva scartata quando l'importo dell'imposta è zero.
- **Estrazione tabelle:** le tabelle restano modificabili quando la mappatura
  configurata prevede più colonne di quante il documento ne fornisca, ed è
  stato corretto un crash su dati di riga inusuali.
- **Modelli AI:** ritiro del livello Turbo, in linea con l'API Service.

## Docflow Service — live: `2.7.2`

- **PO matching nei workflow:** i valori di confronto mancanti vengono
  trattati come dati mancanti, non come una mancata corrispondenza.
- **Card di conferma d'ordine:** acquirente e responsabile vengono risolti
  in modo affidabile.
- **Spese di trasporto:** quando nessuna delle due parti ha spese, il caso
  viene risolto dalla card dell'operatore invece di rimanere in stallo.
- **Sicurezza:** i token API dei workflow vengono validati rispetto
  all'organizzazione a cui appartengono.
- **Attivazione più rapida:** il controllo dei workflow attivi viene messo in
  cache, e i worker in background si riavviano in modo pulito invece di
  lasciare processi in stallo.

## Barcode Service — live: `1.17.4`

- **Suddivisioni di lunga durata:** la connessione alla coda dei task resta
  attiva durante i job barcode prolungati, quindi la suddivisione di batch
  di grandi dimensioni non si blocca più verso la fine.

## FTP Service — live: `1.31.2`

- **Pulizia del log di importazione:** stessa conservazione di 90 giorni e
  stessa pulizia automatica dell'Email Service.

---

## Invariati in questa release

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **Operator** (`1.40.2`) e **Ideas** (`0.3.1`) non presentano
modifiche in questa finestra.

<!-- Generated by the docbits-changelog skill (version-boundary mode), then
     reconciled on 23 Jul 2026 against the Nova versions actually deployed
     (Web App 10.45.1, API 12.64.3, Auth 1.72.8, Email 1.39.9, PO Match
     1.59.1, OCR 1.9.9, Docflow 2.7.2, FTP 1.31.2). Manage Layouts and
     Custom Validation Rules were removed from this page: DOCB-13719 gated
     both behind a beta query parameter, so they are not generally available
     in 10.45.1. -->
