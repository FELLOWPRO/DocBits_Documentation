# PO match tolerance

## Tabela `public.po_match_tolerance`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `item_number`: internal
* `supplier_item_number`: internal
* `description`: internal
* `unit_price_tolerance`: double precision
* `quantity_tolerance`: double precision
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `unit_price_tolerance_type`: internal
* `quantity_tolerance_type`: internal

### Analiza i opis

## Dokumentacja techniczna tabeli `public.po_match_tolerance`

### Wprowadzenie

Tabela `public.po_match_tolerance` służy do zarządzania i przechowywania poziomów tolerancji związanych z procesami dopasowywania zamówień zakupu (PO). Zazwyczaj dotyczy to dopuszczalnych rozbieżności w cenach jednostkowych i ilościach między towarami zamówionymi a otrzymanymi. Każdy wpis w tabeli reprezentuje ustawienia tolerancji dla konkretnych pozycji, co może pomagać organizacjom w zapewnieniu spójności i dokładności procesów zakupowych.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego wpisu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdy rekord ustawień tolerancji.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z ustawieniami tolerancji.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID łączący z organizacją w systemie.

#### item\_number

* **Znaczenie**: Konkretny numer pozycji, dla którego zdefiniowano ustawienia tolerancji.
* **Rola**: Identyfikator biznesowy.
* **Typowa zawartość**: Ciąg znaków reprezentujący kod lub numer pozycji w zapasach organizacji.

#### supplier\_item\_number

* **Znaczenie**: Numer pozycji podany przez dostawcę.
* **Rola**: Identyfikator biznesowy.
* **Typowa zawartość**: Ciąg znaków, który może mieć wartość `None`, jeśli nie został podany; reprezentuje kod lub numer pozycji u dostawcy.

#### description

* **Znaczenie**: Opis tekstowy pozycji.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków zawierający szczegóły dotyczące pozycji, który może mieć wartość `None`.

#### unit\_price\_tolerance

* **Znaczenie**: Dopuszczalne odchylenie ceny jednostkowej pozycji.
* **Rola**: Reguła biznesowa.
* **Typowa zawartość**: Wartość liczbowa wskazująca tolerancję ceny jednostkowej w procentach lub jako wartość bezwzględna.

#### quantity\_tolerance

* **Znaczenie**: Dopuszczalne odchylenie ilości pozycji.
* **Rola**: Reguła biznesowa.
* **Typowa zawartość**: Wartość liczbowa wskazująca tolerancję ilości w procentach lub jako wartość bezwzględna.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył wpis.
* **Rola**: Pole audytowe/rejestrujące.
* **Typowa zawartość**: Liczba całkowita, zazwyczaj odnosząca się do identyfikatora użytkownika w systemie.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia wpisu.
* **Rola**: Pole audytowe/rejestrujące.
* **Typowa zawartość**: Wartość daty i godziny ze strefą czasową wskazująca datę i czas utworzenia.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji wpisu.
* **Rola**: Pole audytowe/rejestrujące.
* **Typowa zawartość**: Wartość daty i godziny ze strefą czasową wskazująca moment ostatniej aktualizacji rekordu; może mieć wartość `None`, jeśli wpis nie był modyfikowany.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy wpis został logicznie usunięty.
* **Rola**: Wskaźnik techniczny/miękkiego usuwania.
* **Typowa zawartość**: Wartość logiczna, gdzie `False` oznacza aktywny, a `True` logicznie usunięty.

#### unit\_price\_tolerance\_type

* **Znaczenie**: Definiuje typ tolerancji ceny jednostkowej (np. procentowa lub wartość bezwzględna).
* **Rola**: Reguła biznesowa.
* **Typowa zawartość**: Ciąg znaków, często 'value', wskazujący typ miary tolerancji.

#### quantity\_tolerance\_type

* **Znaczenie**: Definiuje typ tolerancji ilości (np. procentowa lub wartość bezwzględna).
* **Rola**: Reguła biznesowa.
* **Typowa zawartość**: Ciąg znaków, często 'value', wskazujący typ miary tolerancji.

Niniejsza dokumentacja zawiera szczegółowy przegląd każdego pola w tabeli `public.po_match_tolerance`, przedstawiając ich potencjalną zawartość i role w kontekście zarządzania zamówieniami zakupu.
