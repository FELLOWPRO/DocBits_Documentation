# Training data

## Tabela `public.training_data`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `doc_origin`: Doc Origin
* `doc_locale`: Doc Locale
* `doc_language`: Language
* `first_page_content`: text
* `supplier_name`: Supplier Name
* `supplier_vat`: internal
* `doc_created_on`: timestamp with time zone
* `is_training_sample`: boolean
* `sample_doc_id`: internal
* `sample_file_name`: internal
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_table_training_sample`: boolean

### Analiza i opis

## Dokumentacja techniczna tabeli `public.training_data`

### Wprowadzenie

Tabela `public.training_data` służy prawdopodobnie do przechowywania różnych danych związanych z dokumentami, najpewniej używanych do trenowania modeli lub systemów przetwarzających i analizujących zawartość dokumentów. Tabela zawiera informacje o typie dokumentu, jego pochodzeniu, języku, szczegółach dostawcy oraz znaczniki czasu związane z tworzeniem i modyfikowaniem rekordów, a także inne atrybuty. Wydaje się skupiać szczególnie na fakturach i rachunkach medycznych, co sugeruje jej zastosowanie w aplikacjach do przetwarzania danych finansowych lub z sektora opieki zdrowotnej.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Uniwersalnie unikalny identyfikator (UUID) w formacie znakowym.
* **Uwaga**: Niezbędny do jednoznacznej identyfikacji każdego wpisu.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z dokumentem.
* **Rola**: Klucz obcy łączący z rekordem organizacji.
* **Typowa zawartość**: UUID reprezentujący organizację.
* **Uwaga**: Pomaga w przypisywaniu dokumentów do konkretnych organizacji.

#### doc\_type

* **Znaczenie**: Typ dokumentu przechowywanego w rekordzie.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartości takie jak 'INVOICE' lub 'MEDICAL\_RECEIPT'.
* **Uwaga**: Przydatne do kategoryzowania dokumentów.

#### doc\_origin

* **Znaczenie**: Pochodzenie lub kod kraju źródłowego dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Kod kraju, taki jak 'DE' dla Niemiec.
* **Uwaga**: Wskazuje geograficzne pochodzenie dokumentu.

#### doc\_locale

* **Znaczenie**: Informacje o ustawieniach regionalnych dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Kod ustawień regionalnych, taki jak 'en\_DE'.
* **Uwaga**: Łączy język i region na potrzeby lokalizacji.

#### doc\_language

* **Znaczenie**: Język, w którym napisany jest dokument.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Kod języka, taki jak 'en' lub 'de'.
* **Uwaga**: Wskazuje główny język użyty w dokumencie.

#### first\_page\_content

* **Znaczenie**: Zawartość pierwszej strony dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Dane tekstowe zawierające treść pierwszej strony dokumentu.
* **Uwaga**: Może być używana do analizy lub przetwarzania tekstu.

#### supplier\_name

* **Znaczenie**: Nazwa dostawcy powiązanego z dokumentem.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Nazwa dostawcy w formacie tekstowym.
* **Uwaga**: Ważna do identyfikacji źródła lub twórcy dokumentu.

#### supplier\_vat

* **Znaczenie**: Numer identyfikacji VAT dostawcy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Numer VAT, np. 'DE 129375678'.
* **Uwaga**: Przydatny w procesach fiskalnych i podatkowych.

#### doc\_created\_on

* **Znaczenie**: Znacznik czasu utworzenia dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Data i godzina w formacie UTC.
* **Uwaga**: Zapewnia kontekst czasowy powstania dokumentu.

#### is\_training\_sample

* **Znaczenie**: Wskaźnik, czy rekord jest używany jako próbka treningowa.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).
* **Uwaga**: Identyfikuje rekordy specjalnie oznaczone do celów treningowych.

#### sample\_doc\_id

* **Znaczenie**: Identyfikator dokumentu próbki.
* **Rola**: Pole opisowe lub możliwy klucz obcy.
* **Typowa zawartość**: UUID łączący z innym dokumentem.
* **Uwaga**: Może odwoływać się do powiązanego lub oryginalnego dokumentu użytego do próbkowania.

#### sample\_file\_name

* **Znaczenie**: Nazwa pliku powiązanego z próbką dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Nazwa pliku w formacie tekstowym.
* **Uwaga**: Przydatna w procesach zarządzania plikami lub ich pobierania.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia rekordu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina w formacie UTC.
* **Uwaga**: Wskazuje, kiedy rekord został dodany do bazy danych.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina w formacie UTC.
* **Uwaga**: Śledzi, kiedy rekord był ostatnio aktualizowany.

#### is\_deleted

* **Znaczenie**: Wskaźnik, czy rekord został oznaczony jako usunięty.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).
* **Uwaga**: Obsługuje funkcję miękkiego usuwania.

#### is\_table\_training\_sample

* **Znaczenie**: Wskaźnik, czy rekord jest próbką treningową specyficzną dla tabel.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna (`True` lub `False`).
* **Uwaga**: Odróżnia od ogólnych próbek treningowych, koncentrując się na danych tabelarycznych.
