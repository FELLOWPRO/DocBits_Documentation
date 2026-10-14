# Roadmap DocBits

_Stato della pianificazione al 7 ottobre 2026. Per ogni release sono indicate
la data prevista per sandbox (quando i clienti possono testarla) e la data
prevista per la produzione. I temi descrivono ciò che è pianificato per la
release, non ciò che è già stato rilasciato; ambito e date possono cambiare.
Gli hotfix tra una release e l'altra sono documentati nelle
[Note della versione](release-notes/README.md)._

| Release | Sandbox | Produzione |
|---|---|---|
| R1.1 | 16 ottobre 2026 | 4 novembre 2026 |
| R1.2 | 16 febbraio 2027 | 3 marzo 2027 |
| R1.3 | 1° giugno 2027 | 16 giugno 2027 |
| R1.4 | 5 ottobre 2027 | 20 ottobre 2027 |

---

## R1.1 — Sandbox 16 ottobre 2026 · Produzione 4 novembre 2026

**Regole di trasformazione e layout**

- Un motore di regole per i valori estratti di campi e colonne: impostare,
  sostituire o derivare valori con gruppi di condizioni annidati, con una
  schermata di impostazioni per gestire le regole. La condizione "è uno tra"
  accetta più valori, l'elenco delle regole può essere cercato per ID regola, e
  le regole vengono eseguite anche dopo la ricerca nei dati master.
- Le regole di selezione del layout ottengono le stesse condizioni annidate e un
  log di esecuzione facoltativo. La selezione del layout funziona
  indipendentemente dalla provenienza del documento.
- Manage Layouts, Custom Validation Rules e Transformation Rules non richiedono
  più l'interruttore beta.
- Regole di precedenza chiare per le etichette dei campi di intestazione e delle
  colonne di tabella. Gli utenti possono creare le proprie chiavi di traduzione
  per le impostazioni dei campi e le colonne di tabella.
- Una colonna di tabella può essere assegnata di nuovo dopo essere stata
  eliminata, e la tabella dei prezzi degli articoli del fornitore mostra tutte
  le sue colonne.

**Schermate di approvazione e validazione**

- Le tre tabelle delle voci di riga nella schermata di approvazione (righe della
  fattura, righe di confronto, corrispondenza PO) condividono lo stesso stile.
- L'ultimo pannello laterale aperto (flusso di attività o cronologia delle
  approvazioni) viene ricordato per utente.
- Unione di documenti dalla schermata di approvazione con l'uploader di
  documenti.
- Le regole di validazione personalizzate gestiscono i costi di spedizione in
  modo generico, mostrano un messaggio sul campo invece di un errore generico
  quando un campo obbligatorio è vuoto, e le regole che segnalavano un falso
  negativo sono state corrette. Le regole predefinite di sistema possono essere
  duplicate.
- Viene segnalata una discrepanza tra quantità e importo netto in una tabella
  estratta dall'AI, una fattura con un ordine di acquisto abbinato non viene più
  classificata come fattura di costo, e una data riformattata da una regola
  viene accettata.
- È stata corretta una schermata di approvazione che restava bloccata
  sull'overlay di caricamento dopo l'approvazione o il rifiuto. Una barra di
  caricamento sostituisce la semplice icona di caricamento, e gli URL delle
  pagine sono più leggibili.
- Aprendo il link di un documento dopo la scadenza della sessione si arriva alla
  pagina di accesso invece che a un 404.

**Rilevamento dei duplicati**

- I campi personalizzati compaiono nel risultato del rilevamento dei duplicati,
  e le impostazioni dei duplicati possono essere cercate.
- "Block Duplicate Document Export" blocca l'esportazione di un duplicato
  rilevato.

**Workflow e attività**

- Un pulsante "Nuovo workflow", log per i workflow avanzati, una schermata dei
  log del watchdog più chiara, e i passaggi di workflow che modificano un campo
  o una casella di controllo vengono applicati in modo affidabile.
- L'aggiunta di una riga in un albero decisionale conserva i nomi degli utenti
  invece di mostrare gli ID.
- Ogni cambio di stato di un documento viene registrato.
- La creazione di un nuovo template e-mail funziona di nuovo.
- L'elenco delle attività mostra le proprie attività al primo caricamento.

