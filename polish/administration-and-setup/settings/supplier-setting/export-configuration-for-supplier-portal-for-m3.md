# Eksport konfiguracji dla Portalu Dostawcy

<figure><img src="../../../.gitbook/assets/supplier_export_configuration.png" alt="Supplier Export Configuration"><figcaption><p>Strona Supplier Export Configuration</p></figcaption></figure>

## Przegląd

Plik konfiguracji eksportu jest kluczowym elementem w portalu dostawcy, definiującym, w jaki sposób dane są mapowane między portalem dostawcy a systemem ERP. Ta konfiguracja zapewnia, że dane są dokładnie przesyłane i synchronizowane między systemami, co umożliwia płynne i efektywne operacje.

## Struktura pliku konfiguracyjnego

Plik konfiguracji eksportu jest zorganizowany jako obiekt JSON, który zawiera wiele mapowań. Każde mapowanie jest powiązane z określonym programem w systemie ERP i definiuje działania do wykonania, pola do zmapowania oraz wszelkie warunki do zastosowania.

## Kluczowe komponenty

### 1. Program

* **Definicja**: Określa program ERP, do którego odnosi się mapowanie.
* **Przykład**: `"program": "CRS620MI"`

### 2. Actions

* **Definicja**: Definiuje działania, które można wykonać, takie jak dodawanie lub aktualizowanie rekordów.
*   **Przykład**:

    ```json
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    }
    ```

### 3. Mapping

• Definicja: Określa mapowanie między polami w systemie ERP a polami w portalu dostawcy.

• Komponenty:

• erp\_field\_name: Nazwa pola w systemie ERP.

• value\_field\_name: Odpowiadająca nazwa pola w portalu dostawcy.

• value: Wartość statyczna używana, gdy w portalu dostawcy nie istnieje odpowiadające pole.

• if\_conditions: Opcjonalne warunki, które określają wartość na podstawie określonych kryteriów.

• Przykład:

```json
{
    "erp_field_name": "SUNO",
    "value_field_name": "supplier_number"
}
```

### 4. Logika warunkowa (if\_conditions)

• Definicja: Określa warunki, które muszą zostać spełnione, aby została użyta dana wartość.

• Komponenty:

• field\_name: Nazwa pola w portalu dostawcy, które jest oceniane.

• field\_value: Wartość, która uruchamia warunek.

• then\_value: Wartość użyta, gdy warunek jest spełniony.

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

• Definicja: Określa sekcje, w których konfiguracja ma iterować po liście elementów, takich jak szczegóły adresu lub referencji.

• Przykład:

```json
"loop_on": "address_details"
```

### 6. Pola obliczane (value\_field\_calculated)

• Definicja: Określa pola, które mają być obliczane w czasie wykonania, na przykład generowanie bieżącej daty.

• Przykład:

```json
{
    "erp_field_name": "STDT",
    "value_field_calculated": "now()"
}
```

### 7. Mapowania pól z listami (mapping\_field\_name i mapping\_list)

• Definicja: Mapuje określone wartości z portalu dostawcy na odpowiadające wartości w systemie ERP na podstawie predefiniowanej listy.

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

## Analiza przykładowej konfiguracji

### Dodawanie i aktualizacja dostawcy (CRS620MI)

• Program: CRS620MI

• Actions:

• Add Supplier: AddSupplier

• Update Supplier: UpdSupplier

• Pola mapowania:

• SUNO → supplier\_number

• SUNM → name

• CSCD → supplier\_country

• TINO → tax\_id

• Dodatkowe pola obejmują wartości statyczne i mapowania warunkowe.

### Szczegóły adresu (CRS620MI)

• Loop On: _**address\_details**_

• Actions:

• Add Address: AddAddress

• Update Address: AddAddress

• Pola mapowania:

• SUNO → supplier\_number

• ADR1 → address

• TOWN → city

• Dodatkowe pola obejmują pola obliczane, takie jak now() dla bieżącej daty.

### Szczegóły referencji (CRS620MI)

• Loop On: _**reference\_details**_

• Actions:

• Add Supplier Reference: AddSupplierRef

• Update Supplier Reference: AddSupplierRef

• Pola mapowania:

• SUNO → supplier\_number

• RFTY → reference\_type

• RFID jest mapowane za pomocą listy, aby przetłumaczyć typy takie jak „PURCHASING”, „QA” i „FINANCE”.

## Korzystanie z konfiguracji eksportu

### 1. Przesyłanie pliku konfiguracyjnego

#### 1. Przejdź do Export Configuration:

• Przejdź z menu głównego do sekcji Export Configuration.

#### 2. Prześlij plik konfiguracyjny:

• Kliknij sekcje ION-Mapping File lub IDM Mapping File, aby przesłać odpowiedni plik konfiguracyjny.

#### 3. Zapisz konfigurację:

• Po przesłaniu kliknij przycisk Save, aby zastosować konfigurację.

### 2. Korzystanie z szablonów domyślnych

• Kliknij przycisk Use Default Template, jeśli chcesz wrócić do domyślnego szablonu konfiguracji dostarczanego przez system.

### 3. Formatowanie JSON

• Użyj przycisku Format, aby automatycznie sformatować kod JSON w celu lepszej czytelności.

## Podsumowanie

Ten plik konfiguracyjny jest niezbędny, aby dane między portalem dostawcy a systemem ERP były poprawnie mapowane i synchronizowane. Dzięki zrozumieniu struktury i kluczowych komponentów administratorzy mogą skutecznie zarządzać procesem eksportu i dostosowywać go do swoich specyficznych wymagań biznesowych.

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
```
