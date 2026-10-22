---
description: "P0: Run Workflow, Zielbedingungen und Fehler verstehen"
---

# P0: Run Workflow, Zielbedingungen und Fehler verstehen

**Run Workflow** ruft einen Workflow über seine ID auf und wartet auf dessen Ausführung. Ein Name genügt nicht. Der Designer verwaltet die versteckte ID des aufrufenden Workflows; ändern Sie sie nicht als Geschäftsparameter. Das aktuelle Dokument wird an das Ziel übergeben. Dessen Einstieg und Bedingungen werden erneut ausgewertet.

Der geprüfte ausdrückliche Aufruf erreicht auch einen **inaktiven** Zielworkflow. Inaktiv bedeutet deshalb nicht „durch Run Workflow unaufrufbar“. Im Dev-Test wurden ein inaktives eigenes Ziel, ein Selbstaufruf und eine unbekannte Ziel-ID geprüft. Selbstaufruf und unbekannte ID nahmen den Fehlerweg. Die eingebaute Rekursions- und Kettenbegrenzung ersetzt keine fachliche Begrenzung mehrfacher Aufrufe.

Organisationsvariablen und Dokumentfelder sind von laufbezogenen Rückgaben zu unterscheiden. Der Aufruf überträgt nicht automatisch sämtliche Entscheidungstabellen- oder HTTP-Rückgaben des Elternlaufs. Vereinbaren Sie benötigte Dokumentfelder und prüfen Sie ihren tatsächlichen Wert in der Folgekarte.

Ein grüner Aufruf bestätigt nicht jede fachliche Bedingung des Ziels: Bei Advanced wird ein Zielergebnis ohne technischen Fehler als erfolgreicher Aufruf behandelt; auch `failed_condition` kann darunter fallen. Öffnen Sie den Zielnachweis und prüfen Sie dessen gewählten Weg und Wirkung. Behandeln Sie Fehler im aufrufenden Graphen ausdrücklich; vermeiden Sie A→B→A und wiederholte Aufrufe desselben Ziels.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

### `run_workflow` · v2

Identität: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | Aufruf kann erfolgreich sein; Ziel prüfen |

## Prüfstand und Aussagegrenzen

Die ausgewählten Karten- und Knotenergebnisse wurden mit synthetischen Daten in Advanced Test geprüft. Die Antworten liegen im Übungspaket. Dokumentaktionen sind simuliert; ein tatsächlicher Dokumentlauf und externe Zustellung sind damit nicht belegt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
