# Funkcje Pol

Funkcje do odczytu, zapisu i kontroli pol dokumentu.

**Zrodlo:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Odczytuje wartosc pola z dokumentu.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Obiekt kontekstowy `document_data` |
| `field_name` | `str` | Nazwa pola (np. `"invoice_id"`) |
| `default_value` | `any` | Wartosc zwracana jesli pole jest puste/nie istnieje (domyslnie: `None`) |
| `is_clean` | `bool` | Jesli `True`: wartosc jest konwertowana na WIELKIE LITERY z usunietymi spacjami |

**Zwraca:** Wartosc pola jako string lub `default_value`

**Przyklad — Odczyt numeru faktury z wartoscia domyslna:**

```python
# Odczyt pola z wartoscia domyslna
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# Z is_clean=True: "INV 001" staje sie "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**Co sie dzieje:** Zwraca wartosc pola. Gdy `is_clean=True`, wartosc jest transformowana przez `value.upper().replace(" ", "").strip()` — przydatne do porownan.

---

## set\_field\_value()

Ustawia wartosc pola. Automatycznie tworzy pole, jesli nie istnieje.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Obiekt kontekstowy `document_data` |
| `field_name` | `str` | Nazwa pola |
| `value` | `any` | Nowa wartosc |
| `remove_link` | `bool` | Jesli `True`: usuwa wspolrzedne, pewnosc, regule itp. |

**Zwraca:** `True` jesli wartosc sie zmienila, `False` jesli identyczna

**Efekty uboczne:**
- Ustawia `highlight_field = True` (wskaznik wizualny w UI)
- Ustawia `extraction_method = "SCRIPT"`
- Ustawia `formatted_value = value`

**Przyklad — Warunkowe przypisanie wartosci:**

```python
# Ustaw ID faktury
set_field_value(document_data, "invoice_id", "INV-2026-001")

# Z remove_link: usuwa powiazanie OCR (wspolrzedne, pewnosc itp.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**Co sie dzieje:** Wartosc pola jest aktualizowana i oznaczana jako zmodyfikowana przez skrypt. Jesli pole nie istnieje, jest automatycznie tworzone z `extraction_method: "SCRIPT"` i dodawane zarowno do `fields`, jak i `fields_dict`.

---

## set\_date\_value()

Ustawia wartosc daty z automatycznym formatowaniem i opcjonalna arytmetyka dat.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `value` | `str` | Data ISO: `"2026-03-25"`. Jesli puste: dzisiejsza data |
| `add_days` | `int` | Dni do dodania (np. `30` dla warunkow platnosci) |
| `skip_weekend` | `bool` | Pomijanie weekendow przy dodawaniu dni |
| `exclude_final_days` | `str/list` | Dodatkowe dni do wykluczenia (np. `"MONDAY,FRIDAY"`) |

**Przyklad — Obliczanie terminu platnosci (30 dni, bez weekendow):**

```python
# Termin platnosci: 30 dni po dacie faktury, pomijanie weekendow
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Ustaw date dostawy na dzisiaj
set_date_value(document_data, "delivery_date", None)  # None = dzisiaj

# 14 dni, z wylaczeniem soboty i poniedzialku
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**Co sie dzieje:** Data jest obliczana przez dodanie dni (opcjonalnie z pomijaniem weekendow/okreslonych dni) i automatycznie formatowana zgodnie z `date_format_pattern` dokumentu (np. `%d.%m.%Y` dla Niemiec).

**Kody dni dla `exclude_final_days`:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Ustawia wartosc kwoty z automatycznym formatowaniem regionalnym.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `value` | `str/number` | Kwota w formacie angielskim (np. `"1234.56"`) |

**Przyklad — Ustaw kwote netto:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value staje sie np. "1.234,56" dla lokalizacji de_DE
```

**Co sie dzieje:** Kwota jest formatowana zgodnie z `amount_format_locale` z `document_json` (np. `de_DE`, `en_US`).

---

## create\_new\_field()

Tworzy nowy slownik pola (bez dodawania go do dokumentu).

```python
create_new_field(field_name, value="")
```

