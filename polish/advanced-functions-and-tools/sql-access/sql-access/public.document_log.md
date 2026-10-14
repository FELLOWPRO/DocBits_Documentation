# public.document\_log

## Tabela `public.document_log`

### Kolumny

* `id`: integer
* `org_id`: ID to organisation
* `doc_id`: internal
* `action_type`: internal
* `action_description`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_hidden`: boolean
* `previous_status`: internal
* `current_status`: internal

### Analiza i opis

## Dokumentacja techniczna: tabela `public.document_log`

### Wprowadzenie

Tabela `public.document_log` służy do śledzenia historii i zmian statusu dokumentów w organizacji. Rejestruje czynności wykonywane na dokumentach, takie jak aktualizacje statusu, wraz ze szczegółami dotyczącymi użytkownika, który wykonał daną czynność, oraz znacznikami czasu wskazującymi, kiedy te czynności miały miejsce. Tabela ta ma kluczowe znaczenie dla audytu przepływów przetwarzania dokumentów i zrozumienia cyklu życia każdego dokumentu.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego wpisu dziennika.
* **Rola**: Klucz główny. Kolumna ta pełni funkcję unikalnego identyfikatora każdego rekordu w tabeli.
* **Typowa zawartość**: Wartości całkowite zwiększane z każdym nowym wpisem.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z dokumentem.
* **Rola**: Klucz obcy. Odwołuje się do jednostki organizacji, choć nie zostało to w tym kontekście jawnie zdefiniowane.
* **Typowa zawartość**: Ciągi znaków, prawdopodobnie UUID, reprezentujące identyfikatory organizacji.

#### doc\_id

* **Znaczenie**: Identyfikator dokumentu powiązanego z wpisem dziennika.
* **Rola**: Klucz obcy. Kolumna ta odwołuje się do konkretnego dokumentu w systemie.
* **Typowa zawartość**: Ciągi znaków, prawdopodobnie UUID, reprezentujące identyfikatory dokumentów.

#### action\_type

* **Znaczenie**: Typ zarejestrowanej czynności.
* **Rola**: Pole opisowe. Wskazuje kategorię wykonanej czynności.
* **Typowa zawartość**: Ciągi znaków takie jak `STATUS_CHANGE`, wskazujące charakter czynności.

#### action\_description

* **Znaczenie**: Szczegółowy opis wykonanej czynności.
* **Rola**: Pole opisowe. Dostarcza kontekstu lub szczegółów dotyczących czynności.
* **Typowa zawartość**: Opisy tekstowe, np. "Data extraction started", "Error occurred processing document".

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył wpis dziennika.
* **Rola**: Klucz obcy. Odwołuje się do jednostki użytkownika, wskazując, kto wykonał czynność.
* **Typowa zawartość**: Wartości całkowite reprezentujące identyfikatory użytkowników.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia wpisu dziennika.
* **Rola**: Pole techniczne. Rejestruje dokładny czas zapisania czynności w dzienniku.
* **Typowa zawartość**: Znaczniki czasu z informacją o strefie czasowej, np. `2025-04-01 13:07:51.291193 UTC`.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji wpisu dziennika.
* **Rola**: Pole techniczne. Wskazuje czas ostatniej aktualizacji wpisu dziennika.
* **Typowa zawartość**: Znaczniki czasu, potencjalnie null, jeśli wpis nie był modyfikowany po utworzeniu.

#### is\_deleted

* **Znaczenie**: Flaga wskazująca, czy wpis dziennika został oznaczony jako usunięty.
* **Rola**: Pole techniczne. Służy do logicznego usuwania wpisów.
* **Typowa zawartość**: Wartości logiczne, `False` oznacza wpisy aktywne, a `True` usunięte.

#### is\_hidden

* **Znaczenie**: Flaga wskazująca, czy wpis dziennika jest ukryty w normalnym widoku.
* **Rola**: Pole techniczne. Służy do kontrolowania widoczności wpisów dziennika.
* **Typowa zawartość**: Wartości logiczne, `False` oznacza wpisy widoczne, a `True` ukryte.

#### previous\_status

* **Znaczenie**: Status dokumentu przed wykonaniem czynności.
* **Rola**: Pole opisowe. Podaje stan dokumentu poprzedzający zarejestrowaną czynność.
* **Typowa zawartość**: Ciągi znaków takie jak `new`, `validating`, `running`, reprezentujące stany dokumentu.

#### current\_status

* **Znaczenie**: Status dokumentu po wykonaniu czynności.
* **Rola**: Pole opisowe. Wskazuje zaktualizowany stan dokumentu po wykonaniu czynności.
* **Typowa zawartość**: Ciągi znaków takie jak `running`, `ready_for_validation`, `error`, reprezentujące stany dokumentu.

Niniejsza dokumentacja zawiera przegląd tabeli `public.document_log`, opisując przeznaczenie i strukturę każdej kolumny, co ma kluczowe znaczenie dla programistów zarządzających przepływami dokumentów i utrzymujących ścieżki audytu.
