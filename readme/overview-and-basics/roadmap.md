# Roadmap DocBits

_Stato della pianificazione al 15 settembre 2026. Per ogni release sono
indicate la data prevista per sandbox (quando i clienti possono testarla) e la
data prevista per la produzione. I temi descrivono ciò che è pianificato per
la release, non ciò che è già stato rilasciato; ambito e date possono cambiare.
Gli hotfix tra una release e l'altra sono documentati nelle
[Note della versione](release-notes/README.md)._

| Release | Sandbox | Produzione |
|---|---|---|
| R1.1 | 16 settembre 2026 | 23 settembre 2026 |
| R1.2 | 21 ottobre 2026 | 28 ottobre 2026 |
| R1.3 | 25 novembre 2026 | 2 dicembre 2026 |
| R1.4 | 27 gennaio 2027 | 3 febbraio 2027 |
| R1.5 | 10 marzo 2027 | 17 marzo 2027 |

---

## R1.1 — Sandbox 16 settembre 2026 · Produzione 23 settembre 2026

**Regole di trasformazione e layout**

- Un motore di regole per i valori estratti di campi e colonne: impostare,
  sostituire o derivare valori con gruppi di condizioni annidati, con una
  schermata di impostazioni per gestire le regole. Le regole di selezione del
  layout ottengono le stesse condizioni annidate.
- La selezione del layout funziona indipendentemente dalla provenienza del
  documento.
- Regole di precedenza chiare per le etichette dei campi di intestazione e
  delle colonne di tabella.

**Schermate di approvazione e validazione**

- Le tre tabelle delle voci di riga nella schermata di approvazione (righe
  della fattura, righe di confronto, corrispondenza PO) condividono lo stesso
  stile, e la vista di confronto mostra il numero articolo che appartiene alla
  riga.
- L'ultimo pannello laterale aperto (flusso di attività o cronologia delle
  approvazioni) viene ricordato per utente.
- Unione di documenti dalla schermata di approvazione con l'uploader di
  documenti.
- Le regole di validazione personalizzate gestiscono i costi di spedizione in
  modo generico, e le regole che segnalavano un falso negativo sono state
  corrette.
- Una barra di caricamento sostituisce la semplice icona di caricamento; URL
  delle pagine più leggibili.

**Rilevamento dei duplicati**

- I campi personalizzati compaiono nel risultato del rilevamento dei
  duplicati, e le impostazioni dei duplicati possono essere cercate.

**Workflow e attività**

- Un pulsante "Nuovo workflow", log per i workflow avanzati, e i passaggi di
  workflow che modificano un campo o una casella di controllo vengono
  applicati in modo affidabile.
- Le e-mail di approvazione raggiungono gli approvatori assegnati nei workflow
  delle fatture di acquisto.
- Ogni cambio di stato di un documento viene registrato.

**Importazione**

- L'importazione e-mail sposta una mail fuori dalla posta in arrivo solo dopo
  che il caricamento è stato confermato, tratta un inoltro riconsegnato come
  un'unica consegna, registra chi ha salvato per ultimo e accetta mail
  firmate S/MIME.
- L'importazione FTP ottiene una vera opzione di eliminazione dopo
  l'importazione, accanto a sposta e archivia.
- Il caricamento dall'app scanner funziona di nuovo.

**Elaborazione dei documenti ed estrazione**

- Quando il servizio codici a barre si blocca, il documento mostra l'errore
  invece di restare in "Processing" a tempo indeterminato.
- "Restrict to pages" limita solo l'OCR e il conteggio delle pagine; non
  taglia più pagine dal documento.
- Il salvataggio di un documento lascia intatti i dati non correlati.
- Un nuovo livello di modello AI più economico ("Eco") per l'estrazione, e
  l'applicazione dei tag di tabella sulla tabella AI funziona di nuovo.
- L'unione di un PDF ZUGFeRD con un altro PDF conserva i dati della fattura
  elettronica; i template UBL per gli e-document vengono adeguati; correzioni
  dell'estrazione per importi, aliquote fiscali e numeri di ordine di acquisto
  su layout specifici di fornitori.
- Vengono riconosciuti ulteriori formati di data.

**Corrispondenza degli ordini di acquisto**

- La corrispondenza richiede una colonna quantità, usa il prezzo per quantità
  di unità base, e il fallback sull'ultima riga può essere attivato o
  disattivato per cliente.
- La schermata e-document non si blocca più su fatture con più di 250 righe.
- La diagnostica misura la quantità anche quando una riga PO non ha prezzo.

**Touchless Intelligence**

- Più dettagli nel report Touchless, e un blocco dovuto all'ordine di acquisto
  viene segnalato come tale invece che come errore di validazione di un campo.

**Dashboard**

- La dashboard può contenere fino a 10.000 documenti per ricerca.
- La data di scadenza dello sconto e la data di scadenza della fattura sono
  disponibili come campi del layout e vengono compilate all'importazione.
- Gli utenti con cui una dashboard è condivisa vengono conservati quando la
  dashboard viene salvata; "Assigned to" e "Updated by" mostrano la persona
  giusta.
- I permessi sui documenti si applicano anche all'indice full-text.

**Esportazione ed EDI**

- L'esportazione BOD conserva i valori delle colonne di tabella più lunghi di
  30 caratteri.
- Un passaggio aggiuntivo di esportazione Infor M3 per informazioni
  supplementari sulla fattura, e prezzi unitari nelle esportazioni di tipo
  riga 5.
