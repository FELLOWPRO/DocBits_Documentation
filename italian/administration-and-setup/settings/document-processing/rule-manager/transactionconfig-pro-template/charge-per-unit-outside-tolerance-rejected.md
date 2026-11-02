# Caso 15: Oneri di riga per unità fuori tolleranza (rifiutati)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario

L’onere per unità di una riga è fuori tolleranza e lo scostamento non è stato approvato. Il caso riguarda un onere di riga, non un onere di testata.

## Azione illustrativa

Una mappatura configurata per usare l’onere del PO dopo il rifiuto sostituirebbe l’onere unitario fatturato con quello del PO. Qualsiasi rettifica o nota di debito o di credito separata dipende dalla mappatura di esportazione e dalle decisioni di approvazione.

## Esempio

* **Ordine di acquisto (PO):**
  * Onere di riga per unità: $4.00
  * Quantità: 1,500 unità
  * Totale oneri di riga: $6,000.00
* **Fattura ricevuta:**
  * Onere di riga per unità: $5.00 — 25% superiore al PO, fuori dalla tolleranza configurata di ±5%; rifiutato.
  * Quantità: 1,500 unità
  * Totale oneri di riga: $7,500.00
* **Tolleranza configurata:** Onere per unità ±5%.

In questa mappatura illustrativa:

1. Rifiutare l’onere fatturato di $5.00 per unità perché lo scostamento del 25% supera ±5% e non è approvato.
2. Utilizzare l’onere del PO di $4.00 per unità.
3. Ricalcolare il totale degli oneri di riga: **1,500 unità × $4.00 = $6,000.00**.
4. Calcolare l’eccedenza fatturata: **$7,500.00 - $6,000.00 = $1,500.00**.
5. Applicare il trattamento configurato per la differenza. Una nota di credito di $1,500.00 è un possibile risultato della mappatura, non un’azione garantita del sistema. Importo, segno, tipo di documento ed emissione dipendono dalle regole attive, dalla mappatura di esportazione e dalle approvazioni.

Convalidare la mappatura degli oneri di riga e i documenti contabili risultanti prima di utilizzare lo scenario in produzione.
