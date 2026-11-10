# Zuschlag je Einheit innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Das folgende Szenario ist eine beispielhafte konfigurierte Zuordnung, keine geprüfte, ausgelieferte Standardvorlage. Die tatsächliche Ausgabe, Beträge, Vorzeichen und Dokumenttypen hängen von den aktiven `conflict_resolution`-Regeln und -Ausdrücken, der Exportzuordnung und den Genehmigungsentscheidungen ab. Eine unten beschriebene Belastungsanzeige oder Gutschrift ist von dieser Konfiguration abhängig; das Beispiel garantiert weder eine automatische Ausstellung noch rechtliche Konformität.


## Szenario:

Der Charge Per Unit auf der Rechnung liegt im Vergleich zur Bestellung innerhalb der zulässigen Toleranz.

## Aktion:

Das System übernimmt den Charge Per Unit aus der Rechnung und verarbeitet die Transaktion ohne Anpassungen.

## Beispiel:

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 (variance 2%, within the ±3% tolerance)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Der Charge Per Unit ($5.10) liegt im Vergleich zur Bestellung innerhalb der zulässigen Toleranz von 3%. Das System führt folgende Schritte aus:

1. **Accept the Charge Per Unit:** Das System akzeptiert den fakturierten Charge Per Unit von $5.10, da er innerhalb der festgelegten Toleranzgrenze liegt.
2. **Process the Transaction:** Das System verarbeitet die Rechnung mit dem Total Charge Amount, der sich aus Charge Per Unit und Quantity der Rechnung ergibt:
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:** Das System verarbeitet die Transaktion ohne Anpassungen und übernimmt die Rechnung unverändert.

Damit kann das System kleine zulässige Abweichungen bei Charge Per Unit ohne unnötige Ablehnungen oder Verzögerungen verarbeiten.
