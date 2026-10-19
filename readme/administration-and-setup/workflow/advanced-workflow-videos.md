---
description: "Fünf Erklärvideos zu Advanced Workflows und Workflow Logs auf Deutsch, mit Untertiteldateien und Transkripten."
---

# Videoanleitung

Alle fünf Kapitel haben eine deutsche Tonspur, eine Untertiteldatei und ein Transkript. Das erste Kapitel zeigt die Erstellung des Beispielworkflows Schritt für Schritt; die weiteren Kapitel vertiefen die einzelnen Themen.

Die ersten drei Kapitel zeigen den echten DocBits-Designer mit Demonstrationsentwürfen. Die Testfassung zur Ausführungssuche zeigt echte Dokumentverarbeitung und Protokollfunktionen mit leeren Ergebnissen. Das Diagnosekapitel verwendet weiterhin gekennzeichnete Lehrgrafiken. Die [Advanced-Workflow-Anleitung](advanced-workflow-builder.md) und die [Workflow Logs](workflow-logs.md) ergänzen die Videos.
## Builder und Canvas

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

{% hint style="info" %}
Testfassung: Echte DocBits-Aufnahmen zeigen Dokumentaktionen, Dokumentenfluss, Schrittzeiten, leere Workflow Logs sowie Status- und Datumsfilter. Das Demodokument enthält keine gespeicherte Advanced-Workflow-Ausführung. Ausführungszeilen, Seitenauswahl und Knotendiagnose sind in dieser Vorschau noch nicht enthalten.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/de.mp4" %}

[Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/de.vtt) · 1:51

<details>
<summary>Transkript</summary>

**Beim Dokument beginnen**

Öffnen Sie im Dokumenten-Dashboard das Aktionsmenü und wählen Sie Dokumentenfluss. Die Verarbeitungshistorie zeigt Import und OCR. Öffnen Sie einen Schritt für Wartezeit und Verarbeitungszeit. Diese Schritte sind keine Advanced-Workflow-Knoten.

**Die echten Protokollzähler lesen**

Hier sehen Sie die Workflow Logs desselben Dokuments. Blau zählt alle Läufe, Rot Fehler, Gelb nicht erfüllte Bedingungen und Grün Erfolge. Für dieses Demodokument sind keine Workflow-Ausführungen gespeichert. Deshalb zeigen alle vier Zähler null.

**Die Ausführungsspalten prüfen**

Die Spalten zeigen Workflow-Name, Erstellungszeit, Laufzeit und Ergebnis. Unterscheiden Sie wiederholte Läufe am Zeitstempel. Dieses Demodokument enthält keine Ausführungszeile zum Öffnen.

**Die Statusfilter öffnen**

Das Filtersymbol öffnet das echte Filtermenü. Wählen Sie die Sortierung nach Name oder Erstellungszeit sowie aufsteigende oder absteigende Reihenfolge. Der Status bietet Erfolg, gescheiterte Bedingung und Fehler.

**Zeitraum wählen und Filter löschen**

Wählen Sie einen Zeitraum über Start, Ende oder den Kalender. Das Datumsformat ist Jahr, Monat und Tag. Anwenden lädt die Ergebnisse. Filter löschen setzt die Auswahl zurück. Leeren Sie die Suche gesondert. Die Monatsnamen im Kalender bleiben in dieser Version Englisch.

**Testfassung: Ein gespeicherter Lauf fehlt noch**

Mit dieser Testfassung prüfen Sie den Dokumentzugang, Verarbeitungsdetails und Protokollfunktionen. Für echte Ausführungszeilen, Seitenauswahl, Routen und Knotenmeldungen fehlt noch eine gespeicherte Advanced-Workflow-Ausführung. Diese Ergebnisse werden im Video nicht simuliert.

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
