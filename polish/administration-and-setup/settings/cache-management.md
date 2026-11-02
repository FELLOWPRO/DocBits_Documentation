# Zarządzanie pamięcią podręczną

<figure><img src="../../.gitbook/assets/cache_management.png" alt="Zarządzanie pamięcią podręczną"><figcaption><p>Strona zarządzania pamięcią podręczną</p></figcaption></figure>

Zarządzanie pamięcią podręczną kontroluje automatyczne czyszczenie pamięci podręcznej dla często używanych danych. Włączenie buforowania poprawia wydajność, ograniczając powtarzające się wywołania API.

## Wyczyść pamięć podręczną

Kliknij przycisk **Clear Cache** (w prawym górnym rogu), aby ręcznie natychmiast unieważnić wszystkie dane z pamięci podręcznej.

## Tabela pamięci podręcznej

| Kolumna | Opis |
|--------|-------------|
| **Obiekt** | Typ danych w pamięci podręcznej (np. Receive Delivery Cache, Purchase Order Cache). |
| **Status** | Przełącznik włączający lub wyłączający buforowanie dla tego obiektu. |
| **TTL** | Czas życia w minutach — jak długo dane z pamięci podręcznej pozostają ważne, zanim zostaną automatycznie odświeżone. Ustaw `0`, aby wyłączyć automatyczne wygasanie. |

## Dostępne pamięci podręczne

| Pamięć podręczna | Opis |
|-------|-------------|
| **Receive Delivery Cache** | Buforuje dane potwierdzeń dostaw używane podczas dopasowywania PO. |
| **Purchase Order Cache** | Buforuje dane zamówień zakupu w celu szybszego wyszukiwania podczas przetwarzania dokumentów. |
| **Task and Notification Cache** | Buforuje liczbę zadań i dane powiadomień wyświetlane w dashboardzie. |
