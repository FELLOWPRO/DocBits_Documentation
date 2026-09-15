# Note della versione DocBits — 15 settembre 2026

_Cosa cambia con l'hotfix di produzione di DocBits del 15 settembre 2026
(release R1.0.13), che copre tutto quanto rilasciato dopo la release del
1° settembre. Per ogni servizio è indicata la versione in distribuzione,
seguita dalle novità e correzioni spiegate in linguaggio semplice. I servizi
non elencati non hanno avuto modifiche visibili ai clienti._

---

## Highlights

- **Un unico insieme di regole per la ricerca nella dashboard.** `field=value`
  significa ora esattamente questo valore su ogni motore di ricerca,
  `field:value` significa "contiene" (con `value*` e `*value` per "inizia con"
  e "termina con"), e `field!=value` restituisce anche i documenti che non
  hanno alcun valore. Una ricerca senza chip è una ricerca per sottostringa su
  tutti i campi, identificativi aziendali inclusi. Il conteggio dei risultati e
  l'elenco dei risultati descrivono lo stesso insieme di documenti, e una
  ricerca che ha raggiunto la finestra dei risultati o è stata eseguita senza
  l'indice full-text lo segnala invece di dichiararsi "completa". La
  connessione di ricerca propria della dashboard (WebSocket) prima non
  raggiungeva mai l'indice full-text; ora lo fa.
- **I fornitori vengono riconosciuti più spesso.** Quando un campo di ricerca
  (identificativo fiscale, IBAN, numero fornitore) corrisponde esattamente a
  un solo fornitore, viene usato quel fornitore anche se un campo generico come
  il nome ne trova diversi. I documenti XRechnung CII e Facturae riportano di
  nuovo i campi del fornitore. Dove i dati master hanno sostituito un valore
  estratto, la schermata di validazione lo indica e permette di ripristinare
  l'originale.
- **La corrispondenza degli ordini di acquisto spiega le proprie decisioni.**
  Lo schermo indica perché non c'è corrispondenza e perché una corrispondenza
  non è stata mantenuta, la cronologia della corrispondenza elenca le regole
  di trasformazione eseguite, e i prezzi unitari PO vengono derivati
  dall'importo netto. Le corrispondenze manuali funzionano di nuovo per le
  organizzazioni senza regola di fallback, e un'attività di corrispondenza
  terminata forzatamente contrassegna il documento come fallito invece di
  lasciarlo per sempre in "Queue".
- **Documenti bloccati e falsi errori.** Le organizzazioni che caricano
  documenti in continuo vedevano i propri documenti retrocessi a una priorità
  di coda che non veniva mai servita durante l'orario di lavoro (866 documenti
  fermi in "new" presso un cliente). Un processo periodico dei nuovi tentativi
  poteva sovrascrivere con "error" un documento esportato con successo ore
  dopo e inviare per esso la mail di errore di esportazione. Questo percorso è
  stato chiuso.
- **Touchless Intelligence.** La scheda Analytics che misura quanti documenti
  attraversano DocBits senza intervento umano riceve la sua prima release
  completa: cluster di problemi con consigli AI, analisi in blocco, proposte
  di modifica con anteprima, applicazione e annullamento, una diagnosi AI per
  fornitore e un diagramma del flusso della pipeline per documento.
- **Più veloce dove i dati sono grandi.** Il menu a tendina della contabilità
  funziona per le organizzazioni con più di 2.000 conti, la pagina delle
  regole E-Documents pagina le sue 1.600 regole sul server invece di bloccare
  il browser, e Aggiorna nella dashboard degli ordini di acquisto restituisce
  dati freschi invece di un elenco in cache.
- **Sicurezza.** Le source map del frontend non vengono più distribuite a ogni
  deploy, i filtri di ricerca dei dati master vengono passati come parametri
  SQL invece di essere interpolati, un token scaduto viene rifiutato anche in
  caso di cache hit, e il controllo dell'organizzazione sul token di
  elaborazione viene applicato indipendentemente dal livello che lo precede.

