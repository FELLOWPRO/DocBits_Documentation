# Validierung & Testen

## Video: Variablen, Tests und Aktivierung

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/de.mp4" %}

[Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/de.vtt)

<details>
<summary>Transkript</summary>

Öffnen Sie Variablen über die geschweiften Klammern. Wählen Sie Text, Number, Yes oder No oder Document. Die Suche findet Namen. Eine Workflow Aktion setzt die Dokumentreferenz. Das Formular nimmt keinen Dokumentwert an.

Wählen Sie eindeutigen Namen, Typ und Anfangswert. Anlegen, Bearbeiten und Löschen speichern sofort für die Organisation. Andere Workflows können die Werte teilen. Speichern oder Verwerfen des Canvas macht Variablenänderungen nicht rückgängig.

Wählen Sie Validieren. Ein Klick auf Fehler oder Warnungen zeigt den Knoten. Prüfen Sie Aktionen, Einstiegsverbindungen, Anschlüsse, Schleifen und Zusammenführungen. Strukturvalidierung beweist keine korrekten Laufzeitdaten.

Die Wiedergabetaste öffnet Select Test Document. Wählen Sie Dokument, Custom Data oder Test Without Document für unabhängige Karten. Start spielt direkt ab. Tests verwenden ungespeicherte Änderungen und simulieren destruktive Aktionen.

Bereite getrennte Tests über, unter und genau bei eintausend sowie mit fehlenden Daten vor. Prüfe nach dem Lauf Meldungen und Laufzeiten: Grün bedeutet Erfolg, Orange falsch, Rot Fehler und Grau übersprungen. Teste Korrekturen erneut. Der Testmanager verwaltet wiederholbare Szenarien.

Auto-Save sichert Änderungen etwa alle dreißig Sekunden als lokalen Browserentwurf. Speichern Sie ausdrücklich auf dem Server. Der Aktivierungsschalter bleibt vor dem ersten Speichern gesperrt. Prüfen Sie den aktiven Zustand in der Workflow Liste.

</details>

[Alle fünf Kapitel ansehen](../advanced-workflow-videos.md)

Während Sie einen Advanced Workflow erstellen, können Sie ihn mit zwei Steuerelementen in der Symbolleiste prüfen, ohne den Builder zu verlassen. Diese sind für *schnelle Prüfungen während des Erstellens* gedacht — für gespeicherte, wiederholbare Tests verwenden Sie den [Test Manager](../test-manager.md).

## Validate

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/de.mp4" %}

**Video:** Einen Workflow validieren · 0:52 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Validieren prüft den Aufbau** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/de.mp4#t=0.25)

Klicken Sie vor dem Speichern in der Werkzeugleiste auf Validieren. Es prüft, wie der Workflow gebaut ist: ob eine Wenn-Karte ihn startet, ob jede Karte verbunden ist und ob die Pfade Sinn ergeben. Probleme stehen über der Fläche.

**Meldung anklicken, Karte finden** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/de.mp4#t=16.116)

Klicken Sie auf eine Meldung, um zur betroffenen Karte zu springen. Hier ist die Zuweisungskarte nicht verbunden, sie würde also nie laufen. Verbinden Sie sie.

