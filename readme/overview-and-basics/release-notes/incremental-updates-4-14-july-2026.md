# Note della versione DocBits — 4–14 luglio 2026

_Una panoramica di ciò che cambia per voi con questa release di DocBits. Ogni
servizio qui sotto mostra la versione ora in fase di rilascio, seguita dalle
novità o correzioni spiegate in linguaggio semplice — senza numeri di ticket né
gergo tecnico. I servizi non elencati non hanno avuto modifiche visibili ai
clienti in questo periodo._

---

## Highlights

- **Login multi-organizzazione.** Gli utenti che appartengono a più
  organizzazioni ora dispongono di un vero selettore di organizzazione al
  login, di un commutatore di organizzazione nell'intestazione e di
  un'impostazione per l'organizzazione predefinita. Le sessioni sono legate in
  modo sicuro a una sola organizzazione alla volta e l'app segue
  automaticamente la regione dell'organizzazione attiva. Il login sulla
  regione sbagliata ora riprova automaticamente quella corretta invece di
  fallire.
- **Canali di rilascio (frozen / latest).** Le organizzazioni possono ora
  essere ancorate a una release stabile ("frozen") mentre altre ricevono gli
  aggiornamenti più recenti — consentendo rollout controllati. La finestra
  Versioni dei servizi mostra una nuova colonna *Release* e gli amministratori
  gestiscono il canale dalle Informazioni azienda. In questo periodo diversi
  servizi mostrano salti di versione più ampi dovuti esclusivamente alla nuova
  numerazione delle versioni per canale — tali salti non comportano alcuna
  modifica funzionale.
- **Motori di regole configurabili.** Tre nuovi sistemi di regole arrivano
  nell'API (ognuno disattivato per impostazione predefinita, attivabile per
  organizzazione): **regole di validazione** che controllano i valori
  estratti e segnalano i problemi direttamente sul documento, **regole di
  trasformazione** che ripuliscono o riscrivono automaticamente i valori
  estratti di campi e tabelle, e **selezione del layout basata su regole**
  che sceglie il layout di documento corretto tramite regole invece che in
  base alla provenienza del documento.
- **Trasparenza dell'importazione e-mail.** Il log di importazione e-mail ora
  mostra una riga espandibile per ogni allegato, indica quali documenti sono
  stati creati (con pulsanti che portano direttamente ad essi nella
  dashboard), segnala gli elementi saltati e suddivisi e consente di scaricare
  l'e-mail originale come file `.eml`.
- **Estrazione tabelle con AI.** Una nuova modalità di estrazione AI
  strutturata per le tabelle, con una casella "Use AI" per tabella e per
  colonna nelle impostazioni del Tipo di documento.
- **Stabilità della Web App.** Corretto un loop di ricaricamento infinito dopo
  una sessione scaduta, corretto il Layout Builder che non funzionava, e le
  tabelle di estrazione dispongono ora di un cursore trascinabile per
  regolarne l'altezza.
- **Novità: Auth Bridge Service.** Un nuovo servizio mantiene i dati di login
  continuamente sincronizzati tra le regioni UE e USA, con auto-riparazione e
  monitoraggio integrati.

---

## API Service — live: `12.57.8`

- **Regole di validazione (novità, per organizzazione):** un motore di regole
  configurabile dagli amministratori controlla i valori estratti (totali,
  campi obbligatori e altro) e contrassegna i problemi direttamente sul
  documento, indicando quale regola è scattata. Le regole possono essere
  testate in modalità di prova prima dell'attivazione, possono essere
  attivate per tipo di documento e includono un catalogo iniziale di regole
  predefinite (tutte disattivate finché non decidete di attivarle).
- **Regole di trasformazione (novità, per organizzazione):** ripuliscono o
  riscrivono automaticamente i valori estratti di campi e tabelle durante
  l'elaborazione — configurabili per tipo di documento o per l'intera
  organizzazione.
- **Selezione del layout basata su regole (novità):** i layout dei documenti
  possono ora essere scelti tramite regole configurabili invece di essere
  legati alla provenienza del documento. Il comportamento esistente basato
  sulla provenienza viene migrato automaticamente, i modelli di layout possono
  essere rinominati e i titoli di layout duplicati vengono impediti.
- **Esportazioni dalla dashboard più veloci:** le esportazioni avviate dalla
  dashboard vengono ora inviate a un worker dedicato invece di attendere un
  ciclo di polling, quindi partono subito.
- **Corretto il blocco di esportazione del rilevamento duplicati:** il blocco
  di esportazione per i sospetti duplicati funziona di nuovo.
- **Impostazioni che non venivano salvate:** corretto il caso in cui le
  preferenze salvate occasionalmente non persistevano quando esisteva una
  copia precedente eliminata della stessa impostazione.
