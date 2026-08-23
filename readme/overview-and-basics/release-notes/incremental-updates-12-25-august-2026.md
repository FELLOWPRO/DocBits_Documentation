# Note della versione DocBits — 12–25 agosto 2026

_Cosa cambia con l'aggiornamento di produzione di DocBits del 25 agosto 2026,
che copre tutto quanto rilasciato dopo la release del 12 agosto. Per ogni
servizio è indicata la versione in distribuzione, seguita dalle novità e
correzioni spiegate in linguaggio semplice. I servizi non elencati non hanno
avuto modifiche visibili ai clienti._

---

## Highlights

- **Isolamento più rigoroso delle organizzazioni.** Una verifica di sicurezza
  ha chiuso diversi punti in cui i dati di un'organizzazione potevano essere
  letti o scritti da un'altra: gli script dei documenti, gli elenchi utenti
  delle sotto-organizzazioni, le appartenenze ai gruppi e il token di
  elaborazione che un documento porta con sé lungo la pipeline vengono ora
  tutti verificati rispetto all'organizzazione del chiamante. Le approvazioni
  applicano inoltre correttamente il principio dei quattro occhi: il secondo
  approvatore deve essere una persona diversa dalla prima.
- **I documenti non restano più bloccati.** Corrette quattro cause distinte di
  documenti fermi per sempre: esportazioni rimaste in "Exporting" dopo un
  rifiuto, riavvii congelati al crash di un passaggio di elaborazione,
  suddivisioni per codice a barre che non davano mai riscontro e la schermata
  di contabilità ferma su "Preparing…". In ogni caso il documento ora si
  conclude oppure mostra un errore reale su cui potete agire.
- **Le note di credito vengono riconosciute come note di credito.** Le note di
  credito XRechnung 3.0, 3.0.1 e 3.0.2 in sintassi CII, le note di credito CII
  pure e i documenti ZUGFeRD 2.4 / Factur-X 1.08 vengono ora tutti classificati
  correttamente, con il totale letto dal campo giusto. Per i documenti
  scansionati che menzionano sia "fattura" sia "nota di credito" decide la
  parola chiave più vicina al tipo di documento, e gli importi tornano positivi
  quando riclassificate una nota di credito in fattura.
- **Il PO matching fa calcoli di cui potete fidarvi.** Le tolleranze vengono
  confrontate come decimali esatti invece che come valori in virgola mobile,
  sono basate sul valore dell'ordine d'acquisto, e le fatture che fanno
  riferimento a più ordini d'acquisto vengono confrontate con tutti. Le
  colonne mai mappate non falsano più il controllo dell'importo di riga e,
  quando mancano colonne obbligatorie, l'errore le nomina.
- **Le esecuzioni dei workflow conservano il proprio lavoro.** Un workflow che
  scrive il valore di un campo lo scrive ora sul documento in modo che
  un'esportazione successiva non possa annullarlo in silenzio. I trigger
  ritentati non scartano più quanto l'esecuzione aveva già fatto, e due
  trigger sullo stesso documento si mettono in coda invece di rubarsi il lock
  a vicenda.
- **Le e-mail di reimpostazione della password partono di nuovo.** Non
  lasciavano mai il server, senza alcun segnale. Il modulo di reimpostazione
  mostra inoltre un riscontro reale dopo l'invio, e la risposta non rivela più
  se un account esiste.

---

## Web App — `10.55.0`

### Accesso e account

- La reimpostazione della password funziona di nuovo da cima a fondo: la mail
  arriva, il modulo conferma l'invio e la risposta è la stessa sia che
  l'indirizzo abbia un account sia che non lo abbia.
- La disconnessione in una scheda del browser disconnette anche le altre
  schede, senza i toast di errore che comparivano quando le schede erano in
  disaccordo sulla sessione.
- Se la vostra organizzazione richiede la registrazione al secondo fattore, la
  schermata di login ora lo dice invece di fallire senza messaggio. L'accesso
  con passkey tra regioni mostra messaggi di errore tradotti, e il suo
  pulsante di invio è visibile.
- Gli amministratori non possono più attivare l'obbligo di MFA per l'intera
  organizzazione prima che la registrazione al login sia disponibile, cosa che
  in precedenza poteva escludere le persone dall'accesso.

### Schermata di validazione

