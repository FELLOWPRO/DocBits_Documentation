# Chat Log

## Tabela `public.chat_log`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `supplier_as_org_id`: wewnętrzne
* `message`: wewnętrzne
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `last_modified_by`: wewnętrzne
* `deleted_by`: wewnętrzne
* `chat_type`: wewnętrzne

### Analiza i opis

## Dokumentacja tabeli: `public.chat_log`

### Wprowadzenie

Tabela `public.chat_log` służy do przechowywania historii wiadomości czatu w organizacji. Na podstawie nazw kolumn można wnioskować, że rejestruje szczegóły każdej wiadomości, w tym jej pochodzenie, treść oraz metadane dotyczące utworzenia i modyfikacji. Tabela ta jest prawdopodobnie centralnym elementem aplikacji lub systemów obsługujących logi komunikacji między organizacjami a dostawcami.

### Kolumny

#### id

* **Znaczenie**: Unikalny identyfikator każdej wiadomości czatu w logu.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdy wpis.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z wiadomością czatu.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID reprezentujący organizację.

#### supplier\_as\_org\_id

* **Znaczenie**: Identyfikator dostawcy występującego w czacie jako organizacja.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID reprezentujący organizację dostawcy.

#### message

* **Znaczenie**: Treść wiadomości czatu.
* **Rola**: Pole danych.
* **Typowa zawartość**: Ciąg tekstowy zawierający faktyczną wiadomość wysłaną na czacie.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył wiadomość czatu.
* **Rola**: Klucz obcy (prawdopodobnie odwołuje się do tabeli użytkowników).
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia wiadomości czatu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący dokładny moment utworzenia.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji wiadomości czatu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący, kiedy wiadomość była ostatnio aktualizowana.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy wiadomość czatu została usunięta.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia wiadomości czatu jako usuniętej.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący moment usunięcia. Jeśli wiadomość nie została usunięta, często ustawiona jest domyślna, bardzo odległa data z przeszłości.

#### last\_modified\_by

* **Znaczenie**: Identyfikator użytkownika, który ostatni zmodyfikował wiadomość czatu.
* **Rola**: Klucz obcy (prawdopodobnie odwołuje się do tabeli użytkowników).
* **Typowa zawartość**: Ciąg UUID reprezentujący identyfikator użytkownika.

#### deleted\_by

* **Znaczenie**: Identyfikator użytkownika, który usunął wiadomość czatu.
* **Rola**: Klucz obcy (prawdopodobnie odwołuje się do tabeli użytkowników).
* **Typowa zawartość**: Ciąg UUID reprezentujący identyfikator użytkownika.

#### chat\_type

* **Znaczenie**: Typ lub kategoria wiadomości czatu.
* **Rola**: Pole danych.
* **Typowa zawartość**: Ciąg znaków wskazujący typ czatu, prawdopodobnie kategoryzujący wiadomości (np. 'text', 'image', 'system').

Niniejsza dokumentacja zawiera szczegółowy przegląd struktury tabeli `public.chat_log`, pomagając programistom zrozumieć przeznaczenie każdej kolumny i jej rolę w systemie.
