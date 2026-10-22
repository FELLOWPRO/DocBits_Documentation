# Dokument klasyfikacji niestandardowej

## Tabela `public.custom_classification_document`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `first_page_content`: text
* `content`: text
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean

### Analiza i opis

## Dokumentacja techniczna tabeli `public.custom_classification_document`

### Wprowadzenie

Tabela `public.custom_classification_document` służy do przechowywania szczegółowych informacji o klasyfikacji dokumentów w organizacji. Obejmuje to metadane dokumentu, takie jak jego treść, szczegóły utworzenia i kontekst organizacyjny. Struktura tabeli sugeruje jej użycie do zarządzania dokumentami związanymi z procesami organizacji, prawdopodobnie fakturami lub formularzami zamówień, co wynika z przykładowych danych.

### Opis kolumn

#### id

* **Znaczenie**: Ta kolumna prawdopodobnie przechowuje unikalny identyfikator każdego wpisu dokumentu.
* **Rola**: Klucz główny
* **Typowa zawartość**: UUID reprezentujący unikalny identyfikator dokumentu.

#### org\_id

* **Znaczenie**: Ta kolumna przechowuje identyfikator organizacji powiązanej z dokumentem.
* **Rola**: Klucz obcy
* **Typowa zawartość**: UUID łączący dokument z konkretną organizacją.

#### first\_page\_content

* **Znaczenie**: Ta kolumna zawiera treść tekstową pierwszej strony dokumentu.
* **Rola**: Pole danych
* **Typowa zawartość**: Tekstowa reprezentacja dokumentu organizacji, prawdopodobnie zawierająca nagłówki, adresy i podstawowe informacje z początku faktury lub zamówienia.

#### content

* **Znaczenie**: Ta kolumna przechowuje pełną treść tekstową dokumentu.
* **Rola**: Pole danych
* **Typowa zawartość**: Pełna treść tekstowa dokumentu, w tym wszystkie szczegóły z pierwszej strony i kolejnych stron.

#### created\_by

* **Znaczenie**: Ta kolumna wskazuje użytkownika, który utworzył wpis dokumentu.
* **Rola**: Pole danych
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika będącego twórcą.

#### created\_on

* **Znaczenie**: Ta kolumna zapisuje datę i godzinę utworzenia wpisu dokumentu.
* **Rola**: Pole techniczne
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej, wskazujący datę i godzinę utworzenia.

#### last\_modified\_on

* **Znaczenie**: Ta kolumna przechowuje datę i godzinę ostatniej modyfikacji wpisu dokumentu.
* **Rola**: Pole techniczne
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej, wskazujący datę i godzinę ostatniej modyfikacji. Czasami ma wartość `None`, jeśli po utworzeniu nie dokonano żadnych modyfikacji.

#### is\_deleted

* **Znaczenie**: Ta kolumna wskazuje, czy wpis dokumentu został oznaczony jako usunięty.
* **Rola**: Pole techniczne
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`) pokazująca status usunięcia wpisu dokumentu.

Ta tabela zapewnia solidną strukturę do zarządzania danymi dokumentów, gwarantując, że każdy dokument może być jednoznacznie zidentyfikowany, powiązany z organizacją i śledzony w całym cyklu tworzenia i modyfikacji.
