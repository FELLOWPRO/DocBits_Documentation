# Preferencje TF-IDF

## Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `tfidf_id`: internal
* `pref_key`: internal
* `pref_value`: text
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_by`: internal
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `deleted_by`: internal
* `deleted_on`: znacznik czasu ze strefą czasową
* `supplier_id`: internal

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.tfidf_preferences`

## Wprowadzenie

Tabela `public.tfidf_preferences` służy prawdopodobnie do przechowywania preferencji związanych z konfiguracjami lub modelami TF-IDF (Term Frequency-Inverse Document Frequency). Zawiera informacje o konkretnych preferencjach ustawionych przez organizacje, w tym klucze preferencji i odpowiadające im wartości, a także metadane dotyczące czynności tworzenia, modyfikowania i usuwania.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID reprezentujący unikalny identyfikator wpisu preferencji.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z preferencją.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID łączący preferencję z konkretną organizacją.

### tfidf_id
- **Znaczenie**: Identyfikator konkretnej konfiguracji lub modelu TF-IDF.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID reprezentujący powiązaną konfigurację TF-IDF.

### pref_key
- **Znaczenie**: Klucz lub nazwa ustawienia preferencji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków reprezentujący nazwę preferencji, taki jak 'USE_ETEXT_IF_AVAILABLE' lub 'AI_MODEL'.

### pref_value
- **Znaczenie**: Wartość powiązana z kluczem preferencji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków lub wartość tekstowa odpowiadająca kluczowi preferencji, np. 'true', 'false' lub 'Full'.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył wpis preferencji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika-twórcy.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia wpisu preferencji.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący datę i godzinę utworzenia.

### last_modified_by
- **Znaczenie**: Identyfikator użytkownika, który ostatnio zmodyfikował wpis preferencji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: UUID reprezentujący identyfikator użytkownika, który ostatni zmodyfikował wpis, jeśli dotyczy.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji wpisu preferencji.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową pokazujący datę i godzinę ostatniej modyfikacji.

### is_deleted
- **Znaczenie**: Flaga wskazująca, czy wpis preferencji został oznaczony jako usunięty.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna; `True`, jeśli wpis jest usunięty, w przeciwnym razie `False`.

### deleted_by
- **Znaczenie**: Identyfikator użytkownika, który oznaczył wpis preferencji jako usunięty.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: UUID reprezentujący identyfikator użytkownika, który usunął wpis, jeśli dotyczy.

### deleted_on
- **Znaczenie**: Znacznik czasu oznaczenia wpisu preferencji jako usuniętego.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący, kiedy wpis został usunięty.

### supplier_id
- **Znaczenie**: Identyfikator dostawcy powiązanego z preferencją.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID reprezentujący dostawcę powiązanego z preferencją.

Niniejsza dokumentacja zawiera szczegółowy przegląd przeznaczenia i struktury tabeli `public.tfidf_preferences`, pomagając programistom zrozumieć, jak skutecznie korzystać z tych danych.
```
