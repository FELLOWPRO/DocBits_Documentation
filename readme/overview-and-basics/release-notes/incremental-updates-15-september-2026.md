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
  tutti i campi, numeri di ordine di acquisto, codici a barre e numeri di
  richiesta d'acquisto inclusi. Il conteggio dei risultati, i riquadri di
  stato e la paginazione descrivono lo stesso insieme di documenti, e una
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
  Lo schermo indica perché non c'è corrispondenza, il tooltip di mancata
  corrispondenza nomina la colonna che non ha superato il confronto, la
  cronologia della corrispondenza elenca le regole di trasformazione eseguite,
  e i prezzi unitari PO vengono derivati dall'importo netto. Le corrispondenze
  manuali funzionano di nuovo per le organizzazioni senza regola di fallback,
  gli ordini di acquisto rimossi restano rimossi, e un'attività di
  corrispondenza terminata forzatamente contrassegna il documento come fallito
  invece di lasciarlo per sempre in "Queue".
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
  di modifica con anteprima, applicazione e annullamento, una pagina del
  fornitore con andamento ed esempi, un diagramma del flusso della pipeline
  per documento, e un diagramma dell'insieme di regole degli ordini di
  acquisto che spiega perché un documento non è passato.
- **Più veloce dove i dati sono grandi.** Gli accessi a freddo saltano la
  somma del registro crediti che richiedeva fino a 33 s, il menu a tendina
  della contabilità funziona per le organizzazioni con più di 2.000 conti, la
  pagina delle regole E-Documents pagina le sue 1.600 regole sul server invece
  di bloccare il browser, e Aggiorna nella dashboard degli ordini di acquisto
  restituisce dati freschi invece di un elenco in cache.
- **Sicurezza.** Le source map del frontend non vengono più distribuite a ogni
  deploy, i filtri di ricerca dei dati master vengono passati come parametri
  SQL invece di essere interpolati, un token scaduto viene rifiutato anche in
  caso di cache hit, e il controllo dell'organizzazione sul token di
  elaborazione viene applicato indipendentemente dal livello che lo precede.

---

## Web App — `10.66.3`

### Accesso e account

- L'accesso è più veloce. Il controllo dell'abbonamento all'accesso richiedeva
  il saldo crediti completo, che sommava milioni di righe del registro e
  spesso superava il timeout di 10 s del client. L'accesso ora chiede solo se
  esiste un abbonamento; i saldi vengono ancora calcolati in Impostazioni →
  Abbonamento.
- Il cambio di regione (UE ↔ USA) mantiene l'accesso. La regione di
  destinazione risponde "invalid token" per alcuni secondi finché la sessione
  non è stata replicata, e due percorsi di codice lo interpretavano come una
  sessione scaduta.
- L'overlay "Updating DocBits v10.59.3.1 → v10.59.3.1" che su sandbox si
  ricaricava all'infinito è stato corretto. Un ricaricamento sulla stessa
  versione non mostra più l'overlay, il ciclo è limitato per scheda, e un
  banner offre un ripristino manuale se dovesse ripetersi.
- Gli amministratori possono concedere la scheda Analytics Dashboard a ruoli
  specifici, e le modifiche ai ruoli vengono salvate in modo affidabile.
- La casella System Admin può essere spuntata su un utente esistente. Creare
  un amministratore di sistema dal frontend ora ha effetto; un job di
  sincronizzazione reimpostava il flag a ogni esecuzione.
- Impostazioni → Ruoli: l'elenco dei membri viene visualizzato invece di
  restare bloccato dietro un indicatore di caricamento quando il server
  risponde con un errore.
- L'accesso al server MCP di DocBits applica l'autenticazione a due fattori e
  il consenso monouso.

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
- Una ricerca con zero risultati azzera il paginatore e ogni conteggio della
  pagina. Prima la paginazione conservava il conteggio della ricerca
  precedente.
- I numeri di ordine di acquisto, i numeri d'ordine, i codici a barre, i tipi
  di fattura e i numeri di richiesta d'acquisto possono essere trovati senza
  chip.

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
- L'estrazione strutturata può essere attivata per fornitore, nel popup tfidf
  della schermata di validazione e come colonna di sola lettura in
  Impostazioni → Classificazione ed Estrazione.
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

- Il tooltip di mancata corrispondenza nomina la colonna che non ha trovato
  corrispondenza. Prima era vuoto perché venivano registrate solo le colonne
  corrispondenti, e lo schermo poteva dire solo "Mismatched".
