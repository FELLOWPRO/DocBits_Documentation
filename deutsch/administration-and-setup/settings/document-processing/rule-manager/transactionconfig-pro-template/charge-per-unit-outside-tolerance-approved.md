# Fall 14: Kopfzuschlag – Zuschlag je Einheit außerhalb der Toleranz (genehmigt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Der Zuschlag auf Kopfebene je Einheit liegt außerhalb der Toleranz, wurde jedoch genehmigt.

## Aktion:

Das System übernimmt den genehmigten Zuschlag je Einheit in die Transaktion.

## Beispiel:

* **Bestellung (PO):**
  * Kopfzuschlag je Einheit: $2.50
  * Menge: 2,000 Einheiten
  * Kopfzuschlagsgesamtbetrag: $5,000.00
* **Eingegangene Rechnung:**
  * Kopfzuschlag je Einheit: $3.00 (Abweichung außerhalb der Toleranz: 20%, genehmigt)
  * Menge: 2,000 Einheiten
  * Kopfzuschlagsgesamtbetrag: $6,000.00
* **Toleranzgrenzen:**
  * Toleranz für Kopfzuschläge je Einheit: ±5%

Der Zuschlag auf Kopfebene je Einheit ($3.00) überschreitet die zulässige Toleranz von 5%, wurde jedoch genehmigt. Das System führt folgende Schritte aus:

1. **Genehmigten Kopfzuschlag je Einheit akzeptieren:** Das System akzeptiert den berechneten Zuschlag von $3.00, da er trotz Überschreitung der Toleranzgrenze genehmigt wurde.
2. **Kopfzuschlag verarbeiten:** Das System verarbeitet die Rechnung anhand des genehmigten Zuschlags je Einheit und der Menge:
   * **Kopfzuschlagsgesamtbetrag = Menge × Genehmigter Kopfzuschlag je Einheit**
   * **Kopfzuschlagsgesamtbetrag = 2,000 Einheiten × $3.00 = $6,000.00**
3. **Rechnung abschließen:** Das System verarbeitet die Transaktion mit den genehmigten Zuschlägen und dem Gesamtbetrag von $6,000.00.

Damit berücksichtigt das System genehmigte Abweichungen bei Kopfzuschlägen. Die Transaktion wird entsprechend der Genehmigung verarbeitet und die Finanzdaten bleiben korrekt.
