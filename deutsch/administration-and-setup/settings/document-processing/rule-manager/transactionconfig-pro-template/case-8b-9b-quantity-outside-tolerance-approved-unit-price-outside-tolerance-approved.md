# Fall 8b, 9b: Menge außerhalb der Toleranz (genehmigt), Stückpreis außerhalb der Toleranz (genehmigt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Sowohl die Menge als auch der Stückpreis liegen außerhalb der Toleranz, wurden jedoch genehmigt.

## Aktion:

Das System verarbeitet die Transaktion anhand der Rechnungswerte für Menge und Stückpreis und berücksichtigt gegebenenfalls erforderliche Anpassungen oder Positionszuschläge.

## Beispiel:

* **Bestellung (PO):**
  * Menge: 200 Einheiten
  * Stückpreis: $25.00 je Einheit
  * Gesamtbetrag: $5,000.00
* **Eingegangene Rechnung:**
  * Menge: 220 Einheiten (Abweichung außerhalb der Toleranz: 10%, genehmigt)
  * Stückpreis: $27.00 je Einheit (Abweichung außerhalb der Toleranz: 8%, genehmigt)
  * Gesamtbetrag: $5,940.00
* **Toleranzgrenzen:**
  * Mengentoleranz: ±5%
  * Stückpreistoleranz: ±2%

Sowohl die Menge (220 Einheiten) als auch der Stückpreis ($27.00) liegen außerhalb der zulässigen Toleranzgrenzen, wurden jedoch genehmigt. Das System führt folgende Schritte aus:

1. **Genehmigte Menge akzeptieren:** Das System akzeptiert die berechnete Menge von 220 Einheiten, da sie trotz Überschreitung des Toleranzbereichs genehmigt wurde.
2. **Genehmigten Stückpreis akzeptieren:** Das System akzeptiert den berechneten Stückpreis von $27.00 je Einheit, da er trotz Überschreitung des Toleranzbereichs genehmigt wurde.
3. **Gesamtbetrag berechnen:** Das System berechnet den Gesamtbetrag anhand der genehmigten Rechnungswerte:
   * **Gesamtbetrag = Menge × Stückpreis**
   * **Gesamtbetrag = 220 Einheiten × $27.00 je Einheit = $5,940.00**
4. **Erforderliche Anpassungen oder Positionszuschläge berücksichtigen:** Je nach den Organisationsrichtlinien zum Umgang mit genehmigten Abweichungen kann das System zusätzliche Positionszuschläge oder Anpassungen berücksichtigen.
5. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit den genehmigten Werten für Menge und Stückpreis und schließt die Transaktion mit dem Gesamtbetrag von $5,940.00 ab.

Damit wird die Transaktion entsprechend den genehmigten Abweichungen flexibel verarbeitet und die Finanzdaten bleiben korrekt.
