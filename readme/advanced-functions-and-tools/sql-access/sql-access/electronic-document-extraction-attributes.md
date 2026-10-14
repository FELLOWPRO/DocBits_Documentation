# Electronic document extraction attributes

## Tabela `public.electronic_document_extraction_attributes`

### Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `doc_type_key`: wewnętrzne
* `sub_doc_type_key`: wewnętrzne
* `electronic_document_type`: wewnętrzne
* `attribute_name`: wewnętrzne
* `attribute_type`: wewnętrzne
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `last_modified_by`: wewnętrzne
* `deleted_by`: wewnętrzne

### Analiza i opis

## Dokumentacja techniczna tabeli `public.electronic_document_extraction_attributes`

### Wprowadzenie

Tabela `public.electronic_document_extraction_attributes` służy do zarządzania atrybutami związanymi z ekstrakcją dokumentów elektronicznych. Obejmuje to przechowywanie różnych cech i metadanych dotyczących typów dokumentów elektronicznych, metod ich przetwarzania i powiązanych organizacji. Tabela wspiera funkcje takie jak identyfikacja typu dokumentu, transformacje, podglądy i opisy struktury, które są niezbędne do skutecznej obsługi dokumentów elektronicznych.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący każdy wpis atrybutu ekstrakcji dokumentu.
* **Uwaga**: Stanowi unikalne odwołanie do każdego wiersza.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z atrybutami dokumentu.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID łączący z powiązaną organizacją.
* **Uwaga**: Łączy atrybuty ekstrakcji dokumentu z konkretną organizacją.

#### doc\_type\_key

* **Znaczenie**: Klucz reprezentujący typ dokumentu.
* **Rola**: Identyfikator służący do kategoryzowania dokumentów.
* **Typowa zawartość**: Ciąg znaków wskazujący typ dokumentu, np. 'INVOICE' lub 'ORDER\_CONFIRMATION'.
* **Uwaga**: Służy do określenia kategorii dokumentu.

#### sub\_doc\_type\_key

* **Znaczenie**: Reprezentuje podkategorię głównego typu dokumentu.
* **Rola**: Identyfikator dalszej klasyfikacji.
* **Typowa zawartość**: Null lub ciąg znaków określający konkretny podtyp.
* **Uwaga**: Przydatne do uzyskania większej szczegółowości klasyfikacji dokumentów.

#### electronic\_document\_type

* **Znaczenie**: Format lub standard dokumentu elektronicznego.
* **Rola**: Pole opisowe formatu dokumentu.
* **Typowa zawartość**: Ciągi znaków, takie jak 'EDI' lub 'FACTURX'.
* **Uwaga**: Wskazuje standard lub format dokumentu.

#### attribute\_name

* **Znaczenie**: Nazwa atrybutu związanego z procesem ekstrakcji dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciągi znaków, takie jak 'PREVIEW' lub 'TRANSFORMATION'.
* **Uwaga**: Opisuje konkretny atrybut związany z obsługą dokumentu.

#### attribute\_type

* **Znaczenie**: Typ atrybutu związanego z ekstrakcją dokumentu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciągi znaków, takie jak 'XSLT' lub 'JSON'.
* **Uwaga**: Określa format danych lub metodę używaną dla atrybutu.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył rekord.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.
* **Uwaga**: Rejestruje, kto pierwotnie utworzył rekord.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia rekordu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina w UTC.
* **Uwaga**: Wskazuje czas utworzenia rekordu.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina w UTC lub null, jeśli rekord nie był modyfikowany.
* **Uwaga**: Rejestruje najnowszą aktualizację rekordu.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy rekord został oznaczony jako usunięty.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna, `True` lub `False`.
* **Uwaga**: Pomaga w obsłudze miękkiego usuwania.

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia rekordu jako usuniętego.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data i godzina w UTC lub domyślna, bardzo odległa data z przeszłości, jeśli rekord nie został usunięty.
* **Uwaga**: Służy do śledzenia, kiedy rekord został usunięty.

#### last\_modified\_by

* **Znaczenie**: Identyfikator użytkownika, który ostatni zmodyfikował rekord.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID lub null, jeśli rekord nie był modyfikowany.
* **Uwaga**: Wskazuje użytkownika odpowiedzialnego za ostatnią modyfikację.

#### deleted\_by

* **Znaczenie**: Identyfikator użytkownika, który oznaczył rekord jako usunięty.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID lub null, jeśli rekord nie został usunięty.
* **Uwaga**: Rejestruje, kto wykonał akcję usunięcia.

Niniejsza dokumentacja zawiera szczegółowy przegląd struktury tabeli i jej kolumn, ułatwiając programistom i administratorom baz danych lepsze zrozumienie i wykorzystanie danych.
