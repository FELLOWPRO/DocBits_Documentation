# Pomocne funkcije

Ugradjene funkcije za obradu stringova, matematiku, operacije sa datumima, regex i tipove podataka.

**Izvor:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## Funkcije za stringove

### Konverzija tipova

```python
str(value)       # Konvertuj u string
int(value)       # Konvertuj u ceo broj
float(value)     # Konvertuj u decimalni broj
str_to_bool(s)   # "true"/"1"/"yes" -> True, sve ostalo -> False
```

### Metode stringova

```python
lower(s)              # str.lower -- "ABC" -> "abc"
upper(s)              # str.upper -- "abc" -> "ABC"
split(s, sep)         # str.split -- "a,b,c".split(",") -> ["a","b","c"]
strip(s)              # str.strip -- " abc " -> "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Dostupne su kao samostalne funkcije, ali se takodje mogu pozivati kao metode na stringovima:

```python
# Oba nacina rade:
result = upper("hello")      # -> "HELLO"
result = "hello".upper()     # -> "HELLO"
```
{% endhint %}

---

## Priblizno podudaranje stringova

### levenshtein\_distance()

Izracunava udaljenost uredjivanja izmedju dva stringa (broj potrebnih izmena).

```python
levenshtein_distance(s1, s2)
```

**Primer:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Stringovi su dovoljno slicni
    pass
```

### jaro\_winkler\_similarity()

Izracunava ocenu slicnosti izmedju 0.0 i 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Primer:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (veoma slicno, tipfeler)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (razlicito)
```

{% hint style="success" %}
**Kada koristiti koju funkciju?**
- **Levenshtein**: Dobro za kratke stringove, tacno prebrojavanje gresaka
- **Jaro-Winkler**: Bolje za imena/adrese, vise vrednuje podudaranja na pocetku
{% endhint %}

---

## Regex funkcije

Zasnovane na Python-ovom `re` modulu, ali dostupne kao samostalne funkcije.

### re\_search()

Pretrazuje prvo pojavljivanje obrasca.

```python
re_search(pattern, string)
```

**Vraca:** Match objekat ili `None`

**Primer -- Izdvajanje broja narudzbenice iz celokupnog teksta:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Zamenjuje podudaranja obrasca zamenom.

```python
re_sub(pattern, replacement, string)
```

**Primer -- Uklanjanje specijalnih karaktera iz ID-a fakture:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Pronalazi sva pojavljivanja obrasca.

```python
re_findall(pattern, string)
```

**Primer -- Pronalazenje svih brojeva narudzbenica u dokumentu:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Funkcije za datum/vreme

### datetime\_today()

Vraca danasnji datum kao `datetime` objekat.

```python
today = datetime_today()
```

### datetime\_date

Klasa `date` za kreiranje datuma.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Parsira string datuma u datetime objekat.

```python
strptime(date_string, format)
```

**Primer -- Parsiranje i koriscenje datuma fakture:**

```python
inv_date_str = get_field_value(document_data, "invoice_date", "")
try:
    date_obj = strptime(inv_date_str, "%Y-%m-%d")
    year = date_obj.year
    month = date_obj.month
except ValueError:
    pass
```

### strftime()

Formatira datetime objekat kao string.

```python
strftime(datetime_obj, format)
```

**Primer -- Postavljanje datuma obrade:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Kreira datum iz ISO kalendarske nedelje.

```python
fromisocalendar(year, week, day)
```

**Primer -- Konverzija kalendarske nedelje u datum:**

```python
# KN 12/2026, ponedeljak
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Uobicajeno kod nemackih klijenata:** Datumi isporuke se cesto navode kao "KW 12". Obrazac:

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Ponedeljak kalendarske nedelje
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Vraca dan u nedelji prvog dana i broj dana u mesecu.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Primer:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Funkcije za decimale/lokalitet

### parse\_decimal()

Parsira string u decimalni broj sa detekcijom lokaliteta.

```python
parse_decimal(value, locale="en_US")
```

**Primer:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # -> Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # -> Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Formatira decimalni broj prema lokalitetu.

```python
format_decimal_to_locale(value, locale)
```

**Primer:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # -> "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # -> "1,234.56"
```

---

## Matematicke funkcije

Kompletni `math` modul je dostupan:

| Funkcija | Opis |
| -------- | ----------- |
| `abs(x)` | Apsolutna vrednost |
| `round(x, n)` | Zaokruzivanje na n decimalnih mesta |
| `floor(x)` | Pod (zaokruzivanje nadole) |
| `ceil(x)` | Plafon (zaokruzivanje nagore) |
| `sqrt(x)` | Kvadratni koren |
| `pow(x, y)` | Stepenovanje |
| `log(x)` / `log10(x)` | Logaritam |
| `pi` | pi (3.14159...) |
| `e` | Ojlerov broj (2.71828...) |
| `sin`, `cos`, `tan` | Trigonometrija |
| `acos`, `asin`, `atan` | Inverzna trigonometrija |
| `degrees`, `radians` | Stepeni <-> Radijani |
| `exp`, `fabs`, `fmod` | Dodatne matematicke funkcije |
| `hypot`, `ldexp`, `frexp` | Specijalna izracunavanja |
| `modf` | Razdvajanje celih/decimalnih delova |

---

## Funkcije za strukture podataka

```python
dict()            # Novi recnik
list()            # Nova lista
set()             # Novi skup
tuple()           # Novi tuple
defaultdict(type) # collections.defaultdict

len(x)            # Duzina
isinstance(x, t)  # Provera tipa
type(x)           # Preuzimanje tipa
deepcopy(x)       # Duboka kopija (copy.deepcopy)

print(x)          # Debug izlaz (samo za testiranje)
```

{% hint style="warning" %}
`print()` je dostupan samo za potrebe debagovanja. Izlaz ide u log servera, ne korisniku.
{% endhint %}
