# Data di consegna confermata

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-63b0722ae913-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati.</p></figcaption></figure>

## **Scopo**

Questa scheda di workflow è progettata per verificare che le date di consegna confermate su fatture o documenti di spedizione siano allineate alle date di consegna accettate definite in una tabella di lookup dei dati anagrafici. Confrontando queste date, aiuta a garantire la conformità ai programmi di consegna concordati e migliora l'affidabilità della supply chain.

## **Componenti della scheda**

1. **Operatore**
   * **Descrizione:** Definisce la condizione per confrontare la data di consegna confermata con la data di consegna accettata.
   * **Opzioni:**
     * **Is:** Conferma che la data di consegna corrisponda alla data di consegna accettata nei dati anagrafici.
     * **Non è:** Garantisce che la data di consegna non corrisponda alla data di consegna accettata nei dati anagrafici.
2. **Ricerca tabella dati principali**
   * **Descrizione:** Specifica la tabella di riferimento contenente le date di consegna accettate per il confronto.
   * **Dettaglio:** La tabella è definita dal parametro **Tabella dei dati anagrafici** e può includere metadati aggiuntivi come numeri d'ordine o regioni di consegna.

## **Funzionalità**

* **Confronto di date:** Il sistema confronta la data di consegna confermata della fattura o del documento di spedizione con la data di consegna accettata nella tabella di lookup dei dati anagrafici specificata.
* **Esecuzione dell'azione:** In base al risultato del confronto, la scheda può attivare azioni di follow-up come notifiche.

## **Configurazione e impostazione**

* Per configurare questa scheda, gli utenti selezionano il campo che rappresenta la data di consegna confermata nel documento e specificano la tabella di lookup dei dati anagrafici contenente le date di consegna accettate. Viene quindi scelto un operatore per definire come confrontare le due date (es. **Is** o **Non lo è**).

## **Scenario di esempio**

* Una fattura indica una data di consegna confermata del 10 giugno, mentre la tabella di lookup dei dati anagrafici specifica una data di consegna accettata del 15 giugno. Utilizzando l'operatore **Non lo è**, la scheda segnala la discrepanza per la revisione, consentendo al team logistico di indagare sulla causa e adeguare i programmi di conseguenza.

## **Conclusione**

La scheda di workflow **"Data di consegna confermata rispetto a data di consegna accettata"** aiuta le organizzazioni a mantenere l'aderenza ai programmi di consegna concordati automatizzando il confronto tra le date di consegna confermate e accettate. Questo approccio proattivo alla gestione delle consegne migliora l'efficienza operativa, riduce i ritardi e favorisce una migliore collaborazione lungo la supply chain.
