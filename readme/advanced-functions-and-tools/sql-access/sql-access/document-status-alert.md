# Alert stanu dokumentu

## Tabela `public.document_status_alert`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `doc_type_id`: wewnętrzne
* `doc_type_key`: wewnętrzne
* `doc_status`: wewnętrzne
* `email_address`: text
* `send_to_assigned_user`: boolean
* `delay_delta`: integer
* `delay_delta_type`: wewnętrzne
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `name`: wewnętrzne
* `is_recursive`: boolean
* `is_active`: boolean
* `priority`: wewnętrzne
* `email_template_id`: wewnętrzne

### Analiza i opis

## Dokumentacja tabeli: `public.document_status_alert`

### Wprowadzenie

Tabela `public.document_status_alert` służy do zarządzania alertami związanymi ze statusami dokumentów w organizacji. Na podstawie nazw kolumn można wnioskować, że przechowuje informacje o różnych typach dokumentów i ich statusach, w tym szczegóły dotyczące powiadomień i czasu wysyłania alertów. Tabela ta jest prawdopodobnie używana do wyzwalania alertów na podstawie określonych statusów i warunków dokumentów, np. w celu powiadamiania użytkowników lub eskalacji procesów.

### Opis kolumn

#### `id`

* **Znaczenie**: Unikalny identyfikator każdego rekordu alertu.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdy wiersz w tabeli.

#### `org_id`

* **Znaczenie**: Identyfikator organizacji powiązanej z alertem.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID wskazujący rekord organizacji.

#### `doc_type_id`

* **Znaczenie**: Identyfikator typu dokumentu.
* **Rola**: Klucz obcy (zakładany).
* **Typowa zawartość**: Zazwyczaj UUID, choć przykładowe dane pokazują `None`, co oznacza, że to pole może być opcjonalne.

#### `doc_type_key`

* **Znaczenie**: Klucz reprezentujący typ dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków, np. 'INVOICE' lub 'XML\_INVOICE'.

#### `doc_status`

* **Znaczenie**: Bieżący status dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Opisowe ciągi statusu, np. 'validated\_pending\_approval' lub 'error'.

#### `email_address`

* **Znaczenie**: Adres e-mail, na który wysyłane są alerty.
* **Rola**: Pole powiadomienia.
* **Typowa zawartość**: Adres e-mail; może mieć wartość `None`, jeśli nie podano adresu e-mail.

#### `send_to_assigned_user`

* **Znaczenie**: Wskazuje, czy alert ma zostać wysłany do użytkownika przypisanego do dokumentu.
* **Rola**: Pole logiczne.
* **Typowa zawartość**: `True` lub `False`.

#### `delay_delta`

* **Znaczenie**: Czas opóźnienia wysłania alertu.
* **Rola**: Pole czasowe.
* **Typowa zawartość**: Liczba całkowita reprezentująca czas trwania opóźnienia.

#### `delay_delta_type`

* **Znaczenie**: Jednostka czasu dla `delay_delta`.
* **Rola**: Pole czasowe.
* **Typowa zawartość**: Zazwyczaj 'minutes'.

#### `created_by`

* **Znaczenie**: Identyfikator użytkownika, który utworzył rekord alertu.
* **Rola**: Klucz obcy (zakładany).
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

#### `created_on`

* **Znaczenie**: Znacznik czasu utworzenia rekordu alertu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina z informacją o strefie czasowej.

#### `last_modified_on`

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu alertu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina z informacją o strefie czasowej; może mieć wartość `None`, jeśli rekord nie był modyfikowany.

#### `is_deleted`

* **Znaczenie**: Wskazuje, czy rekord alertu został oznaczony jako usunięty.
* **Rola**: Pole logiczne.
* **Typowa zawartość**: `True` lub `False`.

#### `name`

* **Znaczenie**: Nazwa lub etykieta alertu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący nazwę alertu.

#### `is_recursive`

* **Znaczenie**: Wskazuje, czy alert ma się powtarzać w określonych odstępach czasu.
* **Rola**: Pole logiczne.
* **Typowa zawartość**: `True` lub `False`.

#### `is_active`

* **Znaczenie**: Wskazuje, czy alert jest aktualnie aktywny.
* **Rola**: Pole logiczne.
* **Typowa zawartość**: `True` lub `False`.

#### `priority`

* **Znaczenie**: Poziom priorytetu alertu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Mogą to być ciągi znaków, takie jak 'High', 'Medium', 'Low'; przykładowe dane pokazują `None`.

#### `email_template_id`

* **Znaczenie**: Identyfikator szablonu e-mail używanego dla alertu.
* **Rola**: Klucz obcy (zakładany).
* **Typowa zawartość**: Zazwyczaj UUID; przykładowe dane pokazują `None`, co oznacza, że to pole może być opcjonalne.
