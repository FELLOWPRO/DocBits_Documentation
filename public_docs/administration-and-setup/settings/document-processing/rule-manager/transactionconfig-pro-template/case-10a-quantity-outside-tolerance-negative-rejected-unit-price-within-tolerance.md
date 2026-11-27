# Fall 10a: Menge unterhalb der Toleranz abgelehnt, Stückpreis innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Menge unterschreitet den zulässigen Bereich (negative Toleranz) und wurde nicht genehmigt. Der Stückpreis liegt dagegen innerhalb der Toleranz.

## Aktion:

Das System passt die Menge an den genehmigten Wert an und behält den Stückpreis bei. Anschließend wird die Transaktion entsprechend verarbeitet.

## Beispiel:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $20.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $20.00 per unit (within tolerance)
  * Total Amount: $2,800.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Die Menge (140 Einheiten) unterschreitet die zulässige Toleranzgrenze (negative Abweichung von -6.67%) und wurde nicht genehmigt. Der Stückpreis ($20.00) liegt innerhalb der Toleranz. Das System führt folgende Schritte aus:

1. **Reject the Lower Quantity:** Das System akzeptiert die niedrigere Menge nicht, da sie außerhalb des genehmigten Toleranzbereichs liegt.
2. **Adjust the Quantity:** Das System setzt die Menge auf den genehmigten Wert aus der Bestellung.
   * Approved Quantity = 150 units (from PO)
3. **Maintain the Unit Price:** Der Stückpreis von $20.00 je Einheit liegt innerhalb der Toleranz und bleibt unverändert.
4. **Recalculate the Total Amount:** Das System berechnet den Gesamtbetrag anhand der genehmigten Menge und des akzeptierten Stückpreises:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 150 units × $20.00 per unit = $3,000.00**
5. **Process the Invoice:** Das System verarbeitet die Rechnung mit dem angepassten Gesamtbetrag von $3,000.00, der die genehmigte Menge und den genehmigten Stückpreis widerspiegelt. Der Lieferant soll die vollständige genehmigte Menge berechnen.

Damit entspricht die Finanztransaktion den Bestellbedingungen. Eine zu niedrige Abrechnung wird vermieden und die Finanzdaten bleiben korrekt.
