# Zuschlag je Einheit innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Der Zuschlag auf Kopfebene je Einheit liegt im Vergleich zur Bestellung innerhalb der zulässigen Toleranz.

## Aktion:

Das System übernimmt den Zuschlag auf Kopfebene aus der Rechnung ohne Anpassungen.

## Beispiel:

* **Bestellung (PO):**
  * Kopfzuschlag je Einheit: $3.50
  * Menge: 1,200 Einheiten
  * Kopfzuschlagsgesamtbetrag: $4,200.00
* **Eingegangene Rechnung:**
  * Kopfzuschlag je Einheit: $3.55 (Abweichung innerhalb der Toleranz: 1.43%)
  * Menge: 1,200 Einheiten
  * Kopfzuschlagsgesamtbetrag: $4,260.00
* **Toleranzgrenzen:**
  * Toleranz für Kopfzuschläge je Einheit: ±2%

Der Zuschlag auf Kopfebene je Einheit ($3.55) liegt im Vergleich zur Bestellung innerhalb der zulässigen Toleranz von 2%. Das System führt folgende Schritte aus:

1. **Zuschlag auf Kopfebene je Einheit akzeptieren:** Das System akzeptiert den berechneten Zuschlag von $3.55, da er innerhalb der festgelegten Toleranzgrenze liegt.
2. **Zuschlag auf Kopfebene verarbeiten:** Das System verarbeitet die Rechnung mit dem gesamten Kopfzuschlag, der sich aus dem berechneten Zuschlag je Einheit und der Menge ergibt:
   * **Kopfzuschlagsgesamtbetrag = Menge × Kopfzuschlag je Einheit**
   * **Kopfzuschlagsgesamtbetrag = 1,200 Einheiten × $3.55 = $4,260.00**
3. **Rechnung abschließen:** Das System verarbeitet die Transaktion ohne Anpassungen und übernimmt die Rechnung unverändert.

So lassen sich Transaktionen mit Kopfzuschlägen innerhalb der zulässigen Toleranz ohne unnötige Ablehnungen oder Verzögerungen verarbeiten.
