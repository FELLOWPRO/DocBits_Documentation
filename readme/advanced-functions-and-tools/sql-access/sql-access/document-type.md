# Typ dokumentu

## Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `document_key`: wewnętrzne
* `document_name`: wewnętrzne
* `title`: wewnętrzne
* `translation_key`: wewnętrzne
* `extraction_type`: wewnętrzne
* `document_type_category`: wewnętrzne
* `has_table`: boolean
* `sort_order`: integer
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean

## Analiza i opis

```markdown
# Tabela: public.document_type

## Wprowadzenie
Tabela `public.document_type` służy do przechowywania informacji o różnych typach dokumentów w organizacji. Zawiera identyfikatory i metadane do kategoryzowania, zarządzania i przetwarzania dokumentów, takie jak klucze dokumentów, nazwy, tytuły, klucze tłumaczeń i inne atrybuty ułatwiające obsługę i wyszukiwanie dokumentów. Tabela rejestruje również tworzenie i modyfikację tych wpisów, obsługując zarówno stany aktywne, jak i usunięte.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego wpisu typu dokumentu.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący wpis typu dokumentu.

### org_id
- **Znaczenie**: Identyfikator organizacji, do której należy typ dokumentu.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID odwołujący się do organizacji.

### document_key
- **Znaczenie**: Unikalny klucz identyfikujący typ dokumentu, potencjalnie używany w systemach przechowywania lub przetwarzania dokumentów.
- **Rola**: Identyfikator.
- **Typowa zawartość**: Ciąg znaków łączący informacje o typie dokumentu z identyfikatorem organizacji.

### document_name
- **Znaczenie**: Wewnętrzna nazwa typu dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków zapisany wielkimi literami, reprezentujący nazwę typu dokumentu.

### title
- **Znaczenie**: Wyświetlany tytuł typu dokumentu w interfejsach użytkownika.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków zapisany w formacie tytułowym, czytelny dla człowieka i opisujący typ dokumentu.

### translation_key
- **Znaczenie**: Klucz używany do lokalizacji tytułu lub nazwy dokumentu na różne języki.
- **Rola**: Obsługa internacjonalizacji.
- **Typowa zawartość**: Ciąg znaków zapisany małymi literami, stanowiący odwołanie dla systemów tłumaczeń.

### extraction_type
- **Znaczenie**: Wskazuje metodę lub proces, za pomocą którego dane są wyodrębniane z dokumentu.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: W przykładowych danych obecnie niewypełnione.

### document_type_category
- **Znaczenie**: Kategoryzuje typ dokumentu w szersze kategorie lub klasyfikacje.
- **Rola**: Pole kategoryzacji.
- **Typowa zawartość**: W przykładowych danych obecnie niewypełnione.

### has_table
- **Znaczenie**: Wskazuje, czy typ dokumentu zawiera dane tabelaryczne.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`) wskazująca obecność danych tabelarycznych.

### sort_order
- **Znaczenie**: Określa kolejność, w jakiej typy dokumentów są sortowane lub wyświetlane.
- **Rola**: Pole sortowania.
- **Typowa zawartość**: Liczba całkowita reprezentująca kolejność sortowania.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył wpis typu dokumentu.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: Liczba całkowita odwołująca się do identyfikatora użytkownika.

### created_on
- **Znaczenie**: Znacznik czasu wskazujący, kiedy utworzono wpis typu dokumentu.
- **Rola**: Pole audytu.
- **Typowa zawartość**: Data i godzina z informacją o strefie czasowej.

### last_modified_on
- **Znaczenie**: Znacznik czasu wskazujący datę ostatniej modyfikacji wpisu typu dokumentu.
- **Rola**: Pole audytu.
- **Typowa zawartość**: Data i godzina z informacją o strefie czasowej, `None`, jeśli wpis nigdy nie był modyfikowany.

### is_deleted
- **Znaczenie**: Wskazuje, czy wpis typu dokumentu został oznaczony jako usunięty.
- **Rola**: Pole statusu.
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`) wskazująca status usunięcia.
```
