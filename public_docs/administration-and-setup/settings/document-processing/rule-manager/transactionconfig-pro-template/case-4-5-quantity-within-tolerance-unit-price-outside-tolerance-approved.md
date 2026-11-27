# Fall 4, 5: Menge innerhalb der Toleranz, Stückpreis außerhalb der Toleranz (genehmigt)

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Szenario:

Die Rechnungsmenge liegt innerhalb der Toleranz, der Stückpreis dagegen außerhalb des zulässigen Bereichs. Die zuständigen Stellen haben diese Stückpreisabweichung jedoch geprüft und genehmigt.

## Aktion:

Das System passt den Stückpreis an die Bestellung an und berücksichtigt die Differenz gegebenenfalls über Positionszuschläge.

## Beispiel:

**Purchase Order (PO):**

Quantity: <mark style="color:green;">100</mark> units

Unit Price: $10.00 per unit

Total Amount: <mark style="color:purple;">$1,000.00</mark>

**Invoice Received:**

Quantity: <mark style="color:green;">100</mark> units (within tolerance)

Unit Price: <mark style="color:red;">$11.00</mark> per unit (outside tolerance of ±5%)

Total Amount: <mark style="color:red;">$1,100.00</mark>

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±5% (expected range: $9.50 to $10.50)

**Approval:**

• The $11.00 unit price is outside the tolerance range but has been manually approved by the appropriate department.

Die Menge liegt innerhalb der Toleranz. Der Stückpreis liegt außerhalb der Toleranz, wurde jedoch genehmigt. Das System führt folgende Schritte aus:

1\. **Adjust the Unit Price**: Das System setzt den Stückpreis auf den Bestellwert zurück, da die Abweichung genehmigt wurde:

• **Adjusted Unit Price = $10.00 per unit**

• **Adjusted Total Amount = 100 units × $10.00 per unit = $1,000.00**

2\. **Apply a Line Charge for the Difference**: Der genehmigte Stückpreis von $11.00 liegt über dem Bestellstückpreis von $10.00. Das System berücksichtigt diese Differenz daher als Positionszuschlag:

• **Line Charge Amount = (Approved Invoice Unit Price - PO Unit Price) × Quantity**

• **Line Charge Amount = ($11.00 - $10.00) × 100 units = $100.00**

3\. **Process the Invoice**: Das System verarbeitet die Rechnung mit folgenden Beträgen:

• **Base Amount:** $1,000.00

• **Line Charge:** $100.00

• **Total Processed Amount:** $1,100.00

So bleiben die ursprünglichen Bestellwerte erhalten, während die genehmigte Stückpreisabweichung als zusätzlicher Positionszuschlag berücksichtigt wird. Das ermöglicht eine korrekte Verarbeitung und Buchführung.
