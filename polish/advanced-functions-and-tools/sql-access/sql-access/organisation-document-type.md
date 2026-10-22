# Typ dokumentu organizacji

## Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `document_type_id`: internal
* `document_type_key`: internal
* `document_locale`: internal
* `classification_method`: internal
* `is_active`: boolean
* `extraction_type`: internal
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `sub_org_id`: internal

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.organisation_document_type`

## Wprowadzenie

Tabela `public.organisation_document_type` służy do zarządzania i przechowywania informacji o różnych typach dokumentów powiązanych z organizacjami. Obejmuje to szczegóły, takie jak klucz typu dokumentu, ustawienia regionalne, metody klasyfikacji oraz status typu dokumentu (aktywny, usunięty itp.). Wydaje się pełnić rolę mapowania między organizacjami a typami dokumentów, których używają lub którymi zarządzają, wraz z metadanymi dotyczącymi tych dokumentów.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący wpis typu dokumentu.
- **Uwaga**: Niezbędny do odróżnienia poszczególnych rekordów.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z typem dokumentu.
- **Rola**: Klucz obcy, prawdopodobnie odwołujący się do tabeli organizacji.
- **Typowa zawartość**: Ciąg UUID.
- **Uwaga**: Łączy typ dokumentu z konkretną organizacją.

### document_type_id
- **Znaczenie**: Identyfikator typu dokumentu.
- **Rola**: Klucz obcy, prawdopodobnie powiązany z tabelą referencyjną typów dokumentów.
- **Typowa zawartość**: Ciąg UUID.
- **Uwaga**: Umożliwia mapowanie na konkretne typy dokumentów.

### document_type_key
- **Znaczenie**: Klucz lub kod reprezentujący typ dokumentu.
- **Rola**: Pole opisowe do klasyfikacji typu dokumentu.
- **Typowa zawartość**: Ciąg znaków pełniący funkcję identyfikatora lub etykiety typu dokumentu.
- **Uwaga**: Służy do identyfikacji typu dokumentu w formie czytelnej dla człowieka.

### document_locale
- **Znaczenie**: Ustawienie regionalne lub językowe typu dokumentu.
- **Rola**: Pole opisowe określające ustawienia regionalne.
- **Typowa zawartość**: Ciąg znaków, często 'auto', oznaczający automatyczne ustalanie ustawień regionalnych.
- **Uwaga**: Przydatne w celach internacjonalizacji i lokalizacji.

### classification_method
- **Znaczenie**: Metoda używana do klasyfikacji typu dokumentu.
- **Rola**: Pole opisowe wskazujące sposób klasyfikacji dokumentu.
- **Typowa zawartość**: Ciąg znaków, często 'auto', sugerujący automatyczną klasyfikację.
- **Uwaga**: Ważne dla zrozumienia procesu klasyfikacji.

### is_active
- **Znaczenie**: Status wskazujący, czy typ dokumentu jest aktywny.
- **Rola**: Logiczne pole statusu.
- **Typowa zawartość**: `True` lub `False`.
- **Uwaga**: Określa, czy typ dokumentu jest obecnie używany.

### extraction_type
- **Znaczenie**: Typ metody ekstrakcji używanej dla dokumentu.
- **Rola**: Pole opisowe procesu ekstrakcji.
- **Typowa zawartość**: Ciągi znaków takie jak 'FIX_COORDINATES', 'FLEX_COORDINATES' lub `None`.
- **Uwaga**: Pozwala zrozumieć, w jaki sposób dane są ekstrahowane z dokumentów.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył rekord.
- **Rola**: Pole techniczne do celów audytowych.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.
- **Uwaga**: Przydatny do śledzenia zmian i odpowiedzialności.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia rekordu.
- **Rola**: Pole techniczne do celów audytowych.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową.
- **Uwaga**: Ważny do śledzenia daty i godziny utworzenia rekordu.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
- **Rola**: Pole techniczne do celów audytowych.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową.
- **Uwaga**: Przydatny do śledzenia aktualizacji i zmian rekordu.

### is_deleted
- **Znaczenie**: Status wskazujący, czy rekord został oznaczony jako usunięty.
- **Rola**: Logiczne pole statusu.
- **Typowa zawartość**: `True` lub `False`.
- **Uwaga**: Pomaga we wdrożeniu funkcji miękkiego usuwania.

### sub_org_id
- **Znaczenie**: Identyfikator podorganizacji powiązanej z typem dokumentu.
- **Rola**: Możliwy klucz obcy, dodający hierarchiczną strukturę organizacji.
- **Typowa zawartość**: Ciąg UUID lub `None`.
- **Uwaga**: Dostarcza dodatkowego kontekstu dla struktury organizacji.

```
