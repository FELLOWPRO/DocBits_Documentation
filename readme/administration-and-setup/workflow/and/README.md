# And

## Comprendere le schede "And"

### **Scopo delle schede 'And':**

* Le schede **And** fungono da schede di condizione che specificano i criteri che devono essere soddisfatti affinché il workflow prosegua. Agiscono di fatto come operatori logici "AND", il che significa che tutte le condizioni specificate in queste schede devono essere soddisfatte affinché l'azione successiva venga attivata.

#### Categorie di schede 'And'

Dagli screenshot risulta chiaro che queste schede coprono un'ampia gamma di condizioni, tra cui:

* **Compare with Purchase Order**:
  * Condizioni relative alla validazione e al confronto con gli ordini d'acquisto, come il confronto delle date di consegna, dei prezzi unitari o delle differenze di quantità. Sono fondamentali per garantire che le transazioni siano conformi ai termini concordati.

<figure><img src="../../../.gitbook/assets/image (14) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document Field**:
  * Riguardano condizioni basate su campi specifici all'interno dei documenti, come caselle di controllo selezionate, confronto dei valori dei campi o la verifica che un campo del documento rientri in una determinata tolleranza. Questo è particolarmente importante per l'integrità dei dati e i controlli automatizzati all'interno di moduli o sistemi di gestione documentale.

<figure><img src="../../../.gitbook/assets/image (15) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Date & Time:**
  * Condizioni basate su date e orari

<figure><img src="../../../.gitbook/assets/image (17) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document**:
  * Condizioni basate sulle caratteristiche del documento, come il tipo o l'associazione a una particolare sotto-organizzazione. Queste condizioni possono indirizzare i workflow in base alla categorizzazione del documento o al coinvolgimento di un reparto.

<figure><img src="../../../.gitbook/assets/image (18) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Logic**:
  * Condizioni logiche che possono comportare valutazioni come "Continua con una probabilità di X%" o l'esecuzione di richieste HTTPS, fondamentali per le integrazioni e per il processo decisionale probabilistico all'interno dei workflow.

<figure><img src="../../../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Status**:
  * Concentrandosi sullo stato di documenti o attività, queste condizioni garantiscono che solo gli elementi in determinati stati attivino workflow specifici, aspetto cruciale per la gestione dei processi basata sullo stato.

<figure><img src="../../../.gitbook/assets/image (20) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Table**:
  * Riguardano condizioni basate sui dati di tabella, come la corrispondenza con pattern regex o il confronto di valori all'interno di una tabella. Tali condizioni sono essenziali per validare e manipolare grandi insiemi di dati.

<figure><img src="../../../.gitbook/assets/image (22) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Assignee**:
  * Condizioni basate sugli assegnatari di attività o documenti. Questo garantisce che le azioni vengano intraprese solo quando sono coinvolti determinati utenti, migliorando la responsabilità e la specificità delle attività.

<figure><img src="../../../.gitbook/assets/image (24) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Applicazione pratica

Queste schede "And" vengono configurate all'interno del workflow per eseguire controlli e validazioni che garantiscono che il processo rispetti rigorosamente le regole aziendali e gli standard di integrità dei dati. Ad esempio:

* **Un workflow potrebbe usare una scheda 'And' per verificare che l'importo totale di una fattura corrisponda all'ordine d'acquisto prima di attivare il pagamento.**
* **Un altro workflow potrebbe usare una scheda 'And' per garantire che un documento venga revisionato da specifici membri del team prima di passare alla fase successiva.**

### Conclusione

Le schede "And" sono un componente fondamentale dei sistemi di workflow che richiedono un controllo preciso sull'esecuzione del processo in base a più condizioni. Garantiscono che ogni passaggio di un workflow proceda solo quando tutti i criteri necessari sono pienamente soddisfatti, automatizzando così alberi decisionali complessi all'interno dei processi aziendali.

Comprendere e configurare correttamente queste schede è cruciale per sfruttare appieno le capacità del tuo sistema di gestione dei workflow, al fine di migliorare efficienza, accuratezza e conformità nei processi organizzativi.
