# Esegui prompt DocOperator (script di automazione)

***

Aggiungi questa scheda al gruppo **Allora** del Workflow Builder: le azioni che vengono eseguite una volta che le condizioni Quando/E corrispondono:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-it.png" alt="Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

***

## 📌 Informazioni sulla versione

**Versione corrente:** v3 (Ultima e consigliata) **Stato:** ✅ Attivo

**Cronologia versioni:**

* v2 → Implementazione originale di DocOperator
* **v3 → CURRENT** (aggiunto parametro di controllo dell'esecuzione)
* v4 → Deprecato (funzionalità ripristinate)

**Cosa è cambiato:** v3 ha aggiunto il parametro opzionale "Esegui il prompt" per un maggiore controllo. v4 ha tentato di ripristinare questo problema ma è stato deprecato.

📖 [Cronologia versioni e modifiche](../../release.md) | [Database carte completo](../../cards-overview/export-cards-guide.md)

***

## Scopo

Questa scheda esegue un'azione o uno script automatizzato del browser utilizzando DocOperator. Consideralo come un robot in grado di interagire con siti Web o sistemi esattamente come farebbe un essere umano: facendo clic su pulsanti, compilando moduli, estraendo dati, ecc.

**Esempio reale:** La tua azienda utilizza un sistema di acquisto basato sul web. Questa carta può accedere automaticamente, cercare un prodotto, verificare la disponibilità e ottenere il prezzo corrente, il tutto senza che nessuno lo faccia manualmente.

***

## Quando utilizzare questa carta

Utilizza questa carta quando hai bisogno di:

* Automatizza le attività sui siti Web che non dispongono di API
* Estrarre dati da pagine web
* Compila i moduli automaticamente
* Accedi ai sistemi e recupera le informazioni
* Automatizza le attività manuali ripetitive
* Interagisci con i sistemi legacy che non sono integrati

**Scenari comuni:**

* Accedi ai siti Web dei fornitori e ottieni l'inventario in tempo reale
* Compila automaticamente moduli su sistemi esterni
* Estrai dati da pagine web che non offrono API
* Controlla lo stato della consegna sui siti dei corrieri
* Ottieni prezzi da sistemi senza accesso API

***

## Come funziona

1. **Carta attivata**: il flusso di lavoro raggiunge questa carta e le condizioni sono soddisfatte
2. **Viene avviato lo script**: il bot DocOperator inizia a eseguire lo script di automazione
3. **Azioni bot**: il bot esegue azioni come fare clic, digitare, scorrere, estrarre
4. **Estrazione dati**: il bot raccoglie informazioni dalle pagine web
5. **Return Data**: i dati tornano a DocFlow per essere utilizzati nelle carte successive
6. **Gestione del timeout**: se lo script impiega troppo tempo, si ferma e restituisce ciò che ha

***

## Parametri spiegati

### Prompt/script DocOperator

Lo script di automazione che dice a DocOperator esattamente cosa fare

**Esempio (inglese semplice):**

```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variabili

Dati che vuoi passare nello script

**Esempio:**

```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Queste variabili possono essere utilizzate nello script come:

```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Passi massimi

Quante azioni può eseguire il bot

**Valori tipici:**

* Compito semplice (come ottenere un prezzo): 10-20 passaggi
* Complessità media (compila modulo + estratto): 20-50 passaggi
* Flusso di lavoro complesso (accesso + ricerca + convalida): 50-100 passaggi

**Perché è importante:** Impedisce cicli infiniti e script con esecuzione molto lunga

### Numero massimo di tentativi

Se il bot fallisce un'azione, quante volte dovrebbe riprovare?

**Esempi:**

* 1: Prova una volta, se fallisce vai avanti
* 3: Prova 3 volte prima di arrenderti
* 5: Molto persistente: prova 5 volte

***

## Esempio passo dopo passo

### Scenario: ottenere i prezzi del fornitore dal sito Web

**Definizione dello script:**

```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Variabili passate:**

```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Script che utilizza variabili:**

```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Risultato atteso:**

```
price: 45.50
quantity_available: 500
```

***

## Tipi di azioni che DocOperator può eseguire

### Navigazione

* Vai all'URL
* Fare clic sui collegamenti
* Premere i pulsanti
* Scorri la pagina

### Compilazione moduli

* Digita il testo nei campi
* Seleziona le opzioni a discesa
* Seleziona/deseleziona le caselle
* Fare clic sui pulsanti

### Estrazione dati

* Leggere il testo dalla pagina
* Estrai numeri
* Ottieni i dati della tabella
* Copiare le informazioni

### In attesa

* Attendi il caricamento della pagina
* Attendi che gli elementi vengano visualizzati
* Attendi il contenuto dinamico

### Logica condizionale

* Se esiste qualcosa, fai così
* Se il testo corrisponde, allora...
* Conta i risultati e agisci di conseguenza

***

## Casi d'uso comuni

### 1. Ottieni prezzi in tempo reale

**Scenario:** Il fornitore non ha API ma il sito web mostra i prezzi

**Sceneggiatura:**

```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Controlla la disponibilità dell'inventario

**Scenario:** È necessario sapere se il fornitore ha scorte

**Sceneggiatura:**

```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Invio automatico dei moduli

**Scenario:** Necessità di compilare un modulo su un sito esterno

**Sceneggiatura:**

```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Verifica dell'immissione dei dati

**Scenario:** Verifica la corrispondenza dei dati su due sistemi diversi

**Sceneggiatura:**

```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

***

## Passaggi di configurazione

### Passaggio 1: crea la sceneggiatura

1. Definisci cosa vuoi realizzare
2. Suddividilo in piccoli passi
3. Scrivi chiaramente ogni passaggio
4. Prova prima manualmente (apri il sito web, fallo da solo)
5. Documenta esattamente cosa fai clic, dove scrivi, cosa estrai

### Passaggio 2: identificare le variabili

1. Quali dati cambieranno tra i documenti?
2. Cosa dovrebbe essere passato nello script?
3. Definire i nomi delle variabili
4. Specificare dove vengono utilizzate le variabili nello script

### Passaggio 3: impostare i parametri

* **Passi massimi**: basato sulla complessità dello script
* **Numero massimo di tentativi**: quanto dovrebbe essere persistente il bot?
* **Timeout**: quanto tempo deve attendere per le pagine?

### Passaggio 4: prova

1. Testare con dati campione
2. Verificare che il bot possa accedere al sito Web
3. Verificare che l'estrazione sia corretta
4. Controlla se le variabili funzionano correttamente

***

## Suggerimenti per la scrittura di script

### Linguaggio chiaro

✅ **Fai:**

```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Non farlo:**

```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Selettori specifici

✅ **Fai:**

```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Non farlo:**

```
Click somewhere
Type in a field
```

### Gestione degli errori

✅ **Fai:**

```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Non farlo:**

```
Click "Next" (assumes it's always there)
```

***

## Risoluzione dei problemi

### "Script scaduto"

**Causa:** Il completamento dello script ha richiesto troppo tempo

**Soluzioni:**

* [ ] Ridurre il numero di azioni
* [ ] Aumenta il valore "Passi massimi".
* [ ] Ottimizza lo script per un'esecuzione più rapida
* [ ] Semplifica ciò che stai cercando di estrarre

### "Elemento non trovato"

**Causa:** DocOperator non è riuscito a trovare il pulsante/campo specificato

**Soluzioni:**

* [ ] Verificare che il nome del pulsante/campo sia esattamente corretto
* [ ] Controlla se il layout del sito web è cambiato
* [ ] Aggiungere il tempo di attesa prima di fare clic
* [ ] Controlla se il pulsante viene visualizzato solo in determinate condizioni

### "Accesso non riuscito"

**Causa:** Autenticazione fallita

**Soluzioni:**

* [ ] Verificare che nome utente/password siano corretti
* [ ] Controlla se la password contiene caratteri speciali
* [ ] Verifica che l'account non sia bloccato
* [ ] Controlla se il processo di accesso è cambiato

### "Dati non estratti correttamente"

**Causa:** Lo script è stato eseguito ma ha estratto informazioni errate

**Soluzioni:**

* [ ] Verificare che sia stato selezionato il campo corretto
* [ ] Controlla se i dati si trovano nella posizione prevista
* [ ] Testare manualmente la logica di estrazione
* [ ] Aggiungi passaggi di debug per verificare cosa c'è nella pagina

### "Lo script viene eseguito lentamente"

**Causa:** Troppi passaggi o sito web lento

**Soluzioni:**

* [ ] Rimuovere i passaggi non necessari
* [ ] Ottimizza i tempi di attesa
* [ ] Controllare la connessione Internet
* [ ] Considerare se esiste un'alternativa API

***

## Migliori pratiche

✅ **Fai:**

* Testare accuratamente gli script prima della distribuzione
* Mantieni gli script semplici e mirati
* Aggiungi commenti che spiegano ogni passaggio
* Utilizza nomi di variabili significativi
* Monitorare le prestazioni dello script
* Avere un fallback per quando gli script falliscono

❌ **Non farlo:**

* Crea script estremamente lunghi (>100 passaggi)
* Inserisci le password sensibili nei registri
* Affidarsi alle coordinate esatte (i siti web cambiano)
* Crea loop senza condizioni di uscita
* Ignora i messaggi di errore

***

## Suggerimenti sulle prestazioni

* **Rimuovi i passaggi inutilizzati** - Ogni passaggio richiede tempo
* **Combina azioni simili** - Clic correlati al gruppo
* **Ottimizza le attese** - Utilizza solo i ritardi necessari
* **Cache data** - Non estrarre gli stessi dati due volte
* **Elaborazione parallela** - Esegui più script, se possibile

***

## Considerazioni sulla sicurezza

⚠️ **Importante:**

* Non memorizzare le password in DocFlow
* Utilizza metodi sicuri per trasferire le credenziali
* Non registrare dati sensibili
* Monitora ciò che viene estratto
* Assicurati che l'attività del bot sia registrata e verificabile

***

## Esempio di variabili

### Variabili disponibili che puoi utilizzare:

```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script che utilizza variabili:

```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

***

## Confronto: quando utilizzare DocOperator rispetto all'API

| Situazione              | Utilizzare DocOperator | Utilizza l'API     |
| ---------------------- | --------------- | ----------- |
| Il sito web ha un'API        | ❌No            | ✅ Sì       |
| Il sito web è interattivo | ✅ Sì           | ❌No        |
| Richiede l'accesso         | ✅ Sì           | Dipende     |
| Necessario molto velocemente       | ❌No            | ✅ Sì       |
| Flusso di lavoro complesso       | ✅ Sì           | ❌Forse no |
| I dati cambiano ogni giorno     | ✅ Sì           | ✅ Sì       |

***

## Carte correlate

* **CALL\_API** - Da utilizzare invece quando l'API è disponibile
* **ACTION\_HTTPS\_REQUEST** - Richieste più semplici
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Utilizza i dati estratti
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Controlla lo stato della richiesta
