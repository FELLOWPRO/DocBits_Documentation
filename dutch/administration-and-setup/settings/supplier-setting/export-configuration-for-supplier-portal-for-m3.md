# Exportconfiguratie voor Leverancierportaal voor M3

## Overzicht

Het exportconfiguratiebestand is een cruciaal onderdeel van het leveranciersportaal, dat definieert hoe gegevens worden gemapt tussen het leveranciersportaal en het ERP-systeem. Deze configuratie zorgt ervoor dat gegevens nauwkeurig worden overgedragen en gesynchroniseerd tussen systemen, wat zorgt voor soepele en efficiënte operaties.

## Structuur van het Configuratiebestand

Het exportconfiguratiebestand is gestructureerd als een JSON-object dat meerdere mappings bevat. Elke mapping is gekoppeld aan een specifiek programma in het ERP-systeem en definieert de uit te voeren acties, de te mappen velden en eventuele toe te passen voorwaarden.

## Belangrijke Componenten

### 1. Programma

* **Definitie**: Geeft het ERP-programma aan waarop de mapping van toepassing is.
* **Voorbeeld**: `"program": "CRS620MI"`

### 2. Acties

* **Definitie**: Definieert de acties die kunnen worden uitgevoerd, zoals het toevoegen of bijwerken van records.
*   **Voorbeeld**:

    ```json
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    }
    ```

### 3. Mapping

• Definitie: Geeft de mapping aan tussen velden in het ERP-systeem en velden in het leveranciersportaal.

• Componenten:

• erp\_field\_name: De veldnaam in het ERP-systeem.

• value\_field\_name: De bijbehorende veldnaam in het leveranciersportaal.

• value: Een statische waarde die moet worden gebruikt als er geen bijbehorend veld in het leveranciersportaal bestaat.

• if\_conditions: Optionele voorwaarden die de waarde bepalen op basis van bepaalde criteria.

• Voorbeeld:

```json
{
    "erp_field_name": "SUNO",
    "value_field_name": "supplier_number"
}
```

### 4. Voorwaardelijke Logica (if\_conditions)

• Definitie: Geeft voorwaarden aan die moeten worden vervuld om een bepaalde waarde te gebruiken.

• Componenten:

• field\_name: De veldnaam in het leveranciersportaal die wordt geëvalueerd.

• field\_value: De waarde die de voorwaarde activeert.

• then\_value: De waarde die moet worden gebruikt als aan de voorwaarde is voldaan.

• Voorbeeld:

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

### 5. Lussen (loop\_on)

• Definitie: Definieert de secties waar de configuratie over een lijst van items moet itereren, zoals adres- of referentiedetails.

• Voorbeeld:

```json
"loop_on": "address_details"
```

### 6. Gecalculeerde Velden (value\_field\_calculated)

• Definitie: Geeft velden aan die tijdens runtime moeten worden berekend, zoals het genereren van de huidige datum.

• Voorbeeld:

```json
{
    "erp_field_name": "STDT",
    "value_field_calculated": "now()"
}
```

### 7. Veldmappings met Lijsten (mapping\_field\_name en mapping\_list)

• Definitie: Maakt specifieke waarden van het leveranciersportaal aan de bijbehorende waarden in het ERP-systeem op basis van een vooraf gedefinieerde lijst.

• Componenten:

• mapping\_field\_name: Het veld dat de mapping bepaalt.

• mapping\_list: Een woordenboek dat waarden van het leveranciersportaal naar het ERP-systeem vertaalt.

• Voorbeeld:

```json
{
    "erp_field_name": "RFID",
    "mapping_field_name": "reference_type",
    "mapping_list": {
        "10": "AANKOOP",
        "15": "DLVRY PHN#",
        "20": "COA",
        "25": "QA",
        "30": "FINANCIËN",
        "35": "VERKOOP"
    }
}
```

## Voorbeeldconfiguratie Uiteenzetting

### Leverancier Toevoegen en Bijwerken (CRS620MI)

•  Program: CRS620MI

• Actions:

• Add Supplier: AddSupplier

• Update Supplier: UpdSupplier

• Mapping Fields:

• SUNO → supplier\_number

• SUNM → name

• CSCD → supplier\_country

• TINO → tax\_id

• Extra velden omvatten statische waarden en voorwaardelijke mappings.

### Adresdetails (CRS620MI)

• Loop On: _**address\_details**_

• Actions:

• Add Address: AddAddress

• Update Address: AddAddress

• Mapping Fields:

• SUNO → supplier\_number

• ADR1 → address

• TOWN → city

• Extra velden omvatten gecalculeerde velden zoals now() voor de huidige datum.

### Referentiedetails (CRS620MI)

• Loop On: _**reference\_details**_

• Actions:

• Add Supplier Reference: AddSupplierRef

• Update Supplier Reference: AddSupplierRef

• Mapping Fields:

• SUNO → supplier\_number

• RFTY → reference\_type

• RFID wordt gemapt met behulp van een lijst om types zoals “PURCHASING”, “QA” en “FINANCE” te vertalen.

## Gebruik van de Exportconfiguratie

### 1. Het Configuratiebestand Uploaden

#### **1. Navigeer naar Exportconfiguratie:**

• Ga naar de sectie Exportconfiguratie vanuit het hoofdmenu.

#### **2. Upload het Configuratiebestand:**

• Klik op de secties ION-Mapping Bestand of IDM Mapping Bestand om het respectieve configuratiebestand te uploaden.

#### **3. Sla de Configuratie op:**

• Klik na het uploaden op de Opslaan-knop om de configuratie toe te passen.

### 2. Standaard Sjablonen Gebruiken

• Klik op de knop Gebruik Standaard Sjabloon als je wilt terugkeren naar het standaardconfiguratiesjabloon dat door het systeem wordt aangeboden.

### 3. Het JSON Formatteren

• Gebruik de knop Formatteren om de JSON-code automatisch te formatteren voor betere leesbaarheid.

## Conclusie

Dit configuratiebestand is essentieel om ervoor te zorgen dat gegevens tussen het leveranciersportaal en het ERP-systeem correct worden gemapt en gesynchroniseerd. Door de structuur en belangrijke componenten te begrijpen, kunnen beheerders het exportproces effectief beheren en aanpassen aan hun specifieke zakelijke vereisten.

## Volledig Voorbeeld

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
            "10": "AANKOOP",
            "15": "DLVRY PHN#",
            "20": "COA",
            "25": "QA",
            "30": "FINANCIËN",
            "35": "VERKOOP"
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
