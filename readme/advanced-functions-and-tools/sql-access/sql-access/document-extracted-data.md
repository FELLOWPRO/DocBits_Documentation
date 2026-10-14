# Document extracted data

## Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `doc_id`: wewnętrzne
* `field_name`: wewnętrzne
* `field_value`: wewnętrzne
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `field_type`: wewnętrzne

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.document_extracted_data`

## Wprowadzenie

Tabela `public.document_extracted_data` służy do przechowywania danych wyodrębnionych z różnych dokumentów, prawdopodobnie na potrzeby przetwarzania i analizy dokumentów. Każdy wpis w tabeli odpowiada konkretnemu polu wyodrębnionemu z dokumentu, takiego jak faktura, i zawiera metadane dotyczące procesu ekstrakcji. Tabela ułatwia śledzenie danych dokumentów i zarządzanie nimi, powiązując je z organizacjami i konkretnymi dokumentami.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego wpisu wyodrębnionych danych.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg w formacie UUID jednoznacznie identyfikujący rekord wyodrębnionych danych.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z danymi dokumentu.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg w formacie UUID reprezentujący organizację.

### doc_id
- **Znaczenie**: Identyfikator dokumentu, z którego wyodrębniono dane.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg w formacie UUID reprezentujący dokument.

### field_name
- **Znaczenie**: Nazwa pola wyodrębnionego z dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciągi znaków, takie jak 'invoice_id', 'invoice_date' itp., wskazujące typ wyodrębnionych danych.

### field_value
- **Znaczenie**: Wartość powiązana z wyodrębnionym polem.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciągi znaków reprezentujące różne typy danych, takie jak numery faktur, daty lub kwoty.

### created_by
- **Znaczenie**: Identyfikator użytkownika lub procesu, który utworzył wpis danych.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika lub procesu.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia wpisu danych.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący datę i godzinę utworzenia.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji wpisu danych.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący datę i godzinę ostatniej modyfikacji (może mieć wartość null, jeśli wpis nigdy nie był modyfikowany).

### is_deleted
- **Znaczenie**: Flaga wskazująca, czy wpis danych został oznaczony jako usunięty.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna, gdzie `False` oznacza wpisy aktywne, a `True` wpisy usunięte.

### field_type
- **Znaczenie**: Typ danych przechowywanych w kolumnie `field_value`.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciągi znaków, takie jak 'date', 'AMOUNT', lub null, jeśli typ nie został określony.

Ten ustrukturyzowany model danych umożliwia efektywne przechowywanie i pobieranie danych związanych z dokumentami, wspierając różnorodne zastosowania, od przetwarzania faktur po zarządzanie zgodnością.
```
