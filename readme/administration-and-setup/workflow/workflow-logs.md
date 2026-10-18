# Registri del Flusso di Lavoro

## Video

Questi due video utilizzano diagrammi didattici identificati come illustrazioni.

### Trovare l’esecuzione pertinente

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/it.vtt) · 1:53

<details>
<summary>Trascrizione</summary>

**Apri i log del documento**

Nel pannello documenti, scegli Workflow Logs dal menu Azioni. L’accesso ai workflow deve essere abilitato. I log riguardano il documento selezionato. I test del designer e i registri di eventi o attività dell’organizzazione sono separati.

**Leggi i contatori**

Blu conta le esecuzioni nei risultati attuali; rosso, gli errori; giallo, le condizioni false; verde, i successi. I contatori rappresentano esecuzioni, non definizioni di workflow o nodi. I filtri possono modificare questi numeri.

**Scegli l’esecuzione esatta**

Ogni riga mostra nome, data di creazione, durata in secondi e risultato. Un workflow può essere eseguito più volte per un documento. Confronta gli orari. Una durata breve può apparire come zero virgola zero zero secondi per arrotondamento.

**Restringi i risultati**

Usa Cerca per trovare un workflow. L’icona delle regolazioni apre direzione e criterio di ordinamento, stato e date iniziale e finale. Ordina per nome o creazione. Inserisci le date come anno, mese, giorno e seleziona Applica.

**Controlla pagine e filtri**

Usa la paginazione per i risultati precedenti. Cancella filtri ricarica l’elenco senza selezioni. Svuota Cerca separatamente. Se mancano risultati, controlla documento, date e stato. Un elenco vuoto non dimostra un errore di esecuzione.

**Stati particolari**

Un avviso e un’icona di blocco indicano il limite di esecuzioni del documento. Esamina gli eventi ripetuti prima di cambiare i limiti. Il download video DocOperator compare solo se esiste una registrazione; riguarda quella esecuzione.

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
