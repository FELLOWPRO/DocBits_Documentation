# Veldfuncties

Functies voor het lezen, schrijven en beheren van documentvelden.

**Source:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Leest de waarde van een veld uit het document.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Het `document_data` contextobject |
| `field_name` | `str` | Naam van het veld (bijv. `"invoice_id"`) |
| `default_value` | `any` | Retourwaarde als het veld leeg/ontbrekend is (standaard: `None`) |
| `is_clean` | `bool` | Indien `True`: waarde wordt geconverteerd naar HOOFDLETTERS met spaties verwijderd |

**Retourneert:** De veldwaarde als string, of `default_value`

**Voorbeeld — Factuurnummer lezen met terugvalwaarde:**

```python
# Veld lezen met standaardwaarde
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# Met is_clean=True: "INV 001" wordt "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**Wat gebeurt er:** Retourneert de veldwaarde. Wanneer `is_clean=True`, wordt de waarde getransformeerd via `value.upper().replace(" ", "").strip()` — handig voor vergelijkingen.

---

## set\_field\_value()

Stelt de waarde van een veld in. Maakt het veld automatisch aan als het niet bestaat.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Het `document_data` contextobject |
| `field_name` | `str` | Naam van het veld |
| `value` | `any` | Nieuwe waarde |
| `remove_link` | `bool` | Indien `True`: verwijdert coordinaten, confidence, regel, enz. |

**Retourneert:** `True` als de waarde is gewijzigd, `False` als deze identiek is

**Neveneffecten:**
- Stelt `highlight_field = True` in (visuele indicator in UI)
- Stelt `extraction_method = "SCRIPT"` in
- Stelt `formatted_value = value` in

**Voorbeeld — Voorwaardelijke waarde-toewijzing:**

```python
# Factuurnummer instellen
set_field_value(document_data, "invoice_id", "INV-2026-001")

# Met remove_link: verwijdert OCR-koppeling (coordinaten, confidence enz.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**Wat gebeurt er:** De veldwaarde wordt bijgewerkt en gemarkeerd als scriptgewijzigd. Als het veld niet bestaat, wordt het automatisch aangemaakt met `extraction_method: "SCRIPT"` en toegevoegd aan zowel `fields` als `fields_dict`.

---

## set\_date\_value()

Stelt een datumwaarde in met automatische opmaak en optionele datumberekeningen.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `value` | `str` | ISO-datum: `"2026-03-25"`. Indien leeg: datum van vandaag |
| `add_days` | `int` | Dagen om toe te voegen (bijv. `30` voor betalingstermijnen) |
| `skip_weekend` | `bool` | Weekenden overslaan bij het optellen van dagen |
| `exclude_final_days` | `str/list` | Extra dagen om uit te sluiten (bijv. `"MONDAY,FRIDAY"`) |

**Voorbeeld — Betalingsvervaldatum berekenen (30 dagen, geen weekenden):**

```python
# Vervaldatum: 30 dagen na factuurdatum, weekenden overslaan
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Leverdatum instellen op vandaag
set_date_value(document_data, "delivery_date", None)  # None = vandaag

# 14 dagen, exclusief zaterdag en maandag
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**Wat gebeurt er:** De datum wordt berekend door dagen op te tellen (optioneel weekenden/specifieke dagen overslaan) en automatisch opgemaakt volgens het `date_format_pattern` van het document (bijv. `%d.%m.%Y` voor Duitsland).

**Dagcodes voor `exclude_final_days`:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Stelt een bedragwaarde in met automatische lokale opmaak.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `value` | `str/number` | Bedrag in Engels formaat (bijv. `"1234.56"`) |

**Voorbeeld — Nettobedrag instellen:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value wordt bijv. "1.234,56" voor de_DE-locale
```

**Wat gebeurt er:** Het bedrag wordt opgemaakt volgens `amount_format_locale` uit `document_json` (bijv. `de_DE`, `en_US`).

---

## create\_new\_field()

Maakt een nieuw velddictionary aan (zonder het aan het document toe te voegen).

```python
create_new_field(field_name, value="")
```

