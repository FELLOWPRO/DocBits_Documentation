---
description: "Fünf Erklärvideos zu Advanced Workflows und Workflow Logs auf Deutsch, mit Untertiteldateien und Transkripten."
---

# Videoanleitung

Alle fünf Kapitel enthalten eine deutsche Tonspur, eine Untertiteldatei und ein Transkript. Jedes Kapitel dauert weniger als zwei Minuten.

Die ersten drei Kapitel zeigen die echte DocBits-Oberfläche: einen konfigurierten Workflow, verbundene Steuerknoten, Variablenformulare und Testbedienelemente. Die beiden Kapitel zu Workflow Logs verwenden derzeit gekennzeichnete Lehrgrafiken. Die [Advanced-Workflow-Anleitung](advanced-workflow-builder.md) und die [Workflow Logs](workflow-logs.md) ergänzen die Videos.

## Builder und Canvas

Ein Rechnungsbetrag entscheidet zwischen zwei verbundenen Aktionen. Dieses Kapitel zeigt die echte DocBits-Oberfläche mit einem ungespeicherten Demonstrationsentwurf.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/de.mp4" %}

[Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/de.vtt)

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

## Knoten und Routen

Ein verbundener Demoentwurf zeigt Erfolgs-, Alternativ- und Fehlerwege im echten DocBits-Designer. Zwei Quellknoten führen anschließend zu Wait ALL, Wait ANY und OR. Die Beispielaktionen schreiben Demowerte, um die Routen zu kennzeichnen.


