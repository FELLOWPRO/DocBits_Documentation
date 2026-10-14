# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Assign Document to Disponent / Purchaser"** assegna un documento a un **Disponent** oppure a un **Purchaser**. Se non viene trovato alcun utente valido, viene selezionato un utente di riserva per garantire che il documento sia sempre assegnato a qualcuno.

## **Componenti della scheda:**

1. **Disponent / Purchaser**
   * **Descrizione:** Specifica se il documento verrà assegnato a un Disponent o a un Purchaser.
   * **Opzioni:**
     * **Disponent:** Assegna il documento al Disponent.
     * **Purchaser:** Assegna il documento al Purchaser.
2. **Fallback User**
   * **Descrizione:** Specifica un utente di riserva nel caso in cui il documento non possa essere assegnato al Disponent o Purchaser selezionato.
   * **Dettaglio:** Il menu a discesa degli utenti disponibili ti consente di scegliere un utente di riserva per garantire che il documento venga assegnato anche se l'utente principale non può essere determinato.

## **Funzionalità:**

* **Valutazione della condizione:**\
  La scheda esegue la sua azione solo se sia la sezione **"Where"** che la sezione **"And"** risultano vere.
* **Assegnazione del documento:**\
  La scheda assegna il documento al **Disponent** o al **Purchaser** selezionato. Se la persona selezionata non è disponibile o non è valida, il documento viene assegnato all'utente di riserva.

## **Configurazione e impostazione:**

* **Seleziona Disponent / Purchaser:**\
  Scegli se assegnare il documento al **Disponent** o al **Purchaser**.
* **Seleziona Fallback User:**\
  Scegli un utente di riserva dal menu a discesa che riceverà il documento se l'assegnazione principale non è possibile.

## **Conclusione:**

La scheda di workflow **"Assign Document to Disponent / Purchaser"** garantisce che il documento sia sempre assegnato, al Disponent/Purchaser selezionato o, se necessario, all'utente di riserva. Ciò riduce al minimo le interruzioni del workflow e garantisce che l'elaborazione dei documenti prosegua senza problemi.
