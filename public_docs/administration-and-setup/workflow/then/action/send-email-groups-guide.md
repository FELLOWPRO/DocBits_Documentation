# Invia e-mail ai gruppi

***

Aggiungi questa scheda al gruppo **Allora** del Workflow Builder: le azioni che vengono eseguite una volta che le condizioni Quando/E corrispondono:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-it.png" alt="Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

***

## 📌 Informazioni sulla versione

**Stato:** ✅ Versione singola (nessuna modifica sostanziale) **Ultima versione:** v1 (attiva) **Nota:** Questa scheda utilizza il modello a versione singola con supporto multilingue tramite chiavi di traduzione.

📖 [Database completo delle carte](../../cards-overview/export-cards-guide.md)

***

## Scopo

Questa scheda invia automaticamente notifiche e-mail a gruppi di utenti. Invece di assegnare il lavoro a singole persone, invii il messaggio a un gruppo e tutti i membri di quel gruppo lo ricevono.

**Esempio reale:** Quando arriva una fattura di valore elevato, invia automaticamente una notifica via email a tutti nel gruppo "Team finanziario" in modo che siano consapevoli che necessita di revisione.

***

## Quando utilizzare questa carta

Utilizza questa carta quando hai bisogno di:

* Avvisa più persone contemporaneamente
* Invia avvisi ai gruppi del team
* Trasmetti aggiornamenti ai dipartimenti
* Notifica ai gruppi le modifiche allo stato del documento
* Invia promemoria ai membri del gruppo

**Scenari comuni:**

* Informare il team di approvvigionamento sui nuovi fornitori
* Avvisa il team finanziario in caso di fatture di valore elevato
* Avvisare il team del magazzino delle spedizioni
* Trasmetti le modifiche allo stato del documento

***

## Come funziona

1. **Condition Check**: il flusso di lavoro controlla le condizioni "Quando" e "E"
2. **Prepara email**: il sistema prepara l'email utilizzando il modello
3. **Ottieni membri del gruppo**: il sistema trova tutti i membri del gruppo specificato
4. **Send**: l'e-mail viene inviata a ciascun membro del gruppo
5. **Log**: l'invio di e-mail viene registrato

***

## Parametri spiegati

### Modello di posta elettronica

Il messaggio di posta elettronica da inviare

**Opzioni:**

* Scegli tra i modelli esistenti
* Ogni modello ha oggetto, corpo e formattazione predefiniti
* I modelli possono includere segnaposto come {document\_number}, {supplier\_name}

**Modello di esempio:**

```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Gruppo

Il gruppo di utenti a cui inviare l'e-mail

**Gruppi di esempio:**

* Squadra finanziaria
* Gruppo Acquisti
* Squadra del magazzino
* Comitato di approvazione
* Gruppo di gestione

***

## Passaggi di configurazione

### Passaggio 1: scegli il modello di email

1. Fai clic su "Seleziona modello di email"
2. Scegli il modello dall'elenco
3. Verificare oggetto e contenuto

### Passaggio 2: seleziona Gruppo

1. Fare clic su "Seleziona gruppo"
2. Scegli il gruppo a cui vuoi inviare la notifica
3. Verifica i membri del gruppo (di solito mostra il conteggio)

### Passaggio 3: imposta le condizioni

1. Aggiungi condizione: "Quando \[condizione] è vera"
2. Esempio: "Quando l'importo della fattura è superiore a 5000 €"

### Passaggio 4: prova

1. Prova con il documento di esempio
2. Verifica l'invio di email al gruppo
3. Controlla il rendering del modello

***

## Esempi di modelli di posta elettronica

### Modello 1: Avviso fatture di valore elevato

```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Modello 2: Modifica dello stato del fornitore

```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Modello 3: documento pronto per l'esportazione

```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

***

## Casi d'uso comuni

### Caso d'uso 1: avvisi di controllo qualità

**Innesco:** Quando viene rilevata una discrepanza tra fattura e ordine d'acquisto

**Gruppo e-mail:** Team di qualità

**Contenuto:**

```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Caso d'uso 2: notifiche di approvazione

**Innesco:** Quando il documento raggiunge un determinato stato

**Gruppo email:** Comitato di approvazione

**Contenuto:**

```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Caso d'uso 3: notifiche di eccezioni

**Innesco:** Quando le condizioni non sono soddisfatte

**Gruppo e-mail:** Manager

