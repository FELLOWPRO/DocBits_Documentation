# Debug Collector

Der Debug Collector erstellt eine vollständige Momentaufnahme Ihrer DocBits-Sitzung — Netzwerkaktivität, Fehler, Browser-Umgebung und Leistungswerte — verpackt sie als JSON-Bericht und kann auf Wunsch direkt aus demselben Dialog ein Support-Ticket erstellen.

## Aufrufen

Drücken Sie <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> unter Windows und Linux oder <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> unter macOS. Der Performance-Report-Dialog öffnet sich sofort.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Debug-Collector-Dialog"><figcaption><p>Der Performance-Report-Dialog zeigt die erfasste Momentaufnahme und ein eingebautes Formular zur Ticket-Erstellung.</p></figcaption></figure>

## Was erfasst wird

* **API-Aufrufe** — die letzten 60 REST- und WebSocket-Aufrufe mit Zeitmessung, Statuscodes und Ziel-URLs. Aufrufe, die länger als zwei Sekunden dauern, werden gesondert markiert.
* **Fehler** — aktuelle JavaScript-Fehler und nicht abgefangene Promise-Rejections aus der Browser-Konsole.
* **Konsolen-Logs** — die zuletzt vom Programm geschriebenen Log-Meldungen.
* **Umgebung** — Browser-Version, Betriebssystem, Bildschirmgröße und aktive Feature-Flags.
* **Benutzerkontext** — Ihre Rolle, Organisation und die Seite, auf der Sie sich befanden, als die Momentaufnahme erstellt wurde.
* **Leistungswerte** — Ladezeiten der Seite (LCP, FCP), Speicherverbrauch und DOM-Größe.
* **Trace-IDs** — Korrelations-IDs, die die Momentaufnahme mit den Backend-Logs verbinden.

## Support-Ticket direkt aus dem Dialog erstellen

Sie müssen nichts manuell herunterladen oder anhängen — der Dialog enthält ein integriertes Formular **Support-Ticket erstellen**.

1. Tragen Sie Ihre E-Mail-Adresse ein, übernehmen Sie den vorgeschlagenen Betreff oder ersetzen Sie ihn, wählen Sie eine Priorität und ergänzen Sie kurze Notizen dazu, was Sie gemacht haben, als das Problem auftrat.
2. Klicken Sie auf **Send Report**. Die JSON-Momentaufnahme wird angehängt und das Ticket in einem Schritt erstellt.

Das war es — der Support erhält das Ticket mit allen Daten, die zur Reproduktion nötig sind.

Wenn Sie eine lokale Kopie der Momentaufnahme möchten, verwenden Sie **Copy Debug Data**, um die JSON-Daten in die Zwischenablage zu kopieren, oder die Funktion "Speichern unter" Ihres Browsers, um den Bericht als `.json`-Datei zu sichern.

## Datenschutz und Datenhandhabung

* Authentifizierungstoken und sensible Header werden bereits beim Erstellen der Momentaufnahme aus den erfassten API-Aufrufen entfernt.
* Es verlässt nichts den Browser, bevor Sie auf **Send Report** klicken — die Tastenkombination öffnet nur den Dialog.

<mark>Prüfen Sie die Momentaufnahme vor dem Senden, falls Sie mit Dokumenten gearbeitet haben, die Kundendaten enthalten. Dokument-IDs, die in URLs sichtbar sind, erscheinen auch im Bericht.</mark>
