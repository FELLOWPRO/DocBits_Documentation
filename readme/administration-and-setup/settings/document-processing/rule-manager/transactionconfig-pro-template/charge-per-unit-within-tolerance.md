# Addebito per unità entro la tolleranza

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

L'addebito unitario sulla fattura rientra nell'intervallo di tolleranza accettabile rispetto all'ordine di acquisto.

## Azione:

Il sistema accetta l'addebito per unità come fatturato ed elabora la transazione senza rettifiche.

## Esempio:

* **Purchase Order (PO):**
  * Costo per unità: $5.00
  * Quantity: 500 units
  * Importo totale della commissione: $2,500.00
* **Invoice Received:**
  * Costo per unità: $5.10 (entro la tolleranza del 2%)
  * Quantity: 500 units
  * Importo totale della commissione: $2,550.00
* **Tolerance Levels:**
  * Tolleranza tariffa per unità: ±3%

Poiché l'addebito per unità ($5.10) rientra nell'intervallo di tolleranza accettabile del 3% rispetto all'ordine di acquisto, il sistema:

1. **Accetta l'addebito per unitàà:** Il sistema accetta l'addebito fatturato per unità di $5.10 poiché rientra nel limite di tolleranza definito.
2. **Elabora la transazione:** Il sistema elabora la fattura con l'importo totale dell'addebito in base all'addebito fatturato per unità e quantità:
   * **Importo addebito totale = Quantità × Addebito per unitàà**
   * **Importo totale addebitato = 500 unità × $5.10 = $2,550.00**
3. **Finalizza la fattura:** Il sistema elabora la transazione senza alcuna rettifica, accettando la fattura così com'è.

Questo approccio consente al sistema di accogliere piccole variazioni accettabili delle tariffe, garantendo un'elaborazione regolare ed efficiente delle transazioni senza inutili rifiuti o ritardi.
