# Feld-Funktionen

Funktionen zum Lesen, Schreiben und Steuern von Dokumentfeldern.

**Quelle:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Liest den Wert eines Feldes aus dem Dokument.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `document_data` | `dict` | Das `document_data`-Kontextobjekt |
| `field_name` | `str` | Name des Feldes (z.B. `"invoice_id"`) |
| `default_value` | `any` | Rückgabewert wenn Feld leer/nicht vorhanden (Standard: `None`) |
| `is_clean` | `bool` | Wenn `True`: Wert wird in GROSSBUCHSTABEN umgewandelt und Leerzeichen entfernt |

**Rückgabe:** Der Feldwert als String oder `default_value`

**Beispiel — Rechnungsnummer mit Fallback lesen:**

```python
# Feld mit Standardwert lesen
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# Mit is_clean=True: "INV 001" wird zu "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**Was passiert:** Gibt den Feldwert zurück. Bei `is_clean=True` wird der Wert über `value.upper().replace(" ", "").strip()` transformiert — nützlich für Vergleiche.

---

## set\_field\_value()

Setzt den Wert eines Feldes. Erstellt das Feld automatisch, wenn es nicht existiert.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `document_data` | `dict` | Das `document_data`-Kontextobjekt |
| `field_name` | `str` | Name des Feldes |
| `value` | `any` | Neuer Wert |
| `remove_link` | `bool` | Wenn `True`: entfernt Koordinaten, Konfidenz, Regel usw. |

**Rückgabe:** `True` wenn Wert geändert, `False` wenn identisch

**Nebeneffekte:**
- Setzt `highlight_field = True` (visuelle Kennzeichnung in der UI)
- Setzt `extraction_method = "SCRIPT"`
- Setzt `formatted_value = value`

**Beispiel — Bedingte Wertzuweisung:**

```python
# Rechnungs-ID setzen
set_field_value(document_data, "invoice_id", "INV-2026-001")

# Mit remove_link: entfernt OCR-Verknüpfung (Koordinaten, Konfidenz usw.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**Was passiert:** Der Feldwert wird aktualisiert und als skriptmodifiziert markiert. Wenn das Feld nicht existiert, wird es automatisch mit `extraction_method: "SCRIPT"` erstellt und sowohl zu `fields` als auch zu `fields_dict` hinzugefügt.

---

## set\_date\_value()

Setzt einen Datumswert mit automatischer Formatierung und optionaler Datumsarithmetik.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `value` | `str` | ISO-Datum: `"2026-03-25"`. Wenn leer: heutiges Datum |
| `add_days` | `int` | Tage zum Addieren (z.B. `30` für Zahlungsbedingungen) |
| `skip_weekend` | `bool` | Wochenenden beim Addieren überspringen |
| `exclude_final_days` | `str/list` | Zusätzliche Tage zum Ausschließen (z.B. `"MONDAY,FRIDAY"`) |

**Beispiel — Zahlungsfälligkeit berechnen (30 Tage, keine Wochenenden):**

```python
# Fälligkeitsdatum: 30 Tage nach Rechnungsdatum, Wochenenden überspringen
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Lieferdatum auf heute setzen
set_date_value(document_data, "delivery_date", None)  # None = heute

# 14 Tage, Samstag und Montag ausschließen
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**Was passiert:** Das Datum wird berechnet, indem Tage addiert werden (optional unter Ausschluss von Wochenenden/bestimmten Tagen) und automatisch gemäß dem `date_format_pattern` des Dokuments formatiert (z.B. `%d.%m.%Y` für Deutschland).

**Tagescodes für `exclude_final_days`:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Setzt einen Betragswert mit automatischer Locale-Formatierung.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `value` | `str/number` | Betrag im englischen Format (z.B. `"1234.56"`) |

**Beispiel — Nettobetrag setzen:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value wird z.B. "1.234,56" für de_DE Locale
```

**Was passiert:** Der Betrag wird gemäß `amount_format_locale` aus `document_json` formatiert (z.B. `de_DE`, `en_US`).

---

## create\_new\_field()

Erstellt ein neues Feld-Dictionary (ohne es zum Dokument hinzuzufügen).

```python
create_new_field(field_name, value="")
```

