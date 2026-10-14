# Positionen im Export

Was mit der Positionstabelle geschieht, wenn ein Dokument freigegeben und exportiert wird, hängt von der Exportmethode ab. Diese Seite erklärt, welche Spalten DocBits verlassen, welche Pflicht sind und warum ein Export weniger Zeilen zeigen kann als der Validierungsbildschirm.

## Zwei Arten von Export

| Exportmethode | Was für die Tabelle gesendet wird |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | Die Tabelle so, wie sie im Validierungsbildschirm steht: jede nicht versteckte [Tabellenspalte](../../../admin-section/settings/global-settings/document-types/table-columns.md) jeder Zeile, mit Wert, formatiertem Wert und Konfidenz. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (Infor ERP / SAP BODs) | Nicht die Rohtabelle. DocBits bildet daraus **Wareneingangszeilen** (receipt lines) und **Kostenzeilen** (cost lines) (siehe unten) und bildet sie mit dem unter [Exportieren nach INFOR](../../../infor-integration-and-configuration/exporting-to-infor/README.md) konfigurierten Mapping auf die BOD-Felder ab. |

## Wareneingangszeilen und Kostenzeilen (Infor-Exporte)

Eine ERP-Rechnungszeile ist entweder eine **Wareneingangszeile** (sie gleicht einen Bestelleingang aus) oder eine **Kostenzeile** (sie bucht einen Betrag auf ein Sachkonto mit Dimensionen). DocBits entscheidet pro Rechnungsposition:

* **Wareneingangszeilen** entstehen aus dem **Bestellabgleich (PO-Matching)**. Jede Rechnungsposition, die einer Bestellposition zugeordnet wurde (Dashboard → PO Match, oder automatisch mit *PO auto match*), wird zu einer Wareneingangszeile mit Bestellnummer, Bestellposition, Wareneingangszeile sowie der zugeordneten Menge und dem Betrag. Eine Rechnung ohne Bestellabgleich hat **keine Wareneingangszeilen**; die Exportvorschau zeigt dann `receipt_lines: []`, was korrekt ist und kein Fehler.
* **Kostenzeilen** entstehen aus dem **Buchungssatz**, den der Kontierungsschritt (oder Auto Accounting) erzeugt: Sachkonto, Dimensionen, Betrag, Menge pro Zeile. Eine Rechnung ohne Buchungssatz hat keine Kostenzeilen.
* **Steuerzeilen** werden aus den Steuerbeträgen im Kopf gebildet, nicht aus der Tabelle.

Für Infor-Exporte ist die Positionstabelle also die *Eingabe* für Bestellabgleich und Kontierung; was das ERP erhält, ist das Ergebnis dieser beiden Schritte. Eine Position, die weder einer Bestellung zugeordnet noch kontiert ist, erreicht das ERP nicht.

{% hint style="warning" %}
Damit der Bestellabgleich funktioniert, muss die Tabelle die Standardspalten **Artikelnummer, Einzelpreis, Menge und Gesamtbetrag** haben. Ist eine davon versteckt, zeigt der Validierungsbildschirm *Line Item Table is missing Mandatory column for PO* (In der Positionstabelle fehlt eine obligatorische Spalte für die Bestellung), und es können keine Wareneingangszeilen gebildet werden.
{% endhint %}

## Pflichtspalten und der Freigabedialog

Bevor ein Dokument freigegeben werden kann, prüft DocBits die Tabelle:

1. Jede Spalte mit **Erforderlich** (Einstellungen → Dokumenttypen → Tabellenspalten) muss in jeder Zeile einen Wert haben.
2. Jede Zeile muss die **Positionssummenprüfung** bestehen: `Summe = Menge × Einzelpreis + Zuschläge − Rabatt` innerhalb von 0,02. Fehlgeschlagene Zeilen werden markiert; die Meldung nennt den erwarteten und den tatsächlichen Wert.
3. Die **Summe der Positionssummen** wird mit dem Nettobetrag im Kopf verglichen. Eine Abweichung ist eine Warnung und blockiert die Freigabe nicht.

Der Freigabedialog listet auf, was noch fehlt. Ein Administrator kann alle Tabellenprüfungen pro Dokumenttyp mit **Tabellenvalidierung überspringen** (Dokumenttypen → Weitere Einstellungen) abschalten; Positionssummen und erforderliche Spalten werden dann nicht mehr geprüft, die Kopfprüfungen bleiben.

Details zu den Meldungen: [Tabellenauszug Fehlerbehebung](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md#meldungen-an-der-tabelle).

## Leere Tabelle

* **JSON- / XML-Exporte** senden das Dokument mit `tables: []` (oder die Tabelle mit null Zeilen). Das empfangende System muss mit einer leeren Tabelle umgehen können.
* **Infor-Exporte** ohne Wareneingangszeilen und ohne Kostenzeilen senden nur den Kopf und die Steuerzeilen. Die meisten ERP-Systeme lehnen eine Rechnung ohne Zeilen ab: Konfigurieren Sie Auto Accounting oder eine Standard-Kostenzeile für solche Dokumenttypen, oder leiten Sie sie an einen anderen Export weiter.
* Ein Dokumenttyp **ohne Tabelle** (keine Tabelle konfiguriert) sendet nie Positionsdaten; das ist bei Dokumenttypen wie Auftragsbestätigungen, die auf Kopfebene abgeglichen werden, so vorgesehen.

## Vor der Freigabe prüfen

Partner und Support mit API- oder MCP-Zugang können die Export-Nutzlast eines Dokuments anfordern, bevor sie gesendet wird: Das MCP-Tool `get_export_preview(doc_id)` liefert genau das, was der Export senden wird, `receipt_lines`, `cost_lines` und `tax_lines` bei Infor-Exporten, `tables` bei JSON-Exporten. Verwenden Sie es, wenn das ERP fehlende Zeilen meldet: Ist `receipt_lines` leer, wurde die Rechnung nicht mit einer Bestellung abgeglichen; ist `cost_lines` leer, existiert kein Buchungssatz.

## Weitere Seiten

* [Export](export.md): Exportkonfigurationen und -methoden
* [Tabellenspalten](../../../admin-section/settings/global-settings/document-types/table-columns.md)
* [Exportieren nach INFOR](../../../infor-integration-and-configuration/exporting-to-infor/README.md): BOD-Feldzuordnungen für Wareneingangs-, Kosten- und Steuerzeilen
