# Advanced Workflow

Der **Advanced Workflow**-Builder ist ein Node-Graph-Editor für Workflows, die Verzweigungen, parallele Pfade und Ablaufsteuerung benötigen — über das lineare When/And/Then des Standard-Builders hinaus. Sie ordnen Knoten auf einer Canvas an und verbinden sie, um den Ausführungsfluss zu definieren.

## Video: Rechnungsrouting direkt in DocBits

Das Video zeigt einen konfigurierten Workflow in der echten DocBits-Oberfläche: Betragsprüfung, zwei Aktionen, Verbindungen und die Vorbereitung der Testfälle.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/de.vtt)

Die Aufnahmen zeigen einen ungespeicherten Demonstrationsentwurf. `total_amount` und `approval_route` sind beispielhafte Feldschlüssel. `Approval` und `Standard` kennzeichnen die Routen. Konfigurieren Sie für Ihren Prozess die tatsächlichen fachlichen Aktionen.

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

[Weiter zur fünfteiligen Videoanleitung auf Deutsch](advanced-workflow-videos.md): Knoten, Variablen, Tests und Workflow Logs.

## Nächste Schritte

- Was die einzelnen Karten tun, sehen Sie im Abschnitt **Karten**.
- Für einfache lineare Automatisierungen ist der **Standard Workflow**-Builder schneller eingerichtet.
