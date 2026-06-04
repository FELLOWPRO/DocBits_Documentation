# Assign user from field

<figure><img src="../../../../.gitbook/assets/image (299).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Assign User from Field with Fallback"** assegna dinamicamente un utente in base al valore trovato in un campo specificato del documento. Se il campo non contiene un utente valido, viene selezionato un utente di riserva da un elenco predefinito di utenti disponibili per garantire che l'attività o l'azione venga assegnata correttamente.

## **Componenti della scheda:**

1. **Field Name**
   * **Descrizione:** Specifica il **campo del documento** che contiene le informazioni sull'utente da assegnare.
   * **Dettaglio:** Questo campo viene valutato per determinare quale utente debba essere assegnato. Se il campo contiene un utente valido, a tale utente verrà assegnata l'attività. Se il campo è vuoto o non valido, verrà assegnato l'utente di riserva.
2. **User (Fallback)**
   * **Descrizione:** Specifica l'**utente di riserva** da assegnare se il campo del documento non contiene un utente valido.
   * **Dettaglio:** Viene fornito un menu a discesa con tutti gli utenti disponibili per la selezione. Questo utente verrà assegnato se il campo del documento è vuoto o non contiene un utente valido.

## **Funzionalità:**

* **Valutazione della condizione:**\
  La scheda esegue la sua azione solo se sia la sezione **"Where"** che la sezione **"And"** risultano vere.
* **Assegnazione dell'utente basata sul campo:**\
  La scheda tenta innanzitutto di assegnare l'attività o l'azione all'utente identificato nel **Field Name**.
* **Assegnazione dell'utente di riserva:**\
  Se il campo non contiene un utente valido (o è vuoto), la scheda assegna l'attività all'utente di riserva selezionato dal menu a discesa **User (Fallback)**.

## **Configurazione e impostazione:**

* **Seleziona il Field Name:**\
  Scegli il **campo del documento** che specifica l'utente per l'assegnazione.
* **Seleziona il Fallback User:**\
  Scegli l'**utente di riserva** dal menu a discesa. A questo utente verrà assegnata l'attività se il campo del documento non contiene un utente valido.

## **Conclusione:**

La scheda di workflow **"Assign User from Field with Fallback"** garantisce che un'attività o un'azione venga sempre assegnata a un utente valido. Se l'utente nel campo del documento non è disponibile, l'utente di riserva viene assegnato automaticamente, offrendo flessibilità e garantendo il completamento dell'attività.
