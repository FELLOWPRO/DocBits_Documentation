# TransactionConfig-Pro-Vorlage

> **Hinweis zu den Beispielen:** Die folgenden Abläufe veranschaulichen eine konfigurierte Exportzuordnung. Tatsächliche Ausgaben, Beträge, Vorzeichen und Dokumenttypen hängen von der aktiven Exportzuordnung, ihren Konfliktregeln und den Genehmigungsentscheidungen ab. Die Beispiele beschreiben keine bedingungslose automatische Ausstellung rechtlich wirksamer Belastungsanzeigen oder Gutschriften.


## Umfassendes Konfigurationswerkzeug für die Verarbeitung von Finanzdokumenten

_TransactionConfig Pro Template_ ist ein Konfigurationswerkzeug für die Verarbeitung von Finanzdokumenten wie Rechnungen, Belastungsanzeigen und Gutschriften in Unternehmen. Detaillierte Zuordnungen und Felddefinitionen ermöglichen es, Finanzabläufe gezielt zu automatisieren und anzupassen. Das Werkzeug integriert sich in bestehende Infor-ERP-Systeme. Welche Transaktions- und Korrekturdaten entstehen, bestimmt die konkrete Konfiguration.

### Hauptfunktionen

• Detaillierte Zuordnung: Felder lassen sich für unterschiedliche Transaktionsarten präzise zuordnen, um konsistente und genaue Daten sicherzustellen.

• Anpassung: Finanzdokumenten-Workflows können an die Anforderungen des Unternehmens angepasst werden.

• Automatisierung: Die automatische Bearbeitung von Finanztransaktionen verringert manuelle Fehler und erhöht die Effizienz.

• Integration: Die Anbindung an bestehende Infor-M3/LN-ERP-Systeme erweitert die Möglichkeiten der Finanzverarbeitung.

• Regelpflege: Unternehmen können Zuordnungen und Verarbeitungsregeln an ihre Anforderungen anpassen. Ob die konkrete Konfiguration die einschlägigen steuerlichen und rechtlichen Vorgaben erfüllt, muss für den jeweiligen Anwendungsfall und Rechtsraum geprüft werden.



## Fallbeschreibungen zur Behandlung von Abweichungen

_TransactionConfig Pro Template_ enthält vordefinierte Regeln für häufige Abweichungen zwischen Rechnungs- und Bestelldaten (Purchase Order, PO). Diese Regeln automatisieren Entscheidungen bei Abweichungen und sollen eine konsistente, genaue Finanzverarbeitung sicherstellen.

### [Fall 1, 2, 3: Menge und Stückpreis innerhalb der Toleranz](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Szenario:** Sowohl die Rechnungsmenge als auch der Stückpreis liegen im Vergleich zur Bestellung innerhalb der zulässigen Toleranz.

• **Aktion:** Das System akzeptiert die Rechnungswerte und berechnet den Gesamtbetrag anhand der angegebenen Menge und des Stückpreises.

### [Fall 4, 5: Menge innerhalb der Toleranz, Stückpreis außerhalb der Toleranz (genehmigt)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Szenario:** Die Rechnungsmenge liegt innerhalb der Toleranz. Der Stückpreis liegt außerhalb der Toleranz; diese Abweichung wurde jedoch genehmigt.

• **Aktion:** Das System passt den Stückpreis an die Bestellung an und berücksichtigt die Differenz gegebenenfalls über Positionszuschläge.

### [Fall 6: Menge innerhalb der Toleranz, Stückpreis unterhalb der Toleranzgrenze (abgelehnt)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Szenario:** Die Menge liegt innerhalb der Toleranz. Der Stückpreis unterschreitet jedoch den zulässigen Bereich (negative Toleranz); die Abweichung wurde nicht genehmigt.

• **Aktion:** Die Beispielzuordnung setzt den Stückpreis auf den Bestellwert zurück. Ob weitere Kopfzuschläge oder Korrekturbelege entstehen, hängt von den aktiven Konfliktregeln und Exportaktionen ab.

### [Fall 7: Menge innerhalb der Toleranz, Stückpreis oberhalb der Toleranz abgelehnt](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Szenario:** Die Menge liegt innerhalb der Toleranz. Der Stückpreis überschreitet jedoch den zulässigen Bereich (positive Toleranz); die Abweichung wurde nicht genehmigt.

• **Aktion:** Das System lehnt den Rechnungsstückpreis ab und passt ihn an die Bestellung an. Es kann eine Belastungsanzeige erstellen, um den zu viel berechneten Betrag auszugleichen.

### [Fall 8a, 9a: Menge außerhalb der Toleranz (genehmigt), Stückpreis innerhalb der Toleranz](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Szenario:** Die Rechnungsmenge liegt außerhalb der zulässigen Toleranz, wurde jedoch genehmigt. Der Stückpreis liegt innerhalb der Toleranz.

• **Aktion:** Das System akzeptiert die genehmigte Menge und den Stückpreis aus der Rechnung und verarbeitet die Transaktion entsprechend.

### [Fall 11a: Menge oberhalb der Toleranz abgelehnt, Stückpreis innerhalb der Toleranz](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Szenario:** Die Rechnungsmenge überschreitet den zulässigen Bereich (positive Abweichung) und wird abgelehnt. Der Stückpreis liegt innerhalb der Toleranz.

