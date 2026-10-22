---
description: "Diagnozowanie workflow na podstawie zdarzeń, wejścia, wybranej ścieżki i rzeczywistych wyników."
---

# Systematyczna diagnostyka problemów workflow

Zacznij od jednego dotkniętego problemem wykonania. Zanotuj organizację i środowisko, nazwę i zapisaną rewizję workflow, dokument, czas i strefę oraz dokładny komunikat węzła. W odpowiedziach testowych użyj też `execution_id`. Nie umieszczaj kluczy dostępu ani niechronionych danych klientów we współdzielonych dowodach.

## Od objawu do sprawdzenia

| Objaw | Poszukiwany dowód | Korekta i ponowny test |
| --- | --- | --- |
| Brak wykonania | Licencja, moduł, aktywność, filtry czasu i zdarzenie | Popraw wejście i filtry; powtórz prawdziwe zdarzenie. Ręczny Start go nie dowodzi. |
| Szare działanie | Wynik poprzednika i połączone wyjście | Śledź faktyczną ścieżkę. Pominięty węzeł sam nie zakończył się błędem. |
| Pomarańczowy warunek | Odczytany klucz, typ, wartość i operator | Odróżnij wynik negatywny od błędu. Testuj poniżej, na i powyżej granicy. |
| Czerwony węzeł | Pierwszy błąd i wymagane dane | Popraw dane lub konfigurację; powtórz przypadek błędny i pozytywny. |
| Wait ALL nie kontynuuje | Każde źródło i podłączone wyjście | Nie wymagaj jednocześnie wykluczających się ścieżek. Wykaż możliwy przebieg dla każdego wymaganego źródła. |
| Podwójne zadania lub eksporty | Powtórzenia, zdarzenia, statusy i Run Workflow | Ogranicz warunki i przejścia; wykonaj ten sam przypadek dwukrotnie. Sprawdź ochronę przed współbieżnością w procesie odbiorcy. |
| Zmienna wpływa na inne workflow | Wspólna zmienna organizacji | Sprawdź zależności. Zapis jest niezależny od canvas; ponownie przetestuj dotknięte workflow. |
| Test zdany bez efektu | Co porównano lub zasymulowano? | Sprawdź przypisanie na dokumencie, zadanie w jego obszarze i odbiór u celu. Sam status nie wystarcza. |
| Eksport rozpoczęty bez odbioru | Historia, odpowiedź i dane odbiorcy | Zdiagnozuj przed powtórzeniem; ustal, czy pierwsze żądanie zostało już przetworzone. |

## Interpretacja komunikatów

W [przykładzie Advanced](advanced-workflow-case-study.md) brak kwoty prowadzi czerwonym wyjściem do korekty. Obsługa i OR mogą zakończyć się sukcesem, podczas gdy całość zachowuje pierwotny błąd. Normalnie fałszywy warunek kwoty wybiera pomarańczowy i może pomyślnie zakończyć ścieżkę standardową.

Dwa połączenia z jednego źródła nie są dwiema niezależnymi akceptacjami. Scalenia oceniają podłączone wyniki źródeł. Sprawdź cały przepływ: test częściowy od środkowego węzła może pominąć potrzebnych poprzedników.

## Dowód poprawki

1. Zachowaj pierwotny problem i oczekiwanie biznesowe.
2. Zmień celowo dane lub konfigurację. Zmieniaj oczekiwania wyłącznie po zmianie wymagania.
3. Powtórz błąd, przypadek pozytywny i istotne granice z [pakietem](workflow-training-kit.md).
4. Zapisz regułę i osobno sprawdź aktywację.
5. Porównaj nowe prawdziwe wykonanie ze starym. Dawne logi nadal opisują pierwotną rewizję.

Zapisz przyczynę, poprawkę, wykazany wynik i pozostałe ograniczenia. Oddziel oczekiwanie od wykonania: długi czas łączny sam nie wskazuje wolnego węzła.

## WF-04: Ćwiczenie i odbiór

Zacznij od invalid-number. Zachowaj pierwszy błąd amount i wynik error. Powtórz z above, porównaj nowe dowody i zachowaj stary zapis. Udana obsługa błędu nie wystarcza.

[Ścieżka nauki](workflow-learning-path.md)

## Powtarzanie testu karty z jawnym zakresem

W sprawdzonym projektancie Dev powtórzenie testu uruchomionego od wybranego węzła przełączyło zakres na cały graf. Ponownie otwórz test z menu kontekstowego właściwej karty i sprawdź rzeczywiście odwiedzone węzły. Wynik obejmujący sześć węzłów nie dowodzi osobnego testu pustej wartości. Licznik nieudanych akcji może uwzględniać niespełniony warunek: czytaj także wyjście, log i wynik całości.
