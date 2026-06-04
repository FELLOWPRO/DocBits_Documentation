# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo**

La scheda di workflow "**Assign Document and Create Task/Notification Based on Decision Table**" assegna un documento e crea un'attività o una notifica con dettagli configurabili. L'assegnatario è determinato dal risultato di una decision table e la scheda consente di impostare le priorità e di inviare notifiche email.

## **Componenti della scheda**

1. **Assignee Type**
   * **Descrizione:** Specifica se il risultato della decision table assegna il documento e l'attività/notifica a un utente o a un gruppo.
   * **Dettaglio:** Un campo per configurare il tipo di assegnatario come "User" o "Group" in base all'output della decision table.
2. **Task/Notification**
   * **Descrizione:** Specifica il tipo di azione da creare per l'assegnatario.
   * **Dettaglio:** Un menu a discesa per selezionare "Task" o "Notification" in base alle esigenze del workflow.
3. **Title**
   * **Descrizione:** Il titolo dell'attività o della notifica.
   * **Dettaglio:** Un campo per fornire un titolo conciso che identifichi l'attività o la notifica.
4. **Description**
   * **Descrizione:** Dettagli aggiuntivi sull'attività o sulla notifica.
   * **Dettaglio:** Un campo per descrivere lo scopo e il contesto dell'attività o della notifica.
5. **Priority**
   * **Descrizione:** Definisce il livello di urgenza dell'attività o della notifica.
   * **Opzioni:**
     * **High:** Richiede attenzione immediata.
     * **Medium:** Importante ma non urgente.
     * **Low:** Può essere gestita in seguito.
6. **Assignee Type**
   * **Descrizione:** Questo campo determina il tipo di assegnatario (User o Group) a cui vengono assegnati il documento e l'attività/notifica.
   * **Dettaglio:** Un menu a discesa per selezionare se l'attività/notifica viene assegnata a un utente o a un gruppo in base all'output della decision table.
7. **Send Mail**
   * **Descrizione:** Configura se inviare una notifica email all'assegnatario.
   * **Opzioni:**
     * **True:** Invia una notifica email.
     * **False:** Non viene inviata alcuna notifica email.
8. **Value**
   * **Descrizione:** Imposta la priorità numerica per l'assegnazione del documento.
   * **Dettaglio:** Un campo per inserire un valore numerico, dove i numeri più bassi indicano una priorità più alta.

## **Funzionalità**

* **Valutazione della condizione:**\
  La scheda esegue le sue azioni solo se le condizioni del workflow sono soddisfatte.
* **Valutazione della decision table:**\
  La decision table determina se il documento e l'attività/notifica vengono assegnati a un utente o a un gruppo.
* **Assegnazione del documento e creazione di attività/notifica:**\
  Il documento viene assegnato al risultato della decision table. Viene creata un'attività o una notifica con il titolo, la descrizione e il livello di priorità specificati.
* **Notifica email:**\
  Se "Send Mail" è impostato su True, viene inviata una notifica email all'assegnatario.

## **Configurazione e impostazione**

1. **Definisci l'Assignee Type:**
   * Configura il campo Assignee Type su "User" o "Group" in base all'output della decision table.
2. **Seleziona Task/Notification:**
   * Scegli "Task" o "Notification" dal menu a discesa Task/Notification.
3. **Imposta i dettagli di Task/Notification:**
   * Inserisci il Title e la Description per l'attività o la notifica.
   * Seleziona la Priority (High, Medium o Low) dal menu a discesa.
4. **Abilita la notifica email:**
   * Imposta l'opzione Send Mail su True o False, a seconda che debba essere inviata una notifica email.
5. **Imposta la priorità numerica:**
   * Inserisci un valore numerico nel campo Value per determinare la priorità di assegnazione, dove i numeri più bassi vengono elaborati per primi.
6. Salva la configurazione della scheda e attiva il workflow.

## **Conclusione**

La scheda di workflow "Assign Document and Create Task/Notification Based on Decision Table" garantisce che le attività o le notifiche vengano assegnate dinamicamente all'utente o al gruppo appropriato in base ai risultati della decision table. Questa scheda facilita una delega efficiente delle attività, priorità personalizzabili e notifiche email opzionali per migliorare la reattività del workflow.
