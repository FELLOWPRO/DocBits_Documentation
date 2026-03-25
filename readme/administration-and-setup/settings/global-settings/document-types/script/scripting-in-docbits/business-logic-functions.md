# Funkcije poslovne logike

Funkcije za pretrazivanje, uparivanje narudzbenica, zadatke, upravljanje korisnicima/grupama i promene statusa.

**Izvor:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Pretrazuje maticne podatke iz lookup tabela (dobavljaci, artikli, konta glavne knjige itd.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID organizacije |
| `sub_org_id` | `str/None` | UUID podorganizacije (ili `None`) |
| `lookup_name` | `str` | Naziv lookup-a (npr. `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Uslovi filtriranja (pogledajte formate u nastavku) |
| `skip` | `int` | Pomeraj za paginaciju (podrazumevano: 0) |
| `limit` | `int` | Maks. rezultata (podrazumevano: 100) |
| `match_all` | `bool` | `True` = AND, `False` = OR (podrazumevano: `True`) |
| `sort_order` | `list` | Sortiranje (opciono) |

### Formati filtera

Podrzana su tri formata:

```python
# Format 1: Recnik sa poljem/operatorom/vrednoscu
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Format 2: Tuple/Lista sa 2 elementa (polje, vrednost) -> operator = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Format 3: Tuple/Lista sa 3 elementa (polje, operator, vrednost)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Sortiranje

```python
# Format 1: Recnik
sort_order = [{"field": "NAME", "direction": "asc"}]

# Format 2: Tuple/Lista
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Primer -- Pretrazivanje dobavljaca po ID-u dobavljaca:**

```python
# Pronadjite dobavljaca po ID-u dobavljaca
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Primer -- Pretraga konta glavne knjige sa vise filtera:**

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
Interno koristi `search_operator="SMART"` koji podrzava priblizno podudaranje.
{% endhint %}

---

## is\_supplier\_valid()

Proverava da li dobavljac postoji u lookup podacima.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Kontekstni objekat `user` |
| `filter_data_json` | `dict` | Filter u formatu `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Podorganizacija |

**Vraca:** `True` ako postoji bar 1 podudaranje, u suprotnom `False`

**Primer -- Validacija dobavljaca:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Supplier not found in master data")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Pokrece automatsko uparivanje narudzbenica putem po-match-service mikroservisa.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Mora biti pravi korisnicki objekat |
| `document_data` | `dict` | Kontekst dokumenta |
| `po_numbers` | `str/list` | Brojevi narudzbenica (razdvojeni zarezom ili lista) |

**Vraca:** Azuriran `document_data` sa `po_items`, `po_match_status`, `po_multi_matched`

**Primer -- Automatsko uparivanje narudzbenice:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Zastita od duplikata:** Vec verifikovani brojevi narudzbenica se cuvaju u `already_verified_po_numbers` i nece biti ponovo uparivani.
{% endhint %}

---

## get\_next\_sequence\_number()

Preuzima i atomski uvecava redni broj u bazi podataka.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID organizacije |
| `sequence_name` | `str` | Mora sadrzavati `"sequence"` (npr. `"invoice_sequence"`) |
| `default_value` | `int` | Pocetna vrednost kada se sekvenca tek kreira |

**Vraca:** `int` -- sledeci broj, ili `None` ako je naziv nevazeci

**Primer -- Generisanje internog broja dokumenta:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Pravilo imenovanja:** `sequence_name` mora poceti ili zavrsiti sa "sequence", ili sadrzati "SEQUENCE\_". U suprotnom, funkcija vraca `None`.
{% endhint %}

---

## create\_document\_task()

Kreira zadatak za trenutni dokument.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Korisnicki kontekst |
| `title` | `str` | Naslov zadatka |
| `description` | `str` | Opis |
| `priority` | `str/int` | Prioritet |
| `assigned_to_user_id` | `str/None` | Dodeljeni korisnik |
| `assigned_to_group_id` | `str/None` | Dodeljena grupa |
| `send_email` | `bool` | Slanje obavestenja putem e-poste |

**Primer -- Kreiranje zadatka za fakture visokog iznosa:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="High invoice amount - review required",
        description=f"Invoice amount: {amount} exceeds 50,000 threshold",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Dodeljuje podorganizaciju dokumentu.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Sporedni efekti:**
- Postavlja `sub_org_id` u `document_json`
- Cuva direktno u bazu podataka (ako je `doc_id` prisutan)

**Primer -- Rutiranje na osnovu dobavljaca:**

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

Menja status dokumenta.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `doc_id` | `str` | UUID dokumenta |
| `status` | `str` | Novi status (npr. `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Poruka o statusu |
| `doc_classification_class` | `str/None` | Za `CLASSIFIED` status: novi tip dokumenta |

**Primer -- Postavljanje dokumenta u status greske:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Required field missing: supplier number"
)
```

{% hint style="warning" %}
**Oprez:** Promene statusa pokrecu akcije nizvodno (DocFlow tokovi rada, kuke za promenu statusa). Koristite samo kada je neophodno.
{% endhint %}

---

## get\_document\_content()

Vraca kompletni OCR tekst dokumenta.

```python
get_document_content(document_data)
```

**Vraca:** `str` -- Spojeni tekst svih stranica

**Primer -- Pretraga celokupnog teksta za kljucne reci:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regex pretraga u celokupnom tekstu
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
Rezultat se kesira na 60 sekundi (TTL kes sa maks. 128 unosa).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Pretrazuje korisnika po ID-u ili e-posti.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Vraca:** `UsersCache` objekat sa atributima kao sto su `.email`, `.first_name`, `.last_name`, `.user_id`

**Primer -- Dodeljivanje zadatka odredjenom korisniku:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Review required",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Pretrazuje korisnicku grupu po ID-u ili nazivu.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Vraca:** `GroupCache` objekat

**Primer -- Pronalazenje grupe za dodeljivanje zadatka:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Approval needed",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Inteligentno poredjenje vrednosti sa konverzijom tipova.

```python
compare_values(value1, value2)
```

**Logika poredjenja:**
1. `None == None` -> `True`
2. `None != non-None` -> `False`
3. Stringovi koji su brojevi -> numericko poredjenje (`"1.0" == "1.00"` -> `True`)
4. Stringovi -> bez razlikovanja velikih/malih slova, bez razlikovanja razmaka (`"ABC " == " abc"` -> `True`)
5. Bool naspram String -> poredjenje stringova (`True == "true"` -> `True`)
6. Decimalno poredjenje kao rezerva

**Primer -- Verifikacija da li se iznosi podudaraju:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Amounts match")
```

---

## get\_lov\_values()

Preuzima unose iz Liste vrednosti (LOV).

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID organizacije |
| `key` | `str` | LOV kljuc |
| `return_type` | `str` | `"list_of_objects"` ili `"list_of_values"` |
| `sub_org_id` | `str/None` | Opcioni filter podorganizacije |
| `language_code` | `str` | Jezicki kod (npr. `"en"`, `"de"`) |

**Vraca:** LOV vrednosti kao listu objekata ili kao ravnu listu.

**Primer -- Preuzimanje konfigurisanih poreskih kodova:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
