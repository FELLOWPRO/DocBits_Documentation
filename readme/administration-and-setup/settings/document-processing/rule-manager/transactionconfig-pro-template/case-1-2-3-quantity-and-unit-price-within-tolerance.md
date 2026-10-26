# Fall 1, 2, 3: Menge und Stückpreis innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Sowohl die Rechnungsmenge als auch der Stückpreis liegen im Vergleich zur Bestellung innerhalb der zulässigen Toleranz.

## Aktion:

Das System akzeptiert die Rechnungswerte und berechnet den Gesamtbetrag anhand der angegebenen Menge und des Stückpreises.

## Beispiel:

**Bestellung (PO):**

Menge: 100 Einheiten

Stückpreis: $10.00 je Einheit

Gesamtbetrag: $1,000.00

**Eingegangene Rechnung:**

Menge: 101 Einheiten (Abweichung innerhalb der Toleranz: 1%)

Stückpreis: $10.05 je Einheit (Abweichung innerhalb der Toleranz: 0.5%)

Gesamtbetrag: $1,015.05

**Toleranzgrenzen:**

Mengentoleranz: ±2%

Stückpreistoleranz: ±1%\


Die Menge (101 Einheiten) und der Stückpreis ($10.05) liegen im Vergleich zur Bestellung innerhalb der zulässigen Toleranz. Das System führt folgende Schritte aus:\


1\. **Rechnungswerte akzeptieren:** Menge und Stückpreis der Rechnung werden als gültig akzeptiert, da sie innerhalb der festgelegten Toleranzgrenzen liegen.

2\. **Gesamtbetrag berechnen:** Der Gesamtbetrag wird anhand der akzeptierten Werte berechnet:

• Gesamtbetrag = Menge × Stückpreis

• Gesamtbetrag = 101 Einheiten × $10.05 je Einheit = $1,015.05

3\. **Rechnung verarbeiten:** Die Rechnung wird mit dem Gesamtbetrag von $1,015.05 verarbeitet. Die Finanzdaten werden entsprechend aktualisiert.

So führen kleine Abweichungen innerhalb der zulässigen Toleranz weder zur Ablehnung der Rechnung noch zu Zahlungsverzögerungen. Das vereinfacht den Finanzprozess.
