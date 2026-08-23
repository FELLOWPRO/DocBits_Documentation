# Note della versione DocBits — 29 luglio – 12 agosto 2026

_Cosa è cambiato con l'aggiornamento di produzione di DocBits distribuito il
10–12 agosto 2026, che copre tutto quanto rilasciato dopo la release del
29 luglio. Per ogni servizio è indicata la versione andata in produzione,
seguita dalle novità e correzioni spiegate in linguaggio semplice. I servizi
non elencati (Auto Accounting `1.21.1`, Ideas `0.3.1`, OCR `1.10.3`, Operator
`1.42.1`, PO Match `1.59.3`, FTP `1.32.4`) non hanno avuto modifiche visibili
ai clienti._

---

## Highlights

- **Supporto FacturaE.** Le fatture elettroniche spagnole FacturaE 3.1 vengono
  classificate ed estratte senza alcuna configurazione, con mappature dei
  campi complete. Nella stessa ondata, le mappature ebInterface (Austria) sono
  diventate fedeli alla versione, i default di Factur-X e ZUGFeRD hanno
  ottenuto il percorso del nome dell'azienda e sono state corrette diverse
  mappature predefinite errate per sconti, IVA e prezzi unitari.
- **Ricerca e ordinamento della dashboard riparati.** L'ordinamento non
  dipende più da quali colonne risultino visibili, un filtro OR combinato con
  una condizione di intervallo o uguaglianza non cancella più le frasi di
  ricerca, i nomi dei fornitori compaiono di nuovo nella ricerca rapida e le
  date in formato ISO vengono lette correttamente.
- **L'estrazione AI si corregge da sola.** Uno scambio dimostrabile tra
  importo netto e totale operato dall'AI viene annullato automaticamente, i
  campi scansionati dall'AI non tornano più errati dopo il riavvio di un
  documento e l'estrazione tabelle AI elabora i documenti in batch di pagine,
  così le tabelle lunghe arrivano complete.
- **I workflow sopravvivono a un inciampo dell'autenticazione.** Un servizio
  di autenticazione momentaneamente irraggiungibile viene ritentato invece di
  far fallire l'esecuzione, e un trigger di workflow che non riesce ad
  autenticarsi segnala l'errore invece di lasciare il documento bloccato.
- **I PDF difficili da leggere tornano a essere estratti.** Quando il
  decodificatore standard del testo PDF non riesce a leggere una pagina
  (frequente con i file prodotti da Ghostscript), l'estrazione ricorre a un
  secondo motore invece di non restituire nulla.
- **L'MFA funziona tra le regioni.** I dati di registrazione
  dell'autenticazione a due fattori vengono replicati tra le regioni UE e
  USA, così un secondo fattore configurato in una regione viene riconosciuto
  nell'altra.

---

## Web App — `10.49.4`

### Accesso e account

- La disconnessione in una scheda del browser disconnette anche le altre
  schede, senza i toast di errore che comparivano quando le schede erano in
  disaccordo sulla sessione.
- La modifica della propria password nel profilo passa per l'endpoint
  self-service dedicato, così funziona senza permessi di amministratore.
- L'accesso con passkey dalla regione non principale mostra messaggi di
  errore tradotti, e il suo pulsante di invio è visibile.

### Schermata di validazione

- La scheda "Extracted table" non gira più all'infinito quando esiste già una
  tabella AI.
- I documenti privi di dati del codice a barre non mandano più in errore la
  vista di assegnazione dei codici a barre.
- Le righe multi-imposta M3 offrono il codice imposta come menu a tendina
  alimentato dall'elenco dei valori invece che come campo a testo libero.
- L'apertura di fatture fornitore di grandi dimensioni è sensibilmente più
  veloce.

### Attività

- Le colonne Kanban si paginano durante lo scorrimento, così le bacheche con
  molte attività si caricano rapidamente.
- Il contatore delle attività aperte nella barra laterale conta le attività
  nel contesto della vostra sotto-organizzazione, non nel contesto del
  documento che si trova aperto in quel momento.

### Workflow Builder

- L'elenco dei workflow conserva ricerca, ordinamento, pagina e dimensione
  della pagina quando aprite un workflow e tornate indietro, anche tramite il
  breadcrumb, e la pagina si apre per impostazione predefinita sulla scheda
  List.

### Impostazioni e amministrazione

- La pagina dei dati anagrafici non compare più vuota per una race condition
  nell'ordinamento, e l'ordinamento per badge non manda più in crash la
  pagina.
