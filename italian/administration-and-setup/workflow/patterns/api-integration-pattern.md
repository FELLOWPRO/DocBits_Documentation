# Modello di integrazione API

**Tipo di pattern:** Integrazione **Complessità:** Media **Configurazione stimata:** 45-60 minuti **Casi d'uso comuni:** Recupero di dati esterni, validazione dei prezzi, lookup dei dati master

***

Costruisci questo pattern nel **Costruttore di flussi di lavoro** (Workflow Dashboard → Workflow List → Add Workflow). Clicca **Aggiungi carta** per aprire la libreria delle card e scegli le card usate da questo pattern — `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` e `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`:

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-9a74b1360332-it.png" alt="Schede disponibili nella categoria selezionata. Configurare i campi prima dell’uso. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Schede disponibili nella categoria selezionata. Configurare i campi prima dell’uso. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

***

## Panoramica del pattern

Questo pattern mostra come integrare DocBits con API esterne per recuperare, validare e memorizzare dati da sistemi esterni. È uno dei pattern di workflow più comuni per collegare DocBits a sistemi di pricing, servizi di validazione, sistemi ERP e altre fonti di dati esterne.

**Cosa fa questo pattern:**

1. Chiama un'API esterna per recuperare dati
2. Valida la risposta dell'API
3. Memorizza i dati della risposta nei campi del documento
4. Prende decisioni in base ai dati recuperati
5. Instrada i documenti di conseguenza

***

## Quando usare questo pattern

Usa questo pattern quando devi:

* ✅ Recuperare prezzi in tempo reale da sistemi esterni
* ✅ Validare le informazioni dei fornitori rispetto a un database master
* ✅ Cercare i dettagli dei prodotti dai sistemi di catalogo
* ✅ Ottenere i tassi di cambio dai servizi valutari
* ✅ Verificare gli indirizzi con servizi di geocodifica
* ✅ Controllare i livelli di inventario dai sistemi di magazzino
* ✅ Validare le aliquote fiscali dai servizi fiscali

**Non usare questo pattern quando:**

