# Konfiguracja pola wyszukiwania

## Tabela `public.lookup_field_configuration`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `lookup_rec_id`: internal
* `field_id`: internal
* `lookup_field`: internal
* `is_searchable`: boolean
* `parent_field_id`: internal
* `auto_trigger`: boolean
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `deleted_on`: znacznik czasu ze strefą czasową
* `search_operator`: internal
* `last_modified_by`: internal
* `deleted_by`: internal

### Analiza i opis

## Dokumentacja tabeli: `public.lookup_field_configuration`

### Wprowadzenie

Tabela `public.lookup_field_configuration` jest prawdopodobnie tabelą konfiguracyjną służącą do definiowania i zarządzania polami wyszukiwania (lookup) w aplikacji. Zawiera metadane każdego pola, takie jak jego identyfikator, powiązana organizacja, możliwość wyszukiwania i informacje audytowe. Tabela ta jest prawdopodobnie częścią większego systemu zarządzania dynamicznymi lub definiowanymi przez użytkownika polami, umożliwiającego złożone zapytania i konfigurację.

### Opis kolumn

#### `id`

* **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdy wpis konfiguracji.

#### `org_id`

* **Znaczenie**: Identyfikator organizacji, z którą powiązana jest ta konfiguracja.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID reprezentujący organizację.

#### `lookup_rec_id`

* **Znaczenie**: Identyfikator konkretnego rekordu wyszukiwania, którego dotyczy ta konfiguracja.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID odnoszący się do konkretnego rekordu wyszukiwania.

#### `field_id`

* **Znaczenie**: Identyfikator konfigurowanego pola.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID odnoszący się do konkretnego pola.

#### `lookup_field`

* **Znaczenie**: Nazwa lub etykieta konfigurowanego pola.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący nazwę pola, np. "address\_1" lub "taxratefree".

#### `is_searchable`

* **Znaczenie**: Wskazuje, czy pole może być uwzględniane w operacjach wyszukiwania.
* **Rola**: Flaga konfiguracji.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

#### `parent_field_id`

* **Znaczenie**: Identyfikator pola nadrzędnego, jeśli istnieje.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID lub `None`, jeśli pole nadrzędne nie istnieje.

#### `auto_trigger`

* **Znaczenie**: Określa, czy konfiguracja pola ma automatycznie wyzwalać określone akcje.
* **Rola**: Flaga konfiguracji.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

#### `created_by`

* **Znaczenie**: Identyfikator użytkownika, który utworzył wpis konfiguracji.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

#### `created_on`

* **Znaczenie**: Znacznik czasu utworzenia wpisu konfiguracji.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej.

#### `last_modified_on`

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji wpisu konfiguracji.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej lub `None`, jeśli wpis nigdy nie był modyfikowany.

#### `is_deleted`

* **Znaczenie**: Wskazuje, czy wpis konfiguracji został oznaczony jako usunięty.
* **Rola**: Flaga miękkiego usuwania.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

#### `deleted_on`

* **Znaczenie**: Znacznik czasu oznaczenia wpisu konfiguracji jako usuniętego.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej lub `None`, jeśli wpis nie został usunięty.

#### `search_operator`

* **Znaczenie**: Definiuje operator wyszukiwania używany dla pola.
* **Rola**: Pole konfiguracji.
* **Typowa zawartość**: Ciąg znaków, np. "contains", wskazujący typ operacji wyszukiwania.

#### `last_modified_by`

* **Znaczenie**: Identyfikator użytkownika, który ostatnio zmodyfikował wpis konfiguracji.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Ciąg UUID lub `None`, jeśli wpis nigdy nie był modyfikowany.

#### `deleted_by`

* **Znaczenie**: Identyfikator użytkownika, który oznaczył wpis jako usunięty.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Ciąg UUID lub `None`, jeśli wpis nie został usunięty.

Niniejsza dokumentacja zawiera szczegółowy opis struktury i przeznaczenia każdej kolumny w tabeli `public.lookup_field_configuration`, dając programistom pełny obraz tego, jak pola wyszukiwania są konfigurowane i zarządzane w systemie.
