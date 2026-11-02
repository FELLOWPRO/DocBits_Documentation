# Fall 15: Kopfzuschlag – Zuschlag je Einheit außerhalb der Toleranz (abgelehnt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Der Zuschlag auf Kopfebene je Einheit liegt außerhalb der Toleranz und wurde nicht genehmigt.

## Aktion:

Das System passt den Kopfzuschlag an die Bestellung an, verarbeitet die Transaktion entsprechend und erstellt gegebenenfalls die erforderlichen Korrekturbelege.

## Beispiel:

* **Bestellung (PO):**
  * Kopfzuschlag je Einheit: $4.00
  * Menge: 1,500 Einheiten
  * Kopfzuschlagsgesamtbetrag: $6,000.00
* **Eingegangene Rechnung:**
  * Kopfzuschlag je Einheit: $5.00 (Abweichung außerhalb der Toleranz: 25%, abgelehnt)
  * Menge: 1,500 Einheiten
  * Kopfzuschlagsgesamtbetrag: $7,500.00
* **Toleranzgrenzen:**
  * Toleranz für Kopfzuschläge je Einheit: ±5%

Der Zuschlag auf Kopfebene je Einheit ($5.00) überschreitet die zulässige Toleranz von 5% und wurde nicht genehmigt. Das System führt folgende Schritte aus:

1. **Berechneten Kopfzuschlag je Einheit ablehnen:** Das System akzeptiert den Zuschlag von $5.00 nicht, da die Abweichung die Toleranzgrenze überschreitet.
2. **Kopfzuschlag je Einheit anpassen:** Das System setzt den Zuschlag auf den ursprünglichen Bestellwert oder den genehmigten Wert:
   * Angepasster Kopfzuschlag je Einheit = $4.00 (aus der Bestellung)
3. **Gesamten Kopfzuschlag neu berechnen:** Das System berechnet den gesamten Zuschlagsbetrag anhand des angepassten Zuschlags je Einheit neu:
   * **Korrigierter Kopfzuschlagsgesamtbetrag = Menge × Angepasster Kopfzuschlag je Einheit**
   * **Korrigierter Kopfzuschlagsgesamtbetrag = 1,500 Einheiten × $4.00 = $6,000.00**
4. **Gutschrift erstellen:** Da der ursprüngliche Rechnungsbetrag höher als der korrigierte Gesamtbetrag war, erstellt das System eine Gutschrift über den zu viel berechneten Betrag:
   * **Gutschriftsbetrag = Ursprünglicher Rechnungsbetrag - Korrigierter Kopfzuschlagsgesamtbetrag**
   * **Gutschriftsbetrag = $7,500.00 - $6,000.00 = $1,500.00**
5. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem korrigierten Zuschlagsgesamtbetrag von $6,000.00 und erstellt eine Gutschrift über $1,500.00, um den zu viel berechneten Betrag auszugleichen.

Damit entspricht die Transaktion den ursprünglichen Bestellbedingungen. Zu hohe Beträge werden korrigiert und die Finanzdaten korrekt verarbeitet.
