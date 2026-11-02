# Raport dokumentów

## Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `doc_id`: wewnętrzne
* `doc_type`: typ DOC
* `sub_doc_type`: wewnętrzne
* `time_spent`: wewnętrzne
* `fields_total`: integer
* `fields_correct`: integer
* `checkbox_fields_total`: integer
* `checkbox_fields_correct`: integer
* `table_values_total`: integer
* `table_values_correct`: integer
* `detail_report`: text
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `validated_by`: integer
* `sub_org_id`: wewnętrzne

## Analiza i opis

```markdown
# Dokumentacja tabeli Document Report

## Wprowadzenie
Tabela `public.document_report` służy do przechowywania szczegółowych informacji o raportach z przetwarzania dokumentów, w szczególności dotyczących walidacji i ekstrakcji pól z dokumentów, takich jak faktury. Tabela zawiera metadane dokumentu, metryki przetwarzania i wyniki walidacji, które można wykorzystać do audytu, śledzenia i usprawniania przepływów pracy przetwarzania dokumentów.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego wpisu raportu dokumentu.
- **Rola**: Klucz główny
- **Typowa zawartość**: UUID reprezentujący unikalny raport dokumentu.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z dokumentem.
- **Rola**: Klucz obcy
- **Typowa zawartość**: UUID wskazujący organizację.

### doc_id
- **Znaczenie**: Identyfikator konkretnego dokumentu, którego dotyczy raport.
- **Rola**: Klucz obcy
- **Typowa zawartość**: UUID reprezentujący unikalny dokument.

### doc_type
- **Znaczenie**: Typ przetwarzanego dokumentu, np. faktura.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Wartości takie jak `INVOICE`.

### sub_doc_type
- **Znaczenie**: Podtyp dokumentu zapewniający dalszą kategoryzację.
- **Rola**: Pole opisowe
- **Typowa zawartość**: Może to być `null` lub konkretne podtypy, np. "Cost Invoice".

### time_spent
- **Znaczenie**: Czas poświęcony na walidację dokumentu.
- **Rola**: Pole metryki
- **Typowa zawartość**: Zazwyczaj '0', czas mierzony w predefiniowanych jednostkach.

### fields_total
- **Znaczenie**: Łączna liczba pól wyodrębnionych z dokumentu.
- **Rola**: Pole metryki
- **Typowa zawartość**: Liczba całkowita reprezentująca łączną liczbę pól, np. 13.

### fields_correct
- **Znaczenie**: Liczba pól prawidłowo wyodrębnionych i zwalidowanych.
- **Rola**: Pole metryki
- **Typowa zawartość**: Liczba całkowita reprezentująca poprawnie przetworzone pola, np. 12.

### checkbox_fields_total
- **Znaczenie**: Łączna liczba przetworzonych pól wyboru (checkbox).
- **Rola**: Pole metryki
- **Typowa zawartość**: Zazwyczaj `0`, co wskazuje liczbę przetworzonych pól wyboru.

### checkbox_fields_correct
- **Znaczenie**: Liczba pól wyboru poprawnie zwalidowanych.
- **Rola**: Pole metryki
- **Typowa zawartość**: Zazwyczaj `0`, co wskazuje liczbę poprawnie zwalidowanych pól wyboru.

### table_values_total
- **Znaczenie**: Łączna liczba wartości tabeli wyodrębnionych z dokumentu.
- **Rola**: Pole metryki
- **Typowa zawartość**: Zazwyczaj `0`, co wskazuje łączną liczbę przetworzonych wartości tabeli.

### table_values_correct
- **Znaczenie**: Liczba wartości tabeli poprawnie zwalidowanych.
- **Rola**: Pole metryki
- **Typowa zawartość**: Zazwyczaj `0`, co wskazuje liczbę poprawnie zwalidowanych wartości tabeli.

### detail_report
- **Znaczenie**: Zawartość JSON zapewniająca szczegółowy raport pól dokumentu i ich statusu walidacji.
- **Rola**: Pole opisowe/techniczne
- **Typowa zawartość**: Ciąg JSON zawierający szczegółowe informacje o polach.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia wpisu raportu dokumentu.
- **Rola**: Pole techniczne
- **Typowa zawartość**: Znacznik czasu w UTC, np. `2025-03-10 08:07:24+00`.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji raportu dokumentu.
- **Rola**: Pole techniczne
- **Typowa zawartość**: Znacznik czasu w UTC wskazujący czas ostatniej aktualizacji.

### is_deleted
- **Znaczenie**: Wskazuje, czy raport dokumentu został oznaczony jako usunięty.
- **Rola**: Pole techniczne
- **Typowa zawartość**: Wartość logiczna; `False`, jeśli nie został usunięty.

### validated_by
- **Znaczenie**: Identyfikator użytkownika, który zwalidował dokument.
- **Rola**: Klucz obcy
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator walidatora, np. `1`.

### sub_org_id
- **Znaczenie**: Identyfikator podorganizacji powiązanej z dokumentem.
- **Rola**: Klucz obcy
- **Typowa zawartość**: UUID wskazujący podorganizację.
```
