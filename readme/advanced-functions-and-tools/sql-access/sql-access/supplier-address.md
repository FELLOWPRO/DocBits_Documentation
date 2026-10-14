# Supplier address

## Kolumny

* `org_id`: ID to organisation
* `customer_number`: internal
* `supplier_number`: internal
* `address_id`: internal
* `supplier_name`: Supplier Name
* `address_1`: internal
* `address_2`: internal
* `address_3`: internal
* `address_4`: internal
* `zip_code`: internal
* `town_city`: internal
* `country_code`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: internal
* `id`: internal

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.supplier_address`

## Wprowadzenie

Tabela `public.supplier_address` służy do przechowywania informacji dotyczących adresów dostawców. Zawiera różne pola rejestrujące szczegóły, takie jak identyfikatory organizacji, numery klientów i dostawców, wiele wierszy adresu, dane kontaktowe, metadane utworzenia i modyfikacji oraz status usunięcia. Tabela ta jest prawdopodobnie używana w systemie do zarządzania informacjami o dostawcach i ich adresami, co może mieć kluczowe znaczenie dla logistyki, rozliczeń i kontaktu.

## Opis kolumn

### org_id
- **Znaczenie**: Ta kolumna przechowuje unikalny identyfikator organizacji.
- **Rola**: Klucz obcy, prawdopodobnie łączący z tabelą organizacji.
- **Typowa zawartość**: UUID reprezentujący organizację.

### customer_number
- **Znaczenie**: Ta kolumna może przechowywać unikalny numer przypisany klientom.
- **Rola**: Identyfikator klientów.
- **Typowa zawartość**: Ciąg alfanumeryczny reprezentujący numery klientów.

### supplier_number
- **Znaczenie**: Ta kolumna przechowuje unikalny numer przypisany dostawcom.
- **Rola**: Identyfikator dostawców.
- **Typowa zawartość**: Ciąg numeryczny reprezentujący numery dostawców.

### address_id
- **Znaczenie**: Ta kolumna prawdopodobnie przechowuje typ adresu, taki jak 'Discrete' lub 'Text'.
- **Rola**: Pole opisowe do kategoryzacji adresów.
- **Typowa zawartość**: Wartości takie jak 'Discrete', 'Text'.

### supplier_name
- **Znaczenie**: Ta kolumna przechowuje nazwę dostawcy.
- **Rola**: Pole opisowe do identyfikacji dostawcy.
- **Typowa zawartość**: Nazwa dostawcy, np. "Cake Corp. GmbH Qualitätsstrawberrys".

### address_1
- **Znaczenie**: Ta kolumna przechowuje pierwszy wiersz adresu dostawcy.
- **Rola**: Pole opisowe z informacjami o adresie.
- **Typowa zawartość**: Adres ulicy, np. "Irrweg. 42, D-12345 Blastadt".

### address_2
- **Znaczenie**: Ta kolumna przechowuje drugi wiersz adresu dostawcy, jeśli dotyczy.
- **Rola**: Pole uzupełniające z informacjami o adresie.
- **Typowa zawartość**: Dodatkowe szczegóły adresu, często pozostawione puste.

### address_3
- **Znaczenie**: Ta kolumna przechowuje trzeci wiersz adresu dostawcy, jeśli dotyczy.
- **Rola**: Pole uzupełniające z informacjami o adresie.
- **Typowa zawartość**: Dodatkowe szczegóły adresu, często pozostawione puste.

### address_4
- **Znaczenie**: Ta kolumna przechowuje czwarty wiersz adresu dostawcy, jeśli dotyczy.
- **Rola**: Pole uzupełniające z informacjami o adresie.
- **Typowa zawartość**: Dodatkowe szczegóły adresu, często pozostawione puste.

### zip_code
- **Znaczenie**: Ta kolumna przechowuje kod pocztowy adresu dostawcy.
- **Rola**: Pole opisowe do identyfikacji geograficznej.
- **Typowa zawartość**: Numeryczny kod pocztowy, np. "06449".

### town_city
- **Znaczenie**: Ta kolumna przechowuje nazwę miejscowości lub miasta adresu dostawcy.
- **Rola**: Pole opisowe do identyfikacji geograficznej.
- **Typowa zawartość**: Nazwa miejscowości lub miasta, np. "Aschersleben".

### country_code
- **Znaczenie**: Ta kolumna przechowuje kod kraju ISO adresu dostawcy.
- **Rola**: Pole opisowe do identyfikacji kraju.
- **Typowa zawartość**: Dwuliterowy kod kraju, np. "DE".

### created_by
- **Znaczenie**: Ta kolumna przechowuje identyfikator użytkownika lub systemu, który utworzył rekord.
- **Rola**: Pole techniczne do śledzenia utworzenia rekordu.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### created_on
- **Znaczenie**: Ta kolumna przechowuje znacznik czasu utworzenia rekordu.
- **Rola**: Pole techniczne do śledzenia czasu utworzenia rekordu.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową, np. "2021-11-25 11:24:33 UTC".

### last_modified_on
- **Znaczenie**: Ta kolumna przechowuje znacznik czasu ostatniej modyfikacji rekordu.
- **Rola**: Pole techniczne do śledzenia czasu ostatniej aktualizacji.
- **Typowa zawartość**: Znacznik czasu ze strefą czasową, często pozostawiony jako `None`.

### is_deleted
- **Znaczenie**: Ta kolumna wskazuje, czy rekord został oznaczony jako usunięty.
- **Rola**: Pole techniczne dla funkcji miękkiego usuwania.
- **Typowa zawartość**: Wartość logiczna, np. `False`.

### sub_org_id
- **Znaczenie**: Ta kolumna przechowuje identyfikator podorganizacji, jeśli dotyczy.
- **Rola**: Klucz obcy lub identyfikator podorganizacji.
- **Typowa zawartość**: UUID, często pozostawiony pusty.

### id
- **Znaczenie**: Ta kolumna przechowuje unikalny identyfikator rekordu.
- **Rola**: Klucz główny tabeli.
- **Typowa zawartość**: UUID reprezentujący rekord.

```
