# Sub document type

## Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_key`: internal
* `sub_doc_type_key`: internal
* `name`: internal
* `title`: internal
* `translation_key`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analiza i opis

```markdown
# Tabela `public.sub_document_type`

## Wprowadzenie

Tabela `sub_document_type` służy do przechowywania szczegółowych informacji o różnych podtypach dokumentów w organizacji. Obejmuje to unikalne identyfikatory, powiązania z organizacją, nazwy opisowe oraz metadane dotyczące tworzenia i modyfikowania tych podtypów dokumentów. Tabela przechowuje również status miękkiego usunięcia rekordów.

## Opis kolumn

### id
- **Znaczenie**: Ta kolumna przechowuje unikalny identyfikator każdego podtypu dokumentu.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący rekord podtypu dokumentu (np. `'c2cc2d62-e4be-491b-a43e-c4123dff5aa6'`).

### org_id
- **Znaczenie**: Ta kolumna wskazuje organizację, do której należy podtyp dokumentu.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID odwołujący się do organizacji (np. `'23f3d697-7411-4c95-981d-faf089d266be'`).

### doc_type_key
- **Znaczenie**: Reprezentuje klucz typu dokumentu powiązanego z podtypem dokumentu.
- **Rola**: Klucz obcy (wynika z konwencji nazewnictwa).
- **Typowa zawartość**: Klucz w postaci ciągu znaków łączący z szerszym typem dokumentu (np. `'TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### sub_doc_type_key
- **Znaczenie**: Oznacza konkretny klucz podtypu dokumentu w ramach kategorii dokumentów.
- **Rola**: Unikalny identyfikator podtypu dokumentu w zakresie typu dokumentu.
- **Typowa zawartość**: Klucz w postaci ciągu znaków jednoznacznie identyfikujący podtyp dokumentu (np. `'TEST_SUB_TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### name
- **Znaczenie**: Przechowuje krótką nazwę lub kod podtypu dokumentu.
- **Rola**: Opisowa.
- **Typowa zawartość**: Zwięzły identyfikator lub kod (np. `'TEST_SUB_TEST'`).

### title
- **Znaczenie**: Zawiera czytelny dla człowieka tytuł podtypu dokumentu.
- **Rola**: Opisowa.
- **Typowa zawartość**: Opisowy tytuł do wyświetlania w interfejsach użytkownika lub raportach (np. `'Test Sub Test'`).

### translation_key
- **Znaczenie**: Klucz używany do internacjonalizacji i lokalizacji w celu tłumaczenia nazwy podtypu dokumentu.
- **Rola**: Techniczna.
- **Typowa zawartość**: Ciąg znaków używany w plikach tłumaczeń (np. `'test_sub_test'`).

### created_by
- **Znaczenie**: Identyfikuje użytkownika, który utworzył wpis podtypu dokumentu.
- **Rola**: Techniczna.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika (np. `8`).

### created_on
- **Znaczenie**: Znacznik czasu wskazujący, kiedy utworzono podtyp dokumentu.
- **Rola**: Techniczna.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową (np. `2022-12-13 08:34:13.932893+00:00`).

### last_modified_on
- **Znaczenie**: Znacznik czasu wskazujący, kiedy podtyp dokumentu był ostatnio modyfikowany.
- **Rola**: Techniczna.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową, ewentualnie `None`, jeśli wpis nigdy nie był modyfikowany po utworzeniu.

### is_deleted
- **Znaczenie**: Flaga logiczna wskazująca, czy podtyp dokumentu został miękko usunięty.
- **Rola**: Techniczna.
- **Typowa zawartość**: `True` lub `False` wskazujące status usunięcia (np. `False`).
```
