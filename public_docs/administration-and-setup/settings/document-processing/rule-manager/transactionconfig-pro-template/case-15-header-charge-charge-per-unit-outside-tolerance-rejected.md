# Fall 15: Kopfzuschlag – Zuschlag je Einheit außerhalb der Toleranz (abgelehnt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Der Header Charge Per Unit liegt außerhalb der Toleranz und wurde nicht genehmigt.

## Aktion:

Das System passt den Kopfzuschlag an die Bestellung an, verarbeitet die Transaktion entsprechend und erstellt gegebenenfalls die erforderlichen Korrekturbelege.

## Beispiel:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $4.00
  * Quantity: 1,500 units
  * Total Header Charge Amount: $6,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $5.00 — 25% above the PO value, outside the configured ±5% tolerance; rejected.
  * Quantity: 1,500 units
  * Total Header Charge Amount: $7,500.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Der Header Charge Per Unit ($5.00) überschreitet die zulässige Toleranz von 5% und wurde nicht genehmigt. Das System führt folgende Schritte aus:

1. **Reject the Invoiced Header Charge Per Unit:** Das System akzeptiert den Zuschlag von $5.00 nicht, da die Abweichung die Toleranzgrenze überschreitet.
2. **Adjust the Header Charge Per Unit:** Das System setzt den Zuschlag auf den ursprünglichen Bestellwert oder den genehmigten Wert:
   * Adjusted Header Charge Per Unit = $4.00 (from PO)
3. **Recalculate the Total Header Charge Amount:** Das System berechnet den gesamten Zuschlagsbetrag anhand des angepassten Zuschlags je Einheit neu:
   * **Corrected Total Header Charge Amount = Quantity × Adjusted Header Charge Per Unit**
   * **Corrected Total Header Charge Amount = 1,500 units × $4.00 = $6,000.00**
4. **Generate a Credit Note:** Da der ursprüngliche Rechnungsbetrag höher als der korrigierte Gesamtbetrag war, erstellt das System eine Gutschrift über den zu viel berechneten Betrag:
   * **Credit Note Amount = Original Invoice Total - Corrected Total Header Charge Amount**
   * **Credit Note Amount = $7,500.00 - $6,000.00 = $1,500.00**
5. **Process the Invoice:** Das System verarbeitet die Rechnung mit dem korrigierten Zuschlagsgesamtbetrag von $6,000.00 und erstellt eine Gutschrift über $1,500.00, um den zu viel berechneten Betrag auszugleichen.

Damit entspricht die Transaktion den ursprünglichen Bestellbedingungen. Zu hohe Beträge werden korrigiert und die Finanzdaten korrekt verarbeitet.
