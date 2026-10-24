# Skripterstellung in DocBits

## Videoanleitung: Die wichtigsten Skript-Funktionen

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-script-functions/v2/de.mp4" %}
Die wichtigsten Skript-Funktionen in DocBits
{% endembed %}

Das Video zeigt im Skript-Editor, wie Sie ein Feld lesen (`get_field_value`), einen Wert setzen (`set_field_value`), ein Fälligkeitsdatum berechnen (`set_date_value`), ein Feld als ungültig markieren (`set_field_as_invalid`) und ein Feld zum Pflichtfeld machen (`set_is_required`).

## Leitfaden zur Skripterstellung in DocBits

Willkommen im Docbits Scripting Guide! Hier lernen Sie, wie Sie Skripte verwenden, um die Dokumentenverarbeitung in Docbits zu automatisieren und zu verbessern. Skripte ermöglichen die benutzerdefinierte Feldmanipulation, Datenumwandlung und Logikimplementierung über verschiedene Dokumenttypen hinweg.

### Erste Schritte

Skripte in Docbits werden in Python geschrieben. Sie interagieren mit Dokumentfeldern und Metadaten, um eine Vielzahl von Operationen durchzuführen, von einfacher Datenformatierung bis hin zu komplexer Logik.

#### Wichtige Funktionen

Jedes Skript erhält das Dokument als `document_data`. Übergeben Sie es als erstes Argument an die Feldfunktionen. Die vollständige Referenz finden Sie auf der Seite [Feldfunktionen](field-functions.md).

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)`: Liest den Wert eines Feldes.
* `set_field_value(document_data, field_name, value)`: Schreibt einen Wert in ein Feld und legt das Feld an, falls es nicht existiert.
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)`: Schreibt ein Datum, optional mit addierten Tagen und ohne Wochenenden.
* `set_amount_value(document_data, field_name, value)`: Schreibt einen Betrag im Format der Dokument-Lokalisierung.
* `set_field_as_invalid(document_data, field_name, message, code=None)`: Markiert ein Feld als ungültig und zeigt dem Anwender die Meldung.
* `set_is_required(document_data, field_name, value)`: Macht ein Feld zum Pflichtfeld oder hebt das auf.

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
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```
