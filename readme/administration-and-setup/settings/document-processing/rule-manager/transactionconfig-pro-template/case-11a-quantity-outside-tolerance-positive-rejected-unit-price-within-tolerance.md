# Caso 11a: Eccesso di quantità rifiutato, prezzo unitario entro tolleranza

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La quantità sulla fattura supera l'intervallo accettabile (positivo) e viene rifiutata, ma il prezzo unitario rientra nella tolleranza.

## Azione:

Il sistema adegua la quantità al livello approvato, mantenendo il prezzo unitario ed elabora la transazione. Qualsiasi quantità in eccesso viene rifiutata e non fatturata.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Prezzo unitario: $8.00 per unità
  * Total Amount: $800.00
* **Invoice Received:**
  * Quantità: 110 unità (fuori tolleranza del 10%, rifiutata)
  * Prezzo unitario: $8.00 per unità (entro la tolleranza)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolleranza prezzo unitario: ±2%

Poiché la quantità (110 unità) supera il limite di tolleranza accettabile (variazione positiva del 10%) e non è approvata, ma il prezzo unitario ($8.00) rientra nella tolleranza, il sistema:

1. **Rifiutare la quantità in eccesso:** Il sistema rifiuta la quantità che supera il livello di tolleranza approvato.
2. **Rettifica la quantità:** Il sistema rettifica la quantità in modo che corrisponda al livello approvato specificato nell'ordine d'acquisto.
   * Quantità approvata = 100 unità (da PO)
3. **Mantenere il prezzo unitario:** Il prezzo unitario di $8.00 per unità rientra nella tolleranza e rimane invariato.
4. **Ricalcola l'importo totale:** Il sistema calcola l'importo totale utilizzando la quantità approvata e il prezzo unitario accettato:
   * **Importo totale = Quantità approvata × Prezzo unitario**
   * **Importo totale = 100 unità × $8.00 per unitàà = $800.00**
5. **Elabora la fattura:** Il sistema elabora la fattura con l'importo totale rettificato di $800.00, riflettendo solo la quantità approvata e il prezzo unitario. La quantità in eccesso di 10 unità viene rifiutata e non fatturata.

Questo approccio garantisce che l'importo fatturato sia allineato ai termini concordati nell'ordine di acquisto, anche quando il fornitore tenta di fatturare una quantità in eccesso.
