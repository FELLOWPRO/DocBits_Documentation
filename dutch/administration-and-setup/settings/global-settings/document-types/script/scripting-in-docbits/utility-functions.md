# Hulpfuncties

Ingebouwde functies voor stringverwerking, wiskunde, datumbewerkingen, regex en datatypes.

**Source:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## Stringfuncties

### Typeconversie

```python
str(value)       # Converteren naar string
int(value)       # Converteren naar geheel getal
float(value)     # Converteren naar decimaal getal
str_to_bool(s)   # "true"/"1"/"yes" → True, al het andere → False
```

### Stringmethoden

```python
lower(s)              # str.lower — "ABC" → "abc"
upper(s)              # str.upper — "abc" → "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") → ["a","b","c"]
strip(s)              # str.strip — " abc " → "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Deze zijn beschikbaar als zelfstandige functies maar kunnen ook als methoden op strings worden aangeroepen:

```python
# Beide werken:
result = upper("hello")      # → "HELLO"
result = "hello".upper()     # → "HELLO"
```
{% endhint %}

---

## Fuzzy Stringvergelijking

### levenshtein\_distance()

Berekent de bewerkingsafstand tussen twee strings (aantal benodigde wijzigingen).

```python
levenshtein_distance(s1, s2)
```

**Voorbeeld:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Strings zijn voldoende vergelijkbaar
    pass
```

### jaro\_winkler\_similarity()

Berekent een gelijkenisscore tussen 0.0 en 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Voorbeeld:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (zeer vergelijkbaar, typefout)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (ongelijk)
```

{% hint style="success" %}
**Wanneer welke gebruiken?**
- **Levenshtein**: Goed voor korte strings, exact aantal fouten
- **Jaro-Winkler**: Beter voor namen/adressen, weegt overeenkomsten aan het begin zwaarder
{% endhint %}

---

## Regex-functies

Gebaseerd op Python's `re`-module, maar beschikbaar als zelfstandige functies.

### re\_search()

Zoekt naar de eerste overeenkomst van een patroon.

```python
re_search(pattern, string)
```

**Retourneert:** Match-object of `None`

**Voorbeeld — Ordernummer extraheren uit volledige tekst:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Vervangt patroonovereenkomsten met een vervangende string.

```python
re_sub(pattern, replacement, string)
```

**Voorbeeld — Speciale tekens verwijderen uit factuurnummer:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Vindt alle overeenkomsten van een patroon.

```python
re_findall(pattern, string)
```

**Voorbeeld — Alle PO-nummers in document vinden:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Datum-/tijdfuncties

### datetime\_today()

Retourneert de datum van vandaag als een `datetime`-object.

```python
today = datetime_today()
```

### datetime\_date

De `date`-klasse voor het aanmaken van datums.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Parseert een datumstring naar een datetime-object.

```python
strptime(date_string, format)
```

**Voorbeeld — Factuurdatum parsen en gebruiken:**

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

Maakt een datetime-object op als string.

```python
strftime(datetime_obj, format)
```

**Voorbeeld — Verwerkingsdatum instellen:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Maakt een datum aan op basis van ISO-kalenderweek.

```python
fromisocalendar(year, week, day)
```

**Voorbeeld — Kalenderweek omzetten naar datum:**

```python
# KW 12/2026, maandag
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Veelvoorkomend bij Duitse klanten:** Leverdata worden vaak opgegeven als "KW 12". Patroon:

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Maandag van de KW
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Retourneert de weekdag van de 1e en het aantal dagen in een maand.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Voorbeeld:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Decimaal-/localefuncties

### parse\_decimal()

Parseert een string naar een decimaal getal met localedetectie.

```python
parse_decimal(value, locale="en_US")
```

**Voorbeeld:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # → Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # → Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Maakt een decimaal getal op volgens locale.

```python
format_decimal_to_locale(value, locale)
```

**Voorbeeld:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # → "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # → "1,234.56"
```

---

## Wiskundefuncties

De volledige `math`-module is beschikbaar:

| Functie | Beschrijving |
| -------- | ----------- |
| `abs(x)` | Absolute waarde |
| `round(x, n)` | Afronden op n decimalen |
| `floor(x)` | Naar beneden afronden |
| `ceil(x)` | Naar boven afronden |
| `sqrt(x)` | Vierkantswortel |
| `pow(x, y)` | Machtsverheffing |
| `log(x)` / `log10(x)` | Logaritme |
| `pi` | π (3,14159...) |
| `e` | Getal van Euler (2,71828...) |
| `sin`, `cos`, `tan` | Goniometrie |
| `acos`, `asin`, `atan` | Inverse goniometrie |
| `degrees`, `radians` | Graden ↔ Radialen |
| `exp`, `fabs`, `fmod` | Extra wiskundefuncties |
| `hypot`, `ldexp`, `frexp` | Speciale berekeningen |
| `modf` | Geheel/decimaal scheiden |

---

## Datastructuurfuncties

```python
dict()            # Nieuw woordenboek
list()            # Nieuwe lijst
set()             # Nieuwe verzameling
tuple()           # Nieuwe tuple
defaultdict(type) # collections.defaultdict

len(x)            # Lengte
isinstance(x, t)  # Typecontrole
type(x)           # Type ophalen
deepcopy(x)       # Diepe kopie (copy.deepcopy)

print(x)          # Debug-uitvoer (alleen voor testen)
```

{% hint style="warning" %}
`print()` is alleen beschikbaar voor debugdoeleinden. Uitvoer gaat naar het serverlog, niet naar de gebruiker.
{% endhint %}
