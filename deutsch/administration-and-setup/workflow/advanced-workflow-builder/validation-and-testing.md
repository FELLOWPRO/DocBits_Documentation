# Validierung & Testen

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
