---
description: "P1: Field is, Docfield is und zwei Felder vergleichen"
---

# P1: Field is, Docfield is und zwei Felder vergleichen

Verwenden Sie **Field is** für den Leerzustand, **Docfield is** für den Vergleich mit einem konfigurierten Wert und **Compare two Fields** für zwei Werte desselben Dokuments. Eine Leerprüfung beweist nicht, dass das Feld im Layout existiert oder fachlich korrekt ist.

Für Field is, Version 2, ergeben fehlendes Feld, `null`, leerer Text, nur Leerzeichen und der boolesche Wert `false` den Zustand leer. Die Zahl `0`, der Text `"0"` und der Text `"false"` sind nicht leer. Diese acht Fälle wurden mit vollständigen Dokumentdaten im Dev-Test geprüft. Verwenden Sie eine explizite Checkbox-Bedingung, wenn wahr/falsch die Geschäftsentscheidung ist.

Ein Wert `"1000.01"` mit Feldtyp AMOUNT ist von einem Textfeld gleicher Schreibweise zu unterscheiden. Das v2-Übungspaket verwendet AMOUNT und Dezimalpunkte im JSON. Prüfen Sie technische Feldschlüssel, Layout und Typ gemeinsam. Eine lokalisierte Beschriftung oder ein Währungssymbol ist kein technischer Feldschlüssel beziehungsweise Zahlenwert.

Für Compare two Fields legen Sie linkes Feld, Operator und rechtes Feld fest. Prüfen Sie kompatible Typen und beide Eingaben; ein fehlender oder nicht vergleichbarer Wert ist ein Datenfehler, keine bewiesene Ungleichheit. Wiederholen Sie Positivfall, Negativfall, fehlende Eingabe und den exakten Grenzwert. Das Ergebnisblatt hält Wert, Typ und gewählten Ausgang fest.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

### `condition_docfield_status` · v2

Identität: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identität: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identität: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Prüfstand und Aussagegrenzen

Die ausgewählten Karten- und Knotenergebnisse wurden mit synthetischen Daten in Advanced Test geprüft. Die Antworten liegen im Übungspaket. Dokumentaktionen sind simuliert; ein tatsächlicher Dokumentlauf und externe Zustellung sind damit nicht belegt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
