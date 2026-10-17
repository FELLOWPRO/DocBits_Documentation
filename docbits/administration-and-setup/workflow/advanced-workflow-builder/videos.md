---
description: "Watch five narrated chapters on Advanced Workflows and Workflow Logs in English and German, with caption files and transcripts."
---

# Video guide

Learn how to build, test and diagnose an Advanced Workflow. Each chapter is available with English or German narration and takes less than two minutes. Choose the language tab below each chapter.

The videos use labelled teaching diagrams. For application screenshots and complete control descriptions, use the [Advanced Workflows guide](README.md), [Toolbar & Canvas](toolbar-and-canvas.md), [Nodes](nodes.md), [Variables](variables.md) and [Validation & Testing](validation-and-testing.md).

Caption files are available in WebVTT format below each video. Open the expandable transcript to read the explanation without playing the video.

| Chapter | English | Deutsch |
| --- | --- | --- |
| [1. Builder and canvas](#builder-and-canvas) | 1:48 | 1:58 |
| [2. Nodes and routes](#nodes-and-routes) | 1:42 | 1:56 |
| [3. Variables, tests and activation](#variables-tests-and-activation) | 1:54 | 1:52 |
| [4. Find the relevant execution](#find-the-relevant-execution) | 1:52 | 1:59 |
| [5. Trace nodes and diagnose](#trace-nodes-and-diagnose) | 1:43 | 1:55 |

## Builder and canvas

Choose the builder, open the designer, add and configure cards, navigate and edit the graph, then finish the design.

{% tabs %}
{% tab title="English" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v1/en.vtt) · 1:48

<details>
<summary>Transcript (English)</summary>

Use an Advanced Workflow when a document needs different routes. Standard Workflows suit a linear sequence. In the advanced builder, connections define the route. The position of a card on the canvas does not define execution order.

Open Workflow Dashboard, then Workflow List. Select New Workflow and Advanced Workflow. The advanced module and the required subscription must be available. A Start node appears automatically. Add a When card for an event trigger.

Use Add or right-click the canvas. Choose When, And, or Then and select a card from its category. Configure the fields and the card version. A card version belongs to that card. It is different from the workflow type.

Drag the background to pan. Use zoom or the mouse wheel for detail. The mini-map helps you find distant nodes. Snap to grid aligns cards. Select a node to highlight its incoming and outgoing paths. Other paths become dim.

Select several nodes with Shift and drag. Copy, paste, duplicate, undo, and redo help you change a section. The context menu also offers actions for a selected node. Use Note to explain a decision. Notes never execute.

Enter a workflow name and a useful description. The toolbar also opens variables, help, validation, and testing. Export Image captures the diagram. This image is different from a workflow configuration export. The arrow hides or shows the toolbar.

</details>
{% endtab %}

{% tab title="Deutsch" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v1/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v1/de.vtt) · 1:58

<details>
<summary>Transkript (Deutsch)</summary>

Advanced Workflows führen Dokumente über unterschiedliche Wege. Standard Workflows bilden lineare Abläufe ab. Im erweiterten Editor bestimmen die Verbindungen die Reihenfolge. Die Position der Karten auf dem Canvas legt keine Reihenfolge fest.

Öffnen Sie das Workflow Dashboard und die Workflow Liste. Wählen Sie Neuer Workflow und Advanced Workflow. Das erweiterte Modul und die erforderliche Lizenz müssen verfügbar sein. Der Startknoten erscheint automatisch. Eine When Karte legt einen Ereignisauslöser fest.

Öffnen Sie Hinzufügen oder das Kontextmenü. Wählen Sie When, And oder Then und eine Karte aus ihrer Kategorie. Konfigurieren Sie Felder und Kartenversion. Diese Version gehört zur einzelnen Karte, unabhängig vom Workflow Typ.

Ziehen Sie den Hintergrund, um die Ansicht zu verschieben. Zoom und Mausrad zeigen Details. Die Minikarte hilft bei weit entfernten Knoten. Das Raster richtet Karten aus. Ein ausgewählter Knoten hebt seine eingehenden und ausgehenden Wege hervor. Andere Wege werden abgeblendet.

Wählen Sie mehrere Knoten mit Umschalt und Ziehen aus. Kopieren, Einfügen, Duplizieren, Rückgängig und Wiederholen erleichtern Änderungen. Das Kontextmenü bietet Knotenaktionen. Notizen erklären Entscheidungen, führen aber nichts aus.

Geben Sie Namen und Beschreibung ein. Die Werkzeugleiste öffnet Variablen, Hilfe, Validierung und Tests. Bild exportieren erzeugt ein Diagrammbild, keine Workflow Konfiguration. Der Pfeil blendet die Werkzeugleiste ein oder aus.

</details>
{% endtab %}

{% endtabs %}

## Nodes and routes

Understand node roles, connect success, false-condition and error outputs, build alternatives, use Wait ALL, Wait ANY and OR, and avoid invalid connections.

{% tabs %}
{% tab title="English" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v1/en.vtt) · 1:42

<details>
<summary>Transcript (English)</summary>

Start is the manual entry. When defines an event trigger. Neither accepts incoming connections. And checks a condition. Then performs an action. Both builders share the card catalog. Notes explain the design without executing.

Drag an output to the next input. Designer blue means success, orange means false condition, and red means error. And has three outcomes. Then has success and error. Execution views show success in green.

Check whether an invoice exceeds a threshold. Connect blue to approval, orange to normal processing, and red to error handling. A false condition can continue through its connected route. It does not stop every branch.

Wait ALL joins branches. Every source must have taken a route connected to the gate. Connect both required checks and the next action. An unselected route cannot provide a required result.

Wait ANY and OR join branches when at least one source took a connected route. OR requires two different source nodes. These gates neither create exclusive choices nor cancel other actions. Test the complete graph.

Keep processing nodes reachable from an entry. Avoid cycles and incoming connections to entry nodes. Include a Then action. Validate changed routes. Imported Delay nodes need a positive duration. The current Add menu does not offer Delay.

</details>
{% endtab %}

{% tab title="Deutsch" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v1/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v1/de.vtt) · 1:56

<details>
<summary>Transkript (Deutsch)</summary>

Start ist der manuelle Einstieg. When reagiert auf Ereignisse. Beide haben keinen Eingang. And prüft Bedingungen, Then führt Aktionen aus. Beide Editoren verwenden denselben Kartenkatalog.

Ziehen Sie einen Ausgang zum nächsten Eingang. Blau ist im Editor der Erfolgsweg. Orange bedeutet Bedingung falsch, Rot einen Ausführungsfehler. And hat drei Ergebnisse. Then hat Erfolg und Fehler. In Ergebnisansichten ist Erfolg grün.

Prüfen Sie, ob ein Rechnungsbetrag einen Grenzwert überschreitet. Verbinden Sie Blau mit einer Freigabeaufgabe, Orange mit normaler Verarbeitung und Rot mit einer Fehlerbehandlung. Eine falsche Bedingung folgt ihrem verbundenen Weg. Sie stoppt nicht alle Zweige.

Wait ALL führt Zweige zusammen. Jede Quelle muss einen zum Kontrollknoten verbundenen Weg genommen haben. Verbinden Sie beide Prüfungen und die nächste Aktion. Ein nicht gewählter Weg kann kein erforderliches Ergebnis liefern.

Wait ANY und OR führen Zweige zusammen. Mindestens eine Quelle muss einen verbundenen Weg genommen haben. OR benötigt zwei verschiedene Quellknoten. Diese Knoten erzeugen keine exklusive Auswahl und brechen andere Aktionen nicht ab.

Verarbeitungsknoten müssen von einem Einstieg erreichbar sein. Vermeiden Sie Schleifen und eingehende Verbindungen an Einstiegsknoten. Fügen Sie eine Then Aktion hinzu und validieren Sie. Importierte Delay Knoten brauchen eine positive Dauer. Das aktuelle Hinzufügen Menü bietet Delay nicht an.

</details>
{% endtab %}

{% endtabs %}

## Variables, tests and activation

Choose variable types and understand organization scope, validate the graph, select the test context, inspect results, save and check activation.

{% tabs %}
{% tab title="English" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v1/en.vtt) · 1:54

<details>
<summary>Transcript (English)</summary>

Open Variables with the braces icon. Choose Text, Number, Yes or No, or Document. Search finds variable names. A Document variable stores a reference set by a dedicated workflow action. This form does not accept document values.

Choose a unique name, type and initial value. Creating, editing and deleting variables persist immediately for the organization. Other workflows can share these values. Saving or discarding the canvas cannot undo variable changes.

Select Validate. Review errors and warnings above the canvas. Click a message to focus its node. Check actions, entry connections, handles, cycles and merges. Structural validation does not prove that runtime data is correct.

Toolbar play opens Select Test Document. Choose a document, Custom Data, or Test Without Document for independent cards. Start play runs directly. Tests use the current canvas, including unsaved edits, and simulate destructive actions.

Inspect node messages and durations. Green means success, orange false condition, red error, and gray skipped. Retest corrections. Use Test Manager for repeatable scenarios. Cover the successful route, alternatives, missing data and errors.

Auto-save keeps a local browser draft about every thirty seconds after changes. Save explicitly to the server. The activation toggle is unavailable before the first save. Check the enabled state in Workflow List before expecting automatic execution.

</details>
{% endtab %}

{% tab title="Deutsch" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v1/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v1/de.vtt) · 1:52

<details>
<summary>Transkript (Deutsch)</summary>

Öffnen Sie Variablen über die geschweiften Klammern. Wählen Sie Text, Number, Yes oder No oder Document. Die Suche findet Namen. Eine Workflow Aktion setzt die Dokumentreferenz. Das Formular nimmt keinen Dokumentwert an.

Wählen Sie eindeutigen Namen, Typ und Anfangswert. Anlegen, Bearbeiten und Löschen speichern sofort für die Organisation. Andere Workflows können die Werte teilen. Speichern oder Verwerfen des Canvas macht Variablenänderungen nicht rückgängig.

Wählen Sie Validieren. Ein Klick auf Fehler oder Warnungen zeigt den Knoten. Prüfen Sie Aktionen, Einstiegsverbindungen, Anschlüsse, Schleifen und Zusammenführungen. Strukturvalidierung beweist keine korrekten Laufzeitdaten.

Die Wiedergabetaste öffnet Select Test Document. Wählen Sie Dokument, Custom Data oder Test Without Document für unabhängige Karten. Start spielt direkt ab. Tests verwenden ungespeicherte Änderungen und simulieren destruktive Aktionen.

Prüfen Sie Ergebnisse, Meldungen und Dauer je Knoten. Grün bedeutet Erfolg, Orange eine nicht erfüllte Bedingung, Rot einen Fehler und Grau übersprungen. Testen Sie Korrekturen erneut. Speichern Sie Szenarien im Test Manager und prüfen Sie jeden Weg.

Auto-Save sichert Änderungen etwa alle dreißig Sekunden als lokalen Browserentwurf. Speichern Sie ausdrücklich auf dem Server. Der Aktivierungsschalter bleibt vor dem ersten Speichern gesperrt. Prüfen Sie den aktiven Zustand in der Workflow Liste.

</details>
{% endtab %}

{% endtabs %}

## Find the relevant execution

Open logs for a document, read counters and execution rows, filter results, check dates and pagination, and understand empty or special log states.

{% tabs %}
{% tab title="English" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/en.vtt) · 1:52

<details>
<summary>Transcript (English)</summary>

Open the document Dashboard. Select Workflow Logs in the document Actions menu. Workflow access must be enabled. These logs describe the selected document's executions. Designer tests and organization event or activity logs are separate.

Blue counts executions in the current results. Red counts errors, yellow failed conditions, and green successes. The counters describe executions, not unique workflow definitions or graph nodes. Filters can change these counts.

Each row shows workflow name, creation time, runtime in seconds and result. One workflow can run repeatedly for one document. Compare timestamps. Rounded runtime can display zero point zero zero seconds for a short execution.

Use Search to find a workflow. The tune icon opens Sort Direction, Sort By, Status, Start Date and End Date. Sort by name or creation time. Enter dates as year, month, day. Select Apply.

Use pagination for older results. Clear Filters reloads the list without filter selections. Clear Search separately. For empty results, check document, dates and status. An empty list does not prove execution failed.

A banner and blocked icon identify the document's execution limit. Investigate repeated triggers before changing limits. A DocOperator video download appears only when a recording exists. It is an execution recording, separate from tutorial videos.

</details>
{% endtab %}

{% tab title="Deutsch" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/de.vtt) · 1:59

<details>
<summary>Transkript (Deutsch)</summary>

Öffnen Sie das Dokumenten Dashboard. Wählen Sie Workflow Logs im Aktionsmenü des Dokuments. Workflow Zugriff muss aktiviert sein. Diese Protokolle zeigen Dokumentausführungen. Testergebnisse und Ereignisprotokolle der Organisation sind getrennt.

Blau zählt Ausführungen in der Ergebnismenge, Rot Fehler, Gelb nicht erfüllte Bedingungen und Grün Erfolge. Die Zähler beschreiben Ausführungen, keine eindeutigen Workflow Definitionen oder Diagrammknoten. Filter können die Zähler verändern.

Jede Zeile zeigt Workflow Namen, Erstellungszeit, Laufzeit in Sekunden und Ergebnis. Derselbe Workflow kann mehrfach erscheinen. Vergleichen Sie den Zeitstempel. Die Laufzeit ist gerundet. Ein kurzer Lauf kann null Komma null null Sekunden anzeigen.

Search sucht Workflows. Das Filtersymbol öffnet Sortierrichtung, Sortieren nach, Status, Startdatum und Enddatum. Sortieren Sie nach Name oder Zeit, aufsteigend oder absteigend. Daten verwenden Jahr, Monat, Tag. Anwenden lädt die Ergebnisse.

Die Seitenauswahl zeigt ältere Ergebnisse. Filter zurücksetzen lädt ohne Filterauswahl neu. Leeren Sie die Suche gesondert. Prüfen Sie bei leeren Ergebnissen Dokument, Datum und Status. Eine leere Liste beweist keinen Fehler.

Ein Hinweis und ein Sperrsymbol zeigen das Ausführungslimit des Dokuments. Prüfen Sie wiederholte Auslöser, bevor Sie Limits ändern. Ein DocOperator Videodownload erscheint nur bei vorhandener Ausführungsaufnahme. Er ist vom Erklärvideo getrennt.

</details>
{% endtab %}

{% endtabs %}

## Trace nodes and diagnose

Expand an advanced execution, select nodes, distinguish false conditions, errors and skipped nodes, inspect merge results, then correct, test and verify the workflow.

{% tabs %}
{% tab title="English" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.vtt) · 1:43

<details>
<summary>Transcript (English)</summary>

Expand the workflow row. An advanced execution shows its graph on the left and messages on the right. Standard workflows show a card sequence. Available execution data describes that run, which can differ from today's designer.

Pan or zoom, then click a node. Card Logs shows its messages. Control nodes, including Wait ALL and Wait ANY, can show node-level messages. Read the message with the selected node and execution timestamp.

Green means success, orange false condition, red error, and gray skipped. A skipped node was not executed. Check whether another branch was selected or a required merge input was missing before changing that node.

Follow the actual route from the entry. For a false amount check, inspect orange. For an error, read the message and inspect red. An error handler can succeed while the overall execution still reports the original error.

For Wait ALL, check every source and connected outcome. For ANY or OR, find a matching source. Two handles from one source are not independent approvals. An orange condition result can be intentional.

Record workflow name, document reference, timestamp, node and exact message. Correct configuration or data, then test a repeatable scenario. Save and check activation. Compare a new execution with the old run. Earlier logs still describe earlier behavior.

</details>
{% endtab %}

{% tab title="Deutsch" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/de.vtt) · 1:55

<details>
<summary>Transkript (Deutsch)</summary>

Öffnen Sie die Workflow Zeile. Advanced Ausführungen zeigen links das Diagramm, rechts die Meldungen. Standard Workflows zeigen ihre Kartenfolge. Vorhandene Ausführungsdaten beschreiben diesen Lauf. Er kann vom heutigen Editor abweichen.

Verschieben oder zoomen Sie das Diagramm und klicken Sie einen Knoten an. Card Logs zeigt seine Meldungen. Kontrollknoten wie Wait ALL und Wait ANY können eigene Meldungen haben. Lesen Sie Meldung, gewählten Knoten und Zeitstempel gemeinsam.

Grün bedeutet Erfolg, Orange Bedingung falsch, Rot Fehler und Grau übersprungen. Ein übersprungener Knoten wurde nicht ausgeführt. Prüfen Sie den gewählten Zweig und erforderliche Eingänge der Zusammenführung, bevor Sie diesen Knoten ändern.

Verfolgen Sie den tatsächlichen Weg vom Einstieg. Prüfen Sie bei falscher Betragsbedingung Orange, bei einem Fehler die Meldung und Rot. Eine Fehlerbehandlung kann erfolgreich sein, während der Gesamtlauf weiterhin den ursprünglichen Fehler meldet.

Prüfen Sie bei Wait ALL jede Quelle und ihr verbundenes Ergebnis. Suchen Sie bei ANY oder OR die Quelle mit passender Verbindung. Zwei Ausgänge derselben Quelle sind keine unabhängigen Freigaben. Eine falsche Bedingung kann beabsichtigt sein, wenn ihr orangefarbener Weg verbunden ist.

Notieren Sie Workflow Namen, Dokumentreferenz, Zeitstempel, Knoten und genaue Meldung. Korrigieren Sie Daten oder Konfiguration und testen Sie wiederholbar. Speichern Sie und prüfen Sie die Aktivierung. Vergleichen Sie einen neuen Lauf. Alte Protokolle beschreiben weiterhin das frühere Verhalten.

</details>
{% endtab %}

{% endtabs %}

Continue with the [Advanced Workflows guide](README.md) or [Workflow Logs](../workflow-logs.md).
