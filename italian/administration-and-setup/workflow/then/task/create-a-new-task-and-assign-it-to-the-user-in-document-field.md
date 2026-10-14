# Create a New Task and assign it to the User in Document Field

<figure><img src="../../../../.gitbook/assets/image (290).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Create Field-Based Task or Notification"** viene utilizzata per creare attività o notifiche assegnate dinamicamente agli utenti identificati all'interno di specifici campi del documento. Questa scheda fornisce un meccanismo di riserva opzionale per garantire un'esecuzione fluida del workflow anche quando il campo del documento non specifica un utente valido.

## **Componenti della scheda:**&#x20;

1. **Title**
   * **Descrizione**: Specifica il titolo dell'attività o della notifica.
   * **Dettaglio**: Utilizzato per nominare e identificare l'attività o la notifica creata.
2. **Description**
   * **Descrizione**: Fornisce dettagli aggiuntivi sull'attività o sulla notifica.
   * **Dettaglio**: Garantisce che il destinatario comprenda lo scopo e il contesto dell'attività o della notifica.
3. **Priority**
   * **Descrizione**: Definisce l'urgenza dell'attività o della notifica.
   * **Opzioni**:
     * **High**: Richiede attenzione immediata.
     * **Medium**: Importante ma meno urgente.
     * **Low**: Può essere gestita in un secondo momento.
4. **Field Name**
   * **Descrizione**: Specifica il campo del documento che verrà utilizzato per assegnare l'attività o la notifica.
   * **Dettaglio**: Il campo selezionato determinerà dinamicamente l'utente a cui verrà assegnata l'attività o la notifica. Se il campo è vuoto o non valido, l'attività o la notifica verrà assegnata all'utente di riserva selezionato dal menu a discesa.
5. **Email Notification**
   * **Descrizione**: Configura se l'utente assegnato viene notificato via email.
   * **Opzioni**:
     * **True**: Invia una notifica email all'utente assegnato.
     * **False**: Non viene inviata alcuna notifica email.
6. **Fallback User**
   * **Descrizione**: Consente la selezione di un utente da un menu a discesa per assegnare l'attività o la notifica quando non viene trovato alcun utente valido nel campo del documento.
   * **Dettaglio**: Garantisce che l'attività o la notifica venga assegnata anche se il campo del documento è vuoto o non valido.

## **Componenti aggiuntivi nella Versione 3:**

1. **Notification Type**&#x20;
   * **Descrizione**: Specifica se la scheda crea un'attività o una notifica.
   * **Opzioni**:
     * **Task**: Crea un'attività assegnata all'utente specificato.
     * **Notification**: Invia una notifica anziché creare un'attività.

## **Funzionalità:**

* **Valutazione della condizione**:\
  La scheda esegue la sua azione solo se sia la sezione **"Where"** che la sezione **"And"** risultano vere.
* **Creazione di attività o notifica**:
  * Assegna l'attività o la notifica all'utente identificato nel campo del documento.
  * Nella Versione 3, consente di creare un'attività o una notifica.
* **Meccanismo di riserva**:\
  Se il campo del documento non identifica un utente valido, la scheda assegna l'attività o la notifica all'utente di riserva selezionato dal menu a discesa.
* **Notifica email**:\
  Invia una notifica email all'utente assegnato se configurato.

## **Configurazione e impostazione:**

1. **Definisci i dettagli di attività o notifica**: Inserisci il titolo, la descrizione e la priorità.
2. **Seleziona il campo del documento**: Scegli il campo che specifica l'utente per l'assegnazione dell'attività o della notifica.
3. **Abilita la notifica email**: Specifica se debba essere inviata una notifica email all'utente assegnato.
4. **Seleziona il Fallback User**: Scegli un utente di riserva dal menu a discesa per l'assegnazione se il campo del documento non identifica un utente valido.
5. **Specifica il Notification Type (Versione 3)**: Indica se la scheda crea un'attività o una notifica.

## **Conclusione:**

La scheda di workflow **"Create Field-Based Task or Notification"** semplifica la gestione di attività e notifiche assegnando dinamicamente le responsabilità in base ai campi del documento. Il suo meccanismo di utente di riserva e le opzioni potenziate nella Versione 3 offrono flessibilità, garantendo che le attività o le notifiche vengano sempre assegnate, anche quando i dati del documento sono incompleti.
