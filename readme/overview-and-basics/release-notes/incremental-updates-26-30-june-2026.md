# Note della versione DocBits — 26–30 giugno 2026

_Cosa ha introdotto questo aggiornamento in produzione, spiegato in modo
semplice. Per ogni servizio viene indicata la versione ora attiva in produzione.
I servizi non elencati non hanno avuto modifiche visibili ai clienti in questo
periodo._

---

## Highlights

- **Un'unica connessione per gli assistenti AI (DocBits MCP).** Un unico gateway
  unificato serve ora tutti gli strumenti DocBits — incluso DocFlow — attraverso
  l'API principale, così gli assistenti AI (Claude, Gemini CLI, Codex) si
  connettono tramite un unico endpoint affidabile anziché tramite diversi.
- **Ricerca multilingue più intelligente nella dashboard.** I connettori di ricerca
  (**AND / OR**) appaiono ora nella tua lingua con evidenziazione a colori, i
  sotto-tipi di fattura offrono un menu a tendina dei valori e i messaggi sulla
  sintassi di ricerca sono localizzati — con una gestione da tastiera più fluida
  ovunque.
- **Approvazioni e permessi più fluidi.** L'approvazione non viene più attivata
  quando l'unità di imballaggio di una conferma d'ordine è vuota, gli utenti
  normali possono di nuovo approvare gli elementi di costo dopo la migrazione del
  controllo degli accessi e i permessi a livello di documento vengono applicati
  correttamente anche quando una colonna della tabella esiste già.
- **L'app si aggiorna da sola.** Quando viene rilasciata una nuova versione,
  DocBits ora si aggiorna automaticamente invece di interromperti con un popup
  "Aggiorna ora".
- **Abbinamento degli ordini d'acquisto più robusto.** Le trasformazioni dei valori
  di colonna, le protezioni anti-crash per le righe prive di prezzo o quantità e il
  nuovo tentativo automatico in caso di connessioni al database interrotte rendono
  l'abbinamento più stabile.
- **Meno errori su tutta la linea.** Molti rari errori del server su dashboard,
  fatture fornitore, record PO e job OCR sono stati individuati e corretti.

---

## Web App — live: `10.34.4`

- **Ricerca rapida nella dashboard:** connettori **AND / OR** localizzati (de/fr)
  con evidenziazione della sintassi a colori; menu a tendina dei valori per i
  sotto-tipi di fattura; messaggi di errore sulla sintassi di ricerca localizzati;
  esperienza da tastiera più fluida; l'avviso "full-text richiesto" viene ora
  visualizzato inline, così il layout non si sposta più.
- **Approvazioni e permessi:** corretta l'approvazione attivata erroneamente quando
  l'unità di imballaggio di una conferma d'ordine è vuota; gli utenti normali
  possono di nuovo approvare gli elementi di costo dopo la migrazione del controllo
  degli accessi; i permessi a livello di documento vengono ora applicati quando una
  colonna della tabella esiste già.
- **Aggiornamento automatico:** l'app si aggiorna automaticamente quando è
  disponibile una nuova versione invece di mostrare un popup "Aggiorna ora";
  rimossa la vecchia finestra di dialogo con le informazioni sulla versione.
- **Impostazioni e-mail in entrata:** nuova opzione e nuovo campo per i destinatari
  delle notifiche di errore; il registro di importazione mostra ora l'attività in
  uscita e il motivo dell'errore; l'indirizzo in entrata viene copiato in modo
  affidabile.
- **Suddivisione dei documenti:** la schermata di suddivisione dei documenti ora
  consente lo scorrimento.
- **Modalità scura:** correzioni per l'estrazione delle tabelle, il contatore delle
  attività e i marcatori dei documenti chiusi nella dashboard.
- **Usabilità e stabilità:** correzioni all'interfaccia di esportazione della
  dashboard; le intestazioni di tabella fisse non trapelano più attraverso le
  finestre di dialogo; la dashboard DocNet non va più in crash in caso di richiesta
  di statistiche fallita; gli script dei campi non ripristinano più i campi svuotati
  ai loro vecchi valori; correzioni alle caselle di controllo e al layout delle
  impostazioni PO; correzioni alla visualizzazione dell'elenco di classificazione.
