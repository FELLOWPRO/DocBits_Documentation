# Addebito per unità entro la tolleranza

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

L'addebito dell'intestazione per unità rientra nell'intervallo di tolleranza accettabile rispetto all'ordine di acquisto.

## Azione:

Il sistema elabora l'addebito della testata come fatturato, applicandolo senza rettifiche.

## Esempio:

* **Purchase Order (PO):**
  * Costo di intestazione per unità: $3.50
  * Quantity: 1,200 units
  * Importo totale addebito intestazione: $4,200.00
* **Invoice Received:**
  * Addebito di intestazione per unità: $3.55 (entro la tolleranza dell'1.43%)
  * Quantity: 1,200 units
  * Importo totale addebito intestazione: $4,260.00
* **Tolerance Levels:**
  * Tolleranza addebito intestazione per unità: ±2%

Poiché l'addebito di testata per unità ($3.55) rientra nell'intervallo di tolleranza accettabile del 2% rispetto all'ordine di acquisto, il sistema:

1. **Accetta l'addebito di intestazione per unitàà:** Il sistema accetta l'addebito di intestazione fatturato per unità di $3.55 poiché rientra nel limite di tolleranza definito.
2. **Elabora l'addebito di intestazione:** Il sistema elabora la fattura con l'importo totale dell'addebito di intestazione in base all'addebito fatturato per unità e quantità:
   * **Importo totale addebito intestazione = Quantità × Addebito intestazione per unitàà**
   * **Importo totale addebito intestazione = 1,200 unità × $3.55 = $4,260.00**
3. **Finalizza la fattura:** Il sistema elabora la transazione senza alcuna rettifica, accettando la fattura così com'è.

Questo approccio garantisce un'elaborazione fluida ed efficiente delle transazioni quando le spese di intestazione rientrano nell'intervallo di tolleranza accettabile, evitando rifiuti o ritardi inutili.
