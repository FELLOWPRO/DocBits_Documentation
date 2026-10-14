# Note della versione DocBits — 14 ottobre 2026

_Cosa cambia con l'hotfix di produzione di DocBits del 14 ottobre 2026
(release R1.0.15), che copre tutto quanto rilasciato dopo l'[hotfix del 15 settembre](incremental-updates-15-september-2026.md).
Per ogni servizio è indicata la versione in distribuzione, seguita dalle
novità e correzioni spiegate in linguaggio semplice. I servizi non elencati non
hanno avuto modifiche visibili ai clienti._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/it.mp4" %}

---

## Highlights

- **Il Settings Assistant.** Una barra di chat in ogni pagina delle
  impostazioni risponde alle domande sulla configurazione della vostra
  organizzazione, nella vostra lingua e sulla base della documentazione di
  DocBits. Legge lo stato attuale delle impostazioni e lo spiega (permessi di
  gruppo, canali di importazione, interruttori degli ordini di acquisto,
  contabilità). Quando gli chiedete di attivare o disattivare qualcosa, mostra
  prima un'anteprima, attende la vostra conferma e offre l'annullamento.
  "Open setting" porta direttamente all'impostazione, anche all'interno di una
  sezione compressa, e la evidenzia. Gli amministratori dell'organizzazione
  attivano o disattivano l'assistente in Company Information. Risponde solo a
  domande su DocBits e non modifica mai nulla senza conferma.
- **Nuovi livelli AI.** I livelli Fast e Full usano nuovi modelli. Un nuovo
  livello Auto sceglie Fast o Full per ogni documento, e Nexus Flash si
  affianca a Nexus. Una modalità visione (ibrida o automatica) decide quando
  inviare anche l'immagine della pagina. Le preferenze salvate dei modelli AI
  passano da sole ai nuovi livelli, e le schermate mostrano solo i nomi dei
  livelli. "Use AI" è un menu a tendina (Standard, Sì, No) con un'anteprima di
  ciò che richiederà l'estrazione strutturata.
- **Controllo dei campi di intestazione.** La schermata di validazione ha un
  pulsante "Header field check" accanto a Salva. Il suo report elenca ogni
  campo di intestazione con l'origine del valore (AI, regola, script o dati
  master), in una tabella compatta con filtro per origine, ricerca e
  ordinamento, e con le stesse etichette dei campi della schermata di
  validazione. Il popup dell'origine mostra la fonte di ogni valore in un'unica
  striscia.
- **Sicurezza dell'accesso e dell'organizzazione.** Una sfida MFA può essere
  usata una sola volta su ogni percorso di accesso, e la registrazione di un
  autenticatore richiede il codice via e-mail. Le organizzazioni possiedono un
  elenco di domini e-mail verificati; un accesso social (ad esempio Microsoft)
  entra nell'organizzazione che elenca il dominio e non crea mai da solo
  un'organizzazione, un utente o un abbonamento. Solo gli amministratori
  dell'organizzazione modificano le preferenze dell'organizzazione e scrivono o
  approvano le regole di corrispondenza degli ordini di acquisto. Le risposte in
  cache non possono più trapelare tra organizzazioni.
- **Corrispondenza degli ordini di acquisto e addebiti.** Gli addebiti che
  l'ordine di acquisto prevede a zero ricevono una soglia assoluta, la
  tolleranza sugli addebiti si applica anche agli addebiti che l'ordine non
  prevede a budget, e un campo può elencare più elementi di costo i cui importi
  vengono ripartiti proporzionalmente all'ordine di acquisto. Una colonna di
  corrispondenza può avere un flag "allow mismatch". Le schede dei workflow
  confrontano gli addebiti per elenco, e il limite di esecuzione dei workflow
  passa da 30 a 50.
- **Meno numeri errati.** Gli importi vengono mostrati nel formato personale di
  ogni utente (Svizzera e Slovenia incluse), i valori con sola data mantengono
  il proprio giorno di calendario in ogni fuso orario, l'equazione del totale
  USA tiene conto degli importi aggiuntivi e delle fatture con più imposte, e i
  documenti con importi di intestazione pari a 0,00 non finiscono più nel
  passaggio sbagliato dei candidati.

---

## Corretto anche in questa release

- La dashboard non resta più vuota quando una condizione di concorrenza imposta
  il filtro della sotto-organizzazione sull'id dell'organizzazione, escludendo
  così tutti i documenti.