• **Aktion:** Das System setzt die Menge auf den genehmigten Wert, behält den Stückpreis bei und verarbeitet die Transaktion. Die Mehrmenge wird abgelehnt und nicht berechnet.

### [Fall 10a: Menge unterhalb der Toleranz abgelehnt, Stückpreis innerhalb der Toleranz](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Szenario:** Die Menge unterschreitet den zulässigen Bereich (negative Toleranz) und wurde nicht genehmigt. Der Stückpreis liegt dagegen innerhalb der Toleranz.

• **Aktion:** Das System passt die Menge an den genehmigten Wert an und behält den Stückpreis bei. Anschließend wird die Transaktion entsprechend verarbeitet.

### [Fall 8b, 9b: Menge außerhalb der Toleranz (genehmigt), Stückpreis außerhalb der Toleranz (genehmigt)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Szenario:** Sowohl die Menge als auch der Stückpreis liegen außerhalb der Toleranz, wurden jedoch genehmigt.

• **Aktion:** Das System verarbeitet die Transaktion anhand der Rechnungswerte für Menge und Stückpreis und berücksichtigt gegebenenfalls erforderliche Anpassungen oder Positionszuschläge.

### [Fall 10b: Menge unterhalb der Toleranz abgelehnt, Stückpreisabweichung abgelehnt](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Szenario:** Sowohl die Menge als auch der Stückpreis liegen außerhalb der Toleranz; keiner der Werte wurde genehmigt.

• **Aktion:** Das System lehnt die Rechnungsdaten ab, passt die Werte an die Bestellung an und erstellt die erforderlichen Belastungsanzeigen oder Gutschriften.

### [Fall 11b: Menge oberhalb der Toleranz abgelehnt, Stückpreisabweichung abgelehnt](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Szenario:** Die Menge überschreitet den zulässigen Bereich (positive Abweichung) und wird abgelehnt. Auch der Stückpreis liegt außerhalb der Toleranz und wird abgelehnt.

• **Aktion:** Das System passt Menge und Stückpreis an die genehmigten Bestellwerte an, lehnt darüber hinausgehende Werte ab und verarbeitet die Transaktion.

### [Fall 12, 13: Positionszuschlag – Zuschlag je Einheit innerhalb der Toleranz](charge-per-unit-within-tolerance.md)

**Szenario:** Der Zuschlag je Einheit auf der Rechnung liegt im Vergleich zur Bestellung innerhalb der zulässigen Toleranz.

• **Aktion:** Das System übernimmt den Zuschlag je Einheit aus der Rechnung und verarbeitet die Transaktion ohne Anpassungen.

### [Fall 14: Positionszuschlag – Zuschlag je Einheit außerhalb der Toleranz (genehmigt)](charge-per-unit-outside-tolerance-approved-1.md)

**Szenario:** Der Zuschlag je Einheit liegt außerhalb der Toleranz, wurde jedoch genehmigt.

• **Aktion:** Das System akzeptiert den Zuschlag je Einheit, berücksichtigt die genehmigten Zuschläge und verarbeitet die Transaktion entsprechend.

### [Fall 15: Positionszuschlag – Zuschlag je Einheit außerhalb der Toleranz (abgelehnt)](charge-per-unit-outside-tolerance-rejected.md)

**Szenario:** Der Zuschlag je Einheit liegt außerhalb der Toleranz und wurde nicht genehmigt.

• **Aktion:** Das System passt den Zuschlag je Einheit an die Bestellung oder den genehmigten Wert an und erstellt gegebenenfalls die erforderlichen Belastungsanzeigen oder Gutschriften.

### [Fall 12, 13: Kopfzuschlag – Zuschlag je Einheit innerhalb der Toleranz](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Szenario:** Der Zuschlag auf Kopfebene je Einheit liegt im Vergleich zur Bestellung innerhalb der zulässigen Toleranz.

• **Aktion:** Das System übernimmt den Zuschlag auf Kopfebene aus der Rechnung ohne Anpassungen.

### [Fall 14: Kopfzuschlag – Zuschlag je Einheit außerhalb der Toleranz (genehmigt)](charge-per-unit-outside-tolerance-approved.md)

**Szenario:** Der Zuschlag auf Kopfebene je Einheit liegt außerhalb der Toleranz, wurde jedoch genehmigt.

• **Aktion:** Das System übernimmt den genehmigten Zuschlag je Einheit in die Transaktion.

### [Fall 15: Kopfzuschlag – Zuschlag je Einheit außerhalb der Toleranz (abgelehnt)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Szenario:** Der Zuschlag auf Kopfebene je Einheit liegt außerhalb der Toleranz und wurde nicht genehmigt.

• **Aktion:** Das System passt den Kopfzuschlag an die Bestellung an, verarbeitet die Transaktion entsprechend und erstellt gegebenenfalls die erforderlichen Korrekturbelege.

### [Steuerzeilen](tax-lines.md "mention")

**Szenario:** Behandelt Abweichungen zwischen den Steuerbeträgen der Rechnung und der Bestellung.

• **Aktion:** Das System passt die Steuerzeilen an die genehmigten Steuersätze und -beträge an, um die geltenden Steuervorschriften einzuhalten.
