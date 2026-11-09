# Zuschlag je Einheit außerhalb der Toleranz (abgelehnt)

> **Hinweis zu den Beispielen:** Das folgende Szenario ist eine beispielhafte konfigurierte Zuordnung, keine geprüfte, ausgelieferte Standardvorlage. Die tatsächliche Ausgabe, Beträge, Vorzeichen und Dokumenttypen hängen von den aktiven `conflict_resolution`-Regeln und -Ausdrücken, der Exportzuordnung und den Genehmigungsentscheidungen ab. Eine unten beschriebene Belastungsanzeige oder Gutschrift ist von dieser Konfiguration abhängig; das Beispiel garantiert weder eine automatische Ausstellung noch rechtliche Konformität.


## Szenario:

Der Zuschlag je Einheit liegt außerhalb der Toleranz und wurde nicht genehmigt.

## Aktion:

Das System passt den Zuschlag je Einheit an die Bestellung oder den genehmigten Wert an und erstellt gegebenenfalls die erforderlichen Belastungsanzeigen oder Gutschriften.

## Beispiel:

* **Bestellung (PO):**
  * Zuschlag je Einheit: $6.00
  * Menge: 800 Einheiten
  * Zuschlagsgesamtbetrag: $4,800.00
* **Eingegangene Rechnung:**
  * Zuschlag je Einheit: $7.00 (Abweichung 16.67%, außerhalb der ±5%-Toleranz, abgelehnt)
  * Menge: 800 Einheiten
  * Zuschlagsgesamtbetrag: $5,600.00
* **Toleranzgrenzen:**
  * Toleranz für Zuschläge je Einheit: ±5%

Der Zuschlag je Einheit ($7.00) überschreitet die zulässige Toleranz von 5% und wurde nicht genehmigt. Das System führt folgende Schritte aus:

1. **Berechneten Zuschlag je Einheit ablehnen:** Das System akzeptiert den Zuschlag von $7.00 nicht, da die Abweichung die Toleranzgrenze überschreitet.
2. **Zuschlag je Einheit anpassen:** Das System setzt den Zuschlag auf den Wert aus der Bestellung oder auf den genehmigten Wert:
   * Angepasster Zuschlag je Einheit = $6.00 (aus der Bestellung)
3. **Gesamten Zuschlagsbetrag neu berechnen:** Das System berechnet den gesamten Zuschlagsbetrag anhand des angepassten Zuschlags je Einheit neu:
   * **Korrigierter Zuschlagsgesamtbetrag = Menge × Angepasster Zuschlag je Einheit**
   * **Korrigierter Zuschlagsgesamtbetrag = 800 Einheiten × $6.00 = $4,800.00**
4. **Belastungsanzeige erstellen:** Da der ursprüngliche Rechnungsbetrag höher als der korrigierte Gesamtbetrag war, erstellt das System eine Belastungsanzeige über den zu viel berechneten Betrag:
   * **Betrag der Belastungsanzeige = Ursprünglicher Rechnungsbetrag - Korrigierter Zuschlagsgesamtbetrag**
   * **Betrag der Belastungsanzeige = $5,600.00 - $4,800.00 = $800.00**
5. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem korrigierten Zuschlagsgesamtbetrag von $4,800.00 und erstellt eine Belastungsanzeige über $800.00, um den zu viel berechneten Betrag auszugleichen.

Damit entsprechen die Finanztransaktionen den Bestellbedingungen. Nicht genehmigte Abweichungen werden abgelehnt und eine korrekte Abrechnung wird sichergestellt.
