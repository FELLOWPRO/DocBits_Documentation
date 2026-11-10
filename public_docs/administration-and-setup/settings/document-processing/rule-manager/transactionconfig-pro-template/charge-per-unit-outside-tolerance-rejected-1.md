# Zuschlag je Einheit außerhalb der Toleranz (abgelehnt)

> **Hinweis zu den Beispielen:** Das folgende Szenario ist eine beispielhafte konfigurierte Zuordnung, keine geprüfte, ausgelieferte Standardvorlage. Die tatsächliche Ausgabe, Beträge, Vorzeichen und Dokumenttypen hängen von den aktiven `conflict_resolution`-Regeln und -Ausdrücken, der Exportzuordnung und den Genehmigungsentscheidungen ab. Eine unten beschriebene Belastungsanzeige oder Gutschrift ist von dieser Konfiguration abhängig; das Beispiel garantiert weder eine automatische Ausstellung noch rechtliche Konformität.


## Szenario:

Der Charge Per Unit liegt außerhalb der Toleranz und wurde nicht genehmigt.

## Aktion:

Das System passt den Charge Per Unit an die Bestellung oder den genehmigten Wert an und erstellt gegebenenfalls die erforderlichen Belastungsanzeigen oder Gutschriften.

## Beispiel:

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 — 16.67% above the PO value, outside the configured ±5% tolerance; rejected.
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Der Charge Per Unit ($7.00) überschreitet die zulässige Toleranz von 5% und wurde nicht genehmigt. Das System führt folgende Schritte aus:

1. **Reject the Invoiced Charge Per Unit:** Das System akzeptiert den fakturierten Charge Per Unit von $7.00 nicht, da die Abweichung die Toleranzgrenze überschreitet.
2. **Adjust the Charge Per Unit:** Das System setzt den Charge Per Unit auf den Wert aus der Bestellung oder auf den genehmigten Wert:
   * Adjusted Charge Per Unit = $6.00 (from PO)
3. **Recalculate the Total Charge Amount:** Das System berechnet den Total Charge Amount anhand des angepassten Charge Per Unit neu:
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** Da der ursprüngliche Rechnungsbetrag höher als der korrigierte Gesamtbetrag war, erstellt das System eine Belastungsanzeige über den zu viel berechneten Betrag:
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** Das System verarbeitet die Rechnung mit dem korrigierten Total Charge Amount von $4,800.00 und erstellt eine Belastungsanzeige über $800.00, um den zu viel berechneten Betrag auszugleichen.

Damit entsprechen die Finanztransaktionen den Bestellbedingungen. Nicht genehmigte Abweichungen werden abgelehnt und eine korrekte Abrechnung wird sichergestellt.
