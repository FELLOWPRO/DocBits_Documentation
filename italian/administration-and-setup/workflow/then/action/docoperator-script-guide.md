# Run DocOperator Prompt (Automation Script)

Queste schede vanno nel gruppo **Then** del Generatore di workflow — le azioni eseguite una volta soddisfatte le condizioni When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede vengono aggiunte al gruppo <strong>Then</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

## Scopo
Questa card esegue un'azione automatizzata del browser o uno script utilizzando DocOperator. Pensalo come un robot in grado di interagire con siti web o sistemi esattamente come farebbe un essere umano: fare clic sui pulsanti, compilare moduli, estrarre dati, ecc.

**Esempio reale:** la tua azienda utilizza un sistema di acquisti basato sul web. Questa card può accedere automaticamente, cercare un prodotto, verificarne la disponibilità e ottenere il prezzo corrente, il tutto senza che nessuno lo faccia manualmente.

---

## Quando Usare Questa Card

Usa questa card quando devi:
- Automatizzare attività su siti web privi di API
- Estrarre dati dalle pagine web
- Compilare automaticamente i moduli
- Accedere ai sistemi e recuperare informazioni
- Automatizzare attività manuali ripetitive
- Interagire con sistemi legacy non integrati

**Scenari comuni:**
- Accedere ai siti web dei fornitori e ottenere l'inventario in tempo reale
- Compilare automaticamente i moduli su sistemi esterni
- Estrarre dati da pagine web che non offrono API
- Verificare lo stato di consegna sui siti web dei corrieri
- Ottenere i prezzi da sistemi privi di accesso API

---

## Come Funziona

1. **Card Attivata**: il workflow raggiunge questa card e le condizioni sono soddisfatte
2. **Avvio dello Script**: il bot DocOperator inizia a eseguire il tuo script di automazione
3. **Azioni del Bot**: il bot esegue azioni come fare clic, digitare, scorrere, estrarre
4. **Estrazione dei Dati**: il bot raccoglie le informazioni dalle pagine web
5. **Restituzione dei Dati**: i dati tornano a DocFlow per essere utilizzati nelle card successive
6. **Gestione del Timeout**: se lo script impiega troppo tempo, si interrompe e restituisce ciò che ha

---

## Parametri Spiegati

### DocOperator Prompt/Script
Lo script di automazione che indica a DocOperator esattamente cosa fare

**Esempio (in linguaggio naturale):**
```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variables
I dati che vuoi passare ALL'INTERNO dello script

**Esempio:**
```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Queste variabili possono essere utilizzate nello script così:
```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maximum Steps
Quante azioni il bot è autorizzato a eseguire

**Valori tipici:**
- Attività semplice (come ottenere un prezzo): 10-20 passaggi
- Complessità media (compilare un modulo + estrarre): 20-50 passaggi
- Workflow complesso (login + ricerca + convalida): 50-100 passaggi

**Perché è importante:** previene loop infiniti e script con esecuzione molto lunga

### Maximum Retries
Se il bot non riesce a eseguire un'azione, quante volte deve riprovare?

**Esempi:**
- 1: prova una volta, se fallisce prosegue
- 3: prova 3 volte prima di arrendersi
- 5: molto persistente - prova 5 volte

---

## Esempio Passo dopo Passo

### Scenario: Ottenere i Prezzi del Fornitore da un Sito Web

**Definizione dello Script:**
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

**Variabili Passate:**
```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Script che Usa le Variabili:**
```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Risultato Atteso:**
```
price: 45.50
quantity_available: 500
```

---

## Tipi di Azioni che DocOperator Può Eseguire

### Navigazione
- Andare a un URL
- Fare clic sui link
- Premere i pulsanti
- Scorrere la pagina

### Compilazione dei Moduli
- Digitare testo nei campi
- Selezionare le opzioni dei menu a discesa
- Selezionare/deselezionare le caselle
- Fare clic sui pulsanti

### Estrazione dei Dati
- Leggere il testo dalla pagina
- Estrarre numeri
- Ottenere i dati delle tabelle
- Copiare informazioni

### Attesa
- Attendere il caricamento della pagina
- Attendere la comparsa degli elementi
- Attendere i contenuti dinamici

### Logica Condizionale
- Se qualcosa esiste, fai questo
- Se il testo corrisponde, allora...
- Conta i risultati e agisci di conseguenza

---

## Casi d'Uso Comuni

### 1. Ottenere Prezzi in Tempo Reale
**Scenario:** il fornitore non ha API ma il sito web mostra i prezzi

**Script:**
```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Verificare la Disponibilità dell'Inventario
**Scenario:** devi sapere se il fornitore ha scorte

**Script:**
```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Invio Automatico dei Moduli
**Scenario:** devi compilare un modulo su un sito esterno

**Script:**
```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Verifica dell'Inserimento Dati
**Scenario:** verificare che i dati corrispondano su due sistemi diversi

**Script:**
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

---

## Passaggi di Configurazione

### Passaggio 1: Crea lo Script
1. Definisci cosa vuoi ottenere
2. Suddividilo in piccoli passaggi
3. Scrivi ogni passaggio in modo chiaro
4. Testa prima manualmente (apri il sito web, fallo tu stesso)
5. Documenta esattamente cosa fai clic, dove digiti, cosa estrai

