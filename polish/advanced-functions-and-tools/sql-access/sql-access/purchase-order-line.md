# Purchase Order line

## Tabela `public.purchase_order_line`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `purchase_order_id`: internal
* `purchase_order_number`: internal
* `line_number`: internal
* `item_id`: internal
* `supplier_item_id`: internal
* `description`: internal
* `quantity`: double precision
* `unit_code`: internal
* `unit_price`: double precision
* `total_amount`: double precision
* `currency`: internal
* `status`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `open_quantity`: double precision
* `received_quantity`: double precision
* `confirmed_quantity`: double precision
* `note`: text
* `sub_org_id`: internal
* `sub_line_number`: internal
* `unit_price_per`: double precision
* `buyer_id`: internal
* `buyer_name`: internal
* `unit_code_price`: internal
* `geo_code`: internal
* `promised_delivery_date`: timestamp with time zone
* `delivery_method`: internal
* `requested_ship_date`: date
* `received_base_mou_quantity`: double precision
* `extended_amount`: double precision

### Analiza i opis

## Dokumentacja techniczna tabeli `public.purchase_order_line`

### Wprowadzenie

Tabela `public.purchase_order_line` służy do przechowywania szczegółowych informacji o każdej pozycji zamówienia zakupu. Rejestruje różne atrybuty pozycji zamówienia zakupu, takie jak szczegóły towaru, ilości, ceny i statusy. Tabela ta ma zasadnicze znaczenie dla zarządzania zamówieniami zakupu i śledzenia stanu ich realizacji w kontekście organizacji.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdej pozycji zamówienia zakupu.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Ciąg UUID jednoznacznie identyfikujący pozycję zamówienia zakupu.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z zamówieniem zakupu.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID odnoszący się do organizacji.

#### purchase\_order\_id

* **Znaczenie**: Identyfikator zamówienia zakupu, do którego należy pozycja.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg UUID odnoszący się do zamówienia zakupu.

#### purchase\_order\_number

* **Znaczenie**: Numer przypisany do zamówienia zakupu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący numer zamówienia zakupu.

#### line\_number

* **Znaczenie**: Numer wiersza pozycji w zamówieniu zakupu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków oznaczający kolejność wiersza w zamówieniu zakupu.

#### item\_id

* **Znaczenie**: Identyfikator zamawianego towaru.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg znaków reprezentujący kod towaru.

#### supplier\_item\_id

* **Znaczenie**: Identyfikator towaru specyficzny dla dostawcy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków, może mieć wartość null, jeśli nie został podany przez dostawcę.

#### description

* **Znaczenie**: Opis towaru.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Opis tekstowy towaru.

#### quantity

* **Znaczenie**: Liczba zamówionych jednostek.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa wskazująca zamówioną ilość.

#### unit\_code

* **Znaczenie**: Kod reprezentujący jednostkę miary towaru.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący jednostki, np. 'EA' dla sztuki.

#### unit\_price

* **Znaczenie**: Cena za jednostkę towaru.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa reprezentująca cenę za jednostkę.

#### total\_amount

* **Znaczenie**: Łączna kwota pozycji (ilość \* cena jednostkowa).
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa reprezentująca łączną kwotę.

#### currency

* **Znaczenie**: Waluta, w której dokonywany jest zakup.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący kod waluty, np. 'USD'.

#### status

* **Znaczenie**: Bieżący status pozycji zamówienia zakupu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków wskazujący status, np. 'Received', 'Invoiced'.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył wpis.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia wpisu.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej, może mieć wartość null, jeśli wpis nigdy nie był modyfikowany.

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia wpisu jako usuniętego.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej, może mieć wartość null, jeśli wpis nie został usunięty.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy wpis został oznaczony jako usunięty.
* **Rola**: Pole techniczne.
* **Typowa zawartość**: Wartość logiczna (true/false).

#### open\_quantity

* **Znaczenie**: Ilość jeszcze nieprzyjęta ani niezafakturowana.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa, zazwyczaj zero, jeśli pozycja została w pełni przyjęta.

#### received\_quantity

* **Znaczenie**: Ilość, która została przyjęta.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa wskazująca przyjętą ilość.

#### confirmed\_quantity

* **Znaczenie**: Ilość potwierdzona przez dostawcę.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa, może mieć wartość null, jeśli nie została potwierdzona.

#### note

* **Znaczenie**: Dodatkowe uwagi dotyczące pozycji zamówienia zakupu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Tekst, może zawierać specjalne instrukcje lub komentarze.

#### sub\_org\_id

* **Znaczenie**: Identyfikator podorganizacji powiązanej z pozycją zamówienia zakupu.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg znaków, potencjalnie null, jeśli nie dotyczy.

#### sub\_line\_number

* **Znaczenie**: Numer podwiersza w zamówieniu zakupu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący kolejność podwierszy.

#### unit\_price\_per

* **Znaczenie**: Bazowa cena jednostkowa towaru.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa reprezentująca bazową cenę jednostkową.

#### buyer\_id

* **Znaczenie**: Identyfikator nabywcy odpowiedzialnego za zakup.
* **Rola**: Klucz obcy.
* **Typowa zawartość**: Ciąg znaków reprezentujący identyfikator nabywcy.

#### buyer\_name

* **Znaczenie**: Nazwa odpowiedzialnego nabywcy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący nazwę nabywcy.

#### unit\_code\_price

* **Znaczenie**: Kod jednostki związany z ceną.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków, podobny do unit\_code.

#### geo\_code

* **Znaczenie**: Kod geograficzny dostawy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący lokalizację geograficzną.

#### promised\_delivery\_date

* **Znaczenie**: Obiecana data dostawy.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Znacznik czasu z informacją o strefie czasowej.

#### delivery\_method

* **Znaczenie**: Sposób dostawy pozycji zamówienia zakupu.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Ciąg znaków reprezentujący sposób dostawy.

#### requested\_ship\_date

* **Znaczenie**: Żądana data wysyłki.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość daty.

#### received\_base\_mou\_quantity

* **Znaczenie**: Ilość przyjęta w podstawowych jednostkach miary.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa wskazująca przyjętą ilość w podstawowej jednostce miary (MOU).

#### extended\_amount

* **Znaczenie**: Kwota rozszerzona pozycji.
* **Rola**: Pole opisowe.
* **Typowa zawartość**: Wartość liczbowa reprezentująca kwotę rozszerzoną, która może być równa total\_amount, jeśli nie obowiązują rabaty ani dodatkowe opłaty.
