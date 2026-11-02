# Caso 15: Addebito di intestazione - Addebito per unità fuori tolleranza (Rifiutato)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

L'addebito dell'intestazione per unità è fuori tolleranza e non è stato approvato.

## Azione:

Il sistema adegua l'addebito dell'intestazione in modo che corrisponda all'ordine d'acquisto, elaborando la transazione di conseguenza e generando le eventuali note necessarie.

## Esempio:

* **Purchase Order (PO):**
  * Costo dell'intestazione per unità: $4.00
  * Quantity: 1,500 units
  * Importo totale addebito intestazione: $6,000.00
* **Invoice Received:**
  * Addebito intestazione per unità: $5.00 (fuori tolleranza del 25%, rifiutato)
  * Quantity: 1,500 units
  * Importo totale addebito intestazione: $7,500.00
* **Tolerance Levels:**
  * Tolleranza addebito intestazione per unità: ±5%

Poiché l'addebito dell'intestazione per unità ($5.00) supera l'intervallo di tolleranza accettabile del 5% e non è stato approvato, il sistema:

1. **Rifiutare l'addebito dell'intestazione fatturata per unitàà:** Il sistema non accetta l'addebito dell'intestazione fatturata per unità di $5.00 a causa della varianza che supera il limite di tolleranza.
2. **Rettifica l'addebito di intestazione per unitàà:** Il sistema adegua l'addebito per unità in modo che corrisponda all'ordine di acquisto originale o all'addebito per unità approvato:
   * Addebito di intestazione rettificato per unità = $4.00 (da PO)
3. **Ricalcola l'importo totale dell'addebito dell'intestazione:** Il sistema ricalcola l'importo dell'addebito totale in base all'addebito rettificato per unità:
   * **Importo totale corretto dell'addebito di intestazione = Quantità × Addebito di intestazione rettificato per unitàà**
   * **Importo totale corretto dell'addebito di intestazione = 1,500 unità × $4.00 = $6,000.00**
4. **Genera una nota di accredito:** Poiché il totale della fattura originale era superiore al totale corretto, il sistema genera una nota di accredito per l'importo in eccesso:
   * **Importo nota di credito = Totale fattura originale - Importo totale addebito intestazione corretto**
   * **Importo della nota di credito = $7,500.00 - $6,000.00 = $1,500.00**
5. **Elabora la fattura:** Il sistema elabora la fattura con l'importo dell'addebito totale corretto di $6,000.00 ed emette una nota di accredito di $1,500.00 per tenere conto dell'importo addebitato in eccesso.

Questo approccio garantisce che la transazione sia in linea con i termini originali dell'ordine di acquisto, mantenendo un'accurata elaborazione finanziaria e correggendo eventuali sovrapprezzi.