### Passaggio 2: Identifica le Variabili
1. Quali dati cambieranno tra i documenti?
2. Cosa deve essere passato allo script?
3. Definisci i nomi delle variabili
4. Specifica dove vengono utilizzate le variabili nello script

### Passaggio 3: Imposta i Parametri
- **Maximum Steps**: in base alla complessità dello script
- **Maximum Retries**: quanto deve essere persistente il bot?
- **Timeout**: quanto deve attendere per le pagine?

### Passaggio 4: Testa
1. Testa con dati di esempio
2. Verifica che il bot possa accedere al sito web
3. Verifica che l'estrazione sia corretta
4. Controlla se le variabili funzionano correttamente

---

## Suggerimenti per la Scrittura degli Script

### Linguaggio Chiaro
✅ **Fai:**
```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Non Fare:**
```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Selettori Specifici
✅ **Fai:**
```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Non Fare:**
```
Click somewhere
Type in a field
```

### Gestione degli Errori
✅ **Fai:**
```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Non Fare:**
```
Click "Next" (assumes it's always there)
```

---

## Risoluzione dei Problemi

### "Script Timed Out"
**Causa:** lo script ha impiegato troppo tempo per completarsi

**Soluzioni:**
- [ ] Riduci il numero di azioni
- [ ] Aumenta il valore di "Maximum Steps"
- [ ] Ottimizza lo script per un'esecuzione più rapida
- [ ] Semplifica ciò che stai cercando di estrarre

### "Element Not Found"
**Causa:** DocOperator non è riuscito a trovare il pulsante/campo specificato

**Soluzioni:**
- [ ] Verifica che il nome del pulsante/campo sia esattamente corretto
- [ ] Controlla se il layout del sito web è cambiato
- [ ] Aggiungi un tempo di attesa prima di fare clic
- [ ] Controlla se il pulsante appare solo in determinate condizioni

### "Login Failed"
**Causa:** autenticazione non riuscita

**Soluzioni:**
- [ ] Verifica che nome utente/password siano corretti
- [ ] Controlla se la password contiene caratteri speciali
- [ ] Verifica che l'account non sia bloccato
- [ ] Controlla se il processo di login è cambiato

### "Data Not Extracted Correctly"
**Causa:** lo script è stato eseguito ma ha estratto informazioni errate

**Soluzioni:**
- [ ] Verifica che sia stato selezionato il campo corretto
- [ ] Controlla se i dati si trovano nella posizione prevista
- [ ] Testa la logica di estrazione manualmente
- [ ] Aggiungi passaggi di debug per verificare cosa c'è nella pagina

### "Script Runs Slowly"
**Causa:** troppi passaggi o sito web lento

**Soluzioni:**
- [ ] Rimuovi i passaggi non necessari
- [ ] Ottimizza i tempi di attesa
- [ ] Controlla la connessione a Internet
- [ ] Valuta se esiste un'alternativa via API

---

## Best Practice

✅ **Fai:**
- Testa accuratamente gli script prima di distribuirli
- Mantieni gli script semplici e mirati
- Aggiungi commenti che spieghino ogni passaggio
- Usa nomi di variabili significativi
- Monitora le prestazioni degli script
- Predisponi un piano di riserva per quando gli script falliscono

❌ **Non Fare:**
- Creare script estremamente lunghi (>100 passaggi)
- Inserire password sensibili nei log
- Affidarti a coordinate esatte (i siti web cambiano)
- Creare loop senza condizioni di uscita
- Ignorare i messaggi di errore

---

## Suggerimenti sulle Prestazioni

- **Rimuovi i passaggi inutilizzati** - ogni passaggio richiede tempo
- **Combina azioni simili** - raggruppa i clic correlati
- **Ottimizza le attese** - usa solo i ritardi necessari
- **Memorizza i dati nella cache** - non estrarre due volte gli stessi dati
- **Elaborazione parallela** - esegui più script se possibile

---

## Considerazioni sulla Sicurezza

⚠️ **Importante:**
- Non memorizzare password in DocFlow
- Usa metodi sicuri per passare le credenziali
- Non registrare dati sensibili nei log
- Monitora ciò che viene estratto
- Assicurati che l'attività del bot sia registrata e verificabile

---

## Esempio di Variabili

### Variabili Disponibili che Puoi Usare:
```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script che Usa le Variabili:
```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

---

## Confronto: Quando Usare DocOperator vs API

| Situazione | Usa DocOperator | Usa API |
|-----------|-----------------|---------|
| Il sito web ha API | ❌ No | ✅ Sì |
| Il sito web è interattivo | ✅ Sì | ❌ No |
| Richiede il login | ✅ Sì | Dipende |
| Serve molta velocità | ❌ No | ✅ Sì |
| Workflow complesso | ✅ Sì | ❌ Forse no |
| I dati cambiano ogni giorno | ✅ Sì | ✅ Sì |

---

## Card Correlate

- **CALL_API** - Usala quando è disponibile un'API
- **ACTION_HTTPS_REQUEST** - Richieste più semplici
- **ACTION_SET_FIELD_TO_TEXT** - Usa i dati estratti
- **CONDITION_HTTPS_REQUEST_STATUS** - Verifica lo stato della richiesta
