# Document Operator for Sub-Organizations

<figure><img src="../../../../.gitbook/assets/image (42).png" alt="" width="563"><figcaption></figcaption></figure>

## Scopo:

Questa scheda di workflow valuta se un documento fa parte di una specifica sotto-organizzazione. In base a questa valutazione, il workflow può proseguire o attivare azioni diverse a seconda che il documento sia associato o meno alla sotto-organizzazione specificata.

## Componenti della scheda:

1. **Operator**
   * **Descrizione:** Definisce se il documento deve far parte o meno della sotto-organizzazione specificata.
   * **Opzioni:**
     * **Is:** Il documento deve far parte della sotto-organizzazione specificata affinché la condizione sia vera.
     * **Is Not:** Il documento non deve far parte della sotto-organizzazione specificata affinché la condizione sia vera.
2. **Sub-org**
   * **Descrizione:** Specifica la sotto-organizzazione con cui il documento deve essere confrontato.
   * **Dettaglio:** Deve corrispondere all'identificatore della sotto-organizzazione. Il confronto verifica se il documento appartiene alla sotto-organizzazione specificata.

## Funzionalità:

* **Valutazione della condizione:** Il sistema valuta se il documento fa parte della sotto-organizzazione specificata. Questa valutazione confronta la sotto-organizzazione del documento con quella fornita dall'utente.
* **Esecuzione dell'azione:**
  * **Condizione vera:**\
    Se il documento fa parte della sotto-organizzazione specificata, il workflow prosegue con la condizione vera. Ciò potrebbe attivare ulteriori azioni, come l'instradamento del documento a un reparto specifico, l'applicazione di regole specifiche della sotto-organizzazione o l'abilitazione di funzionalità su misura per tale sotto-organizzazione.
  * **Condizione falsa:**\
    Se il documento non fa parte della sotto-organizzazione specificata, il workflow prosegue con la condizione falsa. Ciò consente di eseguire azioni alternative, come l'invio di notifiche, l'arresto del workflow o l'applicazione di regole generali al di fuori dell'ambito della sotto-organizzazione.

## Configurazione e impostazione:

* Gli utenti configurano la scheda selezionando il campo del documento che contiene il documento e specificando la sotto-organizzazione con cui effettuare il confronto. L'operatore viene quindi scelto da un menu a discesa per definire se il documento debba o meno far parte della sotto-organizzazione specificata. Infine, gli utenti impostano la condizione di continuazione (vera o falsa), che determina il passaggio successivo nel workflow.

## Conclusione:

La scheda di workflow "Document in Sub-organization" è uno strumento utile per automatizzare le azioni in base al fatto che un documento appartenga o meno a una particolare sotto-organizzazione. Garantendo che i documenti vengano elaborati secondo le regole specifiche della sotto-organizzazione, questa scheda migliora l'efficienza del workflow e assicura che le azioni vengano eseguite nel corretto contesto organizzativo.