- Il pulsante Auto Match esporta anche il documento quando "PO Auto Match and
  Export" è attivo. Prima l'esportazione avveniva solo quando il documento
  veniva aperto dalla dashboard tramite "PO Match".
- Il popup della tolleranza su quantità/prezzo unitario resta aperto quando il
  server rifiuta il salvataggio, così i valori inseriti non vanno persi.
- Il pulsante Aggiorna della dashboard degli ordini di acquisto svuota la
  cache lato server prima di ricaricare. Un ordine di acquisto importato
  dall'ERP compariva solo dopo sette-otto minuti.
- La pagina delle regole di corrispondenza PO disegna l'insieme di regole come
  diagramma di flusso, e la cronologia della corrispondenza si è spostata
  nella barra degli strumenti delle azioni.

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
- Elenco di Valori: la barra laterale mostra un nuovo elenco e rimuove uno
  eliminato senza ricaricare; le risposte in ritardo di un elenco precedente
  non sovrascrivono più quello corrente.
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
  agire: la scheda spiega la modifica proposta in quattro domande, vi permette
  di adattarla, mostra in anteprima cosa farebbe (nulla viene salvato), la
  applica, ne misura l'effetto e può annullarla. I passaggi di correzione
  rimandano direttamente alla pagina delle impostazioni che nominano, già
  filtrata per tipo di documento, campo o regola.
- **Pagina del fornitore.** Scegliete un fornitore dalla scheda o cercate
  nella coda delle opportunità per nome o numero. La pagina mostra il tasso
  touchless del fornitore nel tempo (da 30 giorni a 1 anno), i suoi documenti
  problematici e i documenti andati a buon fine, e offre una diagnosi AI per
  fornitore. È possibile confrontare fino a cinque fornitori fianco a fianco.
  Viene mostrato il numero del fornitore invece di un hash interno.
- **Flusso della pipeline.** Un diagramma per documento e per cluster mostra
  il percorso attraverso acquisizione, classificazione, verifica e-document,
  fornitore, OCR, estrazione, validazione, corrispondenza PO, approvazione ed
  esportazione, con la fase che lo ha fermato.
- **Corrispondenza degli ordini di acquisto, spiegata.** L'insieme di regole
  PO viene disegnato come diagramma di flusso nella pagina delle impostazioni
  e in Touchless, con il percorso seguito da un documento e una spiegazione in
  linguaggio semplice del perché non è passato. I codici motivo distinguono
  "ordine di acquisto non trovato" da "righe non corrispondenti" e "campo
  obbligatorio mancante".
- **Segmentazione.** KPI, cluster e proposte possono essere suddivisi per un
  campo del documento, ad esempio Order Type = Direct / Indirect.
- **Numeri corretti.** I riquadri KPI rispettano il filtro per
  sotto-organizzazione e contano solo i documenti che il dettaglio può
  elencare. Una sessione browser dell'utente di sistema dell'organizzazione
  conta come intervento umano, così i documenti corretti a mano non vengono
  più classificati come touchless.
- La barra degli strumenti del report contiene tutti i propri controlli sugli
  schermi larghi, e i colori della modalità scura provengono dal tema.

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
- Esportazione IDM: un campo multivalore mappato su un campo numerico (ad
  esempio una quantità) faceva andare in crash il payload di esportazione. Il
  valore viene prima convertito in testo.

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
  identificativi aziendali inclusi. Ordine di acquisto, numero d'ordine,
  codice a barre, tipo di fattura, sottotipo di fattura e numero di richiesta
  d'acquisto non avevano alcun ramo di ricerca a testo libero.
- Il chip del numero di fattura è esatto su Postgres, come lo era già
  sull'indice. Zeri iniziali, forme decimali e maiuscole/minuscole vengono
  trattati allo stesso modo nel testo libero e nei chip.
- La ricerca WebSocket della dashboard trasmette la credenziale del chiamante
  al servizio full-text. Prima ogni delega veniva rifiutata, così la dashboard
  cercava silenziosamente solo su Postgres e presentava la risposta come
  completa.
- I riquadri di stato, il conteggio dei risultati e l'elenco dei risultati
  usano un unico insieme di predicati. Durante qualsiasi ricerca i riquadri
  descrivevano l'intera organizzazione.
- I permessi per sotto-organizzazione e tipo di documento vengono applicati
  prima della finestra dei risultati, così i documenti consentiti non escono
  più dal limite di 500 / 10.000.
- La ricerca vettoriale si ferma alla finestra reale dei risultati e segnala
  il limite invece di mostrare "(50)" come totale esatto.
