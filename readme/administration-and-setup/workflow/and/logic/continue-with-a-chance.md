# Continue with a chance

<figure><img src="../../../../.gitbook/assets/image (49).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda DocBits introduce una condizione probabilistica, consentendo ai workflow di proseguire con una probabilità stabilita. La scheda è utile per scenari di test, selezioni casuali o variabilità controllata all'interno dei processi.

## **Funzionalità:**

* **Continuazione condizionale:** Questa scheda fa proseguire il workflow in base a una probabilità specificata, impostata dall'utente come valore percentuale. La scheda genera un esito casuale e lo confronta con la percentuale fornita, creando una possibilità controllata di continuazione del workflow.
* **Percentuale di probabilità:** Gli utenti specificano un valore percentuale (0-100%) che rappresenta la probabilità che il workflow prosegua. Ad esempio:
  * **0%:** Il workflow non proseguirà mai.
  * **50%:** Il workflow ha una probabilità del 50/50 di proseguire.
  * **100%:** Il workflow proseguirà sempre.

## **Utilizzo:**

Questa scheda è utile negli scenari in cui sono necessari percorsi di workflow casuali, come test A/B, campionamento controllato o simulazione di processi. Può anche essere applicata per aggiungere variabilità nei workflow automatizzati.

## **Scenario di esempio:**

* Un utente configura la scheda con una **probabilità del 30%**. Quando il workflow raggiunge questa scheda, c'è una probabilità del 30% che il workflow proceda al passaggio successivo. Questa configurazione è ideale per scenari in cui si desidera un campionamento casuale o un'elaborazione parziale.

Utilizzando la scheda "Conditional Continuation", le organizzazioni possono introdurre casualità controllata nei workflow, facilitare esperimenti di processo e migliorare il processo decisionale con condizioni probabilistiche.
