# Fehlerbehebung

## Die neue Spalte erscheint nicht in der Validierungsmaske

* Das Dokument wurde verarbeitet, bevor die Spalte hinzugefügt wurde. Änderungen gelten für Dokumente, die danach hochgeladen oder neu gestartet werden, daher **starten Sie das Dokument neu** (Dashboard → Dokumentmenü → Restart).
* Die Spalte ist **Hidden**. Prüfen Sie das Flag in der Liste Table Columns.
* Die Spalte wurde einer **anderen Tabelle** hinzugefügt als der angezeigten. Die Validierungsmaske zeigt die Tabellen des Dokumenttyps; vergleichen Sie die Spalte *Table name*.
* Das Dokument gehört nicht zu dem Dokumenttyp, den Sie konfiguriert haben.

## Die Spalte ist vorhanden, aber immer leer

* Der Lieferant hat **trainierte Regeln**, und die neue Spalte ist darin nicht zugeordnet. Öffnen Sie eines der Dokumente des Lieferanten im Tabellentraining und ordnen Sie die Spalte zu, oder setzen Sie *Use AI* für die Spalte.
* Bei der KI-Extraktion ist der Wert auf dem Dokument nicht erkennbar (keine Kopfzeile, abgekürzt, in einer anderen Sprache). Fügen Sie einen [AI-Table-Tag](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) hinzu, der die Spalte benennt, oder ordnen Sie sie im Training zu.

## „Column name already exists“

Eine Spalte mit demselben technischen Namen ist bereits in der Tabelle vorhanden. Steht sie nicht in der Liste, handelt es sich um eine ausgeblendete Standardspalte: Die Meldung lautet *Please activate it in Table Column settings*. Entfernen Sie das Flag *Hidden* bei dieser Spalte, statt eine neue anzulegen.

## Die Freigabe ist durch eine erforderliche Spalte blockiert

Die Meldung an der Tabelle nennt die Spalte. Füllen Sie entweder die Zelle in jeder Zeile, oder (wenn der Wert auf diesem Dokument nicht existiert) deaktivieren Sie *Is Required* für die Spalte, starten Sie das Dokument neu und versuchen Sie es erneut. Überlegen Sie, ob die Spalte überhaupt erforderlich sein sollte (siehe [Best Practices](best-practices-2.md)).

## Die KI füllt eine Spalte mit dem falschen Wert

Typischer Fall: `CHARGES` erhält die Zeilensumme, und jede Zeile scheitert dann an der Zeilensummenprüfung mit *Line total does not match quantity x unit price (expected …, got …)*, weil Nebenkosten Teil der Formel `Menge × Einzelpreis + Nebenkosten` sind.

* Deaktivieren Sie *Use AI* für die Spalte, wenn die trainierten Regeln sie korrekt erfassen.
* Hat der Lieferant keine Regeln, trainieren Sie die Tabelle einmal (Tabellentraining), damit die Spalte an die richtige Position gebunden wird, oder blenden Sie die Spalte aus, wenn der Lieferant diesen Wert nie druckt.
* Als letzten Ausweg schaltet *Skip table validation* in den More Settings des Dokumenttyps jede Tabellenprüfung für den gesamten Dokumenttyp ab; die Abweichung wird dann nicht mehr erkannt, ebenso wenig leere erforderliche Spalten.

## Bestellabgleich: „Line Item Table is missing Mandatory column“

Der Bestellabgleich benötigt die Standardspalten Artikelnummer, Einzelpreis, Menge und Gesamtbetrag. Eine davon ist ausgeblendet oder wurde durch eine eigene Spalte ersetzt. Blenden Sie die Standardspalte wieder ein, oder ordnen Sie den Wert im Tabellentraining ihr zu.

## Ein Skript oder Export schlägt nach dem Löschen einer Spalte fehl

Das Skript oder Export-Mapping verweist noch auf den gelöschten *Column name*. Entfernen Sie den Verweis, oder fügen Sie die Spalte mit demselben Titel erneut hinzu; der technische Name wird aus dem Titel abgeleitet und passt dann wieder.

## Wo Sie weiter suchen können

* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): Extraktionsqualität, OCR, E-Text
* [Training Line Fields / Table Training](../../../../setup/document-training/training-line-fields-table-training/README.md)