- **Documenti con caratteri insoliti:** corretti gli errori di salvataggio
  causati da caratteri NUL invisibili nei dati estratti.
- **"Aggiornato da" corretto:** i documenti caricati automaticamente come
  documenti elettronici non mostrano più un utente di sistema come ultimo
  editor — il campo resta vuoto finché una persona non li modifica realmente.
- **PDF scansionati con un buon livello di testo:** una nuova opzione consente
  a DocBits di fidarsi del testo già incorporato in una pagina scansionata
  invece di rieseguire l'OCR — più veloce e spesso più accurato.
- **Fatture elettroniche:** rilevamento più robusto dell'XML incorporato
  quando il file originale deve essere ricontrollato.
- **Attività:** nuovo interruttore a livello di organizzazione che consente
  agli utenti non amministratori di usare il filtro "Tutti" nell'elenco delle
  attività.
- **Abbinamento delle righe:** il comportamento di fuzzy matching è ora
  configurabile per riga.
- **Stabilità:** le connessioni WebSocket si chiudono in modo pulito in caso
  di errore invece di generare eccezioni sul server; la sincronizzazione della
  cache dei permessi si verifica e si ripara da sola; la versione del servizio
  è ora visibile sull'endpoint di health.

## Auth Service — live: `1.71.1`

- **Login multi-organizzazione:** il login ora chiede in quale organizzazione
  entrare quando un utente appartiene a più organizzazioni, le sessioni sono
  legate a quell'organizzazione e nuovi endpoint supportano la selezione, il
  cambio e l'impostazione di un'organizzazione predefinita. Le appartenenze a
  organizzazioni duplicate o in conflitto sono state ripulite e sono ora
  impedite a livello di database, con ricerche di appartenenza più veloci.
- **Correzioni all'organizzazione predefinita:** il login seleziona
  automaticamente la vostra organizzazione predefinita (non una arbitraria) e
  la modifica della predefinita ha effetto immediato invece di mostrare dati
  di profilo obsoleti.
- **Logout corretto:** risolto un errore del server (HTTP 500) al logout e
  ripristinato l'endpoint di revoca dei token.
- **Sicurezza dei token:** la verifica e la memorizzazione nella cache dei
  token ora rispettano l'organizzazione per cui un token è stato emesso, e la
  revoca dei token è centralizzata.
- **Canali di rilascio:** il canale di rilascio dell'organizzazione viene
  memorizzato qui, è gestibile dagli amministratori dell'organizzazione ed è
  esposto all'app e al livello di routing.

## Auth Bridge Service — live: `0.2.4.2` _(nuovo servizio)_

- **Che cos'è:** un nuovo servizio che replica continuamente i dati di
  autenticazione tra le regioni UE e USA, in modo che account e login restino
  coerenti tra le regioni.
- **Auto-riparazione:** rileva e ripara le divergenze di dati tra le regioni —
  garantendo anche la propagazione delle eliminazioni — e si riprende
  automaticamente dalla perdita di connessione invece di perdere dati.
- **Sicurezza e monitoraggio:** un precedente loop di replica bidirezionale è
  stato fermato e viene ora rilevato e bloccato attivamente; il tracciamento
  degli errori e gli avvisi sono integrati; e il servizio riporta la propria
  versione nella finestra Versioni dei servizi.

## Docflow Service — live: `2.6.1`

- **Le schede workflow accettano valori vuoti:** le schede checkbox e partner
  non falliscono più quando un campo è legittimamente vuoto; i controlli sul
  tipo di scheda sono più rigorosi e prevedibili.
- **I workflow vengono rieseguiti su modifiche reali:** il lock dei workflow
  rispetta di nuovo lo stato del documento proveniente dal trigger e ora
  traccia anche la versione del documento — così un documento i cui dati sono
  realmente cambiati può ripassare per il workflow anche con lo stesso stato,
  mentre i veri duplicati restano bloccati.
- **Workflow avanzati più grandi:** il limite sui nodi dei workflow è stato
  aumentato ed è ora configurabile per ambiente.
- **Esportazione alternativa:** le esportazioni alternative avviate da
  workflow sono ora etichettate come tali, così i sistemi a valle possono
  distinguerle.
- **Resilienza:** il servizio si riconnette automaticamente quando una
  connessione al database viene interrotta durante l'uso, tollera un message
  broker più lento invece di fallire, e le richieste API fallite vengono ora
  registrate con contesto completo e ID di esecuzione tracciabili.

## Email Service — live: `1.38.4`

- **Log di importazione, ricostruito per la tracciabilità:** ogni e-mail
  importata ora registra quali documenti sono stati creati da essa, con righe
  di dettaglio per allegato.
- **Download dell'e-mail originale:** il messaggio originale può essere
  scaricato come file `.eml` direttamente dal log di importazione.
