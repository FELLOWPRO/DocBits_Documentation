# Berechnung der Gesamtkosten - Skript für DocBits

Das Skript "Berechnung der Gesamtkosten" automatisiert den Prozess der Summierung verschiedener Gebühren und zusätzlicher Beträge innerhalb von Rechnungsdokumenten. Diese Anleitung führt durch die Skripteinrichtung, Logik und Anwendung, um genaue Gesamtkostenberechnungen in Dokumenten sicherzustellen.

### Zweck

Dieses Skript bietet eine dynamische Möglichkeit, die Gesamtkosten einer Rechnung zu berechnen, indem verschiedene Gebührenarten wie Basisgebühren, Fracht und Verpackung addiert werden. Es aktualisiert dann das Feld für die Gesamtkosten der Rechnung mit der berechneten Summe und stellt so genaue Rechnungsinformationen sicher.

### Skriptübersicht

Das Skript ruft Werte aus angegebenen Feldern ab, konvertiert sie in Gleitkommazahlen, summiert sie und aktualisiert dann das Feld `total_charges` mit dem Ergebnis. Falls das Feld `total_charges` nicht existiert, erstellt das Skript dieses Feld und setzt seinen Wert entsprechend.

#### Code-Ausschnitt

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Summe auf 0 initialisieren
total = 0

# Fracht zur Summe addieren, falls vorhanden
if fracht:
    fracht = float(fracht)
    total += fracht

# Verpackung zur Summe addieren, falls vorhanden
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Summe auf zwei Dezimalstellen formatieren
formatted_total = "{0:.2f}".format(total)

# Prüfen ob das Feld total_charges existiert und entsprechend aktualisieren oder erstellen
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
