# Fall 6: Menge innerhalb der Toleranz, Stückpreis unterhalb der Toleranzgrenze (abgelehnt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Menge liegt innerhalb der Toleranz. Der Stückpreis unterschreitet jedoch den zulässigen Bereich (negative Toleranz); die Abweichung wurde nicht genehmigt.

## Aktion:

Die Beispielzuordnung setzt den Stückpreis auf den Bestellwert zurück. Ob weitere Kopfzuschläge oder Korrekturbelege entstehen, hängt von den aktiven Konfliktregeln und Exportaktionen ab.

## Beispiel:

* **Bestellung (PO):**
  * Menge: 100 Einheiten
  * Stückpreis: $10.00 je Einheit
  * Gesamtbetrag: $1,000.00
* **Eingegangene Rechnung:**
  * Menge: 100 Einheiten (Abweichung innerhalb der Toleranz: 0%)
  * Stückpreis: $9.00 je Einheit (negative Abweichung außerhalb der Toleranz: -10%)
  * Gesamtbetrag: $900.00
* **Toleranzgrenzen:**
  * Mengentoleranz: ±2%
  * Stückpreistoleranz: ±1%

Die Menge (100 Einheiten) liegt innerhalb der zulässigen Toleranz. Der Stückpreis ($9.00) unterschreitet dagegen die Toleranzgrenze und wurde nicht genehmigt. Das System führt folgende Schritte aus:

1. **Stückpreis ablehnen:** Das System akzeptiert den berechneten Stückpreis von $9.00 nicht.
2. **Stückpreis anpassen:** Das System setzt den Stückpreis auf den ursprünglichen Wert aus der Bestellung.
   * Angepasster Stückpreis = $10.00 (aus der Bestellung)
3. **Korrigierten Gesamtbetrag berechnen:** Das System berechnet den Gesamtbetrag mit dem angepassten Stückpreis neu.
   * **Korrigierter Gesamtbetrag = Menge × Angepasster Stückpreis**
   * **Korrigierter Gesamtbetrag = 100 Einheiten × $10.00 je Einheit = $1,000.00**
4. **Vorzeichenbehaftete Abweichung berechnen:** Die Differenz zwischen dem ursprünglichen Rechnungsbetrag und dem korrigierten Betrag ist ein Rechenwert. Ob daraus ein Korrekturbeleg entsteht und welchen Typ sowie welches Vorzeichen er erhält, bestimmt die aktive Exportzuordnung.
   * **Vorzeichenbehaftete Abweichung = Ursprünglicher Rechnungsbetrag - Korrigierter Gesamtbetrag**
   * **Vorzeichenbehaftete Abweichung = $900.00 - $1,000.00 = -$100.00**
5. **Dokument gemäß Zuordnung verarbeiten:** Der angepasste Gesamtbetrag beträgt $1,000.00; der Betrag der Abweichung beträgt $100.00. Die konkrete Korrekturbelegart und ihre Verarbeitung richten sich nach der aktiven Zuordnung.

Damit wird der Preis an die Bestellbedingungen angepasst, auch wenn fälschlicherweise ein niedrigerer Preis berechnet wurde.