**Keine Meldungen: gültig** · [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/de.mp4#t=27.683)

Validieren Sie erneut. Wenn nichts mehr übrig ist, ist der Workflow gültig und Sie können ihn speichern.

**Erst validieren, dann testen** · [0:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/de.mp4#t=35.183)

Speichern macht dieselben Prüfungen, speichert den Workflow aber auch, wenn Probleme übrig sind, also validieren Sie zuerst. Validieren prüft weder Ihre Daten noch die Einstellungen in den Karten. Um zu sehen, was ein Workflow mit einem echten Dokument macht, testen Sie ihn.

</details>

Klicken Sie auf das Steuerelement **Validate** (das Häkchen-Kreis-Symbol oder drücken Sie <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Die Validierung prüft den Graphen auf Probleme — nicht verbundene Knoten, fehlende Konfiguration und ungültige Verbindungen — und weist Sie darauf hin, damit Sie sie beheben können, bevor der Workflow auf echten Dokumenten ausgeführt wird.

## Test

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4" %}

**Video:** Einen Workflow testen · 1:45 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Testen vor dem Einschalten** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4#t=0.25)

Testen Sie einen Workflow, bevor Sie ihn einschalten. Ein Test führt aus, was gerade auf der Fläche steht, auch ungespeicherte Änderungen. Aktionen wie Zuweisen oder Exportieren werden nur simuliert, das Dokument bleibt also, wie es ist.

**Den ganzen Workflow testen** · [0:15](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4#t=15.816)

Hier ist ein Workflow, der noch nicht gespeichert ist. Um den ganzen Workflow zu testen, klicken Sie in der Werkzeugleiste auf Workflow testen.

**Ein Testdokument wählen** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4#t=25.216)

Wählen Sie das Dokument für den Test. Workflows, die kein Dokument brauchen, lassen sich auch ohne testen. Suchen Sie das Dokument nach Namen, wählen Sie es aus und klicken Sie auf Test.

**Das Ergebnis auf der Fläche** · [0:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4#t=38.016)

Der Test folgt dem Pfad des Dokuments. Diese Rechnung wartet nicht auf Genehmigung, also endet die Und-Karte mit einer gescheiterten Bedingung, und der orange Pfad führt zur Zuweisungskarte. Nicht genommene Pfade sind ausgegraut, und das Banner oben zeigt das Ergebnis und die Testdauer.

**Details zu jeder Karte** · [0:55](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4#t=55.916)

Klicken Sie auf Details, um jede Karte mit Ergebnis und Meldung zu sehen. Erneuter Test führt den Test nach einer Änderung noch einmal aus.

**Eine einzelne Karte testen** · [1:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4#t=65.65)

Um eine einzelne Karte zu testen, fahren Sie darüber und klicken auf den Abspielknopf. Sie können auch mit rechts auf die Karte klicken und Test von diesem Knoten wählen. Der Test beginnt bei dieser Karte, mit derselben Dokumentauswahl.

**Abzeichen zeigt Details** · [1:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4#t=79.95)

Nur diese Karte und die Karten danach laufen. Fahren Sie über das Abzeichen, um das Ergebnis der Karte zu sehen. Ändern Sie die Karte und testen Sie erneut, bis sie tut, was Sie erwarten.

**Was die Farben bedeuten** · [1:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/de.mp4#t=92.483)

Kurz gesagt: Grün bedeutet Erfolg, Orange eine gescheiterte Bedingung und Rot einen Fehler. Karten, die nicht liefen, sind blass und bekommen ein graues Abzeichen.

</details>

Klicken Sie auf das Steuerelement **Test** (das Abspielen-Symbol oder drücken Sie <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>), um den aktuellen Ablauf gegen ein Beispiel auszuführen und zu beobachten, wie er sich verhält, ohne Live-Dokumente zu beeinflussen. Dies ist der schnellste Weg, eine soeben auf der Arbeitsfläche vorgenommene Änderung zu überprüfen.

## Wann was verwenden

- **Validate / Test im Builder** (diese Seite) — sofortiges Feedback, während Sie den Ablauf entwerfen.
- **[Test Manager](../test-manager.md)** — speichern Sie das Szenario, damit Sie es später erneut ausführen können (und gemeinsam mit allen Ihren anderen Szenarien), um Regressionen nach künftigen Änderungen zu erkennen.

## Nächste Schritte

- Sehen Sie sich die Knotentypen und Verbindungen unter [Knoten](nodes.md) an.
- Alle Steuerelemente von Symbolleiste und Arbeitsfläche finden Sie unter [Symbolleiste & Arbeitsfläche](toolbar-and-canvas.md).
