---
description: "P0: zmiana statusu i ograniczanie ponownych wykonań"
---

# P0: zmiana statusu i ograniczanie ponownych wykonań

**Change Status to** aktualizuje status dokumentu. W wersji 3 `trigger_docflow` steruje żądaniem dalszego przetwarzania workflow. Ustaw go jawnie. Gdy go brakuje, kod przyjmuje `true`; wersje 1/2 nie odczytują tego przełącznika w tej samej ścieżce wykonania. Sprawdź zapisaną wersję karty.

Zacznij od `validated_pending_approval` oraz `trigger_docflow=false`. Status jest opcją techniczną: wymyślone `pending_approval` nie jest zamiennikiem. Advanced Test symuluje aktualizację. Nie dowodzi ani zapisanej zmiany statusu, ani obsługi żądanego kolejnego wykonania.

Ograniczony proces sprawdza status początkowy i znacznik przetwarzania, wykonuje działanie i przechodzi do następnego stanu. Powtórzone zdarzenie nie powinno już spełniać warunku początkowego. Dwa współbieżne wykonania mogą jednak przeczytać ten sam stary znacznik: zadania i cele eksportu wymagają dodatkowej obsługi duplikatów.

Przy odbiorze porównaj pierwsze i drugie rzeczywiste wykonanie: status, żądane dalsze przetwarzanie oraz liczbę zadań lub rekordów docelowych. Nie przełączaj dwóch statusów tylko eksperymentalnie. Zmiana statusu nie udziela zgody, której warunek biznesowy nadal nie jest spełniony.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `staus_change` · v3

Identyfikacja: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | żądane kolejne wykonanie ≠ ukończone |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## Dowody i ograniczenia

Wybrane wyniki kart i węzłów sprawdzono na danych syntetycznych w Advanced Test. Odpowiedzi są w pakiecie. Działania dokumentalne są symulowane i nie dowodzą zapisanego wykonania ani zewnętrznego dostarczenia.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
