# Validierung & Test

Bevor Sie sich auf einen Advanced Workflow verlassen, verwenden Sie die Steuerelemente der Symbolleiste, um zu bestätigen, dass er korrekt ist und sich wie erwartet verhält.

## Validate

Klicken Sie auf das Steuerelement **Validate** (das Häkchen-Kreis-Symbol oder drücken Sie <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Die Validierung prüft den Graphen auf Probleme — nicht verbundene Knoten, fehlende Konfiguration und ungültige Verbindungen —, sodass Sie diese beheben können, bevor der Workflow auf echten Dokumenten ausgeführt wird.

## Test

Klicken Sie auf das Steuerelement **Test** (das Wiedergabe-Symbol oder drücken Sie <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>), um den Workflow gegen ein Beispiel auszuführen und sein Verhalten zu sehen, ohne Live-Dokumente zu beeinflussen.

## Testszenarien

Für wiederholbare Prüfungen speichern Sie **Testszenarien** im **Test Manager** (siehe [Dashboard](../workflow-dashboard.md)). Jedes Szenario hält ein erwartetes Ergebnis fest und zeigt ein Bestanden/Fehlgeschlagen-Resultat, und **Run All Tests** führt sie gemeinsam erneut aus — sodass Sie bestätigen können, dass sich Ihre Workflows nach einer Änderung weiterhin korrekt verhalten.

<figure><img src="../../../.gitbook/assets/workflow_test_manager.png" alt="Liste des Workflow Test Manager mit Testszenarien und Run All Tests"><figcaption><p>Der Test Manager — gespeicherte Szenarien mit Bestanden/Fehlgeschlagen-Resultaten und <strong>Run All Tests</strong>.</p></figcaption></figure>

## Nächste Schritte

- Sehen Sie sich die Knotentypen und Verbindungen unter [Knoten](nodes.md) an.
- Sehen Sie alle Steuerelemente von Symbolleiste und Arbeitsfläche unter [Symbolleiste & Arbeitsfläche](toolbar-and-canvas.md).
