# Funkcije polja

Funkcije za citanje, pisanje i kontrolu polja dokumenta.

**Izvor:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Cita vrednost polja iz dokumenta.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Kontekstni objekat `document_data` |
| `field_name` | `str` | Naziv polja (npr. `"invoice_id"`) |
| `default_value` | `any` | Povratna vrednost ako je polje prazno/nedostaje (podrazumevano: `None`) |
| `is_clean` | `bool` | Ako je `True`: vrednost se konvertuje u VELIKA SLOVA sa uklonjenim razmacima |

**Vraca:** Vrednost polja kao string, ili `default_value`

**Primer -- Citanje broja fakture sa rezervnom vrednoscu:**

```python
# Citanje polja sa podrazumevanom vrednoscu
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# Sa is_clean=True: "INV 001" postaje "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**Sta se desava:** Vraca vrednost polja. Kada je `is_clean=True`, vrednost se transformise putem `value.upper().replace(" ", "").strip()` -- korisno za poredjenja.

---

## set\_field\_value()

Postavlja vrednost polja. Automatski kreira polje ako ne postoji.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Kontekstni objekat `document_data` |
| `field_name` | `str` | Naziv polja |
| `value` | `any` | Nova vrednost |
| `remove_link` | `bool` | Ako je `True`: uklanja koordinate, pouzdanost, pravilo itd. |

**Vraca:** `True` ako je vrednost promenjena, `False` ako je identicna

**Sporedni efekti:**
- Postavlja `highlight_field = True` (vizuelni indikator u korisnickom interfejsu)
- Postavlja `extraction_method = "SCRIPT"`
- Postavlja `formatted_value = value`

**Primer -- Uslovno dodeljivanje vrednosti:**

```python
# Postavljanje ID-a fakture
set_field_value(document_data, "invoice_id", "INV-2026-001")

# Sa remove_link: uklanja OCR vezu (koordinate, pouzdanost itd.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**Sta se desava:** Vrednost polja se azurira i oznacava kao izmenjena skriptom. Ako polje ne postoji, automatski se kreira sa `extraction_method: "SCRIPT"` i dodaje u `fields` i `fields_dict`.

---

## set\_date\_value()

Postavlja vrednost datuma sa automatskim formatiranjem i opcionom aritmetikom datuma.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `value` | `str` | ISO datum: `"2026-03-25"`. Ako je prazno: danasnji datum |
| `add_days` | `int` | Dani za dodavanje (npr. `30` za uslove placanja) |
| `skip_weekend` | `bool` | Preskoci vikende pri dodavanju dana |
| `exclude_final_days` | `str/list` | Dodatni dani za iskljucivanje (npr. `"MONDAY,FRIDAY"`) |

**Primer -- Obracun datuma dospeca placanja (30 dana, bez vikenda):**

```python
# Datum dospeca: 30 dana posle datuma fakture, preskoci vikende
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Postavljanje datuma isporuke na danas
set_date_value(document_data, "delivery_date", None)  # None = danas

# 14 dana, iskljucujuci subotu i ponedeljak
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**Sta se desava:** Datum se izracunava dodavanjem dana (opciono preskacuci vikende/odredjene dane) i automatski se formatira prema obrascu `date_format_pattern` dokumenta (npr. `%d.%m.%Y` za Nemacku).

**Kodovi dana za `exclude_final_days`:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Postavlja vrednost iznosa sa automatskim formatiranjem prema lokalitetu.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `value` | `str/number` | Iznos u engleskom formatu (npr. `"1234.56"`) |

**Primer -- Postavljanje neto iznosa:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value postaje npr. "1.234,56" za de_DE lokalitet
```

**Sta se desava:** Iznos se formatira prema `amount_format_locale` iz `document_json` (npr. `de_DE`, `en_US`).

---

## create\_new\_field()

Kreira novi recnik polja (bez dodavanja u dokument).

```python
create_new_field(field_name, value="")
```

