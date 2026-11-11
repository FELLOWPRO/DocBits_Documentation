# Fall 7: Menge innerhalb der Toleranz, Stückpreis außerhalb der Toleranz (positiv abgelehnt)

Das folgende Szenario ist eine beispielhafte konfigurierte Zuordnung, keine geprüfte Standardvorlage im Einsatz. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von den aktiven Regeln und Ausdrücken in `conflict_resolution`, der Exportzuordnung und den Genehmigungsentscheidungen ab. Jede unten beschriebene Belastungsanzeige oder Gutschrift ist von dieser Konfiguration abhängig; das Beispiel garantiert weder eine automatische Ausstellung noch rechtliche Konformität.

## Szenario:

Die Menge liegt innerhalb der Toleranz, der Stückpreis überschreitet jedoch den zulässigen Bereich (positive Toleranz) und ist nicht genehmigt.

## Aktion:

Das System lehnt den Rechnungsstückpreis ab, passt ihn an die Bestellung an und kann eine Belastungsanzeige für den zu viel berechneten Betrag erstellen.

## Beispiel:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $15.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 198 units — 1% below the PO value, within the configured ±2% tolerance.
  * Unit Price: $17.00 per unit — 13.33% above the PO value, outside the configured ±1% tolerance; rejected.
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Da die Menge (198 Einheiten) innerhalb des zulässigen Toleranzbereichs liegt, der Stückpreis ($17.00) jedoch die zulässige Toleranz überschreitet und nicht genehmigt ist, führt das System Folgendes aus:

1. **Rechnungsstückpreis ablehnen:** Das System akzeptiert den berechneten Stückpreis von $17.00 nicht.
2. **Stückpreis anpassen:** Das System passt den Stückpreis an den ursprünglichen Stückpreis der Bestellung an.
   * Adjusted Unit Price = $15.00 (aus der Bestellung)
3. **Korrigierten Gesamtbetrag berechnen:** Mit dem angepassten Stückpreis berechnet das System den Gesamtbetrag neu.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 198 units × $15.00 per unit = $2,970.00**
4. **Belastungsanzeige erstellen:** Das System erstellt eine Belastungsanzeige für die Differenz aus der zu hohen Berechnung.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $3,366.00 - $2,970.00 = $396.00**
   * Diese Belastungsanzeige entspricht dem vom Lieferanten zu viel berechneten Betrag.
5. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem korrigierten Gesamtbetrag von $2,970.00 und erstellt eine Belastungsanzeige über $396.00, um die zu hohe Berechnung auszugleichen.

So werden zu hohe Berechnungen korrigiert, die Transaktion an die Bedingungen der Bestellung angeglichen und die finanziellen Interessen des Unternehmens geschützt.