**Zwraca:** Slownik z `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Przyklad:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Prostsza alternatywa:** Uzyj `set_field_value()` zamiast tego — automatycznie tworzy pole, jesli nie istnieje. `create_new_field()` jest potrzebne tylko wtedy, gdy chcesz recznie manipulowac slownikiem pola.
{% endhint %}

---

## delete\_field()

Usuwa pole z dokumentu.

```python
delete_field(document_data, field_name)
```

**Zwraca:** Krotke `(doc_json, fields_dict)` po usunieciu

**Przyklad:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Oznacza pole jako nieprawidlowe z komunikatem bledu.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `message` | `str` | Komunikat bledu (wyswietlany w UI) |
| `code` | `str` | Kod bledu (domyslnie: `INVALID_VALUE`) |

**Efekty uboczne:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Przyklad — Walidacja IBAN:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN musi miec co najmniej 15 znakow",
                         "IBAN_TOO_SHORT")
```

**Co sie dzieje:** Pole jest podswietlone na czerwono na ekranie walidacji z komunikatem bledu wyswietlanym uzytkownikowi.

---

## set\_field\_as\_valid()

Usuwa status nieprawidlowosci z pola.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Przyklad:**

```python
set_field_as_valid(document_data, "iban", "IBAN prawidlowy")
```

**Co sie dzieje:** Usuwa `invalidated_by_script`, `validation_message`, `validation_code` i ustawia `is_valid = True`.

---

## set\_field\_attribute()

Ustawia dowolny atrybut pola.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Przyklad:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Zobacz pelna liste [Obslugiwanych atrybutow](#supported-attributes) ponizej.

---

## set\_is\_required()

Ustawia pole jako obowiazkowe lub usuwa wymaganie.

```python
set_is_required(document_data, field_name, value)
```

**Przyklad — Numer ZZ wymagany dla faktur zakupowych:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Ustawia pole jako tylko do odczytu lub edytowalne.

```python
set_is_readonly(document_data, field_name, value)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = tylko do odczytu, `False` = edytowalne, `None` = usun atrybut |

**Przyklad:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Ukrywa lub pokazuje pole w UI.

```python
set_is_hidden(document_data, field_name, value)
```

**Przyklad — Pokazuj pola podorganizacji tylko gdy sa istotne:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Wymusza reczna walidacje pola.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = wymus walidacje, `False` = usun |
| `reset_validation` | `bool` | Jesli `True`: resetuje `is_validated` z powrotem na `False` |

**Efekty uboczne gdy `value=True`:**
- `force_validation = True`
- `is_valid = False` (jesli jeszcze nie zwalidowane)
- `validation_code = "FORCED_VALIDATION"`

**Przyklad — Wymuszenie walidacji dla wysokich kwot:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Obslugiwane atrybuty

### Podstawowe atrybuty pol

| Atrybut | Typ | Opis |
| --------- | ---- | ----------- |
| `value` | any | Surowa wartosc pola |
| `formatted_value` | string | Wartosc sformatowana do wyswietlania |
| `content` | string | Oryginalna wyodrebniona zawartosc |
| `is_required` | bool | Czy pole jest obowiazkowe |
| `is_valid` | bool | Status walidacji |
| `is_validated` | bool | Czy pole zostalo zwalidowane przez uzytkownika |
| `is_readonly` | bool | Czy pole jest tylko do odczytu |
| `is_hidden` | bool | Czy pole jest ukryte w UI |
| `force_validation` | bool | Wymuszenie walidacji pola przez uzytkownika |
| `highlight_field` | bool | Podswietlenie pola w UI |
| `extraction_method` | string | Sposob ekstrakcji wartosci (np. `"SCRIPT"`) |

### Atrybuty walidacji

| Atrybut | Typ | Opis |
| --------- | ---- | ----------- |
| `validation_message` | string | Komunikat bledu wyswietlany uzytkownikowi |
| `validation_code` | string | Kod bledu (np. `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Oznacza pole jako uniewaznione przez skrypt |

### Atrybuty ekstrakcji/OCR

| Atrybut | Typ | Opis |
| --------- | ---- | ----------- |
| `coords` | object | Wspolrzedne ramki ograniczajacej w dokumencie |
| `confidence` | float | Wynik pewnosci OCR/ekstrakcji |
| `score` | float | Wynik dopasowania/walidacji |
| `score_description` | string | Opis wyniku |
| `page` | int | Numer strony, na ktorej znaleziono pole |
| `rule` | string | Zastosowana regula ekstrakcji |
