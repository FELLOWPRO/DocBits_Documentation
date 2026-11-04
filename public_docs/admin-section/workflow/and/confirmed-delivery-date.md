# Bestätigtes Lieferdatum

<figure><img src="../../../.gitbook/assets/docbits_table_invoice_3.png" alt="Tabelle Rechnung Übersicht"><figcaption></figcaption></figure>

Zweck: Diese DocBits-Karte ist darauf ausgelegt sicherzustellen, dass die bestätigten Liefertermine auf Rechnungen oder Versanddokumenten mit den akzeptierten Lieferterminen gemäß der Master-Daten-Lookup-Tabelle übereinstimmen. Sie hilft dabei, Erwartungen zu managen und die Einhaltung der geplanten Lieferungen innerhalb der Lieferkette sicherzustellen.

## Funktionalität:

* Bestätigtes Lieferdatum: Dieser Bestandteil der Karte erfasst das Lieferdatum, wie es auf der Rechnung oder im Versanddokument bestätigt wurde.
* Master-Daten-Tabellensuche: Die Karte verweist auf eine vom Benutzer festgelegte Master-Daten-Lookup-Tabelle (identifiziert durch den Parameter \<Master Data Table>). Diese Tabelle enthält die akzeptierten Liefertermine zum Vergleich.
* Operatorwert: Benutzer können angeben, wie das bestätigte Lieferdatum im Vergleich zum akzeptierten Lieferdatum aus der Master-Daten-Tabelle stehen soll. Verfügbare Operatoren sind:
*
* Gleich (=): Stellt sicher, dass das bestätigte Lieferdatum mit dem akzeptierten Lieferdatum übereinstimmt.
* Nicht gleich (≠): Zeigt eine Diskrepanz zwischen den bestätigten und akzeptierten Lieferterminen an.
* Vor (<): Überprüft, ob das bestätigte Lieferdatum früher als das akzeptierte Lieferdatum ist.
* Nach (>): Überprüft, ob das bestätigte Lieferdatum später als das akzeptierte Lieferdatum ist.

Verwendung: Diese Karte ist für ERP-Manager und Finanzbuchhalter unverzichtbar, die Lieferpläne überwachen und die Einhaltung sicherstellen müssen. Sie ist besonders nützlich in Branchen, in denen pünktliche Lieferungen entscheidend sind, wie z.B. in der Fertigung, im Einzelhandel und in der Distribution.

## Beispiel Szenario:

* Eine Rechnung listet ein bestätigtes Lieferdatum vom 10. Juni auf. Die Master-Daten-Tabelle zeigt jedoch ein akzeptiertes Lieferdatum vom 15. Juni. Durch Einstellen des Operators auf "Vor" bestätigt die Karte, dass die Waren für eine frühzeitige Lieferung geplant sind, was es der Logistikplanung ermöglicht, entsprechend anzupassen.

Durch die Implementierung der Karte "Vergleich mit Bestellung: Bestätigte vs. Akzeptierte Liefertermine" können Organisationen proaktiv ihre Lieferkette verwalten und sicherstellen, dass Lieferungen gemäß vereinbarter Zeitpläne geplant und durchgeführt werden, wodurch die operationale Effizienz und die Kundenzufriedenheit verbessert werden.
