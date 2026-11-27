# Fall 11a: Menge oberhalb der Toleranz abgelehnt, Stückpreis innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Rechnungsmenge überschreitet den zulässigen Bereich (positive Abweichung) und wird abgelehnt. Der Stückpreis liegt innerhalb der Toleranz.

## Aktion:

Das System setzt die Menge auf den genehmigten Wert, behält den Stückpreis bei und verarbeitet die Transaktion. Die Mehrmenge wird abgelehnt und nicht berechnet.

## Beispiel:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Unit Price: $8.00 per unit
  * Total Amount: $800.00
* **Invoice Received:**
  * Quantity: 110 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $8.00 per unit (within tolerance)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Die Menge (110 Einheiten) überschreitet die zulässige Toleranzgrenze (positive Abweichung von 10%) und wurde nicht genehmigt. Der Stückpreis ($8.00) liegt innerhalb der Toleranz. Das System führt folgende Schritte aus:

1. **Reject the Excess Quantity:** Das System lehnt die Menge ab, die über die genehmigte Toleranzgrenze hinausgeht.
2. **Adjust the Quantity:** Das System setzt die Menge auf den genehmigten Wert aus der Bestellung.
   * Approved Quantity = 100 units (from PO)
3. **Maintain the Unit Price:** Der Stückpreis von $8.00 je Einheit liegt innerhalb der Toleranz und bleibt unverändert.
4. **Recalculate the Total Amount:** Das System berechnet den Gesamtbetrag anhand der genehmigten Menge und des akzeptierten Stückpreises:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 100 units × $8.00 per unit = $800.00**
5. **Process the Invoice:** Das System verarbeitet die Rechnung mit dem angepassten Gesamtbetrag von $800.00. Berücksichtigt werden nur die genehmigte Menge und der genehmigte Stückpreis. Die Mehrmenge von 10 Einheiten wird abgelehnt und nicht berechnet.

Damit entspricht der Rechnungsbetrag den vereinbarten Bestellbedingungen, auch wenn der Lieferant eine höhere Menge in Rechnung stellt.
