# Esegui flusso di lavoro

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-359c9c1abe8c-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati.</p></figcaption></figure>

## Scopo:

La scheda **"Esegui flusso di lavoro"** consente agli utenti di eseguire dinamicamente un workflow selezionato da un elenco di workflow disponibili. Questa scheda è utile per automatizzare i processi in cui più workflow sono interconnessi, consentendo operazioni semplificate.

## Componenti della scheda:

1. **Flusso di lavoro**
   * **Descrizione:** Specifica il workflow da eseguire quando le condizioni risultano vere.
   * **Dettaglio:** Viene fornito un menu a discesa con tutti i workflow disponibili per la selezione.

## Funzionalità:

* **Valutazione della condizione:** La scheda esegue il workflow selezionato solo se entrambe le sezioni **"Quando"** e **"E"** risultano vere.
  * Se una delle condizioni è falsa, non viene intrapresa alcuna azione e il workflow rimane non attivato.
* **Esecuzione del workflow:**
  * Quando le condizioni sono soddisfatte, il workflow specificato viene attivato automaticamente.
  * Se le condizioni non sono soddisfatte, non viene eseguito alcun workflow.

## Configurazione e impostazione:

1. **Seleziona il flusso di lavoro:** Scegli il workflow da attivare dal **menu a discesa** dei workflow disponibili.
2. **Definisci le condizioni:** Configura le sezioni **"Quando"** e **"E"** per specificare i criteri che devono essere soddisfatti affinché il workflow venga eseguito.

## Conclusione:

La scheda **"Esegui flusso di lavoro"** offre un modo comodo ed efficiente per collegare i workflow, automatizzando con facilità i processi a più fasi. Garantendo che le condizioni nelle sezioni **"Quando"** e **"E"** siano soddisfatte, gli utenti possono eseguire i workflow dinamicamente e ridurre l'intervento manuale.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Riutilizzare un flusso di lavoro di convalida esistente.

**Configurazione:** Seleziona un flusso di lavoro figlio demo configurato che imposta `routing_result` su `checked`.

**Risultato previsto e controesempio:** Il flusso di lavoro selezionato viene richiamato nel contesto di esecuzione supportato. Verificare il proprio registro e il risultato del campo; non ricollegarlo al genitore in un ciclo.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
