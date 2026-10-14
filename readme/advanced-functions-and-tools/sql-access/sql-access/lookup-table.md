# Lookup table

## Tabela `public.lookup_table`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `data_key`: internal
* `rec_id`: internal
* `prop_name`: internal
* `prop_value`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `prop_value_clean`: internal
* `version`: integer
* `deleted_on`: timestamp with time zone
* `sub_org_id`: internal

### Analiza i opis

## Dokumentacja techniczna tabeli `public.lookup_table`

### Wprowadzenie

Tabela `public.lookup_table` służy do przechowywania metadanych o różnych właściwościach powiązanych z danymi organizacji. Prawdopodobnie pełni funkcję magazynu klucz-wartość dla różnych atrybutów dotyczących klientów lub innych podmiotów w organizacji. Tabela rejestruje informacje takie jak nazwy właściwości, wartości i kontekst (np. organizacja i podorganizacja, do których należą), a także informacje audytowe, takie jak znaczniki czasu utworzenia i modyfikacji.

### Opis kolumn

#### `id`

* **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdy wpis.

#### `org_id`

* **Znaczenie**: Identyfikator organizacji, do której należą dane.
* **Rola**: Klucz obcy, prawdopodobnie odwołujący się do tabeli organizacji.
* **Typowa zawartość**: Ciąg UUID reprezentujący organizację.

#### `data_key`

* **Znaczenie**: Klucz reprezentujący konkretny zbiór danych lub kontekst w organizacji.
* **Rola**: Identyfikator kontekstowy do grupowania powiązanych właściwości.
* **Typowa zawartość**: Ciąg alfanumeryczny wskazujący kategorię, taki jak `customer_amier`.

#### `rec_id`

* **Znaczenie**: Identyfikator konkretnego rekordu w zbiorze danych.
* **Rola**: Identyfikator kontekstowy, prawdopodobnie klucz obcy do innej tabeli.
* **Typowa zawartość**: Ciąg alfanumeryczny lub null dla rekordów bez konkretnego identyfikatora.

#### `prop_name`

* **Znaczenie**: Nazwa właściwości lub atrybutu.
* **Rola**: Pole opisowe wskazujące, co reprezentuje wartość właściwości.
* **Typowa zawartość**: Ciągi znaków takie jak 'Kundennummer', 'Versandanschrift', 'Kundenname' itp.

#### `prop_value`

* **Znaczenie**: Wartość właściwości opisanej przez `prop_name`.
* **Rola**: Pole opisowe zawierające faktyczne dane lub wartość.
* **Typowa zawartość**: Ciągi znaków lub liczby reprezentujące wartość właściwości.

#### `created_by`

* **Znaczenie**: Identyfikator użytkownika lub systemu, który utworzył rekord.
* **Rola**: Pole techniczne do celów audytowych.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

#### `created_on`

* **Znaczenie**: Znacznik czasu wskazujący, kiedy rekord został utworzony.
* **Rola**: Pole techniczne do celów audytowych.
* **Typowa zawartość**: Data i godzina z informacją o strefie czasowej.

#### `last_modified_on`

* **Znaczenie**: Znacznik czasu wskazujący, kiedy rekord był ostatnio modyfikowany.
* **Rola**: Pole techniczne do celów audytowych.
* **Typowa zawartość**: Data i godzina z informacją o strefie czasowej, potencjalnie null, jeśli rekord nie był modyfikowany.

#### `is_deleted`

* **Znaczenie**: Flaga wskazująca, czy rekord został usunięty.
* **Rola**: Pole techniczne wskazujące usunięcie logiczne.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

#### `prop_value_clean`

* **Znaczenie**: Oczyszczona lub przetworzona wersja `prop_value`.
* **Rola**: Pole opisowe do przechowywania znormalizowanej lub ustandaryzowanej wartości.
* **Typowa zawartość**: Podobna do `prop_value`, potencjalnie null, jeśli nie dotyczy.

#### `version`

* **Znaczenie**: Numer wersji rekordu.
* **Rola**: Pole techniczne do kontroli wersji.
* **Typowa zawartość**: Liczba całkowita reprezentująca wersję rekordu.

#### `deleted_on`

* **Znaczenie**: Znacznik czasu wskazujący, kiedy rekord został oznaczony jako usunięty.
* **Rola**: Pole techniczne do celów audytowych.
* **Typowa zawartość**: Data i godzina z informacją o strefie czasowej, potencjalnie null, jeśli rekord nie został usunięty.

#### `sub_org_id`

* **Znaczenie**: Identyfikator podorganizacji w ramach organizacji głównej.
* **Rola**: Klucz obcy, potencjalnie odwołujący się do tabeli podorganizacji.
* **Typowa zawartość**: Ciąg UUID reprezentujący podorganizację, potencjalnie null, jeśli nie dotyczy.
