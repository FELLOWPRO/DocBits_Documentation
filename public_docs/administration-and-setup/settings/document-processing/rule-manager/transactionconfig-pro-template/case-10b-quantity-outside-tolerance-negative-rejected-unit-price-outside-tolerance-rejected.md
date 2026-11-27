# Fall 10b: Menge unterhalb der Toleranz abgelehnt, Stückpreisabweichung abgelehnt

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Sowohl die Menge als auch der Stückpreis liegen außerhalb der Toleranz; keiner der Werte wurde genehmigt.

## Aktion:

Das System lehnt die Rechnungsdaten ab, passt die Werte an die Bestellung an und erstellt die erforderlichen Belastungsanzeigen oder Gutschriften.

## Beispiel:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $30.00 per unit
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $33.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Sowohl die Menge (140 Einheiten) als auch der Stückpreis ($33.00) liegen außerhalb der zulässigen Toleranzgrenzen; keiner der Werte wurde genehmigt. Das System führt folgende Schritte aus:

1. **Reject the Invoice Data:** Das System akzeptiert weder die berechnete Menge noch den Stückpreis, da beide von den Toleranzgrenzen abweichen.
2. **Adjust the Quantity:** Das System setzt die Menge auf den ursprünglichen Bestellwert.
   * Adjusted Quantity = 150 units (from PO)
3. **Adjust the Unit Price:** Das System setzt den Stückpreis auf den ursprünglichen Wert aus der Bestellung.
   * Adjusted Unit Price = $30.00 per unit (from PO)
4. **Recalculate the Total Amount:** Das System berechnet den Gesamtbetrag anhand der angepassten Menge und des angepassten Stückpreises neu:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 150 units × $30.00 per unit = $4,500.00**
5. **Generate a Debit Note:** Da der ursprüngliche Rechnungsbetrag höher als der korrigierte Gesamtbetrag war, erstellt das System eine Belastungsanzeige über den zu viel berechneten Betrag.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $4,620.00 - $4,500.00 = $120.00**
6. **Process the Invoice:** Das System verarbeitet die Rechnung mit dem korrigierten Gesamtbetrag von $4,500.00 und erstellt eine Belastungsanzeige über $120.00, um den zu viel berechneten Betrag auszugleichen.

Damit wird die Finanztransaktion an die Bestellbedingungen angepasst und eine korrekte, faire Abrechnung sichergestellt.
