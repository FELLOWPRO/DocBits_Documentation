# Berechnung des Gesamtbetrags Skript für DocBits

##

Das Skript "Berechnung des Gesamtbetrags" automatisiert den Prozess, verschiedene Gebühren und zusätzliche Beträge in Rechnungsdokumenten zusammenzufassen. Diese Anleitung führt Sie durch die Skripteinrichtung, Logik und Anwendung, um genaue Gesamtberechnungen über Ihre Dokumente sicherzustellen.

### Zweck

Dieses Skript zielt darauf ab, eine dynamische Möglichkeit bereitzustellen, die Gesamtkosten auf einer Rechnung zu berechnen, indem verschiedene Gebührentypen wie Grundgebühren, Fracht und Verpackung addiert werden. Anschließend aktualisiert es das Feld für die Gesamtkosten der Rechnung mit der berechneten Summe, um genaue Abrechnungsinformationen sicherzustellen.

### Skriptübersicht

Das Skript ruft Werte aus bestimmten Feldern ab, konvertiert sie in Gleitkommazahlen, summiert sie auf und aktualisiert dann das Feld `total_charges` mit dem Ergebnis. Wenn das Feld `total_charges` nicht existiert, erstellt das Skript dieses Feld und setzt seinen Wert entsprechend.

#### Code-Schnipsel
```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
fracht = float(fracht)
total += fracht

# Add verpackung to total if it exists
if verpackung:
verpackung = float(verpackung)
total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

