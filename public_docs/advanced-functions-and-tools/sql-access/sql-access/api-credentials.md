# Dane uwierzytelniające API

## Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `title`: internal
* `credentials_type`: internal
* `credentials_json`: text
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `deleted_on`: znacznik czasu ze strefą czasową
* `last_modified_by`: internal
* `deleted_by`: internal

## Analiza i opis

```markdown
# Dokumentacja tabeli: `public.api_credentials`

## Wprowadzenie

Tabela `public.api_credentials` służy do przechowywania i zarządzania informacjami o danych uwierzytelniających API. Jest kluczowa dla organizacji, które muszą bezpiecznie obsługiwać dane uwierzytelniające API, tak aby różne usługi mogły się ze sobą komunikować przy użyciu właściwych danych. Zawiera informacje o typie danych uwierzytelniających, organizacji, do której należą, oraz metadane dotyczące ich utworzenia i modyfikacji.

## Opisy kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego wpisu w tabeli.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Uniwersalnie unikalny identyfikator (UUID) reprezentujący konkretny zestaw danych uwierzytelniających API.

### org_id
- **Znaczenie**: Identyfikator organizacji, do której należą dane uwierzytelniające.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: UUID łączący z rekordem organizacji w innej tabeli.

### sub_org_id
- **Znaczenie**: Identyfikator podorganizacji w ramach głównej organizacji.
- **Rola**: Klucz obcy (opcjonalny).
- **Typowa zawartość**: Może zawierać UUID łączący z podorganizacją lub `None`.

### title
- **Znaczenie**: Opisowy tytuł danych uwierzytelniających API.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków, np. "supplier_auth", wskazujący cel lub zastosowanie danych uwierzytelniających.

### credentials_type
- **Znaczenie**: Określa typ przechowywanych danych uwierzytelniających.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków, np. "ionapi", wskazujący format lub protokół używany przez dane uwierzytelniające.

### credentials_json
- **Znaczenie**: Obiekt JSON zawierający szczegółowe informacje o danych uwierzytelniających.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Ciąg JSON z różnymi parami klucz-wartość opisującymi parametry uwierzytelniania.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył rekord danych uwierzytelniających.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### created_on
- **Znaczenie**: Znacznik czasu wskazujący, kiedy dane uwierzytelniające zostały utworzone.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość daty i godziny ze strefą czasową, np. `2024-04-08 11:54:55 UTC`.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji danych uwierzytelniających.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość daty i godziny ze strefą czasową lub `None`, jeśli dane nigdy nie były modyfikowane.

### is_deleted
- **Znaczenie**: Flaga wskazująca, czy dane uwierzytelniające są oznaczone jako usunięte.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna, gdzie `False` oznacza aktywne dane uwierzytelniające.

### deleted_on
- **Znaczenie**: Znacznik czasu wskazujący, kiedy dane uwierzytelniające zostały oznaczone jako usunięte.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość daty i godziny ze strefą czasową lub `None`, jeśli dane nie zostały usunięte.

### last_modified_by
- **Znaczenie**: Identyfikator użytkownika, który ostatnio zmodyfikował dane uwierzytelniające.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Ciąg znaków reprezentujący identyfikator użytkownika lub `None`.

### deleted_by
- **Znaczenie**: Identyfikator użytkownika, który oznaczył dane uwierzytelniające jako usunięte.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Ciąg znaków reprezentujący identyfikator użytkownika lub `None`.
```
