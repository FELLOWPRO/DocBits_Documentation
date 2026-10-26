# Steuerzeilen

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Behandelt Abweichungen zwischen den Steuerbeträgen der Rechnung und der Bestellung.

## Aktion:

Die Beispielzuordnung passt die Steuerzeilen an die konfigurierten genehmigten Steuersätze und -beträge an. Die fachliche und steuerliche Richtigkeit dieser Vorgaben muss gesondert geprüft werden.

## Beispiel:

* **Bestellung (PO):**
  * Zwischensumme: $10,000.00
  * Steuersatz: 8%
  * Erwarteter Steuerbetrag: $800.00
  * Gesamtbetrag einschließlich Steuer: $10,800.00
* **Eingegangene Rechnung:**
  * Zwischensumme: $10,000.00
  * Steuersatz: 10% (Abweichung)
  * Berechneter Steuerbetrag: $1,000.00
  * Gesamtbetrag einschließlich Steuer: $11,000.00

Der Steuersatz der Rechnung (10%) weicht vom erwarteten Steuersatz (8%) ab und wurde nicht genehmigt. Das System führt folgende Schritte aus:

1. **Berechneten Steuersatz ablehnen:** Das System akzeptiert den Steuersatz von 10% nicht, da er nicht dem genehmigten Satz aus der Bestellung entspricht.
2. **Steuersatz anpassen:** Das System setzt den Steuersatz auf den genehmigten Wert aus der Bestellung.
   * Angepasster Steuersatz = 8% (aus der Bestellung)
3. **Steuerbetrag neu berechnen:** Das System berechnet den Steuerbetrag anhand des angepassten Steuersatzes neu:
   * **Korrigierter Steuerbetrag = Zwischensumme × Angepasster Steuersatz**
   * **Korrigierter Steuerbetrag = $10,000.00 × 8% = $800.00**
4. **Gesamtbetrag neu berechnen:** Das System berechnet den Gesamtbetrag einschließlich Steuer neu:
   * **Korrigierter Gesamtbetrag einschließlich Steuer = Zwischensumme + Korrigierter Steuerbetrag**
   * **Korrigierter Gesamtbetrag einschließlich Steuer = $10,000.00 + $800.00 = $10,800.00**
5. **Gutschrift erstellen:** Das System erstellt eine Gutschrift, um die zu viel berechnete Steuer zu korrigieren:
   * **Gutschriftsbetrag = Ursprünglicher Rechnungssteuerbetrag - Korrigierter Steuerbetrag**
   * **Gutschriftsbetrag = $1,000.00 - $800.00 = $200.00**
6. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem korrigierten Steuerbetrag von $800.00 und dem Gesamtbetrag von $10,800.00. Über die Steuerdifferenz von $200.00 wird eine Gutschrift erstellt.

Damit verwendet das Beispiel den konfigurierten erwarteten Steuersatz. Ob die Zuordnung im konkreten Anwendungsfall fachlich und steuerlich richtig ist, muss gesondert geprüft werden.
