# Generierung erweiterter Rechnungsnummernskript für Docbits

Dieses Dokument enthält Details zum Skript "Generierung erweiterter Rechnungsnummern", das die Erstellung erweiterter Rechnungsnummern in Docbits automatisiert. Erweiterte Rechnungsnummern kombinieren mehrere Dokumentenidentifikatoren, wie die Rechnungs-ID und die Bestellnummer, zu einem umfassenden Identifikator. Dieses Skript verbessert die Rückverfolgbarkeit von Dokumenten und vereinfacht die Aufzeichnung.

### Zweck

Der Zweck dieses Skripts besteht darin, den Prozess der Generierung erweiterter Rechnungsnummern zu optimieren, indem automatisch die Rechnungs-ID und die Bestellnummer verkettet werden, um so einen einheitlichen und eindeutigen Identifikator für jedes Rechnungsdokument bereitzustellen.

### Übersicht des Skripts

Das Skript überprüft das Vorhandensein der Rechnungs-ID und der Bestellnummerfelder im Dokument, verkettet ihre Werte, wenn beide vorhanden sind (getrennt durch einen Bindestrich), und aktualisiert oder erstellt ein neues Feld, um den kombinierten Wert zu speichern.

#### Code-Schnipsel
```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
# Updating the 'invoice_extended_number' field with the combined value
if not 'invoice_extended_number' in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

