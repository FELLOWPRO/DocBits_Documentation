---
description: "P1: Tabellen berechnen und Regex-Abhängigkeit prüfen"
---

# P1: Tabellen berechnen und Regex-Abhängigkeit prüfen

**Calculate Columns** rechnet mit zwei Spalten derselben Zeile und schreibt die Ergebnisspalte. **Calculate in / CALC_COLUMNS_REGEX** ergänzt eine Regex-Bedingung auf einer dritten Spalte. Die Regex entscheidet, ob gerechnet wird; sie extrahiert oder ersetzt hier keinen Teil des Texts. Die frühere Ersetzungserklärung gehört nicht zu dieser Karte.

Beispiel: `QTY=2`, `PRICE=10`, Operation `*`, Ergebnis `TOTAL=20.0`. Bei der Regex-Variante verwenden Sie `TYPE`, Muster `^A$`. Eine A-Zeile wird berechnet. Für eine nicht passende B-Zeile schreibt der geprüfte Code einen leeren Ergebniswert; ein vorhandener TOTAL-Wert bleibt dabei nicht automatisch erhalten.

Die Rechenhilfe rundet numerische Ergebnisse auf vier Dezimalstellen. Leere Einzelwerte können als 0 behandelt werden; zwei leere Texte ergeben leer. Mit `+` können nicht numerische Texte als Text verbunden werden. `10/0` löst in der geprüften Rechenhilfe einen Fehler aus. Prüfen Sie Zahlen und erforderliche Zellen deshalb vor der Berechnung; definieren Sie einen Fehlerweg.

Halten Sie eine vollständige Vorher-nachher-Tabelle fest: zwei passende Zeilen, eine unpassende Regex-Zeile, leere Eingabe, ungültiger Text und Division durch null. Bei A→B-abhängigen Berechnungen verbinden Sie die Karten ausdrücklich und prüfen Sie, welchen aktualisierten Wert die zweite Karte liest. Vergleichen Sie jede Zeile und vorhandene Fremdspalten, nicht nur den Dokumentstatus.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

### `calc_columns` · v2

Identität: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

Identität: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## Prüfstand und Aussagegrenzen

Parameter und Verhalten wurden gegen den Dev-Katalog und den geprüften Quellstand abgeglichen. Die fachlichen Prüffälle sind eine Abnahmeanleitung. Persönliche Freigaben, reale Datenänderungen und Zustellungen wurden für dieses Kapitel nicht durchgeführt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
