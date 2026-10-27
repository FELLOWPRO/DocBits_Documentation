# Sprawdzanie synchronizacji danych

Ten widok pomaga, gdy brakuje dostawcy, zamówienia lub innych danych podstawowych. Pokazuje zarejestrowany czas synchronizacji każdego typu w bieżącej organizacji, nie zawartość wszystkich importowanych rekordów.

## Kolejne kroki

1. Potwierdź organizację, właściwą podorganizację i firmę źródłową ERP.
2. Otwórz **Ustawienia → Dziennik aktywności → Synchronizacja danych**. Starsze wersje umieszczają widok w ustawieniach dzienników.
3. Znajdź typ w **Data Type** i odczytaj **Last Synchronization Time** według ustawionego formatu daty. Najnowsze aktualizacje są na początku.
4. Porównaj czas ze spodziewaną zmianą w źródle. Aktualizacja dostawców nie dowodzi aktualności zamówień.
5. Wyszukaj brakujący identyfikator w danych podstawowych lub zamówieniach. Porównaj firmę, numer dostawcy/zamówienia i identyfikatory pozycji ze źródłem.
6. Sprawdź kanał importu i dzienniki: wiadomość źródłową, organizację docelową, mapowanie i odpowiedź. Usuń przyczynę w integracji; ten widok nie ma przycisku uruchomienia ani ponowienia.
7. Po poprawnej aktualizacji odśwież widok i ponownie otwórz wyszukiwanie lub dokument. Sprawdź czas oraz rzeczywiste wartości.

## Interpretacja

| Obserwacja | Następna kontrola |
| --- | --- |
| Brak wierszy | Organizacja, konfiguracja importu i zarejestrowane synchronizacje. Pusty widok nie oznacza sukcesu. |
| Jeden typ jest stary | Prześledź ten przepływ niezależnie od pozostałych wierszy. |
| Ostrzeżenie o starych danych | Obecnie może wystąpić bez wierszy lub gdy wszystkie aktualizacje są starsze niż dwa tygodnie. Proces może wymagać znacznie świeższych danych. |
| Świeży czas, brak rekordu | Zakres źródła, identyfikatory, treść, mapowanie i odpowiedź. Czas nie dowodzi kompletności. |

Dla wsparcia zachowaj środowisko, organizację, typ, identyfikator, oczekiwany czas oraz dokładny błąd lub identyfikator śledzenia z odpowiednimi zanonimizowanymi dowodami.

Zobacz [Import danych podstawowych](../../../infor-integration-and-configuration/importing-customer-master-data/README.md), [Dziennik aktywności](README.md) i [Wyszukiwanie danych podstawowych](../document-processing/master-data-lookup.md).
