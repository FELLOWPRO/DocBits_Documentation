# Fall 8b, 9b: Menge außerhalb der Toleranz (genehmigt), Stückpreis außerhalb der Toleranz (genehmigt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Sowohl die Quantity als auch der Unit Price liegen außerhalb der Toleranz, wurden jedoch genehmigt.

## Aktion:

Das System verarbeitet die Transaktion anhand der Rechnungswerte für Quantity und Unit Price und berücksichtigt gegebenenfalls erforderliche Anpassungen oder Positionszuschläge.

## Beispiel:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $25.00 per unit
  * Total Amount: $5,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $27.00 per unit — 8% above the PO value, outside the configured ±2% tolerance; approved.
  * Total Amount: $5,940.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Sowohl die Quantity (220 Einheiten) als auch der Unit Price ($27.00) liegen außerhalb der zulässigen Toleranzgrenzen, wurden jedoch genehmigt. Das System führt folgende Schritte aus:

1. **Accept the Approved Quantity:** Das System akzeptiert die berechnete Menge von 220 Einheiten, da sie trotz Überschreitung des Toleranzbereichs genehmigt wurde.
2. **Accept the Approved Unit Price:** Das System akzeptiert den berechneten Stückpreis von $27.00 je Einheit, da er trotz Überschreitung des Toleranzbereichs genehmigt wurde.
3. **Calculate the Total Amount:** Das System berechnet den Gesamtbetrag anhand der genehmigten Rechnungswerte:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 220 units × $27.00 per unit = $5,940.00**
4. **Apply Necessary Adjustments or Line Charges:** Je nach den Organisationsrichtlinien zum Umgang mit genehmigten Abweichungen kann das System zusätzliche Positionszuschläge oder Anpassungen berücksichtigen.
5. **Process the Invoice:** Das System verarbeitet die Rechnung mit den genehmigten Werten für Menge und Stückpreis und schließt die Transaktion mit dem Gesamtbetrag von $5,940.00 ab.

Damit wird die Transaktion entsprechend den genehmigten Abweichungen flexibel verarbeitet und die Finanzdaten bleiben korrekt.
