# Zamówienie sprzedaży

## Tabela `public.sales_order`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `location_id`: internal
* `order_number`: internal
* `customer_purchase_order`: internal
* `customer_id`: internal
* `customer_name`: internal
* `warehouse_id`: internal
* `warehouse_name`: internal
* `transportation_method`: internal
* `requested_delivery_date`: znacznik czasu ze strefą czasową
* `order_date`: znacznik czasu ze strefą czasową
* `sales_person_id`: internal
* `sales_person_name`: internal
* `ship_to_party_id`: internal
* `ship_to_party_name`: internal
* `ship_to_party_city`: internal
* `ship_to_party_state`: internal
* `ship_to_party_country`: internal
* `ship_to_party_zip`: internal
* `status`: internal
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `deleted_on`: znacznik czasu ze strefą czasową
* `preview_path`: internal
* `last_modified_by`: internal
* `deleted_by`: internal

### Analiza i opis

## Dokumentacja techniczna tabeli `public.sales_order`

### Wprowadzenie

Tabela `public.sales_order` służy do rejestrowania i przechowywania informacji związanych z zamówieniami sprzedaży w kontekście biznesowym. Obejmuje to szczegóły dotyczące zamówienia, klienta, logistyki oraz różnych metadanych związanych z cyklem życia zamówienia. Tabela stanowi centralne repozytorium do śledzenia statusu i historii transakcji sprzedaży.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego zamówienia sprzedaży.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID (np. `'6ffe4673-7563-44dc-8e71-855e8f25534a'`).

#### org\_id

* **Znaczenie**: Identyfikator organizacji, która utworzyła zamówienie sprzedaży.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID reprezentujący organizację (np. `'23f3d697-7411-4c95-981d-faf089d266be'`).

#### sub\_org\_id

* **Znaczenie**: Identyfikator podorganizacji, jeśli dotyczy.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Może mieć wartość `NULL`, jeśli nie dotyczy.

#### location\_id

* **Znaczenie**: Identyfikator lokalizacji powiązanej z zamówieniem sprzedaży.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Kod w postaci ciągu znaków reprezentujący lokalizację (np. `'028'`).

#### order\_number

* **Znaczenie**: Unikalny numer przypisany do zamówienia sprzedaży.
* **Rola**: Pole techniczne do śledzenia zamówienia.
* **Typowa zawartość**: Ciąg znaków (np. `'0010174175'`).

#### customer\_purchase\_order

* **Znaczenie**: Numer referencyjny zamówienia zakupu klienta.
* **Rola**: Pole techniczne do odwołań krzyżowych.
* **Typowa zawartość**: Ciąg znaków (np. `'1YFNC3'`).

#### customer\_id

* **Znaczenie**: Identyfikator klienta składającego zamówienie.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Kod w postaci ciągu znaków (np. `'35623000'`).

#### customer\_name

* **Znaczenie**: Nazwa klienta.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków (np. `'DOLLAR GENERAL'`).

#### warehouse\_id

* **Znaczenie**: Identyfikator magazynu odpowiedzialnego za realizację zamówienia.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Kod w postaci ciągu znaków (np. `'028'`).

#### warehouse\_name

* **Znaczenie**: Nazwa magazynu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków (np. `'USCS - DENTON, TX'`).

#### transportation\_method

* **Znaczenie**: Sposób transportu użyty do dostarczenia zamówienia.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Kod w postaci ciągu znaków (np. `'001'`).

#### requested\_delivery\_date

* **Znaczenie**: Data dostawy żądana przez klienta.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Znacznik czasu (np. `None`).

#### order\_date

* **Znaczenie**: Data złożenia zamówienia.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Znacznik czasu (np. `datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`).

#### sales\_person\_id

* **Znaczenie**: Identyfikator sprzedawcy obsługującego zamówienie.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg znaków (np. `'ROBERTDOCK'`).

#### sales\_person\_name

* **Znaczenie**: Imię i nazwisko sprzedawcy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków (np. `'ROBERT DOCKINS'`).

#### ship\_to\_party\_id

* **Znaczenie**: Identyfikator strony, do której wysyłane jest zamówienie.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg znaków (np. `'35623000 009'`).

#### ship\_to\_party\_name

* **Znaczenie**: Nazwa strony, do której wysyłane jest zamówienie.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków (np. `'DOLLAR GENERAL DC 98061/96460'`).

#### ship\_to\_party\_city

* **Znaczenie**: Miasto adresu dostawy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków (np. `'SAN ANTONIO'`).

#### ship\_to\_party\_state

* **Znaczenie**: Stan (województwo) adresu dostawy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Może mieć wartość `NULL`.

#### ship\_to\_party\_country

* **Znaczenie**: Kraj adresu dostawy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków (np. `'US'`).

#### ship\_to\_party\_zip

* **Znaczenie**: Kod pocztowy adresu dostawy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków (np. `'78218'`).

#### status

* **Znaczenie**: Bieżący status zamówienia sprzedaży.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków (np. `'Allocated'`).

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył wpis.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Liczba całkowita (np. `1`).

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia wpisu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu (np. `datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`).

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu (np. `datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`).

#### is\_deleted

* **Znaczenie**: Flaga wskazująca, czy zamówienie zostało oznaczone jako usunięte.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna (np. `False`).

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia zamówienia jako usuniętego.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Data domyślna, jeśli zamówienie nie zostało usunięte (np. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`).

#### preview\_path

* **Znaczenie**: Ścieżka do dokumentu podglądu zamówienia sprzedaży.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący ścieżkę do pliku (np. `'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`).

#### last\_modified\_by

* **Znaczenie**: Identyfikator użytkownika, który ostatnio zmodyfikował wpis.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Może mieć wartość `NULL`.

#### deleted\_by

* **Znaczenie**: Identyfikator użytkownika, który oznaczył wpis jako usunięty.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Może mieć wartość `NULL`.