---

## Web App — `10.66.3`

### Accesso e account

- L'overlay "Updating DocBits v10.59.3.1 → v10.59.3.1" che su sandbox si
  ricaricava all'infinito è stato corretto. Un ricaricamento sulla stessa
  versione non mostra più l'overlay, il ciclo è limitato per scheda, e un
  banner offre un ripristino manuale se dovesse ripetersi.
- La casella System Admin può essere spuntata su un utente esistente. Creare
  un amministratore di sistema dal frontend ora ha effetto; un job di
  sincronizzazione reimpostava il flag a ogni esecuzione.

### Dashboard e ricerca

- Nuove regole per gli operatori, descritte anche nel popup di aiuto della
  ricerca: `=` è esattamente questo valore (senza distinzione tra maiuscole e
  minuscole), `:` è "contiene", `: value*` "inizia con", `: *value` "termina
  con", `!=` è tutto ciò che non è esattamente questo valore, documenti senza
  valore inclusi. Le virgolette servono solo a raggruppare un valore con
  spazi.
- Una frase tra virgolette come `"Johnson and Johnson"` viene cercata come
  un'unica frase. "and" e "or" tra virgolette non vengono più letti come
  connettori.
- Quando una ricerca semplice non trova nulla, la dashboard spiega la regola e
  offre chip con un clic (`Invoice number : <term>`, `Purchase order : <term>`,
  `Supplier ID : <term>`).
- Una ricerca con zero risultati azzera il paginatore. Prima la paginazione
  conservava il conteggio della ricerca precedente.
- I numeri di richiesta d'acquisto e i richiedenti vengono trovati con una
  ricerca semplice, senza chip.

### Schermata di validazione

- I valori sostituiti dai dati master sono contrassegnati. Un badge color
  ambra mostra il valore originale e quello attuale, il dataset e il modo in
  cui ha trovato corrispondenza, e un pulsante ripristina il valore estratto.
  I valori confermati dai dati master o compilati dall'ordine di acquisto
  ricevono etichette proprie. Prima tutti portavano il badge "Extracted using
  saved rules".
- Il timbro di approvazione viene salvato anche quando la pagina contiene già
  un'altra annotazione. In quel caso i documenti annotati scaricati erano
  privi del timbro.
- "Nascondi colonne non mappate" conserva le colonne che avete addestrato
  manualmente (ad esempio Numero articolo e Ordine di acquisto).
- Il salvataggio delle regole di estrazione funziona dopo aver digitato un
  numero di pagina e poi disegnato un riquadro per un campo. Quella sequenza
  faceva andare in crash il salvataggio.
- Train Model viene eseguito in background. La schermata mostra "training
  started", interroga periodicamente il risultato e segnala successo o
  fallimento. Le organizzazioni grandi ricevevano un errore del gateway mentre
  l'addestramento proseguiva lato server.
- Modalità scura: il cursore a forbice nella schermata di suddivisione e
  l'interruttore di modalità nella schermata Auto Accounting sono di nuovo
  leggibili.

### Corrispondenza degli ordini di acquisto

Le modifiche annunciate in [Hotfixes 8 settembre 2026](incremental-updates-8-september-2026.md)
raggiungono la produzione con questa release: la corrispondenza sopravvive al
salvataggio, la corrispondenza viene eseguita di nuovo quando il numero
dell'ordine di acquisto viene corretto, lo schermo indica perché non c'è
corrispondenza e perché una corrispondenza non è stata mantenuta, la
cronologia della corrispondenza mostra le regole di trasformazione, e il
prezzo unitario PO viene calcolato dall'importo netto. Inoltre:

- Il pulsante Auto Match esporta anche il documento quando "PO Auto Match and
  Export" è attivo. Prima l'esportazione avveniva solo quando il documento
  veniva aperto dalla dashboard tramite "PO Match".
