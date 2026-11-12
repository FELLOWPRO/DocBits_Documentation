---
description: "Wybór Field is, Docfield is lub Compare two Fields"
---

# P1: Wybór Field is, Docfield is lub Compare two Fields

Trzy karty warunków wyglądają w projektancie podobnie, a ich różnica decyduje o tym, co reguła może naprawdę wychwycić. Ta strona pomaga wybrać właściwą, a potem daje trzy krótkie ćwiczenia pokazujące, co zwraca każda karta. Na koniec odróżnisz „puste” od „zera”, „fałsz” od „brak” oraz niespełniony warunek od błędu.

Ćwiczenia wykonaj w Advanced Test, we własnej organizacji testowej, na dokumencie syntetycznym. Nic tutaj nie dotyka dokumentu klienta.

## Której karty potrzebujesz?

| Jeśli chcesz sprawdzić... | Użyj | Karta i wersja |
| --- | --- | --- |
| czy pole w ogóle ma wartość | **Field is** | `condition_docfield_status` v2 |
| pole wobec wartości, którą wpisujesz | **Docfield is** | `condition_docfield_operator_value` v2 |
| dwa pola tego samego dokumentu względem siebie | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

Wszystkie trzy są warunkami: zwracają wynik i niczego nie zmieniają w dokumencie. Sprawdzenie stanu pustego nie dowodzi, że pole istnieje w layoucie ani że jego zawartość jest poprawna biznesowo. Strony poszczególnych kart opisują każde ustawienie: [Field is](../and/document-field/field-is.md), [Docfield is](../and/document-field/docfield-is.md) oraz [Compare two Fields](../and/document-field/compare-two-fields.md).

## Ćwiczenie 1: ustalić, co znaczy „puste”

**Cel:** wiedzieć, które wartości Field is w wersji 2 traktuje jako puste.

1. Dodaj **Field is** w wersji 2 do reguły w swojej organizacji testowej i wybierz pole tekstowe ze swojego layoutu.
2. Ustaw stan pola na `field_empty` (Empty or missing).
3. Uruchom osiem przypadków Advanced Test z pełnymi danymi dokumentu: brakujące pole, `null`, pusty tekst `""`, same spacje `" "`, wartość logiczna `false`, liczba `0`, tekst `"0"` i tekst `"false"`.

**Gotowe, gdy:** pierwsze pięć przypadków zwróci `field_empty=success`, a ostatnie trzy `field_empty=failed_condition`. Te osiem przypadków sprawdzono w Dev na pełnych danych dokumentu.

Liczba `0`, tekst `"0"` i tekst `"false"` to wartości, a nie brak. Jeśli Twoją decyzją biznesową jest prawda lub fałsz, użyj jawnego warunku pola wyboru, zamiast sprawdzać pole pod kątem pustki.

## Ćwiczenie 2: porównać pole z wartością

**Cel:** zobaczyć, jak operator i typ pola zmieniają odpowiedź.

1. Wybierz pole liczbowe, na przykład `total_amount`, operator `gt` i wartość `1000`.
2. Sprawdź `1000`, `1000.01`, brakujące pole oraz wartość nieprawidłową.

**Gotowe, gdy:** `1000` zwróci `failed_condition`, bo `gt` znaczy ściśle większe, `1000.01` zwróci `success`, a brakujące lub nieprawidłowe wejście zwróci `error`.

## Ćwiczenie 3: porównać dwa pola

**Cel:** wiedzieć, kiedy dwie wartości są porównywane, a kiedy karta nie może ich porównać w ogóle.

1. Ustaw pole lewe, operator i pole prawe. Użyj dwóch pól o pasujących typach.
2. Sprawdź wartości równe, wartości różne oraz brakujące wejście.

**Gotowe, gdy:** równe wartości spełniają `eq`, różne wartości zwracają `failed_condition`, a brakujące wejście zwraca `error` zamiast dowiedzionej nierówności.

## Co znaczą trzy wyniki

| Wynik | Co Ci mówi |
| --- | --- |
| `success` | Karta porównała wartości i warunek był spełniony. |
| `failed_condition` | Karta porównała wartości i warunek nie był spełniony. `0` i `"0"` trafiają tutaj przy sprawdzaniu stanu pustego. |
| `error` | Karta nie mogła porównać, na przykład bo wartość brakuje lub jest nieprawidłowa. Błąd to nie ta sama odpowiedź co „różne”. |

## Typ jest częścią porównania

Wartość `"1000.01"` w polu AMOUNT to nie to samo co te same znaki w polu tekstowym. Pakiet ćwiczeń v2 używa AMOUNT i kropek dziesiętnych w JSON. Sprawdzaj razem klucz techniczny pola, layout i typ. Przetłumaczona etykieta nie jest kluczem technicznym, a symbol waluty nie jest wartością liczbową.

## Karty i przykładowe parametry

Te wartości opisują parametry pojedynczych kart, a nie kompletny workflow do importu. Zastąp YOUR\_\* własnymi wyborami testowymi. Ukrytym identyfikatorem wywołującego zarządza projektant. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; dostępne wersje i uprawnienia sprawdź we własnej organizacji.

### `condition_docfield_status` · v2

Tożsamość: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Tożsamość: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Tożsamość: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / układ | Oczekiwany wynik |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Dowody i ograniczenia

Wybrane wyniki kart i węzłów sprawdzono na danych syntetycznych w Advanced Test. Odpowiedzi znajdują się w pakiecie ćwiczeń. Akcje na dokumencie są symulowane; te testy nie dowodzą zapisanego przebiegu dokumentu ani dostarczenia na zewnątrz.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
