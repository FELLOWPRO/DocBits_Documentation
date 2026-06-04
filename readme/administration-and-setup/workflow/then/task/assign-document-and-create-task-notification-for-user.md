# Assign Document and Create Task/Notification for User

<figure><img src="../../../../.gitbook/assets/image (13) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo**

La scheda di workflow "**Assign Document and Create Task/Notification for User**" assegna un documento a un utente specificato, crea un'attività o una notifica con dettagli configurabili e, facoltativamente, invia una notifica email all'utente. Questa scheda consente inoltre di impostare un valore di priorità numerica per determinare l'ordine di esecuzione.

## **Componenti della scheda**

1. **User**
   * **Descrizione:** Specifica l'utente che riceverà l'attività o la notifica.
   * **Dettaglio:** Un menu a discesa per selezionare l'utente a cui verranno assegnati il documento e l'attività/notifica.
2. **Task/Notification**
   * **Descrizione:** Specifica il tipo di azione da creare per l'utente.
   * **Dettaglio:** Un menu a discesa per scegliere "Task" o "Notification" in base all'azione prevista.
3. **Title**
   * **Descrizione:** Il titolo dell'attività o della notifica.
   * **Dettaglio:** Un campo per fornire un titolo conciso e descrittivo per l'attività o la notifica.
4. **Description**
   * **Descrizione:** Dettagli aggiuntivi sull'attività o sulla notifica.
   * **Dettaglio:** Un campo per descrivere lo scopo dell'attività o fornire contesto per la notifica.
5. **Priority**
   * **Descrizione:** Definisce il livello di urgenza dell'attività o della notifica.
   * **Opzioni:**
     * **High:** Richiede attenzione immediata.
     * **Medium:** Importante ma non urgente.
     * **Low:** Può essere gestita in seguito.
6. **Send Mail**
   * **Descrizione:** Configura se viene inviata una notifica email all'utente.
   * **Opzioni:**
     * **True:** Invia una notifica email all'utente.
     * **False:** Non viene inviata alcuna notifica email.
7. **Value**
   * **Descrizione:** Imposta la priorità numerica per l'assegnazione del documento.
   * **Dettaglio:** Un campo per inserire un valore numerico, dove i numeri più bassi indicano una priorità più alta.

## **Funzionalità**

* **Valutazione della condizione:**\
  La scheda esegue le sue azioni solo se le condizioni configurate del workflow sono soddisfatte.
* **Assegnazione del documento e creazione di attività/notifica:**\
  Il documento viene assegnato all'utente specificato nel campo "User". Viene creata un'attività o una notifica con il titolo, la descrizione e il livello di priorità forniti.
* **Notifica email:**\
  Se "Send Mail" è impostato su True, viene inviata un'email all'utente per notificarlo dell'attività o della notifica.

## **Configurazione e impostazione**

1. **Seleziona l'utente:**
   * Scegli l'utente dal menu a discesa User.
2. **Configura i dettagli di Task/Notification:**
   * Seleziona "Task" o "Notification" dal menu a discesa Task/Notification.
   * Inserisci il Title e la Description per l'attività o la notifica.
   * Imposta la Priority selezionando High, Medium o Low dal menu a discesa.
3. **Abilita la notifica email:**
   * Configura l'opzione Send Mail su True o False, a seconda che debba essere inviata una notifica email.
4. **Imposta la priorità numerica:**
   * Inserisci un valore numerico nel campo Value per determinare la priorità dell'assegnazione, dove i valori più bassi vengono elaborati per primi.
5. Salva la configurazione della scheda e attiva il workflow.

## **Conclusione**

La scheda di workflow "Assign Document and Create Task/Notification for User" garantisce che i documenti vengano assegnati all'utente appropriato creando al contempo attività o notifiche con priorità definite e notifiche email opzionali. Questa scheda aiuta a semplificare la delega delle attività e migliora l'efficienza del workflow.
