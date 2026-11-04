# Se il paese nel campo è uno di

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo**

Questa carta di flusso di lavoro è progettata per valutare se un determinato paese, situato in un campo designato, fa parte di un elenco predefinito di paesi. In base a questa valutazione, il flusso di lavoro può continuare con una condizione vera o falsa. Aiuta ad automatizzare i processi in cui le azioni dipendono dal fatto che il paese sia elencato tra un insieme di paesi consentiti o limitati.

## **Componenti della carta:**

1. **Nome del campo**
   * **Descrizione:** Specifica il campo del documento in cui è memorizzato il nome o il codice del paese.
   * **Dettaglio:** Deve corrispondere esattamente all'identificatore del campo dei dati del paese all'interno del documento.
2. **Operatore**
   * **Descrizione:** Definisce se il paese nel campo deve far parte di un elenco predefinito di paesi.
   * **Opzioni:**
     * **È (Is):** Il paese deve essere incluso nell'elenco dei paesi specificati affinché la condizione sia vera.
     * **Non è (Is Not):** Il paese non deve essere incluso nell'elenco dei paesi specificati affinché la condizione sia vera.
3. **Paesi**
   * **Descrizione:** Specifica l'elenco dei paesi con cui verrà confrontato il paese selezionato.
   * **Dettaglio:** Questo è un elenco di paesi separati da virgole. Il confronto verifica se il paese nel campo è incluso in questo elenco.
4. **Condizione di continuazione**
   * **Descrizione:** Definisce il risultato del confronto. Se il paese soddisfa la condizione, il flusso di lavoro continua con il valore booleano specificato.
   * **Opzioni:**
     * **Vero (True):** Il flusso di lavoro continua se la condizione corrisponde.
     * **Falso (False):** Il flusso di lavoro continua se la condizione non corrisponde.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema valuta se il paese specificato nel campo fa parte dell'elenco di paesi predefiniti. Questa valutazione controlla il nome o il codice del paese rispetto all'elenco fornito.
* **Esecuzione dell'azione:**
  * **Condizione vera:**
    Se il paese nel campo fa parte dell'elenco specificato di paesi, il flusso di lavoro continua con la condizione vera. Ciò può attivare ulteriori azioni, come l'instradamento dei documenti al dipartimento appropriato, l'applicazione di specifiche regole di elaborazione o l'abilitazione di funzionalità specifiche della regione.
  * **Condizione falsa:**
    Se il paese non corrisponde all'elenco, il flusso di lavoro continua con la condizione falsa. Ciò consente di eseguire azioni alternative o di interrompere il flusso di lavoro in base alla configurazione del sistema.

## **Installazione e configurazione:**

* Gli utenti configurano la carta selezionando il campo del documento contenente il paese e specificando l'elenco dei paesi da controllare. L'operatore viene quindi scelto da un menu a discesa per definire se il paese deve far parte o meno dell'elenco specificato di paesi. Infine, gli utenti impostano la condizione di continuazione (vera o falsa), che determina il passaggio successivo nel flusso di lavoro.

## **Conclusione:**

La carta di flusso di lavoro "Confronto del paese nel campo con l'elenco" è uno strumento prezioso per automatizzare le azioni in base al fatto che un paese faccia parte di un gruppo predefinito. Confrontando i dati del paese con un elenco di paesi consentiti o limitati, questa carta migliora l'efficienza del flusso di lavoro e garantisce che i processi di sistema seguano le corrette regole geografiche.
