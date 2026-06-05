# Registri del Flusso di Lavoro

## **Panoramica**

I **Registri del Flusso di Lavoro** consentono agli utenti di analizzare quali flussi di lavoro sono stati eseguiti per un documento, comprendere i risultati dell'esecuzione e approfondire i dettagli a livello di condizione per il debug o la convalida.

## **Accesso ai Registri del Flusso di Lavoro**

Per accedere ai registri del flusso di lavoro:

1. Navigare nel **Dashboard**.
2. Fare clic sul **menu Azioni** (icona a tre punti) accanto al documento desiderato.
3. Selezionare **Registri del Flusso di Lavoro** dal menu.
   * <mark style="color:red;">**Nota**</mark>**:** La funzione di workflow deve essere abilitata per accedere a questa opzione.
4.  Viene aperto un **pannello laterale** che mostra un riepilogo dei flussi di lavoro eseguiti.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAlgg3jnSVRVyuYxy4tAp%252Fimage.png%3Falt%3Dmedia%26token%3D4e8fcd63-6113-47eb-95a4-95a7821dc9b9\&width=768\&dpr=4\&quality=100\&sign=9e6ba9f5\&sv=2)

## **Componenti del Pannello dei Registri del Flusso di Lavoro**

#### **1. Contatori Riassuntivi del Flusso di Lavoro**

Posizionati nella parte superiore del pannello dei registri:

* **Blu**: Numero totale di flussi di lavoro eseguiti.
* **Rosso**: Flussi di lavoro che sono terminati con **errori**.
* **Giallo**: Flussi di lavoro che non sono stati **completati** a causa di corrispondenze di condizioni.
* **Verde**: Flussi di lavoro **eseguiti** con successo.

#### **2. Tabella di Esecuzione del Flusso di Lavoro**

Ogni riga nella tabella rappresenta un'**esecuzione del flusso di lavoro** e include:

* **Nome del Flusso di Lavoro**
* **Timestamp** (Creato il)
* **Tempo di Esecuzione** (in secondi)
* **Icona del Risultato**:
  * Segno di spunta verde: Flusso di lavoro eseguito con successo.
  * Croce rossa: Flusso di lavoro eseguito con un errore.
  * Trattino arancione: L'esecuzione è stata interrotta a causa di una condizione non soddisfatta.

Cliccando la **freccia** sulla sinistra di ogni riga si espande la **visualizzazione dettagliata del flusso di lavoro**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

### **Visualizzazione Dettagli Flusso di Lavoro**

Cliccando su una riga specifica del flusso di lavoro si apre il suo **registro dettagliato dell'esecuzione**, mostrando:

#### **Valutazione delle Condizioni**

* Blocco **Quando...**: Condizione iniziale.
* Blocchi **E...**: Condizioni aggiuntive.
* Blocchi **Quindi...**: Azioni eseguite quando tutte le condizioni sono soddisfatte.

Ogni riga di condizione mostra:

* Segno di spunta **verde**: Condizione soddisfatta.
* Trattino arancione: Condizione non soddisfatta.
* Croce rossa: Condizione fallita **a causa di un errore**

### **Nota sul Comportamento Importante**

Se una condizione in un flusso di lavoro **non è soddisfatta**, il sistema **smette di valutare ulteriori carte di flusso di lavoro** all'interno di quel flusso di lavoro. Questo comportamento impedisce un elaborazione non necessaria. Come indicatore visivo, la carta che **non ha soddisfatto la sua condizione** viene mostrata in **grigio**, e tutte le **carte successive** nello stesso flusso di lavoro appariranno anche **grigie**, indicando che non sono state **eseguite**.
