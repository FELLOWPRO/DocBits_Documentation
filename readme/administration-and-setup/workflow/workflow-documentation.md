# Documentazione del Workflow

**Documentazione del Workflow**

Per mantenere una visione d'insieme, puoi assegnare ai workflow intestazioni diverse, così da capire immediatamente di quale attività si occupa ciascun workflow.

Crea un nuovo Workflow: fai clic su + ADD WORKFLOW

![](<../../.gitbook/assets/workflow_add_button.png>)

Puoi utilizzare questi workflow (Test 1,2,3) per assegnare automaticamente i vari documenti al dipendente giusto in azienda.

![](<../../.gitbook/assets/workflow_list_overview.png>)

Se una fattura o un altro documento supera un determinato importo totale che richiede una revisione e un'approvazione preventive, questi documenti possono essere assegnati immediatamente alla persona corretta.

<figure><img src="../../.gitbook/assets/workflow_amount_check.png" alt="Workflow Amount Check"><figcaption></figcaption></figure>

**Test 1: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Invoice

Then: **Assign document to:** Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Delivery Note

Then: **Assign document to:** James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** **Document type is:** Order Confirmation

**Then:** **Assign document to:** Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

È inoltre possibile, se il documento non è assegnato a una singola persona, assegnarlo fin dall'inizio a un dipendente specifico.

<figure><img src="../../.gitbook/assets/workflow_assign_to_employee_start.png" alt="Workflow Assign to Employee Start" width="375"><figcaption></figcaption></figure>

Per avere una visione più semplice di cosa debba accadere a un documento, puoi impostare lo stato dei documenti in entrata in questo workflow. Questo workflow consente di vedere immediatamente se, ad esempio, è presente un'approvazione in sospeso.

**Test 4: Logic Card**

**When:** **Document type is:** Delivery Note

**And:** **Assignee is:** Amier Haider

**Then:** **Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test4_delivery_note_status.png" alt="Workflow Test 4 Delivery Note Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5: Logic Card**

When: **Document type is:** Invoice

And: **Assignee is:** Stefan Reppermund

Then: **Change Status to:** Pending Second Approval

<figure><img src="../../.gitbook/assets/workflow_test5_invoice_approval_status.png" alt="Workflow Test 5 Invoice Approval Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Se una fattura o un altro documento supera un determinato importo totale che richiede una revisione e un'approvazione preventive, questi documenti possono essere assegnati immediatamente alla persona giusta.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6: Logic Card**

When: **Assignee is:** Amier Haider

And: Docfield **total\_amount** is **Greater than 500**

Then: **Assign document to:** Asad Usman Khan

<figure><img src="../../.gitbook/assets/workflow_test6_total_amount_assign.png" alt="Workflow Test 6 Total Amount Assign"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

È inoltre possibile inserire lo stato nel workflow, in modo che la persona assegnata possa vedere immediatamente in quale stato si trova il documento e cosa dovrà accadere successivamente.

**Test 7: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** Docfield **total\_amount** is **Greater then 500**

**Then:** **Assign document to:** Asad Usman Khan

**Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test7_status_update.png" alt="Workflow Test 7 Status Update"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>

Ad esempio, se in un documento mancano informazioni specifiche o importanti, ma necessarie e che devono essere incluse per l'ulteriore elaborazione, puoi configurare il workflow in modo che questi documenti vengano immediatamente inoltrati all'acquirente e a un sostituto (rimpiazzo).

<figure><img src="../../.gitbook/assets/workflow_test8_missing_info.png" alt="Workflow Test 8 Missing Info"><figcaption></figcaption></figure>

**Test 9:**

Il Workflow con queste logic card è progettato per verificare automaticamente che la quantità, il prezzo unitario o lo sconto indicati in una conferma d'ordine corrispondano ai valori corrispondenti nell'ordine di acquisto. Questa verifica garantisce coerenza e accuratezza tra ciò che è stato ordinato e ciò che il fornitore conferma di consegnare.

Puoi assegnare a questi documenti uno stato specifico o assegnarli a un dipendente specifico.

<div align="center"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Workflow Test 9 Match Check Overview"><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/workflow_test9_match_check_detail.png" alt="Workflow Test 9 Match Check Detail"><figcaption></figcaption></figure>

**Logic Card: Quantity or Unit Price or Discount Match**

Questa logic card è progettata per verificare automaticamente che la quantità, il prezzo unitario o lo sconto indicati in una conferma d'ordine corrispondano ai valori corrispondenti nell'ordine di acquisto. Questa verifica garantisce coerenza e accuratezza tra ciò che è stato ordinato e ciò che il fornitore conferma di consegnare.

**Trigger Condition**

La logica si attiva quando una qualsiasi delle seguenti condizioni viene soddisfatta in una conferma d'ordine rispetto all'ordine di acquisto originale:

* **Quantity**: la quantità degli articoli ordinati corrisponde alla quantità confermata dal fornitore.
* **Unit Price**: il prezzo per articolo concordato corrisponde alla conferma del fornitore.
* **Discount**: eventuali sconti applicati sono coerenti tra l'ordine di acquisto e la conferma d'ordine.
* **Define Comparison Parameters**: configura i campi specifici (quantità, prezzo unitario, sconto) di cui la logic card verificherà la corrispondenza.
* **Automate Verification**: configura il sistema per confrontare automaticamente questi dettagli alla ricezione di una conferma d'ordine.
* **Customize Alerts**: decidi il workflow per la gestione delle discrepanze, inclusa la personalizzazione degli avvisi per la revisione manuale.

Questa logic card è fondamentale per garantire che i dettagli di una conferma d'ordine siano allineati con l'ordine di acquisto originale, salvaguardando l'integrità del ciclo di approvvigionamento.

**Test 10:**

Se hai un calcolo diverso per i sovrapprezzi, oppure li applichi solo ad alcuni articoli, puoi utilizzare le card generiche di calcolo della tabella; alcune di esse consentono anche di filtrare tramite espressioni regolari.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Sopra è riportato un esempio di calcolo per MTZ con un filtro per i numeri di articolo che iniziano con 01, 06, 9, 001 o 000.

Con una configurazione manuale è consigliabile suddividere i calcoli che dipendono da nuove colonne in un workflow separato. Per proseguire con il calcolo puoi utilizzare la card Run Workflow.

**Run Workflow**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Con questa card puoi specificare il nome di un workflow che deve essere eseguito dopo il workflow corrente, se le sue condizioni sono soddisfatte e dopo le precedenti card "then" del workflow corrente. Pur dando priorità ai workflow eseguibili e attivi, consente anche di eseguire workflow disattivati se il documento soddisfa le condizioni del workflow.

### **Adding calculated surcharges into an existing column** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Se desideri aggiungere tutti i sovrapprezzi come sconto negativo nella colonna dello sconto, puoi utilizzare la card di calcolo. Potrebbero esserci già voci in questa colonna: puoi impostarla come una delle variabili sulla card, sottrarvi il MTZ e aggiungere nuovamente il risultato in questa colonna. Nel caso siano presenti campi vuoti (sovrapprezzi solo per alcuni articoli), assumerà uno 0 per il suo calcolo.

**Notify user to authorize the order confirmation in DocBits**

Dopo aver calcolato i sovrapprezzi, potresti voler notificare a un utente specifico di autorizzare la conferma d'ordine. A tale scopo puoi utilizzare la card di notifica.

<figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Workflow Notification Card"><figcaption></figcaption></figure>

A seconda delle impostazioni, all'utente viene assegnata una nuova attività in DocBits e, facoltativamente, un'email per notificargli la nuova attività.
