# Eksport konfiguracji dla Portalu Dostawcy

## Przegląd

Plik konfiguracji eksportu jest kluczowym elementem w portalu dostawcy, definiującym, w jaki sposób dane są mapowane między portalem dostawcy a systemem ERP. Ta konfiguracja zapewnia, że dane są dokładnie przesyłane i synchronizowane między systemami, co umożliwia płynne i efektywne operacje.

## Struktura pliku konfiguracyjnego

Plik konfiguracji eksportu jest zorganizowany jako obiekt JSON, który zawiera wiele mapowań. Każde mapowanie jest powiązane z określonym programem w systemie ERP i definiuje działania do wykonania, pola do zmapowania oraz wszelkie warunki do zastosowania.

## Kluczowe komponenty

### 1. Program

* **Definicja**: Określa program ERP, do którego odnosi się mapowanie.
* **Przykład**: `"program": "CRS620MI"`

### 2. Działania

* **Definicja**: Definiuje działania, które można wykonać, takie jak dodawanie lub aktualizowanie rekordów.
*   **Przykład**:

    ```json
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    }
    ```

### 3. Mapowanie

• Definicja: Określa mapowanie między polami w systemie ERP a polami w portalu dostawcy.

• Komponenty:

• erp\_field\_name: Nazwa pola w systemie ERP.

• value\_field\_name: Odpowiednia nazwa pola w portalu dostawcy.

• value: Statyczna wartość, która ma być używana, jeśli nie istnieje odpowiednie pole w portalu dostawcy.

• if\_conditions: Opcjonalne warunki, które określają wartość na podstawie określonych kryteriów.

• Przykład:

```json
{
    "erp_field_name": "SUNO",
    "value_field_name": "supplier_number"
}
```

### 4. Logika warunkowa (if\_conditions)

• Definicja: Określa warunki, które muszą być spełnione, aby użyć określonej wartości.

• Komponenty:

• field\_name: Nazwa pola w portalu dostawcy, które jest oceniane.

• field\_value: Wartość, która uruchamia warunek.

• then\_value: Wartość do użycia, jeśli warunek jest spełniony.

• Przykład:

```json
{
    "erp_field_name": "SUTY",
    "value": "0",
    "if_conditions": [{
        "field_name": "supplier_group",
        "field_value": "FRT",
        "then_value": "5"
    }]
}
```

### 5. Pętle (loop\_on)

• Definicja: Definiuje sekcje, w których konfiguracja powinna iterować po liście elementów, takich jak szczegóły adresu lub referencji.

• Przykład:

```json
"loop_on": "address_details"
```

### 6. Pola obliczeniowe (value\_field\_calculated)

• Definicja: Określa pola, które powinny być obliczane w czasie rzeczywistym, takie jak generowanie bieżącej daty.

• Przykład:

```json
{
    "erp_field_name": "STDT",
    "value_field_calculated": "now()"
}
```

### 7. Mapowania pól z listami (mapping\_field\_name i mapping\_list)

• Definicja: Mapuje konkretne wartości z portalu dostawcy do odpowiadających wartości w systemie ERP na podstawie wcześniej zdefiniowanej listy.

• Komponenty:

• mapping\_field\_name: Pole, które określa mapowanie.

• mapping\_list: Słownik, który tłumaczy wartości z portalu dostawcy na system ERP.

• Przykład:

```json
{
    "erp_field_name": "RFID",
    "mapping_field_name": "reference_type",
    "mapping_list": {
        "10": "PURCHASING",
        "15": "DLVRY PHN#",
        "20": "COA",
        "25": "QA",
        "30": "FINANCE",
        "35": "SALES"
    }
}
```

## Przykład analizy konfiguracji

### Dodawanie i aktualizacja dostawcy (CRS620MI)

• Program: CRS620MI

• Działania:

• Dodaj dostawcę: AddSupplier

• Zaktualizuj dostawcę: UpdSupplier

• Mapowanie pól:

• SUNO → supplier\_number

• SUNM → name

• CSCD → supplier\_country

• TINO → tax\_id

• Dodatkowe pola obejmują statyczne wartości i mapowania warunkowe.

### Szczegóły adresu (CRS620MI)

• Pętla: _**address\_details**_

• Działania:

• Dodaj adres: AddAddress

• Zaktualizuj adres: AddAddress

• Mapowanie pól:

• SUNO → supplier\_number

• ADR1 → address

• TOWN → city

• Dodatkowe pola obejmują pola obliczeniowe, takie jak now() dla bieżącej daty.

### Szczegóły referencji (CRS620MI)

• Pętla: _**reference\_details**_

• Działania:

• Dodaj referencję dostawcy: AddSupplierRef

• Zaktualizuj referencję dostawcy: AddSupplierRef

• Mapowanie pól:

• SUNO → supplier\_number

• RFTY → reference\_type

• RFID jest mapowane przy użyciu listy do tłumaczenia typów, takich jak „PURCHASING”, „QA” i „FINANCE”.

