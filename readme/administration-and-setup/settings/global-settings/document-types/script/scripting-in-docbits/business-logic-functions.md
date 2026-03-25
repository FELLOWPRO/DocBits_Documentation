# Funkcje Logiki Biznesowej

Funkcje do wyszukiwan, dopasowywania ZZ, zadan, zarzadzania uzytkownikami/grupami i zmian statusow.

**Zrodlo:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Odpytuje dane podstawowe z tabel wyszukiwania (dostawcy, pozycje, konta KG itp.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID organizacji |
| `sub_org_id` | `str/None` | UUID podorganizacji (lub `None`) |
| `lookup_name` | `str` | Nazwa wyszukiwania (np. `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Warunki filtrowania (zobacz formaty ponizej) |
| `skip` | `int` | Offset dla paginacji (domyslnie: 0) |
| `limit` | `int` | Maks. wynikow (domyslnie: 100) |
| `match_all` | `bool` | `True` = AND, `False` = OR (domyslnie: `True`) |
| `sort_order` | `list` | Sortowanie (opcjonalne) |

### Formaty filtrow

Obslugiwane sa trzy formaty:

```python
# Format 1: Slownik z field/operator/value
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Format 2: Krotka/Lista z 2 elementami (field, value) -> operator = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Format 3: Krotka/Lista z 3 elementami (field, operator, value)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Sortowanie

```python
# Format 1: Slownik
sort_order = [{"field": "NAME", "direction": "asc"}]

# Format 2: Krotka/Lista
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Przyklad — Wyszukiwanie dostawcy po ID dostawcy:**

```python
# Znajdz dostawce po ID dostawcy
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Przyklad — Wyszukiwanie kont KG z wieloma filtrami:**

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
Wewnetrznie uzywa `search_operator="SMART"`, ktory obsluguje dopasowywanie rozmyte.
{% endhint %}

---

## is\_supplier\_valid()

Sprawdza, czy dostawca istnieje w danych wyszukiwania.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Obiekt kontekstowy `user` |
| `filter_data_json` | `dict` | Filtr w formacie `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Podorganizacja |

**Zwraca:** `True` jesli co najmniej 1 dopasowanie, w przeciwnym razie `False`

**Przyklad — Walidacja dostawcy:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Dostawca nie znaleziony w danych podstawowych")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Uruchamia automatyczne dopasowywanie ZZ przez mikroserwis po-match-service.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Musi byc prawdziwym obiektem uzytkownika |
| `document_data` | `dict` | Kontekst dokumentu |
| `po_numbers` | `str/list` | Numery ZZ (oddzielone przecinkami lub lista) |

**Zwraca:** Zaktualizowane `document_data` z `po_items`, `po_match_status`, `po_multi_matched`

**Przyklad — Automatyczne dopasowanie ZZ:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Ochrona przed duplikatami:** Juz zweryfikowane numery ZZ sa przechowywane w `already_verified_po_numbers` i nie beda ponownie dopasowywane.
{% endhint %}

---

## get\_next\_sequence\_number()

Pobiera i atomowo inkrementuje numer sekwencji w bazie danych.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID organizacji |
| `sequence_name` | `str` | Musi zawierac `"sequence"` (np. `"invoice_sequence"`) |
| `default_value` | `int` | Wartosc poczatkowa gdy sekwencja jest nowo tworzona |

**Zwraca:** `int` — nastepny numer lub `None` jesli nazwa jest nieprawidlowa

**Przyklad — Generowanie wewnetrznego numeru dokumentu:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Regula nazewnictwa:** `sequence_name` musi zaczynac sie lub konczyc na "sequence" lub zawierac "SEQUENCE\_". W przeciwnym razie funkcja zwraca `None`.
{% endhint %}

---

## create\_document\_task()

Tworzy zadanie dla biezacego dokumentu.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Kontekst uzytkownika |
| `title` | `str` | Tytul zadania |
| `description` | `str` | Opis |
| `priority` | `str/int` | Priorytet |
| `assigned_to_user_id` | `str/None` | Przypisany uzytkownik |
| `assigned_to_group_id` | `str/None` | Przypisana grupa |
| `send_email` | `bool` | Wyslij powiadomienie e-mail |

**Przyklad — Tworzenie zadania dla faktur o wysokiej kwocie:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="Wysoka kwota faktury - wymagany przeglad",
        description=f"Kwota faktury: {amount} przekracza prog 50 000",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Przypisuje podorganizacje do dokumentu.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Efekty uboczne:**
- Ustawia `sub_org_id` w `document_json`
- Zapisuje bezposrednio do bazy danych (jesli `doc_id` jest obecne)

**Przyklad — Kierowanie na podstawie dostawcy:**

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

Zmienia status dokumentu.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `doc_id` | `str` | UUID dokumentu |
| `status` | `str` | Nowy status (np. `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Wiadomosc statusu |
| `doc_classification_class` | `str/None` | Dla statusu `CLASSIFIED`: nowy typ dokumentu |

**Przyklad — Ustawienie dokumentu na status bledu:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Brakujace wymagane pole: numer dostawcy"
)
```

{% hint style="warning" %}
**Uwaga:** Zmiany statusu wyzwalaja dalsze akcje (przeplywy DocFlow, hooki zmian statusu). Uzywaj tylko w razie potrzeby.
{% endhint %}

---

## get\_document\_content()

Zwraca pelny tekst OCR dokumentu.

```python
get_document_content(document_data)
```

**Zwraca:** `str` — Polaczony tekst wszystkich stron

**Przyklad — Wyszukiwanie pelnotekstowe slow kluczowych:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Wyszukiwanie regex w pelnym tekscie
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
Wynik jest buforowany przez 60 sekund (pamiec podreczna TTL z maks. 128 wpisami).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Wyszukuje uzytkownika po ID lub adresie e-mail.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Zwraca:** Obiekt `UsersCache` z atrybutami takimi jak `.email`, `.first_name`, `.last_name`, `.user_id`

**Przyklad — Przypisanie zadania do konkretnego uzytkownika:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Wymagany przeglad",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Wyszukuje grupe uzytkownikow po ID lub nazwie.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Zwraca:** Obiekt `GroupCache`

**Przyklad — Wyszukiwanie grupy do przypisania zadania:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Wymagane zatwierdzenie",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Inteligentne porownywanie wartosci z konwersja typow.

```python
compare_values(value1, value2)
```

**Logika porownywania:**
1. `None == None` -> `True`
2. `None != non-None` -> `False`
3. Ciagi znakow bedace liczbami -> porownanie numeryczne (`"1.0" == "1.00"` -> `True`)
4. Ciagi znakow -> bez rozrozniania wielkosci liter, bez rozrozniania spacji (`"ABC " == " abc"` -> `True`)
5. Bool vs String -> porownanie ciagu znakow (`True == "true"` -> `True`)
6. Porownanie Decimal jako awaryjne

**Przyklad — Weryfikacja zgodnosci kwot:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Kwoty sie zgadzaja")
```

---

## get\_lov\_values()

Pobiera wpisy z Listy Wartosci (LOV).

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID organizacji |
| `key` | `str` | Klucz LOV |
| `return_type` | `str` | `"list_of_objects"` lub `"list_of_values"` |
| `sub_org_id` | `str/None` | Opcjonalny filtr podorganizacji |
| `language_code` | `str` | Kod jezyka (np. `"en"`, `"de"`) |

**Zwraca:** Wartosci LOV jako lista obiektow lub jako plaska lista.

**Przyklad — Pobieranie skonfigurowanych kodow podatkowych:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
