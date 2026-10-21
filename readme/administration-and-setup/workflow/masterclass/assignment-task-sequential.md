---
description: "P1: Zuweisung, Aufgabe und sequenzielle Freigabe unterscheiden"
---

# P1: Zuweisung, Aufgabe und sequenzielle Freigabe unterscheiden

Eine **Dokumentzuweisung** bestimmt die aktuelle Zuständigkeit. Eine **Aufgabe** ist ein eigener Arbeitsauftrag. Eine **Benachrichtigung** informiert. Keine dieser drei Wirkungen ist bereits eine persönliche Genehmigung. Eine Gruppenzuweisung beweist auch nicht die Zustimmung jedes Gruppenmitglieds.

Bei sequenziellen Karten werden Empfänger und Reihenfolge für den Freigabeprozess gesammelt. Das Beispiel verwendet Prüfer A mit Reihenfolgewert 10 und Prüfer B mit 20. Die geprüfte Abschlusslogik beginnt mit dem kleineren Wert. Der Übergang zu B entsteht durch die verarbeitete Benutzerentscheidung im Freigabeprozess, nicht durch das bloße Weiterlaufen eines Wait-Knotens im Designer.

Vermeiden Sie eine unmittelbare Zuweisung im selben Lauf, wenn Sie den ersten sequenziellen Empfänger erwarten: Die geprüfte Abschlusslogik kann die erste sequenzielle Zuweisung überspringen, sobald das Dokument bereits direkt zugewiesen wurde. Bei Aufgaben werden `task_type`, Priorität, Empfänger und `send_email` unabhängig konfiguriert. Lassen Sie den Mailversand für reine Übungen deaktiviert.

Die fachliche Abnahme benötigt A→Genehmigung→B→Genehmigung sowie Ablehnung durch A, fehlenden Empfänger und erneutes Auslösen. Nach Ablehnung darf kein Abschluss-Export erfolgen; eine blockierte Empfängerauflösung darf nicht als abgeschlossene Freigabe erscheinen. Prüfen Sie Dokumentzuständigkeit und Aufgabenbestand getrennt. Designer-Simulationen belegen keinen echten Benutzerübergang.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

### `action_assign_doc_to_user_sequential` · v2

Identität: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identität: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → Genehmigen → B → Genehmigen |
| ASSIGN-02 | A → Ablehnen | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | Rückfallroute |
| ASSIGN-04 | RUN-1 → RUN-2 | Doppelverarbeitung prüfen |
| ASSIGN-05 | direct + sequential | ersten Empfänger prüfen |

## Prüfstand und Aussagegrenzen

Parameter und Verhalten wurden gegen den Dev-Katalog und den geprüften Quellstand abgeglichen. Die fachlichen Prüffälle sind eine Abnahmeanleitung. Persönliche Freigaben, reale Datenänderungen und Zustellungen wurden für dieses Kapitel nicht durchgeführt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
