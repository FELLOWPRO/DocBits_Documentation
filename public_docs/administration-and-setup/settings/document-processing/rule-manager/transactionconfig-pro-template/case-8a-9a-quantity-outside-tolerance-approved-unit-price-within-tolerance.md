# Fall 8a, 9a: Menge außerhalb der Toleranz (genehmigt), Stückpreis innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Rechnungsmenge liegt außerhalb der zulässigen Toleranz, wurde jedoch genehmigt. Der Stückpreis liegt innerhalb der Toleranz.

## Aktion:

Das System akzeptiert die genehmigte Menge und den Stückpreis aus der Rechnung und verarbeitet die Transaktion entsprechend.

## Beispiel:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $12.00 per unit
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Quantity: 160 units — 6.67% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $12.00 per unit (within tolerance)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Die Menge (160 Einheiten) überschreitet die zulässige Toleranzgrenze, wurde jedoch genehmigt. Der Stückpreis ($12.00) liegt innerhalb des zulässigen Bereichs. Das System führt folgende Schritte aus:

1. **Accept the Approved Quantity:** Das System berücksichtigt, dass die Menge trotz Überschreitung des normalen Toleranzbereichs genehmigt wurde.
2. **Accept the Unit Price:** Der Stückpreis von $12.00 je Einheit liegt innerhalb der zulässigen Toleranz und wird daher aus der Rechnung übernommen.
3. **Process the Transaction:** Das System berechnet den Gesamtbetrag anhand der genehmigten Menge und des Stückpreises:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 160 units × $12.00 per unit = $1,920.00**
4. **Finalize the Invoice:** Das System verarbeitet die Rechnung mit dem Gesamtbetrag von $1,920.00, der die genehmigte Menge und den akzeptierten Stückpreis widerspiegelt.

Damit berücksichtigt das System genehmigte Mengenabweichungen, während der Stückpreis im erwarteten Bereich bleibt. Das ermöglicht eine reibungslose Transaktionsverarbeitung.
