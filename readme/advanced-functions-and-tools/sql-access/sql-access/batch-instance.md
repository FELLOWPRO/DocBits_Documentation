# Batch instance

## Tabela `public.batch_instance`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analiza i opis

## Dokumentacja tabeli: `public.batch_instance`

### Wprowadzenie

Tabela `public.batch_instance` służy do przechowywania informacji o poszczególnych instancjach wsadów (batch) w organizacji. Zawiera kluczowe metadane każdej instancji, w tym jej unikalny identyfikator, organizację, do której należy, oraz szczegóły dotyczące utworzenia i modyfikacji. Tabela jest niezbędna do śledzenia cyklu życia instancji wsadów i zarządzania nimi, prawdopodobnie w aplikacji zajmującej się przetwarzaniem wsadowym.

### Kolumny

#### `id`

* **Znaczenie**: Ta kolumna przechowuje unikalny identyfikator każdej instancji wsadu.
* **Rola**: Klucz główny (`id`).
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdą instancję wsadu, np. `'e9aa9ad7-6c36-4d7c-b31c-6e10bb8fbd87'`.

#### `org_id`

* **Znaczenie**: Ta kolumna przechowuje identyfikator organizacji powiązanej z instancją wsadu.
* **Rola**: Klucz obcy (`org_id`).
* **Typowa zawartość**: Ciąg UUID reprezentujący organizację, np. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### `created_by`

* **Znaczenie**: Ta kolumna wskazuje użytkownika lub podmiot systemowy, który utworzył instancję wsadu.
* **Rola**: Prawdopodobnie klucz obcy odwołujący się do tabeli użytkowników lub podobnej.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator twórcy, np. `1`.

#### `created_on`

* **Znaczenie**: Ta kolumna zapisuje znacznik czasu utworzenia instancji wsadu.
* **Rola**: Pole techniczne do celów audytu i śledzenia.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową, np. `2021-09-22 10:55:59.755627+00`.

#### `last_modified_on`

* **Znaczenie**: Ta kolumna zawiera znacznik czasu ostatniej modyfikacji instancji wsadu.
* **Rola**: Pole techniczne do audytu zmian.
* **Typowa zawartość**: Zazwyczaj null lub znacznik czasu ze strefą czasową, jeśli dokonano modyfikacji.

#### `is_deleted`

* **Znaczenie**: Ta kolumna wskazuje, czy instancja wsadu została oznaczona jako usunięta.
* **Rola**: Pole techniczne służące do miękkiego usuwania.
* **Typowa zawartość**: Wartość logiczna, zazwyczaj `False`, jeśli instancja jest aktywna, np. `False`.

Niniejsza dokumentacja zawiera kompleksowy przegląd tabeli `public.batch_instance` wraz ze szczegółowym opisem przeznaczenia i struktury każdej kolumny, co jest kluczowe dla programistów pracujących z tym modelem danych.