**Rückgabe:** Dict mit `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Beispiel:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Einfachere Alternative:** Verwenden Sie stattdessen `set_field_value()` — es erstellt das Feld automatisch, wenn es nicht existiert. `create_new_field()` wird nur benötigt, wenn das Feld-Dict manuell manipuliert werden soll.
{% endhint %}

---

## delete\_field()

Entfernt ein Feld aus dem Dokument.

```python
delete_field(document_data, field_name)
```

**Rückgabe:** Tuple `(doc_json, fields_dict)` nach der Löschung

**Beispiel:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Markiert ein Feld als ungültig mit einer Fehlermeldung.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `message` | `str` | Fehlermeldung (wird in der UI angezeigt) |
| `code` | `str` | Fehlercode (Standard: `INVALID_VALUE`) |

**Nebeneffekte:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Beispiel — IBAN-Validierung:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN muss mindestens 15 Zeichen lang sein",
                         "IBAN_TOO_SHORT")
```

**Was passiert:** Das Feld wird im Validierungsbildschirm rot hervorgehoben und die Fehlermeldung wird dem Benutzer angezeigt.

---

## set\_field\_as\_valid()

Entfernt den Ungültig-Status von einem Feld.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Beispiel:**

```python
set_field_as_valid(document_data, "iban", "IBAN gültig")
```

**Was passiert:** Entfernt `invalidated_by_script`, `validation_message`, `validation_code` und setzt `is_valid = True`.

---

## set\_field\_attribute()

Setzt ein beliebiges Attribut auf einem Feld.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Beispiel:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Die vollständige Liste der [unterstützten Attribute](#supported-attributes) finden Sie unten.

---

## set\_is\_required()

Macht ein Feld zum Pflichtfeld oder entfernt die Anforderung.

```python
set_is_required(document_data, field_name, value)
```

**Beispiel — Bestellnummer für Einkaufsrechnungen erforderlich:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Macht ein Feld schreibgeschützt oder bearbeitbar.

```python
set_is_readonly(document_data, field_name, value)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `value` | `bool/None` | `True` = schreibgeschützt, `False` = bearbeitbar, `None` = Attribut entfernen |

**Beispiel:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Blendet ein Feld in der UI ein oder aus.

```python
set_is_hidden(document_data, field_name, value)
```

**Beispiel — Sub-Org-Felder nur bei Relevanz anzeigen:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Erzwingt eine manuelle Validierung für ein Feld.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `value` | `bool` | `True` = Validierung erzwingen, `False` = entfernen |
| `reset_validation` | `bool` | Wenn `True`: setzt `is_validated` auf `False` zurück |

**Nebeneffekte bei `value=True`:**
- `force_validation = True`
- `is_valid = False` (wenn noch nicht validiert)
- `validation_code = "FORCED_VALIDATION"`

**Beispiel — Validierung bei hohen Beträgen erzwingen:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Unterstützte Attribute

### Kern-Feldattribute

| Attribut | Typ | Beschreibung |
| -------- | --- | ------------ |
| `value` | any | Der Roh-Feldwert |
| `formatted_value` | string | Anzeige-formatierter Wert |
| `content` | string | Original extrahierter Inhalt |
| `is_required` | bool | Ob Feld ein Pflichtfeld ist |
| `is_valid` | bool | Validierungsstatus |
| `is_validated` | bool | Ob Feld vom Benutzer validiert wurde |
| `is_readonly` | bool | Ob Feld schreibgeschützt ist |
| `is_hidden` | bool | Ob Feld in der UI ausgeblendet ist |
| `force_validation` | bool | Benutzer zur Validierung dieses Feldes zwingen |
| `highlight_field` | bool | Feld in der UI hervorheben |
| `extraction_method` | string | Wie der Wert extrahiert wurde (z.B. `"SCRIPT"`) |

### Validierungsattribute

| Attribut | Typ | Beschreibung |
| -------- | --- | ------------ |
| `validation_message` | string | Fehlermeldung für den Benutzer |
| `validation_code` | string | Fehlercode (z.B. `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Markiert Feld als durch Skript ungültig gemacht |

### Extraktions-/OCR-Attribute

| Attribut | Typ | Beschreibung |
| -------- | --- | ------------ |
| `coords` | object | Begrenzungsrahmen-Koordinaten im Dokument |
| `confidence` | float | OCR-/Extraktions-Konfidenzwert |
| `score` | float | Match-/Validierungswert |
| `score_description` | string | Beschreibung des Werts |
| `page` | int | Seitennummer auf der das Feld gefunden wurde |
| `rule` | string | Angewendete Extraktionsregel |
