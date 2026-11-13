---
description: "P1: od tabeli decyzyjnej do przypisania dokumentu"
---

# P1: od tabeli decyzyjnej do przypisania dokumentu

Tabela decyzyjna łączy pola wejściowe z typowanymi wynikami. Przykład używa `cost_center=4711` i `total_amount`: do 1000 osoba A, powyżej 1000 osoba B. Utwórz dwie niepokrywające się reguły i użyj prawidłowych użytkowników organizacji testowej. Plik pakietu opisuje konfigurację; nie gwarantuje importu do edytora.

W **Decision Table has Returns** v3 włącz `store_data=wf_store_data`. Wersja 2 odczytuje zamiast tego logiczną opcję zapisu. Następna karta przypisania potrzebuje wyników zapisanych w tym samym wykonaniu. Udane wykonanie tabeli nie potwierdza jeszcze prawidłowego użytkownika.

Wynik użytkownika może zawierać `output_type=user` oraz `value=101`; 101 jest syntetyczne i wymaga zastąpienia istniejącym użytkownikiem testowym. Następnie wybierz **Assign document based on decision table** z `assignee_type=user`. Sprawdzona v2 tej akcji wybiera ostatni pasujący wynik. Wiele trafień nie wymaga automatycznie zatwierdzenia przez wszystkich użytkowników.

Sprawdź jedno, zero i wiele trafień, błędny typ wyniku, nieprawidłowego użytkownika oraz wyłączony zapis. Brak trafienia i błąd przypisania skieruj do jawnej ścieżki rezerwowej. Określ kolejność i politykę trafień zamiast uznawać przypadkową kolejność za regułę biznesową. Odbierz rzeczywiste przypisanie na dokumencie.

Warunek tabeli decyzyjnej rzeczywiście wywołuje usługę w celu oceny tabeli. Tryb testowy nie gwarantuje braku wszystkich skutków ubocznych: używaj własnych danych testowych i sprawdzaj użyte działania.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/pl.mp4" %}

**Film:** Tabele decyzyjne w kartach przypisania · 2:30 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Tabele decyzyjne w dwóch krokach** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/pl.mp4#t=0.25)

Tabele decyzyjne decydują, kto zajmuje się dokumentem. W Workflow działają w dwóch krokach. Karta I uruchamia tabelę decyzyjną i zachowuje to, co zwraca. Karty Następnie używają tych wyników, aby przypisać dokument lub utworzyć zadania.

**Sukces, Niespełniony warunek lub Błąd** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/pl.mp4#t=25.483)

Karta I kończy się sukcesem, gdy tabela zwraca co najmniej jedno dopasowanie dla dokumentu. Bez dopasowania kończy się jako niespełniony warunek i idzie pomarańczową ścieżką. Bez wybranej tabeli albo gdy tabela nie może działać, kończy się błędem.

**Uruchom tabelę i zapisz wyniki** · [0:48](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/pl.mp4#t=48.583)

Dodaj kartę I Tabela decyzyjna zwraca wyniki i wybierz tabelę decyzyjną. Potem ustaw w niej zapisywanie zwróconych danych. Bez tego karty po niej nie mają z czym pracować.

**Pierwszy użytkownik dostaje dokument, każdy zadanie** · [1:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/pl.mp4#t=65.416)

Na ścieżce sukcesu karta Następnie, która przypisuje według pierwszego zwróconego użytkownika, daje dokument pierwszemu użytkownikowi z tabeli. Każdy zwrócony użytkownik, także pierwszy, dostaje zadanie lub powiadomienie. Nadaj zadaniu tytuł, opis i priorytet i wybierz, czy wysłać też e-mail. Grupy w wynikach są ignorowane.

**Bez pól: wszystko z tabeli** · [1:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/pl.mp4#t=97.783)

Natomiast karta Przypisz dokument sekwencyjnie do Użytkownika/Grupy na podstawie tabeli decyzyjnej nie ma żadnych pól. Bierze użytkowników i grupy z tabeli, każdego z priorytetem z tabeli lub domyślnym. Na końcu przebiegu dokument dostaje wpis z najniższym numerem priorytetu, chyba że inna karta już przypisała go bezpośrednio.

**Która karta do jakiego zadania** · [2:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/pl.mp4#t=125.816)

Krótko: aby dać dokument jednej osobie i poinformować pozostałych, użyj karty pierwszego użytkownika. Aby tabela decydowała o wszystkim, także o priorytetach, użyj karty sekwencyjnej bez pól. Aby tylko tworzyć zadania, użyj karty zadań dla wyników tabeli decyzyjnej.

</details>

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