**Vraca:** Recnik sa `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Primer:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Jednostavnija alternativa:** Koristite `set_field_value()` umesto toga -- automatski kreira polje ako ne postoji. `create_new_field()` je potreban samo kada zelite rucno da manipulisete recnikom polja.
{% endhint %}

---

## delete\_field()

Uklanja polje iz dokumenta.

```python
delete_field(document_data, field_name)
```

**Vraca:** Tuple `(doc_json, fields_dict)` nakon brisanja

**Primer:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Oznacava polje kao nevazece sa porukom o gresci.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `message` | `str` | Poruka o gresci (prikazuje se u korisnickom interfejsu) |
| `code` | `str` | Kod greske (podrazumevano: `INVALID_VALUE`) |

**Sporedni efekti:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Primer -- IBAN validacija:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN must be at least 15 characters",
                         "IBAN_TOO_SHORT")
```

**Sta se desava:** Polje se oznacava crvenom bojom na ekranu za validaciju sa porukom o gresci prikazanom korisniku.

---

## set\_field\_as\_valid()

Uklanja status nevazeceg sa polja.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Primer:**

```python
set_field_as_valid(document_data, "iban", "IBAN valid")
```

**Sta se desava:** Uklanja `invalidated_by_script`, `validation_message`, `validation_code` i postavlja `is_valid = True`.

---

## set\_field\_attribute()

Postavlja proizvoljan atribut na polje.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Primer:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Pogledajte kompletnu listu [Podrzanih atributa](#supported-attributes) u nastavku.

---

## set\_is\_required()

Postavlja polje kao obavezno ili uklanja zahtev.

```python
set_is_required(document_data, field_name, value)
```

**Primer -- Broj narudzbenice obavezan za nabavne fakture:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Postavlja polje kao samo za citanje ili za uredjivanje.

```python
set_is_readonly(document_data, field_name, value)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = samo za citanje, `False` = za uredjivanje, `None` = ukloni atribut |

**Primer:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Skriva ili prikazuje polje u korisnickom interfejsu.

```python
set_is_hidden(document_data, field_name, value)
```

**Primer -- Prikazivanje polja podorganizacije samo kada je relevantno:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Forsira rucnu validaciju za polje.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = forsira validaciju, `False` = ukloni |
| `reset_validation` | `bool` | Ako je `True`: resetuje `is_validated` nazad na `False` |

**Sporedni efekti kada je `value=True`:**
- `force_validation = True`
- `is_valid = False` (ako jos nije validirano)
- `validation_code = "FORCED_VALIDATION"`

**Primer -- Forsiranje validacije za visoke iznose:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Podrzani atributi

### Osnovni atributi polja

| Atribut | Tip | Opis |
| --------- | ---- | ----------- |
| `value` | any | Sirova vrednost polja |
| `formatted_value` | string | Formatirana vrednost za prikaz |
| `content` | string | Originalni ekstraktovani sadrzaj |
| `is_required` | bool | Da li je polje obavezno |
| `is_valid` | bool | Status validacije |
| `is_validated` | bool | Da li je polje validirao korisnik |
| `is_readonly` | bool | Da li je polje samo za citanje |
| `is_hidden` | bool | Da li je polje skriveno u korisnickom interfejsu |
| `force_validation` | bool | Forsira korisnika da validira ovo polje |
| `highlight_field` | bool | Istice polje u korisnickom interfejsu |
| `extraction_method` | string | Kako je vrednost ekstraktovana (npr. `"SCRIPT"`) |

### Atributi validacije

| Atribut | Tip | Opis |
| --------- | ---- | ----------- |
| `validation_message` | string | Poruka o gresci prikazana korisniku |
| `validation_code` | string | Kod greske (npr. `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Oznacava polje kao invalidirano skriptom |

### Atributi ekstrakcije/OCR

| Atribut | Tip | Opis |
| --------- | ---- | ----------- |
| `coords` | object | Koordinate okvira na dokumentu |
| `confidence` | float | OCR/ekstrakcija ocena pouzdanosti |
| `score` | float | Ocena podudaranja/validacije |
| `score_description` | string | Opis ocene |
| `page` | int | Broj stranice na kojoj je polje pronadjeno |
| `rule` | string | Pravilo ekstrakcije koje je primenjeno |
