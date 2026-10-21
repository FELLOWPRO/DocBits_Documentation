---
description: "P0: Status wechseln und erneute Ausführung begrenzen"
---

# P0: Status wechseln und erneute Ausführung begrenzen

Mit **Change Status to** ändern Sie den Dokumentstatus. In Version 3 steuert `trigger_docflow`, ob eine weitere Workflow-Verarbeitung angefordert wird. Wählen Sie den Wert ausdrücklich. Bei fehlendem Parameter verwendet der Code `true`; die Ausführung der älteren Versionen 1/2 liest diesen Schalter nicht auf dieselbe Weise. Prüfen Sie die gespeicherte Kartenversion.

Beginnen Sie mit `validated_pending_approval` und `trigger_docflow=false`. Der Schlüssel ist eine technische Auswahl; ein frei erfundenes `pending_approval` ist kein Ersatz. Ein Advanced-Test simuliert den Statuswechsel. Er belegt weder die gespeicherte Änderung noch die Verarbeitung einer angeforderten Folgeausführung.

Ein begrenzter Geschäftsablauf prüft den Ausgangsstatus und ein fachliches Bearbeitungsmerkmal, führt die Aktion aus und wechselt in den Folgezustand. Bei erneutem Ereignis darf die ursprüngliche Bedingung nicht mehr gelten. Zwei gleichzeitig gestartete Läufe können ein solches Merkmal jedoch beide vorher lesen: Für Exporte und Aufgaben muss der Zielprozess doppelte Verarbeitung zusätzlich erkennen.

Für die Abnahme vergleichen Sie ersten und zweiten echten Lauf: Dokumentstatus, angeforderte Folgeausführung und Anzahl erzeugter Aufgaben oder Zielbelege. Wechseln Sie nicht allein zum Ausprobieren zwischen zwei Statuswerten hin und her. Eine unerfüllte Freigabebedingung wird durch einen Statuswechsel nicht zur erteilten Freigabe.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

### `staus_change` · v3

Identität: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | Folgeausführung angefordert ≠ abgeschlossen |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## Prüfstand und Aussagegrenzen

Die ausgewählten Karten- und Knotenergebnisse wurden mit synthetischen Daten in Advanced Test geprüft. Die Antworten liegen im Übungspaket. Dokumentaktionen sind simuliert; ein tatsächlicher Dokumentlauf und externe Zustellung sind damit nicht belegt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
