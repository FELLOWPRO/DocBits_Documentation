---
description: DocBits Workflow Engine
---

# Workflow

[Lernweg vom Einstieg zum Experten](workflow-learning-path.md)

## Lernweg vom Einstieg zum sicheren Betrieb

1. [Wann läuft mein Workflow?](workflow-execution-model.md)
2. [Advanced-Geschäftsfall: Rechnungsrouting](advanced-workflow-case-study.md)
3. [Workflow-Übungspaket](workflow-training-kit.md)
4. [Workflow-Fehler systematisch diagnostizieren](workflow-troubleshooting.md)
5. [Karten verstehen und zuverlässig konfigurieren](card-reference-standard.md)

Beginnen Sie mit dem Standard-Workflow-Tutorial und den vorhandenen Regressionstests. Die fünf Ergänzungen verbinden Ausführungsmodell, geprüfte Advanced-Routen, Übungsdaten, Diagnose und Kartenreferenz.

<figure><img src="../../.gitbook/assets/docbits_workflow_3.png" alt="Workflow Übersicht"><figcaption></figcaption></figure>

## DocBits Workflow Engine: Vereinfachung der Prozessautomatisierung

### Workflows verstehen und vorbereiten <a id="workflow-orientation"></a>

Die Anleitung zeigt das echte DocBits-Testkonto: acht Workflow-Ausführungen im Dashboard, zwei gespeicherte Workflows mit Reihenfolge 100/200 und drei bestandene Testszenarien. Außerdem erklärt sie Standard und Advanced Workflows, Lizenzen, Vorlagen und das Card SDK.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4" %}

[Mit Untertiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.html) · [Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.vtt) · [Transkript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.txt) · 3:11

<details>
<summary>Kapitel und Transkript</summary>

| Kapitel | Start |
| --- | --- |
| Den Administrator kennenlernen | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=0.000) |
| Organisation und Zugriff | [0:02](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=2.375) |
| Dashboard und Filter | [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=14.750) |
| Workflow-Liste | [0:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=49.583) |
| Ausführungsreihenfolge | [1:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=64.042) |
| Standard Workflow | [1:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=82.667) |
| Advanced Workflow | [1:36](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=96.083) |
| Lizenzen | [1:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=113.333) |
| Vorlagen | [2:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=131.042) |
| Test Manager | [2:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=144.250) |
| Card SDK | [2:39](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=159.875) |
| Vorbereitung prüfen | [2:55](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/de.mp4#t=175.042) |

**Den Administrator kennenlernen**

Ich kümmere mich hier um DocBits.

**Organisation und Zugriff**

Gut, ich prüfe zuerst oben die Organisation. Die Workflow-Einstellungen gelten für die ausgewählte Organisation. Für diese Anleitung verwende ich unser Dokumentations-Testkonto.

**Dashboard und Filter**

Das Workflow-Dashboard gibt mir den Überblick. Für diese Übersicht habe ich zwei Trainingsworkflows achtmal manuell mit einer Beispielrechnung ausgeführt. Hier stehen acht Gesamtläufe und sechs erfolgreiche Läufe. Bei zwei Läufen war die Betragsbedingung nicht erfüllt. Die Erfolgsquote zählt auch diese korrekt beendeten Prüfungen. Ich filtere nach Workflownamen und kontrolliere den Zeitraum. So ändern sich Kennzahlen und Diagramm. Rechts wechsle ich zwischen gespeicherten Workflows und Testszenarien. Test-Manager-Läufe zählen separat.

**Workflow-Liste**

In der Workflow-Liste verwalte ich einzelne Workflows. Ich prüfe Name, Typ, Ausführungsreihenfolge, Auslöser und verfügbare Aktionen. Über die Suche finde ich bestehende Workflows, bevor ich einen weiteren anlege.

**Ausführungsreihenfolge**

Die Ausführungsreihenfolge ist wichtig, wenn mehrere Workflows dasselbe Dokument bearbeiten. Ich prüfe, welcher zuerst laufen soll und welche Daten der nächste benötigt. Hier steht die Rechnungsprüfung auf hundert und die weitere Prüfung auf zweihundert. Kleinere Werte laufen zuerst.

**Standard Workflow**

Für eine lineare Regel verwende ich Standard Workflow. Wenn legt den Auslöser fest, Und ergänzt Bedingungen, Dann führt Aktionen aus. Die Kartenbibliothek enthält die verfügbaren Bausteine.

**Advanced Workflow**

Für alternative Wege verwende ich Advanced Workflow. Diese Designer-Vorschau zeigt Start und ausdrückliche Verbindungen. Erfolg, eine nicht erfüllte Bedingung und ein Fehler können unterschiedliche Wege nehmen. Die Kartenposition bestimmt keine Ausführungsreihenfolge.

**Lizenzen**

Unter Lizenz prüfe ich das grundlegende Workflow-Modul und Advanced Workflow getrennt. Hier sind beide inaktiv. Der Plandialog zeigt die verfügbaren Abonnements. Ich schließe diese Ansicht ohne Änderung. Eine Designer-Vorschau aktiviert die Workflow-Engine nicht.

**Vorlagen**

Vorlagen helfen mir, einen Ausgangspunkt wiederzuverwenden. Ich öffne die Vorlagenbibliothek und die Option für Standardvorlagen. Felder, Empfänger und Aktionen prüfe ich trotzdem für meinen eigenen Prozess.

**Test Manager**

Der Test Manager enthält gespeicherte Testszenarien für Standard und Advanced Workflows. Nach der Konfiguration ergänze ich passende Eingaben und erwartete Ergebnisse. Mit Alle Tests ausführen prüfe ich Änderungen gegen diese Szenarien.

**Card SDK**

Das Card SDK ist für eigene Erweiterungen gedacht. Entwickler können eine Vorlage verwenden, ein Paket hochladen oder aus GitHub importieren. Für die normale Administration beginne ich mit der vorhandenen Kartenbibliothek.

**Vorbereitung prüfen**

Vor dem Aufbau prüfe ich Organisation, Zugriff, benötigte Lizenz, Dokumentfelder und gewünschtes Ergebnis. Ich entscheide, ob eine lineare Regel genügt. Im nächsten Video erstellen wir einen Standard Workflow Schritt für Schritt.

</details>

### When <a id="when-trigger"></a>

When filtert den Dokumenttyp. Der tatsächliche Ausführungsanlass wird getrennt durch die Dokumentverarbeitung beziehungsweise einen ausdrücklichen Workflow-Aufruf bestimmt. Speichern allein startet keinen Dokumentlauf.

### And <a id="and-condition"></a>

And prüft Werte und Typen, etwa invoice_id und total_amount. Unterscheiden Sie nicht erfüllte Bedingung, fehlerhafte Eingabe und erfolgreiche Prüfung.

### Then <a id="then-action"></a>

Then führt die konfigurierte Aktion aus. Im Advanced-Test können Änderungen und Schnittstellen simuliert sein. Prüfen Sie gespeicherte Wirkung, Empfängereingang und Freigabe getrennt.

[Lernweg vom Einstieg zum Experten](workflow-learning-path.md)
