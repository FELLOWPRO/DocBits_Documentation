# Chiama l'API esterna

***

Aggiungi questa scheda al gruppo **Allora** del Workflow Builder: le azioni che vengono eseguite una volta che le condizioni Quando/E corrispondono:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-it.png" alt="Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

***

## 📌 Informazioni sulla versione

**Versione corrente:** v2 (Ultima e consigliata) **Stato:** ✅ Attivo

**Cronologia versioni:**

* v1 → Chiamata API di base (non più consigliata)
* **v2 → CURRENT** (aggiunto supporto multilingue)

**Cosa è cambiato:** v2 ha aggiunto il supporto per l'internazionalizzazione (i18n) con chiavi di traduzione. La funzionalità rimane identica.

📖 [Cronologia versioni e modifiche](../../release.md) | [Database carte completo](../../cards-overview/export-cards-guide.md)

***

## Scopo

Questa scheda consente di inviare dati a un sito Web o servizio esterno e ricevere informazioni in cambio. Immagina di inviare una domanda a un servizio esterno e ottenere una risposta che puoi utilizzare nel tuo flusso di lavoro.

**Esempio reale:** La tua azienda utilizza un sistema di prezzi su un altro sito web. Questa carta può richiedere automaticamente a quel sistema di prezzi il prezzo corrente di un articolo e inserire tale prezzo nel tuo documento.

***

## Quando utilizzare questa carta

Utilizza questa carta quando hai bisogno di:

* Ottieni informazioni da un servizio esterno (come prezzi, convalida o dati di ricerca)
* Invia le informazioni del documento a un altro sistema per l'elaborazione
* Integrazione con servizi di terze parti
* Recupera automaticamente i dati senza ricerche manuali
* Connetti più sistemi aziendali insieme

**Scenari comuni:**

* Cerca le informazioni sui fornitori da un database
* Ottieni prezzi in tempo reale da un servizio di determinazione dei prezzi
* Convalidare i dati rispetto a un sistema esterno
* Recupera le informazioni di spedizione da un fornitore di servizi logistici

***

## Come funziona

1. **Condition Check**: il flusso di lavoro controlla innanzitutto se le condizioni nelle sezioni "Quando" e "E" sono soddisfatte
2. **Prepare Data**: La scheda raccoglie i parametri che hai configurato
3. **Invia richiesta**: invia i tuoi dati all'API/servizio esterno
4. **Receive Response**: il servizio esterno risponde con i dati
5. **Continua**: il flusso di lavoro utilizza questi dati nelle carte successive

***

## Parametri spiegati

### URL dell'endpoint API

**Cos'è:** L'indirizzo del servizio esterno con cui vuoi comunicare

**Esempio:** `https://api.supplier-system.com/product/pricing`

**Come trovarlo:** Chiedi al tuo team IT o al fornitore di servizi il loro endpoint API

***

### Metodo HTTP

**Cos'è:** Il tipo di richiesta da inviare

**Opzioni:**

* **GET**: Richiedi informazioni (come fare una domanda)
* **POST**: invia nuovi dati
* **PUT**: aggiorna i dati esistenti
* **DELETE**: rimuove i dati

**Più comune:** GET (per recuperare informazioni)

***

### Intestazioni

**Che cos'è:** Istruzioni aggiuntive per il servizio che stai chiamando

**Esempio:**

```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Perché è necessario:** I servizi spesso richiedono l'autenticazione o istruzioni di formato specifiche

***

### Parametri (parametri della query)

**Che cos'è:** Informazioni aggiuntive passate nell'URL

**Esempio:**

```
?supplier_id=12345&currency=USD
```

**Esempio reale:** Se stai chiedendo i prezzi, i parametri potrebbero includere l'ID del fornitore e la valuta

***

### Richiedi dati (corpo)

**Che cos'è:** Le informazioni che stai inviando al servizio

**Esempio:**

```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Se utilizzato:** Quando si utilizzano i metodi POST o PUT

***

## Esempio passo dopo passo

### Scenario: ottieni i prezzi dei fornitori in tempo reale

**Impostazioni:**

1. **Tipo di carta:** Chiama API
2. **API dell'endpoint:** `https://api.suppliers.com/v1/prices`
3. **Metodo:** POST
4. **Intestazioni:** `Authorization: Bearer YOUR-API-KEY`
5.  **Richiedi dati:**

    ```json
    {
      "product_id": "ABC123",
      "quantity": 100
    }
    ```

**Cosa succede:**

1. Il documento arriva con l'ID prodotto: ABC123, Quantità: 100
2. La carta invia la richiesta all'API del fornitore
3. L'API del fornitore risponde con: `{"unit_price": 25.50, "total_price": 2550}`
4. Il flusso di lavoro continua con queste informazioni sui prezzi
5. La carta successiva può utilizzare questi dati per convalidare il prezzo della fattura

***

## Passaggi di configurazione

### 1. Ottieni informazioni sull'API

Contatta il fornitore di servizi esterno e richiedi:

* [ ] URL dell'endpoint API
* [ ] Metodo di autenticazione (chiave API, nome utente/password, OAuth)
* [ ] Parametri richiesti
* [ ] Formato della risposta previsto
* [ ] Limiti tariffari o quote

### 2. Configura la Carta

1. Inserisci l'URL dell'endpoint API
2. Seleziona il metodo HTTP (solitamente GET o POST)
3. Aggiungi intestazioni di autenticazione, se necessario
4. Aggiungi eventuali parametri richiesti
5. Se necessario, formatta i dati della richiesta come JSON

### 3. Testare la carta

1. Utilizzare un documento di prova
2. Esegui il flusso di lavoro
3. Controlla se la risposta è stata ricevuta correttamente
4. Verificare che il formato dei dati corrisponda alle aspettative