- Il cursore dello zoom arriva ora al 150% (prima si fermava all'80%), e lo
  zoom in una tabella supera la larghezza del contenitore invece di non fare
  nulla.
- I campi importo vuoti contano come 0 invece di far scattare un toast di
  errore, e un doppio clic sull'immagine del documento viene ignorato quando
  nessun campo è selezionato.
- Il banner mostrato quando un'altra sessione detiene il lock del documento
  non aveva testo; ora si spiega. Taggare una tabella non fa più scattare un
  falso avviso "documento modificato esternamente" per la vostra stessa
  modifica.
- Nella tabella AI, un rimappamento di colonna che toglierebbe la mappatura a
  un'altra colonna chiede prima conferma, e i valori che non sono numeri
  vengono segnalati nelle colonne AMOUNT e NUMBER.
- La scheda "Extracted table" torna a rimandare all'addestramento manuale
  delle tabelle quando è vuota, e non gira più all'infinito quando esiste già
  una tabella AI.
- I numeri articolo nella tabella delle righe di Compare vengono mostrati come
  identificativi, non arrotondati come importi.
- I campi approvatore risolvono gli id di utenti e gruppi in nomi, così non
  mostrano mai un id grezzo né restano vuoti. Le scadenze delle attività
  vengono convertite attraverso un unico percorso consapevole dell'UTC, così
  ogni persona vede la stessa data.
- I documenti rimandati in validazione mostrano uno spinner di caricamento
  invece di una schermata morta mentre vengono preparati.
- L'apertura di fatture fornitore di grandi dimensioni è sensibilmente più
  veloce.

### Contabilità

- Le righe suddivise mantengono il segno % dopo la pressione di Invio, e lo
  0 % è accettato come valore.
- Nel filtro dei conti, Invio conferma il primo conto corrispondente invece di
  non fare nulla.
- I caratteri delle flexdimension vengono mappati per id di dimensione, così
  le dimensioni finiscono nella colonna giusta anche quando l'ordine
  differisce.
- Una preparazione contabile fallita si riprende con un messaggio di errore
  invece di restare per sempre su "Preparing…", e la riapertura di un
  documento non serve più dati obsoleti del documento precedente.

### PO matching

- Aprire il PO Matching senza tutte le colonne obbligatorie mappate è di nuovo
  possibile; quando manca qualcosa di necessario, il messaggio nomina le
  colonne esatte.
- Le colonne non mappate a nulla vengono nascoste all'apertura della
  schermata, dopo avervelo chiesto una volta, e non confluiscono più nel
  calcolo dell'importo di riga.
- La quantità abbinata si aggiorna dopo il salvataggio, e il popup delle
  colonne mancanti vi porta alla Validazione dei campi, dove potete
  correggerle.

### Dashboard e ricerca

- Le colonne basate su menu a tendina (tipo di fattura, stato e simili)
  mostrano l'etichetta nella lingua della vostra interfaccia invece del valore
  memorizzato grezzo.
- La ricerca a testo libero accetta le parentesi come testo semplice; prima
  rifiutava la query. L'operatore di filtro "diverso da" resta selezionato, e
  la modifica manuale di un filtro non corrompe più il nome del campo.
- La selezione di una sotto-organizzazione nella ricerca rapida inserisce il
  suo nome, non il suo uuid, e l'autocompletamento delle sotto-organizzazioni
  non elenca più duplicati.
- La dashboard può ora recuperare fino a 10.000 documenti per finestra di
  ricerca, così gli insiemi di risultati ampi vengono paginati correttamente.
- Il pannello dei documenti duplicati mostra le stesse colonne risolte
  dell'elenco principale, e i valori di filtro fornitore composti da più
  parole sopravvivono alla pressione di Invio.
- Il contatore delle attività aperte nella barra laterale conta le attività
  nel contesto della vostra sotto-organizzazione, non nel contesto del
  documento che si trova aperto in quel momento.

### Attività

- Le colonne Kanban si paginano durante lo scorrimento, così le bacheche con
  molte attività si caricano rapidamente.
- L'e-mail di assegnazione parte quando un'attività viene assegnata, una sola
  volta. Modificare un'attività o contrassegnarla come completata non la
  rinvia più, e la data di assegnazione resta la data dell'assegnazione
  effettiva. Le e-mail delle attività vengono inoltre visualizzate
  correttamente in Outlook.

### Workflow Builder

- L'elenco dei workflow conserva ricerca, ordinamento, pagina e dimensione
  della pagina quando aprite un workflow e tornate indietro, anche tramite il
  breadcrumb. La pagina si apre per impostazione predefinita sulla scheda
  List.
- L'interruttore "run workflow on change" nel layout builder ora condiziona
  davvero l'esecuzione, e attivarlo richiede la scelta di un workflow.

### Impostazioni e amministrazione

- Il link di download di WatchDog e il comando di configurazione puntano
  all'ambiente in cui vi trovate, non sempre a produzione.
- Alberi decisionali: il campo documento selezionato resta evidenziato quando
  il selettore si riapre, le etichette troncate ricevono un tooltip, e quando
  si aggiunge una riga vengono mostrati i nomi degli utenti (non gli id
  grezzi).
- La casella System Admin è modificabile quando si modifica un utente.
- La pagina dei dati anagrafici non compare più vuota per una race condition
  nell'ordinamento, e l'ordinamento per badge non manda più in crash la
  pagina.
- Un abbonamento in stato "cancelling" può essere ripreso.
- La pagina di dettaglio XSLT segnala gli errori di caricamento invece di non
  mostrare nulla, e le impostazioni delle notifiche e-mail usano l'intera
  larghezza della pagina con un pannello dei log funzionante.
- Il selettore dell'organizzazione per gli utenti multi-organizzazione ha
  layout delle righe, dimensioni e colori del tema corretti.
- Analytics: i Core Web Vitals vengono visualizzati a partire dai dati di
  misurazione reali, la vista del servizio log funziona, e una richiesta di
  metriche fallita mostra uno stato di errore invece di visualizzare zeri.
- "Use Default Template" nel gestore dei layout copia il layout predefinito
  come previsto; prima andava in crash o sosteneva che non esistesse alcun
  layout predefinito.
- Le etichette dei campi personalizzati non sovrascrivono più le traduzioni
  integrate dei campi standard, e le schermate DocNet (AI Workforce), incluso
  l'Agent Wizard, sono tradotte.
- Offerte del portale fornitori: l'invio di un'offerta con un valore REF1
  fuori dall'elenco consentito viene bloccato, le unità di misura gestite
  compaiono nella tabella delle righe, e lo stile delle approvazioni si
  applica solo alle offerte contrattuali.
- MediOrder ottiene il rilevamento dei documenti duplicati nella propria
  schermata di validazione.

## API Service — `12.82.3`

### Sicurezza e isolamento delle organizzazioni

- Il cambio dell'organizzazione attiva viene validato rispetto alla vostra
  effettiva appartenenza e in caso di dubbio nega l'accesso, ed è stato chiuso
  un endpoint di test interno che poteva essere abusato per attraversare le
  organizzazioni.
- Gli script dei documenti non possono più essere letti o sovrascritti tra
  organizzazioni, né tramite la chiamata di applicazione al documento né
  tramite un id di versione estraneo al salvataggio.
- Gli elenchi utenti delle sotto-organizzazioni e gli elenchi dei membri dei
  gruppi restituiscono solo persone dell'organizzazione del chiamante, e
  l'aggiunta di più utenti a un gruppo in una volta sola non scarta più tutti
  tranne il primo.
- Una credenziale dell'organizzazione sbagliata viene rifiutata prima che
  possa diventare il token di elaborazione di un documento, e le query di
  ricerca full-text vengono eseguite come l'utente chiamante e non come
  un'identità di servizio.
- L'approvazione a quattro occhi è applicata: il secondo approvatore deve
  essere diverso dalla persona che ha approvato per prima.
- L'elenco live del PO Dashboard è limitato alle sotto-organizzazioni
  dell'utente.

### Pipeline dei documenti

- I documenti la cui esportazione è stata negata non restano più in
  "Exporting" per sempre, e gli errori di esportazione portano sempre un
  messaggio invece di uno vuoto.
- Quando un passaggio di elaborazione va in crash, il documento passa a uno
  stato di errore invece di restare bloccato in "restart in progress" senza
  via d'uscita.
- Una suddivisione per codice a barre che fallisce o va in timeout
  contrassegna il documento come Error invece di mostrare silenziosamente
  "Running", e una suddivisione che non produce figli conserva il documento
  padre e lo segnala invece di eliminare tutto.
- Un nuovo tentativo fallito non può più sovrascrivere un documento che nel
  frattempo ha completato l'elaborazione.
- I documenti riavviati senza interazione dell'utente e i figli delle
  suddivisioni vengono ora eseguiti con un token di organizzazione durevole,
  così le elaborazioni lunghe non muoiono con una sessione scaduta.
- Una risposta vuota dei layout template non resta più in cache per sei ore,
  cosa che faceva sparire i layout fino alla scadenza della cache.

### Estrazione ed e-document

- Gli importi scritti con il segno meno finale ("100,00-") vengono
  interpretati come negativi invece di essere scartati.
- I documenti svizzeri vengono riconosciuti come svizzeri (CHF, partite IVA
  CHE, IBAN CH) invece di ricadere sulle convenzioni tedesche, e le date
  scritte con trattini tipografici vengono interpretate correttamente.
- Le note di credito XRechnung 3.0, 3.0.1 e 3.0.2 in sintassi CII vengono
  classificate come note di credito con il totale letto dal campo del totale
  complessivo; lo stesso vale per le note di credito CII pure. Una versione
  ZUGFeRD 2.4 / Factur-X 1.08 dichiarata prevale sull'identificatore di
  profilo generico, e i tipi XRechnung semplici si risolvono nel loro gemello
  UBL o CII invece di fallire.
- I campi a menu a tendina (list-of-values) come Tax Country e Tax Code
  mantengono il valore attraverso la trasformazione dei campi; venivano
  svuotati.
- Estrazione tabelle: un errore in una colonna di soli numeri resta confinato
  a quella colonna invece di far saltare l'intera tabella, l'estrazione
  tabelle AI riceve un timeout che sopravvive alle esecuzioni multi-batch, e
  sono stati corretti due crash su forme di tabella insolite (righe senza
  posizione di pagina, numeri di colonne irregolari).
- I pattern delle regole di provenienza vengono confrontati senza distinguere
  tra maiuscole e minuscole.

### Esportazione

- Un controllo delle imposte che fallisce durante l'anteprima di esportazione
  restituisce un errore leggibile invece di un errore del server, su entrambi
  gli endpoint di anteprima.
- L'esportazione SFTP può inviare il documento originale insieme a quello
  convertito.
- Quando esistono configurazioni di esportazione su più livelli, prevale in
  modo coerente la più specifica.
- Le esportazioni BOD possono trasportare attributi di tipo colonna tramite
  la mappatura.

### Importazione e dati anagrafici

- Il log di importazione delle e-mail è completo: le e-mail in ingresso
  rifiutate o fallite hanno sempre una riga di log con un motivo accurato.
  Niente più scarti silenziosi.
- Le importazioni BOD degli ordini d'acquisto mantengono le sotto-righe
  collegate alla riga giusta; un flag trascinato da una riga all'altra le
  collegava a quella sbagliata.
- L'importazione di un CSV con più fornitori nuovi funziona (gli id generati
  non collidono più), gli alias dei termini di sconto cassa si importano e
  rispettano l'impostazione "on conflict", e la scelta IGNORE in caso di
  conflitto vale anche oltre i fornitori.
