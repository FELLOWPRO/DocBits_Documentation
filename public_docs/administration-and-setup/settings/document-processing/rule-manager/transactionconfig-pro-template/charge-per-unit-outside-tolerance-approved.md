# Fall 14: Kopfzuschlag – Zuschlag je Einheit außerhalb der Toleranz (genehmigt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Der Header Charge Per Unit liegt außerhalb der Toleranz, wurde jedoch genehmigt.

## Aktion:

Das System übernimmt den genehmigten Charge Per Unit in die Transaktion.

## Beispiel:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $2.50
  * Quantity: 2,000 units
  * Total Header Charge Amount: $5,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.00 — 20% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 2,000 units
  * Total Header Charge Amount: $6,000.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Der Header Charge Per Unit ($3.00) überschreitet die zulässige Toleranz von 5%, wurde jedoch genehmigt. Das System führt folgende Schritte aus:

1. **Accept the Approved Header Charge Per Unit:** Das System akzeptiert den berechneten Zuschlag von $3.00, da er trotz Überschreitung der Toleranzgrenze genehmigt wurde.
2. **Process the Header Charge:** Das System verarbeitet die Rechnung anhand des genehmigten Zuschlags je Einheit und der Menge:
   * **Total Header Charge Amount = Quantity × Approved Header Charge Per Unit**
   * **Total Header Charge Amount = 2,000 units × $3.00 = $6,000.00**
3. **Finalize the Invoice:** Das System verarbeitet die Transaktion mit den genehmigten Zuschlägen und dem Gesamtbetrag von $6,000.00.

Damit berücksichtigt das System genehmigte Abweichungen bei Kopfzuschlägen. Die Transaktion wird entsprechend der Genehmigung verarbeitet und die Finanzdaten bleiben korrekt.
