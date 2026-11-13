# Symbolleiste & Arbeitsfläche

## Video: Builder und Canvas

Lernen Sie Thomas kennen und folgen Sie seiner Erklärung direkt in der deutschen DocBits-Oberfläche. Er prüft Workflow-Dashboard, Workflow-Liste und Lizenz und öffnet anschließend einen ungespeicherten Designerentwurf. Schritt für Schritt benennt er den Workflow, konfiguriert die Betragsprüfung und zwei Aktionen, ordnet die Karten an und verbindet beide Routen. Danach zeigt er die Testvorbereitung mit Dokumenten und eigenen Daten. Das Demokonto besitzt kein Advanced-Workflow-Abonnement und blockiert die Validierung; der Entwurf bleibt ungespeichert und inaktiv.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4" %}

[Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.vtt) · [Transkript (Text)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.txt) · 3:21

| In diesem Video | Start |
| --- | --- |
| Administrator kennenlernen | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=0) |
| Workflow-Zugang prüfen | [0:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=8) |
| Workflow benennen | [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=33) |
| Betragsprüfung einrichten | [0:46](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=46) |
| Aktion Approval hinzufügen | [1:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=68) |
| Aktion Standard hinzufügen | [1:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=88) |
| Karten anordnen | [1:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=109) |
| Routen verbinden | [2:02](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=122) |
| Testfälle vorbereiten | [2:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=147) |
| Validieren, speichern und aktivieren | [2:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/de.mp4#t=173) |

<details>
<summary>Transkript</summary>

**Administrator kennenlernen**

Ich kümmere mich hier um DocBits. Ich zeige euch, wie ich einen Rechnungsworkflow mit zwei Routen aufbaue.

**Workflow-Zugang prüfen**

Ich beginne im Workflow-Dashboard und öffne die Workflow-Liste. Dann prüfe ich die Lizenz. Workflow und Advanced Workflow benötigen beide einen aktiven Zugang. Mit diesen Freigaben bietet Neuer Workflow auch Advanced Workflow an. Dieses Dokumentationskonto hat keine aktive Workflow-Lizenz. Deshalb arbeite ich mit einer ungespeicherten Vorschau im Designer weiter.

**Workflow benennen**

Ich arbeite im echten DocBits-Designer. Zuerst gebe ich dem Entwurf einen klaren Namen. Wir prüfen einen Rechnungsbetrag und zeigen die beiden möglichen Routen mit einfachen Aktionen. Der Entwurf bleibt ungespeichert.

**Betragsprüfung einrichten**

Ich öffne das Menü zum Hinzufügen und wähle eine Bedingungskarte. Unter Dokumentenfeld wähle ich die Docfield-Bedingung. Als Feld trage ich total_amount ein. Dann wähle ich den Vergleich größer als. Und gebe eintausend ein. Verwendet euren eigenen Dokumentenfeldschlüssel. Genau eintausend erfüllt diesen Vergleich nicht.

**Aktion Approval hinzufügen**

Jetzt füge ich eine Aktionskarte aus der Kategorie Dokumentenfeld hinzu. Die Aktion setzt ein Dokumentenfeld. Ich verwende den Beispielschlüssel approval_route. Und trage den Wert Approval ein. Das kennzeichnet die Route. Ein echter Freigabeprozess benötigt die passenden Geschäftsaktionen.

**Aktion Standard hinzufügen**

Ich füge eine zweite Aktionskarte mit derselben Aktion hinzu. Die Aktion setzt ein Dokumentenfeld. Ich verwende den Beispielschlüssel approval_route. Diesmal erhält das Beispielfeld den Wert Standard. Beide Karten sind konfiguriert. Erst ihre Verbindungen bestimmen, welche Aktion ausgeführt wird.

**Karten anordnen**

Ich ziehe die Karten in eine übersichtliche Anordnung. Die beiden Aktionen kommen nach rechts. Die Bedingung steht in der Mitte, Start links. Verschieben ändert nur die Position. Es erstellt keine Verbindung.

**Routen verbinden**

Ich ziehe vom Ausgang von Start zum Eingang der Bedingung. Die Erfolgsroute führt über die blaue Verbindung zu Approval. Die orange Route für eine nicht erfüllte Bedingung führt zu Standard. Der rote Fehlerausgang ist ein eigener Ausgang für Auswertungsfehler. Hier bleibt er unverbunden. Legt für einen produktiven Workflow fest, wie solche Fehler behandelt werden.

**Testfälle vorbereiten**

Die Test-Schaltfläche in der Werkzeugleiste öffnet die Auswahl eines Testdokuments. Ich kann ein Beispieldokument auswählen oder vollständige benutzerdefinierte Daten vorbereiten. Testet Beträge über, unter und genau bei eintausend. Prüft auch einen fehlenden Betrag. Dieses Konto hat keine Advanced-Workflow-Lizenz. Ich zeige die Testvorbereitung, kein ausgeführtes Testergebnis.

**Validieren, speichern und aktivieren**

Mit Validieren prüft man Verbindungen und Karteneinstellungen. Hier blockiert die fehlende Lizenz die Validierung. Mit einem freigeschalteten Konto würde ich ausdrücklich auf dem Server speichern. Danach prüfe ich die Aktivierung getrennt. Vor dem ersten Speichern ist der Schalter deaktiviert. Der automatische Entwurfsstatus bezieht sich auf eine lokale Browserkopie. Er bedeutet nicht, dass der Workflow gespeichert oder aktiviert ist.

</details>

[Alle fünf Kapitel ansehen](../advanced-workflow-videos.md)

Die Symbolleiste des Advanced Workflow verläuft am unteren Rand der Arbeitsfläche und bietet Ihnen alles, was Sie zum Erstellen, Navigieren und Verwalten des Ablaufs benötigen.

## Steuerelemente der Symbolleiste

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4" %}

**Video:** Advanced Workflow Designer: Karten und Pfade · 2:19 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Einen neuen Workflow beginnen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=0.25)