- Il suggerimento fornitore (TF-IDF) conserva il proprio id fornitore quando
  una preferenza viene aggiornata, così i suggerimenti smettono di puntare al
  nulla.

### Altre correzioni

- Le righe della dashboard risolvono le etichette dei menu a tendina nella
  lingua dell'utente, senza bloccare la richiesta.
- Dopo la modifica dei campi, lo stato del PO match si aggiorna invece di
  mostrare lo stato precedente alla modifica.
- I documenti Purchase Order Change ricevono cinque campi in parità con
  Purchase Order e un layout predefinito di validazione dei campi.
- Le risposte di errore su 152 endpoint restituiscono messaggi leggibili
  invece di oggetti eccezione grezzi, e la pagina di analytics dei log non
  risponde più con 502 per le organizzazioni senza un indice di log.

## Auth Service — `1.77.9`

- Le e-mail di reimpostazione della password non partivano mai, senza alcun
  segnale; corretto, insieme al problema di thread-safety sottostante.
- Un refresh token riutilizzato viene rifiutato: il controllo autoritativo sul
  database viene ora eseguito ogni volta invece di essere saltato in caso di
  cache hit.
- Autenticazione a due fattori: un'app di autenticazione può essere registrata
  accanto ai codici via e-mail, e la rimozione dell'ultima passkey o la
  rigenerazione dei codici di backup richiedono prima un secondo fattore
  recente.
