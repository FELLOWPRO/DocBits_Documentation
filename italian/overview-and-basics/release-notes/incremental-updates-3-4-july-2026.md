# Note della versione DocBits — 3–4 luglio 2026

_Una panoramica di ciò che cambia per voi con questa release di DocBits. Ogni
servizio qui sotto mostra la versione ora in produzione, seguita dalle novità o
correzioni spiegate in linguaggio semplice — senza numeri di ticket né gergo
tecnico. I servizi non elencati non hanno avuto modifiche visibili ai clienti in
questo periodo._

---

## Highlights

- **Deploy senza downtime, in tutta la flotta.** API, Auto Accounting,
  Docflow, Extraction, OCR e PO Match ora si arrestano in modo pulito quando
  viene rilasciata una nuova versione. In precedenza, una richiesta in corso
  durante un deploy poteva essere interrotta; ora ogni richiesta in corso
  viene completata prima che la versione precedente si fermi, quindi i
  rilasci non causano più brevi interruzioni per gli utenti.
- **Miglioramenti all'esportazione delle fatture elettroniche.** Esportare un
  documento verso più configurazioni di esportazione contemporaneamente è ora
  più affidabile: i controlli anti-duplicazione dell'esportazione vengono
  eseguiti una sola volta per lotto invece che per singolo elemento, e un nuovo
  endpoint di esportazione evita che lo stato dell'esportazione lampeggi quando
  vengono avviate più esportazioni insieme. Anche i documenti XRechnung/ZUGFeRD
  ottengono una mappatura dei campi più coerente.
- **Elaborazione dei documenti più stabile.** Corretto un crash che poteva far
  fallire un intero documento OCR quando una singola pagina falliva, corretta
  la sincronizzazione delle consegne degli ordini di acquisto che recuperava
  sempre e solo i primi 100 record, e rafforzati diversi servizi contro brevi
  interruzioni della connessione al database.
- **Allegati e-mail recuperati.** Corretto un caso in cui gli allegati e-mail
  potevano arrivare corrotti o con byte mancanti durante l'importazione in
  entrata.
- **Affidabilità dei workflow.** Corretti i workflow che rimanevano bloccati a
  causa di un lock che non veniva rilasciato correttamente, e corretta la
  logica di riprogrammazione in modo che i passaggi del workflow saltati
  vengano gestiti e registrati correttamente.
- **Novità: Ideas Service.** Un nuovo servizio backend (Ideas, v0.3.0) si è
  unito alla flotta di produzione.

---

## API Service — live: `12.52.4`

- **Affidabilità OCR:** un crash su una singola pagina non fa più fallire
  l'intero documento.
- **Esportazione:** i controlli anti-duplicazione dell'esportazione vengono ora
  eseguiti una sola volta per lotto invece che una volta per elemento; un nuovo
  endpoint di esportazione evita che lo stato dell'esportazione lampeggi quando
  più esportazioni vengono eseguite contemporaneamente; i documenti
  XRechnung/ZUGFeRD ottengono una mappatura dei campi canonici più coerente.
- **Ordini di acquisto:** corretta la sincronizzazione delle consegne che
  recuperava solo i primi 100 record per ordine.
- **Log delle attività:** corretto il pulsante "Successivo" della pagina che
  saltava a un intervallo temporale non correlato.
- **Ricerca anagrafica fornitori:** corretto un errore del server (HTTP 500).
- **Indicizzazione per la ricerca:** aggiunto un indicatore di consegna
  garantita e un nuovo tentativo, in modo che i documenti vengano messi in coda
  in modo affidabile per la ricerca full-text.
- **Deploy senza downtime:** le richieste in corso vengono ora completate
  prima che un rilascio riavvii il servizio.
- Correzioni generali di stabilità che risolvono diversi errori ricorrenti in
  background.

## Auth Service — live: `1.68.7`

- Solo manutenzione interna e affidabilità in questo periodo.

## Auto Accounting — live: `1.18.8`

- **Deploy senza downtime:** le richieste in corso vengono ora completate
  prima che un rilascio riavvii il servizio.

## Barcode Service — live: `1.15.8`

- Solo una correzione interna alla configurazione di distribuzione in questo
  periodo.

## Docflow Service — live: `2.5.3`

- **Nuova opzione di esportazione** per inviare un documento verso più
  configurazioni di esportazione contemporaneamente.
- **Corretti i workflow che rimanevano bloccati** a causa di un lock che non
  veniva rilasciato correttamente, indipendentemente dallo stato.
- **Corretta la riprogrammazione dei workflow** in modo che i passaggi saltati
  vengano gestiti e registrati correttamente invece di essere scartati in
  silenzio.
- **Avvio più veloce:** i database vengono ora pre-riscaldati in background.
- Maggiore resilienza contro brevi interruzioni della connessione al database.
- Migliorata l'analisi dei campi data per le schede workflow.
- **Deploy senza downtime:** le richieste in corso vengono ora completate
  prima che un rilascio riavvii il servizio.

## Email Service — live: `1.37.9`

- **Corretti gli allegati in entrata** che potevano arrivare corrotti o con
  byte mancanti.
- **Errori più chiari** quando una cartella della casella di posta non può
  essere recuperata, invece di un errore generico.

## Extraction Service — live: `1.49.6`

- **Corretti i crash** su documenti con un tipo di documento non riconosciuto e
  su tabelle con una forma insolita o malformata.
- Maggiore resilienza contro brevi interruzioni della connessione al database
  durante una query.
- **Deploy senza downtime:** le richieste in corso vengono ora completate
  prima che un rilascio riavvii il servizio.

## FTP Service — live: `1.30.3`

- Solo un aggiornamento interno del framework in questo periodo.

## Fulltext Service — live: `1.36.3`

- **Indicizzazione per la ricerca:** un controllo periodico ora ripara
  eventuali documenti che non erano riusciti a raggiungere l'indice di ricerca
  per una qualsiasi organizzazione.
- **Sincronizzazione ERP:** corretto un lock bloccato che poteva impedire la
  sincronizzazione ERP dopo un tentativo fallito.

## OCR Service — live: `1.7.8`

- **Corretta l'autenticazione OCR** in modo che le chiavi API
  dell'organizzazione funzionino di nuovo correttamente.
- **Deploy senza downtime:** le richieste in corso vengono ora completate
  prima che un rilascio riavvii il servizio.

## Operator Service — live: `1.39.7`

- Solo correzioni interne di affidabilità della distribuzione in questo
  periodo.

## PO Match Service — live: `1.56.0`

- **Corretto un crash** durante l'ordinamento delle quantità PO Match che
  includevano valori vuoti.
- **Deploy senza downtime:** le richieste in corso vengono ora completate
  prima che un rilascio riavvii il servizio.

## Web App — live: `10.36.9`

- **Corretto un errore** nel tornare alla schermata di validazione dei campi da
  un'altra schermata.
- **Corretto il pulsante "Scripts"** che indirizzava a una pagina 404.
- **Log delle attività:** corretta una visualizzazione errata "Pagina 2 di 1" e
  corretto il filtro di severità WARN che non trovava alcuna corrispondenza.

---

## Nessuna modifica visibile ai clienti in questo periodo

Auth Service, Barcode Service, FTP Service, Operator Service e Docnet Service
(`1.54.6`, invariato) hanno ricevuto solo manutenzione interna o alla
configurazione di distribuzione.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
