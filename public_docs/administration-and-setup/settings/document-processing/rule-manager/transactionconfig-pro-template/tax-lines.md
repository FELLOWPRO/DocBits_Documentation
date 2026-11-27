# Steuerzeilen

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Behandelt Abweichungen zwischen den Steuerbeträgen der Rechnung und der Bestellung.

## Aktion:

Die Beispielzuordnung passt die Steuerzeilen an die konfigurierten genehmigten Steuersätze und -beträge an. Die fachliche und steuerliche Richtigkeit dieser Vorgaben muss gesondert geprüft werden.

## Beispiel:

* **Purchase Order (PO):**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 8%
  * Expected Tax Amount: $800.00
  * Total Amount with Tax: $10,800.00
* **Invoice Received:**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 10% (discrepancy)
  * Invoiced Tax Amount: $1,000.00
  * Total Amount with Tax: $11,000.00

Der Steuersatz der Rechnung (10%) weicht vom erwarteten Steuersatz (8%) ab und wurde nicht genehmigt. Das System führt folgende Schritte aus:

1. **Reject the Invoiced Tax Rate:** Das System akzeptiert den Steuersatz von 10% nicht, da er nicht dem genehmigten Satz aus der Bestellung entspricht.
2. **Adjust the Tax Rate:** Das System setzt den Steuersatz auf den genehmigten Wert aus der Bestellung.
   * Adjusted Tax Rate = 8% (from PO)
3. **Recalculate the Tax Amount:** Das System berechnet den Steuerbetrag anhand des angepassten Steuersatzes neu:
   * **Corrected Tax Amount = Subtotal Amount × Adjusted Tax Rate**
   * **Corrected Tax Amount = $10,000.00 × 8% = $800.00**
4. **Recalculate the Total Amount:** Das System berechnet den Gesamtbetrag einschließlich Steuer neu:
   * **Corrected Total Amount with Tax = Subtotal Amount + Corrected Tax Amount**
   * **Corrected Total Amount with Tax = $10,000.00 + $800.00 = $10,800.00**
5. **Generate a Credit Note:** Das System erstellt eine Gutschrift, um die zu viel berechnete Steuer zu korrigieren:
   * **Credit Note Amount = Original Invoice Tax Amount - Corrected Tax Amount**
   * **Credit Note Amount = $1,000.00 - $800.00 = $200.00**
6. **Process the Invoice:** Das System verarbeitet die Rechnung mit dem korrigierten Steuerbetrag von $800.00 und dem Gesamtbetrag von $10,800.00. Über die Steuerdifferenz von $200.00 wird eine Gutschrift erstellt.

Damit verwendet das Beispiel den konfigurierten erwarteten Steuersatz. Ob die Zuordnung im konkreten Anwendungsfall fachlich und steuerlich richtig ist, muss gesondert geprüft werden.