- Un id di sotto-organizzazione valido non viene più rifiutato con
  "Organization not found", e una API key creata in una sotto-organizzazione
  risolve il proprio utente tecnico da quella sotto-organizzazione.
- La modifica di un'organizzazione valida il partner id e non reimposta più il
  tipo di organizzazione come effetto collaterale.
- I "token rimanenti" nella vista dell'abbonamento sono ancorati all'anno
  contrattuale, non all'anno solare.

## Auth Bridge Service — `0.5.7`

- La replica degli account tra le regioni UE e USA si riprende da sola. Un
  flusso di replica interrotto si riaggancia sul posto, la replica continua a
  scorrere mentre è in corso una riconciliazione, e la memoria della
  riconciliazione è limitata, così il servizio smette di andare in crash-loop
  sulle tabelle grandi.

## Barcode Service — `1.18.7`

- La lettura dei codici a barre viene eseguita con un limite di tempo e
  segnala un timeout invece di bloccarsi, cosa che prima lasciava il documento
  fermo in elaborazione.

## Docflow Service — `2.9.8`

- I valori dei campi scritti da una card di workflow arrivano sul documento in
  entrambe le rappresentazioni memorizzate, così un'esportazione successiva
  non li annulla più.
- Un trigger ritentato conserva il lavoro già svolto dall'esecuzione, i
  trigger in conflitto sullo stesso documento si mettono in coda invece di
  rubarsi il lock, e un nuovo tentativo in escalation viene collocato in cima
  alla coda.