- Il popup della tolleranza su quantità/prezzo unitario resta aperto quando il
  server rifiuta il salvataggio, così i valori inseriti non vanno persi.
- Il pulsante Aggiorna della dashboard degli ordini di acquisto svuota la
  cache lato server prima di ricaricare. Un ordine di acquisto importato
  dall'ERP compariva solo dopo sette-otto minuti.

### Contabilità automatica

- Le organizzazioni con più di 2.000 conti cercano nell'elenco dei conti sul
  server. Per queste organizzazioni il menu a tendina era vuoto su sandbox, e
  il caricamento della pagina richiedeva cinque secondi.
- I conti a cui un documento fa riferimento vengono risolti in batch: un
  documento di 100 righe con due suddivisioni per riga ha bisogno di 4
  richieste invece di 403.
- Le intestazioni delle tabelle Auto Accounting e PO seguono l'etichetta
  impostata nel layout builder invece di un testo fisso.

### Impostazioni

- Impostazioni → E-Documents → Regole pagina, cerca e ordina il catalogo di
  1.600 regole sul server. La scheda prima renderizzava tutte le regole in una
  volta e bloccava il browser. "Reset all" è una sola chiamata invece di una
  per regola.
- Le Impostazioni avanzate del tipo di documento mostrano lo stato memorizzato
  di ogni interruttore. Un `false` salvato, una tolleranza `0` o un menu a
  tendina vuoto venivano sostituiti dal valore predefinito, e cambiando tipo
  di documento restavano i valori del tipo precedente.
- Regole di trasformazione: un'azione "Set value" viene salvata. L'editor la
  inviava con un nome che il server rifiuta.
- Il link ai sottotipi di documento è visibile sui tipi di documento standard.
- La mappatura JPL dell'esportazione SMB viene scaricata come `.properties`,
  così il file può essere caricato di nuovo. Era denominato `.xml` e veniva
  rifiutato al ricaricamento.

### Workflow

- Rinominare un workflow conserva le modifiche alle card fatte nella stessa
  sessione. I nuovi workflow vengono creati con un'unica richiesta di
  salvataggio, e le rinomine dei template vengono persistite.
- Un file di workflow esportato contiene l'intera struttura di esportazione
  (versione, nome, descrizione). I workflow avanzati possono essere importati
  di nuovo; prima il file perdeva la versione, veniva riletto come workflow
  standard e rifiutato.
- I filtri di colonna nell'elenco dei workflow si combinano con AND. Con un
  filtro per nome e uno per data attivi, finivano nel risultato anche righe
  che corrispondevano solo al nome.
- Le scadenze delle attività usano il formato data delle vostre impostazioni
  utente nell'elenco, nella board e nella vista di dettaglio.

### Analytics: Touchless Intelligence

La scheda Touchless (Analytics → Touchless) misura quanti documenti
attraversano DocBits senza che una persona li tocchi, e perché gli altri non
ci sono riusciti. Questa release la completa:

