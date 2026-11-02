# Fall 4, 5: Menge innerhalb der Toleranz, Stückpreis außerhalb der Toleranz (genehmigt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Rechnungsmenge liegt innerhalb der Toleranz, der Stückpreis dagegen außerhalb des zulässigen Bereichs. Die zuständigen Stellen haben diese Stückpreisabweichung jedoch geprüft und genehmigt.

## Aktion:

Das System passt den Stückpreis an die Bestellung an und berücksichtigt die Differenz gegebenenfalls über Positionszuschläge.

## Beispiel:

**Bestellung (PO):**

Menge: <mark style="color:green;">100</mark> Einheiten

Stückpreis: $10.00 je Einheit

Gesamtbetrag: <mark style="color:purple;">$1,000.00</mark>

**Eingegangene Rechnung:**

Menge: <mark style="color:green;">100</mark> Einheiten (innerhalb der Toleranz)

Stückpreis: <mark style="color:red;">$11.00</mark> je Einheit (Abweichung außerhalb der Toleranz: ±5%)

Gesamtbetrag: <mark style="color:red;">$1,100.00</mark>

**Toleranzgrenzen:**

Mengentoleranz: ±2%

Stückpreistoleranz: ±5% (erwarteter Bereich: $9.50 bis$10.50)

**Genehmigung:**

• Der Stückpreis von $11.00 liegt außerhalb der Toleranz, wurde jedoch von der zuständigen Abteilung manuell genehmigt.

Die Menge liegt innerhalb der Toleranz. Der Stückpreis liegt außerhalb der Toleranz, wurde jedoch genehmigt. Das System führt folgende Schritte aus:

1\. **Stückpreis anpassen**: Das System setzt den Stückpreis auf den Bestellwert zurück, da die Abweichung genehmigt wurde:

• **Angepasster Stückpreis = $10.00 je Einheit**

• **Angepasster Gesamtbetrag = 100 Einheiten × $10.00 je Einheit = $1,000.00**

2\. **Differenz als Positionszuschlag berücksichtigen**: Der genehmigte Stückpreis von $11.00 liegt über dem Bestellstückpreis von $10.00. Das System berücksichtigt diese Differenz daher als Positionszuschlag:

• **Positionszuschlagsbetrag = (Genehmigter Rechnungsstückpreis - Bestellstückpreis) × Menge**

• **Positionszuschlagsbetrag = ($11.00 - $10.00) × 100 Einheiten = $100.00**

3\. **Rechnung verarbeiten**: Das System verarbeitet die Rechnung mit folgenden Beträgen:

• **Grundbetrag:** $1,000.00

• **Positionszuschlag:** $100.00

• **Verarbeiteter Gesamtbetrag:** $1,100.00

So bleiben die ursprünglichen Bestellwerte erhalten, während die genehmigte Stückpreisabweichung als zusätzlicher Positionszuschlag berücksichtigt wird. Das ermöglicht eine korrekte Verarbeitung und Buchführung.
