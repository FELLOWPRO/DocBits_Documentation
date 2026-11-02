# Fall 11b: Menge oberhalb der Toleranz abgelehnt, Stückpreisabweichung abgelehnt

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Menge überschreitet den zulässigen Bereich (positive Abweichung) und wird abgelehnt. Auch der Stückpreis liegt außerhalb der Toleranz und wird abgelehnt.

## Aktion:

Das System passt Menge und Stückpreis an die genehmigten Bestellwerte an, lehnt darüber hinausgehende Werte ab und verarbeitet die Transaktion.

## Beispiel:

* **Bestellung (PO):**
  * Menge: 200 Einheiten
  * Stückpreis: $50.00 je Einheit
  * Gesamtbetrag: $10,000.00
* **Eingegangene Rechnung:**
  * Menge: 220 Einheiten (Abweichung außerhalb der Toleranz: 10%, abgelehnt)
  * Stückpreis: $55.00 je Einheit (Abweichung außerhalb der Toleranz: 10%, abgelehnt)
  * Gesamtbetrag: $12,100.00
* **Toleranzgrenzen:**
  * Mengentoleranz: ±5%
  * Stückpreistoleranz: ±2%

Sowohl die Menge (220 Einheiten) als auch der Stückpreis ($55.00) überschreiten die zulässigen Toleranzgrenzen; keiner der Werte wurde genehmigt. Das System führt folgende Schritte aus:

1. **Mehrmenge ablehnen:** Das System akzeptiert die berechnete Menge von 220 Einheiten nicht und passt sie an die ursprüngliche Bestellung an.
   * Angepasste Menge = 200 Einheiten (aus der Bestellung)
2. **Rechnungsstückpreis ablehnen:** Das System akzeptiert den berechneten Stückpreis von $55.00 nicht und passt ihn an die ursprüngliche Bestellung an.
   * Angepasster Stückpreis = $50.00 je Einheit (aus der Bestellung)
3. **Gesamtbetrag neu berechnen:** Das System berechnet den Gesamtbetrag anhand der angepassten Menge und des angepassten Stückpreises:
   * **Korrigierter Gesamtbetrag = Angepasste Menge × Angepasster Stückpreis**
   * **Korrigierter Gesamtbetrag = 200 Einheiten × $50.00 je Einheit = $10,000.00**
4. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem korrigierten Gesamtbetrag von $10,000.00. Die Mehrmenge und der höhere Stückpreis werden abgelehnt.

Damit entspricht die Transaktion den ursprünglichen Bestellbedingungen. Preise und Mengen werden einheitlich kontrolliert und nicht genehmigte Abweichungen abgelehnt.