- **Cluster di problemi con evidenze.** I documenti che hanno richiesto un
  intervento vengono raggruppati per causa. Ogni scheda di cluster nomina i
  campi, i codici di validazione e i messaggi di errore su cui fallisce, e il
  suo fornitore, oppure dichiara che non ce n'è uno. I cluster che DocBits può
  correggere (una regola, un'impostazione di campo) sono separati da quelli
  che solo il fornitore può correggere, e il budget di analisi AI va per primi
  a quelli correggibili.
- **Analisi AI, dichiarata come tale.** Una scheda di cluster dice se il
  consiglio è stato scritto da un modello linguistico o da una regola, cosa ha
  conteggiato l'analisi e da quando ha smesso di essere valida, e se un clic
  riutilizzerà un'analisi in cache. Se l'advisor AI non può essere eseguito in
  questo ambiente, la scheda ne spiega il motivo.
- **Analisi in blocco.** Analizzate molti cluster in un'unica esecuzione,
  seguite cluster per cluster cosa sta facendo l'esecuzione e ritrovate i
  risultati in seguito. L'elenco dei risultati sopravvive alla navigazione e
  al ricaricamento, e l'esecuzione non resta più bloccata su "Running · 0/6
  done" nella vista di una sotto-organizzazione.
- **Proposte di modifica.** Una raccomandazione diventa qualcosa su cui potete
  agire: una proposta che punta al campo che blocca i documenti, un'anteprima
  che mostra cosa farebbe (nulla viene salvato), l'applicazione, l'effetto
  misurato e l'annullamento. Gli agenti raggiungono gli stessi passaggi
  tramite strumenti MCP. I passaggi di correzione rimandano direttamente alla
  pagina delle impostazioni che nominano, già filtrata per tipo di documento,
  campo o regola.
- **Diagnosi del fornitore.** La pagina del fornitore spiega uno stato vuoto
  invece di mostrare zeri, e offre una diagnosi AI per fornitore. È possibile
  selezionare fino a cinque fornitori e confrontarli fianco a fianco.
- **Flusso della pipeline.** Un diagramma per documento e per cluster mostra
  il percorso attraverso acquisizione, classificazione, verifica e-document,
  fornitore, OCR, estrazione, validazione, corrispondenza PO, approvazione ed
  esportazione, con la fase che lo ha fermato.
- **Motivi della corrispondenza degli ordini di acquisto.** La decisione di
  corrispondenza viene tracciata per documento (fase, passaggio, regola,
  colonna) e condensata nel risultato Touchless. I codici motivo distinguono
  "ordine di acquisto non trovato" da "righe non corrispondenti" e "campo
  obbligatorio mancante", e le proposte di tolleranza dell'advisor puntano al
  motore di regole che decide.
- **Numeri corretti.** I riquadri KPI rispettano il filtro per
  sotto-organizzazione e contano solo i documenti che il dettaglio può
  elencare.

### DocNet

- Il feed delle attività, il widget Recent Activity e la timeline delle
  missioni sono tradotti. I riepiloghi di audit erano in inglese in tutte le
  22 lingue.
- Gli agenti vedono i campi che il tipo di documento definisce ma che
  l'estrazione ha lasciato vuoti. Prima concludevano che tali campi non
  esistessero e saltavano gli aggiornamenti obbligatori senza tentare una
  scrittura.

### Sicurezza

- Le source map del frontend vengono rimosse da ogni deploy. Tutti gli
  ambienti le servivano, produzione inclusa.

---

## API Service — `12.83.156`

### Riconoscimento dei fornitori e dati master

- Un fornitore viene identificato quando un campo di ricerca è univoco. Con
  più campi ricercabili, i risultati venivano combinati come unione, così una
  corrispondenza generica sul nome con quattro fornitori sommergeva un
  identificativo fiscale che ne trovava esattamente uno. I campi che non
  trovano nulla non bloccano più quelli che hanno trovato. Vedere
  [Impostazioni dei dati master](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md)
  per come i campi lavorano insieme.
- Le sostituzioni dai dati master vengono registrate con la loro origine:
  dataset, configurazione, campo sorgente, operatore e tipo di corrispondenza.
  La schermata di validazione lo mostra e può ripristinare il valore estratto.
- Cash Discount Term viene importato dal BOD del fornitore; i fornitori
  sincronizzati dall'ERP lo avevano vuoto. Un Discount Term Overwrite inserito
  come codice completo ("143", "012", "X08") viene applicato; prima veniva
  consultato solo il prefisso percentuale.
- Le ricerche nei dati master sono limitate a 1.000 righe per pagina e il
  pivot avviene in SQL. Una ricerca su 19.000 record richiedeva cinque secondi
  per chiamata e bloccava l'API.
- I nomi delle proprietà di filtro e i tipi di dati nella ricerca dei dati
  master vengono passati come parametri SQL. Venivano interpolati nella query.

### Elaborazione dei documenti

- I documenti di un'organizzazione che carica in continuo venivano retrocessi
  a priorità 9, che la coda serve solo quando ogni priorità superiore è vuota.
  La retrocessione è ora limitata a 3. Il riconciliatore che dovrebbe
  rimettere in coda i documenti bloccati non aveva credenziali funzionanti in
  produzione; ora le ha.
- Un documento concluso ed esportato non viene mai sovrascritto con "error".
  Un flag di workflow mai azzerato faceva sì che il processo dei nuovi
  tentativi riprendesse un documento esportato con successo una volta al
  minuto, finché il limite di tentativi lo marcava come "error" e inviava la
  mail di errore di esportazione al cliente, 2 h e 17 min dopo l'esportazione.
- Unione e aggiunta accettano file `.PDF` e `.Pdf`. L'output dello scanner
  denominato `SCAN0001.PDF` veniva rifiutato con "Only PDF files are allowed."
- L'invalidazione della cache scansiona lo spazio delle chiavi una volta
  invece di due e svuota solo i tipi di dati di ricerca che un BOD ha
  modificato. Prima ogni BOD cancellava l'intera cache di ricerca
  dell'organizzazione, bloccando l'API mentre percorreva le chiavi di tutti.
- Il riaddestramento del modello viene eseguito come attività in background e
  restituisce subito uno stato che l'interfaccia interroga periodicamente.
- Un token di elaborazione di un'altra organizzazione viene rifiutato
  indipendentemente dal controllo di appartenenza alla sotto-organizzazione
  che lo precede.
- La sincronizzazione degli utenti lascia invariato il flag di utente di
  sistema invece di reimpostarlo a ogni esecuzione.

### Esportazione

- Le righe di ricezione M3 abbinano il prezzo unitario esportato alla base di
  prezzo della riga di fattura stessa. Il prezzo viaggiava con il divisore
  della riga dell'ordine di acquisto e l'ERP riprezzava la riga a 1.000 volte
  l'importo fatturato.
- Un'esportazione di tabella sopravvive a una riga il cui ordine di acquisto è
  stato rimosso; la riga viene esportata senza base di prezzo.

### E-document

- Le fatture XRechnung CII il cui importo dovuto è 0,00 perché un importo
  prepagato compensa il totale mostrano il totale complessivo (BT-112) come
  importo totale. Il cliente vedeva "total amount 0,00".
- I documenti XRechnung CII e Facturae restituiscono di nuovo i campi del
  fornitore. Override obsoleti a livello di organizzazione mascheravano la
  mappatura predefinita corretta, così il riconoscimento del fornitore non
  poteva mai trovare corrispondenza.
- Il catalogo delle regole di validazione viene paginato, cercato e ordinato
  sul server, con faccette per la barra dei filtri.

### Classificazione

- I documenti svizzeri vengono classificati `de_CH`, `fr_CH` o `it_CH` in base
  al contenuto (importi in CHF, partite IVA CHE, IBAN CH). Il locale veniva
  preso dal valore predefinito dell'organizzazione e i documenti svizzeri
  ricevevano `de_DE`.

### Ricerca nella dashboard

- Un'unica semantica degli operatori su Postgres e ClickHouse: `=` esatto, `:`
  contiene con caratteri jolly ai bordi, `!=` complemento, valori vuoti
  inclusi. Su Postgres `=` era una corrispondenza per prefisso, così
  `invoice_id=911892112` restituiva anche 911892112333.
- Una ricerca semplice è una ricerca per sottostringa su tutti i campi,
  identificativi aziendali inclusi. Un identificativo con trattino come
  `2026-003` è un unico letterale, e il tipo di clausola non cambia più dopo
  il quinto carattere.
- Il chip del numero di fattura è esatto su Postgres, come lo era già
  sull'indice. Zeri iniziali, forme decimali e maiuscole/minuscole vengono
  trattati allo stesso modo nel testo libero e nei chip.
- La ricerca WebSocket della dashboard trasmette la credenziale del chiamante
  al servizio full-text. Prima ogni delega veniva rifiutata, così la dashboard
  cercava silenziosamente solo su Postgres e presentava la risposta come
  completa.
- Il conteggio dei risultati e l'elenco dei risultati usano un unico insieme
  di predicati. Il conteggio era un'approssimazione di Postgres mentre
  l'elenco proveniva dall'indice.
- La ricerca vettoriale si ferma alla finestra reale dei risultati e segnala
  il limite invece di mostrare "(50)" come totale esatto.
- Una ricerca eseguita senza l'indice full-text (indice in ritardo di minuti,
  ricerca delle capacità fallita, risoluzione dei campi degradata) segnala lo
  stato della propria finestra invece di "completa".
