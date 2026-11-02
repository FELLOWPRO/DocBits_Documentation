---
description: "P1: obliczanie kolumn i zależności od regex"
---

# P1: obliczanie kolumn i zależności od regex

**Calculate Columns** oblicza dwie kolumny tego samego wiersza i zapisuje wynik. **Calculate in / CALC_COLUMNS_REGEX** dodaje warunek regex na trzeciej kolumnie. Regex decyduje tu, czy liczyć; nie wyodrębnia ani nie zastępuje tekstu. Dawny opis zamiany tekstu nie dotyczy tej karty.

Przykład: `QTY=2`, `PRICE=10`, operacja `*`, wynik `TOTAL=20.0`. Dla wariantu regex użyj `TYPE` i wzorca `^A$`. Wiersz A jest obliczany. W niepasującym wierszu B kod zapisuje pusty wynik; istniejące TOTAL nie jest automatycznie zachowywane.

Funkcja arytmetyczna zaokrągla wyniki do czterech miejsc. Pojedynczy pusty argument może stać się 0; dwa puste teksty dają pusty wynik. `+` może łączyć tekst nieliczbowy. `10/0` zgłasza błąd w sprawdzonej funkcji. Przed obliczeniem sprawdzaj liczby i wymagane komórki oraz dodaj ścieżkę błędu.

Zachowaj pełną tabelę przed/po: dwa pasujące wiersze, jeden niepasujący, pustą wartość, błędny tekst i dzielenie przez zero. Dla zależnych obliczeń A→B połącz karty jawnie i sprawdź aktualną wartość czytaną przez B. Porównuj każdy wiersz i pozostałe istniejące kolumny, nie tylko status dokumentu.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `calc_columns` · v2

Identyfikacja: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

Identyfikacja: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## Dowody i ograniczenia

Parametry i zachowanie porównano z katalogiem Dev oraz sprawdzonym kodem. Przypadki biznesowe są instrukcją odbioru. W tym rozdziale nie wykonano osobistych zatwierdzeń, rzeczywistych zmian ani dostarczeń.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
