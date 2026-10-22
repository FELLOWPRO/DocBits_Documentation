# Caso 14: Addebito di intestazione - Addebito per unità fuori tolleranza (Approvato)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

L'addebito dell'intestazione per unità è fuori tolleranza ma è stato approvato.

## Azione:

Il sistema elabora l'addebito unitario approvato, applicandolo alla transazione.

## Esempio:

* **Purchase Order (PO):**
  * Costo di intestazione per unità: $2.50
  * Quantity: 2,000 units
  * Importo totale addebito intestazione: $5,000.00
* **Invoice Received:**
  * Addebito di intestazione per unità: $3.00 (tolleranza esterna del 20%, approvata)
  * Quantity: 2,000 units
  * Importo totale addebito intestazione: $6,000.00
* **Tolerance Levels:**
  * Tolleranza addebito intestazione per unità: ±5%

Poiché l'addebito dell'intestazione per unità ($3.00) supera l'intervallo di tolleranza accettabile del 5% ma è stato approvato, il sistema:

1. **Accetta l'addebito dell'intestazione approvata per unitàà:** Il sistema accetta l'addebito dell'intestazione fatturata per unità di $3.00 poiché è stato approvato nonostante il superamento del limite di tolleranza.
2. **Elabora l'addebito di testata:** Il sistema elabora la fattura utilizzando l'addebito unitario approvato e la quantità:
   * **Importo totale addebito intestazione = Quantità × Addebito intestazione approvato per unitàà**
   * **Importo totale addebito intestazione = 2,000 unità × $3.00 = $6,000.00**
3. **Finalizza la fattura:** Il sistema elabora la transazione con le spese approvate, riflettendo l'importo totale di $6,000.00.

Questo approccio consente al sistema di accogliere le variazioni approvate nelle spese di intestazione, garantendo che la transazione venga elaborata in base all'approvazione mantenendo allo stesso tempo registri finanziari accurati.