- Gli script dei documenti che chiamano la ricerca full-text si autenticano
  correttamente e mostrano gli errori invece di restituire un risultato vuoto.

### Corrispondenza degli ordini di acquisto (matcher in-process)

Per le organizzazioni che eseguono la corrispondenza nell'API invece che nel
PO Match Service: un numero di ordine di acquisto corretto viene abbinato
nello stesso salvataggio che lo corregge.

### Analytics

- Touchless: tutte le modifiche backend dietro la sezione Web App qui sopra,
  incluse le evidenze di fase registrate da ogni fase della pipeline, la
  traccia della corrispondenza PO, le proposte di modifica con anteprima,
  applicazione e ripristino, e lo stato delle analisi in blocco in un'unica
  chiamata per ciclo.

---

## PO Match Service — `1.59.34`

- Il prezzo unitario di una riga PO viene derivato dal suo importo netto, non
  dal totale con imposte, e lo snapshot PO di un documento ricalcola i propri
  prezzi unitari al momento della corrispondenza.
- Il servizio registra da dove proviene ogni candidato numero PO e quali
  numeri un'esecuzione ha cercato. Il numero di fattura stesso di un documento
  non è mai un candidato PO. Una corrispondenza scartata lascia la propria
  motivazione sul documento per lo schermo.
