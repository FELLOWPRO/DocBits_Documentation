# Caso 14: Riga di addebito - Addebito per unità fuori tolleranza (Approvato)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La tariffa per unità è fuori tolleranza ma è stata approvata.

## Azione:

Il sistema accetta l'addebito per unità e applica gli addebiti approvati, elaborando la transazione di conseguenza.

## Esempio:

* **Purchase Order (PO):**
  * Charge Per Unit: $4.50
  * Quantity: 1,000 units
  * Total Charge Amount: $4,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.00 — 11.11% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 1,000 units
  * Total Charge Amount: $5,000.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Poiché il Charge Per Unit ($5.00) non rientra nell'intervallo di tolleranza accettabile del 5% ma è stato approvato, il sistema:

1. **Accetta l'addebito approvato per unità:** Il sistema accetta l'addebito fatturato per unità di $5.00 poiché è stato approvato nonostante il superamento del limite di tolleranza.
2. **Elabora la transazione:** Il sistema elabora la fattura utilizzando la spesa unitaria approvata e la quantità:
   * **Total Charge Amount = Quantity × Approved Charge Per Unit**
   * **Total Charge Amount = 1,000 units × $5.00 = $5,000.00**
3. **Finalizza la fattura:** Il sistema elabora la transazione con le spese approvate, riflettendo l'importo totale di $5,000.00.

Questo approccio garantisce che il sistema possa accogliere le variazioni approvate delle tariffe, consentendo flessibilità pur mantenendo registrazioni finanziarie accurate.
