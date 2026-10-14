# Call External API

Queste schede vanno nel gruppo **Then** del Generatore di workflow — le azioni eseguite una volta soddisfatte le condizioni When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede vengono aggiunte al gruppo <strong>Then</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

## Scopo
Questa card ti consente di inviare dati a un sito web o servizio esterno e di ricevere informazioni in risposta. Pensala come l'invio di una domanda a un servizio esterno per ottenere una risposta che puoi utilizzare nel tuo workflow.

**Esempio reale:** la tua azienda utilizza un sistema di prezzi su un altro sito web. Questa card può chiedere automaticamente a quel sistema il prezzo corrente di un articolo e riportare tale prezzo nel tuo documento.

---

## Quando Usare Questa Card

Usa questa card quando devi:
- Ottenere informazioni da un servizio esterno (come prezzi, convalida o dati di ricerca)
- Inviare le informazioni di un documento a un altro sistema per l'elaborazione
- Integrarti con servizi di terze parti
- Recuperare automaticamente i dati senza ricerche manuali
- Collegare tra loro più sistemi aziendali

**Scenari comuni:**
- Cercare le informazioni di un fornitore in un database
- Ottenere prezzi in tempo reale da un servizio di prezzi
- Convalidare i dati rispetto a un sistema esterno
- Recuperare le informazioni di spedizione da un fornitore di logistica

---

## Come Funziona

1. **Controllo delle Condizioni**: il workflow verifica innanzitutto se le condizioni nelle sezioni "Where" e "And" sono soddisfatte
2. **Preparazione dei Dati**: la card raccoglie i parametri che hai configurato
3. **Invio della Richiesta**: invia i tuoi dati all'API/servizio esterno
4. **Ricezione della Risposta**: il servizio esterno risponde con i dati
5. **Continuazione**: il workflow utilizza questi dati nelle card successive

---

## Parametri Spiegati

### API Endpoint URL
**Cos'è:** l'indirizzo del servizio esterno con cui vuoi comunicare

**Esempio:** `https://api.supplier-system.com/product/pricing`

**Come trovarlo:** chiedi al tuo team IT o al provider del servizio il loro endpoint API

---

### HTTP Method
**Cos'è:** il tipo di richiesta da inviare

**Opzioni:**
- **GET**: richiedi informazioni (come porre una domanda)
- **POST**: invia nuovi dati
- **PUT**: aggiorna dati esistenti
- **DELETE**: rimuovi dati

**Il più comune:** GET (per recuperare informazioni)

---

### Headers
**Cos'è:** istruzioni aggiuntive per il servizio che stai chiamando

**Esempio:**
```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Perché è necessario:** i servizi spesso richiedono l'autenticazione o istruzioni di formato specifiche

---

### Parameters (Query Parameters)
**Cos'è:** informazioni aggiuntive passate nell'URL

**Esempio:**
```
?supplier_id=12345&currency=USD
```

**Esempio reale:** se stai richiedendo i prezzi, i parametri potrebbero includere l'ID del fornitore e la valuta

---

### Request Data (Body)
**Cos'è:** le informazioni che stai inviando al servizio

**Esempio:**
```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Quando si usa:** quando si utilizzano i metodi POST o PUT

---

## Esempio Passo dopo Passo

### Scenario: Ottenere i Prezzi del Fornitore in Tempo Reale

**Configurazione:**
1. **Card Type:** Call API
2. **API Endpoint:** `https://api.suppliers.com/v1/prices`
3. **Method:** POST
4. **Headers:** `Authorization: Bearer YOUR-API-KEY`
5. **Request Data:**
   ```json
   {
     "product_id": "ABC123",
     "quantity": 100
   }
   ```

**Cosa succede:**
1. Arriva un documento con Product ID: ABC123, Quantity: 100
2. La card invia una richiesta all'API del fornitore
3. L'API del fornitore risponde con: `{"unit_price": 25.50, "total_price": 2550}`
4. Il workflow prosegue con queste informazioni sui prezzi
5. La card successiva può utilizzare questi dati per convalidare il prezzo della fattura

---

## Passaggi di Configurazione

### 1. Ottieni le Informazioni sull'API
Contatta il provider del servizio esterno e richiedi:
- [ ] URL dell'endpoint API
- [ ] Metodo di autenticazione (chiave API, nome utente/password, OAuth)
- [ ] Parametri richiesti
- [ ] Formato di risposta previsto
- [ ] Limiti di frequenza o quote

### 2. Configura la Card
1. Inserisci l'URL dell'endpoint API
2. Seleziona il metodo HTTP (di solito GET o POST)
3. Aggiungi le header di autenticazione se richieste
4. Aggiungi eventuali parametri richiesti
5. Formatta i dati della richiesta come JSON se necessario

### 3. Testa la Card
1. Usa un documento di prova
2. Esegui il workflow
3. Controlla se la risposta viene ricevuta correttamente
4. Verifica che il formato dei dati corrisponda alle aspettative

---

## Scenari di Risposta Comuni

### Risposta Riuscita (Status Code 200)
```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```
✅ I dati sono disponibili per essere utilizzati dalle card successive

### Risposta di Errore (Status Code 404)
```json
{
  "error": "Product not found"
}
```
⚠️ L'API non è riuscita a trovare ciò che stai cercando