- Una ricerca eseguita senza l'indice full-text (indice mancante, indice in
  ritardo di minuti, ricerca delle capacità fallita, risoluzione dei campi
  degradata) segnala lo stato della propria finestra invece di "completa".
- Le esportazioni della dashboard di una ricerca troncata contengono una riga
  di avviso nel CSV/XLSX e nella mail di notifica.
- Gli script dei documenti che chiamano la ricerca full-text si autenticano
  correttamente e mostrano gli errori invece di restituire un risultato vuoto.

### Corrispondenza degli ordini di acquisto (matcher in-process)

Per le organizzazioni che eseguono la corrispondenza nell'API invece che nel
PO Match Service:

- Ogni confronto di colonna viene registrato, prezzo unitario e quantità
  inclusi, così il tooltip di mancata corrispondenza può nominare la colonna
  che non ha superato il confronto.
- Gli ordini di acquisto rimossi dall'utente restano rimossi nella
  corrispondenza automatica.
- Un numero di ordine di acquisto corretto viene abbinato nello stesso
  salvataggio che lo corregge.

### Analytics

- Touchless: tutte le modifiche backend dietro la sezione Web App qui sopra,
  incluse le evidenze di fase registrate da ogni fase della pipeline, la
  traccia della corrispondenza PO, le proposte di modifica con anteprima,
  applicazione e ripristino, la segmentazione, lo stato delle analisi in
  blocco in un'unica chiamata per ciclo, e l'endpoint dell'andamento che
  accetta qualsiasi finestra temporale e un fornitore.
- Tre attività in background di Analytics che fallivano a ogni esecuzione
  pianificata sono state corrette.

---

## PO Match Service — `1.59.34`

- Il prezzo unitario di una riga PO viene derivato dal suo importo netto, non
  dal totale con imposte, e lo snapshot PO di un documento ricalcola i propri
  prezzi unitari al momento della corrispondenza.
- Il servizio registra da dove proviene ogni candidato numero PO e quali
  numeri un'esecuzione ha cercato. Il numero di fattura stesso di un documento
  non è mai un candidato PO. Una corrispondenza scartata lascia la propria
  motivazione sul documento per lo schermo.
- La colonna che non ha trovato corrispondenza viene registrata, e le colonne
  rimosse da una regola di fallback vengono misurate.
- Gli ordini di acquisto rimossi dall'utente vengono rispettati, e le
  corrispondenze in background obsolete vengono azzerate dopo l'esclusione
  finale.
- La corrispondenza manuale funziona per le organizzazioni le cui regole non
  hanno il flag `is_fallback`. Gli utenti selezionavano le righe, premevano
  match, e non tornava nulla.
- Niente più documenti orfani in "Queue": i timeout delle istruzioni di
  database, i keepalive e un gestore esplicito del soft time limit
  contrassegnano l'attività come fallita invece di affidarsi a
  un'interruzione forzata che non lasciava traccia.
- Due errori di produzione (un prezzo unitario `NaN`, un gruppo senza
  quantità) non fanno più fallire l'intera corrispondenza.
- Le modifiche alle tolleranze vengono lette a ogni richiesta di
  corrispondenza, così una tolleranza salvata un attimo fa viene usata dalla
  corrispondenza successiva.
- La traccia decisionale in cinque fasi viene persistita per documento per
  Touchless.

---

## Auth Service — `1.78.27`

