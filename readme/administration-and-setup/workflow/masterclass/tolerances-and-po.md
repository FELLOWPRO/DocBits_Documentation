---
description: "P1: Toleranzen und PO-Vergleich mit eindeutiger Referenz"
---

# P1: Toleranzen und PO-Vergleich mit eindeutiger Referenz

Bei einer Prozenttoleranz zählt die **Referenzseite**. In der geprüften PO-Karte, Version 5, liest sich `document_po` als Dokumentwert gegen Bestellwert; der Bestellwert ist die Prozentbasis. `po_document` kehrt Vergleich und Basis um. Die sechs zulässigen Richtungen schließen auch den empfangenen Wert ein. Wählen Sie Richtung, Operator und Any/All ausdrücklich.

Beispiel: Bestellung 100, Dokument 102.02, Gleichheit mit 2 Prozent. Mit Bestellreferenz liegt das zulässige Band bei 98 bis 102: außerhalb. Mit Dokumentreferenz liegt es bei 99.9796 bis 104.0604: der Bestellwert 100 liegt darin. Bei Dokument 102 ist die obere Grenze der ersten Richtung eingeschlossen. Eine absolute Toleranz 2 verwendet dieselbe Einheit wie der verglichene Wert.

Die Karte normalisiert Preise je Preiseinheit und berücksichtigt je Vergleichsrichtung Bestell- beziehungsweise Empfangsdaten. Prüfen Sie Zuordnung, Mengen und Einheiten vor der Toleranz. Any benötigt einen passenden Vergleich, All alle tatsächlich verglichenen Ergebnisse. **Keine vergleichbare Position** ist in v5 ein Datenfehler und kein automatisch erfülltes All. Nicht zugeordnete Zeilen müssen separat erfasst werden.

Bei bestehenden Workflows lesen Sie die gespeicherte Version, Vergleichsrichtung und den Operator erneut: Migrationen haben Vergleichseinstellungen verändert. Die früheren Bezeichnungen reichen als Abnahme nicht. Halten Sie Ausgangswerte und Referenz, Entscheidung bei exakter Grenze, kleinste Überschreitung, Rundungspräzision, fehlende Bestellung und unzugeordnete Position fest. Die Beispielrechnung ersetzt keine PO-Abnahme mit Ihren Stammdaten.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

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
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | Datenfehler |
| PO-05 | unmatched_rows>0 | Abdeckung getrennt prüfen |

## Prüfstand und Aussagegrenzen

Parameter und Verhalten wurden gegen den Dev-Katalog und den geprüften Quellstand abgeglichen. Die fachlichen Prüffälle sind eine Abnahmeanleitung. Persönliche Freigaben, reale Datenänderungen und Zustellungen wurden für dieses Kapitel nicht durchgeführt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
