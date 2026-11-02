# Fall 11a: Menge oberhalb der Toleranz abgelehnt, Stückpreis innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Rechnungsmenge überschreitet den zulässigen Bereich (positive Abweichung) und wird abgelehnt. Der Stückpreis liegt innerhalb der Toleranz.

## Aktion:

Das System setzt die Menge auf den genehmigten Wert, behält den Stückpreis bei und verarbeitet die Transaktion. Die Mehrmenge wird abgelehnt und nicht berechnet.

## Beispiel:

* **Bestellung (PO):**
  * Menge: 100 Einheiten
  * Stückpreis: $8.00 je Einheit
  * Gesamtbetrag: $800.00
* **Eingegangene Rechnung:**
  * Menge: 110 Einheiten (Abweichung außerhalb der Toleranz: 10%, abgelehnt)
  * Stückpreis: $8.00 je Einheit (innerhalb der Toleranz)
  * Gesamtbetrag: $880.00
* **Toleranzgrenzen:**
  * Mengentoleranz: ±5%
  * Stückpreistoleranz: ±2%

Die Menge (110 Einheiten) überschreitet die zulässige Toleranzgrenze (positive Abweichung von 10%) und wurde nicht genehmigt. Der Stückpreis ($8.00) liegt innerhalb der Toleranz. Das System führt folgende Schritte aus:

1. **Mehrmenge ablehnen:** Das System lehnt die Menge ab, die über die genehmigte Toleranzgrenze hinausgeht.
2. **Menge anpassen:** Das System setzt die Menge auf den genehmigten Wert aus der Bestellung.
   * Genehmigte Menge = 100 Einheiten (aus der Bestellung)
3. **Stückpreis beibehalten:** Der Stückpreis von $8.00 je Einheit liegt innerhalb der Toleranz und bleibt unverändert.
4. **Gesamtbetrag neu berechnen:** Das System berechnet den Gesamtbetrag anhand der genehmigten Menge und des akzeptierten Stückpreises:
   * **Gesamtbetrag = Genehmigte Menge × Stückpreis**
   * **Gesamtbetrag = 100 Einheiten × $8.00 je Einheit = $800.00**
5. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem angepassten Gesamtbetrag von $800.00. Berücksichtigt werden nur die genehmigte Menge und der genehmigte Stückpreis. Die Mehrmenge von 10 Einheiten wird abgelehnt und nicht berechnet.

Damit entspricht der Rechnungsbetrag den vereinbarten Bestellbedingungen, auch wenn der Lieferant eine höhere Menge in Rechnung stellt.
