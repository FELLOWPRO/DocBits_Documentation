# Custom classification tag

## Tabela `public.custom_classification_tag`

### Kolumny

* `id`: integer
* `org_id`: ID organizacji
* `name`: wewnętrzne
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analiza i opis

## Dokumentacja techniczna tabeli `public.custom_classification_tag`

### Wprowadzenie

Tabela `public.custom_classification_tag` służy do zarządzania niestandardowymi tagami klasyfikacji w organizacji. Zawiera podstawowe informacje o każdym tagu, w tym jego powiązanie z organizacją, szczegóły utworzenia i modyfikacji oraz status w cyklu życia.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego tagu klasyfikacji.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Wartość całkowita jednoznacznie identyfikująca każdy rekord w tabeli.

#### org\_id

* **Znaczenie**: Identyfikator organizacji, do której należy tag klasyfikacji.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg znaków, prawdopodobnie UUID, reprezentujący unikalny identyfikator organizacji.

#### name

* **Znaczenie**: Nazwa lub etykieta tagu klasyfikacji.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków oznaczający nazwę lub opis tagu. Może to być pusty ciąg, jeśli nazwa nie została podana.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył tag klasyfikacji.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika będącego twórcą.

#### created\_on

* **Znaczenie**: Znacznik czasu wskazujący, kiedy utworzono tag klasyfikacji.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową rejestrujący dokładną datę i godzinę utworzenia.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji tagu klasyfikacji.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu ze strefą czasową, który może mieć wartość `None`, jeśli od utworzenia nie dokonano żadnych modyfikacji.

#### is\_deleted

* **Znaczenie**: Flaga wskazująca, czy tag klasyfikacji został oznaczony jako usunięty.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`), gdzie `False` oznacza, że tag jest aktywny, a `True`, że został usunięty lub dezaktywowany.
