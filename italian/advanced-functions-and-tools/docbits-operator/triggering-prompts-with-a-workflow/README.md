# Attivazione dei Prompts con un Workflow

Questa guida spiega come configurare un workflow di DocBits per attivare automaticamente un prompt salvato. Questo ti consente di integrare i prompt dell'operatore nei flussi di elaborazione dei documenti senza input manuale.

## Passo 1: Creare un Prompt

Prima di collegare un prompt a un workflow:

* Assicurati che il tuo prompt sia già stato creato
* Includi tutte le **variabili** necessarie nel corpo del prompt.

Se hai bisogno di aiuto per scrivere o salvare i prompt, consulta la [Guida alla Scrittura dei Prompts](../prompt-writing-guide.md) e la [Panoramica dell'Interfaccia dell'Operatore](../).

## Passo 2: Configurare il Workflow

Prima di configurare la scheda del Prompt dell'Operatore, assicurati che il tuo workflow sia stato creato correttamente.

1. Vai al **Costruttore del Workflow** nell'interfaccia di DocBits.
2. Crea un nuovo workflow o apri uno esistente.
3. Definisci le **condizioni di attivazione**—queste determinano quando il workflow inizierà (ad esempio, tipo di documento, stato, presenza di campi, ecc.).
4. Aggiungi i passaggi di **azione necessari** al tuo workflow secondo necessità.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fd3qJJhFDHTXDUfUedjaF%252Fimage.png%3Falt%3Dmedia%26token%3D310f9e9c-9e79-4987-af01-2d914f1abbe7&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=873cf566&#x26;sv=2" alt="" width="375"></div>

## Passo 3: Configurare la Scheda del Prompt dell'Operatore nel Workflow

Nel Costruttore del Workflow, utilizza la **scheda del Prompt dell'Operatore** per configurare un prompt che dovrebbe essere eseguito quando le condizioni del workflow sono soddisfatte.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fg11jtpdL4j3mJveYvWSX%252Fimage.png%3Falt%3Dmedia%26token%3Db208669e-b6a8-4879-b08b-d9ba353e908d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=974876f7&#x26;sv=2" alt="" width="375"></div>

### Opzioni di Configurazione Chiave

* **Script:** Seleziona il **Prompt dell'Organizzazione** salvato da eseguire.
* **Dati dello Script (Variabili):** Se il prompt selezionato contiene variabili, definisci qui i loro valori utilizzando coppie chiave-valore.
  * Se una variabile viene lasciata vuota qui, il sistema cercherà di popolarla automaticamente **dal documento**.
  * Perché ciò funzioni, il nome della variabile nel prompt deve corrispondere esattamente all'**ID del campo** dell'attributo del documento.
* **Numero Massimo di Passaggi:** Definisci il numero massimo di passaggi che l'operatore può eseguire durante questo prompt.
* **Numero Massimo di Tentativi:** Imposta quante volte il sistema dovrebbe riprovare il prompt in caso di fallimento.
* **Modalità di Esecuzione:** Scegli se il prompt dovrebbe essere eseguito:
  * **Nel Cloud**
  * **In Locale** (necessario se il tuo ERP o sistema di destinazione è ospitato localmente)
