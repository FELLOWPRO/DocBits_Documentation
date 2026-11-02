# Stan aktywacji skryptu dokumentu

## Tabela `public.document_script_activation_status`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `sort_order`: integer
* `is_active`: boolean
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `script_id`: wewnętrzne

### Analiza i opis

## Dokumentacja tabeli: `public.document_script_activation_status`

### Wprowadzenie

Tabela `public.document_script_activation_status` służy do zarządzania statusem aktywacji skryptów powiązanych z dokumentami w organizacji. Każdy wpis w tabeli odpowiada konkretnemu skryptowi i jego bieżącemu statusowi aktywacji, co potencjalnie pozwala organizacjom kontrolować i porządkować wykonywanie skryptów w odniesieniu do ich dokumentów.

### Opis kolumn

#### id

* **Znaczenie**: Ta kolumna przechowuje unikalny identyfikator każdego wpisu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Uniwersalnie unikalny identyfikator (UUID), np. `c599a3fa-a784-446a-a48e-cf37b95d93cd`.
* **Uwaga**: Zapewnia, że każdy rekord można jednoznacznie zidentyfikować.

#### org\_id

* **Znaczenie**: Reprezentuje identyfikator organizacji.
* **Rola**: Klucz obcy, prawdopodobnie odwołujący się do tabeli organizacji.
* **Typowa zawartość**: UUID identyfikujący organizację, np. `23f3d697-7411-4c95-981d-faf089d266be`.
* **Uwaga**: Łączy status aktywacji skryptu z konkretną organizacją.

#### sort\_order

* **Znaczenie**: Wskazuje kolejność, w jakiej skrypty mają być wykonywane lub wyświetlane.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartości całkowite reprezentujące kolejność, np. `0`.
* **Uwaga**: Może służyć do ustalania priorytetów lub porządkowania skryptów.

#### is\_active

* **Znaczenie**: Oznacza, czy skrypt jest aktualnie aktywny.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartości logiczne, `True` lub `False`.
* **Uwaga**: Określa, czy powiązany skrypt powinien zostać wykonany.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył rekord.
* **Rola**: Klucz obcy, prawdopodobnie odwołujący się do tabeli użytkowników.
* **Typowa zawartość**: Wartość całkowita reprezentująca identyfikator użytkownika, np. `1`.
* **Uwaga**: Rejestruje twórcę rekordu na potrzeby audytu.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia rekordu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina ze strefą czasową, np. `2023-11-20 10:44:14.685170+00:00`.
* **Uwaga**: Dostarcza znacznik czasu utworzenia na potrzeby ewidencji.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina ze strefą czasową lub `None`, jeśli rekord nigdy nie był modyfikowany.
* **Uwaga**: Przydatne do śledzenia zmian w czasie.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy rekord został oznaczony jako usunięty.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartości logiczne, `True` lub `False`.
* **Uwaga**: Umożliwia miękkie usuwanie rekordów bez fizycznego usuwania ich z bazy danych.

#### script\_id

* **Znaczenie**: Identyfikator skryptu powiązanego z rekordem.
* **Rola**: Klucz obcy, prawdopodobnie odwołujący się do tabeli skryptów.
* **Typowa zawartość**: UUID identyfikujący skrypt, np. `4edc8cd7-e1bc-443a-9a23-dc490a09e80b`.
* **Uwaga**: Łączy status aktywacji z konkretnym skryptem.