{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/de.mp4" %}

[Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/de.vtt)

<details>
<summary>Transkript</summary>

Start ist der manuelle Einstieg. When reagiert auf Ereignisse. Beide haben keinen Eingang. And prüft Bedingungen, Then führt Aktionen aus. Beide Editoren verwenden denselben Kartenkatalog.

Ziehen Sie einen Ausgang zum nächsten Eingang. Blau ist im Editor der Erfolgsweg. Orange bedeutet Bedingung falsch, Rot einen Ausführungsfehler. And hat drei Ergebnisse. Then hat Erfolg und Fehler. In Ergebnisansichten ist Erfolg grün.

Prüfen Sie, ob ein Rechnungsbetrag einen Grenzwert überschreitet. Verbinden Sie Blau mit einer Freigabeaufgabe, Orange mit normaler Verarbeitung und Rot mit einer Fehlerbehandlung. Eine falsche Bedingung folgt ihrem verbundenen Weg. Sie stoppt nicht alle Zweige.

Wait ALL führt Zweige zusammen. Jede Quelle muss einen zum Kontrollknoten verbundenen Weg genommen haben. Verbinden Sie beide Prüfungen und die nächste Aktion. Ein nicht gewählter Weg kann kein erforderliches Ergebnis liefern.

Wait ANY und OR führen Zweige zusammen. Mindestens eine Quelle muss einen verbundenen Weg genommen haben. OR benötigt zwei verschiedene Quellknoten. Diese Knoten erzeugen keine exklusive Auswahl und brechen andere Aktionen nicht ab.

Verarbeitungsknoten müssen von einem Einstieg erreichbar sein. Vermeiden Sie Schleifen und eingehende Verbindungen an Einstiegsknoten. Fügen Sie eine Then Aktion hinzu und validieren Sie. Importierte Delay Knoten brauchen eine positive Dauer. Das aktuelle Hinzufügen Menü bietet Delay nicht an.

</details>

## Variablen, Tests und Aktivierung

Folgen Sie dem verbundenen Rechnungsworkflow im echten DocBits-Designer. Öffnen Sie Variablen, vergleichen Sie die Typen und die Dokumentreferenz, finden Sie Validieren, bereiten Sie Tests mit Dokumenten oder eigenen Daten vor und sehen Sie Speichern und Aktivierung. Die Testszenen zeigen die Eingabekonfiguration; sie zeigen kein ausgeführtes Testergebnis.

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

## Die passende Ausführung finden

Die passende Ausführung über Workflow-Suche, Status, Datum und Sortierung finden.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/de.mp4" %}

[Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v1/de.vtt)

<details>
<summary>Transkript</summary>

Öffnen Sie das Dokumenten Dashboard. Wählen Sie Workflow Logs im Aktionsmenü des Dokuments. Workflow Zugriff muss aktiviert sein. Diese Protokolle zeigen Dokumentausführungen. Testergebnisse und Ereignisprotokolle der Organisation sind getrennt.

Blau zählt Ausführungen in der Ergebnismenge, Rot Fehler, Gelb nicht erfüllte Bedingungen und Grün Erfolge. Die Zähler beschreiben Ausführungen, keine eindeutigen Workflow Definitionen oder Diagrammknoten. Filter können die Zähler verändern.

Jede Zeile zeigt Workflow Namen, Erstellungszeit, Laufzeit in Sekunden und Ergebnis. Derselbe Workflow kann mehrfach erscheinen. Vergleichen Sie den Zeitstempel. Die Laufzeit ist gerundet. Ein kurzer Lauf kann null Komma null null Sekunden anzeigen.

Search sucht Workflows. Das Filtersymbol öffnet Sortierrichtung, Sortieren nach, Status, Startdatum und Enddatum. Sortieren Sie nach Name oder Zeit, aufsteigend oder absteigend. Daten verwenden Jahr, Monat, Tag. Anwenden lädt die Ergebnisse.

Die Seitenauswahl zeigt ältere Ergebnisse. Filter zurücksetzen lädt ohne Filterauswahl neu. Leeren Sie die Suche gesondert. Prüfen Sie bei leeren Ergebnissen Dokument, Datum und Status. Eine leere Liste beweist keinen Fehler.

Ein Hinweis und ein Sperrsymbol zeigen das Ausführungslimit des Dokuments. Prüfen Sie wiederholte Auslöser, bevor Sie Limits ändern. Ein DocOperator Videodownload erscheint nur bei vorhandener Ausführungsaufnahme. Er ist vom Erklärvideo getrennt.

</details>

## Knoten verfolgen und Fehler diagnostizieren

Ausführungsreihenfolge und Zustände prüfen, Knotenmeldungen lesen und die Ursache eines falschen oder fehlerhaften Ergebnisses eingrenzen.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/de.mp4" %}

[Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/de.vtt)

<details>
<summary>Transkript</summary>

Öffnen Sie die Workflow Zeile. Advanced Ausführungen zeigen links das Diagramm, rechts die Meldungen. Standard Workflows zeigen ihre Kartenfolge. Vorhandene Ausführungsdaten beschreiben diesen Lauf. Er kann vom heutigen Editor abweichen.

Verschieben oder zoomen Sie das Diagramm und klicken Sie einen Knoten an. Card Logs zeigt seine Meldungen. Kontrollknoten wie Wait ALL und Wait ANY können eigene Meldungen haben. Lesen Sie Meldung, gewählten Knoten und Zeitstempel gemeinsam.

Grün bedeutet Erfolg, Orange Bedingung falsch, Rot Fehler und Grau übersprungen. Ein übersprungener Knoten wurde nicht ausgeführt. Prüfen Sie den gewählten Zweig und erforderliche Eingänge der Zusammenführung, bevor Sie diesen Knoten ändern.

Verfolgen Sie den tatsächlichen Weg vom Einstieg. Prüfen Sie bei falscher Betragsbedingung Orange, bei einem Fehler die Meldung und Rot. Eine Fehlerbehandlung kann erfolgreich sein, während der Gesamtlauf weiterhin den ursprünglichen Fehler meldet.

Prüfen Sie bei Wait ALL jede Quelle und ihr verbundenes Ergebnis. Suchen Sie bei ANY oder OR die Quelle mit passender Verbindung. Zwei Ausgänge derselben Quelle sind keine unabhängigen Freigaben. Eine falsche Bedingung kann beabsichtigt sein, wenn ihr orangefarbener Weg verbunden ist.

Notieren Sie Workflow Namen, Dokumentreferenz, Zeitstempel, Knoten und genaue Meldung. Korrigieren Sie Daten oder Konfiguration und testen Sie wiederholbar. Speichern Sie und prüfen Sie die Aktivierung. Vergleichen Sie einen neuen Lauf. Alte Protokolle beschreiben weiterhin das frühere Verhalten.

</details>
