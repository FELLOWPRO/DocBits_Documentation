# Fall 10a: Menge unterhalb der Toleranz abgelehnt, Stückpreis innerhalb der Toleranz

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Menge unterschreitet den zulässigen Bereich (negative Toleranz) und wurde nicht genehmigt. Der Stückpreis liegt dagegen innerhalb der Toleranz.

## Aktion:

Das System passt die Menge an den genehmigten Wert an und behält den Stückpreis bei. Anschließend wird die Transaktion entsprechend verarbeitet.

## Beispiel:

* **Bestellung (PO):**
  * Menge: 150 Einheiten
  * Stückpreis: $20.00 je Einheit
  * Gesamtbetrag: $3,000.00
* **Eingegangene Rechnung:**
  * Menge: 140 Einheiten (Abweichung außerhalb der Toleranz: -6.67%, abgelehnt)
  * Stückpreis: $20.00 je Einheit (innerhalb der Toleranz)
  * Gesamtbetrag: $2,800.00
* **Toleranzgrenzen:**
  * Mengentoleranz: ±5%
  * Stückpreistoleranz: ±2%

Die Menge (140 Einheiten) unterschreitet die zulässige Toleranzgrenze (negative Abweichung von -6.67%) und wurde nicht genehmigt. Der Stückpreis ($20.00) liegt innerhalb der Toleranz. Das System führt folgende Schritte aus:

1. **Niedrigere Menge ablehnen:** Das System akzeptiert die niedrigere Menge nicht, da sie außerhalb des genehmigten Toleranzbereichs liegt.
2. **Menge anpassen:** Das System setzt die Menge auf den genehmigten Wert aus der Bestellung.
   * Genehmigte Menge = 150 Einheiten (aus der Bestellung)
3. **Stückpreis beibehalten:** Der Stückpreis von $20.00 je Einheit liegt innerhalb der Toleranz und bleibt unverändert.
4. **Gesamtbetrag neu berechnen:** Das System berechnet den Gesamtbetrag anhand der genehmigten Menge und des akzeptierten Stückpreises:
   * **Gesamtbetrag = Genehmigte Menge × Stückpreis**
   * **Gesamtbetrag = 150 Einheiten × $20.00 je Einheit = $3,000.00**
5. **Rechnung verarbeiten:** Das System verarbeitet die Rechnung mit dem angepassten Gesamtbetrag von $3,000.00, der die genehmigte Menge und den genehmigten Stückpreis widerspiegelt. Der Lieferant soll die vollständige genehmigte Menge berechnen.

Damit entspricht die Finanztransaktion den Bestellbedingungen. Eine zu niedrige Abrechnung wird vermieden und die Finanzdaten bleiben korrekt.
