# Validierung & Testen

## Video: Variablen, Tests und Aktivierung

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/de.vtt)

<details>
<summary>Transkript</summary>

Öffnen Sie Variablen über die geschweiften Klammern. Wählen Sie Text, Number, Yes oder No oder Document. Die Suche findet Namen. Eine Workflow Aktion setzt die Dokumentreferenz. Das Formular nimmt keinen Dokumentwert an.

Wählen Sie eindeutigen Namen, Typ und Anfangswert. Anlegen, Bearbeiten und Löschen speichern sofort für die Organisation. Andere Workflows können die Werte teilen. Speichern oder Verwerfen des Canvas macht Variablenänderungen nicht rückgängig.

Wählen Sie Validieren. Ein Klick auf Fehler oder Warnungen zeigt den Knoten. Prüfen Sie Aktionen, Einstiegsverbindungen, Anschlüsse, Schleifen und Zusammenführungen. Strukturvalidierung beweist keine korrekten Laufzeitdaten.

Die Wiedergabetaste öffnet Select Test Document. Wählen Sie Dokument, Custom Data oder Test Without Document für unabhängige Karten. Start spielt direkt ab. Tests verwenden ungespeicherte Änderungen und simulieren destruktive Aktionen.

Prüfen Sie Ergebnisse, Meldungen und Dauer je Knoten. Grün bedeutet Erfolg, Orange eine nicht erfüllte Bedingung, Rot einen Fehler und Grau übersprungen. Testen Sie Korrekturen erneut. Speichern Sie Szenarien im Test Manager und prüfen Sie jeden Weg.

Auto-Save sichert Änderungen etwa alle dreißig Sekunden als lokalen Browserentwurf. Speichern Sie ausdrücklich auf dem Server. Der Aktivierungsschalter bleibt vor dem ersten Speichern gesperrt. Prüfen Sie den aktiven Zustand in der Workflow Liste.

</details>

[Alle fünf Kapitel ansehen](../advanced-workflow-videos.md)

Während Sie einen Advanced Workflow erstellen, können Sie ihn mit zwei Steuerelementen in der Symbolleiste prüfen, ohne den Builder zu verlassen. Diese sind für *schnelle Prüfungen während des Erstellens* gedacht — für gespeicherte, wiederholbare Tests verwenden Sie den [Test Manager](../test-manager.md).

## Validate

Klicken Sie auf das Steuerelement **Validate** (das Häkchen-Kreis-Symbol oder drücken Sie <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Die Validierung prüft den Graphen auf Probleme — nicht verbundene Knoten, fehlende Konfiguration und ungültige Verbindungen — und weist Sie darauf hin, damit Sie sie beheben können, bevor der Workflow auf echten Dokumenten ausgeführt wird.

## Test

Klicken Sie auf das Steuerelement **Test** (das Abspielen-Symbol oder drücken Sie <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>), um den aktuellen Ablauf gegen ein Beispiel auszuführen und zu beobachten, wie er sich verhält, ohne Live-Dokumente zu beeinflussen. Dies ist der schnellste Weg, eine soeben auf der Arbeitsfläche vorgenommene Änderung zu überprüfen.

## Wann was verwenden

- **Validate / Test im Builder** (diese Seite) — sofortiges Feedback, während Sie den Ablauf entwerfen.
- **[Test Manager](../test-manager.md)** — speichern Sie das Szenario, damit Sie es später erneut ausführen können (und gemeinsam mit allen Ihren anderen Szenarien), um Regressionen nach künftigen Änderungen zu erkennen.

## Nächste Schritte

- Sehen Sie sich die Knotentypen und Verbindungen unter [Knoten](nodes.md) an.
- Alle Steuerelemente von Symbolleiste und Arbeitsfläche finden Sie unter [Symbolleiste & Arbeitsfläche](toolbar-and-canvas.md).