- **Fornitori:** le organizzazioni fornitrici possono ora registrarsi tramite magic
  link.

## API Service — live: `12.46.8`

- **Gateway DocBits MCP:** un gateway unificato fa ora da proxy per gli strumenti
  DocFlow attraverso l'API principale, così gli assistenti AI raggiungono ogni
  strumento DocBits tramite un unico endpoint; l'endpoint MCP viene servito senza un
  redirect che potrebbe interrompere le connessioni.
- **Contabilità:** aggiunta la validazione del centro di costo per l'ID contabile.
- **Instradamento OCR:** i documenti vengono inviati per un nuovo OCR completo
  quando l'e-text del fornitore è disattivato, così il testo resta affidabile.
- **Infor ERP / SAP:** gli addebiti aggiuntivi vengono instradati correttamente
  quando l'ERP contiene già l'addebito con un importo pari a zero.
- **Affidabilità (meno errori del server):** rese più robuste le query di
  dashboard, fatture fornitore, record PO e task manager, così non restituiscono
  più rari errori 500; sincronizzazione della cache delle organizzazioni e pulizia
  dei file archiviati più resilienti.
- **Filtri della dashboard più puliti:** rimosso il campo filtro ridondante del
  numero di fattura; corretta la quantità abbinata al PO.
- **Documentazione API per sviluppatori:** l'interfaccia Swagger offre ora un menu
  a tendina delle specifiche (OpenAPI 3.0 più la vista Infor Swagger 2.0) con il
  marchio DocBits.

## Auth Service — live: `1.68.0`

- **Disconnessione / revoca dei token più rapida:** la revoca massiva dei token non
  impiega più diversi minuti né interrompe la connessione.
- **Corrette le e-mail di impostazione password** affinché vengano visualizzate
  correttamente.
- **Fornitori:** le organizzazioni fornitrici possono registrarsi con un magic
  link.
- **Stabilità dell'accesso:** un membro non viene più bloccato in caso di errore
  temporaneo nella ricerca dell'organizzazione e un id organizzazione non valido ora
  restituisce un messaggio chiaro anziché un errore.

## Docflow Service — live: `2.4.1`

- **Gateway AI affidabile:** risolti blocchi e timeout sull'endpoint DocFlow MCP
  (handshake, disconnessioni del client, risposte duplicate) — il lato DocFlow del
  gateway unificato DocBits MCP.

## OCR Service — live: `1.7.1`

- **Elaborazione OCR più stabile:** le code di risposta in background scadono
  automaticamente e i guasti di connessione temporanei vengono ritentati, così meno
  job OCR rimangono bloccati.

## PO Match Service — live: `1.55.7`

- **Le trasformazioni dei valori** vengono ora applicate alle colonne item-id,
  unit-code e static-value durante l'abbinamento basato su regole.
- **Protezioni anti-crash:** una riga priva di prezzo o quantità, una combinazione
  insolita di chiavi ponderate o una divisione impossibile non mandano più in crash
  l'abbinamento.
- **Affidabilità:** le scritture sul database vengono ritentate automaticamente in
  caso di connessioni interrotte o chiuse a livello SSL.
- **Infor ERP / SAP:** gli addebiti aggiuntivi vengono instradati correttamente
  quando l'ERP contiene l'addebito con un importo pari a zero.

## Fulltext Service — live: `1.35.6`

- **Re-indicizzazione più veloce:** tutte le fasi di sincronizzazione ora si
  distribuiscono in parallelo così da attivare l'autoscaling, risolvendo la lenta
  re-indicizzazione seriale e un widget di avanzamento bloccato allo 0%.
- **Statistiche più stabili:** le richieste di statistiche sui documenti tra regioni
  sono limitate così da non andare più in timeout.

---

## Nessuna modifica visibile ai clienti in questo periodo

Stabili, senza modifiche di prodotto rilevanti tra il 26 e il 30 giugno: Auto
Accounting (`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`),
Extraction (`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting e FTP
hanno ricevuto solo manutenzione interna.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
