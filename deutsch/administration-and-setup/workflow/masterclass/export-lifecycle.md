---
description: "P1: Exportvarianten, offene Aufgaben und Abschlussstatus"
---

# P1: Exportvarianten, offene Aufgaben und Abschlussstatus

**Start Export** verwendet den eingerichteten Exportweg. **Export with Export Configuration** führt eine ausgewählte Konfiguration aus. Die verzögerte Variante merkt diese Konfiguration für den finalen Export am Ende des aktuellen Laufs vor. Vormerken heißt nicht „nach allen späteren Benutzerfreigaben automatisch senden“.

Die geprüften neuen Versionen bieten `status=finished` oder `status=exported`: finished schließt das Dokument, exported lässt die weitere Bearbeitung zu. Start Export trägt die Auswahl ab v4, konfigurierter und verzögerter Export ab v3. Ältere Versionen verwenden finished. Fehlt die Auswahl in den neuen Versionen, sieht der Code ebenfalls finished vor; ein ungültiger Wert ist ein Konfigurationsfehler.

Mit `ignore_pending_tasks=false` werden offene Aufgaben berücksichtigt. Beim unmittelbaren konfigurierten Export kann der Dienst den Export deshalb verweigern. Die Karte belegt keine automatische Wiederaufnahme nach späterer Erledigung. Klären Sie den erneuten Ausführungsanlass und prüfen Sie vor einem neuen Versand, ob bereits ein Zielbeleg existiert. Aktivieren Sie das Ignorieren nicht als Ersatz für die Freigabe.

Schließen Sie den Export erst an eine ausdrücklich geprüfte Freigabebedingung an. Die Abnahme umfasst offene Aufgabe, erledigte Aufgabe, fehlende Freigabe, erfolgreichen Testziel-Empfang und erneuten Lauf. Unterscheiden Sie Export angefordert, vom Empfänger erhalten und im ERP verarbeitet. Das Übungspaket enthält keine echten Exportziele; seine Testergebnisse belegen keine Zustellung.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

### `export` · v4

Identität: `757f30ca-ed60-4e04-8131-2779df17f019`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

Identität: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

Identität: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| EXPORT-01 | status=finished | geschlossen |
| EXPORT-02 | status=exported | weiter bearbeitbar |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | Verweigerung möglich; automatische Wiederaufnahme nicht belegt |
| EXPORT-04 | action_export_with_config_deferred | vorgemerkt ≠ empfangen |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## Prüfstand und Aussagegrenzen

Parameter und Verhalten wurden gegen den Dev-Katalog und den geprüften Quellstand abgeglichen. Die fachlichen Prüffälle sind eine Abnahmeanleitung. Persönliche Freigaben, reale Datenänderungen und Zustellungen wurden für dieses Kapitel nicht durchgeführt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
