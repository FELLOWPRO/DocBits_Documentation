# Fall 11b: Menge oberhalb der Toleranz abgelehnt, Stückpreisabweichung abgelehnt

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Menge überschreitet den zulässigen Bereich (positive Abweichung) und wird abgelehnt. Auch der Stückpreis liegt außerhalb der Toleranz und wird abgelehnt.

## Aktion:

Das System passt Menge und Stückpreis an die genehmigten Bestellwerte an, lehnt darüber hinausgehende Werte ab und verarbeitet die Transaktion.

## Beispiel:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $50.00 per unit
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $55.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Sowohl die Menge (220 Einheiten) als auch der Stückpreis ($55.00) überschreiten die zulässigen Toleranzgrenzen; keiner der Werte wurde genehmigt. Das System führt folgende Schritte aus:

1. **Reject the Excess Quantity:** Das System akzeptiert die berechnete Menge von 220 Einheiten nicht und passt sie an die ursprüngliche Bestellung an.
   * Adjusted Quantity = 200 units (from PO)
2. **Reject the Invoice Unit Price:** Das System akzeptiert den berechneten Stückpreis von $55.00 nicht und passt ihn an die ursprüngliche Bestellung an.
   * Adjusted Unit Price = $50.00 per unit (from PO)
3. **Recalculate the Total Amount:** Das System berechnet den Gesamtbetrag anhand der angepassten Menge und des angepassten Stückpreises:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 200 units × $50.00 per unit = $10,000.00**
4. **Process the Invoice:** Das System verarbeitet die Rechnung mit dem korrigierten Gesamtbetrag von $10,000.00. Die Mehrmenge und der höhere Stückpreis werden abgelehnt.

Damit entspricht die Transaktion den ursprünglichen Bestellbedingungen. Preise und Mengen werden einheitlich kontrolliert und nicht genehmigte Abweichungen abgelehnt.
