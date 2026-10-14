# Document table column

## Kolumny

* `id`: wewnętrzne
* `document_table_id`: wewnętrzne
* `table_name`: wewnętrzne
* `org_id`: ID organizacji
* `column_name`: wewnętrzne
* `column_type`: wewnętrzne
* `title`: wewnętrzne
* `translation_key`: wewnętrzne
* `sort_order`: integer
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.document_table_column`

## Wprowadzenie

Tabela `public.document_table_column` służy do przechowywania metadanych o kolumnach w różnych tabelach związanych z dokumentami, takich jak tabele faktur lub dowodów dostawy. Metadane te obejmują informacje o nazwie, typie i właściwościach każdej kolumny, a także identyfikatory organizacyjne i techniczne. Tabela wspiera dynamiczne generowanie schematów dokumentów w systemie i zarządzanie nimi.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego wpisu kolumny w tabeli.
- **Rola**: Klucz główny.
- **Uwaga**: Zazwyczaj ciąg UUID jednoznacznie identyfikujący wiersz w tej tabeli.

### document_table_id
- **Znaczenie**: Odwołuje się do tabeli zawierającej dokument, którego częścią jest ta kolumna.
- **Rola**: Klucz obcy.
- **Uwaga**: Prawdopodobnie UUID łączący z inną tabelą, w której zdefiniowane są tabele dokumentów.

### table_name
- **Znaczenie**: Nazwa tabeli dokumentu, do której należy ta kolumna.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Nazwy takie jak `INVOICE_TABLE`, `DELIVERY_NOTE_TABLE`.
- **Uwaga**: Ułatwia zrozumienie, do jakiej struktury dokumentu należy kolumna.

### org_id
- **Znaczenie**: Identyfikator organizacji, która jest właścicielem tabeli dokumentu lub zarządza nią.
- **Rola**: Klucz obcy.
- **Uwaga**: Zazwyczaj UUID łączący z jednostką organizacji.

### column_name
- **Znaczenie**: Techniczna nazwa kolumny w tabeli dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Nazwy takie jak `COUNTRY_ORIGIN`, `ORDERED_QUANTITY`.
- **Uwaga**: Reprezentuje faktyczną nazwę pola w tabeli dokumentu.

### column_type
- **Znaczenie**: Opisuje typ danych kolumny.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: `STRING`, `DATE`.
- **Uwaga**: Wskazuje rodzaj danych przechowywanych w kolumnie.

### title
- **Znaczenie**: Czytelny dla człowieka tytuł lub etykieta kolumny.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: `COUNTRY_ORIGIN`, `Ordered Quantity`.
- **Uwaga**: Używany do wyświetlania nazw kolumn w przyjazny dla użytkownika sposób.

### translation_key
- **Znaczenie**: Klucz używany do internacjonalizacji i lokalizacji tytułu kolumny.
- **Rola**: Pole techniczne.
- **Uwaga**: W przykładowych danych jest obecnie puste, co sugeruje opcjonalne użycie.

### sort_order
- **Znaczenie**: Określa kolejność kolumn podczas wyświetlania.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczby całkowite, np. `16`, `5`.
- **Uwaga**: Określa kolejność kolumn w widoku tabeli dokumentu.

### clean_field
- **Znaczenie**: Wskazuje, czy kolumna zawiera oczyszczone dane.
- **Rola**: Flaga logiczna.
- **Typowa zawartość**: `True` lub `False`.
- **Uwaga**: Używana do walidacji danych lub oznaczania statusu ich oczyszczenia.

### alphanumeric_field
- **Znaczenie**: Określa, czy kolumna powinna być traktowana jako pole alfanumeryczne.
- **Rola**: Flaga logiczna.
- **Typowa zawartość**: `True` lub `False`.
- **Uwaga**: Przydatna do walidacji danych wejściowych lub formatowania.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył ten wpis kolumny.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Wartości całkowite, np. `1`, `8`.
- **Uwaga**: Łączy z użytkownikiem lub jednostką systemową odpowiedzialną za utworzenie.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia wpisu kolumny.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartości daty i godziny w UTC.
- **Uwaga**: Przydatne do audytu i śledzenia zmian.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji wpisu kolumny.
- **Rola**: Pole techniczne.
- **Uwaga**: W przykładowych danych ma obecnie wartość `None`, co oznacza, że po utworzeniu nie dokonano żadnych modyfikacji.

### is_deleted
- **Znaczenie**: Wskazuje, czy wpis kolumny został logicznie usunięty.
- **Rola**: Flaga logiczna.
- **Typowa zawartość**: `True` lub `False`.
- **Uwaga**: Pomaga zarządzać miękkim usuwaniem bez fizycznego usuwania danych.

```
