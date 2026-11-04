# Operatore documento per sub-organizzazioni

<figure><img src="../../../../.gitbook/assets/image (42).png" alt="" width="563"><figcaption></figcaption></figure>

## Scopo:

Questa carta di flusso di lavoro valuta se un documento fa parte di una specifica sub-organizzazione. In base a questa valutazione, il flusso di lavoro può continuare o attivare azioni diverse a seconda che il documento sia associato alla sub-organizzazione specificata o meno.

## Componenti della carta:

1. **Operatore**
   * **Descrizione:** Definisce se il documento deve far parte della sub-organizzazione specificata o meno.
   * **Opzioni:**
     * **È (Is):** Il documento deve far parte della sub-organizzazione specificata affinché la condizione sia vera.
     * **Non è (Is Not):** Il documento non deve far parte della sub-organizzazione specificata affinché la condizione sia vera.
2. **Sub-org**
   * **Descrizione:** Specifica la sub-organizzazione con cui confrontare il documento.
   * **Dettaglio:** Deve corrispondere all'identificatore della sub-organizzazione. Il confronto verifica se il documento appartiene alla sub-organizzazione specificata.

## Funzionalità:

* **Valutazione della condizione:** Il sistema valuta se il documento fa parte della sub-organizzazione specificata. Questa valutazione confronta la sub-organizzazione del documento con quella fornita dall'utente.
* **Esecuzione dell'azione:**
  * **Condizione vera:**
    Se il documento fa parte della sub-organizzazione specificata, il flusso di lavoro continua con la condizione vera. Ciò potrebbe attivare ulteriori azioni, come l'instradamento del documento a un dipartimento specifico, l'applicazione di regole specifiche della sub-organizzazione o l'abilitazione di funzionalità personalizzate per tale sub-organizzazione.
  * **Condizione falsa:**
    Se il documento non fa parte della sub-organizzazione specificata, il flusso di lavoro continua con la condizione falsa. Ciò consente di eseguire azioni alternative, come l'invio di notifiche, l'interruzione del flusso di lavoro o l'applicazione di regole generali al di fuori dell'ambito della sub-organizzazione.

## Installazione e configurazione:

* Gli utenti configurano la carta selezionando il campo del documento contenente il documento e specificando la sub-organizzazione da controllare. L'operatore viene quindi scelto da un menu a discesa per definire se il documento deve far parte o meno della sub-organizzazione specificata. Infine, gli utenti impostano la condizione di continuazione (vera o falsa), che determina il passaggio successivo nel flusso di lavoro.

## Conclusione:

La carta di flusso di lavoro "Documento in sub-organizzazione" è uno strumento utile per automatizzare le azioni in base al fatto che un documento appartenga o meno a una particolare sub-organizzazione. Garantendo che i documenti vengano elaborati in base a regole specifiche della sub-organizzazione, questa carta migliora l'efficienza del flusso di lavoro e assicura che le azioni vengano eseguite all'interno del corretto contesto organizzativo.
