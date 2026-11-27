# Caso 1, 2, 3: Quantità e prezzo unitario entro la tolleranza

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

Sia la quantità che il prezzo unitario sulla fattura rientrano in un intervallo di tolleranza accettabile rispetto all'ordine di acquisto.

## Azione:

Il sistema accetta i valori della fattura e calcola l'importo totale in base alla quantità fornita e al prezzo unitario.

## Esempio:

**Purchase Order (PO):**

Quantity: 100 units

Unit Price: $10.00 per unit

Total Amount: $1,000.00

**Invoice Received:**

Quantity: 101 units — 1% above the PO value, within the configured ±2% tolerance.

Unit Price: $10.05 per unit — 0.5% above the PO value, within the configured ±1% tolerance.

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±1%


Poiché la quantità (101 unità) e il prezzo unitario ($10.05) rientrano entrambi nei livelli di tolleranza accettabili rispetto all'ordine di acquisto, il sistema:


1\. **Accetta i valori della fattura:** La quantità e il prezzo unitario sulla fattura vengono accettati come validi perché rientrano nei limiti di tolleranza definiti.

2\. **Calcola l'importo totale:** L'importo totale viene calcolato utilizzando i valori accettati:

• Total Amount = Quantity × Unit Price

• Total Amount = 101 units × $10.05 per unit = $1,015.05

3\. **Elabora la fattura:** La fattura viene elaborata con l'importo totale di $1,015.05 e i record finanziari vengono aggiornati di conseguenza.

Questo approccio garantisce che discrepanze minori che rientrano entro livelli di tolleranza accettabili non portino al rifiuto delle fatture o a ritardi nei pagamenti, snellendo così il processo finanziario.
