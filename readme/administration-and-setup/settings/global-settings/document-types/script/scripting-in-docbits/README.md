# Skripterstellung in DocBits

## Leitfaden zur Skripterstellung in DocBits

Willkommen im Docbits Scripting Guide! Hier lernen Sie, wie Sie Skripte verwenden, um die Dokumentenverarbeitung in Docbits zu automatisieren und zu verbessern. Skripte ermöglichen die benutzerdefinierte Feldmanipulation, Datenumwandlung und Logikimplementierung über verschiedene Dokumenttypen hinweg.

### Erste Schritte

Skripte in Docbits werden in Python geschrieben. Sie interagieren mit Dokumentfeldern und Metadaten, um eine Vielzahl von Operationen durchzuführen, von einfacher Datenformatierung bis hin zu komplexer Logik.

#### Wichtige Funktionen

* `get_field_value(fields_dict, field_name, default=None)`: Ruft den Wert eines angegebenen Feldes ab.
* `set_field_value(fields_dict, field_name, value)`: Setzt den Wert eines angegebenen Feldes.
* `create_new_field(field_name, value)`: Erstellt ein neues Feld mit einem angegebenen Namen und Wert.
* `format_decimal_to_locale(value, locale)`: Formatiert einen Dezimalwert gemäß einer angegebenen Lokalisierung.

### Beispielskripte

Im Folgenden finden Sie mehrere Beispiele, die gängige Scripting-Aufgaben demonstrieren.

#### Beispiel 1: Währungszuordnung für Rechnungen

Standardisieren Sie Währungssymbole oder -texte zu ISO-Währungscodes.

```python
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(fields_dict, "currency", currency_value)
```