***

## Scenari di risposta comuni

### Risposta riuscita (codice di stato 200)

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

✅ I dati sono disponibili per le prossime carte da utilizzare

### Risposta all'errore (codice di stato 404)

```json
{
  "error": "Product not found"
}
```

⚠️ L'API non è riuscita a trovare quello che stai cercando

### Timeout

Il servizio esterno non ha risposto entro il limite di tempo ⚠️ Controlla se il servizio è disponibile o se l'URL dell'endpoint è corretto

***

## Flussi di lavoro di esempio

### Esempio 1: convalida automatica del prezzo

**Scenario:** Convalida i prezzi delle fatture rispetto ai prezzi correnti del fornitore

**Portata:**

1. Il documento arriva con la riga della fattura (Prodotto: A123, Prezzo: € 50)
2. **Chiama API Card** → Chiede al fornitore API: "Qual è il prezzo attuale per A123?"
3. Il fornitore risponde: "€48"
4. **Condition Card** → Controlla se il prezzo della fattura (€50) è entro il 5% del prezzo corrente (€48)
5. **Scheda di approvazione** → Approva se entro la tolleranza

### Esempio 2: ricerca automatica del fornitore

**Scenario:** Ottieni i dati anagrafici del fornitore dal database centrale

**Portata:**

1. La fattura arriva con il codice fornitore: SUPP-789
2. **Chiama API Card** → Chiede al sistema: "Dammi i dettagli per il fornitore SUPP-789"
3. Il sistema risponde con: Nome, Contatto, Termini, ecc.
4. **Imposta Schede Campo** → Compila i campi del documento con questi dati
5. **Esporta tessera** → Esporta con informazioni complete

### Esempio 3: costi di spedizione in tempo reale

**Scenario:** Ottieni il costo di spedizione automatico in base alla destinazione

**Portata:**

1. Il documento ha l'indirizzo di consegna
2. **Chiama la scheda API** → Chiedi al corriere: "Qual è il costo per \[indirizzo]?"
3. Il fornitore risponde indicando i costi di spedizione
4. **Calcola carta** → Aggiungi la spedizione all'importo totale della fattura
5. **Esporta Carta** → Invia con totale aggiornato

***

## Risoluzione dei problemi

### Errore "Timeout connessione".

**Causa:** Il servizio API non risponde

**Soluzioni:**

* [ ] Verifica se il servizio è disponibile (visita il sito)
* [ ] Verificare che l'URL dell'endpoint sia corretto (nessun errore di battitura)
* [ ] Controllare la connessione Internet
* [ ] Contattare il fornitore del servizio
* [ ] Controlla se il servizio ha limiti di tariffa (stai inviando troppe richieste)

### Errore "Non autorizzato" o "403 Proibito".

**Causa:** Autenticazione fallita

**Soluzioni:**

* [ ] Verifica che la chiave API sia corretta
* [ ] Controlla se la tua chiave API è scaduta
* [ ] Assicurarsi che l'intestazione di autenticazione sia formattata correttamente
* [ ] Verifica di disporre delle autorizzazioni per questo endpoint

### "Richiesta errata" o "Errore 400"

**Causa:** Il formato dei dati della richiesta non è corretto

**Soluzioni:**

* [ ] Controlla la sintassi JSON (virgole mancanti, virgolette, ecc.)
* [ ] Verificare che tutti i campi obbligatori siano inclusi
* [ ] Verificare che i nomi dei parametri corrispondano a quanto previsto dal servizio
* [ ] Consultare la documentazione dell'API

### "La risposta non funziona come previsto"

**Soluzioni:**

* [ ] Testare l'API utilizzando uno strumento come Postman
* [ ] Confronta il formato della risposta effettiva con il formato previsto
* [ ] Controlla se la documentazione dell'API è cambiata
* [ ] Verifica che i dati che stai inviando siano corretti

***

## Utilizzo dei dati di risposta

Una volta recuperati i dati dall'API, le carte successive possono utilizzarli:

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

***

## Note sulla sicurezza

⚠️ **Importante:** Non inserire mai nella configurazione della carta informazioni sensibili che potrebbero essere visibili ad altri utenti

* Non codificare le password
* Utilizza le chiavi API in modo sicuro
* Non includere dati personali nei log
* Utilizza endpoint HTTPS (non HTTP)

***

## Suggerimenti e migliori pratiche

✅ **Fai:**

* Prova prima con un piccolo campione di documenti
* Mantieni le chiamate API semplici e mirate
* Aggiungi la gestione degli errori con le schede Condizione
* Monitorare l'utilizzo/i costi dell'API
* Documenta i requisiti API per il tuo team

❌ **Non farlo:**

* Chiama le API per ogni singola richiesta se puoi memorizzare nella cache i dati
* Ignorare i codici di errore di risposta
* Utilizza le API di test in produzione
* Dimentica di aggiungere intestazioni di autenticazione
* Supponiamo che l'API sarà sempre disponibile

***

## Carte correlate

* **ACTION\_HTTPS\_REQUEST** - Richieste HTTPS simili ma più semplici
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Controlla se la chiamata API ha avuto successo
* **ACTION\_SEND\_EMAIL** - Invia dati tramite e-mail anziché tramite API
* **CALL\_API** (versione diversa) - Metodo di chiamata API alternativo

***

## Hai bisogno di aiuto?

* Chiedi al tuo team IT/integrazione la documentazione API
* Utilizza lo strumento Postman per testare prima gli endpoint API
* Controlla il portale di supporto del fornitore di servizi
* Consulta la documentazione dell'API per i formati richiesti
