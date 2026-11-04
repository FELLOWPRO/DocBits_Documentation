# Atrybuty typu dokumentu

## Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `doc_type_key`: wewnętrzne
* `sub_doc_type_key`: wewnętrzne
* `attribute_key`: wewnętrzne
* `attribute_value`: text
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `sub_org_id`: wewnętrzne

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.document_type_attributes`

## Wprowadzenie

Tabela `public.document_type_attributes` służy do zarządzania atrybutami powiązanymi z różnymi typami dokumentów w kontekście organizacyjnym. Tabela ta prawdopodobnie wspiera zarządzanie konfiguracją lub metadanymi dla różnych typów dokumentów, takich jak faktury lub dowody dostawy, poprzez przypisywanie określonych atrybutów do każdego typu dokumentu.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący wiersz w tabeli.

### org_id
- **Znaczenie**: Reprezentuje organizację, do której należy atrybut typu dokumentu.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID odwołujący się do organizacji.

### doc_type_key
- **Znaczenie**: Typ dokumentu, do którego odnosi się atrybut (np. INVOICE, DELIVERY_NOTE).
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków reprezentujący typ dokumentu.

### sub_doc_type_key
- **Znaczenie**: Bardziej szczegółowa kategoryzacja w ramach typu dokumentu, jeśli ma zastosowanie.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zazwyczaj `None`, co oznacza, że nie zawsze jest używane.

### attribute_key
- **Znaczenie**: Konkretny klucz atrybutu lub właściwości związanej z typem dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków reprezentujący klucz atrybutu, np. `SECOND_APPROVAL_BEFORE_EXPORT`.

### attribute_value
- **Znaczenie**: Wartość powiązana z kluczem atrybutu dla danego typu dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków lub wartość liczbowa stanowiąca wartość atrybutu, np. `true`, `123`.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył rekord.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia rekordu.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący, kiedy rekord został utworzony.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową wskazujący czas ostatniej aktualizacji.

### is_deleted
- **Znaczenie**: Wskazuje, czy rekord został oznaczony jako usunięty.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna, gdzie `false` oznacza, że rekord jest aktywny.

### sub_org_id
- **Znaczenie**: Reprezentuje podorganizację w ramach organizacji głównej, jeśli ma zastosowanie.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Zazwyczaj `None`, co oznacza, że nie zawsze jest używane.
```

Niniejsza dokumentacja zawiera uporządkowany przegląd tabeli `public.document_type_attributes`, pozwalając programistom zrozumieć przeznaczenie i sposób użycia każdej kolumny.
