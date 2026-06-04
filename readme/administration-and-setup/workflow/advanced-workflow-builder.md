# Advanced Workflow

Der **Advanced Workflow**-Builder ist ein Node-Graph-Editor für Workflows, die Verzweigungen, parallele Pfade und Ablaufsteuerung benötigen — über das lineare When/And/Then des Standard-Builders hinaus. Sie ordnen Knoten auf einer Canvas an und verbinden sie, um den Ausführungsfluss zu definieren.

## Zugang

Öffnen Sie den Advanced-Workflow-Designer aus dem Workflow-Bereich (die Advanced-Builder-Canvas). Sie starten an einem **Start**-Knoten und bauen den Ablauf durch Hinzufügen weiterer Knoten auf.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Advanced-Workflow-Node-Graph-Canvas mit Toolbar"><figcaption><p>Die Advanced-Workflow-Canvas — ein Node-Graph mit Zoom, Ausführen, Raster und Speichern. Vergeben Sie in der Toolbar einen Namen für den Workflow.</p></figcaption></figure>

## Knoten hinzufügen

Klicken Sie auf **+ Add**, um das Knoten-Menü zu öffnen. Zusätzlich zu den bekannten **When**-, **And**- und **Then**-Karten bietet der Advanced-Builder Knoten zur Ablaufsteuerung:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Advanced-Workflow Add-Menü mit Knotentypen"><figcaption><p>Das <strong>+ Add</strong>-Knoten-Menü: When / And / Then sowie Wait ALL, Wait ANY, OR und Note.</p></figcaption></figure>

- **When / And / Then** — dieselben Bedingungs- und Aktionskarten wie im Standard-Builder.
- **Wait ALL** — wartet, bis *alle* eingehenden Zweige abgeschlossen sind, bevor es weitergeht.
- **Wait ANY** — fährt fort, sobald *irgendein* eingehender Zweig abgeschlossen ist.
- **OR** — verzweigt den Ablauf auf alternative Pfade.
- **Note** — eine freie Text-Anmerkung auf der Canvas (ohne Einfluss auf die Ausführung).

Führen Sie den Ablauf über die Play-Schaltfläche aus, validieren Sie ihn und speichern Sie ihn über die Speichern-Schaltfläche in der Toolbar.

## Nächste Schritte

- Was die einzelnen Karten tun, sehen Sie im Abschnitt **Karten**.
- Für einfache lineare Automatisierungen ist der **Standard Workflow**-Builder schneller eingerichtet.
