# Lookup Configuration

## Tabela `public.lookup_configuration`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `lookup_dataset_name`: internal
* `lookup_name`: internal
* `conflict_handle`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `match_all`: boolean
* `last_modified_by`: internal
* `deleted_by`: internal
* `context`: internal
* `context_detail`: internal

### Analiza i opis

## Dokumentacja techniczna tabeli `public.lookup_configuration`

### Wprowadzenie

Tabela `public.lookup_configuration` służy do przechowywania ustawień konfiguracji różnych operacji wyszukiwania danych (lookup) w organizacji. Zawiera informacje o organizacji, typie dokumentów oraz konkretnych zbiorach danych i nazwach używanych do wyszukiwania. Tabela śledzi również tworzenie i modyfikowanie tych konfiguracji oraz ich bieżący status (aktywna lub usunięta).

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego wpisu konfiguracji wyszukiwania w tabeli.
* **Rola**: Klucz główny, który jednoznacznie identyfikuje każdy wiersz.
* **Typowa zawartość**: Wartości UUID, np. `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Znaczenie**: Reprezentuje organizację powiązaną z konfiguracją wyszukiwania.
* **Rola**: Klucz obcy, odwołujący się do organizacji w innej tabeli.
* **Typowa zawartość**: Wartości UUID wskazujące identyfikatory organizacji, np. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Znaczenie**: Określa typ dokumentu, do którego odnosi się konfiguracja wyszukiwania.
* **Rola**: Pole opisowe wskazujące kontekst konfiguracji.
* **Typowa zawartość**: Ciągi znaków takie jak `'MEDI_ORDER'`, `'INVOICE'` itp.

#### lookup\_dataset\_name

* **Znaczenie**: Nazwa zbioru danych używanego do wykonywania wyszukiwań.
* **Rola**: Pole opisowe służące do identyfikacji zbiorów danych.
* **Typowa zawartość**: Opisowe ciągi znaków, takie jak `'customer_tini'`, `'supplier'`.

#### lookup\_name

* **Znaczenie**: Konkretna nazwa lub alias używany w operacji wyszukiwania.
* **Rola**: Pole opisowe wskazujące nazwę operacyjną.
* **Typowa zawartość**: Ciągi znaków takie jak `'customer_tini'`, `'supplier (copy)'`.

#### conflict\_handle

* **Znaczenie**: Wskazuje strategię obsługi konfliktów podczas wyszukiwania.
* **Rola**: Pole opisowe określające strategię rozwiązywania konfliktów.
* **Typowa zawartość**: Wartości takie jak `'BEST_SCORE'`, `'RETURN_NONE'`.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył konfigurację wyszukiwania.
* **Rola**: Pole techniczne do śledzenia twórcy wpisu.
* **Typowa zawartość**: Wartości całkowite reprezentujące identyfikatory użytkowników, np. `1`.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia konfiguracji wyszukiwania.
* **Rola**: Pole techniczne do śledzenia czasu utworzenia.
* **Typowa zawartość**: Znaczniki czasu, np. `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji konfiguracji wyszukiwania.
* **Rola**: Pole techniczne do śledzenia czasu ostatniej aktualizacji.
* **Typowa zawartość**: Znaczniki czasu, zazwyczaj `None`, jeśli nie modyfikowano.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy konfiguracja wyszukiwania została oznaczona jako usunięta.
* **Rola**: Pole logiczne do śledzenia statusu.
* **Typowa zawartość**: Wartości logiczne, `False` dla aktywnych wpisów.

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia konfiguracji wyszukiwania jako usuniętej.
* **Rola**: Pole techniczne do śledzenia czasu usunięcia.
* **Typowa zawartość**: Często domyślnie data zastępcza, np. `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Znaczenie**: Określa, czy wyszukiwanie ma spełniać wszystkie warunki.
* **Rola**: Pole logiczne ustawień konfiguracji.
* **Typowa zawartość**: Wartości logiczne, zazwyczaj `False`.

#### last\_modified\_by

* **Znaczenie**: Identyfikator użytkownika, który ostatnio zmodyfikował konfigurację wyszukiwania.
* **Rola**: Pole techniczne do śledzenia użytkownika, który ostatnio zaktualizował wpis.
* **Typowa zawartość**: UUID lub identyfikator modyfikującego użytkownika, często `None`.

#### deleted\_by

* **Znaczenie**: Identyfikator użytkownika, który oznaczył konfigurację wyszukiwania jako usuniętą.
* **Rola**: Pole techniczne do śledzenia użytkownika odpowiedzialnego za usunięcie.
* **Typowa zawartość**: UUID lub identyfikator, często `None`.

#### context

* **Znaczenie**: Kontekst, w którym stosowane jest wyszukiwanie, np. sekcja dokumentu.
* **Rola**: Pole opisowe kontekstu operacyjnego.
* **Typowa zawartość**: Ciągi znaków takie jak `'header'`.

#### context\_detail

* **Znaczenie**: Dodatkowe szczegóły dotyczące kontekstu wyszukiwania.
* **Rola**: Pole opisowe z rozszerzonymi informacjami o kontekście.
* **Typowa zawartość**: Często `None`, używane do dodatkowego opisu kontekstu.