- La reimportazione di una receive delivery non fallisce più per una chiave
  duplicata.
- Le mappature EDI X12 per fattura (810), ordine di acquisto (850), conferma
  d'ordine (855), avviso di spedizione (856, inclusa l'esportazione WMS) e
  modifica d'ordine (860) sono aggiornate.

**Sicurezza**

- Le mappature del piano dei conti dei fornitori vengono memorizzate con
  parametri SQL vincolati, e il controllo dell'organizzazione per le API key
  viene applicato in ogni ambiente.

---

## R1.2 — Sandbox 21 ottobre 2026 · Produzione 28 ottobre 2026

**Approvazione e corrispondenza degli ordini di acquisto**

- Uno stato "Pending input" mette in pausa un documento finché qualcuno non
  risponde, senza interrompere il workflow o la cronologia di audit, e gli
  approvatori possono porre domande senza interrompere il flusso di
  approvazione.
- Le fatture di prepagamento possono essere abbinate prima del ricevimento
  merci mentre "Match on received quantity" resta attivo.
- Un flag di disponibilità del ricevimento confronta le quantità fatturate e
  ricevute.
- Conferme d'ordine: elementi di costo mostrati mentre l'approvazione è in
  sospeso, posizioni di maggiorazione con codice colore nella corrispondenza
  PO, e la colonna numero articolo nelle voci di riga della fattura.
- Le colonne non mappate non alimentano più il calcolo dell'importo della
  tabella.
- Le righe RMA dei fornitori vengono gestite.

**Importazione e classificazione**

- L'indirizzo del mittente è disponibile dall'importazione e-mail.
- Il tipo di fornitore viene derivato dalle voci di riga.

**Impostazioni e automazione**

- Lo script "Set sub-organisation" diventa una regola di trasformazione.
- Le colonne standard possono essere rimosse da un tipo di documento.
- Un flusso di richiesta di modifica PO e il proprietario del documento nella
  mappatura di esportazione Infor.

**Esportazione**

- La cronologia delle esportazioni elenca di nuovo i documenti esportati.
- Le fatture di trasporto vengono esportate in Infor LN.

---

## R1.3 — Sandbox 25 novembre 2026 · Produzione 2 dicembre 2026

**Rule Manager di Auto Accounting**

- Le regole assegnano automaticamente conti e dimensioni, con ambito per
  sotto-organizzazione e tipo di documento, con una schermata di audit che
  mostra quale regola è scattata.
- Una regola può compilare un valore da una colonna delle righe di tabella.
- Campi e dimensioni possono essere svuotati singolarmente, le righe senza
  importo possono essere eliminate, e le regole continuano a funzionare sui
  campi passati da testo a menu a tendina.

**Corrispondenza degli ordini di acquisto**

- L'icona di corrispondenza naviga, scorre ed evidenzia tra le schede,
  incluse le corrispondenze uno-a-molti.
- Conversione delle unità con alias (ad esempio KG e TO), una varianza di
  arrotondamento configurabile con un conto di arrotondamento, e calcoli a
  quattro decimali mostrati come tre.

**Esportazione**

- Nomi dei file di esportazione configurabili.
- Un documento incompleto in Infor LN viene eliminato dopo un'esportazione
  fallita.
- Il connettore database include tutte le tabelle rilevanti.

---

## R1.4 — Sandbox 27 gennaio 2027 · Produzione 3 febbraio 2027

**Importazione**

- Un meccanismo di nuovi tentativi per l'importazione FTP, e-mail ed e-mail in
  entrata con rielaborazione automatica e manuale.

**DocNet Agents**

- Acquisizione ordini: un ordine cliente diventa un ordine di vendita in Infor
  M3 o Infor LN (prima versione, documenti di testo).

**Approvazione**

- Un flusso di approvazione migliorato, delega a un altro utente durante
  l'approvazione, e un pulsante "Export & Next".

**Corrispondenza degli ordini di acquisto**

- Nella schermata di corrispondenza vengono proposte solo le righe PO
  utilizzabili.
- Più entrate di magazzino possono corrispondere a una riga della fattura, e
  le unità di misura vengono convertite durante la corrispondenza della
  fattura.

**Altro**

- Giro di feedback sul Rule Manager.
- Il modulo dei ticket di supporto accetta allegati e collega automaticamente
  l'organizzazione.
- Integrazione fiscale Vertex estesa.

---

## R1.5 — Sandbox 10 marzo 2027 · Produzione 17 marzo 2027

**Auto Accounting**

- Azione di lookup del Rule Manager: trovare la corrispondenza nei dati master
  e assegnare più campi in una volta.
- Le previsioni supportano più codici imposta e dimensioni, voucher e
  riferimenti di registrazione.
- Schermate Auto Accounting in più lingue.

**Approvazione e corrispondenza degli ordini di acquisto**

- Riassegnazione di un documento a un altro utente.
- L'ordine delle colonne nella schermata di corrispondenza PO viene salvato
  per utente.
- I codici di addebito (pedaggio, trasporto, energia) vengono riconosciuti e
  il loro costo distribuito.

**Controlli sull'esportazione**

- L'esportazione viene bloccata con un avviso quando la quantità abbinata
  supera o si discosta troppo dalla quantità ricevuta, o quando la data di
  registrazione è anteriore alla data di entrata in magazzino.

**Usabilità**

- L'ordine di esecuzione degli script del documento è visibile nel frontend.
- Invio e Tab spostano tra i campi da tastiera.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-15 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
