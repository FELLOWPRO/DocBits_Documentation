# Esporta con configurazione di esportazione

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-10e6b7590bc6-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati.</p></figcaption></figure>

## **Scopo:**

La scheda del flusso di lavoro **"Esporta documento con configurazione di esportazione"** è progettata per esportare un documento utilizzando una configurazione di esportazione specificata. Fornisce la flessibilità di ignorare qualsiasi attività in sospeso associata al documento, garantendo un processo di esportazione regolare indipendentemente dal suo stato attuale.

## **Componenti della Carta:**

1. **Esporta configurazione**
   * **Descrizione**: Specifica la configurazione di esportazione da utilizzare per l'elaborazione del documento.
   * **Dettaglio**: questa configurazione determina il formato, la struttura e la destinazione del documento esportato.
2. **Ignora attività in sospeso**
   * **Descrizione**: Determina se le attività in sospeso collegate al documento devono essere ignorate durante il processo di esportazione.
   * **Opzioni**:
     * **True**: esporta il documento indipendentemente dalle attività in sospeso.
     * **False**: garantisce che le attività in sospeso vengano completate prima dell'esportazione.

## **Funzionalità:**

* **Valutazione Condizioni**: Il sistema valuta le condizioni impostate in **"Quando"** e **"E Sezioni"** del flusso di lavoro. Se entrambe le condizioni sono vere, viene avviato il processo di esportazione.
* **Esportazione documento**: utilizzando la **Configurazione di esportazione** specificata, il documento viene elaborato ed esportato nel formato e nella destinazione definiti.
* **Gestione attività in sospeso**: Se **Ignora attività in sospeso** è impostato su **True**, il processo di esportazione ignora qualsiasi attività in sospeso collegata al documento. Se impostato su **False**, le attività in sospeso possono impedire l'esportazione. Risolverli e organizzare l'attivazione del flusso di lavoro previsto o riprovare.

## **Impostazione e configurazione:**

Per configurare questa carta, gli utenti devono:

1. Selezionare la **Configurazione di esportazione** desiderata per definire come verrà esportato il documento.
2. Scegli se **Ignora attività in sospeso** impostando il valore su **True** o **False.**
3. Assicurati che le condizioni nelle sezioni **"Quando"** e **"E"** siano impostate correttamente, poiché la carta esegue la sua azione solo quando queste condizioni sono vere.

## **Conclusione:**

La scheda del flusso di lavoro **"Esporta documento con configurazione di esportazione"** garantisce che i documenti vengano esportati in modo efficiente e secondo configurazioni predefinite. Grazie alla possibilità di ignorare le attività in sospeso, questa carta offre flessibilità nella gestione dei documenti nelle varie fasi, riducendo i ritardi e semplificando il processo di esportazione.

## Versioni attuali e attività in sospeso

Sulla v3, scegli anche **Stato dopo l'esportazione**: `finished` chiude il documento dopo un'esportazione riuscita; `exported` lo lascia aperto per ulteriori elaborazioni. Le versioni precedenti mantengono `finished`. Una selezione mancante viene impostata automaticamente su `finished`; una selezione non valida viene rifiutata.

Se le attività aperte impediscono l'esportazione, la scheda segnala il rifiuto. Risolvere le attività e organizzare l'attivazione prevista o riprovare; l'attesa e la ripresa automatica non sono garantite da questa carta. La scheda di esportazione in coda separata raccoglie una configurazione per l'esportazione finale al termine dell'esecuzione. Vedi [Esporta carte e stato dei risultati](../../cards-overview/export-cards-guide.md).

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Scegli una configurazione di esportazione specifica per un documento convalidato.

**Configurazione:** Seleziona l'esportatore demo configurato e imposta Ignora attività in sospeso su `false`. Utilizza un documento con un'attività aperta, quindi un test separato senza attività aperte.

**Risultato atteso e controesempio:** Non si deve presumere che il caso del compito aperto riprenda automaticamente. Dopo aver risolto l'attività, attiva nuovamente l'esportazione prevista e verifica il risultato dell'esportatore e lo stato supportato.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
