# Addebito per unità fuori tolleranza (Rifiutato)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La tariffa per unità è fuori tolleranza e non è stata approvata.

## Azione:

Il sistema adegua l'addebito per unità in modo che corrisponda all'ordine di acquisto o ai livelli approvati, generando eventuali note di addebito o accredito necessarie.

## Esempio:

* **Purchase Order (PO):**
  * Costo per unità: $6.00
  * Quantity: 800 units
  * Importo totale della commissione: $4,800.00
* **Invoice Received:**
  * Addebito per unità: $7.00 (fuori tolleranza del 16.67%, rifiutato)
  * Quantity: 800 units
  * Importo totale della commissione: $5,600.00
* **Tolerance Levels:**
  * Tolleranza tariffa per unità: ±5%

Poiché l'addebito per unità ($7.00) supera l'intervallo di tolleranza accettabile del 5% e non è stato approvato, il sistema:

1. **Rifiutare l'addebito fatturato per unitàà:** Il sistema non accetta l'addebito fatturato per unità di $7.00 a causa della varianza che supera il limite di tolleranza.
2. **Rettifica l'addebito per unitàà:** Il sistema adegua l'addebito per unità in modo che corrisponda all'ordine di acquisto o all'addebito per unità approvato:
   * Commissione rettificata per unità = $6.00 (da PO)
3. **Ricalcola l'importo totale della tariffa:** Il sistema ricalcola l'importo totale della tariffa in base alla tariffa modificata per unità:
   * **Importo totale corretto = Quantità × Addebito rettificato per unitàà**
   * **Importo totale corretto = 800 unità × $6.00 = $4,800.00**
4. **Genera una nota di addebito:** Poiché il totale della fattura originale era superiore al totale corretto, il sistema genera una nota di addebito per l'importo in eccesso:
   * **Importo della nota di addebito = Totale della fattura originale - Importo totale dell'addebito corretto**
   * **Importo della nota di addebito = $5,600.00 - $4,800.00 = $800.00**
5. **Elabora la fattura:** Il sistema elabora la fattura con l'importo dell'addebito totale corretto di $4,800.00 ed emette una nota di addebito per $800.00 per tenere conto dell'importo addebitato in eccesso.

Questo approccio garantisce che le transazioni finanziarie siano coerenti con i termini dell'ordine di acquisto, rifiutando variazioni non approvate e mantenendo pratiche di fatturazione accurate.
