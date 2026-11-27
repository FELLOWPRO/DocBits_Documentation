# Caso 10a: Difetto di quantità rifiutato, prezzo unitario entro tolleranza

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La quantità è inferiore all'intervallo accettabile (tolleranza negativa) e non è approvata, sebbene il prezzo unitario rientri nella tolleranza.

## Azione:

Il sistema adegua la quantità in modo che corrisponda al livello approvato, mantenendo coerente il prezzo unitario. La transazione viene elaborata di conseguenza.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $20.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $20.00 per unit (within tolerance)
  * Total Amount: $2,800.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Poiché la quantità (140 unità) è inferiore al limite di tolleranza accettabile (varianza negativa di -6.67%) e non è approvata, ma il prezzo unitario ($20.00) rientra nella tolleranza, il sistema:

1. **Rifiuta la quantità inferiore:** Il sistema non accetta la quantità inferiore poiché non rientra nell'intervallo di tolleranza approvato.
2. **Rettifica la quantità:** Il sistema rettifica la quantità in modo che corrisponda al livello approvato specificato nell'ordine d'acquisto.
   * Approved Quantity = 150 units (from PO)
3. **Mantenere il prezzo unitario:** Il prezzo unitario di $20.00 per unità rientra nella tolleranza e rimane invariato.
4. **Ricalcola l'importo totale:** Il sistema calcola l'importo totale utilizzando la quantità approvata e il prezzo unitario accettato:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 150 units × $20.00 per unit = $3,000.00**
5. **Elabora la fattura:** Il sistema elabora la fattura con l'importo totale rettificato di $3,000.00, che riflette la quantità approvata e il prezzo unitario. Il fornitore è tenuto a fatturare l'intera quantità approvata.

Questo approccio garantisce che la transazione finanziaria sia in linea con i termini dell'ordine di acquisto e previene la sottofatturazione mantenendo allo stesso tempo registri finanziari accurati.
