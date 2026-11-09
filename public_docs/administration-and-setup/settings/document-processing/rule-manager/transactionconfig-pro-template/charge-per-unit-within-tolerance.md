# Addebito per unità entro la tolleranza

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

Il Charge Per Unit sulla fattura rientra nell'intervallo di tolleranza accettabile rispetto all'ordine di acquisto.

## Azione:

Il sistema accetta il Charge Per Unit come fatturato ed elabora la transazione senza rettifiche.

## Esempio:

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 (variance 2%, within the ±3% tolerance)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Poiché il Charge Per Unit ($5.10) rientra nell'intervallo di tolleranza accettabile del 3% rispetto all'ordine di acquisto, il sistema:

1. **Accept the Charge Per Unit:** Il sistema accetta il Charge Per Unit fatturato di $5.10 poiché rientra nel limite di tolleranza definito.
2. **Process the Transaction:** Il sistema elabora la fattura con il Total Charge Amount in base al Charge Per Unit fatturato e alla Quantity:
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:** Il sistema elabora la transazione senza alcuna rettifica, accettando la fattura così com'è.

Questo approccio consente al sistema di accogliere piccole variazioni accettabili delle tariffe, garantendo un'elaborazione regolare ed efficiente delle transazioni senza inutili rifiuti o ritardi.
