# Dokument testu automatycznego

## Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `doc_id`: wewnętrzne
* `doc_type`: typ DOC
* `extracted_data`: text
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `filename`: wewnętrzne

## Analiza i opis

```markdown
# Dokumentacja tabeli: `public.auto_test_document`

## Wprowadzenie

Tabela `public.auto_test_document` służy do przechowywania metadanych i wyników ekstrakcji z przetwarzania dokumentów w organizacji. Tabela zawiera informacje o dokumentach, ich typach oraz danych z nich wyodrębnionych. Obejmuje pola do identyfikacji dokumentu, metadane przetwarzania i flagi statusu, które są niezbędne do zarządzania przepływami pracy dokumentów i zapewnienia integralności danych.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego wpisu dokumentu w tabeli.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID.
- **Uwaga**: Służy jako unikalny identyfikator rekordów i zapewnia, że każdy wpis jest odrębny.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z dokumentem.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID.
- **Uwaga**: Łączy dokument z konkretną organizacją w systemie.

### doc_id
- **Znaczenie**: Identyfikator przetwarzanego dokumentu.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID.
- **Uwaga**: Służy do powiązania wyodrębnionych danych z dokumentem źródłowym.

### doc_type
- **Znaczenie**: Typ lub kategoria dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków, np. "MEDI_ORDER".
- **Uwaga**: Pomaga kategoryzować dokumenty na potrzeby przetwarzania i analizy.

### extracted_data
- **Znaczenie**: Struktura JSON zawierająca szczegółowe dane wyodrębnione z dokumentu.
- **Rola**: Pole danych.
- **Typowa zawartość**: Tekst JSON z polami, wartościami i metadanymi ekstrakcji.
- **Uwaga**: Przechowuje wyniki procesu ekstrakcji danych z dokumentu.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył rekord dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.
- **Uwaga**: Pozwala śledzić, który użytkownik wprowadził dokument do systemu.

### created_on
- **Znaczenie**: Znacznik czasu wskazujący, kiedy utworzono rekord dokumentu.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Data i godzina wraz z informacją o strefie czasowej.
- **Uwaga**: Przydatne do audytu i śledzenia cyklu życia dokumentu.

### last_modified_on
- **Znaczenie**: Znacznik czasu wskazujący ostatnią modyfikację rekordu dokumentu.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Data i godzina wraz z informacją o strefie czasowej.
- **Uwaga**: Pomaga śledzić zmiany i aktualizacje rekordu dokumentu.

### is_deleted
- **Znaczenie**: Flaga wskazująca, czy rekord dokumentu został oznaczony jako usunięty.
- **Rola**: Pole statusu.
- **Typowa zawartość**: Wartość logiczna.
- **Uwaga**: Umożliwia miękkie usuwanie rekordów (soft delete), co pozwala w razie potrzeby je odzyskać.

### filename
- **Znaczenie**: Nazwa pliku powiązanego z dokumentem.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków, np. "7.pdf".
- **Uwaga**: Stanowi odwołanie do fizycznego pliku powiązanego z wpisem dokumentu.

```
