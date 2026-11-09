# Zuschlag je Einheit innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Das folgende Szenario ist eine beispielhafte konfigurierte Zuordnung, keine geprüfte, ausgelieferte Standardvorlage. Die tatsächliche Ausgabe, Beträge, Vorzeichen und Dokumenttypen hängen von den aktiven `conflict_resolution`-Regeln und -Ausdrücken, der Exportzuordnung und den Genehmigungsentscheidungen ab. Eine unten beschriebene Belastungsanzeige oder Gutschrift ist von dieser Konfiguration abhängig; das Beispiel garantiert weder eine automatische Ausstellung noch rechtliche Konformität.


## Szenario:

Der Zuschlag je Einheit auf der Rechnung liegt im Vergleich zur Bestellung innerhalb der zulässigen Toleranz.

## Aktion:

Das System übernimmt den Zuschlag je Einheit aus der Rechnung und verarbeitet die Transaktion ohne Anpassungen.

## Beispiel:

* **Bestellung (PO):**
  * Zuschlag je Einheit: $5.00
  * Menge: 500 Einheiten
  * Zuschlagsgesamtbetrag: $2,500.00
* **Eingegangene Rechnung:**
  * Zuschlag je Einheit: $5.10 (Abweichung 2%, innerhalb der ±3%-Toleranz)
  * Menge: 500 Einheiten
  * Zuschlagsgesamtbetrag: $2,550.00
* **Toleranzgrenzen:**
  * Toleranz für Zuschläge je Einheit: ±3%

Der Zuschlag je Einheit ($5.10) liegt im Vergleich zur Bestellung innerhalb der zulässigen Toleranz von 3%. Das System führt folgende Schritte aus:

1. **Zuschlag je Einheit akzeptieren:** Das System akzeptiert den berechneten Zuschlag von $5.10, da er innerhalb der festgelegten Toleranzgrenze liegt.
2. **Transaktion verarbeiten:** Das System verarbeitet die Rechnung mit dem gesamten Zuschlagsbetrag, der sich aus dem berechneten Zuschlag je Einheit und der Menge ergibt:
   * **Zuschlagsgesamtbetrag = Menge × Zuschlag je Einheit**
   * **Zuschlagsgesamtbetrag = 500 Einheiten × $5.10 = $2,550.00**
3. **Rechnung abschließen:** Das System verarbeitet die Transaktion ohne Anpassungen und übernimmt die Rechnung unverändert.

Damit kann das System kleine zulässige Zuschlagsabweichungen ohne unnötige Ablehnungen oder Verzögerungen verarbeiten.
