# Poprawianie błędu OCR w numerze zamówienia

Trzecim znakiem `06O123` jest **litera O**. Jeżeli ekstrakcja zwraca `060123`, można poprawić ten znany wzorzec za pomocą warunkowej transformacji prefiksu, bez własnego skryptu.

## Konfigurowanie poprawki prefiksu

1. Otwórz **Ustawienia → Typy dokumentów → koło zębate → Reguły transformacji → Zarządzaj regułami transformacji**. Administrator organizacji musi włączyć funkcję dla wybranego typu.
2. Utwórz regułę **pola nagłówka** z **Numerem zamówienia (`Purchase Order`)** jako polem docelowym. Odczytuj z **tego samego pola**.
3. Dla wykonania warunkowego wybierz numer zamówienia, **zaczyna się od** oraz `060`.
4. Usuń początkowy krok usuwania spacji. Dodaj **Afiks → Usuń prefiks → `060`**, a następnie **Afiks → Dodaj prefiks → `06O`**. W drugim kroku wpisz wielką literę O. Warunek ogranicza oba kroki do pasującego prefiksu; pozostałe znaki nie zmieniają się.
5. Sprawdź podgląd, zapisz regułę i otwórz ją ponownie. Przetestuj dokument, zapisz go i wczytaj ponownie, aby zweryfikować zapisany numer zamówienia.

## Sprawdzanie wyniku

| Przykładowe wejście | Oczekiwany wynik | Powód |
| --- | --- | --- |
| `060123` | `06O123` | Pasujący prefiks |
| `060987` | `06O987` | Inna pasująca wartość; końcówka zachowana |
| `06O123` | `06O123` | Już poprawny; warunek niespełniony |
| `160123` | `160123` | Inny prefiks; warunek niespełniony |
| `1060123` | `1060123` | `060` wewnątrz wartości nie jest pasującym prefiksem |

Przykład poprawia znany wzorzec ekstrakcji. Nie potwierdza dokładności OCR, istnienia zamówienia ani poprawnego dopasowania. Stosuj regułę tylko wtedy, gdy konwencja numeracji wymaga `06O`: zmieniony zostałby także prawidłowy prefiks `060`. Dodaj warunki dotyczące dostawcy, jeżeli konwencja obowiązuje tylko wybranych dostawców.

## Dlaczego dwa kroki afiksu?

Obecny edytor wymaga osobnego pola źródłowego dla kroków zależnych od pozycji, takich jak **Znajdź i zamień**, nawet przy włączonej opcji **Uruchom tylko raz na dokument**. Dwa kroki prefiksu działają na tym samym polu. Po poprawce wartość nie zaczyna się już od `060`, więc warunek zapobiega kolejnym zmianom przy ponownym zapisie.
