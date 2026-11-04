# Skripting in DocBits

## DocBits Skripting Anleitung

Willkommen zur DocBits Skripting-Anleitung! Hier lernen Sie, wie Sie Skripte verwenden können, um die Automatisierung und Verbesserung Ihrer Dokumentenverarbeitung in DocBits durchzuführen. Skripte ermöglichen die Anpassung von Feldern, die Datenumwandlung und die Implementierung von Logik in verschiedenen Dokumententypen.

### Erste Schritte

Skripte in DocBits werden in Python geschrieben. Sie interagieren mit Dokumentenfeldern und Metadaten, um eine Vielzahl von Operationen durchzuführen, von einfacher Datenformatierung bis hin zu komplexer Logik.

#### Schlüsselfunktionen

* `get_field_value(fields_dict, field_name, default=None)`: Ruft den Wert eines bestimmten Feldes ab.
* `set_field_value(fields_dict, field_name, value)`: Legt den Wert eines bestimmten Feldes fest.
* `create_new_field(field_name, value)`: Erstellt ein neues Feld mit einem bestimmten Namen und Wert.
* `format_decimal_to_locale(value, locale)`: Formatiert einen Dezimalwert entsprechend einer bestimmten Sprachregion.

### Beispielskripte

Im Folgenden finden Sie mehrere Beispiele, die häufige Skriptaufgaben demonstrieren.

#### Beispiel 1: Währungsumwandlung für Rechnungen

Standardisieren von Währungssymbolen oder Text zu ISO-Währungscodes.
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

