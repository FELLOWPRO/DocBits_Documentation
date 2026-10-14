# Send HTTPS Request

Queste schede vanno nel gruppo **Then** del Generatore di workflow — le azioni eseguite una volta soddisfatte le condizioni When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede vengono aggiunte al gruppo <strong>Then</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

## Scopo
Questa card invia un messaggio sicuro a un sito web o servizio e può ricevere una risposta. È più semplice della card "Call API" ed è utile per integrazioni rapide.

**Esempio reale:** invia i dati di una fattura al tuo sistema di contabilità, oppure chiedi a un sistema esterno se un dipendente è autorizzato a elaborare questo acquisto.

---

## Quando Usare Questa Card

Usa questa card quando devi:
- Inviare notifiche webhook a servizi esterni
- Attivare azioni in altri sistemi
- Interrogare un semplice servizio web
- Inviare aggiornamenti di stato ad altre applicazioni
- Eseguire integrazioni semplici senza requisiti API complessi

---

## Come Funziona

1. **Controllo del Trigger**: il sistema verifica se le condizioni "Where" e "And" sono soddisfatte
2. **Costruzione della Richiesta**: il sistema prepara la richiesta HTTPS con i tuoi parametri
3. **Invio Sicuro**: i dati vengono inviati utilizzando una connessione HTTPS sicura
4. **Ricezione della Risposta**: il servizio esterno risponde
5. **Continuazione**: il workflow prosegue con i dati della risposta

---

## Parametri

### URL
L'indirizzo del sito web a cui inviare la richiesta

**Esempio:** `https://webhook.company.com/process`

### Headers
Istruzioni speciali per il destinatario

**Esempio:**
```
Content-Type: application/json
Authorization: Bearer token123
```

### Method
- **GET**: richiedi informazioni
- **POST**: invia dati
- **PUT**: aggiorna dati

### Parameters (Query String)
Dati aggiunti all'URL

**Esempio:** `?action=approve&user_id=123`

### Request Data
Le informazioni effettive che vengono inviate (in formato JSON)

**Esempio:**
```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

---

## Esempio Passo dopo Passo

### Scenario: Inviare una Fattura al Sistema di Contabilità

**Configurazione della Card:**
- **URL:** `https://accounting.company.com/invoices/create`
- **Method:** POST
- **Headers:** `Authorization: Bearer YOUR-TOKEN`
- **Request Data:**
```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Risposta Attesa:**
```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

---

## Casi d'Uso Comuni

### 1. Notifiche Webhook
Invia notifiche in tempo reale ad altri sistemi ogni volta che accade qualcosa in DocFlow

**Esempio:**
- Documento approvato → Invia una notifica al sistema di evasione
- Fornitore modificato → Notifica il team di acquisto tramite un webhook Slack/Teams

### 2. Integrazione con Sistemi Esterni
Collega DocFlow con altri sistemi aziendali per lo scambio automatico di dati

**Esempio:**
- Dopo l'elaborazione del documento → Sincronizza con il sistema ERP
- Nuovo fornitore aggiunto → Crea un record fornitore nel sistema di dati anagrafici

### 3. Workflow di Approvazione
Invia il documento a un sistema di approvazione esterno e ricevi la decisione

**Esempio:**
- Fattura di alto valore → Invia all'ufficio finanziario per l'approvazione
- Restituisci il documento al sistema esterno con la decisione

---

## Guida alla Configurazione

### Passaggio 1: Ottieni le Informazioni sull'Endpoint
Richiedi al sistema ricevente:
- [ ] URL HTTPS
- [ ] Header richieste
- [ ] Metodo di autenticazione
- [ ] Formato di richiesta previsto
- [ ] Formato di risposta previsto

### Passaggio 2: Configura la Card
1. Inserisci l'URL HTTPS
2. Imposta il metodo HTTP (di solito POST)
3. Aggiungi l'autenticazione se richiesta
4. Formatta i dati della richiesta come JSON
5. Aggiungi eventuali header personalizzate

### Passaggio 3: Testa
Invia una richiesta di prova e verifica la risposta

---

## Gestione della Risposta

La tua richiesta HTTPS riceverà una risposta. Risposte comuni:

### Successo (200, 201)
```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Bad Request (400)
```json
{
  "error": "Missing required field: invoice_number"
}
```

### Unauthorized (401)
```json
{
  "error": "Invalid authentication token"
}
```

### Server Error (500)
Il sistema ricevente ha un problema interno

---

## Risoluzione dei Problemi

### "Certificate Error"
**Causa:** problema con il certificato di sicurezza HTTPS

**Soluzione:**
- Verifica che l'URL sia corretto
- Controlla se il certificato del sito web è valido
- Assicurati di utilizzare HTTPS (non HTTP)

### "Connection Refused"
**Causa:** impossibile connettersi al server

**Soluzione:**
- Verifica che l'URL/indirizzo IP sia corretto
- Controlla se il servizio è in esecuzione
- Controlla le regole del firewall
- Verifica la connettività a Internet

### "No Response / Timeout"
**Causa:** il server non risponde entro il limite di tempo

**Soluzione:**
- Controlla se il servizio è disponibile
- Verifica l'URL dell'endpoint
- Controlla se sono presenti limiti di frequenza (rate limit)
- Contatta l'amministratore di sistema

### "Invalid JSON"
**Causa:** i dati della richiesta sono malformati

**Soluzione:**
- Controlla la mancanza di virgole nel JSON
- Verifica che tutte le virgolette siano corrette
- Convalida il formato JSON (usa un validatore JSON online)
- Controlla la presenza di caratteri speciali

---

## Esempi

### Esempio 1: Inviare a un Servizio Webhook
```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Esempio 2: Aggiornare un Sistema Esterno
```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Esempio 3: Interrogare un Servizio Esterno
```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

---

## Differenza dalla Card "Call API"

| Caratteristica | HTTPS Request | Call API |
|---------|---------------|----------|
| Semplicità | Semplice | Più complessa |
| Parametri | Di base | Avanzati |
| Gestione degli Errori | Di base | Dettagliata |
| Usare per | Integrazioni rapide | API complesse |
| Ideale per | Webhook | API professionali |

---

## Considerazioni sulla Sicurezza

✅ **Usa sempre HTTPS** (connessione sicura)

⚠️ **Mai:**
- Inserire password nell'URL
- Esporre le chiavi API nei log
- Includere dati personali nei parametri
- Usare HTTP per dati sensibili

---

## Best Practice

✅ **Fai:**
- Testa prima con piccole quantità di dati
- Includi la gestione degli errori
- Registra nei log le richieste importanti
- Documenta l'integrazione
- Monitora gli errori

❌ **Non Fare:**
- Chiamare ripetutamente lo stesso endpoint se non necessario
- Ignorare gli errori di risposta
- Includere dati sensibili in testo semplice
- Superare i limiti di frequenza del servizio

---

## Card Correlate

- **CALL_API** - Integrazione API più avanzata
- **CONDITION_HTTPS_REQUEST_STATUS** - Verifica se la richiesta è andata a buon fine
- **ACTION_SEND_EMAIL** - Invia invece tramite email
- **ACTION_RUN_DOCOPERATOR_SCRIPT** - Script automatizzati
