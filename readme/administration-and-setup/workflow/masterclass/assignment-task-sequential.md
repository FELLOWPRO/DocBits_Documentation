---
description: "P1: przypisanie, zadanie i zatwierdzanie sekwencyjne"
---

# P1: przypisanie, zadanie i zatwierdzanie sekwencyjne

**Przypisanie dokumentu** określa bieżącą odpowiedzialność. **Zadanie** jest osobną pracą. **Powiadomienie** informuje. Żadne z nich nie jest jeszcze osobistym zatwierdzeniem. Przypisanie grupy nie dowodzi też zgody wszystkich jej członków.

Karty sekwencyjne zbierają odbiorców i kolejność zatwierdzania. Przykład używa A z kolejnością 10 i B z 20. Sprawdzona finalizacja zaczyna od mniejszej wartości. Przejście do B wynika z przetworzonej decyzji użytkownika w obiegu zatwierdzania; węzeł Wait w projektancie nie wykonuje go samodzielnie.

Unikaj bezpośredniego przypisania w tym samym wykonaniu, jeśli oczekujesz pierwszego odbiorcy sekwencyjnego: finalizacja może pominąć pierwsze przypisanie po wcześniejszym bezpośrednim przypisaniu dokumentu. Konfiguruj `task_type`, priorytet, odbiorcę i `send_email` osobno. Wyłącz e-mail podczas ćwiczeń.

Odbiór biznesowy obejmuje A→zatwierdzenie→B→zatwierdzenie, odrzucenie przez A, brak odbiorcy i ponowne wyzwolenie. Odrzucenie musi zablokować końcowy eksport; nierozwiązany odbiorca nie może wyglądać na zakończone zatwierdzenie. Sprawdzaj osobno odpowiedzialność i zadania. Symulacja nie dowodzi rzeczywistego przekazania między użytkownikami.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `action_assign_doc_to_user_sequential` · v2

Identyfikacja: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identyfikacja: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → Zatwierdź → B → Zatwierdź |
| ASSIGN-02 | A → Odrzuć | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | Ścieżka rezerwowa |
| ASSIGN-04 | RUN-1 → RUN-2 | sprawdź duplikaty |
| ASSIGN-05 | direct + sequential | sprawdź pierwszego odbiorcę |

## Dowody i ograniczenia

Parametry i zachowanie porównano z katalogiem Dev oraz sprawdzonym kodem. Przypadki biznesowe są instrukcją odbioru. W tym rozdziale nie wykonano osobistych zatwierdzeń, rzeczywistych zmian ani dostarczeń.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
