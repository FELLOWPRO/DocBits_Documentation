# Se il paese nel campo

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa carta di flusso di lavoro è progettata per valutare se un determinato paese, situato in un campo designato, fa parte di una particolare area commerciale o politica (Unione Europea, Area Schengen o NAFTA). In base a questa valutazione, il flusso di lavoro può continuare con una condizione vera o falsa, abilitando ulteriori azioni all'interno del sistema. È particolarmente utile per automatizzare le regole aziendali specifiche della regione, garantire la conformità o attivare flussi di lavoro specifici in base alle affiliazioni geografiche.

## **Componenti della carta:**

1. **Nome del campo**
   * **Descrizione:** Specifica il campo del documento in cui è memorizzato il nome o il codice del paese.
   * **Dettaglio:** Deve corrispondere esattamente all'identificatore del campo dei dati del paese all'interno del documento.
2. **Operatore**
   * **Descrizione:** Specifica se il paese nel campo selezionato deve corrispondere o meno alla regione o all'accordo selezionato.
   * **Opzioni:**
     * **È (Is):** Il paese deve far parte dell'accordo selezionato (UE, Schengen o NAFTA) affinché la condizione sia vera.
     * **Non è (Is Not):** Il paese non deve far parte dell'accordo selezionato affinché la condizione sia vera.
3. **Confronto del paese**
   * **Descrizione:** Definisce se il paese nel campo viene controllato rispetto a uno specifico accordo politico o commerciale.
   * **Opzioni:**
     * **Unione Europea:** La carta controlla se il paese è membro dell'Unione Europea.
     * **Area Schengen:** La carta controlla se il paese fa parte dell'Area Schengen.
     * **NAFTA:** La carta controlla se il paese è membro dell'accordo NAFTA.
4. **Booleano**
   * **Descrizione:** Definisce il risultato del confronto. Se il paese soddisfa la condizione, il flusso di lavoro continua con il valore booleano specificato.
   * **Opzioni:**
     * **Vero (True):** Il flusso di lavoro continua se la condizione corrisponde.
     * **Falso (False):** Il flusso di lavoro continua se la condizione non corrisponde.

## **Funzionalità:**

* **Valutazione della condizione:**
  * Il sistema valuta se il paese specificato nel campo fa parte della regione o dell'accordo scelto (Area UE, Schengen o NAFTA) in base all'operatore selezionato. Questa valutazione controlla il nome o il codice del paese rispetto a un elenco predefinito di paesi che appartengono a ciascun rispettivo gruppo.
* **Esecuzione dell'azione:**
  * **Condizione vera:** Se il paese nel campo corrisponde alla regione selezionata (come da operatore), il flusso di lavoro continua con la condizione vera specificata. Ciò può attivare ulteriori azioni, come l'instradamento dei documenti, l'applicazione di speciali regole di elaborazione o l'abilitazione di funzionalità specifiche della regione.
  * **Condizione falsa:** Se il paese non corrisponde alla regione selezionata (come da operatore), il flusso di lavoro continua con la condizione falsa specificata, consentendo l'esecuzione di azioni alternative o la terminazione del flusso di lavoro in base alla configurazione del sistema.

## **Installazione e configurazione:**

* Gli utenti configurano la carta selezionando il campo del documento contenente il paese e specificando la regione (Unione Europea, Area Schengen o NAFTA). L'operatore viene quindi scelto da un menu a discesa per definire se il paese deve far parte o meno della regione selezionata. Infine, gli utenti impostano la condizione di continuazione (vera o falsa), che determina il passaggio successivo nel flusso di lavoro.

## **Conclusione:**

La carta di flusso di lavoro "Confronto del paese nel campo" è uno strumento essenziale per automatizzare i processi che dipendono da regole geografiche, come la conformità con accordi commerciali o affiliazioni politiche. Confrontando i dati del paese con regioni specifiche come l'Unione Europea, l'Area Schengen o il NAFTA, questa carta garantisce che il sistema applichi la corretta logica di elaborazione, migliorando l'efficienza e garantendo un'accurata esecuzione del flusso di lavoro basata sulle condizioni geografiche.
