# Note della versione DocBits — 14–23 luglio 2026

_Cosa cambia con l'aggiornamento di produzione di DocBits del 23 luglio 2026
(l'aggiornamento del canale Nova), che copre tutto quanto rilasciato dopo la
release del 14 luglio. Per ogni servizio è indicata la versione ora in
produzione, seguita dalle novità e correzioni spiegate in linguaggio semplice.
I servizi non elencati non hanno avuto modifiche visibili ai clienti._

---

## Highlights

- **Manage Layouts e le regole di validazione arrivano nell'app.** I motori di
  regole introdotti lato server nella release precedente hanno ora
  un'interfaccia utente completa. Potete gestire direttamente i layout dei
  documenti, definire le vostre regole di validazione e lasciare che siano le
  regole a scegliere il layout giusto invece della provenienza del documento.
  Entrambe le funzioni restano disattivate finché non abilitate **Custom
  Validation Rules** sul tipo di documento, quindi nulla cambia finché non
  decidete di attivarle.
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
- **Le modifiche agli script sono protette da password.** Gli script
  personalizzati possono cambiare il modo in cui i documenti vengono
  elaborati, quindi ogni modifica a uno script richiede ora una password che
  ruota ogni ora. Chiedete quella corrente al vostro amministratore.
- **Ritirato il livello AI Turbo.** Il modello Turbo ha raggiunto il fine
  vita. Chi lo aveva selezionato è stato spostato automaticamente su Fast;
  non è richiesta alcuna azione.

---

## Web App — live: `10.44.4`

- **Manage Layouts:** la gestione dei layout è ora configurabile nell'app.
  I layout possono essere selezionati tramite regole definite da voi invece
  di essere legati alla provenienza del documento. La trovate in
  Impostazioni → Tipi di documento → Manage Layouts.

<figure><img src="../../.gitbook/assets/manage-layouts-selection-rules-en.png" alt="Schermata Layouts &#x26; Selection Rules con le schede dei layout e il nuovo interruttore Selection rules"><figcaption><p>Layouts &#x26; Selection Rules: layout riutilizzabili con selezione basata su regole</p></figcaption></figure>

- **Regole di validazione:** definite i vostri controlli sui valori estratti
  e vedete gli errori segnalati sul documento, con l'indicazione di quale
  regola è scattata. Con la release arriva un catalogo di regole predefinite
  di sistema; ogni regola resta disattivata finché non la attivate. La
  funzione si abilita per tipo di documento sotto Custom Validation Rules.

<figure><img src="../../.gitbook/assets/custom-validation-rules-en.png" alt="Schermata Custom Validation Rules con l'elenco delle regole predefinite di sistema, gravità e interruttori di stato"><figcaption><p>Custom Validation Rules: regole predefinite di sistema, attivate per tipo di documento</p></figcaption></figure>
- **Ticket di supporto dagli errori:** create un ticket direttamente da un
  record di errore. I ticket includono ambiente e canale di rilascio, e la
  cattura dello screenshot non si blocca più.
- **Esportazione dashboard:** le esportazioni usano ora la dashboard
  effettivamente selezionata, e l'app vi avvisa quando esportate una
  dashboard con modifiche non salvate.
- **Approvazioni:** gli utenti non possono più approvare un passaggio Sales
  Tax per cui il loro gruppo non ha i permessi. La cronologia delle
  approvazioni mostra di nuovo tutte le voci.
- **Documenti eliminati:** aprire un documento eliminato nel frattempo mostra
  un messaggio chiaro invece di errori di script.
- **Account eliminati:** l'accesso con un account eliminato ora lo segnala
  esplicitamente, invece di fallire con un errore generico.
- **Login SSO:** corretto un errore all'accesso quando era selezionata una
  regione diversa.
- **Log di importazione:** i documenti suddivisi si trovano tramite il loro
  documento padre, e la colonna Failed Filenames elenca solo i file
  effettivamente falliti o saltati.
- **Pagina di importazione:** non va più in errore per le organizzazioni con
  una voce di abbonamento vuota.
- **Ricerca nella dashboard:** Invoice Type è disponibile come campo di
  ricerca con il suo elenco di valori.
- **Attività e notifiche:** l'opzione di eliminazione è nascosta agli utenti
  senza diritti di amministratore.
- **Workflow Builder:** le card appena create o rinominate, i modelli e-mail
  e le altre voci dei menu a tendina compaiono subito, senza ricaricare la
  pagina.
- **Tipi di documento:** nuova impostazione Structured Extraction nella
  sezione di estrazione.
- **Selezione del modello AI:** il livello Turbo ritirato è sparito dal menu
  a tendina; le selezioni esistenti mostrano Fast.
- **Finestra Versioni dei servizi:** ora è scorrevole, include il servizio
  Auth Bridge e mostra i nomi dei canali di rilascio Vesta e Nova.
- **Validazione dei campi:** il campo del numero di pagina è più largo e
  salta alla pagina premendo Invio. Un campo reso di sola lettura da uno
  script continua a mostrare la sua connessione campo.
- **Estrazione tabelle:** eliminare una colonna libera il suo nome per il
  riutilizzo, e le intestazioni eliminate non ricompaiono più nella tabella
  salvata.
- **Correzioni minori:** le notifiche toast vuote vengono soppresse, la
  finestra di creazione/modifica delle idee è scorrevole, le caselle
  disallineate nelle impostazioni dei campi sono di nuovo allineate, le
  eliminazioni di documenti bloccate spiegano il motivo, e le impostazioni
  E-Document gestiscono correttamente il passaggio da Default a Custom.

## API Service — live: `12.61.8`

- **Regole di validazione, più mature:** nuovi operatori di condizione
  (contiene, inizia con, finisce con), valori provenienti da fonti a elenco
  di valori, attivazione per tipo di documento e un audit trail che mostra
  chi ha creato o modificato ogni regola. Alla modifica delle regole i
  documenti vengono rivalidati automaticamente.
- **Regole di trasformazione:** possono ora impostare o cancellare valori
  sull'intero documento, si attivano per tipo di documento e hanno lo stesso
  audit trail.
- **Regole di selezione del layout:** l'attivazione è passata al tipo di
  documento, e i modelli di layout registrano chi li ha modificati e quando.
- **Sicurezza degli script:** le modifiche agli script richiedono una
  password a tempo (vedi Highlights).
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
  esportazioni M3 possono includere addebiti di riga a importo zero.
- **Approvazioni:** un'approvazione viene collegata a una richiesta di
  approvazione solo quando l'approvatore ne è l'assegnatario.
- **Stabilità del login:** un errore temporaneo nella validazione del token
  non disconnette più gli utenti; l'app riprova.
- **Classificazione:** le regole sulla provenienza confrontano ora tutti i
  campi di origine del documento, non posizioni fisse.
- **Modelli AI:** il livello Turbo (ritirato) viene rimappato ovunque su
  Fast, incluse le varianti fine-tuned, con una protezione che impedisce a
  un modello ritirato di essere eseguito.

## Auth Service — live: `1.72.5`

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

## Email Service — live: `1.39.8`

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

## PO Match Service — live: `1.58.6`

- **Stato "tabella incompleta":** le fatture la cui tabella delle righe non
  poteva essere mappata ricevono un proprio stato invece del fuorviante
  "ordine d'acquisto non trovato" (vedi Highlights). La dashboard lo mostra
  con l'icona di mancata corrispondenza.
- **Dettaglio errori migliore:** gli errori di mappatura della tabella
  indicano la colonna specifica che non è stata mappata.
- **Comportamento API più pulito:** le richieste di regole PO inesistenti
  restituiscono una corretta risposta not-found, e le voci di cache corrotte
  vengono scartate invece di causare errori ripetuti.

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

## OCR Service — live: `1.9.8`

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

## Docflow Service — live: `2.6.5`

- **PO matching nei workflow:** i valori di confronto mancanti vengono
  trattati come dati mancanti, non come una mancata corrispondenza.
- **Card di conferma d'ordine:** acquirente e responsabile vengono risolti
  in modo affidabile.
- **Spese di trasporto:** quando nessuna delle due parti ha spese, il caso
  viene risolto dalla card dell'operatore invece di rimanere in stallo.
- **Sicurezza:** i token API dei workflow vengono validati rispetto
  all'organizzazione a cui appartengono.

## Barcode Service — live: `1.17.4`

- **Suddivisioni di lunga durata:** la connessione alla coda dei task resta
  attiva durante i job barcode prolungati, quindi la suddivisione di batch
  di grandi dimensioni non si blocca più verso la fine.

---

## Invariati in questa release

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **FTP** (`1.31.1`), **Operator** (`1.40.2`) e **Ideas**
(`0.3.1`) non presentano modifiche in questa finestra.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact git
     ranges between the LATEST (2026-07-09..15) and NOVA (2026-07-15..21)
     version-bump commits supplied by the user, per service). -->