### Timeout
Il servizio esterno non ha risposto entro il limite di tempo
⚠️ Controlla se il servizio è disponibile o se l'URL dell'endpoint è corretto

---

## Esempi di Workflow

### Esempio 1: Convalida Automatica dei Prezzi
**Scenario:** convalidare i prezzi della fattura rispetto ai prezzi correnti del fornitore

**Flusso:**
1. Arriva un documento con una voce della fattura (Product: A123, Price: €50)
2. **Call API Card** → Chiede all'API del fornitore: "Qual è il prezzo corrente per A123?"
3. Il fornitore risponde: "€48"
4. **Condition Card** → Verifica se il prezzo della fattura (€50) rientra nel 5% del prezzo corrente (€48)
5. **Approval Card** → Approva se rientra nella tolleranza

### Esempio 2: Ricerca Automatica del Fornitore
**Scenario:** ottenere i dati anagrafici del fornitore da un database centrale

**Flusso:**
1. Arriva una fattura con Supplier Code: SUPP-789
2. **Call API Card** → Chiede al sistema: "Forniscimi i dettagli per il fornitore SUPP-789"
3. Il sistema risponde con: nome, contatto, condizioni, ecc.
4. **Set Field Cards** → Popolano i campi del documento con questi dati
5. **Export Card** → Esporta con informazioni complete

### Esempio 3: Costi di Spedizione in Tempo Reale
**Scenario:** ottenere automaticamente il costo di spedizione in base alla destinazione

**Flusso:**
1. Il documento ha un indirizzo di consegna
2. **Call API Card** → Chiede al fornitore di spedizione: "Qual è il costo per [indirizzo]?"
3. Il fornitore risponde con il costo di spedizione
4. **Calculate Card** → Aggiunge la spedizione all'importo totale della fattura
5. **Export Card** → Invia con il totale aggiornato

---

## Risoluzione dei Problemi

### Errore "Connection Timeout"
**Causa:** il servizio API non risponde

**Soluzioni:**
- [ ] Controlla se il servizio è disponibile (visita il sito web)
- [ ] Verifica che l'URL dell'endpoint sia corretto (senza errori di battitura)
- [ ] Controlla la connessione a Internet
- [ ] Contatta il provider del servizio
- [ ] Verifica se il servizio ha limiti di frequenza (stai inviando troppe richieste)

### Errore "Unauthorized" o "403 Forbidden"
**Causa:** autenticazione non riuscita

**Soluzioni:**
- [ ] Verifica che la tua chiave API sia corretta
- [ ] Controlla se la tua chiave API è scaduta
- [ ] Assicurati che l'header di autenticazione sia formattata correttamente
- [ ] Verifica di avere i permessi per questo endpoint

### Errore "Bad Request" o "400"
**Causa:** il formato dei dati della richiesta è errato

**Soluzioni:**
- [ ] Controlla la sintassi JSON (virgole, virgolette mancanti, ecc.)
- [ ] Verifica che tutti i campi richiesti siano inclusi
- [ ] Controlla che i nomi dei parametri corrispondano a quanto si aspetta il servizio
- [ ] Consulta la documentazione dell'API

### "La risposta non funziona come previsto"
**Soluzioni:**
- [ ] Testa l'API utilizzando uno strumento come Postman
- [ ] Confronta il formato di risposta effettivo con quello previsto
- [ ] Controlla se la documentazione dell'API è cambiata
- [ ] Verifica che i dati che stai inviando siano corretti

---

## Utilizzo dei Dati di Risposta

Una volta ricevuti i dati dall'API, le card successive possono utilizzarli:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

---

## Note sulla Sicurezza

⚠️ **Importante:** non inserire mai informazioni sensibili nella configurazione della card che potrebbero essere visibili ad altri utenti

- Non inserire password direttamente nel codice
- Usa le chiavi API in modo sicuro
- Non includere dati personali nei log
- Usa endpoint HTTPS (non HTTP)

---

## Suggerimenti e Best Practice

✅ **Fai:**
- Testa prima con un piccolo campione di documenti
- Mantieni le chiamate API semplici e mirate
- Aggiungi la gestione degli errori con le Condition card
- Monitora l'utilizzo/i costi dell'API
- Documenta i requisiti dell'API per il tuo team

❌ **Non Fare:**
- Chiamare le API per ogni singola richiesta se puoi memorizzare i dati nella cache
- Ignorare i codici di errore della risposta
- Usare API di test in produzione
- Dimenticare di aggiungere le header di autenticazione
- Presumere che l'API sia sempre disponibile

---

## Card Correlate

- **ACTION_HTTPS_REQUEST** - Richieste HTTPS simili ma più semplici
- **CONDITION_HTTPS_REQUEST_STATUS** - Verifica se la chiamata API è andata a buon fine
- **ACTION_SEND_EMAIL** - Invia dati tramite email invece dell'API
- **CALL_API** (versione diversa) - Metodo alternativo di chiamata API

---

## Hai Bisogno di Aiuto?

- Chiedi al tuo team IT/di integrazione la documentazione dell'API
- Usa lo strumento Postman per testare prima gli endpoint API
- Controlla il portale di supporto del provider del servizio
- Consulta la documentazione dell'API per i formati richiesti