**Importazione**

- L'importazione e-mail sposta una mail fuori dalla posta in arrivo solo dopo
  che il caricamento è stato confermato, tratta un inoltro riconsegnato come
  un'unica consegna, registra chi ha salvato per ultimo ed elenca un allegato
  una sola volta con il motivo, quando fallisce.
- L'importazione FTP e SFTP ottiene una vera opzione di eliminazione dopo
  l'importazione, accanto a sposta e archivia. Le password non vengono più
  corrotte quando si modifica una configurazione, il test della connessione
  funziona per le nuove connessioni SFTP, e una connessione SFTP non riuscita o
  un accesso errato mostra un messaggio specifico invece di un errore generico.
- Gli amministratori vengono avvisati nel Settings Assistant quando
  un'importazione FTP o e-mail configurata smette di funzionare.
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
- Una fattura di costo con due aliquote IVA mantiene entrambe le righe
  contabili.

**Corrispondenza degli ordini di acquisto**

- La corrispondenza richiede una colonna quantità, usa il prezzo per quantità di
  unità base, e il fallback sull'ultima riga può essere attivato o disattivato
  per cliente.
- Le righe delle bolle di consegna possono essere selezionate singolarmente.
- La schermata e-document non si blocca più su fatture con più di 250 righe.

**Touchless Intelligence**

- Più dettagli nel report Touchless, e la casella di controllo Touchless
  riflette l'impostazione salvata.

**Dashboard, account e abbonamento**

- La dashboard può contenere fino a 10.000 documenti per ricerca, e un filtro
  data personalizzato viene applicato correttamente.
- La data di scadenza dello sconto e la data di scadenza della fattura sono
  disponibili come campi del layout e vengono compilate all'importazione.
- Gli utenti con cui una dashboard è condivisa vengono conservati quando la
  dashboard viene salvata, e "Updated by" mostra la persona giusta.
- I documenti archiviati possono essere riportati fuori dallo stato
  "Archived".
- Gli utenti possono di nuovo accedere dopo la reimpostazione della password.
- La pagina del piano di abbonamento mostra l'utilizzo del piano e delle sue
  funzionalità.

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
- Il test della connessione di una nuova configurazione di esportazione Infor
  IDM o Infor LN funziona.

**Sicurezza**

- Il controllo dell'organizzazione per le API key viene applicato in ogni
  ambiente.

---

## R1.2 — Sandbox 16 febbraio 2027 · Produzione 3 marzo 2027

**Approvazione e corrispondenza degli ordini di acquisto**

- Uno stato "Pending input" mette in pausa un documento finché qualcuno non
  risponde, senza interrompere il workflow o la cronologia di audit, e gli
  approvatori possono porre domande senza interrompere il flusso di
  approvazione.
- Un documento può essere riassegnato a un altro utente (prima fase).
- Le fatture di prepagamento possono essere abbinate prima del ricevimento merci
  mentre "Match on received quantity" resta attivo.
- La schermata di corrispondenza propone solo le righe PO utilizzabili, e le
  corrispondenze multi-riga che saltano il confronto dei prezzi mostrano comunque
  il prezzo unitario nella schermata di approvazione.
- Un flag di disponibilità del ricevimento confronta le quantità fatturate e
  ricevute.
- Conferme d'ordine: elementi di costo mostrati mentre l'approvazione è in
  sospeso, posizioni di maggiorazione con codice colore nella corrispondenza PO,
  e la colonna numero articolo nelle voci di riga della fattura.
- Le righe RMA dei fornitori vengono gestite.

**Importazione e classificazione**

- Il tipo di fornitore viene derivato dalle voci di riga.
- Il modulo dei ticket di supporto accetta allegati e collega automaticamente
  l'organizzazione.

**Impostazioni e automazione**

- Lo script "Set sub-organisation" diventa una regola di trasformazione.
- Le colonne standard possono essere rimosse da un tipo di documento.

**Esportazione**

- La cronologia delle esportazioni elenca di nuovo i documenti esportati.
- Le fatture di trasporto vengono esportate in Infor LN.
- I nomi dei file di esportazione sono configurabili.
- Integrazione fiscale Vertex estesa.