**Contenuto:**

```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Caso d'uso 4: aggiornamenti di stato

**Innesco:** Quando cambia lo stato del documento

**E-mail gruppo:** Team responsabile del passaggio successivo

**Contenuto:**

```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

***

## Risoluzione dei problemi

### "E-mail non ricevuta"

**Causa possibile:**

* [] Gli utenti del gruppo non hanno indirizzi email
* [ ] Email bloccata dal filtro antispam
* [] L'indirizzo e-mail nel gruppo non è corretto
* [ ] Il gruppo non ha membri

**Soluzioni:**

1. Verifica che tutti i membri del gruppo dispongano di indirizzi email
2. Controlla la cartella spam/posta indesiderata
3. Verificare che l'appartenenza al gruppo sia corretta
4. Aggiungi utenti al gruppo se mancanti
5. Verificare con l'IT che il servizio di posta elettronica funzioni

### "Il modello non viene visualizzato correttamente"

**Causa:** Variabili segnaposto non trovate

**Soluzione:**

* [ ] Verificare che i nomi dei campi corrispondano esattamente
* [ ] Controlla se il campo ha un valore nel documento
* [ ] Utilizza il formato segnaposto corretto: {field\_name}
* [ ] Prova con un documento di esempio che contiene tutti i campi

### "Alcune persone ricevono la posta elettronica, altre no"

**Causa:** Appartenenza al gruppo incompleta o email non valide

**Soluzioni:**

* [] Verificare che tutti i membri abbiano un'e-mail valida
* [ ] Controlla se alcuni utenti hanno rinunciato
* [ ] Verificare che l'appartenenza al gruppo sia attuale
* [ ] Contattare l'IT per convalidare gli indirizzi e-mail

### "Vuoi aggiungere/rimuovere persone dal gruppo"

**Soluzione:**

* Contatta il tuo amministratore
* I gruppi sono gestiti nelle impostazioni di sistema
* Non può essere modificato da questa carta
* Richiedere modifiche all'appartenenza al gruppo nell'IT

***

## Personalizzazione del modello di posta elettronica

### Segnaposto disponibili

```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Creazione di segnaposto personalizzati

Se hai bisogno di dati aggiuntivi nelle email:

1. Contatta il tuo amministratore
2. Richiedi un nuovo segnaposto
3. Aggiungi il campo necessario al documento
4. Aggiorna il modello di posta elettronica

***

## Migliori pratiche

✅ **Fai:**

* Mantieni il contenuto delle email breve e chiaro
* Includi azioni (cosa dovrebbero fare i destinatari?)
* Includere collegamento o istruzioni per accedere al documento
* Modello di test con dati di esempio
* Invia al gruppo giusto (non inviare notifiche eccessive)
* Utilizza i modelli per coerenza

❌ **Non farlo:**

* Invia troppe email (affaticamento delle notifiche)
* Includi dati sensibili nelle email
* Invia a gruppi che non necessitano di informazioni
* Utilizza argomenti poco chiari
* Dimentica di includere come agire
* Invia email a singoli individui (usa invece il gruppo)

***

## Note sulle prestazioni

* Ogni email impiega \~1 secondo per essere inviata
* I gruppi numerosi potrebbero richiedere tempo (100 persone = \~100 secondi)
* Non creare loop che inviano migliaia di email
* Monitorare la capacità del servizio di posta elettronica
* Considera l'idea di raggruppare molti documenti

***

## Carte correlate

* **ACTION\_SEND\_EMAIL** - Invia a singola persona
* **ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP** - Assegna attività invece di limitarsi a notificare
* **ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL** - Crea attività e notifica
* **STAUS\_CHANGE** - Modifica stato e notifica

***

## Tipico esempio di flusso di lavoro

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

***

## Domande frequenti

**D: Posso inviare a più gruppi?** A: Crea cartoline separate per ciascun gruppo

**D: Cosa succede se l'e-mail di qualcuno torna indietro?** R: L'e-mail viene registrata come non riuscita, l'IT può risolvere il problema

**D: Posso cambiare il modello di email?** A: Contatta il tuo amministratore per modificare i modelli

**D: Posso inviare in base alle condizioni?** A: Sì! Utilizza le condizioni "Quando" e "E" per controllare quando inviare le email

**D: Come faccio a sapere se l'e-mail è stata ricevuta?** A: Controlla i log delle e-mail in DocBits per lo stato di invio