- La corrispondenza manuale funziona per le organizzazioni le cui regole non
  hanno il flag `is_fallback`. Gli utenti selezionavano le righe, premevano
  match, e non tornava nulla.
- Niente più documenti orfani in "Queue": i timeout delle istruzioni di
  database, i keepalive e un gestore esplicito del soft time limit
  contrassegnano l'attività come fallita invece di affidarsi a
  un'interruzione forzata che non lasciava traccia.
- Le modifiche alle tolleranze vengono lette a ogni richiesta di
  corrispondenza, così una tolleranza salvata un attimo fa viene usata dalla
  corrispondenza successiva.
- La traccia decisionale in cinque fasi viene persistita per documento per
  Touchless.

---

## Auth Service — `1.78.27`

- La scadenza del token viene applicata anche in caso di cache hit. Una voce
  in cache poteva autenticare fino a nove ore dopo la scadenza del token.
- La verifica del token non scrive più un `org_id` invariato sulla riga
  dell'utente a ogni richiesta, cosa che produceva un UPDATE per chiamata.
- È stata corretta una perdita di memoria che portava l'autoscaler al massimo
  numero di repliche, e il servizio è tornato a due worker.
- Il flag di utente di sistema può essere modificato su un utente esistente
  quando nessun altro membro lo detiene.

---

## Auth Bridge Service — `0.5.7`

- Quando il flusso di replica UE ↔ USA si interrompe, lo slot di replica viene
  riagganciato sul posto invece di ricostruire il bridge e rieseguire l'intera
  riconciliazione di avvio, durante la quale lo slot restava inattivo.

---

## Extraction Service — `1.55.33`

