# Geschäftslogik-Funktionen

Funktionen für Lookups, PO-Matching, Aufgaben, Benutzer-/Gruppenverwaltung und Statusänderungen.

**Quelle:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Fragt Stammdaten aus Lookup-Tabellen ab (Lieferanten, Artikel, Sachkonten usw.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `org_id` | `str` | Organisations-UUID |
| `sub_org_id` | `str/None` | Sub-Organisations-UUID (oder `None`) |
| `lookup_name` | `str` | Name des Lookups (z.B. `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Filterbedingungen (siehe Formate unten) |
| `skip` | `int` | Offset für Paginierung (Standard: 0) |
| `limit` | `int` | Max. Ergebnisse (Standard: 100) |
| `match_all` | `bool` | `True` = UND, `False` = ODER (Standard: `True`) |
| `sort_order` | `list` | Sortierung (optional) |

### Filterformate

Drei Formate werden unterstützt:

```python
# Format 1: Dict mit field/operator/value
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Format 2: Tuple/Liste mit 2 Elementen (field, value) → operator = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Format 3: Tuple/Liste mit 3 Elementen (field, operator, value)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Sortierung

```python
# Format 1: Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Format 2: Tuple/Liste
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Beispiel — Lieferant nach Lieferanten-ID suchen:**

```python
# Lieferant nach Lieferanten-ID finden
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Beispiel — Sachkonten mit mehreren Filtern suchen:**

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
Intern wird `search_operator="SMART"` verwendet, das Fuzzy-Matching unterstützt.
{% endhint %}

---

## is\_supplier\_valid()

Prüft ob ein Lieferant in den Lookup-Daten existiert.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `user` | `UserAuthentication` | Das `user`-Kontextobjekt |
| `filter_data_json` | `dict` | Filter im Format `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Sub-Organisation |

**Rückgabe:** `True` wenn mindestens 1 Treffer, ansonsten `False`

**Beispiel — Lieferant validieren:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Lieferant nicht in Stammdaten gefunden")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Löst automatisches PO-Matching über den po-match-service Microservice aus.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `user` | `UserAuthentication` | Muss ein echtes Benutzerobjekt sein |
| `document_data` | `dict` | Dokumentkontext |
| `po_numbers` | `str/list` | PO-Nummern (kommagetrennt oder als Liste) |

**Rückgabe:** Aktualisierte `document_data` mit `po_items`, `po_match_status`, `po_multi_matched`

**Beispiel — Automatisches PO-Matching:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Duplikatschutz:** Bereits verifizierte PO-Nummern werden in `already_verified_po_numbers` gespeichert und nicht erneut abgeglichen.
{% endhint %}

---

## get\_next\_sequence\_number()

Holt und inkrementiert atomar eine Sequenznummer in der Datenbank.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `org_id` | `str` | Organisations-UUID |
| `sequence_name` | `str` | Muss `"sequence"` enthalten (z.B. `"invoice_sequence"`) |
| `default_value` | `int` | Startwert bei neuer Sequenz |

**Rückgabe:** `int` — die nächste Nummer, oder `None` wenn Name ungültig

**Beispiel — Interne Dokumentnummer generieren:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Namensregel:** Der `sequence_name` muss mit "sequence" beginnen oder enden, oder "SEQUENCE\_" enthalten. Andernfalls gibt die Funktion `None` zurück.
{% endhint %}

---

## create\_document\_task()

Erstellt eine Aufgabe für das aktuelle Dokument.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `user` | `UserAuthentication` | Benutzerkontext |
| `title` | `str` | Aufgabentitel |
| `description` | `str` | Beschreibung |
| `priority` | `str/int` | Priorität |
| `assigned_to_user_id` | `str/None` | Zugewiesener Benutzer |
| `assigned_to_group_id` | `str/None` | Zugewiesene Gruppe |
| `send_email` | `bool` | E-Mail-Benachrichtigung senden |

**Beispiel — Aufgabe für Rechnungen mit hohem Betrag erstellen:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="Hoher Rechnungsbetrag - Prüfung erforderlich",
        description=f"Rechnungsbetrag: {amount} überschreitet Schwellwert von 50.000",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Weist einem Dokument eine Sub-Organisation zu.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Nebeneffekte:**
- Setzt `sub_org_id` in `document_json`
- Speichert direkt in der Datenbank (wenn `doc_id` vorhanden)

**Beispiel — Zuordnung basierend auf Lieferant:**

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

Ändert den Status eines Dokuments.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `doc_id` | `str` | Dokument-UUID |
| `status` | `str` | Neuer Status (z.B. `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Statusmeldung |
| `doc_classification_class` | `str/None` | Für `CLASSIFIED`-Status: neuer Dokumenttyp |

**Beispiel — Dokument auf Fehlerstatus setzen:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Pflichtfeld fehlt: Lieferantennummer"
)
```

{% hint style="warning" %}
**Vorsicht:** Statusänderungen lösen nachgelagerte Aktionen aus (DocFlow-Workflows, Status-Change-Hooks). Nur bei Bedarf verwenden.
{% endhint %}

---

## get\_document\_content()

Gibt den vollständigen OCR-Text des Dokuments zurück.

```python
get_document_content(document_data)
```

**Rückgabe:** `str` — Zusammengefügter Text aller Seiten

**Beispiel — Volltext nach Schlüsselwörtern durchsuchen:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regex-Suche im Volltext
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
Das Ergebnis wird für 60 Sekunden zwischengespeichert (TTL-Cache mit max. 128 Einträgen).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Sucht einen Benutzer nach ID oder E-Mail.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Rückgabe:** `UsersCache`-Objekt mit Attributen wie `.email`, `.first_name`, `.last_name`, `.user_id`

**Beispiel — Aufgabe an bestimmten Benutzer zuweisen:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Prüfung erforderlich",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Sucht eine Benutzergruppe nach ID oder Name.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Rückgabe:** `GroupCache`-Objekt

**Beispiel — Gruppe für Aufgabenzuweisung finden:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Genehmigung erforderlich",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Intelligenter Wertevergleich mit Typkonvertierung.

```python
compare_values(value1, value2)
```

**Vergleichslogik:**
1. `None == None` → `True`
2. `None != non-None` → `False`
3. Strings die Zahlen sind → numerischer Vergleich (`"1.0" == "1.00"` → `True`)
4. Strings → Groß-/Kleinschreibung-unabhängig, Leerzeichen-unabhängig (`"ABC " == " abc"` → `True`)
5. Bool vs String → String-Vergleich (`True == "true"` → `True`)
6. Decimal-Vergleich als Fallback

**Beispiel — Beträge auf Übereinstimmung prüfen:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Beträge stimmen überein")
```

---

## get\_lov\_values()

Ruft List-of-Values (LOV)-Einträge ab.

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `org_id` | `str` | Organisations-UUID |
| `key` | `str` | LOV-Schlüssel |
| `return_type` | `str` | `"list_of_objects"` oder `"list_of_values"` |
| `sub_org_id` | `str/None` | Optionaler Sub-Organisations-Filter |
| `language_code` | `str` | Sprachcode (z.B. `"en"`, `"de"`) |

**Rückgabe:** LOV-Werte als Liste von Objekten oder als flache Liste.

**Beispiel — Konfigurierte Steuercodes abrufen:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