- Card di confronto degli ordini d'acquisto: le tolleranze si confrontano come
  decimali esatti e si basano sul valore dell'ordine d'acquisto, le direzioni
  di confronto invertite sono disponibili come opzioni, un assegnatario di
  gruppo viene riportato come gruppo invece di far fallire un confronto su id
  utente, gli id di assegnazione si confrontano correttamente come UUID, le
  righe con valori numerici vuoti vengono saltate, e un confronto "received"
  senza alcun dato di ricezione segnala i dati mancanti invece di fingere una
  corrispondenza.
- La card Apply Decision Table è stata ritirata.

## Email Service — `1.41.0`

- Le importazioni Gmail prelevano ogni allegato esattamente una volta; i
  duplicati dovuti a recuperi sovrapposti sono spariti.
- Il cursore di lettura dell'importazione avanza solo dopo che un'importazione
  è confermata, così un crash a metà importazione non può più saltare e-mail.
- Quando una configurazione di importazione viene disattivata perché ne esiste
  una simile, la disattivazione è visibile e notificata invece che silenziosa.

## Extraction Service — `1.54.5`

- Se un documento è una nota di credito o una fattura viene deciso in base
  alla parola chiave più vicina alla menzione del tipo di documento, invece
  che alla prima corrispondenza trovata.
- Quando più interpretazioni delle imposte rientrano nella tolleranza, la
  riconciliazione esatta viene preferita a una quasi corrispondenza.
- Dopo un re-OCR forzato vengono ripristinati il tipo di documento e il
  locale, così l'estrazione tabelle e l'addestramento funzionano di nuovo sui
  documenti sottoposti a nuovo OCR.
- I documenti senza tipo di documento non mandano più in crash la ricerca
  delle regole di tabella.

## FTP Service — `1.32.8`

- La scansione delle cartelle esegue un solo round trip di elenco per cartella
  con una profondità limitata, così le importazioni da directory FTP grandi
  sono molto più veloci e smettono di andare in timeout.

## Fulltext Service — `1.42.3`

- I documenti il cui payload di ricerca memorizzato non aveva campi estratti
  vengono reindicizzati dal database, così ricompaiono nella ricerca della
  dashboard.
- La finestra di ricerca della dashboard supporta fino a 10.000 documenti.
- Le ricerche per faccette non falliscono più quando la ricerca semantica è
  attiva.

## OCR Service — `1.10.7`

- Il budget di tempo dell'OCR viene dimensionato sul costo reale per pagina,
  così i documenti lunghi arrivano in fondo invece di urtare il limite della
  pipeline.

## PO Match Service — `1.59.8`

- Le righe di tabella con quantità zero vengono saltate nei controlli di
  mancata corrispondenza invece di produrre falsi mismatch.
- Quando mancano colonne obbligatorie del PO match, il risultato le nomina.