- `/organisation/subscriptions` può saltare il saldo crediti, e il calcolo dei
  crediti esegue tutte le finestre dell'anno contrattuale in un'unica
  istruzione invece di una query per finestra (32 query da circa 700 ms
  ciascuna per l'organizzazione più grande). Un rollup giornaliero
  dell'utilizzo è predisposto per usi futuri.
- I valori dei token rimanenti nei lettori dell'organizzazione vengono
  calcolati per anno contrattuale.
- La scadenza del token viene applicata anche in caso di cache hit. Una voce
  in cache poteva autenticare fino a nove ore dopo la scadenza del token.
- La verifica del token non scrive più un `org_id` invariato sulla riga
  dell'utente a ogni richiesta, cosa che produceva un UPDATE per chiamata.
- I controlli di integrità saltano l'I/O di Redis, e il client Redis usa un
  pool di connessioni. È stata corretta una perdita di memoria che portava
  l'autoscaler al massimo numero di repliche, e il servizio è tornato a due
  worker.
- Una registrazione fornitore ripetuta (magic link aperto due volte)
  riutilizza l'appartenenza esistente invece di fallire con un errore di
  chiave duplicata.
- Il thread della mail di reimpostazione password usa l'unica app Flask
  registrata; la reimpostazione falliva con "current Flask app is not
  registered" dal 25 agosto.
- Il flag di utente di sistema può essere modificato su un utente esistente
  quando nessun altro membro lo detiene.
- Accesso MCP: MFA vincolata alla transazione, consenso monouso, e scelta
  forzata dell'account quando il browser contiene due identità di sessione.

---

## Auth Bridge Service — `0.5.7`

Replica dell'autenticazione UE ↔ USA:

- La riconciliazione periodica mantiene attivo il flusso di replica.
  Richiedeva circa 95 s mentre il timeout del mittente era di 60 s, così ogni
  riconciliazione a cadenza di sei ore interrompeva puntualmente il flusso.
- Quando il flusso si interrompe, lo slot di replica viene riagganciato sul
  posto invece di ricostruire il bridge e rieseguire l'intera riconciliazione
  di avvio.
- La riconciliazione confronta le chiavi primarie a pagine invece di caricare
  entrambi i lati in memoria, cosa che non è più possibile da quando la
  tabella dei token fa parte della replica.
- Un'origine di replica esistente viene considerata un successo, non un
  degrado.

---

## Extraction Service — `1.55.33`

- L'estrazione strutturata viene risolta per fornitore: l'impostazione di un
  layout addestrato prevale sulla preferenza dell'organizzazione, come già
  avviene per il modello AI.
- Una mappatura di colonne appresa non può vietare colonne che la fattura ha.
- Estrazione tabelle AI: le colonne importo sono tipizzate come numeri con una
  descrizione, e i valori non numerici inventati nelle colonne importo (uno
  "St." copiato dalla cella adiacente in unit price per) vengono scartati
  invece di essere memorizzati.
- Fatture USA: quando l'importo netto è già uguale al totale, l'imposta viene
  risolta a 0 invece di conservare un'imposta estratta spuria. Il rumore in
  virgola mobile inferiore al centesimo non decide più tra coppie candidate
  netto/imposta (268.28 + 22.13 perdeva contro netto = totale, imposta = 0).
- Una tabella la cui riga di intestazione non è mai stata mappata su nomi
  reali viene estratta invece di fallire del tutto.

---

## Fulltext Service — `1.42.35`

- La cache dei risultati di ricerca è attiva in ogni ambiente; produzione,
  sandbox e stage ne erano privi da quando sono stati creati i file env
  attivi. Caricamento ed eliminazione la invalidano, così una ricerca dopo un
  caricamento vede il nuovo documento.
- L'operatore esatto `=` su un campo di testo dinamico confronta solo il
  valore intero. Un carattere jolly sul percorso analizzato faceva sì che
  `note_field=53173` corrispondesse a "PO 53173 / 2024".
- Un identificativo con trattino in una ricerca semplice come `2026-003` è un
  unico letterale, non un insieme di token.
- I numeri di ordine di acquisto vengono trovati in ogni forma di
  memorizzazione, inclusi gli identificativi composti solo da cifre la cui
  clausola esatta veniva scartata silenziosamente.
- I percorsi di lettura non creano più l'indice che leggono. Un indice
  mancante o vuoto rispondeva "completa, 0 risultati"; ogni risposta con zero
  risultati riporta ora uno stato di finestra e un motivo.
- I valori di valuta scritti in lettere, le mappature booleane legacy, le date
  e i flag fiscali sopravvivono alla ricostruzione dell'indice snello, e le
  voci di indice senza campi vengono rilevate e recuperate dall'estrazione.

---

## Docflow Service — `2.10.11`

- Le importazioni di workflow avanzati sono vincolate ai diritti
  dell'organizzazione, e un batch viene verificato prima che venga scritto
  qualcosa. Un'organizzazione senza il modulo avanzato poteva importare un
  workflow avanzato che poi non aveva modo di aprire.
- La rinomina di un workflow viaggia con il salvataggio, e le rinomine dei
  template vengono persistite.
- L'aggiornamento di "pending workflow execution" viene ritentato in caso di
  connessioni interrotte. Una singola richiesta fallita lasciava il flag
  invariato e teneva il documento fuori dall'esportazione finché qualcuno non
  lo riavviava.

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

<!-- Release R1.0.13. Everything in the prod->sandbox code delta is announced.
     Held back because Jira "Release No." names the later release R1.1:
     DRFS-778 (discount due dates on import), DRFS-712, MEF-165, MEF-166,
     DOCB-14389. Announce them with R1.1. -->
