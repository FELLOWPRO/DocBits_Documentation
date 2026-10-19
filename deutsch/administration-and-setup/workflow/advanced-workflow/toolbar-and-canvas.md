# Symbolleiste & Arbeitsfläche

## Video: Builder und Canvas

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/de.vtt)

<details>
<summary>Transkript</summary>

**Eine Rechnung mit zwei Routen**

Hier sehen Sie einen echten Advanced Workflow in DocBits. Eine Prüfung des Rechnungsbetrags führt zu zwei Aktionen. Die Verbindungen bestimmen, welche Aktion ausgeführt wird. Das Beispiel verwendet einen ungespeicherten Entwurf und Demonstrationsfelder.

**Betragsprüfung konfigurieren**

Öffnen Sie Hinzufügen, wählen Sie And und eine Bedingung für ein Dokumentfeld. Legen Sie das Betragsfeld fest, wählen Sie Größer als und geben Sie tausend ein. Verwenden Sie den genauen Feldschlüssel Ihrer Dokumentkonfiguration.

**Aktionen konfigurieren**

Fügen Sie zwei Then-Karten hinzu. Beide setzen das Demonstrationsfeld approval route. Eine schreibt Approval, die andere Standard. Die Werte kennzeichnen die Route. Für einen produktiven Workflow konfigurieren Sie hier Ihre fachlichen Aktionen.

**Ergebnisausgänge verbinden**

Verbinden Sie Start mit dem Eingang der Bedingung. Verbinden Sie den blauen Erfolgsausgang mit Approval und den orangefarbenen Ausgang für eine falsche Bedingung mit Standard. Der rote Fehlerausgang behandelt Auswertungsfehler separat. Die Kartenposition allein erzeugt keine Route.

**Testfälle vorbereiten**

Öffnen Sie Testen in der Werkzeugleiste. Wählen Sie ein Testdokument oder geben Sie vollständige Dokumentdaten als JSON ein. Prüfen Sie Beträge über, unter und genau bei tausend sowie fehlende Werte. Kontrollieren Sie nach der Ausführung die Knotenergebnisse.

**Validieren, speichern und aktivieren**

Validieren Sie Verbindungen und Karteneinstellungen. Speichern Sie explizit auf dem Server und prüfen Sie die Aktivierung separat. Automatische Browserentwürfe ersetzen das Speichern nicht. Ausführung und Logzugriff erfordern das passende Modul und Abonnement.

</details>

[Alle fünf Kapitel ansehen](../advanced-workflow-videos.md)

Die Symbolleiste des Advanced Workflow verläuft am unteren Rand der Arbeitsfläche und bietet Ihnen alles, was Sie zum Erstellen, Navigieren und Verwalten des Ablaufs benötigen.

## Steuerelemente der Symbolleiste

- **+ Add** — öffnet das Knotenmenü zum Hinzufügen eines Knotens (siehe [Knoten](nodes.md)).
- **Undo / Redo** — schrittweise rückwärts oder vorwärts durch Ihre Änderungen.
- **Zoom in / Zoom out** — ändert die Zoomstufe der Arbeitsfläche.
- **Workflow name** — benennt den Workflow direkt vor Ort.
- **Edit description** — fügt eine Beschreibung für den Workflow hinzu.
- **Variables** — öffnet das Panel [Variablen](variables.md).
- **Help** — öffnet den Dialog mit Tastenkürzeln und Hilfe.
- **Validate / Test** — prüft und startet den Ablauf (siehe [Validierung & Test](validation-and-testing.md)).
- **Snap to grid** — schaltet das Einrasten von Knoten am Raster für aufgeräumte Layouts um.
- **Mini-map** — schaltet eine kleine Übersichtskarte zum Navigieren großer Graphen um.
- **Save** — speichert den Workflow. Eine **auto-save**-Anzeige zeigt, wann der Ablauf zuletzt automatisch gespeichert wurde.

## Tastenkürzel

Drücken Sie jederzeit <kbd>?</kbd> auf der Arbeitsfläche, um den Dialog mit Tastenkürzeln und Hilfe zu öffnen.

<figure><img src="../../../.gitbook/assets/workflow_advanced_shortcuts.png" alt="Dialog mit Tastenkürzeln und Hilfe"><figcaption><p>Der Dialog mit Tastenkürzeln und Hilfe — Tastenkürzel, Hervorhebung des Ausführungspfads und Verbindungsfarben.</p></figcaption></figure>

| Tastenkürzel | Aktion |
|---|---|
| <kbd>Cmd/Ctrl</kbd> + <kbd>S</kbd> | Workflow speichern |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Workflow validieren |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | Workflow testen |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Z</kbd> / <kbd>Shift</kbd> + <kbd>Z</kbd> | Rückgängig / Wiederholen |
| <kbd>Cmd/Ctrl</kbd> + <kbd>C</kbd> / <kbd>V</kbd> / <kbd>D</kbd> | Ausgewählte Knoten kopieren / einfügen / duplizieren |
| <kbd>Cmd/Ctrl</kbd> + <kbd>A</kbd> | Alle Knoten auswählen |
| <kbd>Shift</kbd> + Ziehen | Knoten auswählen (Ziehen) |
| <kbd>Cmd/Ctrl</kbd> + Linksklick | Knoten zur Auswahl hinzufügen/entfernen |
| Rechtsklick | Menü zum Hinzufügen von Knoten |
| <kbd>Del</kbd> | Ausgewählten Knoten löschen |
| <kbd>?</kbd> | Diese Hilfe anzeigen |

## Nächste Schritte

- Erstellen Sie den Ablauf mit [Knoten](nodes.md) und [Variablen](variables.md).
