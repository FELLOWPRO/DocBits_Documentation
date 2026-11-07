# Neue Spalte hinzufügen

Fügen Sie eine Spalte hinzu, wenn pro Position ein Wert erfasst werden muss, den die Standardspalten nicht abdecken, zum Beispiel eine Kostenstelle, eine Projektnummer oder eine interne Artikelnummer.

## Bevor Sie beginnen

* Entscheiden Sie, zu welcher **Tabelle** die Spalte gehört. Die meisten Dokumenttypen haben eine Tabelle (zum Beispiel `INVOICE_TABLE`). Ist die Liste leer, klicken Sie zuerst auf **Create new table**; der Dialog fragt nur nach einem Tabellennamen.
* Entscheiden Sie den **Typ**: `AMOUNT` für Geldbeträge, `NUMBER` für Mengen, `DATE`, `BOOLEAN` für Ja/Nein, `CURRENCY` für einen ISO-Währungscode, `STRING` für alles andere. Der Typ kann nach dem Speichern nicht mehr geändert werden.
* Prüfen Sie, ob bereits eine **Standardspalte** mit derselben Bedeutung existiert, aber ausgeblendet ist. Ausgeblendete Spalten stehen mit gesetztem Flag *Hidden* in der Liste; blenden Sie sie wieder ein, statt ein Duplikat anzulegen.

## Schritte

1. Öffnen Sie **Settings → Document Processing → Document Types → Table Columns**.
2. Klicken Sie auf **Add new table column**.

<figure><img src="../../../../../.gitbook/assets/table-columns_add-dialog-de.png" alt="Dialog Add new table column mit Title, Is column required, Select column type und Select Table"><figcaption><p>Dialog zum Hinzufügen einer neuen Tabellenspalte</p></figcaption></figure>

3. Füllen Sie den Dialog aus:

| Feld | Was Sie eingeben |
|---|---|
| **Title** | Bezeichnung, die der Benutzer in der Validierungsmaske sieht, zum Beispiel `Cost Centre`. Nur Buchstaben und Zahlen. DocBits leitet daraus den technischen *Column name* ab (`COST_CENTRE`). |
| **Is column required?** | Aktivieren, wenn das Dokument nicht freigegeben werden darf, solange die Spalte in einer beliebigen Zeile leer ist. |
| **Select column type** | Siehe die Typenliste oben. |
| **Select Table** | Die Tabelle, die die Spalte erhält. |

4. Klicken Sie auf **Weiter**. Ein Bestätigungsdialog weist darauf hin, dass die neue Spalte für **alle zukünftigen Rechnungen aller Lieferanten** gilt, nicht nur für das gerade geöffnete Dokument.

<figure><img src="../../../../../.gitbook/assets/mef178-column-create-confirm-de.png" alt="Bestätigungsdialog „Neue Tabellenspalte anlegen?“ mit den Schaltflächen Abbrechen und Spalte anlegen"><figcaption><p>Bestätigung, bevor die Spalte für alle Lieferanten angelegt wird.</p></figcaption></figure>

5. Prüfen Sie nach dem Anlegen die Einstellungen in der Liste. Read Only und Hidden sind zunächst aus. Use AI steht auf Standard; eine eigene Spalte wird damit normalerweise nicht angefordert. Wählen Sie Ja, wenn die strukturierte KI-Extraktion diese Spalte anfordern soll.

## Nach dem Hinzufügen

* Die Spalte ist bei **bestehenden Dokumenten leer**. Sie wird bei Dokumenten gefüllt, die nach der Änderung hochgeladen oder neu gestartet werden.
* Bei Lieferanten mit **trainierten Regeln** öffnen Sie eines ihrer Dokumente im Tabellentraining und ordnen die neue Spalte zu, sonst bleibt die Spalte für diesen Lieferanten leer. Siehe [Tabellen und Spalten definieren](../../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Setzen Sie bei strukturierter KI-Extraktion die eigene Spalte unter Use AI auf Ja und kontrollieren Sie die Vorschau. Das Anlegen allein fordert sie nicht an. Prüfen Sie gespeicherte Lieferantenzuordnungen und Anweisungen, verarbeiten Sie einen Testbeleg erneut und kontrollieren Sie das Ergebnis.
* Fügen Sie die Spalte dem **Export-Mapping** hinzu, wenn das ERP sie erhalten soll, siehe [Export](../../../document-processing/export.md).

## Meldungen

| Meldung | Bedeutung |
|---|---|
| *Column name already exists* | Eine Spalte mit diesem technischen Namen ist bereits in der Tabelle vorhanden. Wählen Sie einen anderen Titel. |
| *Column name already exists – Please activate it in Table Column settings* | Eine ausgeblendete Standardspalte hat diesen Namen. Entfernen Sie deren Flag *Hidden*, statt eine neue Spalte anzulegen. |
| *No table exists. Please create table before creating columns.* | Der Dokumenttyp hat noch keine Tabelle: Klicken Sie zuerst auf **Create new table**. |

[Structured Output für Tabellen](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
