---
description: "P1: przypisanie, zadanie i zatwierdzanie sekwencyjne"
---

# P1: przypisanie, zadanie i zatwierdzanie sekwencyjne

**Przypisanie dokumentu** określa bieżącą odpowiedzialność. **Zadanie** jest osobną pracą. **Powiadomienie** informuje. Żadne z nich nie jest jeszcze osobistym zatwierdzeniem. Przypisanie grupy nie dowodzi też zgody wszystkich jej członków.

Karty sekwencyjne zbierają odbiorców i kolejność zatwierdzania. Przykład używa A z kolejnością 10 i B z 20. Sprawdzona finalizacja zaczyna od mniejszej wartości. Przejście do B wynika z przetworzonej decyzji użytkownika w obiegu zatwierdzania; węzeł Wait w projektancie nie wykonuje go samodzielnie.

Unikaj bezpośredniego przypisania w tym samym wykonaniu, jeśli oczekujesz pierwszego odbiorcy sekwencyjnego: finalizacja może pominąć pierwsze przypisanie po wcześniejszym bezpośrednim przypisaniu dokumentu. Konfiguruj `task_type`, priorytet, odbiorcę i `send_email` osobno. Wyłącz e-mail podczas ćwiczeń.

Odbiór biznesowy obejmuje A→zatwierdzenie→B→zatwierdzenie, odrzucenie przez A, brak odbiorcy i ponowne wyzwolenie. Odrzucenie musi zablokować końcowy eksport; nierozwiązany odbiorca nie może wyglądać na zakończone zatwierdzenie. Sprawdzaj osobno odpowiedzialność i zadania. Symulacja nie dowodzi rzeczywistego przekazania między użytkownikami.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4" %}

**Film:** Dwuetapowe zatwierdzanie z tabelami decyzyjnymi · 4:00 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Dwa etapy, dwie tabele decyzyjne** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=0.25)

Dwuetapowe zatwierdzanie: najpierw zatwierdzający zwróceni przez tabelę decyzyjną, potem grupa końcowa, która zawsze jest ostatnia. Dwie tabele decyzyjne: jedna zwraca użytkowników, druga grupę.

**Tabela: kto, typ zwracanej wartości i priorytet** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=17.65)

Do przypisywania po kolei skonfiguruj tabelę decyzyjną tak: każdy wiersz zwraca, kto otrzymuje dokument, z typem zwracanej wartości Użytkownik lub Grupa, oraz priorytet. Karta przypisania przyjmuje tylko wartości typu, na który jest ustawiona, a najniższy priorytet jest pierwszy. Wiersze bez priorytetu dostają priorytet z karty.

**Jeden łańcuch: tabela, przypisanie, tabela, przypisanie** · [0:48](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=48.983)

Umieść każdą kartę przypisania zaraz za jej własną tabelą decyzyjną, w jednym łańcuchu: tabela, przypisanie, tabela, przypisanie. Obie tabele zapisują zwrócone dane.

**Każde przypisanie zaraz po swojej tabeli** · [1:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=66.95)

Workflow przechowuje tylko ostatni wynik tabeli decyzyjnej. Każda karta przypisania odczytuje go w chwili uruchomienia, więc musi zadziałać, zanim następna tabela go zastąpi.

**Priorytety ustalają kolejność** · [1:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=82.116)

Kolejność zatwierdzeń wynika z priorytetów, nie z kolejności kart: najniższa liczba dostaje dokument pierwsza. Daj grupie końcowej najwyższą liczbę.

**Test: zatwierdzający, potem grupa** · [1:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=97.75)

Test pokazuje sukces każdej karty. Pierwsza karta przypisania ustawia w kolejce dwóch zatwierdzających, druga grupę końcową. Na końcu przebiegu ostatnie przypisanie przekazuje dokument pierwszemu z nich.

**Obok siebie: nie działa** · [2:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=124.95)

Ten układ nie działa. Dwie ścieżki obok siebie wyglądają tak samo, ale Workflow wykonuje je krok po kroku: najpierw obie tabele, potem obie karty przypisania.

**Zatwierdzający znikają - bez błędu** · [2:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=140.35)

Test uruchamia najpierw obie tabele, potem obie karty przypisania. Obie odczytują wynik drugiej tabeli: grupa trafia do kolejki dwa razy, a zatwierdzający znikają. Każda karta nadal pokazuje sukces, nic cię nie ostrzega. Użyj łańcucha.

**Stały ostatni zatwierdzający: priorytet 99** · [2:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=169.15)

W Standard Workflow stały zatwierdzający może zawsze być ostatni: przypisz użytkowników z tabeli, a potem dodaj kartę, która przypisuje jednego użytkownika z wysokim priorytetem, na przykład 99.

**Niższe priorytety w tabeli** · [3:09](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=189.35)

Priorytety tabeli muszą być niższe niż ta liczba. Jeśli tabela nikogo nie znajdzie, Workflow zatrzymuje się na karcie tabeli i nikt nie zostaje przypisany. Użytkownik zwrócony przez obie zostaje zapytany dwa razy.

**Sprawdź w teście** · [3:31](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v2/pl.mp4#t=211.55)

Standard Workflow testuje jedną kartę naraz, więc przetestuj te same karty w Advanced Workflow. Pierwsza karta przypisania ustawia w kolejce zatwierdzających z tabeli, druga dodaje stałego użytkownika. Priorytety stawiają go na końcu.

</details>

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
