---
description: "P1: Entscheidungstabelle bis zur Zuweisung nachvollziehen"
---

# P1: Entscheidungstabelle bis zur Zuweisung nachvollziehen

Eine Entscheidungstabelle verbindet Eingabefelder mit typisierten Rückgaben. Das Beispiel verwendet `cost_center=4711` und `total_amount`: bis 1000 soll Prüfer A, darüber Prüfer B zuständig sein. Verwenden Sie zwei überschneidungsfreie Regeln und gültige Benutzer-IDs Ihrer Testorganisation. Die Beispieldatei im Paket beschreibt den Aufbau; sie ist kein zugesicherter Import in einen Tabelleneditor.

Bei **Decision Table has Returns**, Version 3, aktivieren Sie `store_data=wf_store_data`. In Version 2 wird stattdessen die boolesche Speicheroption gelesen. Die nachfolgende Zuweisung benötigt die gespeicherten Rückgaben desselben Laufs. Eine erfolgreiche Tabellenausführung allein bestätigt noch keinen gültigen Benutzer.

Eine Rückgabe für Benutzer besitzt beispielsweise `output_type=user` und `value=101`; 101 ist eine synthetische ID und muss durch einen vorhandenen Testbenutzer ersetzt werden. Wählen Sie anschließend **Assign document based on decision table** mit `assignee_type=user`. In der geprüften Version 2 dieser Aktion wird der letzte passende Rückgabeeintrag gewählt. „Mehrere Treffer“ bedeutet hier nicht automatisch „alle Benutzer freigeben lassen“.

Prüfen Sie genau einen Treffer, keinen Treffer, mehrere Treffer, falschen Rückgabetyp, ungültige Benutzer-ID und deaktiviertes Speichern. Verbinden Sie keinen Treffer und Zuweisungsfehler mit einer bewusst konfigurierten Rückfallroute. Ermitteln Sie Reihenfolge und Trefferregel, statt eine zufällige Tabellenreihenfolge als Geschäftsregel zu verwenden. Die tatsächliche Zuweisung wird am Dokument abgenommen.

Eine Entscheidungstabelle wird durch ihre Prüfkarte tatsächlich beim Tabellendienst ausgewertet. Testmodus ist keine allgemeine Garantie gegen Nebenwirkungen; verwenden Sie ausschließlich eigene Testdaten und prüfen Sie die verwendeten Aktionen.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

### `condition_decision_tree_data` · v3

Identität: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

Identität: `699912a7-2369-47e0-9092-8d027e13752a`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | kein Ergebnis / ungültiger Benutzer / falscher Typ | Rückfallroute |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | keine gespeicherte Rückgabe für Zuweisung |

## Prüfstand und Aussagegrenzen

Parameter und Verhalten wurden gegen den Dev-Katalog und den geprüften Quellstand abgeglichen. Die fachlichen Prüffälle sind eine Abnahmeanleitung. Persönliche Freigaben, reale Datenänderungen und Zustellungen wurden für dieses Kapitel nicht durchgeführt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
