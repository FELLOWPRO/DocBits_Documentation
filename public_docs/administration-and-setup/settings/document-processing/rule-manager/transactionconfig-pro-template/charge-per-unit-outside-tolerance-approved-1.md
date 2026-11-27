# Fall 14: Positionszuschlag – Zuschlag je Einheit außerhalb der Toleranz (genehmigt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Der Zuschlag je Einheit liegt außerhalb der Toleranz, wurde jedoch genehmigt.

## Aktion:

Das System akzeptiert den Zuschlag je Einheit, berücksichtigt die genehmigten Zuschläge und verarbeitet die Transaktion entsprechend.

## Beispiel:

* **Purchase Order (PO):**
  * Charge Per Unit: $4.50
  * Quantity: 1,000 units
  * Total Charge Amount: $4,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.00 — 11.11% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 1,000 units
  * Total Charge Amount: $5,000.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Der Zuschlag je Einheit ($5.00) liegt außerhalb der zulässigen Toleranz von 5%, wurde jedoch genehmigt. Das System führt folgende Schritte aus:

1. **Accept the Approved Charge Per Unit:** Das System akzeptiert den berechneten Zuschlag von $5.00, da er trotz Überschreitung der Toleranzgrenze genehmigt wurde.
2. **Process the Transaction:** Das System verarbeitet die Rechnung anhand des genehmigten Zuschlags je Einheit und der Menge:
   * **Total Charge Amount = Quantity × Approved Charge Per Unit**
   * **Total Charge Amount = 1,000 units × $5.00 = $5,000.00**
3. **Finalize the Invoice:** Das System verarbeitet die Transaktion mit den genehmigten Zuschlägen und dem Gesamtbetrag von $5,000.00.

Damit berücksichtigt das System genehmigte Zuschlagsabweichungen flexibel und führt die Finanzdaten weiterhin korrekt.
