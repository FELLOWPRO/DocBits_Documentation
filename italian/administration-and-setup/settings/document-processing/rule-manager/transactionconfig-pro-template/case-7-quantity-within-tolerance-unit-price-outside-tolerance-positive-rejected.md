# Caso 7: Quantità entro tolleranza, eccesso del prezzo unitario rifiutato

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La quantità rientra nella tolleranza, ma il prezzo unitario supera l'intervallo accettabile (tolleranza positiva) e non è approvato.

## Azione:

Il sistema rifiuta il prezzo unitario della fattura, lo rettifica per corrispondere all'ordine di acquisto e può generare una nota di addebito per tenere conto dell'importo in eccesso.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Prezzo unitario: $15.00 per unità
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantità: 198 unità (con tolleranza dell'1%)
  * Prezzo unitario: $17.00 per unità (fuori tolleranza positiva del 13.33%)
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Tolleranza prezzo unitario: ±1%

Poiché la quantità (198 unità) rientra nell'intervallo di tolleranza accettabile ma il prezzo unitario ($17.00) supera la tolleranza accettabile e non è approvato, il sistema:

1. **Rifiutare il prezzo unitario della fattura:** Il sistema non accetta il prezzo unitario fatturato di $17.00.
2. **Rettifica il prezzo unitario:** Il sistema rettifica il prezzo unitario in modo che corrisponda al prezzo unitario dell'ordine di acquisto originale.
   * Prezzo unitario rettificato = $15.00 (da PO)
3. **Calcola l'importo totale corretto:** Utilizzando il prezzo unitario rettificato, il sistema ricalcola l'importo totale.
   * **Importo totale corretto = Quantità × Prezzo unitario rettificato**
   * **Importo totale corretto = 198 unità × $15.00 per unitàà = $2,970.00**
4. **Genera una nota di addebito:** Il sistema genera una nota di addebito per tenere conto della differenza dovuta al sovrapprezzo.
   * **Importo della nota di addebito = Totale della fattura originale - Importo totale corretto**
   * **Importo della nota di addebito = $3,366.00 - $2,970.00 = $396.00**
   * Questa nota di addebito rappresenta l'importo addebitato in eccesso dal fornitore.
5. **Elabora la fattura:** Il sistema elabora la fattura con l'importo totale corretto di $2,970.00 ed emette una nota di addebito per $396.00 per compensare il sovrapprezzo.

Questo approccio garantisce che eventuali sovrapprezzi vengano corretti, allineando la transazione ai termini dell'ordine di acquisto e tutelando gli interessi finanziari dell'azienda.
