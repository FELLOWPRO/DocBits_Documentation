# Note della versione DocBits — 30 giugno – 3 luglio 2026

_Cosa ha introdotto questo aggiornamento in produzione, spiegato in modo
semplice. Per ogni servizio viene indicata la versione ora attiva in produzione.
I servizi non elencati non hanno avuto modifiche visibili ai clienti in questo
periodo._

---

## Highlights

- **Chat AI sui log delle attività.** Un nuovo pannello di chat AI nella pagina
  Activity Logs consente di porre domande direttamente sull'attività dei log,
  senza dover scavare tra le voci grezze.
- **Tracciamento delle e-mail in uscita nel registro di importazione.** Il
  registro di importazione ora registra anche la posta in uscita oltre a quella
  in entrata, con filtri rapidi per Errori / In entrata / In uscita — le caselle
  di posta con errori ripetuti vengono ora disattivate automaticamente, gli
  amministratori possono essere avvisati via e-mail in caso di errore di
  importazione e i tentativi vengono ora ripetuti fino a 15 volte nell'arco di
  circa 5 ore prima di arrendersi.
- **Errori di importazione e-mail più chiari.** Gli errori di accesso mostrano
  ora il motivo reale sottostante, con messaggi dedicati per un certificato non
  valido o una password per app Gmail errata.
- **Corretto il loop di accesso.** Alcuni utenti potevano rimanere bloccati in
  un ciclo ripetuto di accesso durante il refresh del token — risolto.
- **Elaborazione dei documenti più stabile.** Corretto un crash durante
  l'estrazione dei dati causato da valori di coordinate non arrotondati, la
  lettura dei codici a barre ora ritenta automaticamente gli errori recuperabili
  invece di arrendersi silenziosamente, e risolto un raro caso in cui un
  documento poteva essere esportato due volte contemporaneamente.
- **Miglioramenti alla schermata di validazione.** Ora è possibile ingrandire
  ulteriormente i documenti, i campi non vengono più svuotati dagli script
  quando il loro valore non è effettivamente cambiato, e la dashboard ricorda
  la posizione della pagina quando si torna indietro.

---

## Web App — live: `10.35.7`

- **Pannello di chat AI** aggiunto alla pagina Activity Logs (#15512).
- **Registro di importazione:** nuovi filtri rapidi Errori / In entrata / In
  uscita; opzione e campo per i destinatari delle notifiche di errore nelle
  impostazioni e-mail in entrata.
- **Schermata di validazione:** lo zoom sui documenti va ora oltre la
  dimensione predefinita precedente; i campi svuotati dagli script di
  validazione ora mantengono correttamente il proprio valore quando lo script
  restituisce lo stesso valore.
- **Dashboard:** la posizione della pagina viene mantenuta quando si torna
  alla tabella; la maniglia di ridimensionamento delle colonne non fuoriesce
  più dall'intestazione della tabella.
- **Schermata Auto Accounting:** corretto un errore di validazione.
- **DocBits Tasks:** corretto un problema di permessi.
- **Log Watchdog:** aggiunto un filtro per intervallo di tempo e un selettore
  regolabile del numero di righe per pagina.
- **Correzioni:** un errore del grafico ("Element not found") sulla pagina
  Boards; un link di eliminazione-esportazione non funzionante su Activity
  Logs; correzioni di layout sulla schermata Layout Builder; una traduzione
  mancante nel filtro per intervallo di tempo di Activity Logs.
- **Aggiornamento automatico:** ulteriore rafforzamento del meccanismo di
  aggiornamento automatico dell'app (pulizia più rapida all'avvio, rilevamento
  della versione più affidabile, pulizia della cache prima di un ricaricamento
  di recupero).

## API Service — live: `12.48.1`

- **Caricamento più veloce degli script dei documenti:** gli script di
  validazione vengono ora memorizzati nella cache lato server (cache di 6 ore)
  invece di essere recuperati ogni volta.
- **Confidenza degli importi più accurata:** il punteggio di confidenza ora
  tiene conto dei documenti che utilizzano convenzioni diverse per il
  separatore decimale.
- **Affidabilità:** la validazione dei documenti esegue sempre l'unica versione
  attiva dello script, e quale versione è stata eseguita viene ora registrato
  nei log; risolto un raro caso in cui un documento poteva essere esportato due
  volte contemporaneamente; le regole di estrazione specifiche del fornitore
  vengono nuovamente applicate correttamente dopo un nuovo OCR forzato.
- **Importazione e-mail:** aggiunto il supporto backend per la registrazione
  della posta in uscita e le e-mail di notifica degli errori (vedi Email
  Service, di seguito).

## Auth Service — live: `1.68.5`

- **Corretto un loop di accesso** in cui alcuni utenti potevano rimanere
  bloccati mentre il token di sessione veniva aggiornato.
- **Schermate di amministrazione dell'organizzazione più veloci:** i dati di
  utenti e abbonamenti vengono ora caricati in blocco invece che un record alla
  volta.
- **Corretto un raro conflitto del database** durante il collegamento di un
  utente a un'organizzazione.

## Email Service — live: `1.37.4`

- **Il registro di importazione ora traccia anche la posta in uscita** oltre a
  quella in entrata, con un filtro per mostrare solo le importazioni in
  entrata, in uscita o fallite.
- **Le caselle di posta con errori ripetuti vengono ora disattivate
  automaticamente**, e gli amministratori possono essere avvisati via e-mail
  quando un'importazione fallisce; i tentativi vengono ora ripetuti fino a 15
  volte nell'arco di circa 5 ore prima di arrendersi.
- **Messaggi di errore di accesso più chiari:** mostra il motivo reale
  sottostante, un messaggio dedicato per un certificato non valido e un
  messaggio specifico per una password per app Gmail errata.
- **Corretto l'instradamento in entrata** che riscriveva erroneamente gli
  indirizzi server per gli account della regione UE.
- Maggiore resilienza contro brevi interruzioni della connessione Redis.

## Extraction Service — live: `1.49.0`

- **Corretto un crash durante l'estrazione** causato da valori di coordinate
  non arrotondati.
- **Confidenza degli importi più accurata** per i documenti con formati di
  separatore decimale misti; piccole differenze di arrotondamento nel totale
  imposte non bloccano più un abbinamento.

## Docflow Service — live: `2.4.2`

- **Riprogettata l'autenticazione per i workflow avanzati (basati su Celery)**,
  con protezioni che impediscono a un controllo di autenticazione fallito di
  mandare in crash l'esecuzione di un workflow.
- **Risposta più chiara** quando un passaggio del workflow tenta di essere
  eseguito su un workflow che non esiste più.

## Barcode Service — live: `1.15.7`

- **La lettura dei codici a barre ora ritenta automaticamente** gli errori
  recuperabili invece di arrendersi silenziosamente.

## OCR Service — live: `1.7.3`

- **Corretto un errore OCR** causato da un problema di risoluzione del nome
  host Redis.
- Le disconnessioni Redis durante i controlli di integrità non vengono più
  registrate come errori, riducendo i falsi allarmi.

## PO Match Service — live: `1.55.8`

- **Corrette le note che non comparivano** nei record PO Match.

---

## Nessuna modifica visibile ai clienti in questo periodo

Stabili, senza modifiche di prodotto rilevanti tra il 30 giugno e il 3 luglio:
Auto Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext
(`1.35.7`), Operator (`1.39.5`). Auto Accounting ha ricevuto solo manutenzione
interna alla configurazione di distribuzione. Non è stato possibile raggiungere
Ideas Service per un controllo della versione in questo periodo.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
