# Invia richiesta HTTPS

***

Aggiungi questa scheda al gruppo **Allora** del Workflow Builder: le azioni che vengono eseguite una volta che le condizioni Quando/E corrispondono:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-it.png" alt="Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

***

## 📌 Informazioni sulla versione

**Versione corrente:** v2 (Ultima e consigliata) **Stato:** ✅ Attivo

**Cronologia versioni:**

* v1 → Richiesta HTTP semplice (non più consigliata)
* **v2 → CURRENT** (aggiunto supporto multilingue)

**Cosa è cambiato:** v2 ha aggiunto il supporto per l'internazionalizzazione (i18n). La funzionalità principale del webhook/richiesta rimane invariata.

📖 [Cronologia versioni e modifiche](../../release.md) | [Database carte completo](../../cards-overview/export-cards-guide.md)

***

## Scopo

La scheda di richiesta HTTPS usa un URL HTTPS configurato e intestazioni proprie. `call_api` usa un percorso relativo della API DocBits e il contesto dell’utente corrente; il risultato deriva dal testo della risposta. Scegliere in base all’endpoint e al contratto di risposta, non distinguendo tra API semplice e complessa.

## Quando utilizzare questa carta

Utilizza questa carta quando hai bisogno di:

* Invia notifiche webhook a servizi esterni
* Attivare azioni in altri sistemi
* Interrogare un semplice servizio web
* Invia aggiornamenti di stato ad altre applicazioni
* Esegui integrazioni semplici senza requisiti API complessi

***

## Come funziona

1. **Trigger Check**: il sistema controlla se le condizioni "Quando" e "E" sono soddisfatte
2. **Richiesta di creazione**: il sistema prepara la richiesta HTTPS con i tuoi parametri
3. **Invia in modo sicuro**: i dati vengono inviati utilizzando una connessione HTTPS sicura
4. **Ricevi risposta**: il servizio esterno risponde
5. **Continua**: il flusso di lavoro procede con i dati di risposta

***

## Parametri

### URL

L'indirizzo del sito web a cui inviare la richiesta

**Esempio:** `https://webhook.company.com/process`

### Intestazioni

Istruzioni speciali per il destinatario

**Esempio:**

```
Content-Type: application/json
Authorization: Bearer token123
```

### Metodo

* **GET**: Richiedi informazioni
* **POST**: invia i dati
* **PUT**: aggiorna i dati

### Parametri (stringa di query)

Dati aggiunti all'URL

**Esempio:** `?action=approve&user_id=123`

### Richiedi dati

Le informazioni effettive inviate (in formato JSON)

**Esempio:**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## Esempio passo dopo passo

### Scenario: inviare la fattura al sistema contabile

**Configurazione scheda:**

* **URL:** `https://accounting.company.com/invoices/create`
* **Metodo:** POST
* **Intestazioni:** `Authorization: Bearer YOUR-TOKEN`
* **Richiedi dati:**

```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Risposta prevista:**

```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

***

## Casi d'uso comuni

### 1. Notifiche webhook

Invia notifiche in tempo reale ad altri sistemi ogni volta che succede qualcosa in DocFlow

**Esempio:**

* Documento approvato → Invia notifica al sistema di evasione ordini
* Fornitore cambiato → Avvisa il team acquisti tramite webhook Slack/Teams

### 2. Integrazione di sistemi esterni

Connetti DocFlow con altri sistemi aziendali per lo scambio automatico di dati

**Esempio:**

* Dopo che il documento è stato elaborato → Sincronizza con il sistema ERP
* Nuovo fornitore aggiunto → Crea record fornitore nel sistema anagrafico

### 3. Flussi di lavoro di approvazione

Invia il documento al sistema di approvazione esterno e ricevi la decisione

**Esempio:**

* Fattura di valore elevato → Invia alla Finanza per l'approvazione
* Restituire il documento al sistema esterno con decisione

***

## Guida alla configurazione

### Passaggio 1: ottenere informazioni sull'endpoint

Chiedere al sistema ricevente:

* [] URL HTTPS
* [ ] Intestazioni obbligatorie
* [ ] Metodo di autenticazione
* [ ] Formato della richiesta previsto
* [ ] Formato della risposta previsto

### Passaggio 2: configura la carta