- I valori delle dimensioni possono di nuovo essere selezionati da ogni utente.
- È stato corretto un errore di caricamento segnalato da un cliente.
- "Match on total" funziona per i fornitori la cui fattura ha una sola riga, e
  per le configurazioni fornitore che lo avevano segnalato.
- E-document SPS: gli addebiti 810 sono stati adeguati, il layout degli
  addebiti 855 è stato aggiornato, e il logo del cliente nell'anteprima
  dell'e-document è stato corretto.

---

## Web App — `10.78.9.4`

**Settings Assistant**
- Un pannello di chat sul lato destro con un interruttore è presente in tutte
  le pagine delle impostazioni. La conversazione resta attiva al cambio di
  pagina, è limitata a 20 messaggi e mostra le modifiche applicate con la
  possibilità di annullarle.
- Vi accoglie con domande adatte alla pagina delle impostazioni corrente e
  mostra schede delle impostazioni con un interruttore on/off. Esc chiude prima
  i menu, Stop interrompe una risposta in corso, e le schermate nelle risposte
  si aprono in un lightbox.
- L'applicazione di una modifica apre una finestra di dialogo con anteprima,
  conferma e annullamento.
- Ogni impostazione è ricercabile dalla barra laterale, e l'impostazione
  trovata viene evidenziata con un colore diverso. "Open setting" scorre fino
  alla destinazione all'interno di un accordion compresso.
- Un interruttore per gli amministratori dell'organizzazione per l'assistente
  si trova in Company Information.
- I consigli AI sono attribuiti a Nova, e compaiono solo i nomi dei livelli,
  mai gli id dei modelli.

**Schermata di validazione e gestione dei documenti**
- Nuovo pulsante "Header field check" con report, origine per campo e pagina di
  aiuto (vedere Highlights). Le etichette delle origini e i chip di stato
  restano all'interno delle rispettive celle.
- I badge di testo "from master data" accanto alle etichette dei campi sono
  stati rimossi; le informazioni sono ora nel popup dell'origine.
- Un'unica validazione condivisa dei campi viene eseguita ovunque, il che
  elimina l'errore generico "One or more fields need validation" dopo Auto
  Accounting.
- I tooltip sui pulsanti del popup del campo (Elimina, Cancella, Conferma)
  spiegano che cosa fa ciascuno prima di fare clic.
- Una riga ottimistica mostra ora ciò che è stato memorizzato, non ciò che è
  stato digitato. Una rimappatura delle colonne chiede conferma solo quando una
  colonna visibile perde la propria mappatura.
- Le pagine oltre il limite di pagine OCR sono in sola lettura e contrassegnate,
  anche nel visualizzatore di Auto Accounting. Il vecchio pannello di
  restrizione delle pagine in importazione è stato eliminato.
- Compare una tabella PO per ogni numero di ordine di acquisto in un campo di
  intestazione con più PO, e il Layout Builder assegna alle schede PO le
  etichette dalla chiave della tabella PO e non segnala più il modulo come
  disattivato quando la tabella PO è attiva.
- La scheda della proposta mostra la tolleranza invece di `[object Object]`, e
  la schermata di confronto dell'approvazione non arrotonda più le colonne di
  confronto configurate (numeri articolo).

**Account, impostazioni ed errori**
- Ogni messaggio di errore e ogni errore di accesso mostra il trace id della
  richiesta non riuscita, così il supporto può trovarla. Gli errori WebSocket
  della dashboard rifiutano esattamente la richiesta che indicano.
- Company Information elenca i domini e-mail dell'organizzazione.
- Gli amministratori possono inviare di nuovo l'e-mail "Set your password" dalla
  pagina dell'utente.
- Gli amministratori globali impostano l'inizio del contratto nella tabella
  degli abbonamenti.
- Gli amministratori dell'organizzazione vedono la scheda Executive Dashboard e
  i pulsanti di aggiunta ed eliminazione XSLT. I membri salvano i layout come
  preferenza personale.
- Una sessione senza organizzazione riceve un errore chiaro e il selettore
  dell'organizzazione invece di una dashboard vuota.
- Gli importi seguono il formato numerico personale dell'utente, e i valori con
  sola data mantengono il proprio giorno in ogni fuso orario.
- I dati master inviano gli id delle sotto-organizzazioni solo quando
  differiscono dall'id dell'organizzazione, e le intestazioni personalizzate dei
  dati master vengono inviate come intestazioni.
