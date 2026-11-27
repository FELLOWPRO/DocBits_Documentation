# Fall 1, 2, 3: Menge und Stückpreis innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Sowohl die Rechnungsmenge als auch der Stückpreis liegen im Vergleich zur Bestellung innerhalb der zulässigen Toleranz.

## Aktion:

Das System akzeptiert die Rechnungswerte und berechnet den Gesamtbetrag anhand der angegebenen Menge und des Stückpreises.

## Beispiel:

**Purchase Order (PO):**

Menge: 100 Einheiten

Stückpreis: $10.00 je Einheit

Total Amount: $1,000.00

**Invoice Received:**

Menge: 101 Einheiten (Abweichung innerhalb der Toleranz: 1%)

Stückpreis: $10.05 je Einheit (Abweichung innerhalb der Toleranz: 0.5%)

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±1%


Die Menge (101 Einheiten) und der Stückpreis ($10.05) liegen im Vergleich zur Bestellung innerhalb der zulässigen Toleranz. Das System führt folgende Schritte aus:


1\. **Accept the Invoice Values:** Menge und Stückpreis der Rechnung werden als gültig akzeptiert, da sie innerhalb der festgelegten Toleranzgrenzen liegen.

2\. **Calculate the Total Amount:** Der Gesamtbetrag wird anhand der akzeptierten Werte berechnet:

• Total Amount = Quantity × Unit Price

• Total Amount = 101 units × $10.05 per unit = $1,015.05

3\. **Process the Invoice:** Die Rechnung wird mit dem Gesamtbetrag von $1,015.05 verarbeitet. Die Finanzdaten werden entsprechend aktualisiert.

So führen kleine Abweichungen innerhalb der zulässigen Toleranz weder zur Ablehnung der Rechnung noch zu Zahlungsverzögerungen. Das vereinfacht den Finanzprozess.