Öffnen Sie das Workflow-Dashboard und wählen Sie Neuer Workflow.

**Advanced Workflow wählen** · [0:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=5.583)

Wählen Sie Advanced Workflow. Der Designer öffnet sich mit einem Start-Knoten, an dem jeder Workflow beginnt.

**Wenn, Und und Dann** · [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=13.483)

Fügen Sie Karten über das Menü Hinzufügen oder per Rechtsklick auf die Fläche hinzu. Die drei Kartenkategorien sind Wenn, Und und Dann.

**Wenn: die Auslösebedingung** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=25.916)

Die Wenn-Karte ist die Auslösebedingung. Sie entscheidet, wann der Workflow startet, zum Beispiel für einen bestimmten Dokumenttyp.

**Und: eine weitere Bedingung** · [0:39](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=39.383)

Und-Karten fügen weitere Bedingungen hinzu. Sie prüfen das Dokument, zum Beispiel seinen Status. Das Ergebnis ist Erfolg oder eine gescheiterte Bedingung.

**Dann: die Aktionskarte** · [0:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=52.816)

Dann-Karten sind die Aktionskarten. Sie ändern das Dokument, setzen zum Beispiel ein Feld oder genehmigen das Dokument.

**Ziehen zum Verbinden** · [1:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=61.116)

Um zwei Karten zu verbinden, ziehen Sie von einem Anschluss rechts an einer Karte zum Eingang links an der nächsten Karte.

**Blau: Erfolg** · [1:09](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=69.416)

Blau ist der Erfolgspfad. Jede Karte hat ihn. Der Workflow nimmt ihn, wenn die Karte fertig ist.

**Orange: gescheiterte Bedingung** · [1:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=76.35)

Orange ist der Pfad für eine gescheiterte Bedingung. Nur Und-Karten haben ihn. Der Workflow nimmt ihn, wenn die Bedingung nicht erfüllt ist.

**Rot: Fehler** · [1:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=85.85)

Rot ist der Fehlerpfad. Und- und Dann-Karten haben ihn. Der Workflow nimmt ihn, wenn eine Karte mit einem Fehler scheitert.

**Wenn-sonst mit Fehlerbehandlung** · [1:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=95.183)

Zusammen bilden diese Pfade ein Wenn-sonst mit Fehlerbehandlung. Erfolg führt eine Aktion aus, eine gescheiterte Bedingung eine andere, und ein Fehler einen Ausweg, zum Beispiel eine Aufgabe für eine Person.

**Ein Pfad pro Status** · [1:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=109.383)

Für mehrere Fälle verketten Sie Karten für den Dokumentstatus über ihre Pfade für gescheiterte Bedingungen. Jede Karte prüft einen Status, so bekommt jeder Status seinen eigenen Pfad.

**Der Pfad zu einer Karte und von ihr weg** · [2:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v1/de.mp4#t=121.75)

Klicken Sie auf eine Karte, um ihren Ausführungspfad hervorzuheben: die Karten, die ein Dokument bis zu ihr durchläuft, und die Karten, die folgen können. Alles andere wird abgeblendet. Hier wird die Aufgabe nur von der Wenn-Karte aus erreicht, über den roten Fehlerpfad der Statuskarte.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.mp4" %}

**Video:** Workflow-Beschreibungen und Notizen · 1:12 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Erklären Sie Ihren Workflow** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.mp4#t=0.25)

Ein Workflow mit mehreren Zweigen lässt sich leichter pflegen, wenn er sich selbst erklärt. Der Designer hat dafür zwei Werkzeuge: eine Beschreibung des ganzen Workflows und Notizen auf der Fläche.

**Den ganzen Workflow beschreiben** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.mp4#t=12.683)

Wählen Sie Beschreibung bearbeiten in der Werkzeugleiste und sagen Sie in ein, zwei Sätzen, wofür der Workflow da ist. Die Beschreibung wird beim Speichern des Workflows gespeichert.

**Eine Notiz hinzufügen** · [0:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.mp4#t=23.616)

Um einen einzelnen Schritt zu erklären, klicken Sie mit rechts auf die Fläche, öffnen das Menü zum Hinzufügen und wählen Notiz. Die Notiz erscheint dort, wo Sie geklickt haben.

**Doppelklick zum Schreiben** · [0:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.mp4#t=35.816)

Doppelklicken Sie auf die Notiz, um hineinzuschreiben, bis zu fünfhundert Zeichen. Klicken Sie daneben, wenn Sie fertig sind.

**Verschieben und vergrößern** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.mp4#t=45.383)

Ziehen Sie die Notiz neben die Karten, die sie erklärt, und ziehen Sie an ihrer unteren rechten Ecke, um sie zu vergrößern.

**Notizen einfärben** · [0:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.mp4#t=53.283)

Klicken Sie mit rechts auf eine Notiz, um ihre Farbe zu ändern. Farben helfen beim Gruppieren, zum Beispiel Blau für Erklärungen und Rot für offene Fragen.

**Notizen werden nie ausgeführt** · [1:03](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/de.mp4#t=63.25)

Notizen sind nur für Menschen. Sie sind mit keiner Karte verbunden und werden nie ausgeführt, also ändern sie nichts daran, was der Workflow tut.

</details>

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
