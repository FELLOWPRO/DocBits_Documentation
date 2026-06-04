# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per valutare se un paese specificato, situato in un campo designato, fa parte di una particolare area commerciale o politica (Unione Europea, Area Schengen o NAFTA). In base a questa valutazione, il workflow può proseguire con una condizione vera o falsa, abilitando ulteriori azioni all'interno del sistema. È particolarmente utile per automatizzare regole aziendali specifiche per regione, garantire la conformità o attivare workflow specifici in base alle affiliazioni geografiche.

## **Componenti della scheda:**

1. **Field Name**
   * **Descrizione:** Specifica il campo del documento in cui è memorizzato il nome o il codice del paese.
   * **Dettaglio:** Deve corrispondere all'identificatore esatto del campo dei dati del paese all'interno del documento.&#x20;
2. **Operator**
   * **Descrizione:** Specifica se il paese nel campo selezionato debba corrispondere o meno alla regione o all'accordo selezionato.
   * **Opzioni:**
     * **Is:** Il paese deve far parte dell'accordo selezionato (EU, Schengen o NAFTA) affinché la condizione sia vera.
     * **Is Not:** Il paese non deve far parte dell'accordo selezionato affinché la condizione sia vera.
3. **Country Comparison**
   * **Descrizione:** Definisce se il paese nel campo viene confrontato con un accordo politico o commerciale specifico.
   * **Opzioni:**
     * **European Union:** La scheda verifica se il paese è membro dell'Unione Europea.
     * **Schengen Area:** La scheda verifica se il paese fa parte dell'Area Schengen.
     * **NAFTA:** La scheda verifica se il paese è membro dell'accordo NAFTA.
4. **Boolean**
   * **Descrizione:** Definisce il risultato del confronto. Se il paese soddisfa la condizione, il workflow prosegue con il valore Boolean specificato.
   * **Opzioni:**
     * **True:** Il workflow prosegue se la condizione corrisponde.
     * **False:** Il workflow prosegue se la condizione non corrisponde.

## **Funzionalità:**

* **Valutazione della condizione:**
  * Il sistema valuta se il paese specificato nel campo fa parte della regione o dell'accordo scelti (EU, Area Schengen o NAFTA) in base all'operatore selezionato. Questa valutazione confronta il nome o il codice del paese con un elenco predefinito di paesi che appartengono a ciascun rispettivo gruppo.
* **Esecuzione dell'azione:**
  * **Condizione vera:** Se il paese nel campo corrisponde alla regione selezionata (secondo l'operatore), il workflow prosegue con la condizione vera specificata. Ciò può attivare ulteriori azioni, come l'instradamento dei documenti, l'applicazione di regole di elaborazione speciali o l'abilitazione di funzionalità specifiche per regione.
  * **Condizione falsa:** Se il paese non corrisponde alla regione selezionata (secondo l'operatore), il workflow prosegue con la condizione falsa specificata, consentendo l'esecuzione di azioni alternative o la terminazione del workflow in base alla configurazione del sistema.

## **Configurazione e impostazione:**&#x20;

* Gli utenti configurano la scheda selezionando il campo del documento contenente il paese e specificando la regione (Unione Europea, Area Schengen o NAFTA). L'operatore viene quindi scelto da un menu a discesa per definire se il paese debba o meno far parte della regione selezionata. Infine, gli utenti impostano la condizione di continuazione (vera o falsa), che determina il passaggio successivo nel workflow.

## **Conclusione:**

La scheda di workflow "Country in Field Comparison" è uno strumento essenziale per automatizzare i processi che dipendono da regole geografiche, come la conformità agli accordi commerciali o le affiliazioni politiche. Confrontando i dati del paese con regioni specifiche come l'Unione Europea, l'Area Schengen o il NAFTA, questa scheda garantisce che il sistema applichi la logica di elaborazione corretta, migliorando l'efficienza e garantendo un'esecuzione accurata del workflow in base alle condizioni geografiche.
