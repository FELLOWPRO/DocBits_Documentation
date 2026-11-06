# Berichtsseite

Die **Berichtsseite** gibt einen Überblick darüber, wie Dokumente in einem bestimmten Zeitraum durch DocBits verarbeitet wurden: wie viele eingegangen sind, wie lange die Verarbeitung dauerte, welche Felder manuell korrigiert wurden und welchen Status die Dokumente schließlich erreichten. Sie richtet sich an Administratoren und Teamleiter, die die Eingangs- und Validierungsprozesse insgesamt betrachten möchten, nicht ein einzelnes Dokument.

{% embed url="https://www.youtube.com/watch?v=ar9jXYJo_AM" %}

## Berichtsseite aktivieren

Die Seite wird über einen Modulschalter aktiviert. Schalten Sie sie einmal für die Organisation ein:

1. Öffnen Sie **Einstellungen → Module** und wählen Sie die Gruppe **Dokumentenintegration** aus.
2. Aktivieren Sie in der Karte **Dokumenttyp** die Option **Bericht anzeigen**.
3. Anschließend wird den Benutzern der Organisation der Eintrag **Bericht** in der Seitenleiste angezeigt.

<figure><img src="../.gitbook/assets/report-show-report-setting-de.png" alt="Der Schalter Bericht anzeigen."><figcaption><p>Der Schalter Bericht anzeigen.</p></figcaption></figure>

## Berichtsseite öffnen

Wählen Sie das Diagrammsymbol in der Seitenleiste aus. Die Seite öffnet sich mit dem Zeitfilter, den Kennzahlen des Zeitraums und den Feldstatistiken.

<figure><img src="../.gitbook/assets/report-sidebar-icon-de.png" alt="Die DocBits-Seitenleiste mit hervorgehobenem Diagrammsymbol und dem Tooltip Bericht"><figcaption><p>Der Eintrag <strong>Bericht</strong> in der Seitenleiste.</p></figcaption></figure>

## Zeitraum auswählen

Der Filter **Zeiteinheit** oben auf der Seite legt den Zeitraum für alle Kennzahlen und Bereiche darunter fest. Zur Auswahl stehen **Letzte 7 Tage**, **Letzte 30 Tage** und **Zeitbereich wählen**. Über die letzte Option öffnen Sie einen Kalender, in dem Sie ein Start- und ein Enddatum auswählen.

<figure><img src="../.gitbook/assets/dbdc-19-report-time-options-native-20261103-de.png" alt="Optionen der Zeiteinheit: Letzte 7 Tage, Letzte 30 Tage und Zeitbereich wählen. Kopfzeile und Navigation der Anwendung sind nicht im Bild enthalten."><figcaption><p>Optionen der Zeiteinheit: Letzte 7 Tage, Letzte 30 Tage und Zeitbereich wählen. Kopfzeile und Navigation der Anwendung sind nicht im Bild enthalten.</p></figcaption></figure>

## Die Kennzahlen neben dem Filter

<figure><img src="../.gitbook/assets/report-time-unit-filter-de.png" alt="Die obere Zeile der Berichtsseite: Zeiteinheit, die Karte Neue Dokumente, die Karte Durchschnittliche Systemzeit und die Download-Schaltfläche"><figcaption><p><strong>Zeiteinheit</strong>, <strong>Neue Dokumente</strong>, <strong>Durchschnittliche Systemzeit</strong> und die Download-Schaltfläche.</p></figcaption></figure>

- **Neue Dokumente** zeigt, wie viele Dokumente im ausgewählten Zeitraum importiert wurden.
- **Durchschnittliche Systemzeit** gibt die durchschnittliche Zeit in Sekunden an, die DocBits in diesem Zeitraum für die Verarbeitung eines Dokuments benötigt hat.
- Mit der Download-Schaltfläche rechts in der Zeile exportieren Sie den Bericht für den ausgewählten Zeitraum als Excel-Datei (XLSX).

## Geänderte Felder

Das Diagramm **Geänderte Felder** zählt, wie häufig jedes Feld im ausgewählten Zeitraum manuell korrigiert wurde. Für jedes Feld wird ein Balken angezeigt, sodass Sie die am häufigsten bearbeiteten Felder Ihres Teams leicht erkennen. Das Fragezeichen neben der Überschrift erklärt, welche Änderungen das Diagramm zählt. Wurden im ausgewählten Zeitraum keine manuellen Korrekturen vorgenommen, erscheint statt der Balken die Meldung **Keine Dateneinträge im entsprechenden Zeitrahmen gefunden.**

<figure><img src="../.gitbook/assets/report-changed-fields-de.png" alt="Der Bereich Geänderte Felder zeigt keine Balken, sondern die Meldung „Keine Dateneinträge im entsprechenden Zeitrahmen gefunden.“; oben rechts befindet sich das Diagrammmenü."><figcaption><p>Wie häufig jedes Feld manuell geändert wurde.</p></figcaption></figure>

Über das Menü oben rechts im Diagramm laden Sie das Diagramm selbst im Format **SVG**, **PNG** oder **CSV** herunter.

## Weitere Berichtsbereiche

Unter dem Diagramm befinden sich vier Karten. Sie sind standardmäßig eingeklappt. Wählen Sie eine Überschrift aus, um die Tabelle zu öffnen, und wählen Sie sie erneut aus, um sie zu schließen.

1. **Gesamtzahl der Dokumente pro Typ** listet jeden Dokumenttyp mit den Spalten **Typ** und **Anzahl** auf. Bei Typen mit Unterdokumenttypen können Sie die Anzahl über **+** aufschlüsseln.
2. **Tagesdurchschnitt pro Doctype** zeigt dieselbe Liste als täglichen Durchschnitt pro Dokumenttyp.
3. **Status-Statistik** schlüsselt die Dokumente nach Verarbeitungsstatus auf; die Tabelle enthält die Spalten **Typ**, **Status** und **Anzahl**.
4. **Statistik exportieren** listet zunächst die Organisationen Ihres Kontos auf. Klappen Sie eine Organisation auf, um die verwendeten Exportformate anzuzeigen. Die Tabelle enthält die Spalten **Benutzer**, **Typ** und **Exportiert**.

<figure><img src="../.gitbook/assets/report-total-documents-per-type-de.png" alt="Die aufgeklappte Karte Gesamtzahl der Dokumente pro Typ mit den Spalten Typ und Anzahl"><figcaption><p><strong>Gesamtzahl der Dokumente pro Typ</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/report-daily-average-per-doctype-de.png" alt="Die aufgeklappte Karte Tagesdurchschnitt pro Doctype mit den Spalten Typ und Anzahl"><figcaption><p><strong>Tagesdurchschnitt pro Doctype</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/report-status-statistic-de.png" alt="Die aufgeklappte Karte Status-Statistik mit den Spalten Typ, Status und Anzahl"><figcaption><p><strong>Status-Statistik</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/dbdc-19-report-export-stats-native-20261103-de.png" alt="Die Karte Statistik exportieren mit einem aufgeklappten Bereich für eine bestehende Organisation. Organisationsnamen und Zeilenwerte sind unkenntlich gemacht; das Bild zeigt vorhandene Statistiken."><figcaption><p>Die Karte Statistik exportieren mit einem aufgeklappten Bereich für eine bestehende Organisation. Organisationsnamen und Zeilenwerte sind unkenntlich gemacht; das Bild zeigt vorhandene Statistiken.</p></figcaption></figure>
