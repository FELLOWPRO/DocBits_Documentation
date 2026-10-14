# Document Import log

## Kolumny

* `id`: integer
* `org_id`: ID organizacji
* `sub_org_id`: wewnętrzne
* `original_filename`: wewnętrzne
* `filename`: wewnętrzne
* `imported_on`: wewnętrzne
* `source_type`: wewnętrzne
* `source`: wewnętrzne
* `success`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `import_id`: text
* `extra_data`: text
* `doc_id`: wewnętrzne
* `email_connection_id`: integer
* `subject`: wewnętrzne
* `body`: text
* `sender`: wewnętrzne
* `error_resp`: wewnętrzne
* `source_received_on`: timestamp with time zone

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.document_import_log`

## Wprowadzenie

Tabela `public.document_import_log` służy do rejestrowania szczegółów importu dokumentów do systemu. Zawiera informacje o każdym dokumencie, w tym jego pochodzeniu, statusie importu i powiązanych metadanych. Tabela ta jest niezbędna do śledzenia działań importowych oraz diagnozowania problemów, które mogą wystąpić podczas importu.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego wpisu w logu importu.
- **Rola**: Klucz główny
- **Typowa zawartość**: Kolejne wartości całkowite jednoznacznie identyfikujące każdy rekord.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z importem.
- **Rola**: Klucz obcy
- **Typowa zawartość**: UUID lub podobny unikalny identyfikator tekstowy reprezentujący organizację.

### sub_org_id
- **Znaczenie**: Identyfikator podorganizacji lub działu w ramach organizacji głównej.
- **Rola**: Klucz obcy
- **Typowa zawartość**: UUID lub podobny unikalny identyfikator tekstowy; może mieć wartość `None`, jeśli nie dotyczy.

### original_filename
- **Znaczenie**: Oryginalna nazwa pliku dokumentu w momencie jego przesłania.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Ciąg znaków reprezentujący nazwę pliku, np. `anton_invoice-1.pdf`.

### filename
- **Znaczenie**: Nazwa pliku dokumentu po jego przetworzeniu lub zapisaniu w systemie.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Ciąg znaków reprezentujący nazwę pliku, często identyczny z `original_filename`.

### imported_on
- **Znaczenie**: Data i godzina zaimportowania dokumentu.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Znacznik czasu w formacie ISO 8601.

### source_type
- **Znaczenie**: Typ źródła, z którego zaimportowano dokument.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Ciąg znaków, np. `EMAIL`, wskazujący typ źródła.

### source
- **Znaczenie**: Szczegółowe informacje o źródle importu.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Ciąg znaków opisujący źródło, np. `Email:O365:demo@fellow-digital.de:Tini Test`.

### success
- **Znaczenie**: Wskazuje, czy import zakończył się powodzeniem.
- **Rola**: Pole statusu
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

### created_by
- **Znaczenie**: Identyfikator użytkownika, który zainicjował import.
- **Rola**: Klucz obcy
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### created_on
- **Znaczenie**: Data i godzina utworzenia wpisu w logu importu.
- **Rola**: Pole techniczne
- **Typowa zawartość**: Znacznik czasu ze strefą czasową.

### last_modified_on
- **Znaczenie**: Data i godzina ostatniej modyfikacji wpisu w logu importu.
- **Rola**: Pole techniczne
- **Typowa zawartość**: Znacznik czasu ze strefą czasową; może mieć wartość `None`, jeśli wpis nie był modyfikowany.

### is_deleted
- **Znaczenie**: Wskazuje, czy wpis w logu importu został oznaczony jako usunięty.
- **Rola**: Pole statusu
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

### import_id
- **Znaczenie**: Unikalny identyfikator procesu importu.
- **Rola**: Pole techniczne
- **Typowa zawartość**: Ciąg znaków lub tekst reprezentujący unikalny identyfikator procesu.

### extra_data
- **Znaczenie**: Dodatkowe metadane związane z importem.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Ciąg JSON zawierający dodatkowe dane, takie jak data, nadawca, temat i liczba.

### doc_id
- **Znaczenie**: Identyfikator dokumentu.
- **Rola**: Klucz obcy
- **Typowa zawartość**: UUID lub podobny unikalny identyfikator tekstowy; może mieć wartość `None`.

### email_connection_id
- **Znaczenie**: Identyfikator połączenia e-mail użytego podczas importu.
- **Rola**: Klucz obcy
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator połączenia e-mail; może mieć wartość `None`.

### subject
- **Znaczenie**: Temat wiadomości e-mail, z której zaimportowano dokument.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Ciąg znaków reprezentujący temat wiadomości e-mail.

### body
- **Znaczenie**: Treść wiadomości e-mail, z której zaimportowano dokument.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Tekst zawierający treść wiadomości e-mail; może mieć wartość `None`.

### sender
- **Znaczenie**: Adres e-mail nadawcy dokumentu.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Ciąg znaków zawierający adres e-mail nadawcy.

### error_resp
- **Znaczenie**: Odpowiedź o błędzie lub komunikat w przypadku niepowodzenia importu.
- **Rola**: Pole statusu
- **Typowa zawartość**: Ciąg znaków zawierający szczegóły błędu; może mieć wartość `None`.

### source_received_on
- **Znaczenie**: Data i godzina otrzymania dokumentu ze źródła.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Znacznik czasu ze strefą czasową.

Niniejsza dokumentacja zawiera szczegółowy przegląd tabeli `public.document_import_log` i jej kolumn, które są niezbędne do zrozumienia importu dokumentów w systemie i zarządzania nim.
```
