---
description: "P1: jawna podstawa tolerancji i kierunek porównania PO"
---

# P1: jawna podstawa tolerancji i kierunek porównania PO

Tolerancja procentowa zależy od **strony odniesienia**. W sprawdzonej karcie PO v5 `document_po` porównuje dokument z zamówieniem; zamówienie jest podstawą procentu. `po_document` odwraca porównanie i podstawę. Sześć dozwolonych kierunków obejmuje też wartość otrzymaną. Jawnie wybierz kierunek, operator oraz Any/All.

Przykład: zamówienie 100, dokument 102.02, równość z tolerancją 2 %. Przy odniesieniu do zamówienia przedział wynosi 98–102: poza nim. Przy odniesieniu do dokumentu wynosi 99.9796–104.0604: zamówienie 100 mieści się. Dokument 102 leży dokładnie na włączonej górnej granicy pierwszego kierunku. Tolerancja bezwzględna 2 używa jednostki porównywanej wartości.

Karta normalizuje ceny na jednostkę cenową i używa danych zamówienia lub odbioru zależnie od kierunku. Sprawdź dopasowanie, ilości i jednostki. Any wymaga jednego zgodnego porównania; All wszystkich faktycznie wykonanych porównań. **Brak porównywalnej pozycji** to w v5 błąd danych, a nie automatycznie spełnione All. Licz osobno niedopasowane wiersze.

W istniejących workflow ponownie odczytaj zapisaną wersję, kierunek i operator: migracje zmieniały ustawienia. Stare etykiety nie wystarczą do odbioru. Zapisz wartości, podstawę, granicę, najmniejsze przekroczenie, precyzję, brak zamówienia i niedopasowaną pozycję. Przykład nie zastępuje odbioru z własnymi danymi PO.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `condition_docfield_operator_docfield_tolerances` · v2

Identyfikacja: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identyfikacja: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | błąd danych |
| PO-05 | unmatched_rows>0 | sprawdź pokrycie osobno |

## Dowody i ograniczenia

Parametry i zachowanie porównano z katalogiem Dev oraz sprawdzonym kodem. Przypadki biznesowe są instrukcją odbioru. W tym rozdziale nie wykonano osobistych zatwierdzeń, rzeczywistych zmian ani dostarczeń.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
