# DocBits Operator

## Panoramica

Il **DocBits Operator** è un assistente di automazione basato sull'IA, progettato per semplificare le attività ripetitive nei tuoi workflow. Gli utenti creano _prompt_ — istruzioni passo dopo passo arricchite da variabili — che guidano l'IA a navigare, inserire dati e fare clic nelle interfacce in modo automatico. Questo riduce lo sforzo manuale e velocizza le operazioni di routine.

## Abilitare il DocBits Operator

Per abilitare il DocBits Operator, segui questi passaggi:

1. **Vai alle Impostazioni**:
   * Dalla Dashboard, vai su **Settings**.
   *   Seleziona **Document Processing** e poi scegli **Module**.

       <figure><img src="../../.gitbook/assets/docbits_operator_module_selection.png" alt="Selezione del modulo DocBits Operator"><figcaption></figcaption></figure>
2. **Abilita la funzionalità**:
   * Scorri verso il basso per trovare l'opzione **DocBits Operator**.
   *   Attiva l'interruttore per abilitare il **DocBits Operator**.

       <div align="left"><figure><img src="../../.gitbook/assets/docbits_operator_enable_toggle.png" alt="Interruttore per abilitare il DocBits Operator" width="563"><figcaption></figcaption></figure></div>

## Accedere all'Interfaccia

* Una volta abilitata la funzionalità, apri il **DocBits Operator** dal menu di navigazione principale.

### **1. Inserimento del Prompt**

In fondo alla schermata c'è un campo di input con l'etichetta _“Enter your prompt here…”_. Qui gli utenti scrivono le istruzioni che l'operator deve seguire.

Accanto al campo di input ci sono diversi pulsanti di controllo:

* **Prompt Variables** – Apre un popup in cui puoi inserire coppie chiave-valore usate nel prompt. Le variabili si scrivono tra parentesi graffe, ad esempio `{invoice_number}` o `{url}`. Questi valori si applicano solo al prompt corrente nel campo di input.
* **Save Prompt** – Salva il prompt corrente. Puoi scegliere di salvarlo come:
  * **Organization Prompt** – Modificabile all'interno della tua organizzazione; include sia il prompt sia i valori delle variabili definiti.
  * **Global Prompt** – Condiviso tra tutti i tenant; include solo il prompt e i segnaposto delle variabili (nessun valore viene salvato).
* **Clear Chat** – Cancella la conversazione corrente con l'operator, ma lascia invariato il prompt nel campo di input. Utile quando riutilizzi o perfezioni un prompt.

Per una guida dettagliata su come scrivere prompt efficaci — inclusi sintassi, variabili ed esempi — consulta la [**Guida alla Scrittura dei Prompt**](prompt-writing-guide.md).

### **2. Navigazione nella Barra Laterale**

Usa l'icona in alto a sinistra per aprire o chiudere la barra laterale. La barra laterale mostra i prompt salvati, organizzati in due categorie:

* **Organization Prompts**: Modificabili e riutilizzabili all'interno della tua organizzazione.
* **Global Prompts**: Condivisi tra tutti i tenant. Non possono memorizzare variabili e non possono essere modificati né eliminati.
  * Un global prompt resta comunque modificabile ed eliminabile dall'**organizzazione che lo ha creato**, dove compare sotto Organization Prompts.
* **Funzione di ricerca:** una barra di ricerca in cima alla barra laterale permette di trovare rapidamente i prompt salvati per nome o parola chiave.
* **Riferimento delle icone:** Ogni prompt salvato ha un insieme di icone di azione
  * **Freccia** – Avvia il prompt
  * **Penna** – Modifica il prompt (disponibile solo per i prompt della tua organizzazione)
  * **Cestino** – Elimina il prompt (disponibile solo per i prompt della tua organizzazione)

### 3. Salvare il Prompt

Cliccando sul pulsante **Save Prompt** si apre un popup in cui puoi salvare il prompt corrente per usi futuri.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Popup Save Prompt"><figcaption></figcaption></figure></div>

#### **Campi del Popup Save Prompt**

* **Prompt Name:** Inserisci un nome per identificare il prompt.
* **Save Prompt Publicly (Checkbox):** Se selezionata, il prompt verrà salvato come **Global Prompt**. I Global Prompt sono condivisi tra tutti i tenant e non possono memorizzare i **valori** delle variabili (solo i **nomi** delle variabili).
* **Edit Variables:** Apre il [**Popup delle Variabili del Prompt**](prompt-writing-guide.md#popup-delle-variabili-del-prompt) per rivedere o modificare le definizioni delle variabili prima di salvare.

**Azioni**

* **Cancel:** Chiude il popup senza salvare.
* **Save:** Salva il prompt con il nome e l'impostazione di visibilità specificati.

### 4. Controlli di Esecuzione del Prompt

Quando un prompt è in esecuzione, gli utenti hanno diverse opzioni di controllo per gestire o intervenire nel processo di esecuzione:

* **Pause Prompt:** Interrompe temporaneamente l'esecuzione corrente. Utile se vuoi osservare lo stato attuale o preparare il sistema per i passaggi successivi.&#x20;
* **Resume Prompt:** Riprende l'esecuzione dal punto in cui era stata messa in pausa. ![](<../../.gitbook/assets/image (3) (1).png>)
* **Cancel Prompt:** Interrompe completamente l'esecuzione e reimposta la sessione. È utile se il prompt deve essere interrotto o riavviato a causa di un comportamento errato o di modifiche all'input.&#x20;
* **Take Control:** Permette all'utente di intervenire manualmente interagendo direttamente con il sistema. È utile se l'operator si blocca o interpreta male un passaggio. Prendere il controllo **mette automaticamente in pausa** il prompt e passa alla modalità manuale finché non scegli di riprendere o annullare.

### 5. Vista di Dettaglio dell'Operator

Una volta avviato un prompt, diventa disponibile un pulsante aggiuntivo che permette agli utenti di passare a una **vista di esecuzione dettagliata**. ![](<../../.gitbook/assets/Detailed view .jpg>)

* **Open Detail View:** Questo pulsante ti porta a una vista dedicata che mostra, passo dopo passo, cosa sta facendo l'operator in tempo reale.

Nella vista di dettaglio, gli utenti possono:

* Monitorare ogni azione eseguita (ad es. clic, input, attese).
* Vedere quale passaggio è attualmente attivo.
* Individuare dove si verificano i problemi se il prompt incontra difficoltà.
* Usare le stesse azioni **Pause**, **Resume**, **Cancel** e **Take Control**.

<div align="left"><figure><img src="../../.gitbook/assets/detailed view 2 .jpg" alt="" width="563"><figcaption></figcaption></figure></div>
