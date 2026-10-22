---
description: "P1: od tabeli decyzyjnej do przypisania dokumentu"
---

# P1: od tabeli decyzyjnej do przypisania dokumentu

Tabela decyzyjna łączy pola wejściowe z typowanymi wynikami. Przykład używa `cost_center=4711` i `total_amount`: do 1000 osoba A, powyżej 1000 osoba B. Utwórz dwie niepokrywające się reguły i użyj prawidłowych użytkowników organizacji testowej. Plik pakietu opisuje konfigurację; nie gwarantuje importu do edytora.

W **Decision Table has Returns** v3 włącz `store_data=wf_store_data`. Wersja 2 odczytuje zamiast tego logiczną opcję zapisu. Następna karta przypisania potrzebuje wyników zapisanych w tym samym wykonaniu. Udane wykonanie tabeli nie potwierdza jeszcze prawidłowego użytkownika.

Wynik użytkownika może zawierać `output_type=user` oraz `value=101`; 101 jest syntetyczne i wymaga zastąpienia istniejącym użytkownikiem testowym. Następnie wybierz **Assign document based on decision table** z `assignee_type=user`. Sprawdzona v2 tej akcji wybiera ostatni pasujący wynik. Wiele trafień nie wymaga automatycznie zatwierdzenia przez wszystkich użytkowników.

Sprawdź jedno, zero i wiele trafień, błędny typ wyniku, nieprawidłowego użytkownika oraz wyłączony zapis. Brak trafienia i błąd przypisania skieruj do jawnej ścieżki rezerwowej. Określ kolejność i politykę trafień zamiast uznawać przypadkową kolejność za regułę biznesową. Odbierz rzeczywiste przypisanie na dokumencie.

Warunek tabeli decyzyjnej rzeczywiście wywołuje usługę w celu oceny tabeli. Tryb testowy nie gwarantuje braku wszystkich skutków ubocznych: używaj własnych danych testowych i sprawdzaj użyte działania.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `condition_decision_tree_data` · v3

Identyfikacja: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

Identyfikacja: `699912a7-2369-47e0-9092-8d027e13752a`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | brak wyniku / nieprawidłowy użytkownik / zły typ | Ścieżka rezerwowa |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | brak zapisanego wyniku do przypisania |

## Dowody i ograniczenia

Parametry i zachowanie porównano z katalogiem Dev oraz sprawdzonym kodem. Przypadki biznesowe są instrukcją odbioru. W tym rozdziale nie wykonano osobistych zatwierdzeń, rzeczywistych zmian ani dostarczeń.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
