# Caso 4, 5: Quantità entro la tolleranza, Prezzo unitario fuori tolleranza (Approvato)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

La quantità sulla fattura rientra nella tolleranza, ma il prezzo unitario non rientra nell'intervallo di tolleranza accettabile. Tuttavia, questa variazione del prezzo unitario è stata esaminata e approvata dalle autorità competenti.

## Azione:

Il sistema rettifica il prezzo unitario in modo che corrisponda all'ordine d'acquisto e applica eventuali addebiti di riga necessari per tenere conto della differenza.

## Esempio:

**Purchase Order (PO):**

Quantity: <mark style="color:green;">100</mark> units

Prezzo unitario: $10.00 per unità

Total Amount: <mark style="color:purple;">$1,000.00</mark>

**Invoice Received:**

Quantità: <mark style="color:green;">100</mark> unità (entro la tolleranza)

Prezzo unitario: <mark style="color:red;">$11.00</mark> per unità (tolleranza esterna di ±5%)

Total Amount: <mark style="color:red;">$1,100.00</mark>

**Tolerance Levels:**

Quantity Tolerance: ±2%

Tolleranza prezzo unitario: ±5% (intervallo previsto: da $9.50 a $10.50)

**Approval:**

• Il prezzo unitario di $11.00 non rientra nell'intervallo di tolleranza ma è stato approvato manualmente dal reparto appropriato.

Poiché la quantità rientra nella tolleranza ma il prezzo unitario è fuori tolleranza (comunque approvato), il sistema:

1\. **Adegua il prezzo unitario**: il sistema adegua il prezzo unitario al prezzo unitario di PO perché la varianza è stata approvata:

• **Prezzo unitario rettificato = $10.00 per unitàà**

• **Importo totale rettificato = 100 unità × $10.00 per unitàà = $1,000.00**

2\. **Applica un addebito di riga per la differenza**: poiché il prezzo unitario approvato di $11.00 è superiore al prezzo unitario PO di $10.00, il sistema applica un addebito di riga per tenere conto di questa differenza:

• **Importo addebito riga = (Prezzo unitario della fattura approvata - PO Prezzo unitario) × Quantità**

• **Importo addebito linea = ($11.00 - $10.00) × 100 unità = $100.00**

3\. **Elabora la fattura**: Il sistema elabora la fattura con:

• **Base Amount:** $1,000.00

• **Line Charge:** $100.00

• **Importo totale elaborato:** $1,100.00

Ciò garantisce che, mentre i valori di base PO siano mantenuti per coerenza, la variazione approvata del prezzo unitario venga contabilizzata attraverso un addebito di riga aggiuntivo, con conseguente elaborazione finanziaria e tenuta dei registri accurati.
