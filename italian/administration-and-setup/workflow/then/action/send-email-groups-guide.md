# Send Email to Groups

Queste schede vanno nel gruppo **Then** del Generatore di workflow — le azioni eseguite una volta soddisfatte le condizioni When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede vengono aggiunte al gruppo <strong>Then</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

## Scopo
Questa card invia automaticamente notifiche email a gruppi di utenti. Invece di assegnare il lavoro a singole persone, invii il messaggio a un gruppo e tutti i membri di quel gruppo lo ricevono.

**Esempio reale:** quando arriva una fattura di alto valore, invia automaticamente una notifica email a tutti i membri del gruppo "Finance Team" in modo che sappiano che richiede una revisione.

---

## Quando Usare Questa Card

Usa questa card quando devi:
- Notificare più persone contemporaneamente
- Inviare avvisi a gruppi di team
- Diffondere aggiornamenti ai reparti
- Notificare ai gruppi i cambiamenti di stato dei documenti
- Inviare promemoria ai membri del gruppo

**Scenari comuni:**
- Notificare al team di approvvigionamento i nuovi fornitori
- Avvisare il team finanziario delle fatture di alto valore
- Notificare al team di magazzino le spedizioni
- Diffondere i cambiamenti di stato dei documenti

---

## Come Funziona

1. **Controllo delle Condizioni**: il workflow verifica le condizioni "Where" e "And"
2. **Preparazione dell'Email**: il sistema prepara l'email utilizzando il template
3. **Recupero dei Membri del Gruppo**: il sistema individua tutti i membri del gruppo specificato
4. **Invio**: l'email viene inviata a ciascun membro del gruppo
5. **Log**: l'invio dell'email viene registrato

---

## Parametri Spiegati

### Email Template
Il messaggio email da inviare

**Opzioni:**
- Scegli da template esistenti
- Ogni template ha oggetto, corpo e formattazione predefiniti
- I template possono includere segnaposto come {document_number}, {supplier_name}

**Template di Esempio:**
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

### Group
Il gruppo di utenti a cui inviare l'email

**Gruppi di esempio:**
- Finance Team
- Procurement Team
- Warehouse Team
- Approval Committee
- Management Group

---

## Passaggi di Configurazione

### Passaggio 1: Scegli il Template Email
1. Fai clic su "Select Email Template"
2. Scegli il template dall'elenco
3. Verifica l'oggetto e il contenuto

### Passaggio 2: Seleziona il Gruppo
1. Fai clic su "Select Group"
2. Scegli il gruppo che vuoi notificare
3. Verifica i membri del gruppo (di solito mostra il conteggio)

### Passaggio 3: Imposta le Condizioni
1. Aggiungi la condizione: "When [condition] is true"
2. Esempio: "When invoice amount is greater than €5000"

### Passaggio 4: Testa
1. Testa con un documento di esempio
2. Verifica che l'email venga inviata al gruppo
3. Controlla il rendering del template

---

## Esempi di Template Email

### Template 1: Avviso di Fattura di Alto Valore
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

### Template 2: Cambio di Stato del Fornitore
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

### Template 3: Documento Pronto per l'Esportazione
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

---

## Casi d'Uso Comuni

### Caso d'Uso 1: Avvisi di Controllo Qualità
**Trigger:** quando viene rilevata una discrepanza tra la fattura e il PO

**Gruppo Email:** Quality Team

**Contenuto:**
```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Caso d'Uso 2: Notifiche di Approvazione
**Trigger:** quando un documento raggiunge un determinato stato

**Gruppo Email:** Approval Committee

**Contenuto:**
```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Caso d'Uso 3: Notifiche di Eccezione
**Trigger:** quando le condizioni non sono soddisfatte

**Gruppo Email:** Managers

**Contenuto:**
```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Caso d'Uso 4: Aggiornamenti di Stato
**Trigger:** quando lo stato di un documento cambia

**Gruppo Email:** team responsabile del passaggio successivo

**Contenuto:**
```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

