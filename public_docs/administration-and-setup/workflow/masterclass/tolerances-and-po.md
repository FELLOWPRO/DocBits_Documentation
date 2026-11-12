---
description: "Toleranz und Referenzrichtung beim PO-Vergleich eindeutig machen"
---

# Toleranzen und PO-Vergleich mit eindeutiger Referenz

Eine Toleranz von 2 Prozent ist kein fester Betrag. Sie ist 2 Prozent der Seite, gegen die Sie vergleichen, deshalb kann dieselbe Rechnungsposition in der einen Richtung durchfallen und in der anderen bestehen. Diese Seite zeigt das an einem Wertepaar, gibt Ihnen drei Übungen zum Nachbauen und listet danach die sechs Vergleichsrichtungen und die Kartenparameter auf, die Sie in Ihren eigenen Test übernehmen können.

Führen Sie die Übungen im Advanced Test in Ihrer eigenen Testorganisation mit einem synthetischen Dokument und einer zugeordneten Bestellung durch.

## Die Referenzseite ist die Basis

In der geprüften PO-Karte Version 5 vergleicht `document_po` den Dokumentwert mit dem Bestellwert, der Bestellwert ist also die Basis für eine Prozenttoleranz. `po_document` dreht sowohl den Vergleich als auch die Basis um. Die sechs zulässigen Richtungen umfassen außerdem die empfangene Seite. Setzen Sie Richtung, Operator und Any/All ausdrücklich, statt sich darauf zu verlassen, was eine gespeicherte Karte noch enthält.

## Übung 1: gleiche Werte, zwei Richtungen

**Ziel:** sehen, wie aus denselben Zahlen zwei verschiedene Ergebnisse werden.

1. Legen Sie eine zugeordnete Bestellung über `100` und einen Dokument-Einzelpreis von `102.02` an.
2. Vergleichen Sie mit dem Operator `eq` und einer Toleranz von `2` Prozent, zuerst mit `document_po`. Erwarten Sie `false`: 2 Prozent von 100 sind 2, das geschlossene Intervall reicht also von 98 bis 102, und 102.02 liegt 0.02 darüber.
3. Wiederholen Sie denselben Fall mit `po_document`. Erwarten Sie `true`: 2 Prozent von 102.02 sind 2.0404, das Intervall reicht von 99.9796 bis 104.0604, und der Bestellwert 100 liegt darin.

**Fertig, wenn:** beide Ergebnisse und beide Intervalle notiert sind und Sie für jede Richtung sagen können, von welchem Wert der Prozentsatz berechnet wurde.

Eine absolute Toleranz von `2` verhält sich anders: Sie verwendet die Einheit des verglichenen Werts und verschiebt sich nicht mit der Referenz.

## Übung 2: die exakte Grenze finden

**Ziel:** wissen, ob der Rand des Intervalls mitzählt.

1. Behalten Sie `document_po`, `eq` und die Toleranz von 2 Prozent und ändern Sie den Dokumentwert auf `102`.
2. Führen Sie den Fall aus, danach noch einmal mit `102.01`.

**Fertig, wenn:** `102` `true` liefert und `102.01` `false`. Die Grenze ist eingeschlossen: 102 liegt genau auf der oberen Grenze des Intervalls 98 bis 102.

## Übung 3: Any, All und die verglichenen Positionen

**Ziel:** wissen, was die Karte mit mehreren Positionen macht und was passiert, wenn es nichts zu vergleichen gibt.

1. Bauen Sie ein Dokument mit zwei Positionen gegen dieselbe zugeordnete Bestellung: eine innerhalb der Toleranz, eine außerhalb.
2. Führen Sie die Karte mit `match_any` aus, danach mit `match_all`.
3. Führen Sie ein Dokument aus, das gar keine vergleichbare Position enthält.

**Fertig, wenn:** `match_any` an der einen passenden Position besteht, `match_all` scheitert, sobald ein Vergleich scheitert, und das Dokument ohne vergleichbare Position einen Datenfehler zurückgibt. In Version 5 ist das ein Fehler und kein automatisch erfülltes All.

## Welche Seite ist die Basis?

| Gespeicherte Option | Verglichene Seite | Referenzseite (Prozentbasis) |
| --- | --- | --- |
| `po_document` | Bestellung | Dokument |
| `received_document` | Empfangene Daten | Dokument |
| `po_received` | Bestellung | Empfangene Daten |
| `document_po` | Dokument | Bestellung |
| `document_received` | Dokument | Empfangene Daten |
| `received_po` | Empfangene Daten | Bestellung |

## Prüfen, bevor Sie einem bestehenden Workflow trauen

Die Karte normalisiert Preise je Preiseinheit und verwendet je nach Richtung Bestell- oder Empfangsdaten. Prüfen Sie deshalb zuerst Zuordnung, Mengen und Einheiten. Any braucht einen passenden Vergleich, All jeden tatsächlich durchgeführten Vergleich. Nicht zugeordnete Zeilen erfassen Sie getrennt.

Bei bestehenden Workflows lesen Sie gespeicherte Version, Richtung und Operator erneut: Migrationen haben Vergleichseinstellungen verändert, historische Bezeichnungen sind also kein ausreichender Abnahmebeleg. Halten Sie Werte und Referenz, die exakte Grenze, die kleinste Überschreitung, die Rundungspräzision, die fehlende Bestellung und die unzugeordnete Position fest. Diese Rechnung ersetzt keine Abnahme mit Ihren eigenen PO-Stammdaten.

## Karten und Beispielparameter

Diese Werte beschreiben einzelne Kartenparameter, nicht einen importierbaren vollständigen Workflow. Ersetzen Sie YOUR\_\* durch Ihre eigenen Testauswahlen. Die verborgene Aufrufer-ID verwaltet der Designer. Katalog: Dev, DocFlow 2.10.38, 21. Oktober 2026; prüfen Sie verfügbare Versionen und Berechtigungen in Ihrer eigenen Organisation.

### `condition_docfield_operator_docfield_tolerances` · v2

Identität: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identität: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | Datenfehler |
| PO-05 | unmatched\_rows>0 | Abdeckung getrennt prüfen |

## Prüfstand und Aussagegrenzen

Parameter und Verhalten wurden gegen den Dev-Katalog und die geprüfte Quellversion kontrolliert. Die fachlichen Prüffälle sind ein Abnahmeverfahren. Persönliche Freigaben, echte Datenänderungen und eine Auslieferung wurden für dieses Kapitel nicht durchgeführt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
