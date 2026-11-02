# Custom\_classification\_document\_label

## Tabela `public.custom_classification_document_label`

### Kolumny

* `id`: integer
* `org_id`: ID organizacji
* `doc_id`: wewnętrzne
* `label_id`: integer
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean

### Analiza i opis

## Dokumentacja techniczna tabeli `public.custom_classification_document_label`

### Wprowadzenie

Tabela `public.custom_classification_document_label` służy do zarządzania powiązaniami między dokumentami a ich etykietami w organizacji oraz do ich przechowywania. Tabela ułatwia kategoryzowanie i wyszukiwanie dokumentów na podstawie niestandardowych etykiet, zapewniając uporządkowany sposób zarządzania klasyfikacją dokumentów dla różnych potrzeb organizacyjnych.

### Opis kolumn

#### id

* **Znaczenie**: Ta kolumna służy jako unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny
* **Typowa zawartość**: Wartość całkowita jednoznacznie identyfikująca każdy wiersz.
* **Uwaga**: Każdy wpis w tabeli ma odrębny `id`, co zapewnia integralność danych i umożliwia efektywne odwoływanie się do rekordów.

#### org\_id

* **Znaczenie**: Reprezentuje organizację, do której należy powiązanie dokumentu z etykietą.
* **Rola**: Klucz obcy
* **Typowa zawartość**: Ciąg znaków, prawdopodobnie UUID, jednoznacznie identyfikujący organizację.
* **Uwaga**: Zapewnia, że powiązanie dokumentów i etykiet jest ograniczone do właściwego kontekstu organizacyjnego.

#### doc\_id

* **Znaczenie**: Identyfikuje dokument, któremu przypisano etykietę.
* **Rola**: Klucz obcy
* **Typowa zawartość**: Ciąg znaków, prawdopodobnie UUID, jednoznacznie identyfikujący dokument.
* **Uwaga**: Umożliwia powiązanie konkretnych dokumentów z etykietami, a tym samym ich kategoryzowanie.

#### label\_id

* **Znaczenie**: Odnosi się do etykiety przypisanej do dokumentu.
* **Rola**: Klucz obcy
* **Typowa zawartość**: Liczba całkowita odwołująca się do etykiety z osobnej tabeli etykiet.
* **Uwaga**: Ułatwia powiązanie dokumentów z ich etykietami.

#### created\_by

* **Znaczenie**: Identyfikuje użytkownika, który utworzył rekord.
* **Rola**: Klucz obcy (potencjalnie do tabeli użytkowników)
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.
* **Uwaga**: Pozwala śledzić pochodzenie każdego powiązania dokumentu z etykietą na potrzeby audytu i rozliczalności.

#### created\_on

* **Znaczenie**: Wskazuje, kiedy utworzono rekord.
* **Rola**: Pole techniczne
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej.
* **Uwaga**: Dostarcza kontekstu czasowego, kiedy powiązanie dokumentu z etykietą zostało ustanowione.

#### last\_modified\_on

* **Znaczenie**: Zapisuje znacznik czasu ostatniej modyfikacji rekordu.
* **Rola**: Pole techniczne
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej; może mieć wartość `None`, jeśli rekord nigdy nie był modyfikowany.
* **Uwaga**: Przydatne do śledzenia historii zmian powiązań dokumentów z etykietami.

#### is\_deleted

* **Znaczenie**: Oznacza, czy rekord został oznaczony jako usunięty.
* **Rola**: Pole techniczne
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).
* **Uwaga**: Wspiera praktykę miękkiego usuwania, umożliwiając logiczne usunięcie danych bez ich fizycznego kasowania z bazy danych.
