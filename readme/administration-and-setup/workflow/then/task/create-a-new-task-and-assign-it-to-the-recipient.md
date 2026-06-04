# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Create Task with Fallback"** garantisce una delega efficiente delle attività assegnandole a ruoli specifici — dispatcher o purchaser — incorporando al contempo un meccanismo di riserva per prevenire i fallimenti nell'assegnazione delle attività. Questa scheda migliora l'affidabilità e l'adattabilità del workflow in scenari dinamici.

## **Componenti della scheda:**

1. **Title**
   * **Descrizione**: Specifica il titolo dell'attività creata.
   * **Dettaglio**: Fornisce un identificatore conciso per l'attività.
2. **Description**
   * **Descrizione**: Descrive lo scopo o il contesto dell'attività.
   * **Dettaglio**: Chiarisce i dettagli dell'attività.
3. **Priority**
   * **Descrizione**: Imposta il livello di urgenza dell'attività.
   * **Opzioni**:
     * **High**: Richiede attenzione immediata.
     * **Medium**: Importante ma non urgente.
     * **Low**: Può essere gestita in seguito.
4. **Assigned Role**
   * **Descrizione**: Specifica il ruolo principale a cui viene assegnata l'attività.
   * **Opzioni**:
     * **Disponent**: Assegna l'attività al disponent.
     * **Purchaser**: Assegna l'attività al purchaser.
5. **Email Notification**
   * **Descrizione**: Consente di notificare l'utente assegnato via email.
   * **Opzioni**:
     * **True**: Invia una notifica email all'utente.
     * **False**: Non viene inviata alcuna notifica email.
6. **Fallback User**
   * **Descrizione**: Fornisce un'opzione di riserva per l'assegnazione dell'attività se il ruolo destinatario non viene trovato.
   * **Dettaglio**: Consente di selezionare un utente da un menu a discesa per garantire la delega dell'attività.

## **Funzionalità:**

* **Valutazione della condizione**:\
  La scheda viene eseguita solo se le condizioni nelle sezioni **"Where"** e **"And"** sono soddisfatte.
* **Assegnazione dell'attività**:
  * L'attività viene assegnata al ruolo selezionato (dispatcher o purchaser).
  * Se il ruolo specificato non viene trovato, l'attività viene assegnata a un utente dal menu a discesa di riserva.
* **Notifica email**:\
  Invia un'email all'utente assegnato se la notifica email è abilitata.

## **Configurazione e impostazione:**

1. **Specifica i dettagli dell'attività**: Inserisci il titolo, la descrizione e la priorità dell'attività.
2. **Seleziona il ruolo principale**: Scegli il ruolo a cui verrà assegnata l'attività (dispatcher o purchaser).
3. **Configura l'utente di riserva**: Seleziona un utente di riserva dal menu a discesa per garantire l'assegnazione dell'attività se il ruolo principale non viene trovato.
4. **Abilita la notifica email**: Indica se l'utente assegnato debba ricevere una notifica email.

## **Conclusione:**

La scheda di workflow **"Create Task with Fallback"** garantisce una delega delle attività fluida integrando un meccanismo di riserva. Assegnando le attività in base ai ruoli e offrendo un'opzione di utente alternativo, migliora l'affidabilità e la flessibilità nei processi di gestione delle attività.
