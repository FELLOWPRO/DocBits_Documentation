# Bedrijfslogica Functies

Functies voor lookups, PO-matching, taken, gebruikers-/groepsbeheer en statuswijzigingen.

**Source:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Bevraagt stamgegevens uit lookup-tabellen (leveranciers, artikelen, grootboekrekeningen, enz.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organisatie-UUID |
| `sub_org_id` | `str/None` | Sub-organisatie-UUID (of `None`) |
| `lookup_name` | `str` | Naam van de lookup (bijv. `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Filtervoorwaarden (zie formaten hieronder) |
| `skip` | `int` | Offset voor paginering (standaard: 0) |
| `limit` | `int` | Max resultaten (standaard: 100) |
| `match_all` | `bool` | `True` = EN, `False` = OF (standaard: `True`) |
| `sort_order` | `list` | Sortering (optioneel) |

### Filterformaten

Drie formaten worden ondersteund:

```python
# Formaat 1: Dict met field/operator/value
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Formaat 2: Tuple/Lijst met 2 elementen (field, value) → operator = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Formaat 3: Tuple/Lijst met 3 elementen (field, operator, value)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Sortering

```python
# Formaat 1: Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Formaat 2: Tuple/Lijst
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Voorbeeld — Leverancier opzoeken op leveranciers-ID:**

```python
# Leverancier zoeken op leveranciers-ID
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Voorbeeld — Grootboekrekeningen zoeken met meerdere filters:**

```python
records = get_lookup_records(
    org_id, document_json.get("sub_org_id"), "gl_account",
    [
        {"field": "ACCOUNT_TYPE", "operator": "exact", "value": "EXPENSE"},
        {"field": "IS_ACTIVE", "operator": "exact", "value": "true"},
    ],
    limit=50,
    sort_order=[["ACCOUNT_NUMBER", "asc"]],
)
```

{% hint style="info" %}
Intern wordt `search_operator="SMART"` gebruikt, wat fuzzy matching ondersteunt.
{% endhint %}

---

## is\_supplier\_valid()

Controleert of een leverancier bestaat in de lookup-gegevens.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Het `user` contextobject |
| `filter_data_json` | `dict` | Filter in formaat `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Sub-organisatie |

**Retourneert:** `True` als minimaal 1 overeenkomst, anders `False`

**Voorbeeld — Leverancier valideren:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Leverancier niet gevonden in stamgegevens")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Start automatische PO-matching via de po-match-service microservice.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Moet een echt gebruikersobject zijn |
| `document_data` | `dict` | Documentcontext |
| `po_numbers` | `str/list` | PO-nummers (kommagescheiden of lijst) |

**Retourneert:** Bijgewerkte `document_data` met `po_items`, `po_match_status`, `po_multi_matched`

**Voorbeeld — Automatische PO-matching:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Duplicaatbeveiliging:** Reeds geverifieerde PO-nummers worden opgeslagen in `already_verified_po_numbers` en worden niet opnieuw gematcht.
{% endhint %}

---

## get\_next\_sequence\_number()

Haalt atomair een volgnummer op en verhoogt dit in de database.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organisatie-UUID |
| `sequence_name` | `str` | Moet `"sequence"` bevatten (bijv. `"invoice_sequence"`) |
| `default_value` | `int` | Startwaarde wanneer de reeks nieuw wordt aangemaakt |

**Retourneert:** `int` — het volgende nummer, of `None` als de naam ongeldig is

**Voorbeeld — Intern documentnummer genereren:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Naamgevingsregel:** De `sequence_name` moet beginnen of eindigen met "sequence", of "SEQUENCE\_" bevatten. Anders retourneert de functie `None`.
{% endhint %}

---

## create\_document\_task()

Maakt een taak aan voor het huidige document.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Gebruikerscontext |
| `title` | `str` | Taaktitel |
| `description` | `str` | Beschrijving |
| `priority` | `str/int` | Prioriteit |
| `assigned_to_user_id` | `str/None` | Toegewezen gebruiker |
| `assigned_to_group_id` | `str/None` | Toegewezen groep |
| `send_email` | `bool` | E-mailnotificatie versturen |

**Voorbeeld — Taak aanmaken voor facturen met hoog bedrag:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="Hoog factuurbedrag - beoordeling vereist",
        description=f"Factuurbedrag: {amount} overschrijdt drempel van 50.000",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Wijst een sub-organisatie toe aan een document.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Neveneffecten:**
- Stelt `sub_org_id` in `document_json` in
- Slaat direct op in de database (als `doc_id` aanwezig is)

**Voorbeeld — Routering op basis van leverancier:**

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
sub_org_map = {
    "ACMECORP": "uuid-acme-sub-org",
    "WIDGETSINC": "uuid-widgets-sub-org",
}
for key, sub_org in sub_org_map.items():
    if key in supplier:
        set_document_sub_org_id(document_data, sub_org)
        break
```

---

## update\_document\_status\_with\_doc\_id()

Wijzigt de status van een document.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `doc_id` | `str` | Document-UUID |
| `status` | `str` | Nieuwe status (bijv. `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Statusbericht |
| `doc_classification_class` | `str/None` | Voor `CLASSIFIED`-status: nieuw documenttype |

**Voorbeeld — Document op foutstatus zetten:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Verplicht veld ontbreekt: leveranciersnummer"
)
```

{% hint style="warning" %}
**Let op:** Statuswijzigingen activeren downstream-acties (DocFlow-workflows, statuswijzigingshooks). Gebruik alleen wanneer noodzakelijk.
{% endhint %}

---

## get\_document\_content()

Retourneert de volledige OCR-tekst van het document.

```python
get_document_content(document_data)
```

**Retourneert:** `str` — Samengevoegde tekst van alle pagina's

**Voorbeeld — Volledige tekst doorzoeken op trefwoorden:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regex-zoekopdracht in volledige tekst
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
Het resultaat wordt 60 seconden gecachet (TTL-cache met maximaal 128 vermeldingen).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Zoekt een gebruiker op via ID of e-mail.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Retourneert:** `UsersCache`-object met attributen zoals `.email`, `.first_name`, `.last_name`, `.user_id`

**Voorbeeld — Taak toewijzen aan specifieke gebruiker:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Beoordeling vereist",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Zoekt een gebruikersgroep op via ID of naam.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Retourneert:** `GroupCache`-object

**Voorbeeld — Groep zoeken voor taaktoewijzing:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Goedkeuring vereist",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Intelligente waardevergelijking met typeconversie.

```python
compare_values(value1, value2)
```

**Vergelijkingslogica:**
1. `None == None` → `True`
2. `None != non-None` → `False`
3. Strings die getallen zijn → numerieke vergelijking (`"1.0" == "1.00"` → `True`)
4. Strings → hoofdletterongevoelig, spatieongevoelig (`"ABC " == " abc"` → `True`)
5. Bool vs String → stringvergelijking (`True == "true"` → `True`)
6. Decimal-vergelijking als terugval

**Voorbeeld — Controleren of bedragen overeenkomen:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Bedragen komen overeen")
```

---

## get\_lov\_values()

Haalt Lijst-van-Waarden (LOV) entries op.

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organisatie-UUID |
| `key` | `str` | LOV-sleutel |
| `return_type` | `str` | `"list_of_objects"` of `"list_of_values"` |
| `sub_org_id` | `str/None` | Optioneel sub-organisatiefilter |
| `language_code` | `str` | Taalcode (bijv. `"en"`, `"de"`) |

**Retourneert:** LOV-waarden als een lijst van objecten of als een platte lijst.

**Voorbeeld — Geconfigureerde belastingcodes ophalen:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
