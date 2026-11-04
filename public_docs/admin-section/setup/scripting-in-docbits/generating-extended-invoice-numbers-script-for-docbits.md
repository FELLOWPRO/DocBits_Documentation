# Generierung von erweiterten Rechnungsnummern Skript für Docbits

### Überblick

Dieser Leitfaden konzentriert sich auf die Automatisierung der Erstellung erweiterter Rechnungsnummern in Docbits, eine wichtige Funktion zur Verbesserung des Rechnungsmanagements und der Verfolgung. Das Skript "Generierung erweiterter Rechnungsnummern" verknüpft verschiedene Dokumentenidentifikatoren wie Rechnungs-ID und Bestellnummer, um einen umfassenden und eindeutigen Bezeichner für jede Rechnung zu erstellen.

### Ziel

Das Hauptziel dieses Skripts ist es, die Generierung erweiterter Rechnungsnummern zu automatisieren, um das einfachere Tracking und Management von Rechnungen zu ermöglichen, indem mehrere Identifikatoren zu einer einzigen, eindeutigen Nummer kombiniert werden.

### Implementierung des Skripts

#### Code-Schnipsel
```python
# Retrieve the values of invoice ID and purchase order number from the document
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Concatenate the invoice ID and purchase order number with a hyphen if both exist
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check and update the 'invoice_extended_number' field with the concatenated value
if extended_number:
if 'invoice_extended_number' not in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

