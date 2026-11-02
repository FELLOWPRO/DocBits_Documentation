# Caso 8a, 9a: Quantità fuori tolleranza (Approvato), Prezzo unitario entro la tolleranza

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La quantità sulla fattura non rientra nella tolleranza accettabile ma è stata approvata, mentre il prezzo unitario rimane entro la tolleranza.

## Azione:

Il sistema accetta la quantità approvata e il prezzo unitario come da fattura ed elabora la transazione di conseguenza.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Prezzo unitario: $12.00 per unità
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Quantità: 160 unità (tolleranza esterna del 6.67% ma approvata)
  * Prezzo unitario: $12.00 per unità (entro la tolleranza)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolleranza prezzo unitario: ±2%

Poiché la quantità (160 unità) supera il limite di tolleranza accettabile ma è stata approvata e il prezzo unitario ($12.00) rientra nell'intervallo accettabile, il sistema:

1. **Accetta la quantità approvata:** Il sistema riconosce che la quantità è stata approvata nonostante sia al di fuori del normale intervallo di tolleranza.
2. **Accetta il prezzo unitario:** Il prezzo unitario di $12.00 per unità rientra nella tolleranza accettabile, quindi viene accettato come fatturato.
3. **Elabora la transazione:** Il sistema calcola l'importo totale utilizzando la quantità approvata e il prezzo unitario:
   * **Importo totale = Quantità × Prezzo unitario**
   * **Importo totale = 160 unità × $12.00 per unitàà = $1,920.00**
4. **Finalizza la fattura:** Il sistema elabora la fattura con l'importo totale di $1,920.00, riflettendo la quantità approvata e il prezzo unitario accettato.

Questo approccio consente al sistema di accogliere le variazioni approvate nella quantità garantendo al tempo stesso che il prezzo unitario rimanga all'interno dell'intervallo previsto, facilitando l'elaborazione regolare delle transazioni.
