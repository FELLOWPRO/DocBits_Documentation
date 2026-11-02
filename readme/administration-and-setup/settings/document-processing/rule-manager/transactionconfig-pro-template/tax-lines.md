# Righe d’imposta

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

Gestisce le discrepanze negli importi delle imposte tra la fattura e l'ordine di acquisto.

## Azione:

Il sistema adegua le linee fiscali in base alle aliquote e agli importi fiscali approvati, garantendo il rispetto delle normative fiscali applicabili.

## Esempio:

* **Purchase Order (PO):**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 8%
  * Importo fiscale previsto: $800.00
  * Importo totale con tasse: $10,800.00
* **Invoice Received:**
  * Subtotal Amount: $10,000.00
  * Aliquota fiscale: 10% (discrepanza)
  * Importo imposta fatturato: $1,000.00
  * Importo totale con tasse: $11,000.00

Poiché l'aliquota fiscale sulla fattura (10%) differisce dall'aliquota fiscale prevista (8%) e non è approvata, il sistema:

1. **Rifiutare l'aliquota fiscale fatturata:** Il sistema non accetta l'aliquota fiscale del 10% perché non corrisponde all'aliquota approvata nell'ordine d'acquisto.
2. **Rettifica l'aliquota fiscale:** Il sistema rettifica l'aliquota fiscale in modo che corrisponda all'aliquota approvata dall'ordine di acquisto.
   * Aliquota fiscale rettificata = 8% (da PO)
3. **Ricalcola l'importo dell'imposta:** Il sistema ricalcola l'importo dell'imposta in base all'aliquota fiscale rettificata:
   * **Importo fiscale corretto = Importo totale parziale × Aliquota fiscale corretta**
   * **Importo fiscale corretto = $10,000.00 × 8% = $800.00**
4. **Ricalcola l'importo totale:** Il sistema ricalcola l'importo totale comprensivo delle tasse:
   * **Importo totale corretto con imposta = Importo subtotale + Importo imposta corretto**
   * **Importo totale corretto con imposte = $10,000.00 + $800.00 = $10,800.00**
5. **Genera una nota di credito:** Il sistema genera una nota di credito per correggere l'imposta sovraccaricata:
   * **Importo della nota di credito = Importo dell'imposta sulla fattura originale - Importo dell'imposta corretto**
   * **Importo della nota di credito = $1,000.00 - $800.00 = $200.00**
6. **Elabora la fattura:** Il sistema elabora la fattura con l'importo fiscale corretto di $800.00 e l'importo totale di $10,800.00, emettendo una nota di accredito per la discrepanza fiscale di $200.00.

Questo approccio garantisce che l'imposta sulla fattura sia coerente con l'ordine di acquisto e sia conforme alle normative fiscali applicabili, prevenendo pagamenti in eccesso e garantendo l'accuratezza dei registri finanziari.