- Un abbonamento in stato "cancelling" può essere ripreso.
- La pagina di dettaglio XSLT segnala gli errori di caricamento invece di non
  mostrare nulla, e le impostazioni delle notifiche e-mail usano l'intera
  larghezza della pagina con un pannello dei log funzionante.
- Il selettore dell'organizzazione per gli utenti multi-organizzazione ha
  layout delle righe, dimensioni e colori del tema corretti, scorre
  correttamente e offre un filtro per gli account con molte organizzazioni.
- Analytics: una richiesta di metriche fallita mostra uno stato di errore
  invece di visualizzare zeri, e i widget di utilizzo segnalano onestamente
  quando non sono disponibili dati di misurazione.
- Le opzioni di cache obsolete sono state rimosse dalla pagina di gestione
  della cache, e le pagine Utenti e Gruppi hanno perso le doppie barre di
  scorrimento annidate.
- "Use Default Template" nel gestore dei layout non va più in crash né resta
  inerte; smette inoltre di sostenere che non esista alcun layout predefinito.
- Le regole di selezione mantengono gli operatori di corrispondenza testuale,
  presenza e regex quando una regola viene riaperta.
- I tipi di documento supportano regole di trasformazione per singolo tipo, e
  l'interfaccia dell'elenco delle regole ha ottenuto un'azione di valore
  fisso.
- I badge di stato degli ordini d'acquisto vengono mappati correttamente per
  i valori di stato con maiuscole in stile ERP.
- Le schermate DocNet (AI Workforce), incluso l'Agent Wizard, sono tradotte,
  e la finestra di dialogo di creazione/modifica delle idee scorre
  orizzontalmente.
- Offerte del portale fornitori: le unità di misura gestite compaiono nella
  tabella delle righe, lo stile delle approvazioni si applica solo alle
  offerte contrattuali, e la riga di confronto non compare più quando i due
  valori sono identici.
- Il fallback JSON della pagina di errore è leggibile in modalità scura, e i
  report usano una vera etichetta "ultimi 7 giorni" invece di un "7" isolato.

## API Service — `12.74.0`

### Dashboard e ricerca

- L'ordinamento funziona indipendentemente da quali colonne siano visibili, e
  una parola chiave che la ricerca delega al full-text non lascia più dietro
  di sé un frammento SQL corrotto.
- I nomi dei fornitori compaiono di nuovo nella ricerca rapida per le
  organizzazioni senza indicizzazione full-text.
- Le date in formato ISO (2026-08-12) non vengono più fraintese dal
  normalizzatore di date giorno-prima.
- Le esportazioni della dashboard indirizzano i valori di testo semplici,
  come i numeri di fattura, nella colonna giusta.

### Fatture elettroniche

- FacturaE 3.1 (Spagna): regola di classificazione e mappature dei campi
  complete.
- Le regole di classificazione XRechnung sono ancorate alla loro famiglia di
  sintassi, così un documento UBL non viene più intercettato dalle regole CII
  e viceversa.
- La versione accettata "3.0" copre l'intera famiglia di patch (3.0.1,
  3.0.2).
- Le fatture CII usano la ragione sociale del fornitore, ricorrendo al nome
  commerciale solo come fallback.
- Le mappature ebInterface (Austria) sono fedeli alla versione, con un
  catch-all corretto e fixture ricostruite.
- I default di Factur-X e ZUGFeRD hanno ottenuto il percorso di estrazione
  del nome dell'azienda, e sono state corrette le trasformazioni di
  intestazione predefinite per aliquota, tipo di fattura e campi di terzo
  livello, insieme alla semantica di sconti, IVA e prezzi unitari per
  l'intera famiglia.
- I codici di categoria fiscale di origine non vengono più mappati alla cieca
  sui vostri codici ERP.
- I documenti che menzionano sia "fattura" sia "nota di credito" preferiscono
  la classificazione come nota di credito.

### Documenti ed estrazione

- Quando il decodificatore PDF standard non riesce a leggere il testo
  incorporato di una pagina, l'estrazione ricorre a un secondo motore, così i
  PDF interessati vengono estratti invece di tornare vuoti.
- L'interruttore principale dei codici a barre è ora `BARCODE_EXTRACTION`; la
  vecchia impostazione dei codici QR continua a funzionare come alias.
- È stata tappata una perdita di memoria nello scheduler in background, che
  degradava lentamente l'elaborazione dopo giorni di attività.
- I fornitori importati senza paese restano senza paese invece di ricevere la
  Germania come valore predefinito.

