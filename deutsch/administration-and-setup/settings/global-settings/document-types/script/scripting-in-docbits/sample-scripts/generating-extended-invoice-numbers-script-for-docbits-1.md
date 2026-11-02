# Generierung erweiterter Rechnungsnummern - Skript für DocBits

Dieses Dokument beschreibt das Skript "Generierung erweiterter Rechnungsnummern", das die Erstellung erweiterter Rechnungsnummern in DocBits automatisiert. Erweiterte Rechnungsnummern kombinieren mehrere Dokumentkennungen, wie die Rechnungs-ID und die Bestellnummer, zu einem einzigen, umfassenden Identifikator. Dieses Skript verbessert die Dokumentenrückverfolgbarkeit und vereinfacht die Datenhaltung.

### Zweck

Der Zweck dieses Skripts ist es, den Prozess der Generierung erweiterter Rechnungsnummern zu optimieren, indem die Rechnungs-ID und die Bestellnummer automatisch verkettet werden, wodurch ein einheitlicher und eindeutiger Identifikator für jedes Rechnungsdokument bereitgestellt wird.

### Skriptübersicht

Das Skript prüft das Vorhandensein der Felder Rechnungs-ID und Bestellnummer innerhalb des Dokuments, verkettet deren Werte, falls beide vorhanden sind (getrennt durch einen Bindestrich), und aktualisiert oder erstellt ein neues Feld, um den kombinierten Wert zu speichern.

#### Code-Ausschnitt

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Rechnungs-ID und Bestellnummer mit Bindestrich als Trennzeichen kombinieren
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Prüfen ob eine erweiterte Nummer zum Setzen vorhanden ist
if extended_number:
    # Feld 'invoice_extended_number' mit dem kombinierten Wert aktualisieren
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```
