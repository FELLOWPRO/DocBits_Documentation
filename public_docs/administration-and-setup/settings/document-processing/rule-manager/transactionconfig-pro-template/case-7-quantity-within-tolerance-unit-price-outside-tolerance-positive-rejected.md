# Caso 7: Quantità entro tolleranza, prezzo unitario fuori tolleranza (rifiuto in positivo)

Lo scenario seguente è una mappatura configurata a scopo illustrativo, non un modello predefinito distribuito e verificato. L'output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di addebito o di credito descritta di seguito è subordinata a tale configurazione; l'esempio non garantisce l'emissione automatica né la conformità legale.

## Scenario:

La quantità rientra nella tolleranza, ma il prezzo unitario supera l'intervallo accettabile (tolleranza positiva) e non è approvato.

## Azione:

Il sistema rifiuta il prezzo unitario della fattura, lo rettifica per allinearlo all'ordine di acquisto e può generare una nota di addebito per tenere conto dell'importo addebitato in eccesso.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $15.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 198 units — 1% below the PO value, within the configured ±2% tolerance.
  * Unit Price: $17.00 per unit — 13.33% above the PO value, outside the configured ±1% tolerance; rejected.
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Poiché la quantità (198 unità) rientra nell'intervallo di tolleranza accettabile ma il prezzo unitario ($17.00) supera la tolleranza accettabile e non è approvato, il sistema:

1. **Rifiuta il prezzo unitario della fattura:** il sistema non accetta il prezzo unitario fatturato di $17.00.
2. **Rettifica il prezzo unitario:** il sistema rettifica il prezzo unitario per allinearlo al prezzo unitario dell'ordine di acquisto originale.
   * Prezzo unitario rettificato = $15.00 (dal PO)
3. **Calcola l'importo totale corretto:** usando il prezzo unitario rettificato, il sistema ricalcola l'importo totale.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 198 units × $15.00 per unit = $2,970.00**
4. **Genera una nota di addebito:** il sistema genera una nota di addebito per tenere conto della differenza dovuta all'addebito in eccesso.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $3,366.00 - $2,970.00 = $396.00**
   * Questa nota di addebito rappresenta l'importo addebitato in eccesso dal fornitore.
5. **Elabora la fattura:** il sistema elabora la fattura con l'importo totale corretto di $2,970.00 ed emette una nota di addebito di $396.00 per compensare l'addebito in eccesso.

Questo approccio garantisce che qualsiasi addebito in eccesso venga corretto, allineando la transazione ai termini dell'ordine di acquisto e tutelando gli interessi finanziari dell'azienda.