### Esportazione e dati anagrafici

- Save Rules segnala il fallimento quando non scrive nulla, invece di
  dichiarare il successo.
- Le righe a importo zero non vengono più eliminate dalle esportazioni di
  contabilità automatica, ed è stato corretto un filtro che corrispondeva a
  ogni bucket.
- Le esportazioni M3 supportano post-hook per le informazioni aggiuntive.
- Un singolo probe di dataset fallito non svuota più l'intera schermata dei
  dati anagrafici.
- Le cache dei PO vengono invalidate quando l'ERP aggiorna lo stato di un
  ordine d'acquisto, così la dashboard smette di mostrare lo stato obsoleto.

### Amministrazione

- Ogni preferenza mostra quale utente l'ha modificata per ultimo.
- Le regole di estrazione possono essere eliminate per fornitore e clonate
  tramite nuovi endpoint.
- I destinatari delle e-mail di avviso di stato vengono confrontati in modo
  NULL-safe, correggendo un crash nella consegna delle notifiche.

## Auth Service — `1.75.9`

- Una API key di organizzazione usata contro un'organizzazione estranea viene
  rifiutata.
- La creazione di un'organizzazione restituiva un errore pur salvando
  effettivamente la riga; ora risponde correttamente.
- L'accesso con una passkey quando non ne è registrata nessuna restituisce un
  proprio codice di errore, così la schermata di login può dire cosa non va.

## Auth Bridge Service — `0.4.2`

- Le tabelle di registrazione dell'autenticazione a due fattori vengono
  replicate tra le regioni UE e USA, e le righe sono identificate dalla loro
  vera chiave primaria.

## Docflow Service — `2.8.7`

- Un trigger di workflow che non riesce ad autenticarsi segnala il fallimento
  invece di lasciare il documento bloccato, e un servizio di autenticazione
  momentaneamente irraggiungibile viene ritentato invece di essere trattato
  come token non valido.
- Card di confronto delle offerte: i numeri articolo vengono confrontati solo
  per le righe descritte dalla matrice dei prezzi articolo, e le righe senza
  unità di misura o senza prezzo vengono saltate invece di far fallire il
  confronto.
- La card di confronto dei prezzi contrattuali ha ottenuto un'opzione
  operatore any/all, e le cache delle card vengono invalidate correttamente
  dopo migrazioni e aggiornamenti del codice.
- Le connessioni SSL cadute vengono trattate come transitorie e ritentate
  invece di far fallire l'esecuzione.

## Docnet Service — `1.56.4`

- Gli endpoint di salute e versione non si bloccano più su verifiche live,
  cosa che faceva restare appesa la finestra di dialogo Service Versions.

## Email Service — `1.40.6`

- Quando un'e-mail in ingresso viene saltata, il motivo compare nella riga
  dell'evento di importazione invece di restare silenzioso.
- I file contenitore `.eml` allegati non vengono più importati come
  documenti.
- Un accesso Microsoft Office fallito produce un messaggio di errore
  leggibile, e un errore di trasporto dal servizio AI conta come "unclear"
  anziché come rifiuto.

## Extraction Service — `1.53.8`

- Uno scambio dimostrabile tra importo netto e totale operato dall'AI viene
  annullato dopo l'estrazione dei campi, e i fallimenti delle salvaguardie
  vengono registrati nei log invece di passare in silenzio.
- I campi scansionati dall'AI non tornano più errati dopo il riavvio di un
  documento.
- L'estrazione tabelle AI procede in batch di pagine e accumula tutti i
  batch, così le tabelle lunghe arrivano complete.
- I documenti che menzionano sia "fattura" sia "nota di credito" preferiscono
  la classificazione come nota di credito.
- La pulizia ripetuta di intestazioni e piè di pagina viene messa in cache,
  il che velocizza l'estrazione sui documenti multipagina.

## Fulltext Service — `1.41.7`

- Un filtro OR combinato con una condizione di intervallo o uguaglianza non
  cancella più le frasi di ricerca.
- L'ordinamento usa i percorsi di indice corretti e fa emergere il motivo
  reale quando il backend di ricerca rifiuta una query; una regressione
  dell'ordinamento che aveva rotto del tutto la ricerca raw-query è stata
  corretta la stessa settimana in cui è comparsa.
- Le ricerche di documenti funzionano sugli indici più vecchi con mappatura
  di tipo testo.
- La cache dei token è delimitata alla coppia token-organizzazione, così il
  cambio di organizzazione non può servire risultati nel contesto precedente.