* ❌ I dati sono già nei dati master di DocBits (usa invece il lookup dei dati master)
* ❌ Il sistema esterno non ha un'API (usa invece il pattern DocOperator Script)
* ❌ I dati non cambiano frequentemente (considera l'importazione manuale)

***

## Esempio completo di flusso di lavoro

### Scenario: Validare il prezzo della fattura rispetto a un'API di pricing corrente

**Requisito aziendale:**

* Il fornitore invia una fattura
* La fattura mostra un prezzo unitario di €52,00
* Dobbiamo verificare che corrisponda al prezzo corrente del fornitore
* Se il prezzo varia di oltre il 5%, inoltra per la revisione

**Scheda di flusso di lavoro utilizzato:**

1. CALL\_API - Recupera il prezzo corrente dall'API del fornitore
2. CONDITION\_HTTPS\_REQUEST\_STATUS - Verifica se la chiamata API è andata a buon fine
3. ACTION\_SET\_FIELD\_TO\_TEXT - Memorizza il prezzo dell'API in un campo del documento
4. CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES - Confronta il prezzo della fattura con il prezzo dell'API
5. ACTION\_ASSIGN\_TO\_USER - Instrada in base al risultato del confronto
6. tasks\_create - Crea un'attività di revisione se necessaria

***

## Implementazione passo passo

### Passo 1: Chiama l'API esterna

**Carta:** CALL\_API o ACTION\_CALL\_EXTERNAL\_API

**Configurazione:**

```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**Risposta attesa:**

```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**Riferimento alla guida:** [Call API Guide](../then/action/call-api-guide.md)

***

### Passo 2: Valida la risposta dell'API

**Carta:** CONDITION\_HTTPS\_REQUEST\_STATUS

**Configurazione:**

```
Operator: IS EQUAL TO
Status Code: 200
```

**Logica:**

```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**Riferimento alla guida:** [Condition Cards Guide - HTTP Status](../and/condition-cards-complete-guide.md)

***

### Passo 3: Memorizza la risposta dell'API nei campi del documento

**Carta:** ACTION\_SET\_FIELD\_TO\_TEXT (o equivalente impostatore di campo)

**Configurazione:**

**Campo 1: Current\_API\_Price**

```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**Campo 2: API\_Price\_Valid\_Until**

```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**Campo 3: API\_Discount\_Available**

```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**Risultato:** I dati dell'API sono ora memorizzati nei campi del documento per un uso successivo

**Riferimento alla guida:** [Field Manipulation Guide - API Data Storage](../then/document-field/field-manipulation-guide.md)

***

### Passo 4: Confronta il prezzo della fattura con il prezzo dell'API

**Carta:** CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

**Configurazione:**

```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**Calcolo:**

```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**Riferimento alla guida:** [Guida alle Carte Condizioni - Confronto Campi](../and/condition-cards-complete-guide.md)

***

### Passo 5: Instrada in base al risultato della validazione

**Scenario A: Prezzo entro la tolleranza (Pass)**

**Carta:**

* ACTION\_SET\_FIELD\_TO\_TEXT
  * Imposta il campo "Price\_Validation\_Status" = "PASS"
  * Imposta il campo "Price\_Variance\_Percent" = "4%"
* ACTION\_APPROVE\_DOCUMENT
  * Approva automaticamente il documento

**Scenario B: Prezzo oltre la tolleranza (Fail)**

**Carta:**

* ACTION\_SET\_FIELD\_TO\_TEXT
  * Imposta il campo "Price\_Validation\_Status" = "FAIL"
  * Imposta il campo "Price\_Variance\_Percent" = "12%" (esempio)
* tasks\_create
  * Titolo del task: "Review Price Variance - \{{DOCUMENT\_NUMBER\}}"
  * Descrizione dell'attività: "Il prezzo della fattura (€\{{Invoice\_Unit\_Price\}}) supera il prezzo API (€\{{Current\_API\_Price\}}) di \{{Price\_Variance\_Percent\}}"
  * Priorità: Alta
* ACTION\_ASSIGN\_TO\_USER
  * Assegna a: Procurement Manager
* ACTION\_SEND\_EMAIL\_TO\_GROUPS
  * Invia notifica al team Approvvigionamenti

**Riferimenti alle guide:**

* [Guida all'assegnazione](../then/assignee/assignment-user-guide.md)
* [Guida all'assegnazione delle attività](../then/task/task-assignment-guide.md)
* [Invia guida via e-mail](../then/action/send-email-groups-guide.md)

***

## Diagramma completo del flusso di lavoro

```
DOCUMENT ARRIVES (Invoice with Product ABC123, Price €52)
│
├─ STEP 1: Call Pricing API
│  Card: CALL_API
│  Request: Get current price for ABC123
│  │
│  ├─ SUCCESS (200) ✅
│  │  Response: {"unit_price": 50.00}
│  │  │
│  │  ├─ STEP 2: Check API Status
│  │  │  Card: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Result: 200 = Success
│  │  │  │
│  │  │  ├─ STEP 3: Store API Data
│  │  │  │  Card: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Action: Store €50 in "Current_API_Price" field
│  │  │  │  │
│  │  │  │  ├─ STEP 4: Compare Prices
│  │  │  │  │  Card: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Calculate: Variance = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF Variance ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Set Status Field: "PASS"
│  │  │  │  │  │  └─ Auto-Approve Document
│  │  │  │  │  │     → END (Document Approved)
│  │  │  │  │  │
│  │  │  │  │  └─ IF Variance > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Set Status Field: "FAIL"
│  │  │  │  │     ├─ Create Review Task
│  │  │  │  │     ├─ Assign to Procurement Manager
│  │  │  │  │     └─ Send Email Notification
│  │  │  │  │        → END (Pending Review)
│  │  │  │  │
│  │  │  │  └─ [Field storage complete]
│  │  │  │
│  │  │  └─ [Status check complete]
│  │  │
│  │  └─ [API data retrieved]
│  │
│  └─ ERROR (Non-200) ❌
│     │
│     ├─ Set Error Status
│     ├─ Create "API Error" Task
│     ├─ Assign to IT Support
│     └─ Send Email to Admin
│        → END (API Error - Manual Review)
```

***

## Modelli di configurazione

### Modello 1: Semplice richiesta GET (Lookup)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

**Uso:** Semplice lookup di dati per ID

***

### Modello 2: Richiesta POST con corpo (Validazione)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**Uso:** Invia i dati del documento per la validazione

***

### Modello 3: Richiesta complessa con dati annidati

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**Uso:** Elaborazione complessa di documenti con dati tabellari

***

## Gestione degli errori

### Errori comuni e soluzioni

#### Errore 1: Timeout della connessione

**Sintomi:**

* L'API non risponde
* Il workflow rimane bloccato in attesa

**Soluzione:**

```
1. Check API endpoint URL (typo?)
2. Verify network connectivity
3. Check API service status
4. Implement timeout handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Create "API Timeout" task
     → Assign to IT Support
     → Send email notification
     → Use fallback value (if available)
```

#### Errore 2: 401 Non autorizzato

**Sintomi:**

* L'API restituisce lo stato 401
* Autenticazione fallita

**Soluzione:**

```
1. Verify API key is correct
2. Check if API key expired
3. Ensure Authorization header formatted correctly
4. Implement auth error handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Create "API Auth Failed" task
     → Assign to Admin
     → Log error details
     → Stop workflow execution
```

#### Errore 3: Formato di risposta non valido

**Sintomi:**

* Risposta ricevuta ma non analizzabile
* Campi attesi mancanti

**Soluzione:**

```
1. Verify API documentation
2. Check response structure matches expectations
3. Implement response validation:

   IF API_RESPONSE:data.unit_price IS NULL:
     → Set default value
     → Create "Invalid Response" task
     → Log response for debugging
```

**Riferimento alla guida:** [Risoluzione dei problemi delle chiamate API](../then/action/call-api-guide.md)

***

## Varianti avanzate

### Variante 1: Concatenamento di più API

**Scenario:** Servono dati da più API

```
Step 1: Call Supplier API → Get Supplier Details
Step 2: Call Product API → Get Product Info (using Supplier ID from Step 1)
Step 3: Call Pricing API → Get Price (using Product ID from Step 2)
Step 4: Validate & Store all data
```

***

### Variante 2: Chiamate API condizionali

**Scenario:** Chiamare l'API solo in determinate condizioni

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

***

### Variante 3: Caching delle risposte API

**Scenario:** Ridurre le chiamate API memorizzando in cache le risposte

```
1. Check if "API_Last_Called" date is today
2. IF Yes:
     → Use cached value from "Cached_API_Price" field
3. IF No:
     → Call API
     → Store response in "Cached_API_Price"
     → Set "API_Last_Called" to today
```

***

## Considerazioni sulle prestazioni

### Best practice

✅ **Cosa fare:**

* Memorizzare in cache le risposte API quando possibile
* Usare le impostazioni di timeout (30-60 secondi)
* Implementare la logica di retry per i guasti temporanei
* Registrare le chiamate API per il debug
* Monitorare l'utilizzo/i costi delle API
* Eseguire prima dei test con documenti di esempio

❌ **Cosa non fare:**

* Chiamare le API in modo sincrono per ogni documento (considerare l'elaborazione batch)
* Ignorare gli errori di risposta
* Codificare in modo fisso le credenziali nel workflow
* Effettuare chiamate API non necessarie
* Dimenticare di gestire i timeout

***

## Checklist di test

Prima di distribuire questo pattern:

* [ ] Testa la chiamata API con dati validi
* [ ] Testa la chiamata API con dati non validi
* [ ] Testa lo scenario di timeout (cosa succede se l'API è lenta?)
* [ ] Testa il fallimento dell'autenticazione
* [ ] Testa il formato di risposta non valido
* [ ] Testa la memorizzazione dei campi (i dati sono memorizzati correttamente?)
* [ ] Testa la logica di confronto (calcolo corretto?)
* [ ] Testa l'instradamento (i documenti vanno al posto giusto?)
* [ ] Testa la gestione degli errori (gli errori sono gestiti correttamente?)
* [ ] Testa con volumi elevati (prestazioni accettabili?)

***

## Esempi reali

### Esempio 1: Lookup del tasso di cambio valutario

**API:** https://api.exchangerate-api.com/v4/latest/USD

**Flusso di lavoro:**

1. Estrai la valuta della fattura: "GBP"
2. Chiama l'API dei tassi di cambio
3. Ottieni il tasso di cambio GBP→EUR
4. Calcola l'equivalente in EUR
5. Memorizza nel campo "Amount\_EUR"
6. Continua l'elaborazione con l'importo in EUR

***

### Esempio 2: Controllo del credito del fornitore

**API:** Servizio interno di controllo del credito

**Flusso di lavoro:**

1. Estrai il codice del fornitore
2. Chiama l'API di controllo del credito
3. Ottieni lo stato del credito: "APPROVED" o "BLOCKED"
4. SE BLOCCATO:
   * Interrompi l'elaborazione
   * Crea un compito urgente
   * Notifica il team finanziario
5. SE APPROVATO:
   * Continua il flusso di lavoro normale

***

### Esempio 3: Arricchimento dei dati master del prodotto

**API:** Servizio di catalogo prodotti

**Flusso di lavoro:**

1. Estrai il codice del prodotto dalla fattura
2. Chiama l'API del prodotto
3. Ottieni: nome del prodotto, categoria, conto contabile
4. Memorizza nei campi del documento
5. Usa per la contabilizzazione automatica

***

## Pattern correlati

### Questo pattern funziona bene con:

* [**Modello di trasformazione dei dati**](data-transformation-pattern.md) - Trasforma i dati della risposta API
* [**Modello logico decisionale**](decision-logic-pattern.md) - Instrada in base ai dati dell'API
* [**Modello di gestione delle attività**](task-management-pattern.md) - Crea task per gli errori API
* [**Modello di corrispondenza PO**](po-matching-pattern.md) - Combina il pricing dell'API con la validazione del PO

***

## Guide correlate

### Prerequisiti

* [Call API Guide](../then/action/call-api-guide.md) - Documentazione della card API
* [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Logica delle condizioni
* [Guida alla manipolazione del campo](../then/document-field/field-manipulation-guide.md) - Operazioni sui campi

### Card correlate

* **CALL\_API** - [Chiama Guida API](../then/action/call-api-guide.md)
* **ACTION\_HTTPS\_REQUEST** - [Guida alla richiesta HTTPS](../then/action/https-request-guide.md)
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - [Guida alle carte condizione](../and/condition-cards-complete-guide.md)
* **ACTION\_SET\_FIELD\_TO\_TEXT** - [Guida alla manipolazione del campo](../then/document-field/field-manipulation-guide.md)
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - [Guida alle carte condizione](../and/condition-cards-complete-guide.md)

### Prossimi passi

* Risolvi gli errori API: [Gestione degli errori](api-integration-pattern.md#gestione-degli-errori) sopra
* Aggiungi la creazione di task: [Task Management Pattern](task-management-pattern.md)
* Trasforma i dati: [Data Transformation Pattern](data-transformation-pattern.md)

***

## Supporto e risorse

**Hai bisogno di aiuto?**

* Esamina il [Risoluzione problemi API chiamata](../then/action/call-api-guide.md)
* Consulta i [Codici di risposta dell'API](../then/action/call-api-guide.md)
* Testa prima l'API con Postman
* Contatta il supporto del provider dell'API

**Risposta:**

* Segnala i problemi del pattern a: docs@docbits.com
* Suggerisci miglioramenti
* Condividi i tuoi casi d'uso

***

**Versione del pattern:** 1.0 **Ultimo aggiornamento:** 23 ottobre 2025 **Difficoltà:** Media **Tempo stimato:** 45-60 minuti **Tasso di successo:** Alto (quando l'API è stabile)
