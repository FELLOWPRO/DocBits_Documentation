# Fall 14: Positionszuschlag – Zuschlag je Einheit außerhalb der Toleranz (genehmigt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Der Zuschlag je Einheit liegt außerhalb der Toleranz, wurde jedoch genehmigt.

## Aktion:

Das System akzeptiert den Zuschlag je Einheit, berücksichtigt die genehmigten Zuschläge und verarbeitet die Transaktion entsprechend.

## Beispiel:

* **Bestellung (PO):**
  * Zuschlag je Einheit: $4.50
  * Menge: 1,000 Einheiten
  * Zuschlagsgesamtbetrag: $4,500.00
* **Eingegangene Rechnung:**
  * Zuschlag je Einheit: $5.00 (Abweichung außerhalb der Toleranz: 11.11%, genehmigt)
  * Menge: 1,000 Einheiten
  * Zuschlagsgesamtbetrag: $5,000.00
* **Toleranzgrenzen:**
  * Toleranz für Zuschläge je Einheit: ±5%

Der Zuschlag je Einheit ($5.00) liegt außerhalb der zulässigen Toleranz von 5%, wurde jedoch genehmigt. Das System führt folgende Schritte aus:

1. **Genehmigten Zuschlag je Einheit akzeptieren:** Das System akzeptiert den berechneten Zuschlag von $5.00, da er trotz Überschreitung der Toleranzgrenze genehmigt wurde.
2. **Transaktion verarbeiten:** Das System verarbeitet die Rechnung anhand des genehmigten Zuschlags je Einheit und der Menge:
   * **Zuschlagsgesamtbetrag = Menge × Genehmigter Zuschlag je Einheit**
   * **Zuschlagsgesamtbetrag = 1,000 Einheiten × $5.00 = $5,000.00**
3. **Rechnung abschließen:** Das System verarbeitet die Transaktion mit den genehmigten Zuschlägen und dem Gesamtbetrag von $5,000.00.

Damit berücksichtigt das System genehmigte Zuschlagsabweichungen flexibel und führt die Finanzdaten weiterhin korrekt.
