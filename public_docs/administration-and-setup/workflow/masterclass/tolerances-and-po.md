---
description: "Jednoznaczny punkt odniesienia tolerancji i porównania PO"
---

# P1: Jednoznaczny punkt odniesienia tolerancji i porównania PO

Tolerancja 2 procent to nie stała kwota. To 2 procent strony, z którą porównujesz, dlatego ta sama pozycja faktury może nie przejść w jednym kierunku, a przejść w drugim. Ta strona pokazuje to na jednej parze wartości, daje trzy ćwiczenia do odtworzenia, a następnie wymienia sześć kierunków porównania i parametry kart, które możesz przenieść do własnego testu.

Ćwiczenia wykonaj w Advanced Test, we własnej organizacji testowej, na dokumencie syntetycznym i powiązanym zamówieniu.

## Strona odniesienia jest podstawą

W badanej karcie PO w wersji 5 `document_po` porównuje wartość dokumentu z wartością zamówienia, więc to zamówienie jest podstawą tolerancji procentowej. `po_document` odwraca zarówno porównanie, jak i podstawę. Sześć dozwolonych kierunków obejmuje także stronę odebraną. Ustawiaj kierunek, operator i Any/All wprost, zamiast polegać na tym, co jeszcze zawiera zapisana karta.

## Ćwiczenie 1: te same wartości, dwa kierunki

**Cel:** zobaczyć, jak z tych samych liczb powstają dwa różne wyniki.

1. Przygotuj powiązane zamówienie na `100` i cenę jednostkową w dokumencie `102.02`.
2. Porównaj operatorem `eq` i tolerancją `2` procent, najpierw z `document_po`. Oczekuj `false`: 2 procent ze 100 to 2, więc przedział domknięty biegnie od 98 do 102, a 102.02 leży 0.02 powyżej.
3. Powtórz ten sam przypadek z `po_document`. Oczekuj `true`: 2 procent ze 102.02 to 2.0404, przedział biegnie od 99.9796 do 104.0604, a wartość zamówienia 100 mieści się w nim.

**Gotowe, gdy:** oba wyniki i oba przedziały są zapisane, a dla każdego kierunku potrafisz wskazać, z której wartości obliczono procent.

Tolerancja bezwzględna `2` zachowuje się inaczej: używa jednostki porównywanej wartości i nie przesuwa się wraz z odniesieniem.

## Ćwiczenie 2: znaleźć dokładną granicę

**Cel:** wiedzieć, czy brzeg przedziału się liczy.

1. Zachowaj `document_po`, `eq` i tolerancję 2 procent, a wartość dokumentu zmień na `102`.
2. Uruchom przypadek, a potem jeszcze raz z `102.01`.

**Gotowe, gdy:** `102` zwróci `true`, a `102.01` zwróci `false`. Granica jest włączona: 102 leży dokładnie na górnej granicy przedziału od 98 do 102.

## Ćwiczenie 3: Any, All i porównane pozycje

**Cel:** wiedzieć, co karta robi z wieloma pozycjami i co się dzieje, gdy nie ma czego porównywać.

1. Zbuduj dokument z dwiema pozycjami wobec tego samego powiązanego zamówienia: jedną w tolerancji i jedną poza nią.
2. Uruchom kartę z `match_any`, a następnie z `match_all`.
3. Uruchom dokument, który nie ma żadnej porównywalnej pozycji.

**Gotowe, gdy:** `match_any` przechodzi na jednej pasującej pozycji, `match_all` zawodzi, gdy zawiedzie choć jedno porównanie, a dokument bez porównywalnej pozycji zwraca błąd danych. W wersji 5 to błąd, a nie automatycznie spełnione All.

## Która strona jest podstawą?

| Zapisana opcja | Porównywana strona | Strona odniesienia (podstawa procentowa) |
| --- | --- | --- |
| `po_document` | Zamówienie | Dokument |
| `received_document` | Odebrane dane | Dokument |
| `po_received` | Zamówienie | Odebrane dane |
| `document_po` | Dokument | Zamówienie |
| `document_received` | Dokument | Odebrane dane |
| `received_po` | Odebrane dane | Zamówienie |

## Sprawdź, zanim zaufasz istniejącemu workflow

Karta normalizuje ceny na jednostkę ceny i w zależności od kierunku używa danych zamówienia lub odbioru, dlatego najpierw sprawdź powiązanie, ilości i jednostki. Any potrzebuje jednego pasującego porównania, All każdego faktycznie wykonanego. Pozycje niepowiązane ujmuj osobno.

W istniejących workflow odczytaj ponownie zapisaną wersję, kierunek i operator: migracje zmieniały ustawienia porównania, więc historyczne etykiety nie są wystarczającym dowodem odbioru. Zapisz wartości i odniesienie, dokładną granicę, najmniejsze przekroczenie, precyzję zaokrąglenia, brakujące zamówienie i niepowiązaną pozycję. To wyliczenie nie zastępuje odbioru na własnych danych podstawowych PO.

## Karty i przykładowe parametry

Te wartości opisują parametry pojedynczych kart, a nie kompletny workflow do importu. Zastąp YOUR\_\* własnymi wyborami testowymi. Ukrytym identyfikatorem wywołującego zarządza projektant. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; dostępne wersje i uprawnienia sprawdź we własnej organizacji.

### `condition_docfield_operator_docfield_tolerances` · v2

Tożsamość: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Tożsamość: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / układ | Oczekiwany wynik |
| --- | --- | --- |
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | błąd danych |
| PO-05 | unmatched\_rows>0 | sprawdź pokrycie osobno |

## Dowody i ograniczenia

Parametry i zachowanie sprawdzono wobec katalogu Dev oraz badanej wersji kodu. Biznesowe przypadki testowe są procedurą odbioru. W tym rozdziale nie wykonano osobistych zatwierdzeń, zmian prawdziwych danych ani dostarczenia.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
