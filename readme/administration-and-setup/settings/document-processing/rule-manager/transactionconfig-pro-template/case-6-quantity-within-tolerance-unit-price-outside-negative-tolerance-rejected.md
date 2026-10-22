# Caso 6: Quantità entro tolleranza, prezzo sotto il limite (rifiutato)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario

La quantità è entro tolleranza, ma il prezzo unitario della fattura è inferiore all’intervallo consentito e lo scostamento di prezzo non è stato approvato.

## Azione illustrativa

Una mappatura configurata per usare il prezzo del PO dopo il rifiuto manterrebbe la quantità e sostituirebbe il prezzo unitario fatturato con quello del PO. L’eventuale produzione di una rettifica, di una nota di debito, di una nota di credito o di nessun documento separato dipende dalla mappatura attiva e dalle approvazioni. Gli oneri aggiuntivi di testata si applicano solo se espressamente configurati.

## Esempio

* **Ordine di acquisto (PO):**
  * Quantità: 100 unità
  * Prezzo unitario: $10.00 per unità
  * Totale: $1,000.00
* **Fattura ricevuta:**
  * Quantità: 100 unità — scostamento effettivo 0%, entro la tolleranza configurata di ±2%.
  * Prezzo unitario: $9.00 — scostamento effettivo -10%, fuori dalla tolleranza configurata di ±1%; rifiutato.
  * Totale: $900.00
* **Tolleranze configurate:**
  * Quantità: ±2%
  * Prezzo unitario: ±1%

In questa mappatura illustrativa:

1. Rifiutare il prezzo unitario fatturato di $9.00 perché lo scostamento supera la tolleranza e non è approvato.
2. Utilizzare il prezzo unitario del PO di $10.00.
3. Ricalcolare il totale dell’esempio: **100 unità × $10.00 = $1,000.00**.
4. Calcolare lo scostamento con segno come totale fatturato meno totale ricalcolato: **$900.00 - $1,000.00 = -$100.00**.
5. Applicare la mappatura di esportazione e la decisione di approvazione configurate. Il valore -$100.00 è uno scostamento con segno, non un’istruzione incondizionata a emettere una nota di credito. La mappatura determina importo, segno e tipo di documento di ogni rettifica.

L’esempio non indica che una nota di credito annulli automaticamente un importo fatturato in difetto. Verificare il trattamento contabile previsto nella mappatura di esportazione attiva prima di utilizzare la regola.
