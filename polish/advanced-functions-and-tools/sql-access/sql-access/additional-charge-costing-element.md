# Additional charge costing element

## Table `public.additional_charge_costing_element`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `costing_element`: internal
* `description`: internal
* `charge_type`: internal
* `distribution_method`: internal
* `distribution_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `sub_org_id`: internal
* `charge_count`: integer
* `charge_icon`: internal
* `charge_category`: internal
* `charge_sequence_number`: integer
* `charge_operator`: integer
* `last_modified_by`: internal
* `deleted_by`: internal

### Analiza i opis

## Dokumentacja tabeli: `public.additional_charge_costing_element`

### Wprowadzenie

Tabela `public.additional_charge_costing_element` służy do zarządzania i przechowywania informacji o różnych elementach kalkulacji kosztów dodatkowych w organizacji. Obejmuje dane o typie opłat, sposobie ich rozdzielania oraz administracyjne metadane, takie jak szczegóły utworzenia i modyfikacji. Tabela ta jest prawdopodobnie wykorzystywana w zarządzaniu finansowym i operacyjnym organizacji, ze szczególnym uwzględnieniem kosztów dodatkowych, które trzeba śledzić i analizować.

### Opisy kolumn

#### id

* **Znaczenie**: Ta kolumna przechowuje unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Unikalny ciąg alfanumeryczny identyfikujący każdy rekord elementu kalkulacji kosztów.

#### org\_id

* **Znaczenie**: Identyfikator organizacji, do której należy ten element kalkulacji kosztów.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: UUID reprezentujący organizację.

#### costing\_element

* **Znaczenie**: Identyfikator lub kod elementu kalkulacji kosztów.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg alfanumeryczny reprezentujący konkretny element kalkulacji kosztów.

#### description

* **Znaczenie**: Opis tekstowy elementu kalkulacji kosztów.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Krótkie wyjaśnienie tekstowe elementu kalkulacji kosztów.

#### charge\_type

* **Znaczenie**: Typ opłaty powiązanej z tym elementem kalkulacji kosztów.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Kod lub krótki tekst wskazujący typ opłaty.

#### distribution\_method

* **Znaczenie**: Metoda, za pomocą której opłata jest rozdzielana.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Kod lub krótki tekst wskazujący metodę rozdzielania.

#### distribution\_type

* **Znaczenie**: Typ rozdzielania opłaty.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Kod lub krótki tekst wskazujący typ rozdzielania.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył rekord.
* **Rola**: Pole administracyjne.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

#### created\_on

* **Znaczenie**: Znacznik czasu wskazujący, kiedy rekord został utworzony.
* **Rola**: Pole administracyjne.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
* **Rola**: Pole administracyjne.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy rekord jest oznaczony jako usunięty.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia rekordu jako usuniętego.
* **Rola**: Pole administracyjne.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej lub `None`, jeśli rekord nie został usunięty.

#### sub\_org\_id

* **Znaczenie**: Identyfikator podorganizacji powiązanej z elementem kalkulacji kosztów.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: UUID reprezentujący podorganizację.

#### charge\_count

* **Znaczenie**: Liczba opłat powiązanych z elementem kalkulacji kosztów.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Liczba całkowita reprezentująca liczbę opłat.

#### charge\_icon

* **Znaczenie**: Ikona lub symbol powiązany z opłatą.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący ikonę, prawdopodobnie ścieżkę lub identyfikator.

#### charge\_category

* **Znaczenie**: Kategoria, do której należy opłata.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący kategorię opłaty.

#### charge\_sequence\_number

* **Znaczenie**: Numer kolejności służący do porządkowania opłat.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Liczba całkowita używana do ustalania kolejności opłat.

#### charge\_operator

* **Znaczenie**: Identyfikator operatora odpowiedzialnego za opłatę.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator operatora.

#### last\_modified\_by

* **Znaczenie**: Identyfikator użytkownika, który ostatnio zmodyfikował rekord.
* **Rola**: Pole administracyjne.
* **Typowa zawartość**: Ciąg znaków reprezentujący identyfikator użytkownika, potencjalnie `None`, jeśli rekord nigdy nie był modyfikowany.

#### deleted\_by

* **Znaczenie**: Identyfikator użytkownika, który oznaczył rekord jako usunięty.
* **Rola**: Pole administracyjne.
* **Typowa zawartość**: Ciąg znaków reprezentujący identyfikator użytkownika, potencjalnie `None`, jeśli rekord nie został usunięty.