- La maschera Tabelle non taglia più il menu a tendina "Use AI", il testo di
  suggerimento AI non copre più la riga di addestramento, e la tabella AI
  mantiene il pulsante Applica diretto, con un controllo dell'intestazione a
  sola icona e un messaggio di licenza.
- Le icone dell'estrazione delle tabelle vengono di nuovo visualizzate dopo la
  rimozione del vecchio font di icone.

**Tasks board**
- La board carica la prima pagina con meno richieste duplicate, Invio avvia
  subito la ricerca, le risposte tardive vengono associate alla ricerca giusta,
  il piè di pagina mostra il numero reale di risultati invece della capacità
  della pagina, e un'eliminazione avviata in un'organizzazione viene annullata
  prima dell'invio quando si cambia organizzazione.

---

## API Service — `12.83.293`

**Settings Assistant e MCP**
- Endpoint di chat con barriere di sicurezza: solo domande su DocBits, nessuna
  modifica senza conferma, le domande poco chiare o meta ricevono aiuto invece
  di un rifiuto, e le risposte trasmettono prima le schede, poi il testo.
- Elementi di base in sola lettura per ogni area delle impostazioni (permessi di
  gruppo, canali di importazione, PO matching, contabilità, domini e-mail), un
  catalogo di collegamenti diretti con uno strumento di ricerca delle
  impostazioni, e una ricerca nella documentazione con immagini dalla
  documentazione di DocBits.
- Flusso di applicazione, prima ondata: anteprima, conferma e annullamento per
  le impostazioni supportate, una regola di ambito unica per tutti e tre,
  protetto da doppia conferma e da scadenza.
- Gli strumenti MCP non leggono mai file dal server in modalità remota, e gli
  strumenti di fixture e laboratorio funzionano solo su dev.

**AI**
- Nuovi modelli dietro i livelli Fast e Full, il livello Auto, Nexus Flash e la
  preferenza della modalità visione. Le preferenze `AI_MODEL` memorizzate
  passano ai nuovi livelli.
- "Use AI" documenta ciò che richiede l'estrazione strutturata.

**Sicurezza e isolamento**
- Solo gli amministratori dell'organizzazione modificano le preferenze
  dell'organizzazione.
- La chiamata `/accounting/rebuild` addestra solo l'organizzazione del
  chiamante, si blocca in modo sicuro se la ricerca dell'organizzazione fallisce
  e risponde 400 per un id non valido.
- Il rendering di XSLT, XML e PDF nega l'accesso a file e rete, non risolve
  inclusioni esterne, e i byte delle fatture vengono sanificati prima di
  raggiungere il trasformatore. Le anteprime PDF renderizzate consentono solo
  host di immagini attendibili.
- Le chiavi della cache includono l'organizzazione e lo stesso identificatore
  produce sempre la stessa chiave, quindi l'id di un'altra organizzazione non
  può più leggere dati in cache. Le cancellazioni della cache della dashboard
  su tutta l'organizzazione a ogni modifica di documento sono state eliminate.
- L'elenco dei domini e-mail dell'organizzazione viene inoltrato ad Auth.

**Corrispondenza degli ordini di acquisto ed esportazione**
- Un campo può elencare più elementi di costo i cui importi vengono ripartiti
  proporzionalmente al PO.
- I sostituti di approvazione puntano alla richiesta di approvazione attiva, i
  salvataggi di approvazioni riparate non bloccano più, e un documento in
  attesa di approvazione viene rifiutato per l'esportazione.
- L'annotazione PDF/A conserva il catalogo e l'XML incorporato, così le
  e-fatture mantengono il proprio XML dopo l'annotazione. Le fatture UBL con il
  CustomizationID EN 16931 semplice vengono classificate (rete di e-fatture).
- GRPR arrotonda a 6 decimali, il massimo accettato da M3. I fattori di
  conversione dell'unità di misura di base vengono aggiunti alla riga
  congelata.
- Gli addestramenti e le regole di formattazione eliminati in modo logico
  vengono rispettati, e `update_document_fields` di MCP non conferma più una
  scrittura andata persa. `get_table_rules` risponde con un mancato riscontro
  tipizzato, e un payload di traduzioni vuoto usa il proprio fallback.
- Gli importi sloveni usano `sl_SI` e le preferenze salvate vengono migrate. Le
  etichette di classificazione personalizzate inviate come id UUID vengono
  risolte. Le dashboard condivise mantengono `created_by` e l'elenco di
  condivisione all'aggiornamento.
