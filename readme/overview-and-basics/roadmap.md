# Roadmap DocBits

_Stato della pianificazione al 18 settembre 2026. Per ogni release sono
indicate la data prevista per sandbox (quando i clienti possono testarla) e la
data prevista per la produzione. I temi descrivono ciò che è pianificato per
la release, non ciò che è già stato rilasciato; ambito e date possono cambiare.
Gli hotfix tra una release e l'altra sono documentati nelle
[Note della versione](release-notes/README.md)._

| Release | Sandbox | Produzione |
|---|---|---|
| R1.1 | 5 ottobre 2026 | 14 ottobre 2026 |
| R1.2 | 23 novembre 2026 | 2 dicembre 2026 |
| R1.3 | 8 febbraio 2027 | 17 febbraio 2027 |
| R1.4 | 7 aprile 2027 | 15 aprile 2027 |
| R1.5 | 18 maggio 2027 | 27 maggio 2027 |
| R1.6 | 6 luglio 2027 | 15 luglio 2027 |
| R1.7 | 21 settembre 2027 | 30 settembre 2027 |
| R2.0 | da definire | da definire |

---

## R1.1 — Sandbox 5 ottobre 2026 · Produzione 14 ottobre 2026

**Regole di trasformazione e layout**

- Un motore di regole per i valori estratti di campi e colonne: impostare,
  sostituire o derivare valori con gruppi di condizioni annidati, con una
  schermata di impostazioni per gestire le regole. Le regole di selezione del
  layout ottengono le stesse condizioni annidate.
- La selezione del layout funziona indipendentemente dalla provenienza del
  documento.
- Regole di precedenza chiare per le etichette dei campi di intestazione e
  delle colonne di tabella.
- Una colonna di tabella può essere assegnata di nuovo dopo essere stata
  eliminata, e la tabella dei prezzi degli articoli del fornitore mostra tutte
  le sue colonne.

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

- Un pulsante "Nuovo workflow", log per i workflow avanzati, una schermata dei
  log del watchdog più chiara, e i passaggi di workflow che modificano un campo
  o una casella di controllo vengono applicati in modo affidabile.
- L'aggiunta di una riga in un albero decisionale conserva i nomi degli utenti
  invece di mostrare gli ID.
- Ogni cambio di stato di un documento viene registrato.
- La creazione di un nuovo template e-mail funziona di nuovo.

**Importazione**

- L'importazione e-mail sposta una mail fuori dalla posta in arrivo solo dopo
  che il caricamento è stato confermato, tratta un inoltro riconsegnato come
  un'unica consegna, registra chi ha salvato per ultimo e accetta mail
  firmate S/MIME.
- L'importazione FTP ottiene una vera opzione di eliminazione dopo
  l'importazione, accanto a sposta e archivia.
- Il caricamento dall'app scanner funziona di nuovo.
- I file BOD degli ordini di acquisto caricati nella regione USA restano nella
  regione USA.

**Elaborazione dei documenti ed estrazione**

- Quando il servizio codici a barre si blocca, il documento mostra l'errore
  invece di restare in "Processing" a tempo indeterminato.
- Un nuovo livello di modello AI più economico ("Eco") per l'estrazione.
- Con l'estrazione AI strutturata, i numeri articolo fornitore addestrati
  restano addestrati, e numero articolo e numero articolo fornitore non vengono
  più scambiati.
- I template UBL per gli e-document vengono adeguati; correzioni
  dell'estrazione per importi, aliquote fiscali, prezzi unitari e numeri di
  ordine di acquisto su layout specifici di fornitori.
- Vengono riconosciuti ulteriori formati di data.

**Corrispondenza degli ordini di acquisto**

- La corrispondenza richiede una colonna quantità, usa il prezzo per quantità
  di unità base, e il fallback sull'ultima riga può essere attivato o
  disattivato per cliente.
- Le righe delle bolle di consegna possono essere selezionate singolarmente.
- La schermata e-document non si blocca più su fatture con più di 250 righe.

**Touchless Intelligence**

- Più dettagli nel report Touchless, e la casella di controllo Touchless
  riflette l'impostazione salvata.

