# Addebito per unità fuori tolleranza (Rifiutato)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

Il Charge Per Unit è fuori tolleranza e non è stato approvato.

## Azione:

Il sistema adegua il Charge Per Unit in modo che corrisponda all'ordine di acquisto o ai livelli approvati, generando eventuali note di addebito o accredito necessarie.

## Esempio:

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 (variazione 16.67%, fuori dalla tolleranza del ±5%, rifiutato)
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Poiché Charge Per Unit ($7.00) supera l'intervallo di tolleranza accettabile del 5% e non è stato approvato, il sistema:

1. **Reject the Invoiced Charge Per Unit:** Il sistema non accetta il Charge Per Unit fatturato di $7.00 a causa della varianza che supera il limite di tolleranza.
2. **Adjust the Charge Per Unit:** Il sistema adegua il Charge Per Unit in modo che corrisponda all'ordine di acquisto o al Charge Per Unit approvato:
   * Adjusted Charge Per Unit = $6.00 (da PO)
3. **Recalculate the Total Charge Amount:** Il sistema ricalcola il Total Charge Amount in base al Charge Per Unit modificato:
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** Poiché il totale della fattura originale era superiore al totale corretto, il sistema genera una nota di addebito per l'importo in eccesso:
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** Il sistema elabora la fattura con il Total Charge Amount corretto di $4,800.00 ed emette una nota di addebito per $800.00 per tenere conto dell'importo addebitato in eccesso.

Questo approccio garantisce che le transazioni finanziarie siano coerenti con i termini dell'ordine di acquisto, rifiutando variazioni non approvate e mantenendo pratiche di fatturazione accurate.
