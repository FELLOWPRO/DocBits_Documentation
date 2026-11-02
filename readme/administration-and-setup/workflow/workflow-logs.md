# Registri del Flusso di Lavoro

## Video

Il video di ricerca è un’anteprima con schermate reali DocBits. Il video di diagnosi usa ancora diagrammi didattici identificati come illustrazioni.
### Trovare l’esecuzione pertinente

{% hint style="info" %}
Anteprima da provare: schermate reali DocBits con azioni del documento, flusso dei documenti, tempi dei passaggi, registri vuoti e filtri di stato e data. Il documento non ha un’esecuzione Advanced Workflow salvata. Questa anteprima non include ancora righe di esecuzione, paginazione o diagnosi dei nodi.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/it.mp4" %}

[Apri video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/it.mp4) · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/it.vtt) · 1:48

<details>
<summary>Trascrizione</summary>

**Iniziare dal documento**

Nel dashboard dei documenti, apri il menu delle azioni e scegli Flusso dei documenti. La cronologia reale mostra importazione e OCR. Apri un passaggio per esaminare i tempi di attesa e di elaborazione. Questi passaggi sono distinti dai nodi Advanced Workflow.

**Leggere i contatori reali**

Qui vedi i registri dei workflow dello stesso documento. Il blu indica il totale, il rosso gli errori, il giallo le condizioni non soddisfatte e il verde i successi. Questo documento dimostrativo non ha esecuzioni registrate. Tutti e quattro i contatori mostrano quindi zero.

**Controllare le colonne delle esecuzioni**

Le colonne mostrano nome del workflow, data di creazione, durata e risultato. Distingui le esecuzioni ripetute dal timestamp. Questo documento non ha una riga da aprire.

**Aprire i filtri di stato**

L’icona dei filtri apre il menu reale. Ordina per nome o data di creazione, in ordine crescente o decrescente. Lo stato offre successo, condizione non soddisfatta ed errore.

**Scegliere le date e cancellare i filtri**

Scegli un periodo con le date di inizio e fine o il calendario. Il formato è anno, mese e giorno. Applicare richiede i risultati. Cancella i filtri reimposta la selezione. Svuota la ricerca separatamente.

**Anteprima: manca un’esecuzione salvata**

Questa anteprima permette di controllare l’accesso al documento, i dettagli di elaborazione e i comandi dei registri. Manca ancora un’esecuzione Advanced Workflow salvata per mostrare righe reali, paginazione, percorsi e messaggi dei nodi. Questi risultati non sono simulati nel video.

</details>

### Seguire i nodi e diagnosticare

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/it.vtt) · 1:51

<details>
<summary>Trascrizione</summary>

**Espandi un’esecuzione**

Espandi la riga del workflow. Un’esecuzione avanzata mostra il grafo a sinistra e i messaggi a destra; un workflow standard mostra schede in sequenza. I dati descrivono quell’esecuzione e possono differire dal designer attuale.

**Seleziona un nodo**

Sposta o ingrandisci il grafo, poi seleziona un nodo. Card Logs mostra i messaggi. Anche Wait ALL e Wait ANY possono avere messaggi di nodo. Leggi il messaggio insieme al nodo selezionato e all’orario dell’esecuzione.

**Distingui i risultati**

Verde significa successo; arancione, condizione falsa; rosso, errore; grigio, saltato. Un nodo saltato non è stato eseguito. Prima di modificarlo, verifica se è stato scelto un altro ramo o manca un ingresso alla giunzione.

**Segui la prima divergenza**

Segui il percorso reale dall’ingresso. Per un controllo importo falso, esamina arancione; per un errore, leggi il messaggio e segui rosso. Il gestore errori può riuscire mentre l’esecuzione continua a riportare l’errore originale.

**Verifica le giunzioni**

Per Wait ALL, controlla ogni sorgente e risultato collegato. Per ANY o OR, cerca una sorgente corrispondente. Due uscite dello stesso nodo non sono approvazioni indipendenti. Una condizione arancione può essere intenzionale.

**Correggi e verifica**

Annota workflow, riferimento documento, orario, nodo e messaggio esatto. Correggi configurazione o dati e prova uno scenario ripetibile. Salva e verifica l’attivazione. Confronta una nuova esecuzione con la precedente; i vecchi log conservano il comportamento precedente.

</details>

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
