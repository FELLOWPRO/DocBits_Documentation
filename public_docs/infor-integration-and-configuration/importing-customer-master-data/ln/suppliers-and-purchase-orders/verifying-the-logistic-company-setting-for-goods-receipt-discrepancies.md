# Verifica dell'impostazione della Logistic Company per le discrepanze nell'entrata merci

Nei processi di approvvigionamento su larga scala non è raro imbattersi in situazioni in cui alcuni dati non coincidono come previsto. Ad esempio, potresti visualizzare un messaggio di errore come:

**“Delivery Note L1234, Order Type: Purchase, Order 100000211, Position 10, Subsequent Number 1, Logistic Company&#x20;**<mark style="color:red;">**XXXX**</mark>**, Goods Receipt WE0000293 and Entry Position 10 not found in direct debit.”**

Questo tipo di messaggio indica spesso una mancata corrispondenza o l'assenza di informazioni relative alla configurazione della tua logistic company. La logistic company è un elemento fondamentale nei sistemi di pianificazione delle risorse aziendali (ERP), soprattutto nelle catene di fornitura complesse che si estendono su più entità legali o logistiche.

**Perché accade?**

Negli ambienti multi-entità, ogni transazione (acquisto, ricezione della merce o avvio dei pagamenti) deve essere assegnata correttamente alla logistic company giusta. La “logistic company” è più di un semplice identificativo: determina quale magazzino, centro di distribuzione o nodo della rete di fornitura è responsabile dell'ordine e delle attività di evasione. Se il numero della società non corrisponde all'entità prevista, i processi successivi, come la verifica dell'entrata merci o i regolamenti con addebito diretto, possono fallire.

## **Controlli principali da eseguire:**

### 1. Verifica la Logistic Company assegnata:

Controlla i record dei dati anagrafici per assicurarti che la logistic company indicata (in questo caso <mark style="color:red;">XXXX</mark>) sia l'entità corretta per l'ordine in questione. <mark style="color:red;">XXXX</mark> è il codice società giusto per gestire gli acquisti da questo fornitore o per questa specifica linea di prodotti?

### 2. Controlla la configurazione dell'ordine di acquisto (PO):

Verifica che la logistic company dell'ordine di acquisto sia allineata con la sede di ricezione prevista. A volte un ordine viene creato con una logistic company, ma la merce viene ricevuta con un'altra se la configurazione non è coerente.

### 3. Confronta l'entrata merci con i record del magazzino:

Esamina l'entrata merci (WE0000293) e assicurati che sia stata registrata nel magazzino della società corretta. Se il magazzino appartiene a un'altra logistic company, potrebbe essere necessario correggere la configurazione o eseguire un trasferimento verso l'entità corretta.

### 4. Verifica l'integrazione e la coerenza dei dati anagrafici:

I punti di integrazione tra i diversi moduli (Acquisti, Magazzino, Finanza) si basano su codici coerenti. Assicurati che la logistic company sia definita in modo uniforme in tutti i moduli pertinenti.

### 5. Consulta la documentazione e il supporto:

Se i controlli interni non risolvono il problema, consulta la documentazione del sistema o contatta il supporto del tuo ERP. Potranno aiutarti a verificare se il codice della logistic company è configurato correttamente o se sono necessari ulteriori passaggi di configurazione.
