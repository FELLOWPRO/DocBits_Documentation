---
description: "Field is, Docfield is oder Compare two Fields wählen"
---

# Field is, Docfield is und zwei Felder vergleichen

Drei Bedingungskarten sehen im Designer ähnlich aus, und ihr Unterschied entscheidet, was eine Regel tatsächlich erkennen kann. Diese Seite hilft Ihnen, die richtige auszuwählen, und gibt Ihnen danach drei kurze Übungen, die zeigen, was jede Karte zurückgibt. Am Ende können Sie „leer“ von der Zahl `0`, „falsch“ von „fehlend“ und eine nicht erfüllte Bedingung von einem Fehler unterscheiden; technisches `null` gilt dabei als leer, die Zahl `0` nicht.

Führen Sie die Übungen im Advanced Test in Ihrer eigenen Testorganisation mit einem synthetischen Dokument aus. Hier berührt nichts ein Kundendokument.

## Welche Karte brauchen Sie?

| Wenn Sie prüfen wollen, ... | Verwenden Sie | Karte und Version |
| --- | --- | --- |
| ob ein Feld überhaupt einen Wert trägt | **Field is** | `condition_docfield_status` v2 |
| ein Feld gegen einen Wert, den Sie eingeben | **Docfield is** | `condition_docfield_operator_value` v2 |
| zwei Felder desselben Dokuments gegeneinander | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

Alle drei sind Bedingungen: Sie liefern ein Ergebnis und ändern nichts am Dokument. Eine Leerprüfung beweist nicht, dass ein Feld im Layout existiert oder dass sein Inhalt fachlich gültig ist. Die einzelnen Kartenseiten führen jede Einstellung auf: [Field is](../and/document-field/field-is.md), [Docfield is](../and/document-field/docfield-is.md) und [Compare two Fields](../and/document-field/compare-two-fields.md).

## Übung 1: herausfinden, was „leer“ bedeutet

**Ziel:** wissen, welche Werte Field is in Version 2 als leer behandelt.

1. Fügen Sie **Field is** Version 2 in Ihrer Testorganisation einer Regel hinzu und wählen Sie ein Textfeld aus Ihrem Layout.
2. Setzen Sie den Feldstatus auf `field_empty` (Empty or missing).
3. Führen Sie acht Advanced-Test-Fälle mit vollständigen Dokumentdaten aus: fehlendes Feld, `null`, leerer Text `""`, nur Leerzeichen `" "`, boolesches `false`, Zahl `0`, Text `"0"` und Text `"false"`.

**Fertig, wenn:** die ersten fünf Fälle `field_empty=success` liefern und die letzten drei `field_empty=failed_condition`. Diese acht Fälle wurden in Dev mit vollständigen Dokumentdaten geprüft.

Zahl `0`, Text `"0"` und Text `"false"` sind Werte, keine Abwesenheit. Wenn wahr oder falsch Ihre Geschäftsentscheidung ist, verwenden Sie eine ausdrückliche Checkbox-Bedingung, statt das Feld auf Leerheit zu prüfen.

## Übung 2: ein Feld mit einem Wert vergleichen

**Ziel:** sehen, wie Operator und Feldtyp die Antwort verändern.

1. Wählen Sie ein numerisches Feld wie `total_amount`, den Operator `gt` und den Wert `1000`.
2. Testen Sie `1000`, `1000.01`, ein fehlendes Feld und einen ungültigen Wert.

**Fertig, wenn:** `1000` `failed_condition` liefert, weil `gt` echt größer bedeutet, `1000.01` `success` liefert und eine fehlende oder ungültige Eingabe `error` zurückgibt.

## Übung 3: zwei Felder vergleichen

**Ziel:** wissen, wann zwei Werte verglichen werden und wann die Karte sie gar nicht vergleichen kann.

1. Legen Sie linkes Feld, Operator und rechtes Feld fest. Verwenden Sie zwei Felder mit zueinander passenden Typen.
2. Testen Sie gleiche Werte, unterschiedliche Werte und eine fehlende Eingabe.

**Fertig, wenn:** gleiche Werte `eq` erfüllen, unterschiedliche Werte `failed_condition` liefern und eine fehlende Eingabe `error` zurückgibt statt einer bewiesenen Ungleichheit.

## Was die drei Ergebnisse bedeuten

| Ergebnis | Was es Ihnen sagt |
| --- | --- |
| `success` | Die Karte hat die Werte verglichen und die Bedingung war erfüllt. |
| `failed_condition` | Die Karte hat die Werte verglichen und die Bedingung war nicht erfüllt. `0` und `"0"` landen bei einer Leerprüfung hier. |
| `error` | Die Karte konnte nicht vergleichen, etwa weil ein Wert fehlt oder ungültig ist. Ein Fehler ist nicht dieselbe Antwort wie „ungleich“. |

## Der Typ gehört zum Vergleich

Ein Wert `"1000.01"` in einem AMOUNT-Feld ist nicht dasselbe wie dieselben Zeichen in einem Textfeld. Das v2-Übungspaket verwendet AMOUNT und Dezimalpunkte im JSON. Prüfen Sie technischen Feldschlüssel, Layout und Typ gemeinsam. Eine übersetzte Beschriftung ist kein technischer Schlüssel, und ein Währungssymbol ist kein Zahlenwert.

## Karten und Beispielparameter

Diese Werte beschreiben einzelne Kartenparameter, nicht einen importierbaren vollständigen Workflow. Ersetzen Sie YOUR\_\* durch Ihre eigenen Testauswahlen. Die verborgene Aufrufer-ID verwaltet der Designer. Katalog: Dev, DocFlow 2.10.38, 21. Oktober 2026; prüfen Sie verfügbare Versionen und Berechtigungen in Ihrer eigenen Organisation.

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
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Prüfstand und Aussagegrenzen

Ausgewählte Karten- und Knotenergebnisse wurden mit synthetischen Daten im Advanced Test geprüft. Die Antworten liegen im Übungspaket. Dokumentaktionen sind simuliert; diese Tests belegen keinen gespeicherten Dokumentlauf und keine externe Zustellung.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
