# Create a New Task and assign it to the group

<figure><img src="../../../../.gitbook/assets/image (289).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Create Group Task or Notification"** facilita la creazione di attività o notifiche per gruppi specificati, garantendo una comunicazione e una gestione delle attività efficienti. Potenziata con la funzionalità decision tree nelle versioni successive, determina dinamicamente il gruppo assegnato o il metodo, semplificando le operazioni.

## **Componenti della scheda:**

1. **Title**
   * **Descrizione**: Specifica il titolo dell'attività o della notifica.
   * **Dettaglio**: Funge da identificatore per l'attività o la notifica creata.
2. **Description**
   * **Descrizione**: Descrive il contesto o i dettagli dell'attività o della notifica.
   * **Dettaglio**: Fornisce chiarezza sul suo scopo.
3. **Priority**
   * **Descrizione**: Imposta il livello di importanza dell'attività.
   * **Opzioni**:
     * **High**: Richiede un'azione immediata.
     * **Medium**: Importante ma meno urgente.
     * **Low**: Può essere gestita in seguito.
4. **Assigned Group**
   * **Descrizione**: Specifica il gruppo responsabile dell'attività o della notifica.
   * **Dettaglio**: Selezionato da un menu a discesa dei gruppi disponibili.
5. **Email Notification**
   * **Descrizione**: Consente l'invio di un'email per notificare il gruppo assegnato.
   * **Opzioni**:
     * **True**: Invia una notifica email.
     * **False**: Non viene inviata alcuna notifica email.

## **Componenti aggiuntivi nella Versione 3 e nella Versione 4**

1. **Decision Tree (solo Versione 3)**
   * **Descrizione**: Consente l'utilizzo di una decision tree per la creazione dinamica delle attività.
   * **Opzioni**:
     * **True**: Attiva l'elaborazione della decision tree.
     * **False**: Disabilita l'elaborazione della decision tree.
2. **Task/Notification Option (solo Versione 4)**
   * **Descrizione**: Consente di creare un'attività o una notifica.
   * **Opzioni**:
     * **Task**: Crea un'attività per il gruppo selezionato.
     * **Notification**: Invia una notifica anziché creare un'attività.

## **Funzionalità:**

* **Valutazione della condizione**:\
  Esegue l'azione della scheda solo quando le sezioni **"Where"** e **"And"** sono vere.
* **Creazione di attività o notifica**:
  * Viene creata un'attività per il gruppo selezionato con il titolo, la descrizione e la priorità specificati.
  * Nella Versione 4, la scheda può creare una notifica anziché un'attività.
* **Assegnazione dinamica (solo Versione 3)**:\
  Se abilitata, la decision tree determina dinamicamente il gruppo di destinazione.
* **Notifica email**:\
  Invia una notifica email al gruppo se l'opzione email è impostata su true.

## **Configurazione e impostazione:**

1. **Definisci i dettagli di attività o notifica**: Inserisci il titolo, la descrizione e la priorità.
2. **Assegna a un gruppo**: Seleziona un gruppo dal menu a discesa per l'assegnazione dell'attività o della notifica.
3. **Abilita la notifica email**: Indica se il gruppo debba essere notificato via email.
4. **Use Decision Tree (solo Versione 3)**: Abilita la decision tree per assegnare dinamicamente il gruppo.
5. **Seleziona il tipo di output (solo Versione 4)**: Scegli se la scheda crea un'attività o una notifica.

## **Conclusione:**

La scheda di workflow **"Create Group Task or Notification"** semplifica la gestione di attività e notifiche indirizzandole direttamente ai gruppi. La sua funzionalità di assegnazione dinamica, abilitata dalla decision tree, migliora la flessibilità, mentre le notifiche email garantiscono una comunicazione tempestiva. Le Versioni 3 e 4 aggiungono funzionalità avanzate, rendendola uno strumento versatile per un'esecuzione efficiente del workflow.
