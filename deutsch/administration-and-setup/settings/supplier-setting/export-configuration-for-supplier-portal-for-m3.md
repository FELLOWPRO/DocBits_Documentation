# Export Konfiguration für Lieferanten Portal M3

**Übersicht**\
Die Exportkonfigurationsdatei ist ein entscheidendes Element im Lieferantenportal, das definiert, wie Daten zwischen dem Lieferantenportal und dem ERP-System zugeordnet werden. Diese Konfiguration stellt sicher, dass Daten genau zwischen den Systemen übertragen und synchronisiert werden, was einen reibungslosen und effizienten Betrieb ermöglicht.

**Struktur der Konfigurationsdatei**\
Die Exportkonfigurationsdatei ist als JSON-Objekt strukturiert, das mehrere Zuordnungen enthält. Jede Zuordnung ist mit einem bestimmten Programm im ERP-System verbunden und definiert die auszuführenden Aktionen, die zuzuordnenden Felder und die anzuwendenden Bedingungen.

**Wichtige Komponenten**

1. **Programm**\
   **Definition:** Gibt das ERP-Programm an, auf das die Zuordnung zutrifft.\
   **Beispiel:** "program": "CRS620MI"
2. **Aktionen**\
   **Definition:** Definiert die Aktionen, die ausgeführt werden können, wie das Hinzufügen oder Aktualisieren von Datensätzen.\
   **Beispiel:**\
   "actions": {\
   "add": "AddSupplier",\
   "update": "UpdSupplier"\
   }
3. **Zuordnung**\
   • **Definition:** Gibt die Zuordnung zwischen Feldern im ERP-System und Feldern im Lieferantenportal an.\
   • **Komponenten:**\
   • **erp\_field\_name:** Der Feldname im ERP-System.\
   • **value\_field\_name:** Der entsprechende Feldname im Lieferantenportal.\
   • **value:** Ein statischer Wert, der verwendet wird, wenn im Lieferantenportal kein entsprechendes Feld vorhanden ist.\
   • **if\_conditions:** Optionale Bedingungen, die den Wert basierend auf bestimmten Kriterien bestimmen.\
   • **Beispiel:**

```
{
    "erp_field_name": "SUNO",
    "value_field_name": "supplier_number"
}
```

4.  **Bedingte Logik (if\_conditions)**\
    • **Definition:** Gibt die Bedingungen an, die erfüllt sein müssen, damit ein bestimmter Wert verwendet wird.\
    • **Komponenten:**\
    • **field\_name:** Der Feldname im Lieferantenportal, der ausgewertet wird.\
    • **field\_value:** Der Wert, der die Bedingung auslöst.\
    • **then\_value:** Der Wert, der verwendet wird, wenn die Bedingung erfüllt ist.\
    • **Beispiel:**

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
5. **Schleifen (loop\_on)**\
   • **Definition:** Definiert die Abschnitte, in denen die Konfiguration über eine Liste von Elementen, wie Adressen oder Referenzdetails, iterieren soll.\
   • **Beispiel:**\
   "loop\_on": "address\_details"
6.  **Berechnete Felder (value\_field\_calculated)**\
    • **Definition:** Gibt Felder an, die zur Laufzeit berechnet werden sollen, wie z. B. die Erzeugung des aktuellen Datums.\
    • **Beispiel:**

    ```json
    jsonCode kopieren{
        "erp_field_name": "STDT",
        "value_field_calculated": "now()"
    }
    ```
7.  **Feldzuordnungen mit Listen (mapping\_field\_name und mapping\_list)**\
    • **Definition:** Ordnet spezifische Werte aus dem Lieferantenportal den entsprechenden Werten im ERP-System basierend auf einer vordefinierten Liste zu.\
    • **Komponenten:**\
    • **mapping\_field\_name:** Das Feld, das die Zuordnung bestimmt.\
    • **mapping\_list:** Ein Wörterbuch, das Werte vom Lieferantenportal ins ERP-System übersetzt.\
    • **Beispiel:**

    ```json
    jsonCode kopieren{
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

**Beispiel für die Konfigurationsaufgliederung**\
**Lieferant hinzufügen und aktualisieren (CRS620MI)**\
• **Programm:** CRS620MI\
• **Aktionen:**\
• Lieferanten hinzufügen: AddSupplier\
• Lieferanten aktualisieren: UpdSupplier\
• **Zuordnungsfelder:**\
• SUNO → supplier\_number\
• SUNM → name\
• CSCD → supplier\_country\
• TINO → tax\_id\
• Zusätzliche Felder umfassen statische Werte und bedingte Zuordnungen.

**Adressdetails (CRS620MI)**\
• **Schleife über:** address\_details\
• **Aktionen:**\
• Adresse hinzufügen: AddAddress\
• Adresse aktualisieren: AddAddress\
• **Zuordnungsfelder:**\
• SUNO → supplier\_number\
• ADR1 → address\
• TOWN → city\
• Zusätzliche Felder umfassen berechnete Felder wie now() für das aktuelle Datum.

**Referenzdetails (CRS620MI)**\
• **Schleife über:** reference\_details\
• **Aktionen:**\
• Lieferantenreferenz hinzufügen: AddSupplierRef\
• Lieferantenreferenz aktualisieren: AddSupplierRef\
• **Zuordnungsfelder:**\
• SUNO → supplier\_number\
• RFTY → reference\_type\
• RFID wird mithilfe einer Liste zugeordnet, um Typen wie „EINKAUF“, „QA“ und „FINANZEN“ zu übersetzen.

**Verwendung der Exportkonfiguration**

1. **Hochladen der Konfigurationsdatei**
   1. **Navigieren zur Exportkonfiguration:**\
      • Gehen Sie zum Abschnitt Exportkonfiguration im Hauptmenü.
   2. **Hochladen der Konfigurationsdatei:**\
      • Klicken Sie auf die Abschnitte ION-Mapping-Datei oder IDM-Mapping-Datei, um die jeweilige Konfigurationsdatei hochzuladen.
   3. **Konfiguration speichern:**\
      • Nach dem Hochladen klicken Sie auf die Schaltfläche Speichern, um die Konfiguration anzuwenden.
2. **Verwendung der Standardvorlagen**\
   • Klicken Sie auf die Schaltfläche Standardvorlage verwenden, wenn Sie zur standardmäßigen Konfigurationsvorlage zurückkehren möchten, die vom System bereitgestellt wird.
3. **Formatierung des JSON**\
   • Verwenden Sie die Schaltfläche Formatieren, um den JSON-Code automatisch für eine bessere Lesbarkeit zu formatieren.

**Fazit**\
Diese Konfigurationsdatei ist entscheidend, um sicherzustellen, dass die Daten zwischen dem Lieferantenportal und dem ERP-System korrekt zugeordnet und synchronisiert werden. Durch das Verständnis der Struktur und der wichtigsten Komponenten können Administratoren den Exportprozess effektiv verwalten und anpassen, um ihre spezifischen Geschäftsanforderungen zu erfüllen.

**Vollständiges Beispiel**

```json
jsonCode kopieren[{
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
```