1. Inserisci l'URL HTTPS
2. Imposta il metodo HTTP (solitamente POST)
3. Aggiungi l'autenticazione se necessario
4. Formatta i dati della richiesta come JSON
5. Aggiungi eventuali intestazioni personalizzate

### Passaggio 3: prova

Invia una richiesta di prova e verifica la risposta

***

## Gestione della risposta

La tua richiesta HTTPS riceverà una risposta. Risposte comuni:

### Successo (200, 201)

```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Richiesta errata (400)

```json
{
  "error": "Missing required field: invoice_number"
}
```

### Non autorizzato (401)

```json
{
  "error": "Invalid authentication token"
}
```

### Errore del server (500)

Il sistema ricevente ha un problema interno

***

## Risoluzione dei problemi

### "Errore certificato"

**Causa:** Problema relativo al certificato di sicurezza HTTPS

**Soluzione:**

* Verifica che l'URL sia corretto
* Controlla se il certificato del sito web è valido
* Assicurati di utilizzare HTTPS (non HTTP)

### "Connessione rifiutata"

**Causa:** Impossibile connettersi al server

**Soluzione:**

* Verificare che l'URL/indirizzo IP sia corretto
* Controlla se il servizio è in esecuzione
* Controlla le regole del firewall
* Verificare la connettività Internet

### "Nessuna risposta/Timeout"

**Causa:** Il server non risponde entro il limite di tempo

**Soluzione:**

* Controlla se il servizio è disponibile
* Verifica l'URL dell'endpoint
* Controlla se ci sono limiti di tariffa
* Contatta l'amministratore di sistema

### "JSON non valido"

**Causa:** I dati della richiesta non sono corretti

**Soluzione:**

* Controlla le virgole mancanti in JSON
* Verificare che tutte le virgolette siano corrette
* Convalida il formato JSON (utilizza il validatore JSON online)
* Controlla i caratteri speciali

***

## Esempi

### Esempio 1: Invia al servizio Webhook

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

### Esempio 2: aggiornamento del sistema esterno

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

### Esempio 3: interrogare il servizio esterno

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## Differenza dalla scheda "Call API".

La scheda di richiesta HTTPS usa un URL HTTPS configurato e intestazioni proprie. `call_api` usa un percorso relativo della API DocBits e il contesto dell’utente corrente; il risultato deriva dal testo della risposta. Scegliere in base all’endpoint e al contratto di risposta, non distinguendo tra API semplice e complessa.

***

## Considerazioni sulla sicurezza

✅ **Utilizza sempre HTTPS** (connessione sicura)

⚠️ **Mai:**

* Inserisci le password nell'URL
* Esporre le chiavi API nei log
* Includere i dati personali nei parametri
* Utilizza HTTP per i dati sensibili

***

## Migliori pratiche

✅ **Fai:**

* Testare prima con piccole quantità di dati
* Includere la gestione degli errori
* Registra richieste importanti
* Documentare l'integrazione
* Monitorare i guasti

❌ **Non farlo:**

* Chiama ripetutamente lo stesso endpoint se non necessario
* Ignorare gli errori di risposta
* Includere dati sensibili in testo semplice
* Superare i limiti della tariffa del servizio

***

## Carte correlate

* **CALL\_API** - Integrazione API più avanzata
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Controlla se la richiesta è riuscita
* **ACTION\_SEND\_EMAIL** - Invia invece tramite email
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** - Script automatizzati

<!-- workflow-card-complete-example-20261021 action_https_request -->

### Esempio di azione HTTPS

**Configurazione:** Seleziona il metodo `POST`, sostituisci `DEMO_WEBHOOK_URL` con l'endpoint del test autorizzato, aggiungi l'intestazione `Content-Type: application/json` e il corpo `{"document_number":"DEMO-001"}`. Configura l'autenticazione solo come richiesto da quell'endpoint; non copiare mai un vero segreto nella documentazione.

**Risultato previsto e controesempio:** L'azione invia la richiesta configurata quando viene eseguito il percorso del flusso di lavoro. Esaminare la risposta HTTP e ricevere il servizio di test. Un timeout non è una prova che il servizio non abbia fatto nulla e questa azione Then è separata dalla scheda And che controlla lo stato HTTP. Questa richiesta illustrativa non è stata inviata.

Questa è una configurazione di test illustrativa e il risultato atteso; non è stato eseguito. Utilizza dati e destinatari configurati nella tua organizzazione di test.
