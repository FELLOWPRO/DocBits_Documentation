---
description: "Konfiguracja kart według nazwy, wersji, wejść, zakresu danych, wyników i skutków."
---

# Zrozumieć i skonfigurować karty workflow

Wybieraj kartę według działania i zakresu danych. **Field is** sprawdza obecność lub pustą wartość; **Docfield is** porównuje wartość. Przypisanie dokumentu, zadanie i powiadomienie mają odmienne skutki. Kategoria nie zastępuje opisu konkretnej wersji karty.

## Co wyjaśnia pełny opis

| Element | Wymagane pytanie |
| --- | --- |
| Tożsamość | Widoczna nazwa, typ techniczny, wersja i rola When/And/Then? |
| Wymagania | Potrzebna licencja, uprawnienia i dane? |
| Wejścia | Typ, wartość, domyślna wartość i dozwolone opcje parametru? |
| Zakres | Pole, wiersz, wszystkie pozycje czy zmienna organizacji? |
| Wyniki | Sukces, fałsz czy błąd? Co odczyta następna karta? |
| Skutki | Zmiany dokumentów, zadań lub systemów zewnętrznych? Co symuluje test? |
| Przykłady | Jaka pełna konfiguracja i wejście dają określony wynik? |
| Granice i wersje | Brak danych, dokładne granice i starsze wersje? |

## Wypełniony przykład: Docfield is

**Typ techniczny:** `condition_docfield_operator_value` · **Wersja:** 2 · **Rola:** And. Wymaga dokumentu ze zdefiniowanym layout i sprawdzanym polem.

| Wejście | Konfiguracja |
| --- | --- |
| Field Name | `total_amount`, techniczny klucz, nie przetłumaczona etykieta |
| Operator | `gt` / Większe niż |
| Field Value | `1000`, bez symbolu waluty |

Karta porównuje pole bieżącego dokumentu ze skonfigurowaną wartością. Nie zmienia statusu, nie tworzy zadania i nie eksportuje. W Advanced prawda wybiera Success, zwykły fałsz Failed Condition, a błąd oceny Error. W Standard niespełniony warunek zatrzymuje liniową sekwencję.

Rzeczywiście sprawdzone przypadki: **1785** → Success; **999** i **1000** → Failed Condition; **1000,01** → Success; brak lub niepoprawna liczba → Error. JSON używa kropki dziesiętnej. Wyniki dotyczą tej konfiguracji liczbowej, nie wszystkich typów i operatorów.

Odróżnij tę kartę od jawnych kart tolerancji. Nie wywodź równości ani operatorów obejmujących granicę wyłącznie z `gt`; sprawdź potrzebną kombinację z własnymi granicami.

## Dalsze kroki

Połącz sukces z weryfikacją, fałsz z przetwarzaniem standardowym i błąd z korektą danych. [Pełny przykład](advanced-workflow-case-study.md) zawiera konfigurację, kolejne karty i rzeczywiste wyniki. [Model wykonania](workflow-execution-model.md) opisuje zapis i aktywację, a [diagnostyka](workflow-troubleshooting.md) pomaga badać inne wyniki.

## WF-05: Ćwiczenie i odbiór

Opisz Run Workflow i kartę PO według jednego planu: parametry, sprawdzone wartości domyślne, ścieżki, skutki i wersje. Zbadaj nieaktywny cel, brak danych i podstawę procentu.

[Ścieżka nauki](workflow-learning-path.md)