---

## Risoluzione dei Problemi

### "Email not received"

**Possibili Cause:**
- [ ] Gli utenti nel gruppo non hanno indirizzi email
- [ ] Email bloccata dal filtro antispam
- [ ] L'indirizzo email nel gruppo è errato
- [ ] Il gruppo non ha membri

**Soluzioni:**
1. Verifica che tutti i membri del gruppo abbiano indirizzi email
2. Controlla la cartella spam/posta indesiderata
3. Verifica che l'appartenenza al gruppo sia corretta
4. Aggiungi gli utenti al gruppo se mancanti
5. Verifica con l'IT che il servizio email funzioni

### "Template not rendering correctly"

**Causa:** variabili segnaposto non trovate

**Soluzione:**
- [ ] Verifica che i nomi dei campi corrispondano esattamente
- [ ] Controlla se il campo ha un valore nel documento
- [ ] Usa il formato corretto del segnaposto: {field_name}
- [ ] Testa con un documento di esempio che contenga tutti i campi

### "Some people getting email, others not"

**Causa:** appartenenza al gruppo incompleta o email non valide

**Soluzioni:**
- [ ] Verifica che tutti i membri abbiano un'email valida
- [ ] Controlla se alcuni utenti hanno disattivato le notifiche
- [ ] Verifica che l'appartenenza al gruppo sia aggiornata
- [ ] Contatta l'IT per convalidare gli indirizzi email

### "Want to add/remove people from group"

**Soluzione:**
- Contatta il tuo amministratore
- I gruppi sono gestiti nelle impostazioni di sistema
- Non possono essere modificati da questa card
- Richiedi le modifiche all'appartenenza al gruppo all'IT

---

## Personalizzazione del Template Email

### Segnaposto Disponibili
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

### Creazione di Segnaposto Personalizzati
Se hai bisogno di dati aggiuntivi nelle email:
1. Contatta il tuo amministratore
2. Richiedi un nuovo segnaposto
3. Aggiungi il campo necessario al documento
4. Aggiorna il template email

---

## Best Practice

✅ **Fai:**
- Mantieni il contenuto dell'email breve e chiaro
- Includi le azioni da svolgere (cosa devono fare i destinatari?)
- Includi un link o le istruzioni per accedere al documento
- Testa il template con dati di esempio
- Invia al gruppo giusto (non notificare in eccesso)
- Usa i template per coerenza

❌ **Non Fare:**
- Inviare troppe email (affaticamento da notifiche)
- Includere dati sensibili nelle email
- Inviare a gruppi che non hanno bisogno delle informazioni
- Usare oggetti poco chiari
- Dimenticare di indicare come agire
- Inviare email a singole persone (usa invece il gruppo)

---

## Note sulle Prestazioni

- Ogni email impiega ~1 secondo per essere inviata
- I gruppi numerosi possono richiedere tempo (100 persone = ~100 secondi)
- Non creare loop che inviano migliaia di email
- Monitora la capacità del servizio email
- Valuta il batching se hai molti documenti

---

## Card Correlate

- **ACTION_SEND_EMAIL** - Invia a una singola persona
- **ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP** - Assegna un'attività invece di limitarsi a notificare
- **ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL** - Crea un'attività e notifica
- **STAUS_CHANGE** - Cambia lo stato e notifica

---

## Esempio di Workflow Tipico

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

---

## FAQ

**D: Posso inviare a più gruppi?**
R: crea card separate per ciascun gruppo

**D: Cosa succede se l'email di qualcuno non viene recapitata (bounce)?**
R: l'email viene registrata come non riuscita, l'IT può risolvere il problema

**D: Posso modificare il template email?**
R: contatta il tuo amministratore per modificare i template

**D: Posso inviare in base alle condizioni?**
R: sì! Usa le condizioni "Where" e "And" per controllare quando inviare le email

**D: Come faccio a sapere se l'email è stata ricevuta?**
R: controlla i log delle email in DocBits per lo stato dell'invio
