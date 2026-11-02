# Caso 10b: Difetto di quantità e prezzo oltre tolleranza, entrambi rifiutati

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

Sia la quantità che il prezzo unitario sono fuori tolleranza e nessuno dei due è stato approvato.

## Azione:

Il sistema rifiuta i dati della fattura, rettifica i valori in modo che corrispondano all'ordine d'acquisto e genera le note di addebito o accredito necessarie.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Prezzo unitario: $30.00 per unità
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Quantità: 140 unità (tolleranza esterna di -6.67%, rifiutata)
  * Prezzo unitario: $33.00 per unità (fuori tolleranza del 10%, rifiutato)
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolleranza prezzo unitario: ±2%

Poiché sia la quantità (140 unità) che il prezzo unitario ($33.00) non rientrano nei limiti di tolleranza accettabili e nessuno dei due è stato approvato, il sistema:

1. **Rifiuta i dati della fattura:** Il sistema non accetta la quantità fatturata o il prezzo unitario a causa della loro deviazione dai limiti di tolleranza.
2. **Rettifica la quantità:** Il sistema rettifica la quantità in modo che corrisponda alla quantità dell'ordine d'acquisto originale.
   * Quantità rettificata = 150 unità (da PO)
3. **Rettifica il prezzo unitario:** Il sistema rettifica il prezzo unitario in modo che corrisponda al prezzo unitario dell'ordine di acquisto originale.
   * Prezzo unitario rettificato = $30.00 per unità (da PO)
4. **Ricalcola l'importo totale:** Il sistema ricalcola l'importo totale utilizzando la quantità rettificata e il prezzo unitario:
   * **Importo totale corretto = Quantità rettificata × Prezzo unitario rettificato**
   * **Importo totale corretto = 150 unità × $30.00 per unitàà = $4,500.00**
5. **Genera una nota di addebito:** Poiché il totale della fattura originale era superiore al totale corretto, il sistema genera una nota di addebito per l'importo addebitato in eccesso.
   * **Importo della nota di addebito = Totale della fattura originale - Importo totale corretto**
   * **Importo della nota di addebito = $4,620.00 - $4,500.00 = $120.00**
6. **Elabora la fattura:** Il sistema elabora la fattura con l'importo totale corretto di $4,500.00 ed emette una nota di addebito per $120.00 per compensare l'importo in eccesso.

Questo approccio garantisce che la transazione finanziaria venga corretta per corrispondere ai termini dell'ordine di acquisto, mantenendo pratiche di fatturazione accurate ed eque.
