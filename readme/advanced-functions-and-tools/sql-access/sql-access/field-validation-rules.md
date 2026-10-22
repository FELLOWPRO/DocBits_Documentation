# Reguły walidacji pól

## Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `field_id`: wewnętrzne
* `doc_type`: typ DOC
* `is_sub_doc_type_field`: boolean
* `profile`: wewnętrzne
* `field_name`: wewnętrzne
* `field_length`: integer
* `field_label`: wewnętrzne
* `is_required`: boolean
* `is_readonly`: boolean
* `is_hidden`: boolean
* `force_validation`: boolean
* `validation_pattern`: wewnętrzne
* `confidence_threshold`: integer
* `match_score_threshold`: integer
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `additional_attributes`: text

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.field_validation_rules`

## Wprowadzenie

Tabela `public.field_validation_rules` przechowuje metadane i reguły walidacji pól powiązanych z różnymi typami dokumentów w organizacji. Prawdopodobnie służy do egzekwowania integralności i spójności danych w formularzach lub dokumentach poprzez określanie wymagań, takich jak to, czy pole jest wymagane, jego długość, widoczność oraz wzorce walidacji, które mają być stosowane.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdej reguły walidacji pola.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący rekord.

### org_id
- **Znaczenie**: Identyfikator organizacji, do której odnosi się reguła walidacji.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID odwołujący się do konkretnej organizacji.

### field_id
- **Znaczenie**: Identyfikator konkretnego pola, z którym powiązana jest reguła walidacji.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID odwołujący się do konkretnego pola.

### doc_type
- **Znaczenie**: Określa typ dokumentu, z którym powiązana jest reguła walidacji pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków wskazujący typ dokumentu (np. `PURCHASE_ORDER_FORM`).

### is_sub_doc_type_field
- **Znaczenie**: Wskazuje, czy pole jest częścią podtypu dokumentu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

### profile
- **Znaczenie**: Reprezentuje profil lub kontekst, w którym stosowana jest walidacja pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków, np. `DEFAULT`.

### field_name
- **Znaczenie**: Nazwa pola, dla którego zdefiniowano regułę walidacji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków reprezentujący nazwę pola (np. `Test`).

### field_length
- **Znaczenie**: Maksymalna dozwolona długość zawartości pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita określająca limit znaków.

### field_label
- **Znaczenie**: Etykieta lub nazwa wyświetlana pola w interfejsie użytkownika.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: W przykładowych danych zazwyczaj null.

### is_required
- **Znaczenie**: Wskazuje, czy pole jest obowiązkowe dla dokumentu.
- **Rola**: Wskaźnik ograniczenia.
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

### is_readonly
- **Znaczenie**: Określa, czy pole jest edytowalne, czy tylko do odczytu.
- **Rola**: Wskaźnik ograniczenia.
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

### is_hidden
- **Znaczenie**: Wskazuje, czy pole powinno być ukryte w interfejsie użytkownika.
- **Rola**: Wskaźnik ograniczenia.
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

### force_validation
- **Znaczenie**: Określa, czy walidacja powinna być wymuszana niezależnie od innych warunków.
- **Rola**: Wskaźnik ograniczenia.
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

### validation_pattern
- **Znaczenie**: Wzorzec (prawdopodobnie regex), któremu musi odpowiadać zawartość pola.
- **Rola**: Reguła walidacji.
- **Typowa zawartość**: W przykładowych danych zazwyczaj null.

### confidence_threshold
- **Znaczenie**: Minimalny poziom pewności wymagany do walidacji pola.
- **Rola**: Ograniczenie walidacji.
- **Typowa zawartość**: Wartość całkowita reprezentująca próg pewności.

### match_score_threshold
- **Znaczenie**: Minimalny wynik dopasowania wymagany do walidacji zawartości pola.
- **Rola**: Ograniczenie walidacji.
- **Typowa zawartość**: Wartość całkowita reprezentująca próg wyniku dopasowania.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył tę regułę walidacji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### created_on
- **Znaczenie**: Znacznik czasu wskazujący, kiedy utworzono regułę walidacji.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową.

### last_modified_on
- **Znaczenie**: Znacznik czasu wskazujący ostatnią modyfikację reguły walidacji.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową; może mieć wartość null, jeśli reguła nigdy nie była modyfikowana.

### is_deleted
- **Znaczenie**: Wskazuje, czy reguła walidacji została oznaczona jako usunięta.
- **Rola**: Wskaźnik miękkiego usuwania.
- **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

### additional_attributes
- **Znaczenie**: Przechowuje dodatkowe atrybuty lub metadane powiązane z regułą walidacji pola.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Tekst, w przykładowych danych często null.
```
