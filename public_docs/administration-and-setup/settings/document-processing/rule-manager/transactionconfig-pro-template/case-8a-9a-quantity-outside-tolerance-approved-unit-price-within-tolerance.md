# Caso 8a, 9a: Quantità fuori tolleranza (Approvato), Prezzo unitario entro la tolleranza

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La quantità sulla fattura non rientra nella tolleranza accettabile ma è stata approvata, mentre il prezzo unitario rimane entro la tolleranza.

## Azione:

Il sistema accetta la quantità approvata e il prezzo unitario come da fattura ed elabora la transazione di conseguenza.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $12.00 per unit
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Quantity: 160 units — 6.67% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $12.00 per unit (within tolerance)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Poiché la quantità (160 unità) supera il limite di tolleranza accettabile ma è stata approvata e il prezzo unitario ($12.00) rientra nell'intervallo accettabile, il sistema:

1. **Accept the Approved Quantity:** Il sistema riconosce che la quantità è stata approvata nonostante sia al di fuori del normale intervallo di tolleranza.
2. **Accept the Unit Price:** Il prezzo unitario di $12.00 per unità rientra nella tolleranza accettabile, quindi viene accettato come fatturato.
3. **Process the Transaction:** Il sistema calcola l'importo totale utilizzando la quantità approvata e il prezzo unitario:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 160 units × $12.00 per unit = $1,920.00**
4. **Finalize the Invoice:** Il sistema elabora la fattura con l'importo totale di $1,920.00, riflettendo la quantità approvata e il prezzo unitario accettato.

Questo approccio consente al sistema di accogliere le variazioni approvate nella quantità garantendo al tempo stesso che il prezzo unitario rimanga all'interno dell'intervallo previsto, facilitando l'elaborazione regolare delle transazioni.
