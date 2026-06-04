# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Scopo:

La scheda di workflow **"AI Calculation for Cost Increase Surcharges"** utilizza l'AI per calcolare automaticamente gli importi dei sovrapprezzi in base agli aumenti dei costi. Garantisce calcoli dei sovrapprezzi coerenti e accurati, semplificando i workflow e riducendo lo sforzo manuale.

## Componenti della scheda:

* **Cost Increase Factor**
  * **Descrizione:** Il moltiplicatore o la percentuale applicati al costo base per calcolare il sovrapprezzo.
  * **Dettaglio:** Determina l'importo del sovrapprezzo in base all'aumento del costo (es. un fattore di 1,10 per un aumento del 10%).
* **Base Cost Field**
  * **Descrizione:** Il campo contenente il valore del costo originale utilizzato come base per il calcolo del sovrapprezzo.
  * **Dettaglio:** Selezionato automaticamente o definito all'interno del workflow come riferimento durante il calcolo.
* **Surcharge Field**
  * **Descrizione:** Il campo in cui viene memorizzato il valore del sovrapprezzo calcolato dall'AI.
  * **Dettaglio:** Questo campo riflette il sovrapprezzo calcolato, rendendolo disponibile per ulteriori elaborazioni o reportistica.

## Funzionalità:

**Valutazione della condizione:**

* La scheda si attiva solo se entrambe le condizioni delle sezioni **"Where"** e **"And"** risultano vere.
* Se una delle condizioni risulta falsa, non viene eseguito alcun calcolo del sovrapprezzo.

**Calcolo guidato dall'AI:**

* Il sistema applica il **Cost Increase Factor** al **Base Cost Field** per calcolare il sovrapprezzo.
* Il risultato viene memorizzato nel **Surcharge Field**, garantendone l'accessibilità per i passaggi successivi del workflow.

## Conclusione:

La scheda di workflow **"AI Calculation for Cost Increase Surcharges"** automatizza l'applicazione dei sovrapprezzi in base agli aumenti dei costi. Sfruttando l'AI per precisione e coerenza, questa scheda elimina i calcoli manuali, migliora l'efficienza e supporta una gestione accurata dei costi nei workflow automatizzati.