- Estrazione tabelle AI: le colonne importo sono tipizzate come numeri con una
  descrizione, e i valori non numerici inventati nelle colonne importo (uno
  "St." copiato dalla cella adiacente in unit price per) vengono scartati
  invece di essere memorizzati.
- Fatture USA: il rumore in virgola mobile inferiore al centesimo non decide
  più tra coppie candidate netto/imposta (268.28 + 22.13 perdeva contro
  netto = totale, imposta = 0).

---

## Fulltext Service — `1.42.35`

- La cache dei risultati di ricerca è attiva in ogni ambiente; produzione,
  sandbox e stage ne erano privi da quando sono stati creati i file env
  attivi. Caricamento ed eliminazione la invalidano, così una ricerca dopo un
  caricamento vede il nuovo documento.
- Una ricerca semplice per un numero di fattura restituisce la fattura con
  corrispondenza esatta. I valori di valuta scritti in lettere, le mappature
  booleane legacy, le date e i flag fiscali sopravvivono alla ricostruzione
  dell'indice snello, e le voci di indice senza campi vengono rilevate e
  recuperate dall'estrazione.
- L'operatore esatto `=` su un campo di testo dinamico confronta solo il
  valore intero. Un carattere jolly sul percorso analizzato faceva sì che
  `note_field=53173` corrispondesse a "PO 53173 / 2024".
- Un identificativo con trattino come `2026-003` è un unico letterale, non un
  insieme di token.
- I percorsi di lettura non creano più l'indice che leggono, e ogni risposta
  con zero risultati riporta uno stato di finestra e un motivo.
- Il limite lato servizio di 50 della ricerca vettoriale è stato rimosso.

---

## Docflow Service — `2.10.11`

- Le importazioni di workflow avanzati sono vincolate ai diritti
  dell'organizzazione, e un batch viene verificato prima che venga scritto
  qualcosa. Un'organizzazione senza il modulo avanzato poteva importare un
  workflow avanzato che poi non aveva modo di aprire.
- La rinomina di un workflow viaggia con il salvataggio, e le rinomine dei
  template vengono persistite.

---

## Docnet Service — `1.56.12`

- La scoperta dei campi restituisce ogni campo di intestazione definito dal
  layout, compilato o meno, e coincide con ciò che il controllo di scrittura
  verifica. Gli agenti saltavano aggiornamenti obbligatori dei campi perché i
  campi vuoti sembravano assenti.
- Le identità vengono memorizzate in cache sotto la stessa chiave con ambito
  di organizzazione usata dall'API, così il confine delle API key per
  organizzazione regge in entrambi i servizi.

---

## Email Service — `1.41.6`

- Le caselle di posta condivise di Office 365 con più di dieci sottocartelle
  risolvono ogni cartella. Microsoft Graph restituisce le cartelle a pagine di
  dieci; dall'undicesima configurazione in poi ogni polling falliva con
  "unable to find the selected Folder".

---

## FTP Service — `1.32.18`

- Lo scheduler SFTP si avvia in ciascun processo worker invece che prima del
  fork. Le importazioni SFTP periodiche fallivano silenziosamente con uno
  stato dello scheduler corrotto, mentre un processo nuovo funzionava.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Solo modifiche di build e distribuzione (aggiornamento dell'immagine base,
credenziali CI). Nessun cambiamento nel comportamento.

<!-- Release R1.0.13. Announced: tickets with Jira "Release No." = R1.0.13 and a
     status on sandbox or beyond, plus DOCB-14454, DOCB-14450, DOCB-14415,
     DOCB-14419, DOCB-14431, DOCB-14045/46 (no Release No., on sandbox).
     Held back (Release No. R1.1): DRFS-778, DRFS-712, MEF-165, MEF-166, DOCB-14389.
     Labelled R1.0.12 but code ships now: DRFS-746/748/749/750/751, DOCB-14282. -->
