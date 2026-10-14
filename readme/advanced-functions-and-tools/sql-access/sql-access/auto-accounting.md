# Auto accounting

## Tabela `public.auto_accounting`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `supplier_name`: nazwa dostawcy
* `description`: wewnętrzne
* `item_number`: wewnętrzne
* `line_amount`: double precision
* `total_amount`: double precision
* `mapped_amount`: double precision
* `ledger_account`: wewnętrzne
* `doc_id`: wewnętrzne

### Analiza i opis

## Dokumentacja techniczna tabeli `public.auto_accounting`

### Wprowadzenie

Tabela `public.auto_accounting` służy do zarządzania danymi księgowymi powiązanymi z różnymi dostawcami i organizacjami oraz do ich przechowywania. Tabela zawiera informacje o transakcjach finansowych, w tym kwoty i konta księgi głównej, które są niezbędne w sprawozdawczości finansowej i analizie.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdy wpis.
* **Uwaga**: Zapewnia możliwość jednoznacznej identyfikacji każdego rekordu.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z wpisem księgowym.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID wskazujący organizację w tabeli nadrzędnej.
* **Uwaga**: Służy do powiązania wpisów księgowych z konkretnymi organizacjami.

#### supplier\_name

* **Znaczenie**: Nazwa dostawcy uczestniczącego w transakcji.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Tekst zawierający nazwę dostawcy, np. "Fellow Consulting AG".
* **Uwaga**: Dostarcza informacji o dostawcy powiązanym z transakcją.

#### description

* **Znaczenie**: Krótki opis transakcji lub pozycji.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Tekst opisujący transakcję, np. nazwa towaru ("apple" lub "Peaches").
* **Uwaga**: Pomaga zrozumieć charakter transakcji.

#### item\_number

* **Znaczenie**: Identyfikator konkretnej pozycji uczestniczącej w transakcji.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Może to być identyfikator produktu lub SKU, choć nie podano przykładowych danych.
* **Uwaga**: Przydatne do śledzenia konkretnych pozycji lub odwoływania się do nich.

#### line\_amount

* **Znaczenie**: Kwota pieniężna dla konkretnej pozycji (wiersza) transakcji.
* **Rola**: Pole finansowe.
* **Typowa zawartość**: Wartość dziesiętna przedstawiająca kwotę pojedynczej pozycji.
* **Uwaga**: Ważne w szczegółowej analizie finansowej na poziomie pozycji.

#### total\_amount

* **Znaczenie**: Łączna kwota pieniężna transakcji.
* **Rola**: Pole finansowe.
* **Typowa zawartość**: Wartość dziesiętna przedstawiająca łączną kwotę transakcji.
* **Uwaga**: Stanowi sumę wszystkich kwot pozycji w transakcji.

#### mapped\_amount

* **Znaczenie**: Kwota, która została przypisana lub zmapowana do określonego konta.
* **Rola**: Pole finansowe.
* **Typowa zawartość**: Wartość dziesiętna wskazująca, jaka część transakcji została przypisana.
* **Uwaga**: Przydatne do zrozumienia, jak środki są rozdzielone między konta.

#### ledger\_account

* **Znaczenie**: Numer konta w księdze głównej, na którym zaksięgowano transakcję.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Tekst reprezentujący numer konta, np. "2200" lub "2500".
* **Uwaga**: Kluczowe z punktu widzenia księgowości do śledzenia, gdzie transakcje są księgowane.

#### doc\_id

* **Znaczenie**: Identyfikator powiązanego dokumentu lub rekordu.
* **Rola**: Klucz obcy lub odwołanie.
* **Typowa zawartość**: Ciąg UUID lub inny identyfikator wskazujący powiązane dokumenty.
* **Uwaga**: Pomaga powiązać transakcje z konkretnymi dokumentami lub rekordami, co zapewnia ich identyfikowalność.

Niniejsza dokumentacja zawiera szczegółowy przegląd struktury tabeli `public.auto_accounting` oraz przeznaczenia każdej kolumny, aby ułatwić programistom i administratorom baz danych zrozumienie danych i ich efektywne wykorzystanie.