## Używanie konfiguracji eksportu

### 1. Przesyłanie pliku konfiguracyjnego

#### 1. Przejdź do konfiguracji eksportu:

• Przejdź do sekcji konfiguracji eksportu z głównego menu.

#### 2. Prześlij plik konfiguracyjny:

• Kliknij na sekcje pliku ION-Mapping lub IDM Mapping, aby przesłać odpowiedni plik konfiguracyjny.

#### 3. Zapisz konfigurację:

• Po przesłaniu kliknij przycisk Zapisz, aby zastosować konfigurację.

### 2. Używanie domyślnych szablonów

• Kliknij przycisk Użyj domyślnego szablonu, jeśli chcesz powrócić do domyślnego szablonu konfiguracji dostarczonego przez system.

### 3. Formatowanie JSON

• Użyj przycisku Formatuj, aby automatycznie sformatować kod JSON dla lepszej czytelności.

## Podsumowanie

Ten plik konfiguracyjny jest niezbędny do zapewnienia, że dane między portalem dostawcy a systemem ERP są poprawnie mapowane i synchronizowane. Rozumiejąc strukturę i kluczowe komponenty, administratorzy mogą skutecznie zarządzać i dostosowywać proces eksportu, aby spełnić swoje specyficzne wymagania biznesowe.

## Pełny przykład&#x20;

```json
[{
    "program": "CRS620MI",
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "value_field_name": "supplier_number"
    }, {
        "erp_field_name": "SUNM",
        "value_field_name": "name"
    }, {
        "erp_field_name": "SUTY",
        "value": "0",
        "if_conditions": [{
            "field_name": "supplier_group",
            "field_value": "FRT",
            "then_value": "5"
        }]
    }, {
        "erp_field_name": "CSCD",
        "value_field_name": "supplier_country"
    }, {
        "erp_field_name": "DTFM",
        "value_field_name": "date_format"
    }, {
        "erp_field_name": "ORTY",
        "value": "F20"
    }, {
        "erp_field_name": "DT4T",
        "value": "1"
    }, {
        "erp_field_name": "DTCD",
        "value": "2"
    }, {
        "erp_field_name": "CUCD",
        "value_field_name": "currency"
    }, {
        "erp_field_name": "TINO",
        "value_field_name": "tax_id"
    }, {
        "erp_field_name": "PHNO",
        "value_field_name": "supplier_phone"
    }, {
        "erp_field_name": "CRTP",
        "value": "1"
    }, {
        "erp_field_name": "ATPR",
        "value": "1"
    }, {
        "erp_field_name": "SUCL",
        "value_field_name": "supplier_group"
    }, {
        "erp_field_name": "LNCD",
        "value_field_name": "language"
    }, {
        "erp_field_name": "CONO",
        "value": "781_DDD"
    }, {
        "erp_field_name": "TEDL",
        "value": "FOB"
    }, {
        "erp_field_name": "TEPY",
        "value_field_name": "payment_term"
    }, {
        "erp_field_name": "TEPA",
        "value": "001"
    }, {
        "erp_field_name": "PYME",
        "value": "CRP"
    }]
}, {
    "program": "CRS620MI",
    "loop_on": "address_details",
    "actions": {
        "add": "AddAddress",
        "update": "AddAddress"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "main_value_field": "supplier_number"
    }, {
        "erp_field_name": "ADTE",
        "value_field_name": "address_type"
    }, {
        "erp_field_name": "ADID",
        "value_field_name": "address_type",
        "if_conditions": [{
            "field_name": "address_type",
            "field_value": "10",
            "then_value": ""
        }]
    }, {
        "erp_field_name": "STDT",
        "value_field_calculated": "now()"
    }, {
        "erp_field_name": "ADR1",
        "value_field_name": "address"
    }, {
        "erp_field_name": "TOWN",
        "value_field_name": "city"
    }, {
        "erp_field_name": "ECAR",
        "value_field_name": "state"
    }, {
        "erp_field_name": "PONO",
        "value_field_name": "postal_code"
    }, {
        "erp_field_name": "CSCD",
        "value_field_name": "supplier_country"
    }]
}, {
    "program": "CRS620MI",
    "loop_on": "reference_details",
    "actions": {
        "add": "AddSupplierRef",
        "update": "AddSupplierRef"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "main_value_field": "supplier_number"
    }, {
        "erp_field_name": "RFTY",
        "value_field_name": "reference_type"
    }, {
        "erp_field_name": "RFID",
        "mapping_field_name": "reference_type",
        "mapping_list": {
            "10": "PURCHASING",
            "15": "DLVRY PHN#",
            "20": "COA",
            "25": "QA",
            "30": "FINANCE",
            "35": "SALES"
        }
    }, {
        "erp_field_name": "YRE1",
        "value_field_name": "reference_name"
    }, {
        "erp_field_name": "PHNO",
        "value_field_name": "telephone_no"
    }, {
        "erp_field_name": "EMAL",
        "value_field_name": "email_address"
    }]
}]