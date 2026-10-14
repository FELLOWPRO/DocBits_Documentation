# Assign document to User

<figure><img src="../../../../.gitbook/assets/image (300).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Assign Document to User"** consente agli utenti di assegnare un documento a un utente specifico, garantendo una gestione fluida del workflow instradando i documenti alla persona appropriata. La Versione 3 aggiunge la possibilità di utilizzare una decision tree per determinare dinamicamente l'assegnazione dell'utente in base alle condizioni disponibili.

## **Componenti della scheda:**

1. **User**
   * **Descrizione:** Specifica l'utente a cui verrà assegnato il documento.
   * **Dettaglio:** Viene fornito un menu a discesa con tutti gli utenti disponibili per la selezione. All'utente selezionato verrà assegnato il documento per l'ulteriore azione.

## **Componenti aggiuntivi nella Versione 3:**

1. **Use Decision Tree**
   * **Descrizione:** Se abilitata, la scheda utilizza una decision tree per determinare dinamicamente l'assegnazione dell'utente.
   * **Opzioni:**
     * **True:** Utilizza la decision tree per l'assegnazione dinamica dell'utente.
     * **False:** Assegna il documento all'utente selezionato senza utilizzare la decision tree.

## **Funzionalità:**

* **Valutazione della condizione:**\
  La scheda esegue la sua azione solo se sia la sezione **"Where"** che la sezione **"And"** risultano vere.
* **Assegnazione del documento:**\
  La scheda assegna il documento all'utente selezionato, garantendo che l'attività venga instradata alla persona appropriata per l'azione. Ciò favorisce la responsabilità e una gestione documentale efficace.
* **Decision Tree (Versione 3):**\
  Se la decision tree è abilitata, la scheda valuta le condizioni definite all'interno dell'albero per selezionare dinamicamente l'utente per l'assegnazione del documento.

## **Configurazione e impostazione:**

* **Seleziona l'utente:**\
  Scegli l'**utente** dal menu a discesa a cui verrà assegnato il documento.
* **Use Decision Tree (Versione 3):**\
  Abilita o disabilita l'utilizzo della decision tree per selezionare dinamicamente l'utente.

## **Conclusione:**

La scheda di workflow **"Assign Document to User"** facilita un instradamento efficiente dei documenti assegnandoli all'utente selezionato, con la flessibilità aggiuntiva nella Versione 3 di determinare dinamicamente l'utente tramite una decision tree. Ciò garantisce un processo di workflow più adattivo ed efficiente.
