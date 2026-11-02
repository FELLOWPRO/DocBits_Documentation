# Preferencje

## Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `pref_key`: internal
* `pref_value`: text
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `deleted_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `user_id`: integer
* `sub_org_id`: internal

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.preferences`

## Wprowadzenie
Tabela `public.preferences` służy do przechowywania ustawień konfiguracyjnych i preferencji dla różnych jednostek organizacyjnych w systemie. Każdy wpis w tabeli reprezentuje konkretny klucz preferencji i odpowiadającą mu wartość, powiązane z organizacją lub podorganizacją. Dane konfiguracyjne mogą obejmować ustawienia dotyczące numerów VAT, ustawienia ekstrakcji, aktywację modułów i inne.

## Opis kolumn

### id
- **Znaczenie**: Ta kolumna przechowuje unikalny identyfikator każdego wpisu preferencji.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdy wiersz, taki jak `23f3d697-7411-4c95-981d-faf089d266be`.

### org_id
- **Znaczenie**: Ta kolumna przechowuje identyfikator organizacji, z którą powiązana jest preferencja.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID odpowiadający organizacji, podobny do `23f3d697-7411-4c95-981d-faf089d266be`.

### pref_key
- **Znaczenie**: Ta kolumna reprezentuje klucz lub nazwę ustawienia preferencji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciągi znaków reprezentujące klucze konfiguracji, takie jak `VAT_NUMBERS`, `TABLE_EXTRACTION_SETTING`.

### pref_value
- **Znaczenie**: Ta kolumna zawiera wartość preferencji odpowiadającą `pref_key`.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zależy od `pref_key`; przykłady to numery VAT oddzielone przecinkami lub wartości logiczne, takie jak `true` lub `false`.

### created_by
- **Znaczenie**: Ta kolumna wskazuje identyfikator użytkownika, który utworzył wpis preferencji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika, np. `1`.

### created_on
- **Znaczenie**: Ta kolumna rejestruje znacznik czasu utworzenia preferencji.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową, np. `2021-11-09 11:04:18+00`.

### last_modified_on
- **Znaczenie**: Ta kolumna zawiera znacznik czasu ostatniej modyfikacji preferencji.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący czas ostatniej aktualizacji, taki jak `2023-12-04 10:10:26+00`.

### deleted_on
- **Znaczenie**: Ta kolumna zawiera znacznik czasu oznaczenia preferencji jako usuniętej.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Zazwyczaj `null`, chyba że wiersz został oznaczony do usunięcia.

### is_deleted
- **Znaczenie**: Ta kolumna wskazuje, czy preferencja została oznaczona jako usunięta.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna, zazwyczaj `false`.

### user_id
- **Znaczenie**: Ta kolumna przechowuje identyfikator użytkownika powiązanego z preferencją.
- **Rola**: Pole opisowe, potencjalnie klucz obcy.
- **Typowa zawartość**: Liczba całkowita lub `null`, jeśli nie dotyczy.

### sub_org_id
- **Znaczenie**: Ta kolumna identyfikuje podorganizację powiązaną z preferencją.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID lub `null`, jeśli nie dotyczy.

Tabela `public.preferences` zapewnia elastyczny i kompleksowy sposób zarządzania ustawieniami konfiguracyjnymi w różnych jednostkach organizacyjnych, dzięki czemu preferencje mogą być dynamicznie dostosowywane i śledzone w czasie.
```