- I frame di errore della dashboard riportano il `request_id` della richiesta, e
  ogni risposta JSON non riuscita riporta un trace id.
- Il sistema riavvia solo i worker non integri invece dell'intera flotta API e
  controlla correttamente l'elenco dei task registrati. La coda del monitor
  dei blocchi viene di nuovo consumata.

---

## Auth Service — `1.78.49`

- Una sfida a più fattori è monouso su ogni percorso di accesso, non solo nel
  flusso MCP. La registrazione richiede il codice via e-mail, dopo un accesso
  con password condivisa non viene emesso alcun token di registrazione, e gli
  utenti vengono avvisati quando un fattore viene registrato.
- Le organizzazioni possiedono un elenco di domini e-mail, ciascuno
  assegnabile una sola volta. Un accesso social entra nell'organizzazione che
  elenca il dominio verificato, non inventa mai un'organizzazione, un utente o
  un abbonamento, e rifiuta senza nominare nessuno, mentre gli amministratori
  vengono avvisati. I domini restituiti da Microsoft vengono gestiti.
- Ogni accesso rifiutato riporta un trace id. Gli amministratori possono
  inviare di nuovo l'e-mail "Set your password". Il saldo del contratto è con
  segno e l'inizio del contratto viene sottoposto ad audit.

## Auth Bridge — `0.5.7`

- La replica degli account UE e USA mantiene alimentata la propria connessione
  durante la riconciliazione, riaggancia da sola uno slot di replica
  interrotto, usa memoria limitata e considera un'origine di replica esistente
  come un successo. L'accesso tra regioni è più affidabile.

## Docflow Service — `2.10.22`

- La scheda separata del prezzo unitario legge le definizioni di campo
  predefinite dell'organizzazione per gli addebiti e confronta ogni elemento di
  costo elencato da un campo.
- Il limite di esecuzione dei workflow passa da 30 a 50, e le ricerche nei log
  dei workflow rifiutano un id che non è un UUID.

## Docnet Service — `1.56.15`

- `list_document_fields` riporta ogni colonna di tabella configurata, comprese
  quelle vuote.

## Extraction Service — `1.56.0.1`

- Livelli: nuovi modelli dietro Fast e Full, Auto, Nexus Flash e una modalità
  visione. Le richieste di visione verso l'host di inferenza restano entro il
  suo limite di dimensione.
- L'estrazione delle tabelle con Nexus raggruppa le pagine in lotti (due per
  lotto), esegue i lotti in parallelo con un timeout misurato, ripete gli errori
  transitori e divide un lotto andato in timeout. I campi di intestazione
  vengono letti da tutti i lotti.
- Totali USA: gli importi aggiuntivi fanno parte dell'equazione del totale, la
  coppia 1 conta nella protezione della coppia 2, i candidati con punteggio
  basso vengono saltati quando le imposte non sono zero, e "above" e "below"
  corrispondono a etichette di più parole.
- I campi identificativi riparano i caratteri che si presentano davvero, e i
  caratteri invisibili vengono trattati per il loro significato, così una "O"
  non diventa più un carattere strano.

## Fulltext Service — `1.42.41`

- Nuovo indice per la documentazione di DocBits, con endpoint di ingestione e di
  ricerca, immagini nelle risposte e un limite di tempo per l'intera ricerca.
  Alimenta il Settings Assistant.

## PO Match Service — `1.59.48`

- Soglia assoluta per gli addebiti che l'ordine di acquisto prevede a zero, e
  tolleranza sugli addebiti che l'ordine non prevede a budget.
- Una colonna può avere un flag "allow mismatch". Più elementi di costo per
  campo vengono ripartiti proporzionalmente.
- Solo gli amministratori dell'organizzazione scrivono o approvano le regole di
  corrispondenza, e le condizioni delle regole accettano solo una grammatica di
  espressioni in whitelist.
- Le modifiche alle regole possono essere simulate rispetto a un insieme di
  regole di override senza scrivere, per le proposte di modifica di Touchless.
  Le colonne extra del PO da abbinare vengono lette dall'attributo del tipo di
  documento, con la migrazione della vecchia preferenza.

---

_Non interessati in questa release: Auto Accounting, Barcode, E-Mail, FTP,
Ideas, OCR, Operator. FTP e Operator contengono solo manutenzione interna._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Wednesday 14 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from one supplier not arriving, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->