---

## R1.3 — Sandbox 1° giugno 2027 · Produzione 16 giugno 2027

**Rule Manager di Auto Accounting**

- Le regole assegnano automaticamente conti e dimensioni, con ambito per
  sotto-organizzazione e tipo di documento, con una schermata di audit che
  mostra quale regola è scattata.
- Una regola può cercare nei dati master e assegnare più campi in una volta,
  oppure compilare un valore da una colonna delle righe di tabella.
- Campi e dimensioni possono essere svuotati singolarmente, le voci di riga
  possono essere eliminate (incluse le righe senza importo), e le regole
  continuano a funzionare sui campi passati da testo a menu a tendina.
- Le previsioni supportano più codici imposta e dimensioni, voucher e
  riferimenti di registrazione. Le schermate di Auto Accounting sono disponibili
  in più lingue.

**Corrispondenza degli ordini di acquisto**

- L'icona di corrispondenza naviga, scorre ed evidenzia tra le schede, incluse
  le corrispondenze uno-a-molti.
- Conversione delle unità con alias (ad esempio KG e TO), una varianza di
  arrotondamento configurabile con un conto di arrotondamento, e calcoli a
  quattro decimali mostrati come tre.

**Usabilità**

- L'ordine di esecuzione degli script del documento è visibile nel frontend.
- Invio e Tab spostano tra i campi da tastiera.

**Esportazione**

- Un documento incompleto in Infor LN viene eliminato dopo un'esportazione
  fallita.
- Il connettore database include tutte le tabelle rilevanti.

---

## R1.4 — Sandbox 5 ottobre 2027 · Produzione 20 ottobre 2027

**Auto Accounting nella schermata di approvazione**

- Gli approvatori possono lavorare con Auto Accounting direttamente nella
  schermata di approvazione.
- L'approvazione può essere subordinata a campi contabili come il conto
  contabile o il paese, con una correzione nella contabilità fornitori quando un
  documento viene restituito.
- Un menu a tendina per il codice imposta in Auto Accounting senza dover
  configurare più righe di imposta.
- Le dimensioni vengono memorizzate in una nuova struttura, così i set di
  dimensioni più ampi si caricano più velocemente, e il Rule Manager ottiene un
  giro di feedback.

**Approvazione**

- Un flusso di approvazione migliorato, delega a un altro utente durante
  l'approvazione, e un pulsante "Export & Next".

**Corrispondenza degli ordini di acquisto e controlli sull'esportazione**

- Le fatture con corrispondenza in eccesso, in cui la quantità fatturata supera
  la quantità ricevuta, vengono riconosciute nella schermata di corrispondenza,
  e le unità di misura vengono convertite durante la corrispondenza della
  fattura.
- I codici di addebito (pedaggio, trasporto, energia) vengono riconosciuti e il
  loro costo distribuito.
- L'esportazione viene bloccata con un avviso quando la quantità abbinata supera
  o si discosta troppo dalla quantità ricevuta, o quando la data di registrazione
  è anteriore alla data di entrata in magazzino.

**Importazione e impostazioni**

- Un meccanismo di nuovi tentativi per l'importazione FTP, e-mail ed e-mail in
  entrata con rielaborazione automatica e manuale, e l'indirizzo del mittente è
  disponibile dall'importazione e-mail.
- Le impostazioni possono essere cercate in tutti gli interruttori e in tutte le
  sottopagine.
- La configurazione del server e-mail permette di sostituire un secret OAuth o
  client secret scaduto senza dover configurare di nuovo la casella di posta.
- La mappa dei numeri articolo fornitore (tabella di conversione dei numeri
  articolo) può essere compilata da un'importazione CSV.
- La cronologia delle approvazioni può essere esportata tramite esportazione
  SFTP.

**DocNet Agents**

- Acquisizione ordini: un ordine cliente diventa un ordine di vendita in Infor
  M3 o Infor LN (prima versione, documenti di testo).

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-10-07 by the
     docbits-roadmap skill. Releases up to R1.4 only; R1.5 and later are not
     published yet. Themes only; ticket keys, customer names and internal work
     are deliberately left out. Rerun the skill to refresh. -->
