# Zweck und Verwendung

Eine Tabellenspalte ist ein Feld der Positionstabelle. Alles, was DocBits mit einer Tabelle macht (Extraktion, Validierung, Bestellabgleich, Export), arbeitet mit den hier konfigurierten Spalten.

## Wo eine Spalte erscheint

| Ort | Was die Spalte dort bewirkt |
|---|---|
| **Validierungsmaske** | Eine Spalte in der Positionstabelle. Der *Title* ist die Kopfzeile, der *Column Type* bestimmt den Editor (Betrag, Datum, Text, Ja/Nein). Ausgeblendete Spalten werden nicht angezeigt. |
| **Tabellentraining** | Beim Training der Tabelle eines Lieferanten ordnen Sie jede erkannte Tabellenspalte einer dieser konfigurierten Spalten zu. Nur konfigurierte Spalten können zugeordnet werden. |
| **KI-Tabellenextraktion** | Die KI füllt die konfigurierten Spalten. Eine mit *Use AI* markierte Spalte wird von der KI auch bei Lieferanten mit trainierten Regeln gefüllt. |
| **Validierungsregeln** | Positionsprüfungen wie *Menge × Einzelpreis = Zeilensumme* laufen auf den Standardspalten `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **Bestellabgleich** | Benötigt die Standardspalten Artikelnummer, Einzelpreis, Menge und Gesamtbetrag. Fehlen sie, zeigt das Dokument *Line Item Table is missing Mandatory column for PO*. |
| **Export** | Jede nicht ausgeblendete Spalte ist Teil der Positionsdaten, die an das ERP gesendet werden. Das Export-Mapping verweist auf den *Column name*. |
| **Skripte** | Skripte lesen und schreiben Spalten über den *Column name*, zum Beispiel `row["TOTAL_AMOUNT"]`. |

## Geltungsbereich

* Tabellenspalten werden **pro Tabelle** konfiguriert, und eine Tabelle gehört zu einem **Dokumenttyp**. Rechnungsspalten wirken sich nicht auf Lieferscheine aus.
* Die Konfiguration gilt **pro Organisation**. Unterorganisationen erben sie.
* Welche Spalten für einen bestimmten Lieferanten *gefüllt* werden, entscheidet das Training dieses Lieferanten oder die KI; die Spaltenkonfiguration legt nur fest, welche Spalten existieren.

## Typische Gründe, die Konfiguration zu ändern

* Ein kundenspezifischer Wert muss pro Position erfasst werden (Kostenstelle, Projektnummer, interne Artikelnummer) → Spalte hinzufügen.
* Eine Standardspalte wird nie verwendet und überfrachtet die Validierungsmaske → ausblenden.
* Eine Spalte muss vor dem Export immer gefüllt sein → als *Required* markieren.
* Ein Wert stammt aus dem ERP-Lookup und darf von Benutzern nicht bearbeitet werden → als *Read Only* markieren.
* Die KI erfasst eine Spalte besser als die trainierten Regeln (zum Beispiel Freitextbeschreibungen) → als *Use AI* markieren.

## Verwandte Seiten

* [Neue Spalte hinzufügen](adding-a-new-column.md)
* [Spalten bearbeiten und löschen](editing-and-deleting-columns.md)
* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
