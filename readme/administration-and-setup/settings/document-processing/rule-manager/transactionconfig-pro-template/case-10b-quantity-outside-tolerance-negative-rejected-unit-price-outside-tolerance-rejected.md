# Fall 10b: Menge unterhalb der Toleranz abgelehnt, Stückpreisabweichung abgelehnt

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Sowohl die Menge als auch der Stückpreis liegen außerhalb der Toleranz; keiner der Werte wurde genehmigt.

## Aktion:

Das System lehnt die Rechnungsdaten ab, passt die Werte an die Bestellung an und erstellt die erforderlichen Belastungsanzeigen oder Gutschriften.

## Beispiel:

* **Bestellung (PO):**
  * Menge: 150 Einheiten
  * Stückpreis: $30.00 je Einheit
  * Gesamtbetrag: $4,500.00
* **Eingegangene Rechnung:**
  * Menge: 140 Einheiten (Abweichung außerhalb der Toleranz: -6.67%, abgelehnt)
  * Stückpreis: $33.00 je Einheit (Abweichung außerhalb der Toleranz: 10%, abgelehnt)
  * Gesamtbetrag: $4,620.00
* **Toleranzgrenzen:**
  * Mengentoleranz: ±5%
  * Stückpreistoleranz: ±2%

Sowohl die Menge (140 Einheiten) als auch der Stückpreis ($33.00) liegen außerhalb der zulässigen Toleranzgrenzen; keiner der Werte wurde genehmigt. Das System führt folgende Schritte aus:

1. **Rechnungsdaten ablehnen:** Das System akzeptiert weder die berechnete Menge noch den Stückpreis, da beide von den Toleranzgrenzen abweichen.
2. **Menge anpassen:** Das System setzt die Menge auf den ursprünglichen Bestellwert.
   * Angepasste Menge = 150 Einheiten (aus der Bestellung)
3. **Stückpreis anpassen:** Das System setzt den Stückpreis auf den ursprünglichen Wert aus der Bestellung.
   * Angepasster Stückpreis = $30.00 je Einheit (aus der Bestellung)
4. **Gesamtbetrag neu berechnen:** Das System berechnet den Gesamtbetrag anhand der angepassten Menge und des angepassten Stückpreises neu:
   * **Korrigierter Gesamtbetrag = Angepasste Menge × Angepasster Stückpreis**
   * **Korrigierter Gesamtbetrag = 150 Einheiten × $30.00 je Einheit = $4,500.00**
5. **Belastungsanzeige erstellen:** Da der ursprüngliche Rechnungsbetrag höher als der korrigierte Gesamtbetrag war, erstellt das System eine Belastungsanzeige über den zu viel berechneten Betrag.
   * **Betrag der Belastungsanzeige = Ursprünglicher Rechnungsbetrag - Korrigierter Gesamtbetrag**
   * **Betrag der Belastungsanzeige = $4,620.00 - $4,500.00 = $120.00**
6. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem korrigierten Gesamtbetrag von $4,500.00 und erstellt eine Belastungsanzeige über $120.00, um den zu viel berechneten Betrag auszugleichen.

Damit wird die Finanztransaktion an die Bestellbedingungen angepasst und eine korrekte, faire Abrechnung sichergestellt.
