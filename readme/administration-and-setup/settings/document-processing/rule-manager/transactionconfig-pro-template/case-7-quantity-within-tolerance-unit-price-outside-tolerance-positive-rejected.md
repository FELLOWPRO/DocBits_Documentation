# Fall 7: Menge innerhalb der Toleranz, Stückpreis oberhalb der Toleranz abgelehnt

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Menge liegt innerhalb der Toleranz. Der Stückpreis überschreitet jedoch den zulässigen Bereich (positive Toleranz); die Abweichung wurde nicht genehmigt.

## Aktion:

Das System lehnt den Rechnungsstückpreis ab und passt ihn an die Bestellung an. Es kann eine Belastungsanzeige erstellen, um den zu viel berechneten Betrag auszugleichen.

## Beispiel:

* **Bestellung (PO):**
  * Menge: 200 Einheiten
  * Stückpreis: $15.00 je Einheit
  * Gesamtbetrag: $3,000.00
* **Eingegangene Rechnung:**
  * Menge: 198 Einheiten (Abweichung innerhalb der Toleranz: 1%)
  * Stückpreis: $17.00 je Einheit (positive Abweichung außerhalb der Toleranz: 13.33%)
  * Gesamtbetrag: $3,366.00
* **Toleranzgrenzen:**
  * Mengentoleranz: ±2%
  * Stückpreistoleranz: ±1%

Die Menge (198 Einheiten) liegt innerhalb der zulässigen Toleranz. Der Stückpreis ($17.00) überschreitet dagegen die Toleranzgrenze und wurde nicht genehmigt. Das System führt folgende Schritte aus:

1. **Rechnungsstückpreis ablehnen:** Das System akzeptiert den berechneten Stückpreis von $17.00 nicht.
2. **Stückpreis anpassen:** Das System setzt den Stückpreis auf den ursprünglichen Wert aus der Bestellung.
   * Angepasster Stückpreis = $15.00 (aus der Bestellung)
3. **Korrigierten Gesamtbetrag berechnen:** Das System berechnet den Gesamtbetrag mit dem angepassten Stückpreis neu.
   * **Korrigierter Gesamtbetrag = Menge × Angepasster Stückpreis**
   * **Korrigierter Gesamtbetrag = 198 Einheiten × $15.00 je Einheit = $2,970.00**
4. **Belastungsanzeige erstellen:** Das System erstellt eine Belastungsanzeige über den zu viel berechneten Differenzbetrag.
   * **Betrag der Belastungsanzeige = Ursprünglicher Rechnungsbetrag - Korrigierter Gesamtbetrag**
   * **Betrag der Belastungsanzeige = $3,366.00 - $2,970.00 = $396.00**
   * Diese Belastungsanzeige entspricht dem vom Lieferanten zu viel berechneten Betrag.
5. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem korrigierten Gesamtbetrag von $2,970.00 und erstellt eine Belastungsanzeige über $396.00, um den zu viel berechneten Betrag auszugleichen.

Damit werden zu hohe Rechnungsbeträge korrigiert, die Transaktion an die Bestellbedingungen angepasst und die finanziellen Interessen des Unternehmens geschützt.