**Retourneert:** Dict met `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Voorbeeld:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Eenvoudiger alternatief:** Gebruik in plaats daarvan `set_field_value()` — deze maakt het veld automatisch aan als het niet bestaat. `create_new_field()` is alleen nodig wanneer u het velddictionary handmatig wilt bewerken.
{% endhint %}

---

## delete\_field()

Verwijdert een veld uit het document.

```python
delete_field(document_data, field_name)
```

**Retourneert:** Tuple `(doc_json, fields_dict)` na verwijdering

**Voorbeeld:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Markeert een veld als ongeldig met een foutmelding.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `message` | `str` | Foutmelding (weergegeven in UI) |
| `code` | `str` | Foutcode (standaard: `INVALID_VALUE`) |

**Neveneffecten:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Voorbeeld — IBAN-validatie:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN moet minimaal 15 tekens bevatten",
                         "IBAN_TOO_SHORT")
```

**Wat gebeurt er:** Het veld wordt rood gemarkeerd in het validatiescherm met de foutmelding weergegeven aan de gebruiker.

---

## set\_field\_as\_valid()

Verwijdert de ongeldige status van een veld.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Voorbeeld:**

```python
set_field_as_valid(document_data, "iban", "IBAN geldig")
```

**Wat gebeurt er:** Verwijdert `invalidated_by_script`, `validation_message`, `validation_code` en stelt `is_valid = True` in.

---

## set\_field\_attribute()

Stelt een willekeurig attribuut in op een veld.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Voorbeeld:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Zie de volledige lijst van [Ondersteunde Attributen](#ondersteunde-attributen) hieronder.

---

## set\_is\_required()

Maakt een veld verplicht of verwijdert de verplichting.

```python
set_is_required(document_data, field_name, value)
```

**Voorbeeld — PO-nummer verplicht voor inkoopfacturen:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Maakt een veld alleen-lezen of bewerkbaar.

```python
set_is_readonly(document_data, field_name, value)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = alleen-lezen, `False` = bewerkbaar, `None` = attribuut verwijderen |

**Voorbeeld:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Verbergt of toont een veld in de UI.

```python
set_is_hidden(document_data, field_name, value)
```

**Voorbeeld — Sub-organisatievelden alleen tonen wanneer relevant:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Forceert handmatige validatie voor een veld.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = validatie forceren, `False` = verwijderen |
| `reset_validation` | `bool` | Indien `True`: zet `is_validated` terug naar `False` |

**Neveneffecten wanneer `value=True`:**
- `force_validation = True`
- `is_valid = False` (als nog niet gevalideerd)
- `validation_code = "FORCED_VALIDATION"`

**Voorbeeld — Validatie forceren bij hoge bedragen:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Ondersteunde Attributen

### Kernveldattributen

| Attribuut | Type | Beschrijving |
| --------- | ---- | ----------- |
| `value` | any | De ruwe veldwaarde |
| `formatted_value` | string | Opgemaakte weergavewaarde |
| `content` | string | Oorspronkelijke geextraheerde inhoud |
| `is_required` | bool | Of het veld verplicht is |
| `is_valid` | bool | Validatiestatus |
| `is_validated` | bool | Of het veld door de gebruiker is gevalideerd |
| `is_readonly` | bool | Of het veld alleen-lezen is |
| `is_hidden` | bool | Of het veld verborgen is in de UI |
| `force_validation` | bool | Gebruiker dwingen dit veld te valideren |
| `highlight_field` | bool | Veld markeren in de UI |
| `extraction_method` | string | Hoe de waarde is geextraheerd (bijv. `"SCRIPT"`) |

### Validatieattributen

| Attribuut | Type | Beschrijving |
| --------- | ---- | ----------- |
| `validation_message` | string | Foutmelding getoond aan de gebruiker |
| `validation_code` | string | Foutcode (bijv. `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Markeert veld als ongeldig verklaard door script |

### Extractie-/OCR-attributen

| Attribuut | Type | Beschrijving |
| --------- | ---- | ----------- |
| `coords` | object | Begrenzingskadercoordinaten op document |
| `confidence` | float | OCR-/extractie-betrouwbaarheidsscore |
| `score` | float | Match-/validatiescore |
| `score_description` | string | Beschrijving van de score |
| `page` | int | Paginanummer waar het veld is gevonden |
| `rule` | string | Toegepaste extractieregel |
