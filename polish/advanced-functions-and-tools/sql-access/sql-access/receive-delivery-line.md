# Pozycja przyjęcia dostawy

## Tabela `public.receive_delivery_line`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `receive_delivery_id`: internal
* `delivery_number`: internal
* `line_number`: internal
* `item_id`: internal
* `description`: internal
* `shipped_quantity`: double precision
* `status`: internal
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_on`: znacznik czasu ze strefą czasową
* `deleted_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `purchase_order`: internal
* `sequence_number`: internal
* `sub_org_id`: internal
* `shipped_quantity_unit_code`: internal
* `packing_slip_quantity`: double precision
* `packing_slip_quantity_unit_code`: internal
* `received_quantity`: double precision
* `received_quantity_unit_code`: internal
* `purchase_order_line_number`: internal
* `status_effective_from`: znacznik czasu ze strefą czasową
* `purchase_order_sub_line_number`: internal
* `invoiced_quantity`: double precision
* `invoice_matching_status`: internal
* `open_quantity`: double precision
* `last_modified_by`: internal
* `deleted_by`: internal

### Analiza i opis

## Dokumentacja tabeli: `public.receive_delivery_line`

### Wprowadzenie

Tabela `public.receive_delivery_line` jest prawdopodobnie szczegółowym rejestrem pozycji dostaw i przyjęć związanych z operacjami logistycznymi i łańcuchem dostaw organizacji. Każdy wiersz tabeli reprezentuje konkretną pozycję dostawy i rejestruje szczegóły, takie jak opis towaru, ilości wysłane i przyjęte oraz różne pola statusu. Tabela stanowi istotny element śledzenia przepływu towarów od wysyłki do przyjęcia, w tym fakturowania i zarządzania zamówieniami.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdej pozycji dostawy.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Unikalny identyfikator UUID.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z dostawą.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: UUID reprezentujący organizację.

#### receive\_delivery\_id

* **Znaczenie**: Identyfikator łączący z całą transakcją dostawy.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: UUID powiązany z konkretną transakcją dostawy.

#### delivery\_number

* **Znaczenie**: Unikalny numer przypisany do dostawy.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Ciąg znaków reprezentujący numer dostawy.

#### line\_number

* **Znaczenie**: Konkretny numer wiersza w dostawie.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Ciąg numeryczny wskazujący kolejność wiersza.

#### item\_id

* **Znaczenie**: Identyfikator wysyłanego towaru.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Ciąg numeryczny odpowiadający towarowi.

#### description

* **Znaczenie**: Opis towaru.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Opis tekstowy towaru, np. "FLOUR, WHEAT, UN-BLEACHED ENRICHED, BULK".

#### shipped\_quantity

* **Znaczenie**: Ilość towaru, która została wysłana.
* **Rola**: Pole ilościowe.
* **Typowa zawartość**: Liczba dziesiętna wskazująca wysłaną ilość.

#### status

* **Znaczenie**: Bieżący status pozycji dostawy.
* **Rola**: Pole statusu.
* **Typowa zawartość**: Tekst, np. "Received".

#### created\_by

* **Znaczenie**: Identyfikator użytkownika lub systemu, który utworzył rekord.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia rekordu.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Data i godzina ze strefą czasową.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Data i godzina ze strefą czasową.

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia rekordu jako usuniętego.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: Data i godzina ze strefą czasową, często null, chyba że rekord został usunięty.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy rekord został oznaczony jako usunięty.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna, true lub false.

#### purchase\_order

* **Znaczenie**: Odwołanie do powiązanego zamówienia zakupu.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Ciąg alfanumeryczny reprezentujący numer zamówienia zakupu.

#### sequence\_number

* **Znaczenie**: Numer kolejny pozycji dostawy.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Ciąg numeryczny, często null.

#### sub\_org\_id

* **Znaczenie**: Identyfikator zaangażowanej podorganizacji.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: UUID, często null.

#### shipped\_quantity\_unit\_code

* **Znaczenie**: Jednostka miary wysłanej ilości.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Kod reprezentujący jednostki, np. "LBP".

#### packing\_slip\_quantity

* **Znaczenie**: Ilość zgodnie z listem przewozowym (packing slip).
* **Rola**: Pole ilościowe.
* **Typowa zawartość**: Liczba dziesiętna, często null.

#### packing\_slip\_quantity\_unit\_code

* **Znaczenie**: Kod jednostki ilości z listu przewozowego.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Kod reprezentujący jednostki, często null.

#### received\_quantity

* **Znaczenie**: Ilość towarów faktycznie przyjętych.
* **Rola**: Pole ilościowe.
* **Typowa zawartość**: Liczba dziesiętna wskazująca przyjętą ilość.

#### received\_quantity\_unit\_code

* **Znaczenie**: Kod jednostki przyjętej ilości.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Kod reprezentujący jednostki, np. "LBP".

#### purchase\_order\_line\_number

* **Znaczenie**: Numer wiersza w zamówieniu zakupu.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Ciąg numeryczny.

#### status\_effective\_from

* **Znaczenie**: Data i godzina, od której obowiązuje status.
* **Rola**: Pole statusu.
* **Typowa zawartość**: Data i godzina ze strefą czasową, często null.

#### purchase\_order\_sub\_line\_number

* **Znaczenie**: Numer podwiersza w zamówieniu zakupu.
* **Rola**: Pole referencyjne.
* **Typowa zawartość**: Ciąg numeryczny, często "000".

#### invoiced\_quantity

* **Znaczenie**: Ilość, która została zafakturowana.
* **Rola**: Pole ilościowe.
* **Typowa zawartość**: Liczba dziesiętna.

#### invoice\_matching\_status

* **Znaczenie**: Status procesu dopasowania faktury.
* **Rola**: Pole statusu.
* **Typowa zawartość**: Tekstowy kod statusu, np. "9.0".

#### open\_quantity

* **Znaczenie**: Ilość, która pozostaje otwarta lub nie została jeszcze przetworzona.
* **Rola**: Pole ilościowe.
* **Typowa zawartość**: Liczba dziesiętna.

#### last\_modified\_by

* **Znaczenie**: Identyfikator użytkownika, który ostatnio zmodyfikował rekord.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: UUID użytkownika, często null.

#### deleted\_by

* **Znaczenie**: Identyfikator użytkownika, który oznaczył rekord jako usunięty.
* **Rola**: Pole audytowe.
* **Typowa zawartość**: UUID użytkownika, często null.
