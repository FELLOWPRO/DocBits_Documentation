# If Country in Field is One of

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo**

Questa scheda di workflow è progettata per valutare se un paese specificato, situato in un campo designato, fa parte di un elenco predefinito di paesi. In base a questa valutazione, il workflow può proseguire con una condizione vera o falsa. Aiuta ad automatizzare i processi in cui le azioni dipendono dal fatto che il paese sia incluso o meno in un insieme di paesi consentiti o limitati.

## **Componenti della scheda:**

1. **Field Name**
   * **Descrizione:** Specifica il campo del documento in cui è memorizzato il nome o il codice del paese.
   * **Dettaglio:** Deve corrispondere all'identificatore esatto del campo dei dati del paese all'interno del documento.&#x20;
2. **Operator**
   * **Descrizione:** Definisce se il paese nel campo debba far parte di un elenco predefinito di paesi.
   * **Opzioni:**
     * **Is:** Il paese deve essere incluso nell'elenco dei paesi specificati affinché la condizione sia vera.
     * **Is Not:** Il paese non deve essere incluso nell'elenco dei paesi specificati affinché la condizione sia vera.
3. **Countries**
   * **Descrizione:** Specifica l'elenco di paesi con cui verrà confrontato il paese selezionato.
   * **Dettaglio:** È un elenco di paesi separati da virgole. Il confronto verifica se il paese nel campo è incluso in questo elenco.
4. **Continue Condition**
   * **Descrizione:** Definisce il risultato del confronto. Se il paese soddisfa la condizione, il workflow prosegue con il valore Boolean specificato.
   * **Opzioni:**
     * **True:** Il workflow prosegue se la condizione corrisponde.
     * **False:** Il workflow prosegue se la condizione non corrisponde.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema valuta se il paese specificato nel campo fa parte dell'elenco di paesi predefiniti. Questa valutazione confronta il nome o il codice del paese con l'elenco fornito.
* **Esecuzione dell'azione:**
  * **Condizione vera:**\
    Se il paese nel campo fa parte dell'elenco specificato di paesi, il workflow prosegue con la condizione vera. Ciò può attivare ulteriori azioni, come l'instradamento dei documenti al reparto appropriato, l'applicazione di regole di elaborazione specifiche o l'abilitazione di funzionalità specifiche per regione.
  * **Condizione falsa:**\
    Se il paese non corrisponde all'elenco, il workflow prosegue con la condizione falsa. Ciò consente di eseguire azioni alternative o di arrestare il workflow in base alla configurazione del sistema.

## **Configurazione e impostazione:**

* Gli utenti configurano la scheda selezionando il campo del documento contenente il paese e specificando l'elenco di paesi con cui effettuare il confronto. L'operatore viene quindi scelto da un menu a discesa per definire se il paese debba o meno far parte dell'elenco specificato di paesi. Infine, gli utenti impostano la condizione di continuazione (vera o falsa), che determina il passaggio successivo nel workflow.

## **Conclusione:**

La scheda di workflow "Country in Field Comparison with List" è uno strumento prezioso per automatizzare le azioni in base al fatto che un paese faccia parte di un gruppo predefinito. Confrontando i dati del paese con un elenco di paesi consentiti o limitati, questa scheda migliora l'efficienza del workflow e garantisce che i processi del sistema seguano le corrette regole geografiche.
