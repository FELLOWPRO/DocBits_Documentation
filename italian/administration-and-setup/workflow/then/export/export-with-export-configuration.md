# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Export Document with Export Configuration"** è progettata per esportare un documento utilizzando una configurazione di esportazione specificata. Offre la flessibilità di ignorare eventuali attività in sospeso associate al documento, garantendo un processo di esportazione fluido indipendentemente dal suo stato corrente.

## **Componenti della scheda:**

1. **Export Configuration**
   * **Descrizione**: Specifica la configurazione di esportazione da utilizzare per l'elaborazione del documento.
   * **Dettaglio**: Questa configurazione determina il formato, la struttura e la destinazione del documento esportato.
2. **Ignore Pending Tasks**
   * **Descrizione**: Determina se le attività in sospeso collegate al documento debbano essere ignorate durante il processo di esportazione.
   * **Opzioni**:
     * **True**: Esporta il documento indipendentemente dalle attività in sospeso.
     * **False**: Garantisce che le attività in sospeso vengano completate prima dell'esportazione.

## **Funzionalità:**

* **Valutazione della condizione**: Il sistema valuta le condizioni impostate nelle sezioni **"Where"** e **"And"** del workflow. Se entrambe le condizioni sono vere, il processo di esportazione viene avviato.
* **Esportazione del documento**: Utilizzando la **Export Configuration** specificata, il documento viene elaborato ed esportato nel formato e nella destinazione definiti.
* **Gestione delle attività in sospeso**: Se **Ignore Pending Tasks** è impostato su **True**, il processo di esportazione ignora eventuali attività in sospeso collegate al documento. Se impostato su **False**, l'esportazione viene rinviata fino alla risoluzione di tutte le attività.

## **Configurazione e impostazione:**

Per configurare questa scheda, gli utenti devono:

1. Selezionare la **Export Configuration** desiderata per definire come verrà esportato il documento.
2. Scegliere se **Ignore Pending Tasks** impostando il valore su **True** o **False**.
3. Assicurarsi che le condizioni nelle sezioni **"Where"** e **"And"** siano impostate correttamente, poiché la scheda esegue la sua azione solo quando queste condizioni sono vere.

## **Conclusione:**

La scheda di workflow **"Export Document with Export Configuration"** garantisce che i documenti vengano esportati in modo efficiente e secondo configurazioni predefinite. Grazie alla possibilità di ignorare le attività in sospeso, questa scheda offre flessibilità nella gestione dei documenti in varie fasi, riducendo i ritardi e semplificando il processo di esportazione.
