# Caso 11b: Eccesso di quantità e prezzo oltre tolleranza, entrambi rifiutati

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La quantità supera l'intervallo accettabile (positivo) e viene rifiutata, anche il prezzo unitario è fuori tolleranza e viene rifiutato.

## Azione:

Il sistema adegua la quantità e il prezzo unitario in modo che corrispondano ai livelli approvati dall'ordine d'acquisto, rifiutando eventuali eccedenze ed elabora la transazione.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Prezzo unitario: $50.00 per unità
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Quantità: 220 unità (fuori tolleranza del 10%, rifiutata)
  * Prezzo unitario: $55.00 per unità (fuori tolleranza del 10%, rifiutato)
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolleranza prezzo unitario: ±2%

Poiché sia la quantità (220 unità) che il prezzo unitario ($55.00) superano i limiti di tolleranza accettabili e nessuno dei due è stato approvato, il sistema:

1. **Rifiutare la quantità in eccesso:** Il sistema non accetta la quantità fatturata di 220 unità e la rettifica in modo che corrisponda all'ordine d'acquisto originale.
   * Quantità rettificata = 200 unità (da PO)
2. **Rifiutare il prezzo unitario della fattura:** Il sistema non accetta il prezzo unitario fatturato di $55.00 e lo rettifica in modo che corrisponda all'ordine di acquisto originale.
   * Prezzo unitario rettificato = $50.00 per unità (da PO)
3. **Ricalcola l'importo totale:** Il sistema calcola l'importo totale utilizzando la quantità rettificata e il prezzo unitario:
   * **Importo totale corretto = Quantità rettificata × Prezzo unitario rettificato**
   * **Importo totale corretto = 200 unità × $50.00 per unitàà = $10,000.00**
4. **Elabora la fattura:** Il sistema elabora la fattura con l'importo totale corretto di $10,000.00, rifiutando la quantità in eccesso e il prezzo unitario più elevato.

Questo approccio garantisce che la transazione sia in linea con i termini originali dell'ordine di acquisto, mantenendo prezzi e quantità coerenti e rifiutando variazioni non approvate.
