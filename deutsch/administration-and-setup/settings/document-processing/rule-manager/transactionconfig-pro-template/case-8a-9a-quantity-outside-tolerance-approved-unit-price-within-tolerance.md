# Fall 8a, 9a: Menge außerhalb der Toleranz (genehmigt), Stückpreis innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Rechnungsmenge liegt außerhalb der zulässigen Toleranz, wurde jedoch genehmigt. Der Stückpreis liegt innerhalb der Toleranz.

## Aktion:

Das System akzeptiert die genehmigte Menge und den Stückpreis aus der Rechnung und verarbeitet die Transaktion entsprechend.

## Beispiel:

* **Bestellung (PO):**
  * Menge: 150 Einheiten
  * Stückpreis: $12.00 je Einheit
  * Gesamtbetrag: $1,800.00
* **Eingegangene Rechnung:**
  * Menge: 160 Einheiten (Abweichung außerhalb der Toleranz: 6.67%, jedoch genehmigt)
  * Stückpreis: $12.00 je Einheit (innerhalb der Toleranz)
  * Gesamtbetrag: $1,920.00
* **Toleranzgrenzen:**
  * Mengentoleranz: ±5%
  * Stückpreistoleranz: ±2%

Die Menge (160 Einheiten) überschreitet die zulässige Toleranzgrenze, wurde jedoch genehmigt. Der Stückpreis ($12.00) liegt innerhalb des zulässigen Bereichs. Das System führt folgende Schritte aus:

1. **Genehmigte Menge akzeptieren:** Das System berücksichtigt, dass die Menge trotz Überschreitung des normalen Toleranzbereichs genehmigt wurde.
2. **Stückpreis akzeptieren:** Der Stückpreis von $12.00 je Einheit liegt innerhalb der zulässigen Toleranz und wird daher aus der Rechnung übernommen.
3. **Transaktion verarbeiten:** Das System berechnet den Gesamtbetrag anhand der genehmigten Menge und des Stückpreises:
   * **Gesamtbetrag = Menge × Stückpreis**
   * **Gesamtbetrag = 160 Einheiten × $12.00 je Einheit = $1,920.00**
4. **Rechnung abschließen:** Das System verarbeitet die Rechnung mit dem Gesamtbetrag von $1,920.00, der die genehmigte Menge und den akzeptierten Stückpreis widerspiegelt.

Damit berücksichtigt das System genehmigte Mengenabweichungen, während der Stückpreis im erwarteten Bereich bleibt. Das ermöglicht eine reibungslose Transaktionsverarbeitung.