**Dashboard**

- La dashboard può contenere fino a 10.000 documenti per ricerca.
- La data di scadenza dello sconto e la data di scadenza della fattura sono
  disponibili come campi del layout e vengono compilate all'importazione.
- Gli utenti con cui una dashboard è condivisa vengono conservati quando la
  dashboard viene salvata, e "Updated by" mostra la persona giusta.
- I documenti archiviati possono essere riportati fuori dallo stato
  "Archived".

**Esportazione ed EDI**

- Un passaggio aggiuntivo di esportazione Infor M3 per informazioni
  supplementari sulla fattura.
- Una packing list con più numeri di container viene esportata come un record
  per container.
- La reimportazione di una receive delivery non fallisce più per una chiave
  duplicata, e i BOD di receive delivery vengono applicati nell'ordine
  corretto.
- Le mappature EDI per fattura, ordine di acquisto e conferma d'ordine sono
  aggiornate.

**Sicurezza**

- Il controllo dell'organizzazione per le API key viene applicato in ogni
  ambiente.

---

## R1.2 — Sandbox 23 novembre 2026 · Produzione 2 dicembre 2026

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

**Esportazione**

- La cronologia delle esportazioni elenca di nuovo i documenti esportati.
- Le fatture di trasporto vengono esportate in Infor LN.

---

## R1.3 — Sandbox 8 febbraio 2027 · Produzione 17 febbraio 2027

**Rule Manager di Auto Accounting**

- Le regole assegnano automaticamente conti e dimensioni, con ambito per
  sotto-organizzazione e tipo di documento, con una schermata di audit che
  mostra quale regola è scattata.
- Una regola può compilare un valore da una colonna delle righe di tabella.
- Campi e dimensioni possono essere svuotati singolarmente, le voci di riga
  possono essere eliminate (incluse le righe senza importo), e le regole
  continuano a funzionare sui campi passati da testo a menu a tendina.

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

## R1.4 — Sandbox 7 aprile 2027 · Produzione 15 aprile 2027

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
- Le fatture con corrispondenza in eccesso, in cui la quantità fatturata supera
  la quantità ricevuta, vengono riconosciute nella schermata di corrispondenza,
  e le unità di misura vengono convertite durante la corrispondenza della
  fattura.

**Altro**

- Giro di feedback sul Rule Manager.
- Il modulo dei ticket di supporto accetta allegati e collega automaticamente
  l'organizzazione.
- Integrazione fiscale Vertex estesa.

---

## R1.5 — Sandbox 18 maggio 2027 · Produzione 27 maggio 2027

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

---

## R1.6 — Sandbox 6 luglio 2027 · Produzione 15 luglio 2027

**Impostazioni**

- Le impostazioni possono essere cercate in tutti gli interruttori e in tutte
  le sottopagine.
- La configurazione del server e-mail permette di sostituire un secret OAuth o
  client secret scaduto senza dover configurare di nuovo la casella di posta.
- La mappa dei numeri articolo fornitore (tabella di conversione dei numeri
  articolo) può essere compilata da un'importazione CSV.

**Auto Accounting**

- Le dimensioni vengono memorizzate in una nuova struttura, così i set di
  dimensioni più ampi si caricano più velocemente.

---

## R1.7 — Sandbox 21 settembre 2027 · Produzione 30 settembre 2027

**Auto Accounting nella schermata di approvazione**

- Gli approvatori possono lavorare con Auto Accounting direttamente nella
  schermata di approvazione.
- L'approvazione può essere subordinata a campi contabili come il conto
  contabile o il paese, con una correzione nella contabilità fornitori quando
  un documento viene restituito.
- Un menu a tendina per il codice imposta in Auto Accounting senza dover
  configurare più righe di imposta.

---

## R2.0 — Sandbox da definire · Produzione da definire

**Auto Accounting**

- I campi basati su un elenco accettano anche testo libero.
- I campi obbligatori vengono validati.
- Le previsioni del modello compilano automaticamente i campi contabili
  (modalità ibrida con il modello di previsione addestrato), con una traccia di
  audit di ciò che il modello ha compilato.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
