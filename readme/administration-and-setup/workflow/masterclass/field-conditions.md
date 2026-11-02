---
description: "P1: wybór Field is, Docfield is i Compare two Fields"
---

# P1: wybór Field is, Docfield is i Compare two Fields

Używaj **Field is** do sprawdzania pustej wartości, **Docfield is** do porównania ze skonfigurowaną wartością, a **Compare two Fields** do dwóch wartości bieżącego dokumentu. Test pustej wartości nie dowodzi istnienia pola w układzie ani jego poprawności biznesowej.

Dla Field is v2 brak pola, `null`, pusty tekst, same spacje i wartość logiczna `false` oznaczają puste. Liczba `0`, tekst `"0"` i tekst `"false"` nie są puste. Te osiem przypadków sprawdzono w Dev z pełnymi danymi dokumentu. Gdy decyzja dotyczy prawda/fałsz, użyj jawnego warunku checkbox.

`"1000.01"` w polu AMOUNT różni się od tych samych znaków w polu tekstowym. Pakiet v2 używa AMOUNT i kropek dziesiętnych w JSON. Sprawdzaj razem klucz techniczny, układ i typ. Przetłumaczona etykieta nie jest kluczem technicznym, a symbol waluty nie jest wartością liczbową.

Dla Compare two Fields ustaw lewe pole, operator i prawe pole. Sprawdź zgodne typy i obie wartości: brak lub nieporównywalność to błąd danych, nie dowiedziona nierówność. Powtórz przypadek dodatni, ujemny, brak wejścia i dokładną granicę. Zapisz wartość, typ i wybrane wyjście.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `condition_docfield_status` · v2

Identyfikacja: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identyfikacja: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identyfikacja: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Dowody i ograniczenia

Wybrane wyniki kart i węzłów sprawdzono na danych syntetycznych w Advanced Test. Odpowiedzi są w pakiecie. Działania dokumentalne są symulowane i nie dowodzą zapisanego wykonania ani zewnętrznego dostarczenia.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
