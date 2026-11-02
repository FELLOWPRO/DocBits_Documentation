# Steuercode-Erkennung

## Was macht dieses Skript?

Ermittelt automatisch den korrekten Steuercode basierend auf dem Volltext des Dokuments und den Steuer-/Nettobeträgen. Erkennt Reverse-Charge-Szenarien, steuerfreie Rechnungen und berechnet den Steuersatz, um den passenden Code zuzuweisen (z.B. S1 für 19%, S2 für 7%).

## Auslöser

`AFTER_FORMATTING` für Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
# Dokument-Volltext und Beträge abrufen
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Regel 1: Reverse-Charge-Erkennung über Volltext
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regel 2: Keine Steuer = steuerfrei
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Regel 3: Steuersatz aus Beträgen berechnen
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Normalsatz
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Ermäßigter Satz
    else:
        set_field_value(document_data, "tax_code", "S3")    # Anderer Satz
```

## Schritt-für-Schritt-Erklärung

1. **Volltext lesen** mit `get_document_content()` für Schlüsselwort-Erkennung
2. **Steuer- und Nettobeträge lesen** für die Steuersatzberechnung
3. **Auf Reverse Charge prüfen** — Schlüsselwörter im Dokumenttext suchen (deutsch und englisch)
4. **Auf Steuer null prüfen** — wenn der Steuerbetrag 0 ist, steuerfreien Code zuweisen
5. **Steuersatz berechnen** aus dem Verhältnis Steuer/Netto und den passenden Code zuweisen

## Verwendete Funktionen

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — OCR-Volltext lesen
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Feldwerte lesen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Steuercode setzen