- **Recupero degli allegati:** il percorso di recupero dalla corruzione ora
  gestisce anche i messaggi in testo semplice, così più e-mail in entrata
  danneggiate vengono recuperate invece di essere saltate.

## Extraction Service — live: `1.51.6`

- **Imposta/netto non più invertiti:** corretto un caso sui documenti USA in
  cui l'importo dell'imposta poteva essere assegnato come maggiore
  dell'importo netto quando venivano trovate più coppie candidate.
- **Più aliquote fiscali per fornitore:** l'estrazione ora gestisce i
  fornitori le cui fatture riportano aliquote fiscali diverse su un unico
  documento.
- **Estrazione tabelle con AI (novità, opt-in):** endpoint di estrazione AI
  strutturata per le tabelle, attivati per organizzazione tramite feature
  flag.
- **Chiamate AI più veloci:** ottimizzata la configurazione del modello AI
  usata durante l'estrazione per evitare tempi di elaborazione inutili.
- **Correzione di un crash:** risolto un errore su documenti che producevano
  un elenco di candidati vuoto durante l'estrazione.

## Fulltext Service — live: `1.37.2`

- **Riparate le migrazioni dell'indice di ricerca:** ripristinate definizioni
  di migrazione che si erano disallineate, mantenendo affidabili gli
  aggiornamenti dell'indice di ricerca.
- Lavoro interno di routing per la nuova infrastruttura dei canali di
  rilascio.

## PO Match Service — live: `1.58.2`

- **Abbinamento più tollerante:** il PO matching non fallisce più su dati
  insoliti — numeri articolo non testuali, quantità mancanti e importi non
  testuali vengono ora gestiti correttamente invece di generare errori.

## Web App — live: `10.41.8`

- **Esperienza multi-organizzazione:** nuova pagina di selezione
  dell'organizzazione al login, un'icona dedicata per cambiare organizzazione
  nell'intestazione, impostazioni per l'organizzazione predefinita, e l'app
  segue la regione della vostra organizzazione attiva. Il login sulla regione
  sbagliata riprova silenziosamente la regione corretta e vi indirizza al
  selettore di organizzazione quando necessario.
- **Basta ricaricamenti infiniti:** corretto un loop di ricaricamento infinito
  che poteva verificarsi quando il server rifiutava un token di sessione
  memorizzato — l'app ora forza un vero rinnovo del token invece di
  ricaricare all'infinito.
- **Layout Builder corretto:** il Layout Builder funziona di nuovo, e la
  selezione del layout è disaccoppiata dalla provenienza del documento
  (in linea con la nuova selezione basata su regole nell'API).
- **Tabelle di estrazione:** le tabelle delle righe dispongono ora di una
  maniglia di ridimensionamento trascinabile, così potete dare più spazio
  alla tabella durante la validazione.
- **Log di importazione e-mail:** nuovi badge per gli stati "saltato" e
  "suddiviso", righe espandibili per allegato, download dell'e-mail originale
  e pulsanti con l'ID del documento che portano direttamente alla dashboard
  filtrata su quel documento.
- **Ricerca nella dashboard:** il menu a tendina dei valori di ricerca ora
  mostra l'etichetta localizzata per i campi a elenco di valori, e gli esempi
  della guida alla ricerca sono stati rielaborati.
- **Affidabilità delle impostazioni:** le preferenze utente ora si caricano
  in modo affidabile quando si accede via SSO, e la conferma di salvataggio
  viene mostrata solo quando il salvataggio è effettivamente riuscito.
- **Attività:** il filtro "Tutti" può essere ripristinato per gli utenti non
  amministratori tramite un nuovo interruttore a livello di organizzazione.
- **Log del watchdog:** non più limitati a 10.000 voci, oltre a miglioramenti
  generali di usabilità.
- **Ticket di supporto:** il modulo di supporto precompila il vostro indirizzo
  e-mail dal profilo.
- **Impostazioni del Tipo di documento:** nuova casella "Use AI" su tabelle e
  colonne per controllare l'estrazione delle tabelle assistita dall'AI.
- **Finestra Versioni dei servizi:** nuova colonna *Release* che mostra il
  canale di ogni servizio (frozen/latest), instradata in modo da restare
  veloce per le organizzazioni ancorate.
- **Validazione dei campi:** corretto un errore nel tornare alla Validazione
  dei campi da un'altra schermata, e il pulsante "Scripts" non indirizza più
  a una pagina 404.

---

## Solo rinumerazione delle versioni (nessuna modifica funzionale)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) e **Ideas Service** (`0.3.1`) sono stati rinumerati nell'ambito
della nuova infrastruttura dei canali di rilascio. I loro salti di versione
apparentemente più ampi non comportano alcuna modifica di funzionalità o
comportamento in questo periodo. **Docnet Service** (`1.54.6`) è invariato dal
19 giugno.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..14)
     version-bump commits supplied by the user, per service). -->
